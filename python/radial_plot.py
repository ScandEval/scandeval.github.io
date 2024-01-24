"""Script to produce radial plots."""

import plotly.graph_objects as go
import plotly
import json
from pathlib import Path
import numpy as np
from collections import defaultdict
import pandas as pd
import click
from pydantic import BaseModel


class Task(BaseModel):
    """Class to hold task information."""

    name: str
    metric: str

    def __hash__(self):
        return hash(self.name)


class Language(BaseModel):
    """Class to hold language information."""

    code: str
    name: str

    def __hash__(self):
        return hash(self.code)


class Dataset(BaseModel):
    """Class to hold dataset information."""

    name: str
    language: Language
    task: Task

    def __hash__(self):
        return hash(self.name)


TEXT_CLASSIFICATION = Task(name="text classification", metric="mcc")
INFORMATION_EXTRACTION = Task(name="information extraction", metric="micro_f1_no_misc")
GRAMMAR = Task(name="grammar", metric="mcc")
QUESTION_ANSWERING = Task(name="question answering", metric="em")
SUMMARISATION = Task(name="summarisation", metric="bertscore")
KNOWLEDGE = Task(name="knowledge", metric="mcc")
REASONING = Task(name="reasoning", metric="mcc")
ALL_TASKS = {obj.name: obj for obj in globals().values() if isinstance(obj, Task)}

DANISH = Language(code="da", name="Danish")
NORWEGIAN = Language(code="no", name="Norwegian")
SWEDISH = Language(code="sv", name="Swedish")
ICELANDIC = Language(code="is", name="Icelandic")
FAROESE = Language(code="fo", name="Faroese")
GERMAN = Language(code="de", name="German")
DUTCH = Language(code="nl", name="Dutch")
ENGLISH = Language(code="en", name="English")
ALL_LANGUAGES = {
    obj.code: obj for obj in globals().values() if isinstance(obj, Language)
}

