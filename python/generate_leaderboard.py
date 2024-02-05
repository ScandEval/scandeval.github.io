"""Python script to generate ScandEval leaderboards."""

from collections import defaultdict
from pathlib import Path
import json
import logging
from datetime import datetime
import click
import re
import scipy.stats as stats
import os
import pandas as pd
import numpy as np

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)


# Variable determining whether all models that haven't been fully benchmarked should be
# logged along with the datasets they are missing
LOG_MISSING = bool(os.getenv("LOG_MISSING", None))


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

    title_kebab = title.lower().replace(" ", "-")

    BENCHMARK_HTML_START = f"""---
layout: leaderboard
title: {title}
---

<center>Last updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} CET</center>

<div class="table-wrapper centered">

<input type="checkbox" id="merged-models-checkbox">
<label for="merged-models-checkbox">Include merged models</label>

<table id="{title_kebab}" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    """

    # Add language score columns, if there are multiple languages
    if len(language_mapping) > 1:
        for language_code, language_name in language_mapping.items():
            if language_code is None:
                continue
            language_code_upper = language_code.upper()
            language_name_title = language_name.title()
            BENCHMARK_HTML_START += f"""
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total {language_name_title} score">{language_code_upper}</span></th>"""
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

    BENCHMARK_HTML_START += """
  </tr>
 </thead>
 <tbody>"""

    BENCHMARK_HTML_END = f""" </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/{title_kebab}.csv" target="_blank">Download as CSV</a>
</div>"""

    BENCHMARK_ENTRY = """  <tr class="{merge}">
   <td class="rank">{rank}</td> <!-- Rank -->
   <td>{model_id}</td> <!-- Model ID -->
   <td class="num_model_parameters">{num_model_parameters}</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">{vocabulary_size}</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">{max_sequence_length}</td> <!-- Maximum sequence length of the model-->
   <td class="speed">{speed}</td> <!-- Model inference speed -->
   <td class="score">{score}</td> <!-- ScandEval score -->"""

    # Add language score columns, if there are multiple languages
    if len(language_mapping) > 1:
        for language_code, language_name in language_mapping.items():
            if language_code is None:
                continue
            language_code_lower = language_code.lower()
            language_name_title = language_name.title()
            BENCHMARK_ENTRY += f"""
   <td class="{language_code_lower}-score">{{{language_code_lower}_score}}</td> <!-- {language_name_title} score -->"""

    # Add dataset score columns
    for dataset_name, language_code, task_code, _, _ in datasets:
        language_code_with_space = language_code.lower() + " " if language_code is not None else ""
        task_code_lower = task_code.lower()
        dataset_name_lower = dataset_name.lower().replace(" ", "_").replace("-", "_")
        BENCHMARK_ENTRY += f"""
   <td class="{language_code_with_space}{task_code_lower}">{{{dataset_name_lower}}}</td> <!-- {dataset_name} -->"""

    BENCHMARK_ENTRY += """
  </tr>"""

    # Create path to the leaderboard, and ensure that the parent directory exists
    benchmark_path = Path(f"{title_kebab}.md")
    benchmark_path.parent.mkdir(exist_ok=True, parents=True)
    benchmark_path.unlink(missing_ok=True)

    # Remove the CSV file, if it exists
    Path(f"{title_kebab}.csv").unlink(missing_ok=True)

    # Create path to the scores JSONL file, and raise error if it doesn't exist
    scores_path = Path("scandeval_benchmark_results.jsonl")
    if not scores_path.exists():
        raise FileNotFoundError(f"Could not find {scores_path!r}")

    # Load in scores
    with scores_path.open() as f:
        scores = [json.loads(line) for line in f if line.strip()]

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
            "num_model_parameters", "vocabulary_size", "max_sequence_length",
        ]:
            if metadata not in model_scores[model_id] and metadata in record:
                record_metadata = str(record[metadata])
                model_scores[model_id][metadata] = (record_metadata, "", "")

        # Add information on whether the model is a merge of other models
        if "merge" in record:
            model_scores[model_id]["merge"] = (str(int(record["merge"])), "", "")

    # Generate language model benchmark HTML
    html_lines = [BENCHMARK_HTML_START]
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

        # Add aggregated scores for each language
        total_score: float = 0.0
        total_score_se: float = 0.0
        for language_code in language_mapping.keys():

            # Get all the task scores for the language
            task_mean_score_lists: dict[str, list[float]] = defaultdict(list)
            task_se_score_lists: dict[str, list[float]] = defaultdict(list)
            for dataset, language, task, _, _ in datasets:
                if language != language_code:
                    continue
                dataset_underscore = dataset.lower().replace(" ", "_").replace("-", "_")
                dataset_score_str = values.get(dataset_underscore, "")
                if dataset_score_str:
                    task_mean_score_lists[task].append(float(dataset_score_str.split()[0]))
                    task_se_score_lists[task].append(float(dataset_score_str.split()[2]))

            task_mean_scores = {
                task: sum(score_list) / len(score_list)
                for task, score_list in task_mean_score_lists.items()
            }
            task_se_scores = {
                task: sum(score_list) / len(score_list)
                for task, score_list in task_se_score_lists.items()
            }

            if not task_mean_scores:
                continue

            # Compute the language score
            language_mean_score = sum(task_mean_scores.values()) / len(task_mean_scores)
            language_se_score = sum(task_se_scores.values()) / len(task_se_scores)
            values[f"{language_code}_score"] = (
                f"{language_mean_score:.2f} ± {language_se_score:.2f}"
            )

            # Add the language score to the total score
            total_score += language_mean_score
            total_score_se += language_se_score

        # Compute the total score
        total_score = total_score / len(language_mapping)
        total_score_se = total_score_se / len(language_mapping)
        values["score"] = f"{total_score:.2f} ± {total_score_se:.2f}"

        # Add the value dictionary to the list of all values
        if all([value != "" for value in values.values()]):
            all_values.append(values)
        else:
            if LOG_MISSING:
                missing_datasets = [
                    dataset for dataset, score_str in values.items() if score_str == ""
                ]
                all_are_missing = all(
                    dataset.lower().replace(" ", "_").replace("-", "_") in missing_datasets
                    for dataset, _, _, _, _ in datasets
                )
                if not all_are_missing:
                    logger.info(
                        f"In the {title}, {values['model_id']!r} is missing the "
                        f"datasets {missing_datasets}."
                    )

    def extract_scores_for_model(model_id: str) -> dict[str, list[float]]:
        validation_split = re.search(r"\(.*val.*\)", model_id) is not None
        rank_score_dict = {
            score_dict["dataset"]: [
                result_dict.get(f"test_{metric_name}", result_dict.get(metric_name, -1))
                for result_dict in score_dict["results"]["raw"]["test"]
                for dataset, _, _, metric_name, _ in datasets
                if dataset.lower().replace(" ", "-") == score_dict["dataset"]
            ]
            for score_dict in scores
            if score_dict["model"] == re.sub(r" *\(.+\) *", "", model_id)
            and score_dict.get("validation_split", False) == validation_split
        }

        if any(-1 in scores for scores in rank_score_dict.values()):
            raise ValueError(f"Found -1 in {rank_score_dict}")

        rank_score_dict = {
            dataset: scores
            for dataset, scores in sorted(rank_score_dict.items(), key=lambda x: x[0])
            if scores
        }

        # Ensure that the scores are on the same scale
        for dataset, score_list in rank_score_dict.items():
            if max(score_list) < 1:
                rank_score_dict[dataset] = [score * 100 for score in score_list]

        return rank_score_dict

    def score_dicts_statistically_better(
        score_dict_1: dict[str, list[float]], score_dict_2: dict[str, list[float]]
    ) -> bool:
        if list(score_dict_1.keys()) != list(score_dict_2.keys()):
            raise ValueError(
                f"The two score dicts must have the same keys: "
                f"{list(score_dict_1.keys())} != {list(score_dict_2.keys())}"
            )

        score_values_1 = [
            score
            for scores in score_dict_1.values()
            for score in scores
        ]
        score_values_2 = [
            score
            for scores in score_dict_2.values()
            for score in scores
        ]
        assert len(score_values_1) == len(score_values_2)

        # Separate the scores into groups of 10, consisting of the scores for each
        # dataset
        group_scores_1 = [
            score_values_1[idx:idx+10] for idx in range(0, len(score_values_1), 10)
        ]
        group_scores_2 = [
            score_values_2[idx:idx+10] for idx in range(0, len(score_values_2), 10)
        ]

        # Compute t-statistics for each group separately, and compute the mean
        # t-statistic
        t_statistics = [
            stats.ttest_ind(a=group_1, b=group_2, alternative="greater").statistic
            for group_1, group_2 in zip(group_scores_1, group_scores_2)
        ]
        mean_t_statistic = np.mean(t_statistics)

        # Compute the p-value for the mean t-statistic, where the null hypothesis is
        # that the first group does not have a larger mean score than the second group
        degrees_of_freedom = len(score_values_1) - 1
        p_value = 1 - stats.t.cdf(abs(mean_t_statistic), degrees_of_freedom)

        return p_value < 0.05

    # Add the rank to each model
    all_values = sorted(
        all_values, key=lambda x: float(x["score"].split()[0]), reverse=True
    )
    rank = 1
    rank_scores: dict[str, list[float]] = dict()
    for idx, values in enumerate(all_values):
        if idx == 0:
            values["rank"] = str(rank)
            rank_scores = extract_scores_for_model(model_id=values["model_id"])
            continue
        current_scores = extract_scores_for_model(model_id=values["model_id"])

        if score_dicts_statistically_better(rank_scores, current_scores):
            rank_scores = current_scores
            rank += 1
        values["rank"] = str(rank)

    # Add "=" suffixes to the rank if the models have the same rank
    for idx, values in enumerate(all_values):
        rank = values["rank"]
        num_models_with_rank = len(
            [value for value in all_values if value["rank"].rstrip("=") == rank]
        )
        if num_models_with_rank > 1:
            values["rank"] += "="

    # Add HTML entry for the model, if it has been evaluated on all datasets
    for values in all_values:
        html_lines.append(BENCHMARK_ENTRY.format(**values))

    html_lines.append(BENCHMARK_HTML_END)
    html = "\n".join(html_lines)

    # Write table to the file
    if all_values:
        with benchmark_path.open("w") as f:
            f.write(html)
        generate_csv(all_values=all_values, datasets=datasets, file_name=title_kebab)
        logger.info(
            f"Generated {title} with results from {len(all_values):,} models, stored "
            f"at {str(benchmark_path)!r}"
        )


