"""Python script to generate the leaderboard."""

from collections import defaultdict
from pathlib import Path
import json
from typing import Dict, List, Set


HTML_START = """---
layout: leaderboard
title: Leaderboard
---

<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="leaderboard" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of traininable model parametes">Parameters</span></th>
   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score - Macro-average across tasks">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score - Macro-average across tasks">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score - Macro-average across tasks">SV</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total named entity recognition score - Macro-average across languages">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification tagging score - Macro-average across languages">SENT</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total linguistic acceptability score - Macro-average across languages">LA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total question answering score - Macro-average across languages">QA</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">DaNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">AngryTweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact match / F1-score">ScandiQA-da</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews correlation coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact match / F1-score">ScandiQA-no</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">ABSAbank-Imm</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact match / F1-score">ScandiQA-sv</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The version of the scandeval package used to benchmark">Version</span></th>
  </tr>
 </thead>
 <tbody>"""


HTML_END = """ </tbody>
</table>
</div>"""


ENTRY = """  <tr>
   <td>{}</td> <!-- Model ID -->
   <td class="num_parameters">{}</td> <!-- Number of trainable parameters -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">{}</td> <!-- DaNE -->
   <td class="da sent">{}</td> <!-- AngryTweets -->
   <td class="da la">{}</td> <!-- ScaLA-da -->
   <td class="da qa">{}</td> <!-- ScandiQA-da -->
   <td class="no ner">{}</td> <!-- NorNE -->
   <td class="no sent">{}</td> <!-- NoReC -->
   <td class="no la">{}</td> <!-- ScaLA-nb -->
   <td class="no la">{}</td> <!-- ScaLA-nn -->
   <td class="no qa">{}</td> <!-- ScandiQA-no -->
   <td class="sv ner">{}</td> <!-- SUC3 -->
   <td class="sv sent">{}</td> <!-- ABSAbank-Imm -->
   <td class="sv la">{}</td> <!-- ScaLA-sv -->
   <td class="sv qa">{}</td> <!-- ScandiQA-sv -->
  </tr>"""


# Set up primary/secondary metrics
PRIMARY_METRICS = ["mcc", "em", "micro_f1"]
SECONDARY_METRICS = ["macro_f1", "f1", "micro_f1_no_misc"]


def main() -> None:
    """Generate the leaderboard."""

    # Create path to the leaderboard, and ensure that it exists
    leaderboard_path = Path("leaderboard.md")
    leaderboard_path.parent.mkdir(exist_ok=True, parents=True)
    leaderboard_path.touch(exist_ok=True)

    # Create path to the scores JSONL file, and raise error if it doesn't exist
    scores_path = Path("scandeval_benchmark_results.jsonl")
    if not scores_path.exists():
        raise ValueError(f"Could not find {scores_path!r}")

    # Load in scores
    with scores_path.open() as f:
        scores = [json.loads(line) for line in f if line.strip()]

    # Reorganize the scores by each model
    model_scores: Dict[str, Dict[str, str]] = defaultdict(dict)
    for record in scores:
        model_id: str = record["model"]
        num_model_parameters: int = record["num_model_parameters"]
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
            raise ValueError(
                f"Found a model ({model_id}) that is not defined for one language: "
                f"{languages}"
            )

        # Extract shorthand notation for the task
        if task == "sentiment-classification":
            task_shorthand = "sent"
        elif task == "named-entity-recognition":
            task_shorthand = "ner"
        elif task == "linguistic-acceptability":
            task_shorthand = "la"
        elif task == "question-answering":
            task_shorthand = "qa"
        else:
            raise ValueError(f"Found invalid task: {task!r}")

        # Add the metrics to the model's score dict
        model_scores[model_id][f"{language} {task_shorthand}"] = score_str

        # Add the number of model parameters to the model's score dict, if it hasn't
        # previously been entered
        if "num_parameters" not in model_scores[model_id]:
            model_scores[model_id]["num_parameters"] = f"{num_model_parameters:,}"

    # Generate leaderboard HTML
    html_lines = [HTML_START]
    for model_id, model_dict in model_scores.items():
        values = [
            model_id,
            model_dict["num_parameters"],
            model_dict.get("da ner", ""),
            model_dict.get("da sent", ""),
            model_dict.get("da la", ""),
            model_dict.get("da qa", ""),
            model_dict.get("no ner", ""),
            model_dict.get("no sent", ""),
            model_dict.get("nb la", ""),
            model_dict.get("nn la", ""),
            model_dict.get("no qa", ""),
            model_dict.get("sv ner", ""),
            model_dict.get("sv sent", ""),
            model_dict.get("sv la", ""),
            model_dict.get("sv qa", ""),
        ]
        html_lines.append(ENTRY.format(*values))
    html_lines.append(HTML_END)
    html = "\n".join(html_lines)

    # Write table to the leaderboard file
    with leaderboard_path.open("w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