DATASETS = [
    Dataset(name="swerec", language=SWEDISH, task=TEXT_CLASSIFICATION),
    Dataset(name="angry-tweets", language=DANISH, task=TEXT_CLASSIFICATION),
    Dataset(name="norec", language=NORWEGIAN, task=TEXT_CLASSIFICATION),
    Dataset(name="sb10k", language=GERMAN, task=TEXT_CLASSIFICATION),
    Dataset(name="dutch-social", language=DUTCH, task=TEXT_CLASSIFICATION),
    Dataset(name="sst5", language=ENGLISH, task=TEXT_CLASSIFICATION),
    Dataset(name="suc3", language=SWEDISH, task=INFORMATION_EXTRACTION),
    Dataset(name="dansk", language=DANISH, task=INFORMATION_EXTRACTION),
    Dataset(name="norne-nb", language=NORWEGIAN, task=INFORMATION_EXTRACTION),
    Dataset(name="norne-nn", language=NORWEGIAN, task=INFORMATION_EXTRACTION),
    Dataset(name="mim-gold-ner", language=ICELANDIC, task=INFORMATION_EXTRACTION),
    Dataset(name="fone", language=FAROESE, task=INFORMATION_EXTRACTION),
    Dataset(name="germeval", language=GERMAN, task=INFORMATION_EXTRACTION),
    Dataset(name="conll-nl", language=DUTCH, task=INFORMATION_EXTRACTION),
    Dataset(name="conll-en", language=ENGLISH, task=INFORMATION_EXTRACTION),
    Dataset(name="scala-sv", language=SWEDISH, task=GRAMMAR),
    Dataset(name="scala-da", language=DANISH, task=GRAMMAR),
    Dataset(name="scala-nb", language=NORWEGIAN, task=GRAMMAR),
    Dataset(name="scala-nn", language=NORWEGIAN, task=GRAMMAR),
    Dataset(name="scala-is", language=ICELANDIC, task=GRAMMAR),
    Dataset(name="scala-fo", language=FAROESE, task=GRAMMAR),
    Dataset(name="scala-de", language=GERMAN, task=GRAMMAR),
    Dataset(name="scala-nl", language=DUTCH, task=GRAMMAR),
    Dataset(name="scala-en", language=ENGLISH, task=GRAMMAR),
    Dataset(name="scandiqa-da", language=DANISH, task=QUESTION_ANSWERING),
    Dataset(name="norquad", language=NORWEGIAN, task=QUESTION_ANSWERING),
    Dataset(name="scandiqa-sv", language=SWEDISH, task=QUESTION_ANSWERING),
    Dataset(name="nqii", language=ICELANDIC, task=QUESTION_ANSWERING),
    Dataset(name="germanquad", language=GERMAN, task=QUESTION_ANSWERING),
    Dataset(name="squad", language=ENGLISH, task=QUESTION_ANSWERING),
    Dataset(name="squad-nl", language=DUTCH, task=QUESTION_ANSWERING),
    Dataset(name="nordjylland-news", language=DANISH, task=SUMMARISATION),
    Dataset(name="mlsum", language=GERMAN, task=SUMMARISATION),
    Dataset(name="rrn", language=ICELANDIC, task=SUMMARISATION),
    Dataset(name="no-sammendrag", language=NORWEGIAN, task=SUMMARISATION),
    Dataset(name="wiki-lingua-nl", language=DUTCH, task=SUMMARISATION),
    Dataset(name="swedn", language=SWEDISH, task=SUMMARISATION),
    Dataset(name="cnn-dailymail", language=ENGLISH, task=SUMMARISATION),
    Dataset(name="mmlu-da", language=DANISH, task=KNOWLEDGE),
    Dataset(name="mmlu-no", language=NORWEGIAN, task=KNOWLEDGE),
    Dataset(name="mmlu-sv", language=SWEDISH, task=KNOWLEDGE),
    Dataset(name="mmlu-is", language=ICELANDIC, task=KNOWLEDGE),
    Dataset(name="mmlu-de", language=GERMAN, task=KNOWLEDGE),
    Dataset(name="mmlu-nl", language=DUTCH, task=KNOWLEDGE),
    Dataset(name="mmlu", language=ENGLISH, task=KNOWLEDGE),
    Dataset(name="arc-da", language=DANISH, task=KNOWLEDGE),
    Dataset(name="arc-no", language=NORWEGIAN, task=KNOWLEDGE),
    Dataset(name="arc-sv", language=SWEDISH, task=KNOWLEDGE),
    Dataset(name="arc-is", language=ICELANDIC, task=KNOWLEDGE),
    Dataset(name="arc-de", language=GERMAN, task=KNOWLEDGE),
    Dataset(name="arc-nl", language=DUTCH, task=KNOWLEDGE),
    Dataset(name="arc", language=ENGLISH, task=KNOWLEDGE),
    Dataset(name="hellaswag-da", language=DANISH, task=REASONING),
    Dataset(name="hellaswag-no", language=NORWEGIAN, task=REASONING),
    Dataset(name="hellaswag-sv", language=SWEDISH, task=REASONING),
    Dataset(name="hellaswag-is", language=ICELANDIC, task=REASONING),
    Dataset(name="hellaswag-de", language=GERMAN, task=REASONING),
    Dataset(name="hellaswag-nl", language=DUTCH, task=REASONING),
    Dataset(name="hellaswag", language=ENGLISH, task=REASONING),
]


