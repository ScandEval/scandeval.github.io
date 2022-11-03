---
layout: page
mathjax: true
title: ScandEval
subtitle: A Scandinavian Natural Language Understanding Benchmark
use-site-title: true
meta-description: ScandEval Benchmark of language models on Scandinavian language tasks
---
The `ScandEval` benchmark can be used to compare pretrained language models on
Scandinavian language tasks. The benchmark evaluates the models on a variety of tasks:
named entity recognition, sentiment classification, linguistic acceptability and
question answering. By "Scandinavian" we here mean Danish, Swedish and Norwegian (both
Bokmål and Nynorsk).

The [Leaderboard](https://scandeval.github.io/language-model-benchmark/) contains
the result of finetuning the language model 10 times, and evaluating each of
these 10 finetuned models on the test set of the given dataset along with 9
bootstrapped versions of the dataset. The mean of the resulting 100 scores for
the given (model, dataset) pair are then presented in the leaderboard, with an
associated 95% confidence interval.

All benchmark results have been computed using the associated
[ScandEval Python package](https://github.com/saattrupdan/ScandEval), which you
can use to replicate the results as well. A paper on the package and
leaderboards is in preparation, describing the methodology and all the datasets
used in more depth.
