---
layout: leaderboard
title: Insular Scandinavian NLG
---

<center>Last updated: 05/02/2024 11:05:01 CET</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="insular-scandinavian-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Icelandic score">IS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Faroese score">FO</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">ARC-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-is</span></th>
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
   <td class="score">39.20 ± 3.36</td> <!-- ScandEval score -->
   <td class="is-score">38.01 ± 2.57</td> <!-- Icelandic score -->
   <td class="fo-score">40.39 ± 4.16</td> <!-- Faroese score -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">23.78 ± 2.81 / 42.70 ± 2.13</td> <!-- MMLU-is -->
   <td class="is know">37.79 ± 1.33 / 53.01 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">24.78 ± 2.63 / 42.97 ± 1.94</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,065 ± 472 / 1,055 ± 321</td> <!-- Model inference speed -->
   <td class="score">30.46 ± 1.82</td> <!-- ScandEval score -->
   <td class="is-score">26.68 ± 1.51</td> <!-- Icelandic score -->
   <td class="fo-score">34.23 ± 2.12</td> <!-- Faroese score -->
   <td class="is ner">50.02 ± 1.71 / 41.97 ± 3.98</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.18 ± 1.24 / 50.43 ± 1.44</td> <!-- ScaLA-is -->
   <td class="is qa">22.23 ± 3.29 / 53.90 ± 3.08</td> <!-- NQiI -->
   <td class="fo ner">64.44 ± 2.40 / 60.87 ± 2.59</td> <!-- FoNE -->
   <td class="fo la">4.03 ± 1.85 / 48.93 ± 3.63</td> <!-- ScaLA-fo -->
   <td class="is summ">65.66 ± 0.53 / 19.57 ± 0.74</td> <!-- RRN -->
   <td class="is know">9.65 ± 1.00 / 32.00 ± 0.89</td> <!-- MMLU-is -->
   <td class="is know">7.39 ± 1.65 / 30.33 ± 1.19</td> <!-- ARC-is -->
   <td class="is reason">9.45 ± 0.95 / 31.81 ± 0.74</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">29.29 ± 2.38</td> <!-- ScandEval score -->
   <td class="is-score">25.84 ± 2.12</td> <!-- Icelandic score -->
   <td class="fo-score">32.73 ± 2.64</td> <!-- Faroese score -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td class="is summ">64.81 ± 1.16 / 19.31 ± 0.91</td> <!-- RRN -->
   <td class="is know">10.31 ± 1.06 / 32.74 ± 0.64</td> <!-- MMLU-is -->
   <td class="is know">7.36 ± 1.18 / 30.77 ± 0.78</td> <!-- ARC-is -->
   <td class="is reason">6.55 ± 1.30 / 29.83 ± 1.01</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">25.19 ± 2.15</td> <!-- ScandEval score -->
   <td class="is-score">20.76 ± 1.80</td> <!-- Icelandic score -->
   <td class="fo-score">29.62 ± 2.50</td> <!-- Faroese score -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.12 ± 2.50 / 39.44 ± 1.99</td> <!-- NQiI -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td class="is summ">64.14 ± 0.87 / 16.89 ± 1.86</td> <!-- RRN -->
   <td class="is know">3.27 ± 0.84 / 26.91 ± 0.86</td> <!-- MMLU-is -->
   <td class="is know">2.13 ± 1.49 / 27.86 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">1.54 ± 0.83 / 26.63 ± 0.65</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">24.66 ± 2.06</td> <!-- ScandEval score -->
   <td class="is-score">21.06 ± 1.86</td> <!-- Icelandic score -->
   <td class="fo-score">28.27 ± 2.27</td> <!-- Faroese score -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">17.92 ± 3.21 / 42.41 ± 2.86</td> <!-- NQiI -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="is summ">63.83 ± 1.29 / 17.92 ± 1.27</td> <!-- RRN -->
   <td class="is know">7.22 ± 1.33 / 29.40 ± 1.04</td> <!-- MMLU-is -->
   <td class="is know">4.34 ± 1.43 / 27.42 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">3.12 ± 1.36 / 27.42 ± 0.86</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">23.21 ± 2.63</td> <!-- ScandEval score -->
   <td class="is-score">20.20 ± 1.98</td> <!-- Icelandic score -->
   <td class="fo-score">26.23 ± 3.28</td> <!-- Faroese score -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.31 ± 3.62 / 40.78 ± 4.26</td> <!-- NQiI -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td class="is summ">64.30 ± 1.22 / 19.07 ± 1.13</td> <!-- RRN -->
   <td class="is know">5.05 ± 1.56 / 28.95 ± 1.00</td> <!-- MMLU-is -->
   <td class="is know">3.84 ± 1.07 / 25.73 ± 1.14</td> <!-- ARC-is -->
   <td class="is reason">0.80 ± 1.18 / 25.46 ± 0.72</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">22.03 ± 1.91</td> <!-- ScandEval score -->
   <td class="is-score">16.97 ± 1.74</td> <!-- Icelandic score -->
   <td class="fo-score">27.09 ± 2.08</td> <!-- Faroese score -->
   <td class="is ner">22.55 ± 3.91 / 22.44 ± 3.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.44 ± 0.79 / 33.03 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is qa">11.98 ± 2.87 / 33.09 ± 1.83</td> <!-- NQiI -->
   <td class="fo ner">54.17 ± 4.15 / 54.25 ± 4.13</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="is summ">65.35 ± 0.78 / 19.71 ± 0.93</td> <!-- RRN -->
   <td class="is know">2.15 ± 0.98 / 24.92 ± 0.93</td> <!-- MMLU-is -->
   <td class="is know">1.99 ± 1.11 / 25.64 ± 0.71</td> <!-- ARC-is -->
   <td class="is reason">0.34 ± 1.06 / 25.83 ± 0.66</td> <!-- HellaSwag-is -->
  </tr>
  <tr>
   <td class="rank">4</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">2.45 ± 0.19</td> <!-- ScandEval score -->
   <td class="is-score">4.90 ± 0.38</td> <!-- Icelandic score -->
   <td class="fo-score">0.00 ± 0.00</td> <!-- Faroese score -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="is summ">30.20 ± 0.17 / 2.36 ± 0.06</td> <!-- RRN -->
   <td class="is know">0.85 ± 0.83 / 22.51 ± 0.58</td> <!-- MMLU-is -->
   <td class="is know">-1.13 ± 0.89 / 22.53 ± 0.61</td> <!-- ARC-is -->
   <td class="is reason">-0.67 ± 1.27 / 24.79 ± 0.84</td> <!-- HellaSwag-is -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>