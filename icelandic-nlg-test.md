---
layout: leaderboard
title: Icelandic NLG 🇮🇸
---

<center>Last updated: 15/10/2024 11:49:05 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="icelandic-nlg-test" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic reading comprehension - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">ARC-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">Winogrande-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
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
   <td class="rank">1.16</td> <!-- ScandEval rank -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">69.61 ± 0.61 / 23.98 ± 1.17</td> <!-- RRN -->
   <td class="is know">89.09 ± 1.59 / 91.76 ± 1.19</td> <!-- ARC-is -->
   <td class="is reason">72.03 ± 3.91 / 86.09 ± 1.96</td> <!-- Winogrande-is -->
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">1.20</td> <!-- ScandEval rank -->
   <td class="is ner">81.19 ± 2.45 / 54.02 ± 5.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is rc">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="is summ">68.25 ± 0.27 / 19.22 ± 0.51</td> <!-- RRN -->
   <td class="is know">91.27 ± 1.41 / 93.40 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">70.85 ± 5.98 / 85.55 ± 3.05</td> <!-- Winogrande-is -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8190</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.48</td> <!-- ScandEval rank -->
   <td class="is ner">78.67 ± 2.16 / 59.54 ± 4.85</td> <!-- MIM-GOLD-NER -->
   <td class="is la">33.65 ± 3.19 / 60.56 ± 2.35</td> <!-- ScaLA-is -->
   <td class="is rc">32.25 ± 2.01 / 60.12 ± 1.31</td> <!-- NQiI -->
   <td class="is summ">69.21 ± 0.25 / 22.50 ± 0.53</td> <!-- RRN -->
   <td class="is know">86.32 ± 1.50 / 89.65 ± 1.16</td> <!-- ARC-is -->
   <td class="is reason">74.02 ± 4.17 / 86.80 ± 2.02</td> <!-- Winogrande-is -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="is ner">67.56 ± 1.93 / 43.20 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">23.28 ± 7.61 / 52.43 ± 7.20</td> <!-- ScaLA-is -->
   <td class="is rc">24.91 ± 1.14 / 52.48 ± 0.90</td> <!-- NQiI -->
   <td class="is summ">67.32 ± 0.95 / 17.55 ± 1.32</td> <!-- RRN -->
   <td class="is know">67.57 ± 3.31 / 75.27 ± 2.62</td> <!-- ARC-is -->
   <td class="is reason">15.36 ± 5.77 / 49.21 ± 3.61</td> <!-- Winogrande-is -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- RRN version -->
   <td>12.11.0</td> <!-- ARC-is version -->
   <td>12.11.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="is ner">45.42 ± 1.86 / 36.69 ± 2.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">24.23 ± 0.89 / 61.40 ± 0.70</td> <!-- ScaLA-is -->
   <td class="is rc">24.96 ± 1.52 / 55.04 ± 0.80</td> <!-- NQiI -->
   <td class="is summ">68.19 ± 0.25 / 22.04 ± 0.48</td> <!-- RRN -->
   <td class="is know">54.30 ± 1.60 / 65.62 ± 1.20</td> <!-- ARC-is -->
   <td class="is reason">24.35 ± 2.31 / 62.81 ± 1.08</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is rc">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">49.88 ± 2.38 / 62.27 ± 1.75</td> <!-- ARC-is -->
   <td class="is reason">18.61 ± 6.00 / 61.33 ± 2.93</td> <!-- Winogrande-is -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="is ner">59.70 ± 1.67 / 41.69 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.64 ± 3.09 / 38.48 ± 2.74</td> <!-- ScaLA-is -->
   <td class="is rc">29.68 ± 1.85 / 58.88 ± 0.87</td> <!-- NQiI -->
   <td class="is summ">68.13 ± 0.31 / 20.42 ± 0.65</td> <!-- RRN -->
   <td class="is know">41.76 ± 1.72 / 56.28 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">13.24 ± 4.12 / 56.22 ± 1.89</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="is ner">30.89 ± 4.28 / 24.06 ± 1.93</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.29 ± 3.38 / 35.79 ± 2.12</td> <!-- ScaLA-is -->
   <td class="is rc">32.25 ± 1.89 / 58.20 ± 1.70</td> <!-- NQiI -->
   <td class="is summ">67.58 ± 0.63 / 21.53 ± 0.99</td> <!-- RRN -->
   <td class="is know">55.69 ± 1.49 / 66.84 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">17.50 ± 2.56 / 58.33 ± 1.75</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="is ner">55.09 ± 1.76 / 40.34 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">8.45 ± 1.33 / 51.00 ± 1.95</td> <!-- ScaLA-is -->
   <td class="is rc">29.65 ± 1.09 / 56.96 ± 1.35</td> <!-- NQiI -->
   <td class="is summ">68.27 ± 0.25 / 22.14 ± 0.62</td> <!-- RRN -->
   <td class="is know">30.33 ± 1.72 / 47.81 ± 1.31</td> <!-- ARC-is -->
   <td class="is reason">10.48 ± 2.28 / 54.89 ± 1.49</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="is ner">61.69 ± 2.17 / 41.25 ± 3.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.10 ± 1.61 / 48.74 ± 3.05</td> <!-- ScaLA-is -->
   <td class="is rc">31.52 ± 2.08 / 58.96 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">66.98 ± 1.04 / 19.84 ± 1.97</td> <!-- RRN -->
   <td class="is know">25.16 ± 1.55 / 43.57 ± 1.26</td> <!-- ARC-is -->
   <td class="is reason">1.50 ± 1.22 / 48.33 ± 1.21</td> <!-- Winogrande-is -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="is ner">52.57 ± 2.04 / 36.81 ± 2.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.87 ± 2.28 / 40.95 ± 4.97</td> <!-- ScaLA-is -->
   <td class="is rc">30.12 ± 4.65 / 57.81 ± 4.78</td> <!-- NQiI -->
   <td class="is summ">66.17 ± 0.86 / 18.71 ± 0.89</td> <!-- RRN -->
   <td class="is know">25.93 ± 1.51 / 44.54 ± 1.14</td> <!-- ARC-is -->
   <td class="is reason">8.48 ± 2.66 / 53.76 ± 1.54</td> <!-- Winogrande-is -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="is ner">62.08 ± 2.27 / 51.09 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.58 ± 1.03 / 44.38 ± 3.90</td> <!-- ScaLA-is -->
   <td class="is rc">29.66 ± 3.02 / 56.60 ± 2.22</td> <!-- NQiI -->
   <td class="is summ">66.11 ± 0.85 / 18.74 ± 0.90</td> <!-- RRN -->
   <td class="is know">18.75 ± 1.02 / 38.96 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">7.64 ± 1.91 / 49.40 ± 1.45</td> <!-- Winogrande-is -->
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="is ner">48.70 ± 3.02 / 34.52 ± 2.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.49 ± 2.51 / 43.40 ± 4.41</td> <!-- ScaLA-is -->
   <td class="is rc">29.56 ± 5.47 / 55.53 ± 5.79</td> <!-- NQiI -->
   <td class="is summ">66.34 ± 1.09 / 19.13 ± 0.96</td> <!-- RRN -->
   <td class="is know">26.78 ± 1.59 / 45.17 ± 1.12</td> <!-- ARC-is -->
   <td class="is reason">7.41 ± 3.26 / 52.13 ± 1.97</td> <!-- Winogrande-is -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="is ner">42.15 ± 2.74 / 33.52 ± 3.32</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.49 ± 1.81 / 47.31 ± 3.24</td> <!-- ScaLA-is -->
   <td class="is rc">27.51 ± 3.63 / 56.11 ± 1.65</td> <!-- NQiI -->
   <td class="is summ">66.89 ± 0.34 / 19.60 ± 0.89</td> <!-- RRN -->
   <td class="is know">19.27 ± 1.47 / 39.42 ± 1.10</td> <!-- ARC-is -->
   <td class="is reason">9.45 ± 2.76 / 54.44 ± 1.24</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="is ner">30.61 ± 4.61 / 25.80 ± 3.57</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.60 ± 1.68 / 38.26 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">32.22 ± 3.19 / 55.22 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.03 ± 1.82 / 18.15 ± 2.24</td> <!-- RRN -->
   <td class="is know">32.53 ± 0.82 / 48.03 ± 0.80</td> <!-- ARC-is -->
   <td class="is reason">1.14 ± 1.26 / 39.92 ± 1.92</td> <!-- Winogrande-is -->
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.9.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is rc">22.48 ± 4.43 / 55.51 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">5.19 ± 3.15 / 28.44 ± 2.45</td> <!-- ARC-is -->
   <td class="is reason">12.90 ± 6.92 / 56.88 ± 3.57</td> <!-- Winogrande-is -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- RRN version -->
   <td>9.3.2</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="is ner">50.82 ± 2.72 / 40.35 ± 4.51</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.99 ± 1.54 / 39.38 ± 3.81</td> <!-- ScaLA-is -->
   <td class="is rc">25.74 ± 5.44 / 49.45 ± 5.29</td> <!-- NQiI -->
   <td class="is summ">61.72 ± 3.16 / 16.00 ± 1.82</td> <!-- RRN -->
   <td class="is know">10.78 ± 1.15 / 33.40 ± 0.91</td> <!-- ARC-is -->
   <td class="is reason">3.94 ± 2.97 / 54.60 ± 1.62</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.70 ± 5.36 / 49.31 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.96 ± 3.10 / 16.11 ± 1.80</td> <!-- RRN -->
   <td class="is know">10.25 ± 0.96 / 32.89 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">1.99 ± 2.95 / 54.48 ± 1.27</td> <!-- Winogrande-is -->
   <td>9.1.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.1.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="is ner">56.71 ± 1.98 / 46.71 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">65.39 ± 0.80 / 18.24 ± 1.00</td> <!-- RRN -->
   <td class="is know">9.11 ± 0.92 / 32.06 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">3.30 ± 2.81 / 44.40 ± 1.61</td> <!-- Winogrande-is -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="is ner">49.20 ± 2.64 / 40.79 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.45 ± 1.40 / 51.11 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">24.61 ± 3.36 / 54.99 ± 2.36</td> <!-- NQiI -->
   <td class="is summ">63.74 ± 2.25 / 18.29 ± 1.40</td> <!-- RRN -->
   <td class="is know">8.45 ± 1.35 / 31.54 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">1.14 ± 0.97 / 50.10 ± 0.82</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="is ner">44.68 ± 3.50 / 36.20 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.12 ± 1.68 / 35.09 ± 1.17</td> <!-- ScaLA-is -->
   <td class="is rc">25.52 ± 5.24 / 49.15 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.40 ± 2.38 / 14.90 ± 1.60</td> <!-- RRN -->
   <td class="is know">10.25 ± 1.54 / 32.81 ± 1.22</td> <!-- ARC-is -->
   <td class="is reason">5.24 ± 1.65 / 52.80 ± 2.41</td> <!-- Winogrande-is -->
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="is ner">36.47 ± 4.24 / 30.33 ± 3.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is rc">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="is summ">63.68 ± 1.75 / 16.38 ± 1.24</td> <!-- RRN -->
   <td class="is know">5.12 ± 1.30 / 28.85 ± 0.99</td> <!-- ARC-is -->
   <td class="is reason">8.30 ± 1.28 / 57.35 ± 0.75</td> <!-- Winogrande-is -->
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.3</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is rc">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.01 ± 1.51 / 18.34 ± 1.35</td> <!-- RRN -->
   <td class="is know">5.49 ± 1.98 / 28.73 ± 1.39</td> <!-- ARC-is -->
   <td class="is reason">0.24 ± 0.71 / 38.95 ± 0.84</td> <!-- Winogrande-is -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="is ner">42.04 ± 3.53 / 25.31 ± 1.59</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 32.97 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is rc">24.07 ± 4.63 / 49.31 ± 4.59</td> <!-- NQiI -->
   <td class="is summ">61.80 ± 2.80 / 14.50 ± 2.00</td> <!-- RRN -->
   <td class="is know">13.79 ± 1.55 / 35.23 ± 1.26</td> <!-- ARC-is -->
   <td class="is reason">0.25 ± 2.45 / 48.10 ± 1.67</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.02</td> <!-- ScandEval rank -->
   <td class="is ner">40.71 ± 2.93 / 34.57 ± 4.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is rc">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="is summ">65.25 ± 0.97 / 19.09 ± 1.05</td> <!-- RRN -->
   <td class="is know">5.35 ± 1.32 / 28.11 ± 1.13</td> <!-- ARC-is -->
   <td class="is reason">0.35 ± 2.49 / 51.16 ± 2.74</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.1</td> <!-- Winogrande-is version -->
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
   <td class="is la">0.98 ± 1.44 / 35.86 ± 1.12</td> <!-- ScaLA-is -->
   <td class="is rc">20.39 ± 3.04 / 44.20 ± 2.72</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 2.31 / 14.45 ± 1.79</td> <!-- RRN -->
   <td class="is know">7.59 ± 1.44 / 31.07 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">3.44 ± 2.28 / 46.89 ± 1.02</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4065</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="is ner">37.53 ± 3.42 / 30.51 ± 3.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.14 ± 1.96 / 39.45 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">20.91 ± 2.93 / 43.86 ± 1.90</td> <!-- NQiI -->
   <td class="is summ">66.15 ± 0.59 / 19.08 ± 1.08</td> <!-- RRN -->
   <td class="is know">7.17 ± 1.32 / 30.61 ± 0.94</td> <!-- ARC-is -->
   <td class="is reason">-0.55 ± 2.76 / 47.83 ± 2.20</td> <!-- Winogrande-is -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- RRN version -->
   <td>12.11.0</td> <!-- ARC-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="is summ">62.55 ± 3.03 / 15.26 ± 2.31</td> <!-- RRN -->
   <td class="is know">5.98 ± 1.66 / 28.18 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">-0.51 ± 1.95 / 47.23 ± 2.39</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.2.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="is ner">50.89 ± 2.90 / 35.75 ± 4.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.50 ± 0.94 / 33.77 ± 0.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.43 ± 3.38 / 41.32 ± 3.18</td> <!-- NQiI -->
   <td class="is summ">59.94 ± 2.87 / 12.62 ± 1.91</td> <!-- RRN -->
   <td class="is know">5.52 ± 1.26 / 28.97 ± 0.97</td> <!-- ARC-is -->
   <td class="is reason">1.73 ± 2.31 / 50.89 ± 3.35</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">4.10</td> <!-- ScandEval rank -->
   <td class="is ner">36.56 ± 3.03 / 34.23 ± 3.45</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.73 ± 1.56 / 45.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is rc">21.97 ± 4.26 / 46.27 ± 3.94</td> <!-- NQiI -->
   <td class="is summ">63.50 ± 2.92 / 16.51 ± 2.19</td> <!-- RRN -->
   <td class="is know">5.60 ± 1.25 / 29.83 ± 1.00</td> <!-- ARC-is -->
   <td class="is reason">-5.80 ± 2.91 / 46.82 ± 2.65</td> <!-- Winogrande-is -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">4.10</td> <!-- ScandEval rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">62.80 ± 1.69 / 15.23 ± 1.01</td> <!-- RRN -->
   <td class="is know">5.44 ± 1.14 / 28.13 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">6.35 ± 2.71 / 50.49 ± 1.57</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">4.12</td> <!-- ScandEval rank -->
   <td class="is ner">37.69 ± 3.97 / 34.52 ± 3.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.11 ± 1.49 / 48.48 ± 2.77</td> <!-- ScaLA-is -->
   <td class="is rc">18.34 ± 2.07 / 43.26 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">63.71 ± 1.04 / 16.63 ± 0.98</td> <!-- RRN -->
   <td class="is know">7.70 ± 1.44 / 28.98 ± 1.20</td> <!-- ARC-is -->
   <td class="is reason">-5.17 ± 2.94 / 53.84 ± 1.87</td> <!-- Winogrande-is -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,602 ± 855 / 779 ± 245</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="is ner">27.62 ± 1.70 / 22.55 ± 1.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.62 ± 1.10 / 34.28 ± 1.83</td> <!-- ScaLA-is -->
   <td class="is rc">23.02 ± 2.62 / 51.06 ± 1.56</td> <!-- NQiI -->
   <td class="is summ">62.22 ± 1.82 / 14.45 ± 1.88</td> <!-- RRN -->
   <td class="is know">13.54 ± 1.19 / 35.59 ± 0.88</td> <!-- ARC-is -->
   <td class="is reason">0.50 ± 1.49 / 50.68 ± 1.09</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="is ner">26.28 ± 5.09 / 22.73 ± 3.35</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.17 ± 1.98 / 48.03 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">22.65 ± 3.50 / 45.48 ± 2.99</td> <!-- NQiI -->
   <td class="is summ">62.07 ± 1.73 / 11.04 ± 1.91</td> <!-- RRN -->
   <td class="is know">-0.07 ± 0.85 / 23.51 ± 0.95</td> <!-- ARC-is -->
   <td class="is reason">-2.92 ± 4.86 / 53.55 ± 3.32</td> <!-- Winogrande-is -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.5</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">62.30 ± 0.90 / 13.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.16 ± 0.79 / 27.40 ± 0.79</td> <!-- ARC-is -->
   <td class="is reason">1.84 ± 2.19 / 43.79 ± 0.73</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="is ner">19.39 ± 1.31 / 19.04 ± 1.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.01 ± 1.49 / 34.61 ± 0.73</td> <!-- ScaLA-is -->
   <td class="is rc">20.92 ± 3.41 / 51.75 ± 2.10</td> <!-- NQiI -->
   <td class="is summ">66.55 ± 0.34 / 18.80 ± 0.51</td> <!-- RRN -->
   <td class="is know">6.02 ± 1.50 / 29.00 ± 1.28</td> <!-- ARC-is -->
   <td class="is reason">-2.37 ± 1.71 / 39.83 ± 3.57</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="is ner">14.79 ± 4.70 / 13.03 ± 2.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.10 ± 1.54 / 34.67 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.42 ± 1.09 / 51.72 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">62.67 ± 1.62 / 16.91 ± 1.38</td> <!-- RRN -->
   <td class="is know">10.76 ± 1.56 / 32.34 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-5.20 ± 1.82 / 53.08 ± 0.91</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.33 / 26.91 ± 1.00</td> <!-- ARC-is -->
   <td class="is reason">-0.00 ± 2.41 / 44.93 ± 0.92</td> <!-- Winogrande-is -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="is ner">27.22 ± 3.65 / 24.21 ± 2.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.31 ± 1.28 / 39.67 ± 4.39</td> <!-- ScaLA-is -->
   <td class="is rc">17.24 ± 2.72 / 41.15 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.66 / 15.80 ± 1.12</td> <!-- RRN -->
   <td class="is know">1.85 ± 1.18 / 26.88 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">1.06 ± 2.84 / 47.19 ± 2.14</td> <!-- Winogrande-is -->
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="is ner">34.62 ± 4.64 / 33.25 ± 4.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.24 ± 1.43 / 33.75 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is rc">18.10 ± 1.85 / 43.52 ± 0.87</td> <!-- NQiI -->
   <td class="is summ">61.81 ± 0.98 / 15.04 ± 0.70</td> <!-- RRN -->
   <td class="is know">3.06 ± 1.01 / 28.01 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">-1.90 ± 2.28 / 44.34 ± 1.19</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="is ner">33.05 ± 4.29 / 29.75 ± 3.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 1.18 / 34.80 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">17.23 ± 2.51 / 39.88 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">60.08 ± 1.45 / 13.80 ± 0.81</td> <!-- RRN -->
   <td class="is know">2.67 ± 1.35 / 27.04 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">2.74 ± 2.28 / 53.18 ± 0.93</td> <!-- Winogrande-is -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.5</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">4.26</td> <!-- ScandEval rank -->
   <td class="is ner">27.44 ± 3.28 / 23.50 ± 3.29</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.46 ± 1.18 / 41.20 ± 3.25</td> <!-- ScaLA-is -->
   <td class="is rc">17.26 ± 3.80 / 39.06 ± 3.00</td> <!-- NQiI -->
   <td class="is summ">58.30 ± 4.50 / 14.03 ± 2.00</td> <!-- RRN -->
   <td class="is know">2.14 ± 1.25 / 25.83 ± 1.11</td> <!-- ARC-is -->
   <td class="is reason">2.43 ± 2.93 / 55.15 ± 1.40</td> <!-- Winogrande-is -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="is ner">36.59 ± 3.56 / 27.50 ± 2.53</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.86 ± 2.41 / 36.44 ± 1.27</td> <!-- ScaLA-is -->
   <td class="is rc">14.58 ± 2.13 / 37.44 ± 1.86</td> <!-- NQiI -->
   <td class="is summ">61.99 ± 1.16 / 15.07 ± 0.81</td> <!-- RRN -->
   <td class="is know">1.48 ± 1.63 / 23.23 ± 0.93</td> <!-- ARC-is -->
   <td class="is reason">-0.98 ± 2.63 / 56.13 ± 0.62</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="is ner">34.76 ± 4.42 / 23.42 ± 2.33</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.77 ± 1.05 / 39.63 ± 2.41</td> <!-- ScaLA-is -->
   <td class="is rc">12.80 ± 2.37 / 30.77 ± 2.12</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 1.78 / 15.53 ± 0.95</td> <!-- RRN -->
   <td class="is know">2.01 ± 0.96 / 25.83 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-0.76 ± 3.69 / 53.64 ± 2.57</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="is ner">27.96 ± 3.08 / 25.78 ± 3.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.00 ± 1.28 / 35.53 ± 1.87</td> <!-- ScaLA-is -->
   <td class="is rc">23.17 ± 2.78 / 44.72 ± 2.82</td> <!-- NQiI -->
   <td class="is summ">55.57 ± 4.13 / 9.41 ± 1.58</td> <!-- RRN -->
   <td class="is know">0.94 ± 1.26 / 22.66 ± 0.57</td> <!-- ARC-is -->
   <td class="is reason">-2.72 ± 3.17 / 53.79 ± 1.42</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="is ner">33.76 ± 3.44 / 32.21 ± 2.82</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.13 ± 1.34 / 42.66 ± 3.62</td> <!-- ScaLA-is -->
   <td class="is rc">12.43 ± 2.62 / 33.38 ± 1.39</td> <!-- NQiI -->
   <td class="is summ">59.46 ± 2.42 / 13.23 ± 1.87</td> <!-- RRN -->
   <td class="is know">2.09 ± 1.34 / 25.68 ± 0.67</td> <!-- ARC-is -->
   <td class="is reason">3.56 ± 2.07 / 56.72 ± 0.99</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="is ner">38.52 ± 3.25 / 28.84 ± 5.49</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.94 ± 2.60 / 36.06 ± 2.17</td> <!-- NQiI -->
   <td class="is summ">58.58 ± 4.00 / 12.91 ± 2.09</td> <!-- RRN -->
   <td class="is know">2.11 ± 1.02 / 27.80 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-4.75 ± 2.84 / 50.40 ± 4.21</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
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
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="is ner">21.41 ± 5.01 / 19.94 ± 5.01</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 42.86 ± 2.68</td> <!-- ScaLA-is -->
   <td class="is rc">22.54 ± 1.74 / 44.93 ± 1.92</td> <!-- NQiI -->
   <td class="is summ">57.33 ± 2.62 / 10.47 ± 1.06</td> <!-- RRN -->
   <td class="is know">0.97 ± 1.29 / 26.73 ± 0.99</td> <!-- ARC-is -->
   <td class="is reason">-0.36 ± 2.40 / 44.44 ± 1.08</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="is ner">10.67 ± 5.23 / 13.01 ± 3.26</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.21 ± 0.99 / 33.71 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">20.22 ± 3.01 / 43.48 ± 2.32</td> <!-- NQiI -->
   <td class="is summ">59.97 ± 2.49 / 13.32 ± 2.03</td> <!-- RRN -->
   <td class="is know">10.08 ± 1.82 / 32.08 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">1.16 ± 2.48 / 51.00 ± 1.70</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="is ner">1.42 ± 1.60 / 3.11 ± 1.85</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.75 ± 0.73 / 45.87 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">23.33 ± 2.22 / 45.28 ± 1.58</td> <!-- NQiI -->
   <td class="is summ">64.23 ± 1.78 / 15.08 ± 2.03</td> <!-- RRN -->
   <td class="is know">0.40 ± 1.88 / 23.35 ± 1.22</td> <!-- ARC-is -->
   <td class="is reason">0.68 ± 4.15 / 50.85 ± 2.65</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is rc">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="is summ">62.11 ± 2.22 / 14.98 ± 1.53</td> <!-- RRN -->
   <td class="is know">4.50 ± 1.47 / 28.86 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">-1.89 ± 2.66 / 43.72 ± 0.92</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="is ner">17.79 ± 1.18 / 18.12 ± 1.18</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.08 ± 0.15 / 33.73 ± 0.26</td> <!-- ScaLA-is -->
   <td class="is rc">15.04 ± 2.53 / 34.77 ± 1.72</td> <!-- NQiI -->
   <td class="is summ">59.45 ± 1.99 / 12.89 ± 1.04</td> <!-- RRN -->
   <td class="is know">1.06 ± 1.26 / 22.59 ± 0.63</td> <!-- ARC-is -->
   <td class="is reason">5.69 ± 2.26 / 56.71 ± 0.87</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">4.46</td> <!-- ScandEval rank -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="is summ">60.00 ± 2.62 / 13.07 ± 1.31</td> <!-- RRN -->
   <td class="is know">2.52 ± 1.20 / 26.23 ± 1.40</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 2.53 / 56.42 ± 0.98</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">4.47</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">16.91 ± 2.57 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="is summ">60.02 ± 3.15 / 14.22 ± 1.52</td> <!-- RRN -->
   <td class="is know">4.35 ± 1.25 / 28.94 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">0.72 ± 2.33 / 52.54 ± 2.18</td> <!-- Winogrande-is -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">4.52</td> <!-- ScandEval rank -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">57.17 ± 3.07 / 11.73 ± 1.00</td> <!-- RRN -->
   <td class="is know">5.46 ± 1.45 / 29.23 ± 1.11</td> <!-- ARC-is -->
   <td class="is reason">-1.71 ± 3.79 / 50.88 ± 1.29</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is rc">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 0.96 / 9.92 ± 1.05</td> <!-- RRN -->
   <td class="is know">0.45 ± 1.44 / 22.94 ± 0.76</td> <!-- ARC-is -->
   <td class="is reason">0.62 ± 1.42 / 56.02 ± 0.95</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">4.56</td> <!-- ScandEval rank -->
   <td class="is ner">17.77 ± 6.81 / 16.42 ± 6.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 1.50 / 34.29 ± 1.64</td> <!-- ScaLA-is -->
   <td class="is rc">8.15 ± 2.21 / 30.75 ± 2.05</td> <!-- NQiI -->
   <td class="is summ">54.21 ± 3.27 / 11.06 ± 1.56</td> <!-- RRN -->
   <td class="is know">0.71 ± 1.34 / 25.40 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">2.88 ± 1.84 / 54.45 ± 2.60</td> <!-- Winogrande-is -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">4.64</td> <!-- ScandEval rank -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">57.27 ± 1.42 / 10.43 ± 0.97</td> <!-- RRN -->
   <td class="is know">1.62 ± 1.18 / 25.09 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">1.92 ± 2.32 / 50.07 ± 2.68</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.45 / 26.36 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.13 ± 3.74 / 52.30 ± 2.26</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">4.66</td> <!-- ScandEval rank -->
   <td class="is ner">24.98 ± 5.71 / 25.35 ± 4.78</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.18 ± 1.09 / 39.01 ± 2.76</td> <!-- ScaLA-is -->
   <td class="is rc">8.52 ± 2.30 / 21.32 ± 2.25</td> <!-- NQiI -->
   <td class="is summ">39.94 ± 9.39 / 5.18 ± 1.53</td> <!-- RRN -->
   <td class="is know">4.83 ± 1.40 / 29.14 ± 1.10</td> <!-- ARC-is -->
   <td class="is reason">4.70 ± 2.96 / 56.56 ± 0.97</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.3.2</td> <!-- Winogrande-is version -->
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
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is rc">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="is summ">58.92 ± 1.57 / 10.09 ± 1.41</td> <!-- RRN -->
   <td class="is know">-1.28 ± 1.48 / 24.82 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.48 ± 3.56 / 53.95 ± 2.45</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">1.96 ± 1.72 / 25.55 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">0.85 ± 1.91 / 52.12 ± 2.92</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="is ner">23.67 ± 5.16 / 23.19 ± 4.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 14.61 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">50.54 ± 0.14 / 3.11 ± 0.06</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 22.04 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 56.52 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.86</td> <!-- ScandEval rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is rc">1.04 ± 0.96 / 7.35 ± 3.52</td> <!-- NQiI -->
   <td class="is summ">55.16 ± 1.26 / 10.52 ± 1.13</td> <!-- RRN -->
   <td class="is know">-0.80 ± 2.00 / 23.89 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">-0.16 ± 0.86 / 32.02 ± 2.77</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">5.15</td> <!-- ScandEval rank -->
   <td class="is ner">1.68 ± 1.40 / 1.54 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.38 ± 1.13 / 34.41 ± 2.16</td> <!-- ScaLA-is -->
   <td class="is rc">0.08 ± 0.09 / 10.05 ± 2.08</td> <!-- NQiI -->
   <td class="is summ">44.02 ± 1.31 / 6.35 ± 0.43</td> <!-- RRN -->
   <td class="is know">0.15 ± 1.45 / 23.95 ± 1.29</td> <!-- ARC-is -->
   <td class="is reason">0.28 ± 1.39 / 32.09 ± 2.15</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">5.16</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 3.90 ± 0.28</td> <!-- NQiI -->
   <td class="is summ">44.80 ± 0.65 / 3.34 ± 0.08</td> <!-- RRN -->
   <td class="is know">0.23 ± 0.75 / 22.11 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.38 ± 0.75 / 56.53 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">5.19</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.64 ± 0.34</td> <!-- NQiI -->
   <td class="is summ">42.46 ± 0.47 / 3.58 ± 0.45</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 22.04 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 56.52 ± 0.89</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- ARC-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.58</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">-0.02 ± 1.16 / 22.75 ± 0.50</td> <!-- ARC-is -->
   <td class="is reason">0.47 ± 4.14 / 46.93 ± 3.13</td> <!-- Winogrande-is -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
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
   <td class="rank">5.85</td> <!-- ScandEval rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NQiI -->
   <td class="is summ">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- RRN -->
   <td class="is know">-0.26 ± 0.90 / 22.02 ± 0.48</td> <!-- ARC-is -->
   <td class="is reason">-0.01 ± 1.21 / 55.08 ± 0.99</td> <!-- Winogrande-is -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
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
  <a href="https://scandeval.com/icelandic-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Icelandic NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-TVzaJ&quot; src=&quot;https://datawrapper.dwcdn.net/TVzaJ/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
