"""Python script to generate the Insular Scandinavian NLU leaderboard."""

from collections import defaultdict
from pathlib import Path
import json
from typing import Dict, List, Set
import logging
from datetime import datetime

# Set up logging, which should display logs as "HH:MM:SS [LEVEL] MESSAGE"
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


BENCHMARK_HTML_START = f"""---
layout: leaderboard
title: Insular Scandinavian NLU Benchmark
---

<center>Last updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="insular-scandinavian-nlu-benchmark" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Icelandic score - Macro-average across tasks">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Faroese score - Macro-average across tasks">NO</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total named entity recognition score - Macro-average across languages">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification tagging score - Macro-average across languages">SENT</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total linguistic acceptability score - Macro-average across languages">LA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total question answering score - Macro-average across languages">QA</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Matthews correlation coefficient / Macro-average F1-score">???</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact match / F1-score">NQiI</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">WikiANN-FO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Matthews correlation coefficient / Macro-average F1-score">???</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese question answering - Exact match / F1-score">???</span></th>
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
   <td class="score"></td> <!-- ScandEval score -->
   <td class="is-score"></td> <!-- Icelandic score -->
   <td class="fo-score"></td> <!-- Faroese score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="is ner">{is_ner}</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">{is_sent}</td> <!-- ??? -->
   <td class="is la">{is_la}</td> <!-- ScaLA-is -->
   <td class="is qa">{is_qa}</td> <!-- NQiI -->
   <td class="fo ner">{nb_ner}</td> <!-- WikiANN-FO -->
   <td class="fo sent">{no_sent}</td> <!-- ??? -->
   <td class="fo la">{nb_la}</td> <!-- ScaLA-fo -->
   <td class="fo qa">{no_qa}</td> <!-- ??? -->
  </tr>"""


# Set up primary/secondary metrics
PRIMARY_METRICS = ["mcc", "em", "micro_f1", "speed"]
SECONDARY_METRICS = ["macro_f1", "f1", "micro_f1_no_misc", "speed_short"]


# Set up list of outdated datasets
OUTDATED_DATASETS = []


def main() -> None:
    """Generate the leaderboard(s)."""

    # Create path to the leaderboard, and ensure that it exists
    benchmark_path = Path("insular-scandinavian-nlu-benchmark.md")
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
    model_scores: Dict[str, Dict[str, str]] = defaultdict(dict)
    for record in scores:

        # Skip record if it's a benchmark of an outdated dataset
        if record["dataset"] in OUTDATED_DATASETS:
            continue

        # Extract data from record
        model_id: str = record["model"]
        if record.get("few_shot", True):
            model_id += " (few-shot)"
        task: str = record["task"]
        languages: List[str] = record["dataset_languages"]

        # Extract the scores from the dict
        results: Dict[str, float] = record["results"]["total"]
        metrics: Set[str] = {
            key.replace('test_', '').replace('_se', '')
            for key in results.keys() if key.startswith("test_")
        }
        score_dict: Dict[str, str] = dict()
        for metric in metrics:

            # Raise error if the metric is unknown
            if metric not in PRIMARY_METRICS + SECONDARY_METRICS:
                raise ValueError(f"Unknown metric: {metric!r}")

            test_score = results[f"test_{metric}"]
            test_se = results[f"test_{metric}_se"]
            if metric.startswith("speed"):
                score_dict[metric] = f"{test_score:,.0f} ± {test_se:,.0f}"
            else:
                score_dict[metric] = f"{test_score:.2f} ± {test_se:.2f}"

        # Order the metric scores and generate final score string
        primary_metrics = [m for m in PRIMARY_METRICS if m in metrics]
        secondary_metrics = [m for m in SECONDARY_METRICS if m in metrics]
        score_list = primary_metrics + secondary_metrics
        score_str = " / ".join(score_dict[metric] for metric in score_list)

        # Extract single language from the languages
        if len(languages) == 1:
            language = languages[0]
        elif set(languages) == {"nb", "nn"}:
            language = "no"
        else:
            language = None

        # Extract shorthand notation for the task
        if task == "sentiment-classification":
            task_shorthand = "sent"
        elif task == "named-entity-recognition":
            task_shorthand = "ner"
        elif task == "linguistic-acceptability":
            task_shorthand = "la"
        elif task == "question-answering":
            task_shorthand = "qa"
        elif task == "speed":
            task_shorthand = "speed"
        else:
            continue

        # Add the metrics to the model's score dict
        if language in ["da", "no", "nb", "nn", "sv"]:
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
            speed=model_dict.get("speed", ""),
            is_ner=model_dict.get("is ner", ""),
            is_sent=model_dict.get("is sent", ""),
            is_la=model_dict.get("is la", ""),
            is_qa=model_dict.get("is qa", ""),
            fo_ner=model_dict.get("fo ner", ""),
            fo_sent=model_dict.get("fo sent", ""),
            fo_la=model_dict.get("fo la", ""),
            fo_qa=model_dict.get("fo qa", ""),
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
        "Generated Insular Scandinavian NLU benchmark with results from "
        f"{len(model_scores):,} models, stored at {str(benchmark_path)!r}"
    )


if __name__ == "__main__":
    main()
