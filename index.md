---
layout: page
mathjax: true
title: ScandEval
subtitle: A Scandinavian Natural Language Understanding Benchmark
use-site-title: true
meta-description: ScandEval Benchmark of language models on Scandinavian language tasks
---
The `ScandEval` benchmark can be used to compare both pretrained language
models on Scandinavian language tasks, as well as comparing finetuned models on
the tasks they were finetuned for.

The [Pretrained Benchmark](https://scandeval.github.io/pretrained/) contains
the result of finetuning the language model 10 times, and evaluating each of
these 10 finetuned models on the test set of the given dataset along with 9
bootstrapped versions of the dataset. The mean of the resulting 100 scores for
the given (model, dataset) pair are then presented in the leaderboard, with an
associated 95% confidence interval.

The [Finetuned Benchmark](https://scandeval.github.io/finetuned/) is computed
in the sammer manner, except that we have not finetuned the models in question,
but solely evaluated the finetuned model on the test set and 9 bootstrapped
versions of the test set. The resulting 95% confidence interval will thus be
wider than the pretrained benchmark results, as we have to take the variability
of the initialised parameters of the model into account.

All benchmark results have been computed using the associated
[ScandEval](https://github.com/saattrupdan/ScandEval) Python package, which you
can use to replicate the results as well. A paper on the package and
leaderboards is in preparation, describing the methodology and all the datasets
used in more depth.
