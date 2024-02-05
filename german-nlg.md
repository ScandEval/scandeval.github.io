---
layout: leaderboard
title: German NLG
---

<center>Last updated: 05/02/2024 17:05:51 CET</center>

<div class="small-font">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

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
  <tr class="not-merged-model">
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
  <tr class="not-merged-model">
   <td class="rank">2</td> <!-- Rank -->
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
  <tr class="not-merged-model">
   <td class="rank">3</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">38.53 ± 1.91</td> <!-- ScandEval score -->
   <td class="de ner">51.79 ± 0.92 / 36.09 ± 1.73</td> <!-- GermEval -->
   <td class="de sent">47.27 ± 3.06 / 63.50 ± 2.88</td> <!-- SB10k -->
   <td class="de la">22.15 ± 1.83 / 56.64 ± 4.04</td> <!-- ScaLA-de -->
   <td class="de qa">24.30 ± 3.79 / 54.51 ± 4.48</td> <!-- GermanQuAD -->
   <td class="de summ">67.96 ± 1.05 / 26.56 ± 2.90</td> <!-- MLSum -->
   <td class="de know">26.88 ± 0.94 / 44.64 ± 0.79</td> <!-- MMLU-de -->
   <td class="de know">44.97 ± 1.73 / 58.53 ± 1.31</td> <!-- ARC-de -->
   <td class="de reason">20.34 ± 1.39 / 39.65 ± 0.94</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">34.81 ± 1.88</td> <!-- ScandEval score -->
   <td class="de ner">50.00 ± 1.33 / 38.45 ± 1.68</td> <!-- GermEval -->
   <td class="de sent">46.54 ± 2.92 / 63.66 ± 2.14</td> <!-- SB10k -->
   <td class="de la">15.30 ± 1.79 / 55.12 ± 1.92</td> <!-- ScaLA-de -->
   <td class="de qa">25.57 ± 3.57 / 56.05 ± 3.74</td> <!-- GermanQuAD -->
   <td class="de summ">67.66 ± 0.90 / 23.98 ± 2.48</td> <!-- MLSum -->
   <td class="de know">20.13 ± 1.16 / 39.49 ± 1.04</td> <!-- MMLU-de -->
   <td class="de know">29.29 ± 1.06 / 46.55 ± 0.89</td> <!-- ARC-de -->
   <td class="de reason">13.92 ± 1.52 / 34.03 ± 1.27</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">32.26 ± 2.33</td> <!-- ScandEval score -->
   <td class="de ner">39.09 ± 2.92 / 31.71 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">47.83 ± 2.81 / 60.24 ± 3.30</td> <!-- SB10k -->
   <td class="de la">10.31 ± 2.60 / 46.65 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">26.13 ± 3.79 / 53.13 ± 4.50</td> <!-- GermanQuAD -->
   <td class="de summ">66.72 ± 1.03 / 23.80 ± 2.02</td> <!-- MLSum -->
   <td class="de know">19.03 ± 1.31 / 36.85 ± 1.79</td> <!-- MMLU-de -->
   <td class="de know">32.26 ± 1.36 / 47.72 ± 1.23</td> <!-- ARC-de -->
   <td class="de reason">10.10 ± 1.81 / 30.36 ± 1.81</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5</td> <!-- Rank -->
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
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">20.36 ± 1.91</td> <!-- ScandEval score -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.54 ± 5.12 / 49.63 ± 5.78</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.40 ± 3.28 / 45.47 ± 3.32</td> <!-- GermanQuAD -->
   <td class="de summ">62.18 ± 0.62 / 16.27 ± 1.10</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de know">-0.37 ± 1.14 / 24.56 ± 0.85</td> <!-- ARC-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">4.68 ± 0.67</td> <!-- ScandEval score -->
   <td class="de ner">0.30 ± 0.60 / 0.26 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">0.03 ± 0.44 / 17.26 ± 0.45</td> <!-- SB10k -->
   <td class="de la">0.72 ± 1.40 / 42.53 ± 3.84</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.54 ± 0.12</td> <!-- GermanQuAD -->
   <td class="de summ">30.97 ± 0.49 / 1.94 ± 0.26</td> <!-- MLSum -->
   <td class="de know">-0.35 ± 0.95 / 22.36 ± 0.43</td> <!-- MMLU-de -->
   <td class="de know">0.57 ± 0.90 / 23.42 ± 0.90</td> <!-- ARC-de -->
   <td class="de reason">0.64 ± 0.82 / 24.19 ± 0.54</td> <!-- HellaSwag-de -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlg.csv" target="_blank">Download as CSV</a>
</div>