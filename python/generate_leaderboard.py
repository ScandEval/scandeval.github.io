"""Python script to generate ScandEval leaderboards."""

from collections import defaultdict
from pathlib import Path
import json
import logging
from datetime import datetime
import time
from typing import Any
import click
import re
import scipy.stats as stats
import os
import pandas as pd
import numpy as np
from datawrapper import Datawrapper
from dotenv import load_dotenv


load_dotenv()


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)


# Variable determining whether all models that haven't been fully benchmarked should be
# logged along with the datasets they are missing
LOG_MISSING = bool(os.getenv("LOG_MISSING", None))


# Number of attempts to publish the chart to Datawrapper
NUM_EMBED_ATTEMPTS = 3


@click.command()
@click.argument("title", type=str)
@click.option(
    "--language_mapping",
    "-l",
    required=True,
    type=(str, str),
    multiple=True,
    help="A dict mapping language codes to language names.",
)
@click.option(
    "--task_mapping",
    "-t",
    required=True,
    type=(str, str),
    multiple=True,
    help="A dict mapping task codes to task names.",
)
@click.option(
    "--metric_mapping",
    "-m",
    required=True,
    type=(str, str),
    multiple=True,
    help="A dict mapping metric codes to metric names.",
)
@click.option(
    "--datasets",
    "-d",
    required=True,
    type=(str, str, str, str, str),
    multiple=True,
    help="A list of (dataset_name, language_code, task_code, primary_metric_code, "
    "secondary_metric_code) tuples. These are the datasets that will be included in "
    "the leaderboard.",
)
def generate_leaderboard(
    title: str,
    language_mapping: dict[str | None, str],
    task_mapping: dict[str, str],
    metric_mapping: dict[str, str],
    datasets: list[tuple[str, str | None, str, str, str]],
) -> None:
    """Generate a ScandEval leaderboard and store it to disk.

    Args:
        title:
            The title of the leaderboard.
        language_mapping:
            A dict mapping language codes to language names.
        task_mapping:
            A dict mapping task codes to task names.
        metric_mapping:
            A dict mapping metric codes to metric names.
        datasets:
            A list of (dataset_name, language_code, task_code, primary_metric_code,
            secondary_metric_code) tuples. These are the datasets that will be included
            in the leaderboard.
    """
    language_mapping = dict(language_mapping)
    task_mapping = dict(task_mapping)
    metric_mapping = dict(metric_mapping)
    datasets = list(datasets)

    # Add speed metrics
    metric_mapping["speed"] = "Number of tokens processed per second"
    metric_mapping["speed_short"] = "Number of tokens processed in small documents per second"

    title_kebab = title.lower().replace(" ", "-") + "-test"

    BENCHMARK_HTML_START = f"""---
layout: leaderboard
title: {title}
---

<center>Last updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="{title_kebab}" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The average number of standard deviations away from the best model">Rank</span></th>
    """

    # Add language rank columns, if there are multiple languages
    if len(language_mapping) > 1:
        for language_code, language_name in language_mapping.items():
            if language_code is None:
                continue
            language_name_title = language_name.title()
            BENCHMARK_HTML_START += f"""
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The average number of standard deviations away from the best model on {language_name_title} tasks">{language_name_title} Rank</span></th>"""
        BENCHMARK_HTML_START += "\n"

    # Add dataset score columns
    for dataset_name, language_code, task_code, primary_metric_code, secondary_metric_code in datasets:
        if language_code is None:
            language_name_title = ""
        else:
            language_name_title = language_mapping[language_code].title() + " "
        task_name_lower = task_mapping[task_code].lower()
        primary_metric_name = metric_mapping[primary_metric_code]
        secondary_metric_name = metric_mapping[secondary_metric_code]
        BENCHMARK_HTML_START += f"""
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="{language_name_title}{task_name_lower} - {primary_metric_name} / {secondary_metric_name}">{dataset_name}</span></th>"""

    # Add ScandEval version at the end of the header
    for dataset_name, language_code, task_code, primary_metric_code, secondary_metric_code in datasets:
        BENCHMARK_HTML_START += f"""
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on {dataset_name}">{dataset_name} version</span></th>"""

    BENCHMARK_HTML_START += """
  </tr>
 </thead>
 <tbody>"""

    BENCHMARK_HTML_END = """ </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/{title_kebab}.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="{embed_code}">Copy embed HTML</a>
</div>
""".format(title_kebab=title_kebab, embed_code="{embed_code}")

    BENCHMARK_ENTRY = """  <tr class="{merge}">
   <td>{model_id}</td> <!-- Model ID -->
   <td class="num_model_parameters">{num_model_parameters}</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">{vocabulary_size}</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">{max_sequence_length}</td> <!-- Maximum sequence length of the model-->
   <td class="speed">{speed}</td> <!-- Model inference speed -->
   <td class="rank">{rank}</td> <!-- ScandEval rank -->"""

    # Add language rank columns, if there are multiple languages
    if len(language_mapping) > 1:
        for language_code, language_name in language_mapping.items():
            if language_code is None:
                continue
            language_code_lower = language_code.lower()
            language_name_title = language_name.title()
            BENCHMARK_ENTRY += f"""
   <td class="{language_code_lower}-rank">{{{language_code_lower}_rank}}</td> <!-- {language_name_title} rank -->"""

    # Add dataset score columns
    for dataset_name, language_code, task_code, _, _ in datasets:
        language_code_with_space = language_code.lower() + " " if language_code is not None else ""
        task_code_lower = task_code.lower()
        dataset_name_lower = dataset_name.lower().replace(" ", "_").replace("-", "_")
        BENCHMARK_ENTRY += f"""
   <td class="{language_code_with_space}{task_code_lower}">{{{dataset_name_lower}}}</td> <!-- {dataset_name} -->"""

    # Add ScandEval version at the end of the entry
    for dataset_name, _, _, _, _ in datasets:
        dataset_name_lower = dataset_name.lower().replace(" ", "_").replace("-", "_")
        BENCHMARK_ENTRY += f"""
   <td>{{{dataset_name_lower}-version}}</td> <!-- {dataset_name} version -->"""

    BENCHMARK_ENTRY += """
   </tr>"""

    # Create path to the leaderboard, and ensure that the parent directory exists
    benchmark_path = Path(f"{title_kebab}.md")
    benchmark_path.parent.mkdir(exist_ok=True, parents=True)

    # Create path to the scores JSONL file, and raise error if it doesn't exist
    scores_path = Path("scandeval_benchmark_results.jsonl")
    if not scores_path.exists():
        raise FileNotFoundError(f"Could not find {scores_path!r}")

    # Load in scores
    scores = list()
    with scores_path.open() as f:
        for line_idx, line in enumerate(f):
            if not line.strip():
                continue
            for record in line.replace("}{", "}\n{").split("\n"):
                if not record.strip():
                    continue
                try:
                    scores.append(json.loads(record))
                except json.JSONDecodeError:
                    logger.error(f"Invalid JSON on line {line_idx:,}: {record}.")
                    return

    # Reorganize the scores by each model
    model_scores: dict[str, dict[str, tuple[str, str, str]]] = defaultdict(dict)
    for record in scores:

        # Extract data from record
        model_id: str = record["model"]
        model_notes: list[str] = list()
        if record.get("generative", True) and record.get("few_shot", True):
            model_notes.append("few-shot")
        if record.get("validation_split", False):
            model_notes.append("val")
        if model_notes:
            model_id += f" ({', '.join(model_notes)})"
        task: str = record["task"]
        languages: list[str] = record["dataset_languages"]

        # Special case if the record is a speed benchmark
        if task == "speed":
            results: dict[str, float] = record["results"]["total"]
            metrics: set[str] = {
                key.replace('test_', '').replace('_se', '')
                for key in results.keys() if key.startswith("test_")
            }
            score_dict: dict[str, str] = dict()
            for metric in metrics:
                test_score = results[f"test_{metric}"]
                test_se = results[f"test_{metric}_se"]
                score_dict[metric] = f"{test_score:,.0f} ± {test_se:,.0f}"

            relevant_metrics = ["speed", "speed_short"]
            score_str = " / ".join(score_dict[metric] for metric in relevant_metrics)
            model_scores[model_id]["speed"] = (score_str, " ".join(languages), task)

        # Non-speed case
        else:
            # Skip record if we are not including it in the leaderboard
            dataset_names = [dataset[0].lower().replace(" ", "-") for dataset in datasets]
            if record["dataset"] not in dataset_names:
                continue

            # Add Norwegian if Bokmål or Nynorsk is included
            languages = list(
                {re.sub(r"nb|nn", "no", language.lower()) for language in languages}
            )

            # Skip record if it is in a language we are not including
            if not any(language in language_mapping.keys() for language in languages):
                continue

            # Extract the scores from the dict
            results: dict[str, float] = record["results"]["total"]
            metrics: set[str] = {
                key.replace('test_', '').replace('_se', '')
                for key in results.keys() if key.startswith("test_")
            }

            # Skip the record if any of the metrics is unknown
            if any(metric not in metric_mapping.keys() for metric in metrics):
                continue

            score_dict: dict[str, str] = dict()
            for metric in metrics:
                test_score = results[f"test_{metric}"]
                test_se = results[f"test_{metric}_se"]
                score_dict[metric] = f"{test_score:.2f} ± {test_se:.2f}"

            # Order the metric scores and generate final score string
            relevant_metrics = [
                (primary_metric, secondary_metric)
                for dataset_name, _, _, primary_metric, secondary_metric in datasets
                if dataset_name.lower().replace(" ", "-") == record["dataset"]
            ][0]
            score_str = " / ".join(score_dict[metric] for metric in relevant_metrics)

            # Extract shorthand notation for the task
            for task_code, task_name in task_mapping.items():
                task_name_kebab = task_name.lower().replace(" ", "-")
                if task == task_name_kebab:
                    task_shorthand = task_code
                    break
            else:
                logger.info(f"{task} not among {task_mapping.values()}")
                continue

            # Add the metrics to the model's score dict
            model_scores[model_id][record['dataset']] = (
                score_str, " ".join(languages), task_shorthand
            )

            # Add the ScandEval version to the model's score dict
            model_scores[model_id][f"{record['dataset']}-version"] = (
                record.get("scandeval_version", "0.0.0"), "", ""
            )

        # Round the number of parameters to nearest million
        num_params = (
            round(record["num_model_parameters"] / 1_000_000)
            if record["num_model_parameters"] >= 0
            else "unknown"
        )
        record["num_model_parameters"] = num_params

        # Round the vocabulary size to nearest thousand
        vocab_size = round(record["vocabulary_size"] / 1_000)
        record["vocabulary_size"] = vocab_size

        # Add the model metadata to the model's dict, if it hasn't previously been
        # entered
        for metadata in [
            "num_model_parameters",
            "vocabulary_size",
            "max_sequence_length",
        ]:
            if metadata not in model_scores[model_id] and metadata in record:
                record_metadata = str(record[metadata])
                model_scores[model_id][metadata] = (record_metadata, "", "")

        # Add information on whether the model is a merge of other models
        if "merge" in record:
            model_scores[model_id]["merge"] = (str(int(record["merge"])), "", "")

    # Generate language model benchmark HTML
    all_values: list[dict[str, str]] = list()
    for model_id, model_dict in model_scores.items():

        merge = bool(int(model_dict.get("merge", ["0"])[0]))
        merge_tag = "merged-model" if merge else "not-merged-model"

        # Add the model metadata and speed score
        values = dict(
            model_id=model_id,
            merge=merge_tag,
            num_model_parameters=model_dict.get("num_model_parameters", [""])[0],
            vocabulary_size=model_dict.get("vocabulary_size", [""])[0],
            max_sequence_length=model_dict.get("max_sequence_length", [""])[0],
            speed=model_dict.get("speed", [""])[0],
        )

        # Add the scores for each dataset
        for dataset, _, _, _, _ in datasets:
            dataset_underscore = dataset.lower().replace(" ", "_").replace("-", "_")
            dataset_hyphen = dataset.lower().replace(" ", "-")
            values[dataset_underscore] = model_dict.get(dataset_hyphen, [""])[0]
            values[f"{dataset_underscore}-version"] = model_dict.get(
                f"{dataset_hyphen}-version", [""]
            )[0]

        # Add the value dictionary to the list of all values
        if all([value != "" for value in values.values()]):
            all_values.append(values)
        else:
            missing_datasets = [
                dataset for dataset, score_str in values.items() if score_str == ""
            ]
            if LOG_MISSING:
                pct_missing = sum(
                    int(
                        dataset.lower().replace(" ", "_").replace("-", "_")
                        in missing_datasets
                    )
                    for dataset, _, _, _, _ in datasets
                ) / len(datasets)
                if pct_missing < 0.3:
                    logger.info(
                        f"In the {title}, {values['model_id']!r} is missing the "
                        f"datasets {missing_datasets}."
                    )

    def extract_scores_for_model(model_id: str, dataset: str) -> list[float]:
        """Extract the scores for a model on a specific dataset.

        Args:
            model_id:
                The model ID to extract the scores for.
            dataset:
                The dataset to extract the scores for.

        Returns:
            The scores for the model on the dataset.

        Raises:
            ValueError:
                If the scores for the model on the dataset could not be found, or if
                there are multiple scores for the model on the dataset.
        """
        validation_split = re.search(r"\(.*val.*\)", model_id) is not None
        model_id = re.sub(r" *\(.+\) *", "", model_id.lower())

        possible_score_dicts = [
            dct for dct in scores
            if dct["model"].lower() == model_id
            and dct["dataset"].lower().replace(" ", "_").replace("-", "_") == dataset
            and dct.get("validation_split", False) == validation_split
        ]
        if not possible_score_dicts:
            raise ValueError(f"Could not find scores for {model_id} on {dataset}")
        if len(possible_score_dicts) > 1:
            raise ValueError(f"Found multiple scores for {model_id} on {dataset}")

        raw_scores = [
            result_dict.get(f"test_{metric_name}", result_dict.get(metric_name, -1))
            for score_dict in possible_score_dicts
            for result_dict in score_dict["results"]["raw"]["test"]
            for dataset, _, _, metric_name, _ in datasets
            if dataset.lower().replace(" ", "-") == score_dict["dataset"]
        ]

        if any(score == -1 for score in raw_scores):
            raise ValueError(f"Found -1 in {raw_scores}")

        # Ensure that the scores are on the same scale
        if max(raw_scores) <= 1:
            raw_scores = [score * 100 for score in raw_scores]

        return raw_scores

    def significantly_better(
        score_values_1: list[float], score_values_2: list[float]
    ) -> float:
        """Compute one-tailed t-statistic for the difference between two sets of scores.

        Args:
            score_values_1:
                The first set of scores.
            score_values_2:
                The second set of scores.

        Returns:
            The t-statistic of the difference between the two sets of scores, where
            a positive t-statistic indicates that the first set of scores is
            statistically better than the second set of scores.
        """
        assert len(score_values_1) == len(score_values_2)
        if score_values_1 == score_values_2:
            return 0
        test_result = stats.ttest_ind(
            a=score_values_1, b=score_values_2, alternative="greater", equal_var=False
        )
        return test_result.pvalue < 0.05

    # Compute rank scores for all datasets
    for dataset, _, _, _, _ in datasets:
        dataset_underscore = dataset.lower().replace(" ", "_").replace("-", "_")
        dataset_values_sorted = sorted(
            all_values,
            key=lambda x: float(x[dataset_underscore].split()[0]),
            reverse=True,
        )
        stddev = np.std([
            float(values[dataset_underscore].split()[0])
            for values in dataset_values_sorted
        ])
        rank_score = 0
        previous_scores: list[float] = list()
        for idx, values in enumerate(dataset_values_sorted):
            if idx == 0:
                values[f"{dataset_underscore}_rank"] = str(rank_score)
                previous_scores = extract_scores_for_model(
                    model_id=values["model_id"], dataset=dataset_underscore
                )
                continue
            current_scores = extract_scores_for_model(
                model_id=values["model_id"], dataset=dataset_underscore
            )

            if significantly_better(previous_scores, current_scores):
                difference = np.mean(previous_scores) - np.mean(current_scores)
                normalised_difference = difference / stddev
                previous_scores = current_scores
                rank_score += normalised_difference
            values[f"{dataset_underscore}_rank"] = str(rank_score)

    # Compute average scores for each language
    for language_code in language_mapping.keys():
        for values in all_values:
            mean_scores = list()
            for task_code in task_mapping.keys():
                datasets_for_language_and_task = [
                    dataset.lower().replace(" ", "_").replace("-", "_")
                    for dataset, language, task, _, _ in datasets
                    if language == language_code and task == task_code
                ]
                if not datasets_for_language_and_task:
                    continue
                mean_score = np.mean([
                    float(values[f"{dataset}_rank"])
                    for dataset in datasets_for_language_and_task
                ]).item()
                mean_scores.append(mean_score)
            mean_score = np.mean(mean_scores).item()
            values[f"{language_code}_rank"] = f"{mean_score:.2f}"

    # Compute the final score for each model
    for values in all_values:
        all_language_scores = [
            float(values[f"{language_code}_rank"])
            for language_code in language_mapping.keys()
        ]
        mean_rank = np.mean(all_language_scores).item()
        values["rank"] = f"{mean_rank:.2f}"

    all_values = sorted(all_values, key=lambda x: float(x["rank"]))

    if all_values:
        df = generate_csv_df(
            all_values=all_values, datasets=datasets
        ).set_index("model_id")

        # Get the new model IDs in the leaderboard
        csv_path = Path(f"{title_kebab}.csv")
        if csv_path.exists():
            old_df = pd.read_csv(csv_path).set_index("model_id")
            changed_model_ids = [
                str(model_id)
                for model_id, row in df.iterrows()
                if model_id not in old_df.index.values
                or {key: val for key, val in row.to_dict().items() if "rank" not in key}
                != {key: val for key, val in old_df.loc[model_id].to_dict().items() if "rank" not in key}
            ]
        else:
            changed_model_ids = df.index.tolist()

        df.to_csv(csv_path)

        embed_code = get_embed_code(
            title=title, csv_url=f"https://scandeval.com/{title_kebab}.csv", csv_df=df,
        )

        # Build the HTML for the leaderboard
        if changed_model_ids:
            html_lines = [BENCHMARK_HTML_START]
            for values in all_values:
                html_lines.append(BENCHMARK_ENTRY.format(**values))
            html_lines.append(BENCHMARK_HTML_END.format(embed_code=embed_code))
            html = "\n".join(html_lines)

            with benchmark_path.open("w") as f:
                f.write(html)

            logger.info(
                f"Generated {title} with results from {len(all_values):,} models, out "
                f"of which the following {len(changed_model_ids):,} were changed or "
                f"new: {', '.join(changed_model_ids)}."
            )

        else:
            logger.info(
                f"No changes to {title} were detected, so the leaderboard was not "
                f"updated."
            )


