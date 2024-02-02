---
layout: leaderboard
title: German NLG
---

<center>Last updated: 02/02/2024 07:43:07 CET</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="german-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German summarization - BERTScore / ROUGE-L">MLSum</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">ARC-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-de</span></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td class="rank">1</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">51.56 ± 2.47</td> <!-- ScandEval score -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">64.90 ± 0.22 / 15.99 ± 0.32</td> <!-- MLSum -->
   <td class="de know">35.39 ± 3.89 / 51.41 ± 2.98</td> <!-- MMLU-de -->
   <td class="de know">70.58 ± 2.18 / 77.93 ± 1.65</td> <!-- ARC-de -->
   <td class="de reason">56.88 ± 2.50 / 66.76 ± 2.02</td> <!-- HellaSwag-de -->
  </tr>
  <tr>
   <td class="rank">2</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,065 ± 472 / 1,055 ± 321</td> <!-- Model inference speed -->
   <td class="score">47.61 ± 1.42</td> <!-- ScandEval score -->
   <td class="de ner">62.22 ± 1.13 / 51.16 ± 2.01</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.35 / 68.95 ± 1.08</td> <!-- SB10k -->
   <td class="de la">27.88 ± 1.38 / 63.49 ± 0.77</td> <!-- ScaLA-de -->
   <td class="de qa">19.43 ± 2.78 / 57.12 ± 2.32</td> <!-- GermanQuAD -->
   <td class="de summ">68.18 ± 0.98 / 26.38 ± 2.97</td> <!-- MLSum -->
   <td class="de know">34.58 ± 0.67 / 50.63 ± 0.54</td> <!-- MMLU-de -->
   <td class="de know">63.00 ± 1.09 / 72.26 ± 0.82</td> <!-- ARC-de -->
   <td class="de reason">52.33 ± 1.44 / 63.96 ± 1.15</td> <!-- HellaSwag-de -->
  </tr>
  <tr>
   <td class="rank">3</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">42.69 ± 2.01</td> <!-- ScandEval score -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">22.94 ± 3.05 / 47.19 ± 4.45</td> <!-- GermanQuAD -->
   <td class="de summ">68.72 ± 0.87 / 28.11 ± 2.14</td> <!-- MLSum -->
   <td class="de know">35.63 ± 1.12 / 51.69 ± 0.85</td> <!-- MMLU-de -->
   <td class="de know">60.46 ± 1.23 / 70.30 ± 0.94</td> <!-- ARC-de -->
   <td class="de reason">26.40 ± 1.86 / 43.98 ± 1.58</td> <!-- HellaSwag-de -->
  </tr>
  <tr>
   <td class="rank">4</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">32.23 ± 1.99</td> <!-- ScandEval score -->
   <td class="de ner">41.88 ± 1.87 / 31.88 ± 1.77</td> <!-- GermEval -->
   <td class="de sent">50.17 ± 2.52 / 65.78 ± 1.89</td> <!-- SB10k -->
   <td class="de la">15.82 ± 2.45 / 53.27 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">18.35 ± 2.70 / 39.71 ± 4.79</td> <!-- GermanQuAD -->
   <td class="de summ">68.99 ± 1.06 / 28.97 ± 2.45</td> <!-- MLSum -->
   <td class="de know">18.43 ± 1.34 / 38.16 ± 1.18</td> <!-- MMLU-de -->
   <td class="de know">25.68 ± 1.63 / 43.75 ± 1.33</td> <!-- ARC-de -->
   <td class="de reason">8.37 ± 1.83 / 30.00 ± 1.48</td> <!-- HellaSwag-de -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlg.csv" target="_blank">Download as CSV</a>
</div>