def generate_csv(
    all_values: list[dict[str, str]],
    datasets: list[tuple[str, str | None, str, str, str]],
    file_name: str,
) -> None:
    """Generate a CSV file from the list of values.

    Args:
        all_values:
            A list of dictionaries containing the values for each model.
        datasets:
            A list of (dataset_name, language_code, task_code, primary_metric_code,
            secondary_metric_code) tuples. These are the datasets that will be included
            in the leaderboard.
        file_name:
            The name of the CSV file to generate, without the .csv extension.
    """
    def clean_value(value: str) -> str | float | int:
        if isinstance(value, str):
            numeric_value = (
                value.replace(",", "").replace("=","").split()[0]
            )
            if numeric_value.replace("-", "").replace(".", "").isdigit():
                return float(numeric_value)
        return value

    df = pd.DataFrame(all_values).map(clean_value).convert_dtypes()
    df = df[[
        "rank",
        "model_id",
        "num_model_parameters",
        "vocabulary_size",
        "max_sequence_length",
        "speed",
        "score",
    ] + [
        language_score_column
        for language_score_column in df.columns
        if "_score" in language_score_column
    ] + [
        dataset.lower().replace(" ", "_").replace("-", "_")
        for dataset, _, _, _, _ in datasets
    ]]

    df.to_csv(f"{file_name}.csv", index=False)


if __name__ == "__main__":
    generate_leaderboard()