def generate_csv_df(
    all_values: list[dict[str, str]],
    datasets: list[tuple[str, str | None, str, str, str]],
) -> pd.DataFrame:
    """Generate a CSV file from the list of values.

    Args:
        all_values:
            A list of dictionaries containing the values for each model.
        datasets:
            A list of (dataset_name, language_code, task_code, primary_metric_code,
            secondary_metric_code) tuples. These are the datasets that will be included
            in the leaderboard.

    Returns:
        The DataFrame containing the values.
    """
    def clean_value(value: str) -> str | float | int:
        if value == "unknown":
            return -1
        elif isinstance(value, str):
            numeric_value = (
                value.replace(",", "").replace("=","").split()[0]
            )
            if numeric_value.replace("-", "").replace(".", "", 1).isdigit():
                return float(numeric_value)
        return value

    df = pd.DataFrame(all_values).map(clean_value).convert_dtypes()

    columns_to_include = [
        "model_id",
        "num_model_parameters",
        "vocabulary_size",
        "max_sequence_length",
        "merge",
        "speed",
        "rank",
    ]
    language_score_columns = [
        language_score_column
        for language_score_column in df.columns
        if re.match(r"^[a-z]{2}_rank$", language_score_column) is not None
    ]
    if len(language_score_columns) > 1:
        columns_to_include.extend(language_score_columns)
    columns_to_include.extend([
        dataset.lower().replace(" ", "_").replace("-", "_")
        for dataset, _, _, _, _ in datasets
    ])
    df = df[columns_to_include]
    assert isinstance(df, pd.DataFrame)
    return df


