---
layout: leaderboard
title: Icelandic NLG 🇮🇸
---

<center>Last updated: 09/01/2025 09:21:21 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="icelandic-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Hotter-and-Colder-sentiment</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic reading comprehension - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">ARC-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">Winogrande-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Hotter-and-Colder-sentiment">Hotter-and-Colder-sentiment version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on RRN">RRN version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ARC-is">ARC-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Winogrande-is">Winogrande-is version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.14</td> <!-- ScandEval rank -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">49.59 ± 2.76 / 62.50 ± 2.08</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">69.61 ± 0.61 / 23.98 ± 1.17</td> <!-- RRN -->
   <td class="is know">89.09 ± 1.59 / 91.76 ± 1.19</td> <!-- ARC-is -->
   <td class="is reason">72.03 ± 3.91 / 86.09 ± 1.96</td> <!-- Winogrande-is -->
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.5.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.19</td> <!-- ScandEval rank -->
   <td class="is ner">81.19 ± 2.45 / 54.02 ± 5.60</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">49.86 ± 5.14 / 64.51 ± 3.68</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is rc">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="is summ">68.25 ± 0.27 / 19.22 ± 0.51</td> <!-- RRN -->
   <td class="is know">91.27 ± 1.41 / 93.40 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">70.85 ± 5.98 / 85.55 ± 3.05</td> <!-- Winogrande-is -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">784 ± 310 / 95 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="is ner">64.69 ± 1.77 / 37.89 ± 3.23</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">56.18 ± 4.37 / 69.53 ± 2.97</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">45.52 ± 4.15 / 71.51 ± 2.48</td> <!-- ScaLA-is -->
   <td class="is rc">15.80 ± 6.24 / 55.19 ± 4.14</td> <!-- NQiI -->
   <td class="is summ">67.06 ± 0.10 / 15.92 ± 0.24</td> <!-- RRN -->
   <td class="is know">82.10 ± 1.93 / 86.37 ± 1.50</td> <!-- ARC-is -->
   <td class="is reason">42.82 ± 4.17 / 71.48 ± 2.40</td> <!-- Winogrande-is -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.0</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- RRN version -->
   <td>14.0.1</td> <!-- ARC-is version -->
   <td>14.0.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">436 ± 152 / 57 ± 21</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="is ner">30.39 ± 3.49 / 25.88 ± 1.98</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">47.47 ± 3.03 / 63.45 ± 2.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">43.30 ± 3.41 / 71.54 ± 1.71</td> <!-- ScaLA-is -->
   <td class="is rc">29.82 ± 1.09 / 51.48 ± 0.89</td> <!-- NQiI -->
   <td class="is summ">63.89 ± 0.21 / 13.99 ± 0.19</td> <!-- RRN -->
   <td class="is know">86.79 ± 1.30 / 90.12 ± 0.97</td> <!-- ARC-is -->
   <td class="is reason">54.76 ± 4.75 / 77.97 ± 2.44</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">637 ± 306 / 92 ± 31</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="is ner">72.85 ± 2.10 / 33.36 ± 1.59</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">53.43 ± 2.20 / 66.07 ± 1.59</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">49.26 ± 4.89 / 73.99 ± 2.32</td> <!-- ScaLA-is -->
   <td class="is rc">27.36 ± 0.94 / 48.73 ± 0.97</td> <!-- NQiI -->
   <td class="is summ">67.01 ± 0.08 / 15.62 ± 0.12</td> <!-- RRN -->
   <td class="is know">78.98 ± 1.73 / 83.91 ± 1.34</td> <!-- ARC-is -->
   <td class="is reason">9.83 ± 4.86 / 60.62 ± 2.37</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">908 ± 303 / 96 ± 36</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="is ner">31.11 ± 2.16 / 14.28 ± 0.85</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">50.02 ± 2.61 / 65.44 ± 1.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">35.85 ± 1.55 / 66.14 ± 0.82</td> <!-- ScaLA-is -->
   <td class="is rc">26.93 ± 1.10 / 49.25 ± 1.18</td> <!-- NQiI -->
   <td class="is summ">66.48 ± 0.12 / 14.96 ± 0.13</td> <!-- RRN -->
   <td class="is know">72.80 ± 2.91 / 79.45 ± 2.24</td> <!-- ARC-is -->
   <td class="is reason">28.63 ± 7.69 / 59.45 ± 3.75</td> <!-- Winogrande-is -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="is ner">67.23 ± 2.77 / 45.61 ± 4.86</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">50.38 ± 1.18 / 66.21 ± 1.00</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">20.01 ± 1.09 / 59.74 ± 0.60</td> <!-- ScaLA-is -->
   <td class="is rc">21.18 ± 1.67 / 49.26 ± 0.93</td> <!-- NQiI -->
   <td class="is summ">67.61 ± 0.15 / 19.31 ± 0.26</td> <!-- RRN -->
   <td class="is know">66.74 ± 1.30 / 75.07 ± 0.99</td> <!-- ARC-is -->
   <td class="is reason">33.03 ± 1.47 / 66.80 ± 0.84</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-sonnet-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">193 ± 87 / 55 ± 19</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="is ner">61.70 ± 2.37 / 41.44 ± 1.76</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">51.24 ± 1.69 / 65.49 ± 1.06</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">52.43 ± 2.29 / 73.78 ± 1.09</td> <!-- ScaLA-is -->
   <td class="is rc">22.92 ± 1.06 / 47.06 ± 1.02</td> <!-- NQiI -->
   <td class="is summ">66.02 ± 0.13 / 15.54 ± 0.10</td> <!-- RRN -->
   <td class="is know">15.97 ± 2.78 / 23.83 ± 1.74</td> <!-- ARC-is -->
   <td class="is reason">5.31 ± 4.38 / 59.84 ± 2.96</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,007 ± 316 / 162 ± 45</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="is ner">60.20 ± 2.76 / 40.38 ± 4.22</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">38.09 ± 2.38 / 54.51 ± 2.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">9.14 ± 0.98 / 49.56 ± 2.11</td> <!-- ScaLA-is -->
   <td class="is rc">28.66 ± 1.28 / 58.93 ± 1.41</td> <!-- NQiI -->
   <td class="is summ">67.50 ± 0.21 / 18.61 ± 0.39</td> <!-- RRN -->
   <td class="is know">17.93 ± 1.69 / 38.38 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">5.59 ± 1.88 / 54.19 ± 1.33</td> <!-- Winogrande-is -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.2</td> <!-- RRN version -->
   <td>14.0.2</td> <!-- ARC-is version -->
   <td>14.0.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,005 ± 330 / 196 ± 74</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="is ner">46.48 ± 1.98 / 24.57 ± 1.73</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">39.91 ± 2.35 / 57.39 ± 1.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">11.72 ± 1.81 / 51.67 ± 1.45</td> <!-- ScaLA-is -->
   <td class="is rc">25.91 ± 0.99 / 53.39 ± 1.83</td> <!-- NQiI -->
   <td class="is summ">67.67 ± 0.21 / 18.97 ± 0.43</td> <!-- RRN -->
   <td class="is know">25.83 ± 1.36 / 44.48 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">6.40 ± 3.07 / 50.66 ± 1.69</td> <!-- Winogrande-is -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- RRN version -->
   <td>14.0.2</td> <!-- ARC-is version -->
   <td>14.0.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,610 ± 751 / 176 ± 66</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="is ner">52.97 ± 1.54 / 38.17 ± 4.65</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">41.29 ± 2.30 / 59.30 ± 1.75</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">5.95 ± 2.81 / 40.86 ± 3.68</td> <!-- ScaLA-is -->
   <td class="is rc">31.99 ± 2.60 / 60.26 ± 1.51</td> <!-- NQiI -->
   <td class="is summ">65.19 ± 0.73 / 17.47 ± 0.61</td> <!-- RRN -->
   <td class="is know">21.56 ± 1.35 / 40.99 ± 1.01</td> <!-- ARC-is -->
   <td class="is reason">4.44 ± 1.77 / 54.52 ± 1.51</td> <!-- Winogrande-is -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.0</td> <!-- RRN version -->
   <td>14.0.0</td> <!-- ARC-is version -->
   <td>14.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,335 ± 338 / 260 ± 88</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="is ner">50.45 ± 1.95 / 37.62 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">34.68 ± 3.74 / 53.39 ± 3.75</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">8.69 ± 2.70 / 44.84 ± 4.03</td> <!-- ScaLA-is -->
   <td class="is rc">31.94 ± 2.16 / 59.26 ± 1.50</td> <!-- NQiI -->
   <td class="is summ">65.22 ± 0.77 / 17.53 ± 0.72</td> <!-- RRN -->
   <td class="is know">19.93 ± 1.86 / 39.95 ± 1.39</td> <!-- ARC-is -->
   <td class="is reason">4.52 ± 2.03 / 53.43 ± 2.36</td> <!-- Winogrande-is -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- RRN version -->
   <td>14.0.2</td> <!-- ARC-is version -->
   <td>14.0.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,302 ± 323 / 253 ± 86</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="is ner">47.10 ± 1.90 / 22.63 ± 2.03</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">24.43 ± 2.98 / 39.27 ± 3.37</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">7.19 ± 2.76 / 44.62 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">28.73 ± 1.45 / 54.38 ± 2.28</td> <!-- NQiI -->
   <td class="is summ">66.62 ± 0.16 / 17.04 ± 0.23</td> <!-- RRN -->
   <td class="is know">21.98 ± 1.25 / 40.56 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">0.10 ± 2.39 / 55.15 ± 1.19</td> <!-- Winogrande-is -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.0</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- RRN version -->
   <td>14.0.1</td> <!-- ARC-is version -->
   <td>14.0.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,151 ± 294 / 227 ± 76</td> <!-- Model inference speed -->
   <td class="rank">3.70</td> <!-- ScandEval rank -->
   <td class="is ner">50.99 ± 3.49 / 41.71 ± 4.09</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">24.17 ± 5.04 / 45.19 ± 5.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.15 ± 1.86 / 38.83 ± 2.36</td> <!-- ScaLA-is -->
   <td class="is rc">27.31 ± 2.99 / 51.45 ± 2.09</td> <!-- NQiI -->
   <td class="is summ">56.73 ± 2.99 / 13.21 ± 1.46</td> <!-- RRN -->
   <td class="is know">8.81 ± 1.12 / 31.68 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">3.23 ± 1.68 / 56.53 ± 0.94</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,446 ± 354 / 295 ± 100</td> <!-- Model inference speed -->
   <td class="rank">3.70</td> <!-- ScandEval rank -->
   <td class="is ner">50.69 ± 3.67 / 41.90 ± 4.06</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">24.38 ± 5.21 / 44.65 ± 5.83</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.46 ± 1.66 / 38.73 ± 2.27</td> <!-- ScaLA-is -->
   <td class="is rc">27.11 ± 3.11 / 51.14 ± 2.22</td> <!-- NQiI -->
   <td class="is summ">56.76 ± 2.97 / 13.19 ± 1.46</td> <!-- RRN -->
   <td class="is know">8.71 ± 0.95 / 31.51 ± 0.81</td> <!-- ARC-is -->
   <td class="is reason">3.21 ± 2.55 / 56.74 ± 1.01</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">3.76</td> <!-- ScandEval rank -->
   <td class="is ner">56.71 ± 1.98 / 46.71 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">7.92 ± 3.63 / 32.79 ± 2.05</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">65.39 ± 0.80 / 18.24 ± 1.00</td> <!-- RRN -->
   <td class="is know">9.11 ± 0.92 / 32.06 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">3.30 ± 2.81 / 44.40 ± 1.61</td> <!-- Winogrande-is -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,364 ± 343 / 266 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="is ner">46.73 ± 3.51 / 38.01 ± 4.18</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">26.28 ± 4.82 / 46.42 ± 4.24</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.50 ± 1.18 / 36.24 ± 1.65</td> <!-- ScaLA-is -->
   <td class="is rc">25.17 ± 3.82 / 50.14 ± 2.43</td> <!-- NQiI -->
   <td class="is summ">55.71 ± 3.49 / 12.57 ± 1.70</td> <!-- RRN -->
   <td class="is know">7.21 ± 1.17 / 30.37 ± 0.97</td> <!-- ARC-is -->
   <td class="is reason">2.09 ± 2.31 / 55.37 ± 1.42</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="is ner">42.04 ± 3.53 / 25.31 ± 1.59</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">14.53 ± 4.72 / 32.88 ± 5.49</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 32.97 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is rc">24.07 ± 4.63 / 49.31 ± 4.59</td> <!-- NQiI -->
   <td class="is summ">61.80 ± 2.80 / 14.50 ± 2.00</td> <!-- RRN -->
   <td class="is know">13.79 ± 1.55 / 35.23 ± 1.26</td> <!-- ARC-is -->
   <td class="is reason">0.25 ± 2.45 / 48.10 ± 1.67</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,018 ± 326 / 189 ± 73</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="is ner">28.98 ± 2.63 / 21.75 ± 1.89</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">19.83 ± 4.76 / 41.64 ± 3.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">4.93 ± 1.06 / 49.69 ± 2.65</td> <!-- ScaLA-is -->
   <td class="is rc">24.72 ± 2.22 / 54.41 ± 1.43</td> <!-- NQiI -->
   <td class="is summ">63.45 ± 1.92 / 16.81 ± 2.23</td> <!-- RRN -->
   <td class="is know">10.97 ± 1.13 / 33.51 ± 0.81</td> <!-- ARC-is -->
   <td class="is reason">4.23 ± 1.80 / 49.31 ± 0.84</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,629 ± 573 / 262 ± 149</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="is ner">42.23 ± 4.22 / 25.96 ± 4.27</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">27.93 ± 2.80 / 48.93 ± 1.43</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">6.38 ± 0.99 / 49.63 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is rc">19.39 ± 3.38 / 53.87 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">61.92 ± 1.25 / 15.31 ± 1.05</td> <!-- RRN -->
   <td class="is know">4.22 ± 0.83 / 28.35 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">0.31 ± 2.64 / 54.29 ± 1.30</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,473 ± 493 / 448 ± 143</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="is ner">19.41 ± 1.02 / 18.58 ± 0.98</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">44.79 ± 1.30 / 61.83 ± 1.22</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.93 ± 1.59 / 35.05 ± 1.59</td> <!-- ScaLA-is -->
   <td class="is rc">21.13 ± 3.56 / 52.41 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">61.90 ± 0.85 / 16.43 ± 0.33</td> <!-- RRN -->
   <td class="is know">4.05 ± 1.09 / 28.19 ± 0.81</td> <!-- ARC-is -->
   <td class="is reason">-2.29 ± 4.88 / 52.60 ± 2.17</td> <!-- Winogrande-is -->
   <td>14.0.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.2</td> <!-- ScaLA-is version -->
   <td>14.0.2</td> <!-- NQiI version -->
   <td>14.0.2</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="is ner">40.71 ± 2.93 / 34.57 ± 4.02</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">14.70 ± 7.78 / 36.09 ± 6.06</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is rc">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="is summ">65.25 ± 0.97 / 19.09 ± 1.05</td> <!-- RRN -->
   <td class="is know">5.35 ± 1.32 / 28.11 ± 1.13</td> <!-- ARC-is -->
   <td class="is reason">0.35 ± 2.49 / 51.16 ± 2.74</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-haiku-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">277 ± 77 / 70 ± 25</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="is ner">34.99 ± 2.03 / 17.39 ± 1.24</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">31.19 ± 1.29 / 43.32 ± 1.05</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-10.68 ± 2.75 / 33.95 ± 1.08</td> <!-- ScaLA-is -->
   <td class="is rc">23.65 ± 1.16 / 46.35 ± 1.25</td> <!-- NQiI -->
   <td class="is summ">66.12 ± 0.10 / 15.71 ± 0.20</td> <!-- RRN -->
   <td class="is know">9.00 ± 1.46 / 20.47 ± 1.01</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 59.30 ± 3.13</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">16.23 ± 4.59 / 35.37 ± 4.49</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="is summ">62.55 ± 3.03 / 15.26 ± 2.31</td> <!-- RRN -->
   <td class="is know">5.98 ± 1.66 / 28.18 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">-0.51 ± 1.95 / 47.23 ± 2.39</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.2.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="is ner">42.67 ± 3.13 / 35.40 ± 3.93</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.95 ± 3.78 / 30.20 ± 5.91</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.11 ± 1.45 / 34.61 ± 0.82</td> <!-- ScaLA-is -->
   <td class="is rc">22.25 ± 2.78 / 49.58 ± 2.19</td> <!-- NQiI -->
   <td class="is summ">63.81 ± 1.05 / 16.07 ± 1.19</td> <!-- RRN -->
   <td class="is know">5.12 ± 1.20 / 27.91 ± 0.90</td> <!-- ARC-is -->
   <td class="is reason">0.89 ± 2.37 / 53.27 ± 1.64</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,431 ± 352 / 287 ± 97</td> <!-- Model inference speed -->
   <td class="rank">4.00</td> <!-- ScandEval rank -->
   <td class="is ner">33.21 ± 3.20 / 25.94 ± 2.59</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">25.50 ± 6.42 / 38.95 ± 8.69</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.08 ± 1.20 / 39.03 ± 2.81</td> <!-- ScaLA-is -->
   <td class="is rc">25.76 ± 3.16 / 48.38 ± 2.42</td> <!-- NQiI -->
   <td class="is summ">56.52 ± 1.61 / 10.46 ± 0.85</td> <!-- RRN -->
   <td class="is know">0.81 ± 1.83 / 26.69 ± 0.79</td> <!-- ARC-is -->
   <td class="is reason">-3.96 ± 2.24 / 49.77 ± 3.10</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="is ner">31.81 ± 1.93 / 29.47 ± 2.02</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">18.33 ± 5.09 / 30.21 ± 5.80</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.63 ± 1.69 / 44.49 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is rc">16.72 ± 7.29 / 46.83 ± 5.93</td> <!-- NQiI -->
   <td class="is summ">58.72 ± 3.28 / 13.71 ± 1.35</td> <!-- RRN -->
   <td class="is know">12.62 ± 1.36 / 34.51 ± 1.27</td> <!-- ARC-is -->
   <td class="is reason">3.43 ± 2.18 / 44.56 ± 1.09</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">12.93 ± 5.42 / 30.40 ± 3.15</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">62.80 ± 1.69 / 15.23 ± 1.01</td> <!-- RRN -->
   <td class="is know">5.44 ± 1.14 / 28.13 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">6.35 ± 2.71 / 50.49 ± 1.57</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="is ner">24.92 ± 3.54 / 23.09 ± 3.30</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.76 ± 7.16 / 26.68 ± 6.80</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.15 ± 0.29 / 33.01 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is rc">28.18 ± 1.51 / 54.08 ± 0.71</td> <!-- NQiI -->
   <td class="is summ">64.67 ± 1.48 / 18.74 ± 1.31</td> <!-- RRN -->
   <td class="is know">11.10 ± 0.78 / 33.53 ± 0.69</td> <!-- ARC-is -->
   <td class="is reason">0.89 ± 1.86 / 51.27 ± 1.18</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">4.02</td> <!-- ScandEval rank -->
   <td class="is ner">50.89 ± 2.90 / 35.75 ± 4.67</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.52 ± 4.25 / 29.57 ± 4.96</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.50 ± 0.94 / 33.77 ± 0.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.43 ± 3.38 / 41.32 ± 3.18</td> <!-- NQiI -->
   <td class="is summ">59.94 ± 2.87 / 12.62 ± 1.91</td> <!-- RRN -->
   <td class="is know">5.52 ± 1.26 / 28.97 ± 0.97</td> <!-- ARC-is -->
   <td class="is reason">1.73 ± 2.31 / 50.89 ± 3.35</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="is ner">38.15 ± 2.30 / 28.10 ± 4.65</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">5.32 ± 3.81 / 29.01 ± 5.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.98 ± 1.44 / 35.86 ± 1.12</td> <!-- ScaLA-is -->
   <td class="is rc">20.39 ± 3.04 / 44.20 ± 2.72</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 2.31 / 14.45 ± 1.79</td> <!-- RRN -->
   <td class="is know">7.59 ± 1.44 / 31.07 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">3.44 ± 2.28 / 46.89 ± 1.02</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="is ner">36.47 ± 4.24 / 30.33 ± 3.70</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">1.84 ± 3.02 / 23.26 ± 3.53</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is rc">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="is summ">63.68 ± 1.75 / 16.38 ± 1.24</td> <!-- RRN -->
   <td class="is know">5.12 ± 1.30 / 28.85 ± 0.99</td> <!-- ARC-is -->
   <td class="is reason">8.30 ± 1.28 / 57.35 ± 0.75</td> <!-- Winogrande-is -->
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="is ner">27.57 ± 1.71 / 22.52 ± 1.18</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">10.07 ± 5.45 / 28.32 ± 4.30</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.39 ± 1.30 / 34.40 ± 1.96</td> <!-- ScaLA-is -->
   <td class="is rc">22.98 ± 2.48 / 50.74 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.89 / 14.40 ± 1.93</td> <!-- RRN -->
   <td class="is know">13.33 ± 1.23 / 35.42 ± 0.93</td> <!-- ARC-is -->
   <td class="is reason">0.74 ± 1.09 / 50.92 ± 0.73</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">973 ± 251 / 174 ± 59</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="is ner">37.82 ± 3.63 / 32.97 ± 3.97</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.29 ± 1.16 / 15.66 ± 0.37</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.12 ± 1.31 / 33.78 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">21.59 ± 2.22 / 47.09 ± 1.09</td> <!-- NQiI -->
   <td class="is summ">62.35 ± 3.34 / 16.15 ± 1.66</td> <!-- RRN -->
   <td class="is know">6.54 ± 1.30 / 28.63 ± 1.24</td> <!-- ARC-is -->
   <td class="is reason">1.83 ± 3.53 / 49.23 ± 2.07</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">13.59 ± 6.27 / 36.87 ± 4.51</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">62.30 ± 0.90 / 13.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.16 ± 0.79 / 27.40 ± 0.79</td> <!-- ARC-is -->
   <td class="is reason">1.84 ± 2.19 / 43.79 ± 0.73</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,370 ± 416 / 711 ± 242</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="is ner">34.80 ± 1.37 / 24.03 ± 2.32</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">17.64 ± 3.40 / 40.55 ± 3.17</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">5.46 ± 1.31 / 51.42 ± 1.10</td> <!-- ScaLA-is -->
   <td class="is rc">12.66 ± 2.33 / 45.06 ± 2.27</td> <!-- NQiI -->
   <td class="is summ">61.79 ± 0.68 / 8.78 ± 1.49</td> <!-- RRN -->
   <td class="is know">2.88 ± 0.65 / 26.40 ± 0.51</td> <!-- ARC-is -->
   <td class="is reason">-1.11 ± 3.79 / 53.57 ± 2.07</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="is ner">14.79 ± 4.70 / 13.03 ± 2.92</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">15.24 ± 6.48 / 34.96 ± 6.66</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.10 ± 1.54 / 34.67 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.42 ± 1.09 / 51.72 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">62.67 ± 1.62 / 16.91 ± 1.38</td> <!-- RRN -->
   <td class="is know">10.76 ± 1.56 / 32.34 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-5.20 ± 1.82 / 53.08 ± 0.91</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,121 ± 288 / 205 ± 68</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="is ner">47.16 ± 2.83 / 38.60 ± 4.04</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.33 ± 0.93 / 15.64 ± 1.01</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.84 ± 1.27 / 40.06 ± 3.79</td> <!-- ScaLA-is -->
   <td class="is rc">21.75 ± 2.21 / 48.25 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 2.91 / 14.91 ± 1.85</td> <!-- RRN -->
   <td class="is know">3.70 ± 1.01 / 27.71 ± 0.66</td> <!-- ARC-is -->
   <td class="is reason">-3.24 ± 3.16 / 49.96 ± 2.38</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,382 ± 337 / 257 ± 91</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="is ner">29.67 ± 3.72 / 27.17 ± 3.34</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">26.31 ± 7.12 / 39.72 ± 8.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.03 ± 1.37 / 36.71 ± 1.69</td> <!-- ScaLA-is -->
   <td class="is rc">21.77 ± 2.71 / 44.31 ± 1.72</td> <!-- NQiI -->
   <td class="is summ">52.52 ± 1.06 / 8.43 ± 0.54</td> <!-- RRN -->
   <td class="is know">0.09 ± 1.89 / 23.25 ± 0.85</td> <!-- ARC-is -->
   <td class="is reason">-0.74 ± 2.25 / 54.29 ± 1.70</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="is ner">27.22 ± 3.65 / 24.21 ± 2.67</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">17.80 ± 4.22 / 36.50 ± 4.92</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.31 ± 1.28 / 39.67 ± 4.39</td> <!-- ScaLA-is -->
   <td class="is rc">17.24 ± 2.72 / 41.15 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.66 / 15.80 ± 1.12</td> <!-- RRN -->
   <td class="is know">1.85 ± 1.18 / 26.88 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">1.06 ± 2.84 / 47.19 ± 2.14</td> <!-- Winogrande-is -->
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,194 ± 687 / 650 ± 216</td> <!-- Model inference speed -->
   <td class="rank">4.14</td> <!-- ScandEval rank -->
   <td class="is ner">33.05 ± 4.29 / 29.75 ± 3.67</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">14.42 ± 3.18 / 37.82 ± 2.65</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.71 ± 1.18 / 34.80 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">17.23 ± 2.51 / 39.88 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">60.08 ± 1.45 / 13.80 ± 0.81</td> <!-- RRN -->
   <td class="is know">2.67 ± 1.35 / 27.04 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">2.74 ± 2.28 / 53.18 ± 0.93</td> <!-- Winogrande-is -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.5</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>neuralmagic/Sparse-Llama-3.1-8B-2of4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,996 ± 817 / 284 ± 96</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="is ner">22.23 ± 2.11 / 22.77 ± 2.37</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">21.46 ± 6.37 / 35.83 ± 5.28</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.10 ± 0.51 / 33.23 ± 0.41</td> <!-- ScaLA-is -->
   <td class="is rc">23.34 ± 2.39 / 45.64 ± 1.96</td> <!-- NQiI -->
   <td class="is summ">51.47 ± 3.70 / 10.97 ± 1.31</td> <!-- RRN -->
   <td class="is know">6.43 ± 1.33 / 29.48 ± 1.16</td> <!-- ARC-is -->
   <td class="is reason">1.43 ± 2.24 / 56.48 ± 0.99</td> <!-- Winogrande-is -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- RRN version -->
   <td>14.0.3</td> <!-- ARC-is version -->
   <td>14.0.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">13.24 ± 8.29 / 31.92 ± 6.23</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.33 / 26.91 ± 1.00</td> <!-- ARC-is -->
   <td class="is reason">-0.00 ± 2.41 / 44.93 ± 0.92</td> <!-- Winogrande-is -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">4.18</td> <!-- ScandEval rank -->
   <td class="is ner">34.62 ± 4.64 / 33.25 ± 4.37</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">12.72 ± 4.04 / 28.92 ± 4.48</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.24 ± 1.43 / 33.75 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is rc">18.10 ± 1.85 / 43.52 ± 0.87</td> <!-- NQiI -->
   <td class="is summ">61.81 ± 0.98 / 15.04 ± 0.70</td> <!-- RRN -->
   <td class="is know">3.06 ± 1.01 / 28.01 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">-1.90 ± 2.28 / 44.34 ± 1.19</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.18</td> <!-- ScandEval rank -->
   <td class="is ner">36.59 ± 3.56 / 27.50 ± 2.53</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">11.75 ± 4.91 / 34.26 ± 5.32</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.86 ± 2.41 / 36.44 ± 1.27</td> <!-- ScaLA-is -->
   <td class="is rc">14.58 ± 2.13 / 37.44 ± 1.86</td> <!-- NQiI -->
   <td class="is summ">61.99 ± 1.16 / 15.07 ± 0.81</td> <!-- RRN -->
   <td class="is know">1.48 ± 1.63 / 23.23 ± 0.93</td> <!-- ARC-is -->
   <td class="is reason">-0.98 ± 2.63 / 56.13 ± 0.62</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="is ner">17.79 ± 1.18 / 18.12 ± 1.18</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">21.09 ± 4.78 / 36.73 ± 5.45</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.08 ± 0.15 / 33.73 ± 0.26</td> <!-- ScaLA-is -->
   <td class="is rc">15.04 ± 2.53 / 34.77 ± 1.72</td> <!-- NQiI -->
   <td class="is summ">59.45 ± 1.99 / 12.89 ± 1.04</td> <!-- RRN -->
   <td class="is know">1.06 ± 1.26 / 22.59 ± 0.63</td> <!-- ARC-is -->
   <td class="is reason">5.69 ± 2.26 / 56.71 ± 0.87</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="is ner">34.76 ± 4.42 / 23.42 ± 2.33</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">12.07 ± 3.53 / 32.35 ± 5.40</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.77 ± 1.05 / 39.63 ± 2.41</td> <!-- ScaLA-is -->
   <td class="is rc">12.80 ± 2.37 / 30.77 ± 2.12</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 1.78 / 15.53 ± 0.95</td> <!-- RRN -->
   <td class="is know">2.01 ± 0.96 / 25.83 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-0.76 ± 3.69 / 53.64 ± 2.57</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="is ner">10.67 ± 5.23 / 13.01 ± 3.26</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">12.86 ± 6.56 / 28.74 ± 6.46</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.21 ± 0.99 / 33.71 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">20.22 ± 3.01 / 43.48 ± 2.32</td> <!-- NQiI -->
   <td class="is summ">59.97 ± 2.49 / 13.32 ± 2.03</td> <!-- RRN -->
   <td class="is know">10.08 ± 1.82 / 32.08 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">1.16 ± 2.48 / 51.00 ± 1.70</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="is ner">33.76 ± 3.44 / 32.21 ± 2.82</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.91 ± 4.60 / 27.56 ± 4.17</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.13 ± 1.34 / 42.66 ± 3.62</td> <!-- ScaLA-is -->
   <td class="is rc">12.43 ± 2.62 / 33.38 ± 1.39</td> <!-- NQiI -->
   <td class="is summ">59.46 ± 2.42 / 13.23 ± 1.87</td> <!-- RRN -->
   <td class="is know">2.09 ± 1.34 / 25.68 ± 0.67</td> <!-- ARC-is -->
   <td class="is reason">3.56 ± 2.07 / 56.72 ± 0.99</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="is ner">30.21 ± 4.29 / 29.79 ± 3.81</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">5.88 ± 2.95 / 21.46 ± 3.02</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.67 ± 1.87 / 48.02 ± 3.06</td> <!-- ScaLA-is -->
   <td class="is rc">15.12 ± 1.65 / 40.55 ± 1.13</td> <!-- NQiI -->
   <td class="is summ">56.75 ± 2.25 / 10.37 ± 1.58</td> <!-- RRN -->
   <td class="is know">3.22 ± 0.92 / 27.64 ± 0.84</td> <!-- ARC-is -->
   <td class="is reason">1.88 ± 2.37 / 49.26 ± 1.60</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="is ner">26.23 ± 3.53 / 23.26 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.86 ± 5.25 / 23.96 ± 4.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.69 ± 1.42 / 45.61 ± 2.69</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.59 / 28.57 ± 2.09</td> <!-- NQiI -->
   <td class="is summ">60.43 ± 2.70 / 15.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">1.93 ± 1.38 / 25.06 ± 1.16</td> <!-- ARC-is -->
   <td class="is reason">3.27 ± 2.97 / 54.02 ± 1.79</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">7.56 ± 4.87 / 26.07 ± 4.12</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is rc">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="is summ">62.11 ± 2.22 / 14.98 ± 1.53</td> <!-- RRN -->
   <td class="is know">4.50 ± 1.47 / 28.86 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">-1.89 ± 2.66 / 43.72 ± 0.92</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="is ner">43.20 ± 3.61 / 32.10 ± 3.76</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.54 ± 2.60 / 17.05 ± 2.70</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">14.28 ± 2.94 / 38.21 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">49.66 ± 3.28 / 7.97 ± 1.43</td> <!-- RRN -->
   <td class="is know">3.07 ± 1.66 / 25.74 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">2.79 ± 3.13 / 47.97 ± 1.43</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">4.34</td> <!-- ScandEval rank -->
   <td class="is ner">38.52 ± 3.25 / 28.84 ± 5.49</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">4.29 ± 3.60 / 23.24 ± 4.11</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.94 ± 2.60 / 36.06 ± 2.17</td> <!-- NQiI -->
   <td class="is summ">58.58 ± 4.00 / 12.91 ± 2.09</td> <!-- RRN -->
   <td class="is know">2.11 ± 1.02 / 27.80 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-4.75 ± 2.84 / 50.40 ± 4.21</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="is ner">28.74 ± 2.37 / 19.43 ± 1.48</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">4.30 ± 1.28 / 19.35 ± 2.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.06 ± 1.39 / 34.20 ± 1.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.41 ± 2.45 / 45.55 ± 1.65</td> <!-- NQiI -->
   <td class="is summ">60.79 ± 0.72 / 13.13 ± 0.60</td> <!-- RRN -->
   <td class="is know">0.18 ± 1.16 / 23.06 ± 0.66</td> <!-- ARC-is -->
   <td class="is reason">-1.64 ± 2.16 / 53.50 ± 2.67</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">10.08 ± 5.54 / 31.35 ± 3.02</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="is summ">60.00 ± 2.62 / 13.07 ± 1.31</td> <!-- RRN -->
   <td class="is know">2.52 ± 1.20 / 26.23 ± 1.40</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 2.53 / 56.42 ± 0.98</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="is ner">29.51 ± 2.44 / 29.14 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">1.70 ± 2.98 / 16.77 ± 2.07</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.32 ± 0.63 / 33.70 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.36 ± 2.12 / 34.06 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">59.43 ± 1.83 / 13.09 ± 1.58</td> <!-- RRN -->
   <td class="is know">2.35 ± 1.26 / 27.85 ± 0.87</td> <!-- ARC-is -->
   <td class="is reason">0.01 ± 2.73 / 45.18 ± 1.36</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">4.38</td> <!-- ScandEval rank -->
   <td class="is ner">23.14 ± 2.08 / 23.09 ± 2.24</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">5.07 ± 2.69 / 27.01 ± 2.31</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.18 ± 1.67 / 33.93 ± 0.34</td> <!-- ScaLA-is -->
   <td class="is rc">14.15 ± 2.49 / 36.10 ± 1.65</td> <!-- NQiI -->
   <td class="is summ">60.80 ± 0.81 / 10.79 ± 1.85</td> <!-- RRN -->
   <td class="is know">2.86 ± 1.31 / 26.61 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">-1.31 ± 2.24 / 50.29 ± 1.93</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="is ner">1.42 ± 1.60 / 3.11 ± 1.85</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">4.18 ± 2.03 / 17.89 ± 1.60</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.75 ± 0.73 / 45.87 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">23.33 ± 2.22 / 45.28 ± 1.58</td> <!-- NQiI -->
   <td class="is summ">64.23 ± 1.78 / 15.08 ± 2.03</td> <!-- RRN -->
   <td class="is know">0.40 ± 1.88 / 23.35 ± 1.22</td> <!-- ARC-is -->
   <td class="is reason">0.68 ± 4.15 / 50.85 ± 2.65</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="is ner">26.58 ± 1.47 / 22.13 ± 2.38</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.79 ± 2.98 / 26.06 ± 1.66</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.63 ± 1.36 / 43.80 ± 3.59</td> <!-- ScaLA-is -->
   <td class="is rc">15.14 ± 2.49 / 44.23 ± 2.12</td> <!-- NQiI -->
   <td class="is summ">60.84 ± 0.65 / 13.75 ± 0.70</td> <!-- RRN -->
   <td class="is know">1.17 ± 1.56 / 23.34 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">-0.12 ± 2.10 / 54.54 ± 1.79</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">4.40</td> <!-- ScandEval rank -->
   <td class="is ner">20.50 ± 4.51 / 18.93 ± 3.84</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">10.09 ± 3.91 / 29.11 ± 2.96</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.83 ± 1.65 / 45.84 ± 2.02</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.45 / 28.36 ± 1.48</td> <!-- NQiI -->
   <td class="is summ">57.52 ± 4.61 / 13.43 ± 2.11</td> <!-- RRN -->
   <td class="is know">3.16 ± 0.85 / 26.13 ± 0.67</td> <!-- ARC-is -->
   <td class="is reason">-1.83 ± 3.11 / 49.80 ± 1.96</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">4.48</td> <!-- ScandEval rank -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.17 ± 4.79 / 31.18 ± 2.72</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">57.17 ± 3.07 / 11.73 ± 1.00</td> <!-- RRN -->
   <td class="is know">5.46 ± 1.45 / 29.23 ± 1.11</td> <!-- ARC-is -->
   <td class="is reason">-1.71 ± 3.79 / 50.88 ± 1.29</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.75 ± 1.97 / 22.91 ± 2.76</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is rc">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 0.96 / 9.92 ± 1.05</td> <!-- RRN -->
   <td class="is know">0.45 ± 1.44 / 22.94 ± 0.76</td> <!-- ARC-is -->
   <td class="is reason">0.62 ± 1.42 / 56.02 ± 0.95</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="is ner">18.07 ± 3.62 / 18.73 ± 2.54</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.65 ± 3.12 / 18.97 ± 1.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.72 ± 1.22 / 33.96 ± 0.50</td> <!-- ScaLA-is -->
   <td class="is rc">12.27 ± 2.81 / 30.66 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">56.49 ± 3.33 / 8.77 ± 1.24</td> <!-- RRN -->
   <td class="is know">0.32 ± 1.35 / 24.82 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">1.00 ± 2.57 / 51.21 ± 2.91</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="is ner">17.77 ± 6.81 / 16.42 ± 6.19</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">7.64 ± 4.41 / 25.58 ± 4.40</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.35 ± 1.50 / 34.29 ± 1.64</td> <!-- ScaLA-is -->
   <td class="is rc">8.15 ± 2.21 / 30.75 ± 2.05</td> <!-- NQiI -->
   <td class="is summ">54.21 ± 3.27 / 11.06 ± 1.56</td> <!-- RRN -->
   <td class="is know">0.71 ± 1.34 / 25.40 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">2.88 ± 1.84 / 54.45 ± 2.60</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="is ner">24.98 ± 5.71 / 25.35 ± 4.78</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">13.57 ± 4.68 / 28.38 ± 5.14</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.18 ± 1.09 / 39.01 ± 2.76</td> <!-- ScaLA-is -->
   <td class="is rc">8.52 ± 2.30 / 21.32 ± 2.25</td> <!-- NQiI -->
   <td class="is summ">39.94 ± 9.39 / 5.18 ± 1.53</td> <!-- RRN -->
   <td class="is know">4.83 ± 1.40 / 29.14 ± 1.10</td> <!-- ARC-is -->
   <td class="is reason">4.70 ± 2.96 / 56.56 ± 0.97</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">4.56</td> <!-- ScandEval rank -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.87 ± 6.27 / 28.55 ± 3.29</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">57.27 ± 1.42 / 10.43 ± 0.97</td> <!-- RRN -->
   <td class="is know">1.62 ± 1.18 / 25.09 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">1.92 ± 2.32 / 50.07 ± 2.68</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">4.57</td> <!-- ScandEval rank -->
   <td class="is ner">13.29 ± 2.33 / 14.72 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.83 ± 5.62 / 31.41 ± 4.70</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.92 ± 1.51 / 42.09 ± 3.39</td> <!-- ScaLA-is -->
   <td class="is rc">7.49 ± 1.26 / 24.16 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">56.76 ± 2.66 / 9.80 ± 1.05</td> <!-- RRN -->
   <td class="is know">0.59 ± 0.49 / 23.09 ± 0.56</td> <!-- ARC-is -->
   <td class="is reason">1.87 ± 3.67 / 49.58 ± 3.20</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="is ner">22.56 ± 3.90 / 22.69 ± 3.50</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.53 ± 2.22 / 20.28 ± 1.55</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.26 ± 0.43 / 33.59 ± 1.01</td> <!-- ScaLA-is -->
   <td class="is rc">11.77 ± 1.87 / 31.39 ± 2.24</td> <!-- NQiI -->
   <td class="is summ">53.36 ± 3.05 / 8.87 ± 1.05</td> <!-- RRN -->
   <td class="is know">0.36 ± 1.59 / 23.64 ± 0.76</td> <!-- ARC-is -->
   <td class="is reason">0.24 ± 3.00 / 55.12 ± 1.24</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="is ner">18.86 ± 5.30 / 18.63 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.67 ± 2.61 / 21.03 ± 3.38</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.76 ± 0.76 / 33.16 ± 0.37</td> <!-- ScaLA-is -->
   <td class="is rc">8.09 ± 1.59 / 26.19 ± 2.53</td> <!-- NQiI -->
   <td class="is summ">60.61 ± 1.18 / 12.59 ± 0.80</td> <!-- RRN -->
   <td class="is know">-0.78 ± 1.21 / 22.85 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">-0.84 ± 2.04 / 56.38 ± 1.01</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="is ner">33.57 ± 2.48 / 33.47 ± 2.48</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.60 ± 2.01 / 16.42 ± 1.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">11.27 ± 2.38 / 33.54 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">49.32 ± 3.71 / 8.01 ± 2.04</td> <!-- RRN -->
   <td class="is know">1.37 ± 1.11 / 25.57 ± 1.36</td> <!-- ARC-is -->
   <td class="is reason">-4.04 ± 3.58 / 50.55 ± 3.65</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,136 ± 558 / 942 ± 290</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="is ner">19.07 ± 1.70 / 20.43 ± 1.80</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.51 ± 3.34 / 18.63 ± 3.02</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.99 ± 1.27 / 39.24 ± 3.43</td> <!-- ScaLA-is -->
   <td class="is rc">9.54 ± 0.94 / 25.84 ± 1.85</td> <!-- NQiI -->
   <td class="is summ">59.42 ± 0.72 / 10.23 ± 1.25</td> <!-- RRN -->
   <td class="is know">0.79 ± 1.16 / 24.04 ± 0.75</td> <!-- ARC-is -->
   <td class="is reason">-3.20 ± 3.60 / 51.52 ± 1.92</td> <!-- Winogrande-is -->
   <td>13.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.2.0</td> <!-- ScaLA-is version -->
   <td>13.2.0</td> <!-- NQiI version -->
   <td>13.2.0</td> <!-- RRN version -->
   <td>13.2.0</td> <!-- ARC-is version -->
   <td>13.2.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">4.62</td> <!-- ScandEval rank -->
   <td class="is ner">9.90 ± 5.26 / 15.24 ± 2.90</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.13 ± 2.07 / 21.55 ± 2.63</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.02 ± 1.43 / 34.31 ± 2.24</td> <!-- ScaLA-is -->
   <td class="is rc">10.64 ± 2.56 / 31.31 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">54.83 ± 2.32 / 11.29 ± 0.66</td> <!-- RRN -->
   <td class="is know">-0.56 ± 1.92 / 23.31 ± 1.19</td> <!-- ARC-is -->
   <td class="is reason">1.21 ± 2.27 / 53.67 ± 2.22</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,964 ± 2,255 / 1,299 ± 433</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="is ner">17.74 ± 3.49 / 16.16 ± 1.89</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.84 ± 4.22 / 27.14 ± 5.28</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.13 ± 1.09 / 44.10 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">7.74 ± 1.43 / 24.78 ± 1.48</td> <!-- NQiI -->
   <td class="is summ">58.60 ± 1.15 / 10.95 ± 1.08</td> <!-- RRN -->
   <td class="is know">-1.11 ± 1.33 / 22.73 ± 0.90</td> <!-- ARC-is -->
   <td class="is reason">-4.23 ± 3.18 / 51.91 ± 2.86</td> <!-- Winogrande-is -->
   <td>13.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.2.0</td> <!-- ScaLA-is version -->
   <td>13.2.0</td> <!-- NQiI version -->
   <td>13.2.0</td> <!-- RRN version -->
   <td>13.2.0</td> <!-- ARC-is version -->
   <td>13.2.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="is ner">9.50 ± 3.17 / 9.41 ± 3.40</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">1.63 ± 1.45 / 19.19 ± 0.27</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is rc">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="is summ">58.92 ± 1.57 / 10.09 ± 1.41</td> <!-- RRN -->
   <td class="is know">-1.28 ± 1.48 / 24.82 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.48 ± 3.56 / 53.95 ± 2.45</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.71</td> <!-- ScandEval rank -->
   <td class="is ner">13.43 ± 1.36 / 13.81 ± 1.45</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.82 ± 2.09 / 24.09 ± 2.81</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.14 ± 1.52 / 36.93 ± 3.69</td> <!-- ScaLA-is -->
   <td class="is rc">3.71 ± 1.14 / 16.21 ± 2.86</td> <!-- NQiI -->
   <td class="is summ">51.93 ± 3.96 / 8.48 ± 0.87</td> <!-- RRN -->
   <td class="is know">0.95 ± 1.48 / 22.52 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">2.90 ± 2.91 / 56.72 ± 0.69</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.10 ± 1.78 / 18.76 ± 2.62</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">1.96 ± 1.72 / 25.55 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">0.85 ± 1.91 / 52.12 ± 2.92</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="is ner">14.74 ± 2.42 / 16.01 ± 2.04</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.13 ± 3.12 / 22.51 ± 2.62</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.25 ± 0.60 / 34.69 ± 3.02</td> <!-- ScaLA-is -->
   <td class="is rc">1.35 ± 0.73 / 10.92 ± 2.52</td> <!-- NQiI -->
   <td class="is summ">52.66 ± 3.89 / 8.73 ± 0.71</td> <!-- RRN -->
   <td class="is know">1.21 ± 0.80 / 26.20 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">1.69 ± 2.26 / 49.46 ± 3.56</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1385</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,808 ± 2,183 / 1,289 ± 428</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="is ner">5.62 ± 3.01 / 8.37 ± 2.88</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">4.82 ± 4.50 / 22.80 ± 5.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.20 ± 0.76 / 33.73 ± 0.26</td> <!-- ScaLA-is -->
   <td class="is rc">4.94 ± 1.33 / 18.58 ± 2.50</td> <!-- NQiI -->
   <td class="is summ">58.01 ± 2.21 / 10.21 ± 1.25</td> <!-- RRN -->
   <td class="is know">0.78 ± 1.22 / 22.17 ± 0.62</td> <!-- ARC-is -->
   <td class="is reason">-2.14 ± 2.71 / 51.91 ± 3.81</td> <!-- Winogrande-is -->
   <td>13.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.2.0</td> <!-- ScaLA-is version -->
   <td>13.2.0</td> <!-- NQiI version -->
   <td>13.2.0</td> <!-- RRN version -->
   <td>13.2.0</td> <!-- ARC-is version -->
   <td>13.2.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">4.74</td> <!-- ScandEval rank -->
   <td class="is ner">17.73 ± 1.58 / 18.22 ± 1.53</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.38 ± 2.00 / 21.79 ± 2.03</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.18 ± 1.21 / 37.94 ± 4.17</td> <!-- ScaLA-is -->
   <td class="is rc">1.59 ± 0.83 / 12.57 ± 3.10</td> <!-- NQiI -->
   <td class="is summ">52.81 ± 2.78 / 8.12 ± 0.57</td> <!-- RRN -->
   <td class="is know">0.89 ± 1.75 / 25.64 ± 1.59</td> <!-- ARC-is -->
   <td class="is reason">-1.11 ± 3.80 / 55.19 ± 1.68</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="is ner">23.67 ± 5.16 / 23.19 ± 4.37</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">7.76 ± 3.65 / 29.49 ± 4.31</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 14.61 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">50.54 ± 0.14 / 3.11 ± 0.06</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 22.04 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 56.52 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="is ner">13.60 ± 1.50 / 13.99 ± 1.39</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.12 ± 4.92 / 27.55 ± 4.21</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.28 ± 1.41 / 37.58 ± 4.34</td> <!-- ScaLA-is -->
   <td class="is rc">4.09 ± 1.03 / 16.34 ± 2.86</td> <!-- NQiI -->
   <td class="is summ">50.00 ± 3.22 / 7.84 ± 0.71</td> <!-- RRN -->
   <td class="is know">-0.11 ± 0.95 / 22.28 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">2.51 ± 3.01 / 51.41 ± 3.27</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.79</td> <!-- ScandEval rank -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-9.69 ± 4.92 / 18.53 ± 1.70</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.45 / 26.36 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.13 ± 3.74 / 52.30 ± 2.26</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.32 ± 3.76 / 21.42 ± 3.52</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is rc">1.04 ± 0.96 / 7.35 ± 3.52</td> <!-- NQiI -->
   <td class="is summ">55.16 ± 1.26 / 10.52 ± 1.13</td> <!-- RRN -->
   <td class="is know">-0.80 ± 2.00 / 23.89 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">-0.16 ± 0.86 / 32.02 ± 2.77</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="is ner">18.38 ± 1.54 / 20.76 ± 1.34</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-1.70 ± 2.31 / 21.85 ± 2.75</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.49 ± 1.54 / 42.54 ± 4.23</td> <!-- ScaLA-is -->
   <td class="is rc">6.30 ± 2.23 / 23.24 ± 0.99</td> <!-- NQiI -->
   <td class="is summ">51.62 ± 2.09 / 8.63 ± 0.96</td> <!-- RRN -->
   <td class="is know">2.25 ± 1.26 / 26.07 ± 1.15</td> <!-- ARC-is -->
   <td class="is reason">-6.17 ± 1.44 / 52.90 ± 2.42</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.85</td> <!-- ScandEval rank -->
   <td class="is ner">13.70 ± 2.05 / 15.01 ± 2.07</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.01 ± 2.55 / 22.58 ± 2.22</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.83 ± 0.71 / 32.99 ± 0.27</td> <!-- ScaLA-is -->
   <td class="is rc">0.94 ± 0.54 / 10.22 ± 2.52</td> <!-- NQiI -->
   <td class="is summ">50.30 ± 4.32 / 7.82 ± 0.77</td> <!-- RRN -->
   <td class="is know">1.10 ± 1.16 / 25.43 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">-0.07 ± 3.01 / 46.28 ± 3.42</td> <!-- Winogrande-is -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="is ner">13.80 ± 3.19 / 14.46 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.17 ± 2.73 / 22.31 ± 3.55</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.63 ± 0.78 / 36.66 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is rc">1.29 ± 0.69 / 10.96 ± 2.80</td> <!-- NQiI -->
   <td class="is summ">43.40 ± 4.76 / 4.83 ± 1.49</td> <!-- RRN -->
   <td class="is know">1.16 ± 0.83 / 25.72 ± 0.93</td> <!-- ARC-is -->
   <td class="is reason">1.21 ± 4.89 / 55.31 ± 1.38</td> <!-- Winogrande-is -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- RRN version -->
   <td>14.0.4</td> <!-- ARC-is version -->
   <td>14.0.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="is ner">1.68 ± 1.40 / 1.54 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.78 ± 2.87 / 22.52 ± 3.50</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.38 ± 1.13 / 34.41 ± 2.16</td> <!-- ScaLA-is -->
   <td class="is rc">0.08 ± 0.09 / 10.05 ± 2.08</td> <!-- NQiI -->
   <td class="is summ">44.02 ± 1.31 / 6.35 ± 0.43</td> <!-- RRN -->
   <td class="is know">0.15 ± 1.45 / 23.95 ± 1.29</td> <!-- ARC-is -->
   <td class="is reason">0.28 ± 1.39 / 32.09 ± 2.15</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">5.07</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.31 ± 2.42 / 20.87 ± 2.00</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 3.90 ± 0.28</td> <!-- NQiI -->
   <td class="is summ">44.80 ± 0.65 / 3.34 ± 0.08</td> <!-- RRN -->
   <td class="is know">0.23 ± 0.75 / 22.11 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.38 ± 0.75 / 56.53 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icechat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">49,558 ± 7,930 / 13,921 ± 4,425</td> <!-- Model inference speed -->
   <td class="rank">5.14</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">1.86 ± 2.32 / 23.48 ± 4.78</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.64 ± 0.34</td> <!-- NQiI -->
   <td class="is summ">42.46 ± 0.47 / 3.58 ± 0.45</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 22.04 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 56.52 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.25</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-1.30 ± 1.45 / 18.79 ± 0.29</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- NQiI -->
   <td class="is summ">36.58 ± 2.96 / 0.16 ± 0.02</td> <!-- RRN -->
   <td class="is know">-0.00 ± 1.73 / 24.71 ± 1.42</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 43.48 ± 0.89</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.48</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.54 ± 2.23 / 21.79 ± 2.35</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">-0.02 ± 1.16 / 22.75 ± 0.50</td> <!-- ARC-is -->
   <td class="is reason">0.47 ± 4.14 / 46.93 ± 3.13</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>11.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/jonas-hallgrimsson-gpt2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">32,644 ± 3,887 / 11,289 ± 3,585</td> <!-- Model inference speed -->
   <td class="rank">5.76</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.00 ± 0.00 / 18.81 ± 0.27</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NQiI -->
   <td class="is summ">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- RRN -->
   <td class="is know">-0.26 ± 0.90 / 22.02 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">-0.01 ± 1.21 / 55.08 ± 0.99</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/icelandic-nlg.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
