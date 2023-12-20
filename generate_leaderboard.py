"""Python script to generate ScandEval leaderboards."""

from collections import defaultdict
from pathlib import Path
import json
import logging
from datetime import datetime
import click
import re

# Set up logging, which should display logs as "HH:MM:SS [LEVEL] MESSAGE"
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


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

<center>Last updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="{title_kebab}" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval model rank">Rank</span></th>
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

    # Add task score columns
    for task_code, task_name in task_mapping.items():
        task_code_upper = task_code.upper()
        task_name_lower = task_name.lower()
        BENCHMARK_HTML_START += f"""
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total {task_name_lower} score">{task_code_upper}</span></th>"""
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

    BENCHMARK_HTML_END = """ </tbody>
</table>
</div>"""

    BENCHMARK_ENTRY = """  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>{model_id}</td> <!-- Model ID -->
   <td class="num_model_parameters">{num_model_parameters}</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">{vocabulary_size}</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">{max_sequence_length}</td> <!-- Maximum sequence length of the model-->
   <td class="speed">{speed}</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->"""

    # Add language score columns, if there are multiple languages
    if len(language_mapping) > 1:
        for language_code, language_name in language_mapping.items():
            if language_code is None:
                continue
            language_code_lower = language_code.lower()
            language_name_title = language_name.title()
            BENCHMARK_ENTRY += f"""
   <td class="{language_code_lower}-score"></td> <!-- {language_name_title} score -->"""

    # Add task score columns
    for task_code, task_name in task_mapping.items():
        task_code_lower = task_code.lower()
        task_name_lower = task_name.lower()
        BENCHMARK_ENTRY += f"""
   <td class="{task_code_lower}-score"></td> <!-- Mean {task_name_lower} score -->"""

    # Add dataset score columns
    for dataset_name, language_code, task_code, _, _ in datasets:
        language_code_with_space = language_code.lower() + " " if language_code is not None else ""
        language_code_with_underscore = language_code.lower() + "_" if language_code is not None else ""
        task_code_lower = task_code.lower()
        BENCHMARK_ENTRY += f"""
   <td class="{language_code_with_space}{task_code_lower}">{{{language_code_with_underscore}{task_code_lower}}}</td> <!-- {dataset_name} -->"""

    BENCHMARK_ENTRY += """
  </tr>"""

    # Create path to the leaderboard, and ensure that it exists
    benchmark_path = Path(f"{title_kebab}.md")
    benchmark_path.parent.mkdir(exist_ok=True, parents=True)
    benchmark_path.touch(exist_ok=True)

    # Create path to the scores JSONL file, and raise error if it doesn't exist
    scores_path = Path("scandeval_benchmark_results.jsonl")
    if not scores_path.exists():
        raise FileNotFoundError(f"Could not find {scores_path!r}")

    # Load in scores
    with scores_path.open() as f:
        scores = [json.loads(line) for line in f if line.strip()]

    # Reorganize the scores by each model
    model_scores: dict[str, dict[str, str]] = defaultdict(dict)
    for record in scores:

        # Extract data from record
        model_id: str = record["model"]
        if record.get("few_shot", True):
            model_id += " (few-shot)"
        task: str = record["task"]
        languages: list[str] = record["dataset_languages"]

        # Special case if the record is a speed benchmark
        if record["task"] == "speed":
            results: dict[str, float] = record["results"]["total"]
            metrics: set[str] = {
                key.replace('test_', '').replace('_se', '')
                for key in results.keys() if key.startswith("test_")
            }
            score_dict: dict[str, str] = dict()
            for metric in metrics:

                # Raise error if the metric is unknown
                if metric not in metric_mapping.keys():
                    raise ValueError(f"Unknown metric: {metric!r}")

                test_score = results[f"test_{metric}"]
                test_se = results[f"test_{metric}_se"]
                score_dict[metric] = f"{test_score:,.0f} ± {test_se:,.0f}"

            relevant_metrics = ["speed", "speed_short"]
            score_str = " / ".join(score_dict[metric] for metric in relevant_metrics)
            model_scores[model_id]["speed"] = score_str

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
            score_dict: dict[str, str] = dict()
            for metric in metrics:

                # Raise error if the metric is unknown
                if metric not in metric_mapping.keys():
                    raise ValueError(f"Unknown metric: {metric!r}")

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

            # Extract single language from the languages
            if len(languages) == 1:
                language = languages[0]
            else:
                language = None

            # Extract shorthand notation for the task
            for task_code, task_name in task_mapping.items():
                task_name_kebab = task_name.lower().replace(" ", "-")
                if task == task_name_kebab:
                    task_shorthand = task_code
                    break
            else:
                print(f"{task} not among {task_mapping.values()}")
                continue

            # Add the metrics to the model's score dict
            if language in languages:
                model_scores[model_id][f"{language} {task_shorthand}"] = score_str
            else:
                model_scores[model_id][task_shorthand] = score_str

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
        for metadata in ["num_model_parameters", "vocabulary_size", "max_sequence_length"]:
            if metadata not in model_scores[model_id] and metadata in record:
                model_scores[model_id][metadata] = str(record[metadata])

    # Generate language model benchmark HTML
    models_to_remove = list()
    html_lines = [BENCHMARK_HTML_START]
    for model_id, model_dict in model_scores.items():
        values = dict(
            model_id=model_id,
            num_model_parameters=model_dict.get("num_model_parameters", ""),
            vocabulary_size=model_dict.get("vocabulary_size", ""),
            max_sequence_length=model_dict.get("max_sequence_length", ""),
            speed=model_dict.get("speed", "")
        )
        for language_code, language_name in language_mapping.items():
            for task_code, task_name in task_mapping.items():
                if language_code is None or task_code == "speed":
                    continue
                values[f"{language_code}_{task_code}"] = model_dict.get(
                    f"{language_code} {task_code}", ""
                )
        if all([value != "" for value in values.values()]):
            html_lines.append(BENCHMARK_ENTRY.format(**values))
        else:
            models_to_remove.append(model_id)
    html_lines.append(BENCHMARK_HTML_END)
    html = "\n".join(html_lines)

    # Remove the models not added to the leaderboard
    for model_id in models_to_remove:
        del model_scores[model_id]

    # Write table to the file
    with benchmark_path.open("w") as f:
        f.write(html)

    # Log status
    logging.info(
        f"Generated {title} with results from {len(model_scores):,} models, stored "
        f"at {str(benchmark_path)!r}"
    )


if __name__ == "__main__":
    generate_leaderboard()