@click.command()
@click.option(
    "--model",
    "-m",
    multiple=True,
    required=True,
    help="Model to plot.",
)
@click.option(
    "--task",
    "-t",
    multiple=True,
    help="Task to plot. If not specified, all tasks will be plotted.",
)
@click.option(
    "--language",
    "-l",
    multiple=True,
    required=True,
    help="The language of the datasets to plot.",
)
@click.option(
    "--use-win-ratio/--use-score",
    default=True,
    help="Whether to use the win ratio or the score.",
)
def main(model, task, language, use_win_ratio) -> None:
    """Produce a radial plot.

    Args:
        model:
            The models to plot.
        task:
            The tasks to plot.
        language:
            The languages to plot.
        use_win_ratio:
            Whether to use the win ratio or the score as the radial axis.
    """
    # Rename the variables to plural
    model_ids = model
    tasks = [ALL_TASKS[task] for task in task]
    languages = [ALL_LANGUAGES[lang] for lang in language]

    with Path('scandeval_benchmark_results.jsonl').open() as f:
        records = [json.loads(dct_str) for dct_str in f if dct_str.strip("\n")]

    # Build a dictionary of languages -> results-dataframes, whose indices are the
    # models and columns are the tasks.
    results_dfs = dict()
    for language in {dataset.language for dataset in DATASETS}:
        possible_dataset_names = {
            dataset.name
            for dataset in DATASETS
            if dataset.language == language
        }
        data_dict = defaultdict(dict)
        for record in records:
            model_name = record["model"]
            dataset_name = record["dataset"]
            if dataset_name in possible_dataset_names:
                dataset = next(
                    dataset for dataset in DATASETS if dataset.name == dataset_name
                )
                results_dict = record['results']['total']
                score = results_dict.get(
                    f"test_{dataset.task.metric}", results_dict.get(dataset.task.metric)
                )
                if dataset.task in data_dict[model_name]:
                    data_dict[model_name][dataset.task].append(score)
                else:
                    data_dict[model_name][dataset.task] = [score]
        results_df = pd.DataFrame(data_dict).T.map(
            lambda list_or_nan:
            np.mean(list_or_nan) if list_or_nan == list_or_nan else list_or_nan
        )
        results_dfs[language] = results_df

    if not tasks:
        tasks = list({dataset.task for dataset in DATASETS})
        for model_id in model_ids:
            dfs_with_results = {
                language: results_df
                for language, results_df in results_dfs.items()
                if model_id in results_df.index
                and language in languages
            }
            if not dfs_with_results:
                raise ValueError(f"Model {model_id!r} has not been evaluated yet!")
            for language, results_df in dfs_with_results.items():
                tasks = list(
                    set(tasks).intersection(
                        results_df.loc[model_id].dropna().index.tolist()
                    )
                )

    results_dfs_filtered = {
        language: df[tasks].dropna()
        for language, df in results_dfs.items()
        if language in languages
    }

    # Add all the evaluation results for each model
    results: list[list[float]] = list()
    for model_id in model_ids:
        result_list = list()
        for task in tasks:
            win_ratios = list()
            scores = list()
            for language in languages:
                score = results_dfs_filtered[language].loc[model_id][task]
                win_ratio = np.mean([
                    score >= other_score
                    for other_score in results_dfs_filtered[language][task].dropna()
                ])
                win_ratios.append(win_ratio)
                scores.append(score)
            if use_win_ratio:
                result_list.append(np.mean(win_ratios))
            else:
                result_list.append(np.mean(scores))
        results.append(result_list)

    # Sort the results to avoid misleading radial plots
    model_idx_with_highest_variance = np.argmax(
        [np.std(result_list) for result_list in results]
    )
    sorted_idxs = np.argsort(results[model_idx_with_highest_variance])
    results = [np.asarray(result_list)[sorted_idxs] for result_list in results]
    tasks = np.asarray(tasks)[sorted_idxs]

    # Add the results to a plotly figure
    fig = go.Figure()
    for model_id, result_list in zip(model_ids, results):
        fig.add_trace(go.Scatterpolar(
            r=result_list,
            theta=[task.name for task in tasks],
            fill='toself',
            name=model_id,
        ))

    languages_str = ""
    if len(languages) > 1:
        languages_str = ", ".join([language.name for language in languages[:-1]])
        languages_str += " and "
    languages_str += languages[-1].name

    if use_win_ratio:
        title = f'Win Ratio on on {languages_str} Language Tasks'
    else:
        title = f'LLM Score on on {languages_str} Language Tasks'

    # Builds the radial plot from the results
    margin = plotly.graph_objects.layout.Margin(l=200, r=200)
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=True,
        width=1000,
        height=500,
        margin=margin,
        title=title,
    )

    fig.show()

if __name__ == "__main__":
    main()