def get_embed_code(title: str, csv_url: str, csv_df: pd.DataFrame) -> str:
    """Get the HTML embed code for the leaderboard.

    Args:
        title:
            The title of the leaderboard.
        csv_url:
            The URL to the CSV file.
        csv_df:
            The DataFrame containing the values.

    Returns:
        The HTML embed code for the leaderboard.

    Raises:
        ValueError:
            If the Datawrapper API key is not found.
    """
    api_key = os.getenv("DATAWRAPPER_API_KEY")
    if api_key is None:
        raise ValueError("No Datawrapper API key found.")

    dw = Datawrapper(access_token=api_key)

    # Never generate embed code for test leaderboards
    csv_url = csv_url.replace("-test", "")

    # Create the metadata for the datawrapper table, being all the relevant formatting
    metadata: dict[str, Any] = dict(
        visualize=dict(
            perPage=10,
            showRank=True,
            firstColumnIsSticky=True,
            searchable=True,
        ),
    )
    number_columns = [
        col
        for col in csv_df.columns
        if col not in [
            "model_id",
            "num_model_parameters",
            "vocabulary_size",
            "max_sequence_length",
            "speed",
        ]
    ]
    metadata['visualize']["columns"] = {
        number_column: dict(format="0.00") for number_column in number_columns
    }

    dw_kwargs = dict(
        title=title,
        chart_type="tables",
        external_data_url=csv_url,
        metadata=metadata,
    )

    # Load the chart if it already exists, otherwise create a new one
    all_charts = dw.get_charts()["list"]
    matching_charts = [chart for chart in all_charts if chart["title"] == title]
    if matching_charts:
        dw_table = matching_charts[0]
        dw.update_chart(chart_id=dw_table["id"], **dw_kwargs)
    else:
        dw_table = dw.create_chart(**dw_kwargs)

    dw.update_description(
        chart_id=dw_table["id"],
        source_name="ScandEval",
        source_url=csv_url.replace(".csv", ""),
        byline="Dan Saattrup Nielsen",
    )

    dw.update_chart(chart_id=dw_table["id"], metadata=metadata)

    for attempt in range(NUM_EMBED_ATTEMPTS):
        try:
            dw.publish_chart(chart_id=dw_table["id"], display=False)
            embed_code = dw.get_iframe_code(chart_id=dw_table["id"], responsive=True)
            embed_code = embed_code.replace('"', "&quot;")
            return embed_code
        except TimeoutError:
            logger.warning(f"Attempt {attempt + 1} to publish the chart timed out.")
            time.sleep(5)
    else:
        logger.error(
            f"Failed to publish the chart after {NUM_EMBED_ATTEMPTS} attempts."
        )
        return "Embed code could not be generated."


if __name__ == "__main__":
    generate_leaderboard()
