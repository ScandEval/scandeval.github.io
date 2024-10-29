---
layout: page
mathjax: true
title: ScandEval
subtitle: A Natural Language Processing Benchmark
use-site-title: true
meta-description: A Multilingual Robust Natural Language Processing Benchmark
---
The `ScandEval` benchmark can be used to compare pretrained language models on tasks in
Danish, Swedish, Norwegian Bokmål, Norwegian Nynorsk, Icelandic, Faroese, German, Dutch
and English.

When evaluating language models we also split "Natural Language Processing" (NLP) into
two groups. "Natural Language Understanding" (NLU) is concerned with an analysis of
input text, and being able to extract insights from it. "Natural Language Generation"
(NLG) is about *generating* text in a coherent and human-like way. ScandEval has both
NLU and NLG leaderboards, which you can access in the top menu.

The NLU benchmarks evaluate the models on a variety of tasks: named entity recognition,
sentiment classification, linguistic acceptability and question answering. For encoder
(i.e., BERT-style) models, the scores are the the result of finetuning the models 10
times and evaluating each of these 10 finetuned models on a bootstrapped version of the
test set of the given dataset (different bootstrap for each of the 10 runs). The mean
of these 10 scores for the given (model, dataset) pair are then presented in the
leaderboard, with an associated 95% confidence interval. For decoder (i.e., GPT-style)
models, the models are evaluated using in-context learning with few-shot prompts. The
few-shot examples are sampled randomly from the training split, and we again benchmark
the models 10 times with bootstrapped test sets and different few-shot examples in each
iteration.

All benchmark results have been computed using the associated [ScandEval Python
package](https://github.com/ScandEval/ScandEval), which you can use to replicate the
results as well. The methodology of the benchmark can be found in the associated
research papers:

- [ScandEval: A Benchmark for Scandinavian Natural Language Processing](https://aclanthology.org/2023.nodalida-1.20/)
- [Encoder vs Decoder: Comparative Analysis of Encoder and Decoder Language Models on Multilingual NLU Tasks](https://doi.org/10.48550/arXiv.2406.13469)


## Frequently asked questions

### How do you determine if a model is "Commercial" or not? 
We generally determine this based on whether a model's license allows commercial use of the model. However if we are aware that a model is trained on data, that does not allow for commercial use, we will specify it as non-commercial model, despite the stated license. If you find an issue with any of models feel free to open an [issue](https://github.com/ScandEval/ScandEval/issues).

### Not finding the answer that you are looking for?
If don't find the answer that you are looking for feel free to ask your question in the [forum](https://github.com/ScandEval/ScandEval/discussions).
