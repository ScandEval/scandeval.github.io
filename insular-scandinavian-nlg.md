---
layout: leaderboard
title: Insular Scandinavian NLG
---

<center>Last updated: 08/04/2024 20:04:28 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="insular-scandinavian-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic rank, computed as 1 + the average number of standard deviations from the best model">Icelandic Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese rank, computed as 1 + the average number of standard deviations from the best model">Faroese Rank</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">Winogrande-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on RRN">RRN version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-is">MMLU-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Winogrande-is">Winogrande-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoNE">FoNE version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-fo">ScaLA-fo version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model-->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.00</td> <!-- ScandEval rank -->
   <td class="is-rank">1.00</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.00</td> <!-- Faroese rank -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">52.13 ± 4.37 / 71.97 ± 3.44</td> <!-- ScaLA-is -->
   <td class="is qa">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">69.61 ± 0.61 / 23.98 ± 1.17</td> <!-- RRN -->
   <td class="is know">68.38 ± 2.60 / 76.29 ± 1.93</td> <!-- MMLU-is -->
   <td class="is reason">74.78 ± 4.30 / 87.50 ± 2.14</td> <!-- Winogrande-is -->
   <td class="fo ner">86.51 ± 2.01 / 85.01 ± 2.45</td> <!-- FoNE -->
   <td class="fo la">35.09 ± 5.70 / 65.72 ± 3.27</td> <!-- ScaLA-fo -->
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.1</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.5.1</td> <!-- RRN version -->
   <td>12.5.1</td> <!-- MMLU-is version -->
   <td>12.5.1</td> <!-- Winogrande-is version -->
   <td>12.5.1</td> <!-- FoNE version -->
   <td>12.5.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="is-rank">3.53</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.51</td> <!-- Faroese rank -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">23.78 ± 2.81 / 42.70 ± 2.13</td> <!-- MMLU-is -->
   <td class="is reason">18.61 ± 6.00 / 61.33 ± 2.93</td> <!-- Winogrande-is -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- RRN version -->
   <td>0.0.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">3.89</td> <!-- ScandEval rank -->
   <td class="is-rank">4.09</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.69</td> <!-- Faroese rank -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.42 ± 4.37 / 55.49 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">10.13 ± 2.94 / 32.62 ± 2.20</td> <!-- MMLU-is -->
   <td class="is reason">12.90 ± 6.92 / 56.88 ± 3.57</td> <!-- Winogrande-is -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.2</td> <!-- ScaLA-is version -->
   <td>9.3.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- RRN version -->
   <td>9.3.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>9.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="is-rank">4.17</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.69</td> <!-- Faroese rank -->
   <td class="is ner">50.82 ± 2.72 / 40.35 ± 4.51</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.99 ± 1.54 / 39.38 ± 3.81</td> <!-- ScaLA-is -->
   <td class="is qa">25.74 ± 5.44 / 49.45 ± 5.29</td> <!-- NQiI -->
   <td class="is summ">61.72 ± 3.16 / 16.00 ± 1.82</td> <!-- RRN -->
   <td class="is know">10.43 ± 1.25 / 32.96 ± 0.81</td> <!-- MMLU-is -->
   <td class="is reason">3.94 ± 2.97 / 54.60 ± 1.62</td> <!-- Winogrande-is -->
   <td class="fo ner">62.82 ± 3.50 / 58.05 ± 3.79</td> <!-- FoNE -->
   <td class="fo la">4.96 ± 2.36 / 43.40 ± 4.95</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="is-rank">4.23</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.69</td> <!-- Faroese rank -->
   <td class="is ner">50.85 ± 4.15 / 42.91 ± 5.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.80 ± 3.84 / 49.12 ± 2.51</td> <!-- ScaLA-is -->
   <td class="is qa">20.23 ± 3.73 / 52.99 ± 2.11</td> <!-- NQiI -->
   <td class="is summ">64.46 ± 1.03 / 17.62 ± 1.10</td> <!-- RRN -->
   <td class="is know">9.92 ± 2.10 / 32.19 ± 1.69</td> <!-- MMLU-is -->
   <td class="is reason">9.09 ± 6.37 / 49.53 ± 5.40</td> <!-- Winogrande-is -->
   <td class="fo ner">64.39 ± 3.14 / 59.80 ± 3.68</td> <!-- FoNE -->
   <td class="fo la">4.74 ± 4.59 / 48.96 ± 4.16</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">3.97</td> <!-- ScandEval rank -->
   <td class="is-rank">4.26</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.69</td> <!-- Faroese rank -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">25.70 ± 5.36 / 49.31 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.96 ± 3.10 / 16.11 ± 1.80</td> <!-- RRN -->
   <td class="is know">10.31 ± 1.06 / 32.74 ± 0.64</td> <!-- MMLU-is -->
   <td class="is reason">1.99 ± 2.95 / 54.48 ± 1.27</td> <!-- Winogrande-is -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td>9.1.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.1.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>9.1.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.1.2</td> <!-- FoNE version -->
   <td>9.1.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="is-rank">4.15</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.31</td> <!-- Faroese rank -->
   <td class="is ner">50.64 ± 5.79 / 43.64 ± 5.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.06 ± 3.83 / 38.01 ± 2.85</td> <!-- ScaLA-is -->
   <td class="is qa">23.36 ± 4.19 / 46.70 ± 2.79</td> <!-- NQiI -->
   <td class="is summ">63.80 ± 1.14 / 15.18 ± 1.69</td> <!-- RRN -->
   <td class="is know">9.94 ± 2.33 / 31.91 ± 2.10</td> <!-- MMLU-is -->
   <td class="is reason">15.83 ± 5.74 / 53.67 ± 3.46</td> <!-- Winogrande-is -->
   <td class="fo ner">60.21 ± 3.50 / 58.44 ± 3.67</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.10 ± 0.80</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">4.26</td> <!-- ScandEval rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.22</td> <!-- Faroese rank -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is qa">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.01 ± 1.51 / 18.34 ± 1.35</td> <!-- RRN -->
   <td class="is know">7.55 ± 0.67 / 29.89 ± 0.47</td> <!-- MMLU-is -->
   <td class="is reason">0.24 ± 0.71 / 38.95 ± 0.84</td> <!-- Winogrande-is -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="is-rank">4.39</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.22</td> <!-- Faroese rank -->
   <td class="is ner">36.79 ± 8.13 / 30.81 ± 7.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is qa">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="is summ">65.25 ± 0.97 / 19.09 ± 1.05</td> <!-- RRN -->
   <td class="is know">8.10 ± 0.93 / 29.90 ± 0.88</td> <!-- MMLU-is -->
   <td class="is reason">0.35 ± 2.49 / 51.16 ± 2.74</td> <!-- Winogrande-is -->
   <td class="fo ner">61.90 ± 2.44 / 61.08 ± 2.76</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.3.1</td> <!-- MMLU-is version -->
   <td>12.3.1</td> <!-- Winogrande-is version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">4.41</td> <!-- ScandEval rank -->
   <td class="is-rank">4.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.31</td> <!-- Faroese rank -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="is summ">62.55 ± 3.03 / 15.26 ± 2.31</td> <!-- RRN -->
   <td class="is know">7.64 ± 0.91 / 29.55 ± 1.22</td> <!-- MMLU-is -->
   <td class="is reason">-0.51 ± 1.95 / 47.23 ± 2.39</td> <!-- Winogrande-is -->
   <td class="fo ner">58.67 ± 3.95 / 58.47 ± 3.96</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.2.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">4.47</td> <!-- ScandEval rank -->
   <td class="is-rank">4.53</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.42</td> <!-- Faroese rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">62.80 ± 1.69 / 15.23 ± 1.01</td> <!-- RRN -->
   <td class="is know">7.22 ± 1.33 / 29.40 ± 1.04</td> <!-- MMLU-is -->
   <td class="is reason">6.35 ± 2.71 / 50.49 ± 1.57</td> <!-- Winogrande-is -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.53</td> <!-- ScandEval rank -->
   <td class="is-rank">4.63</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.42</td> <!-- Faroese rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">5.05 ± 1.56 / 28.95 ± 1.00</td> <!-- MMLU-is -->
   <td class="is reason">-0.00 ± 2.41 / 44.93 ± 0.92</td> <!-- Winogrande-is -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>9.2.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.2.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="is-rank">4.69</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.42</td> <!-- Faroese rank -->
   <td class="is ner">34.62 ± 4.64 / 33.25 ± 4.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.24 ± 1.43 / 33.75 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is qa">18.10 ± 1.85 / 43.52 ± 0.87</td> <!-- NQiI -->
   <td class="is summ">61.81 ± 0.98 / 15.04 ± 0.70</td> <!-- RRN -->
   <td class="is know">6.52 ± 1.10 / 30.08 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">-1.90 ± 2.28 / 44.34 ± 1.19</td> <!-- Winogrande-is -->
   <td class="fo ner">53.38 ± 3.96 / 53.04 ± 3.85</td> <!-- FoNE -->
   <td class="fo la">0.46 ± 2.01 / 44.83 ± 3.28</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">4.57</td> <!-- ScandEval rank -->
   <td class="is-rank">4.65</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.48</td> <!-- Faroese rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">62.30 ± 0.90 / 13.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.27 ± 0.84 / 26.91 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">1.84 ± 2.19 / 43.79 ± 0.73</td> <!-- Winogrande-is -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">4.68</td> <!-- ScandEval rank -->
   <td class="is-rank">4.77</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.59</td> <!-- Faroese rank -->
   <td class="is ner">34.76 ± 4.42 / 23.42 ± 2.33</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.77 ± 1.05 / 39.63 ± 2.41</td> <!-- ScaLA-is -->
   <td class="is qa">12.80 ± 2.37 / 30.77 ± 2.12</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 1.78 / 15.53 ± 0.95</td> <!-- RRN -->
   <td class="is know">0.93 ± 1.13 / 25.19 ± 0.78</td> <!-- MMLU-is -->
   <td class="is reason">-0.76 ± 3.69 / 53.64 ± 2.57</td> <!-- Winogrande-is -->
   <td class="fo ner">53.24 ± 2.75 / 50.65 ± 2.85</td> <!-- FoNE -->
   <td class="fo la">-0.52 ± 1.71 / 42.25 ± 3.52</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,480 ± 727 / 822 ± 274</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="is-rank">4.80</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.85</td> <!-- Faroese rank -->
   <td class="is ner">20.51 ± 3.13 / 20.32 ± 2.89</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.12 ± 1.87 / 46.10 ± 3.55</td> <!-- ScaLA-is -->
   <td class="is qa">21.85 ± 3.13 / 45.40 ± 2.16</td> <!-- NQiI -->
   <td class="is summ">59.41 ± 2.83 / 10.57 ± 1.68</td> <!-- RRN -->
   <td class="is know">-0.48 ± 0.57 / 22.75 ± 0.82</td> <!-- MMLU-is -->
   <td class="is reason">0.06 ± 2.69 / 44.46 ± 1.65</td> <!-- Winogrande-is -->
   <td class="fo ner">43.11 ± 3.04 / 43.01 ± 2.90</td> <!-- FoNE -->
   <td class="fo la">-0.26 ± 1.84 / 45.69 ± 3.07</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="is-rank">4.84</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.85</td> <!-- Faroese rank -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is qa">14.55 ± 2.68 / 32.34 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">62.11 ± 2.22 / 14.98 ± 1.53</td> <!-- RRN -->
   <td class="is know">6.32 ± 1.09 / 29.87 ± 0.80</td> <!-- MMLU-is -->
   <td class="is reason">-1.89 ± 2.66 / 43.72 ± 0.92</td> <!-- Winogrande-is -->
   <td class="fo ner">43.80 ± 4.46 / 44.36 ± 3.59</td> <!-- FoNE -->
   <td class="fo la">-0.42 ± 2.18 / 34.33 ± 1.47</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">4.88</td> <!-- ScandEval rank -->
   <td class="is-rank">5.08</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.68</td> <!-- Faroese rank -->
   <td class="is ner">24.98 ± 5.71 / 25.35 ± 4.78</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.18 ± 1.09 / 39.01 ± 2.76</td> <!-- ScaLA-is -->
   <td class="is qa">8.52 ± 2.30 / 21.32 ± 2.25</td> <!-- NQiI -->
   <td class="is summ">39.94 ± 9.39 / 5.18 ± 1.53</td> <!-- RRN -->
   <td class="is know">5.09 ± 1.11 / 28.86 ± 0.73</td> <!-- MMLU-is -->
   <td class="is reason">4.70 ± 2.96 / 56.56 ± 0.97</td> <!-- Winogrande-is -->
   <td class="fo ner">43.52 ± 3.97 / 44.38 ± 3.42</td> <!-- FoNE -->
   <td class="fo la">1.82 ± 2.08 / 34.03 ± 0.66</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">4.96</td> <!-- ScandEval rank -->
   <td class="is-rank">4.81</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.11</td> <!-- Faroese rank -->
   <td class="is ner">27.96 ± 3.08 / 25.78 ± 3.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.00 ± 1.28 / 35.53 ± 1.87</td> <!-- ScaLA-is -->
   <td class="is qa">23.17 ± 2.78 / 44.72 ± 2.82</td> <!-- NQiI -->
   <td class="is summ">55.57 ± 4.13 / 9.41 ± 1.58</td> <!-- RRN -->
   <td class="is know">-0.57 ± 0.97 / 21.78 ± 0.78</td> <!-- MMLU-is -->
   <td class="is reason">-2.72 ± 3.17 / 53.79 ± 1.42</td> <!-- Winogrande-is -->
   <td class="fo ner">32.16 ± 4.25 / 31.47 ± 4.12</td> <!-- FoNE -->
   <td class="fo la">-0.48 ± 2.65 / 38.61 ± 2.83</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.3.2</td> <!-- MMLU-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">4.99</td> <!-- ScandEval rank -->
   <td class="is-rank">4.98</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.99</td> <!-- Faroese rank -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is qa">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">57.17 ± 3.07 / 11.73 ± 1.00</td> <!-- RRN -->
   <td class="is know">6.15 ± 0.90 / 29.29 ± 0.65</td> <!-- MMLU-is -->
   <td class="is reason">-1.71 ± 3.79 / 50.88 ± 1.29</td> <!-- Winogrande-is -->
   <td class="fo ner">34.20 ± 5.85 / 35.35 ± 5.04</td> <!-- FoNE -->
   <td class="fo la">-0.36 ± 1.07 / 35.09 ± 1.96</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">5.00</td> <!-- ScandEval rank -->
   <td class="is-rank">5.01</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.99</td> <!-- Faroese rank -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is qa">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 0.96 / 9.92 ± 1.05</td> <!-- RRN -->
   <td class="is know">2.42 ± 0.70 / 23.15 ± 0.70</td> <!-- MMLU-is -->
   <td class="is reason">0.62 ± 1.42 / 56.02 ± 0.95</td> <!-- Winogrande-is -->
   <td class="fo ner">37.60 ± 2.86 / 36.37 ± 2.61</td> <!-- FoNE -->
   <td class="fo la">-1.62 ± 2.08 / 43.25 ± 3.61</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">5.02</td> <!-- ScandEval rank -->
   <td class="is-rank">4.87</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.16</td> <!-- Faroese rank -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="is summ">60.00 ± 2.62 / 13.07 ± 1.31</td> <!-- RRN -->
   <td class="is know">4.71 ± 1.02 / 26.81 ± 0.83</td> <!-- MMLU-is -->
   <td class="is reason">0.00 ± 2.53 / 56.42 ± 0.98</td> <!-- Winogrande-is -->
   <td class="fo ner">20.15 ± 4.19 / 19.76 ± 4.13</td> <!-- FoNE -->
   <td class="fo la">1.28 ± 1.43 / 39.41 ± 3.29</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="is-rank">5.05</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.08</td> <!-- Faroese rank -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">57.27 ± 1.42 / 10.43 ± 0.97</td> <!-- RRN -->
   <td class="is know">3.87 ± 0.97 / 26.29 ± 0.94</td> <!-- MMLU-is -->
   <td class="is reason">1.92 ± 2.32 / 50.07 ± 2.68</td> <!-- Winogrande-is -->
   <td class="fo ner">26.11 ± 3.40 / 27.37 ± 2.80</td> <!-- FoNE -->
   <td class="fo la">0.15 ± 2.21 / 34.34 ± 0.53</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,467 ± 656 / 986 ± 297</td> <!-- Model inference speed -->
   <td class="rank">5.10</td> <!-- ScandEval rank -->
   <td class="is-rank">4.61</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.59</td> <!-- Faroese rank -->
   <td class="is ner">0.93 ± 0.72 / 0.85 ± 0.61</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.44 ± 1.81 / 35.14 ± 1.24</td> <!-- ScaLA-is -->
   <td class="is qa">25.38 ± 5.24 / 49.07 ± 5.19</td> <!-- NQiI -->
   <td class="is summ">61.39 ± 2.45 / 14.87 ± 1.62</td> <!-- RRN -->
   <td class="is know">10.21 ± 0.95 / 32.56 ± 0.63</td> <!-- MMLU-is -->
   <td class="is reason">4.62 ± 1.79 / 51.48 ± 2.63</td> <!-- Winogrande-is -->
   <td class="fo ner">3.00 ± 0.90 / 3.18 ± 0.97</td> <!-- FoNE -->
   <td class="fo la">1.30 ± 1.59 / 45.16 ± 3.18</td> <!-- ScaLA-fo -->
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.1</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.5.1</td> <!-- RRN version -->
   <td>12.5.1</td> <!-- MMLU-is version -->
   <td>12.5.1</td> <!-- Winogrande-is version -->
   <td>12.5.1</td> <!-- FoNE version -->
   <td>12.5.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">5.15</td> <!-- ScandEval rank -->
   <td class="is-rank">5.19</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.11</td> <!-- Faroese rank -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">2.71 ± 0.84 / 24.35 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">0.85 ± 1.91 / 52.12 ± 2.92</td> <!-- Winogrande-is -->
   <td class="fo ner">29.34 ± 1.57 / 30.91 ± 1.51</td> <!-- FoNE -->
   <td class="fo la">-1.47 ± 1.54 / 35.84 ± 1.76</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">5.16</td> <!-- ScandEval rank -->
   <td class="is-rank">5.16</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.16</td> <!-- Faroese rank -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is qa">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.79 ± 1.12 / 25.76 ± 0.91</td> <!-- MMLU-is -->
   <td class="is reason">1.13 ± 3.74 / 52.30 ± 2.26</td> <!-- Winogrande-is -->
   <td class="fo ner">18.65 ± 5.84 / 20.64 ± 4.75</td> <!-- FoNE -->
   <td class="fo la">1.14 ± 1.66 / 37.04 ± 3.83</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="is-rank">5.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.33</td> <!-- Faroese rank -->
   <td class="is ner">9.50 ± 3.17 / 9.41 ± 3.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is qa">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="is summ">58.92 ± 1.57 / 10.09 ± 1.41</td> <!-- RRN -->
   <td class="is know">2.82 ± 0.73 / 26.56 ± 0.56</td> <!-- MMLU-is -->
   <td class="is reason">1.48 ± 3.56 / 53.95 ± 2.45</td> <!-- Winogrande-is -->
   <td class="fo ner">22.30 ± 2.37 / 22.37 ± 2.40</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.72 / 36.22 ± 2.35</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">5.29</td> <!-- ScandEval rank -->
   <td class="is-rank">5.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.08</td> <!-- Faroese rank -->
   <td class="is ner">8.84 ± 2.72 / 8.59 ± 2.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.38 ± 1.52 / 34.73 ± 1.40</td> <!-- ScaLA-is -->
   <td class="is qa">5.08 ± 1.06 / 18.85 ± 2.62</td> <!-- NQiI -->
   <td class="is summ">42.35 ± 0.38 / 6.36 ± 0.24</td> <!-- RRN -->
   <td class="is know">2.31 ± 1.36 / 25.90 ± 1.45</td> <!-- MMLU-is -->
   <td class="is reason">-1.79 ± 3.44 / 45.33 ± 2.32</td> <!-- Winogrande-is -->
   <td class="fo ner">25.08 ± 6.04 / 25.94 ± 6.17</td> <!-- FoNE -->
   <td class="fo la">1.69 ± 2.72 / 36.58 ± 2.95</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">5.31</td> <!-- ScandEval rank -->
   <td class="is-rank">5.68</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.94</td> <!-- Faroese rank -->
   <td class="is ner">13.60 ± 2.38 / 14.36 ± 2.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.04 ± 0.90 / 34.46 ± 1.41</td> <!-- ScaLA-is -->
   <td class="is qa">1.51 ± 0.68 / 13.16 ± 3.12</td> <!-- NQiI -->
   <td class="is summ">37.41 ± 0.29 / 5.10 ± 0.15</td> <!-- RRN -->
   <td class="is know">-0.09 ± 0.72 / 22.80 ± 0.92</td> <!-- MMLU-is -->
   <td class="is reason">-1.03 ± 1.32 / 56.25 ± 0.87</td> <!-- Winogrande-is -->
   <td class="fo ner">31.84 ± 5.22 / 34.80 ± 3.88</td> <!-- FoNE -->
   <td class="fo la">1.01 ± 2.39 / 39.75 ± 4.10</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">5.31</td> <!-- ScandEval rank -->
   <td class="is-rank">5.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.16</td> <!-- Faroese rank -->
   <td class="is ner">9.04 ± 5.36 / 9.25 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.08 ± 1.02 / 34.02 ± 0.68</td> <!-- ScaLA-is -->
   <td class="is qa">8.86 ± 2.70 / 27.28 ± 1.45</td> <!-- NQiI -->
   <td class="is summ">40.35 ± 0.29 / 6.83 ± 0.14</td> <!-- RRN -->
   <td class="is know">1.17 ± 1.14 / 23.52 ± 1.31</td> <!-- MMLU-is -->
   <td class="is reason">-3.46 ± 3.64 / 47.67 ± 2.88</td> <!-- Winogrande-is -->
   <td class="fo ner">19.57 ± 7.44 / 20.21 ± 6.81</td> <!-- FoNE -->
   <td class="fo la">0.70 ± 1.76 / 42.12 ± 4.88</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">5.35</td> <!-- ScandEval rank -->
   <td class="is-rank">5.37</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.33</td> <!-- Faroese rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.33 ± 3.51</td> <!-- NQiI -->
   <td class="is summ">55.16 ± 1.26 / 10.52 ± 1.13</td> <!-- RRN -->
   <td class="is know">0.74 ± 0.76 / 25.88 ± 1.33</td> <!-- MMLU-is -->
   <td class="is reason">-0.16 ± 0.86 / 32.02 ± 2.77</td> <!-- Winogrande-is -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">5.36</td> <!-- ScandEval rank -->
   <td class="is-rank">4.89</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.83</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">16.91 ± 2.57 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="is summ">60.02 ± 3.15 / 14.22 ± 1.52</td> <!-- RRN -->
   <td class="is know">8.44 ± 0.73 / 31.23 ± 0.59</td> <!-- MMLU-is -->
   <td class="is reason">0.72 ± 2.33 / 52.54 ± 2.18</td> <!-- Winogrande-is -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 0.79 / 33.70 ± 0.64</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>10.0.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>10.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">5.62</td> <!-- ScandEval rank -->
   <td class="is-rank">5.66</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.59</td> <!-- Faroese rank -->
   <td class="is ner">1.68 ± 1.40 / 1.54 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.38 ± 1.13 / 34.41 ± 2.16</td> <!-- ScaLA-is -->
   <td class="is qa">0.08 ± 0.09 / 10.05 ± 2.08</td> <!-- NQiI -->
   <td class="is summ">44.02 ± 1.31 / 6.35 ± 0.43</td> <!-- RRN -->
   <td class="is know">-0.40 ± 0.83 / 23.98 ± 0.87</td> <!-- MMLU-is -->
   <td class="is reason">0.28 ± 1.39 / 32.09 ± 2.15</td> <!-- Winogrande-is -->
   <td class="fo ner">1.84 ± 1.25 / 1.80 ± 1.23</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">5.96</td> <!-- ScandEval rank -->
   <td class="is-rank">6.08</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.83</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">0.69 ± 0.98 / 23.34 ± 0.72</td> <!-- MMLU-is -->
   <td class="is reason">0.47 ± 4.14 / 46.93 ± 3.13</td> <!-- Winogrande-is -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.24 ± 0.93 / 43.16 ± 3.72</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>11.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>11.0.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>11.0.0</td> <!-- ScaLA-fo version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Insular Scandinavian NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-FKbXo&quot; src=&quot;https://datawrapper.dwcdn.net/FKbXo/1015/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
