---
layout: leaderboard
title: Insular Scandinavian NLU
---

<center>Last updated: 25/01/2024 10:08:04 CET</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="insular-scandinavian-nlu" class="sortable fixed centered small-font">
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
  </tr>
 </thead>
 <tbody>
  <tr>
   <td class="rank">1</td> <!-- Rank -->
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,152 ± 2,029 / 2,282 ± 736</td> <!-- Model inference speed -->
   <td class="score">64.08 ± 2.41</td> <!-- ScandEval score -->
   <td class="is-score">51.03 ± 2.44</td> <!-- Icelandic score -->
   <td class="fo-score">77.14 ± 2.38</td> <!-- Faroese score -->
   <td class="is ner">83.92 ± 0.81 / 84.37 ± 0.80</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.40 ± 4.18 / 72.77 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">17.76 ± 2.33 / 36.98 ± 3.29</td> <!-- NQiI -->
   <td class="fo ner">91.31 ± 0.69 / 91.79 ± 0.47</td> <!-- FoNE -->
   <td class="fo la">62.96 ± 4.08 / 80.59 ± 2.79</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">2</td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score">61.55 ± 1.58</td> <!-- ScandEval score -->
   <td class="is-score">55.39 ± 1.79</td> <!-- Icelandic score -->
   <td class="fo-score">67.70 ± 1.36</td> <!-- Faroese score -->
   <td class="is ner">81.12 ± 2.02 / 81.48 ± 1.69</td> <!-- MIM-GOLD-NER -->
   <td class="is la">54.11 ± 2.40 / 76.46 ± 1.28</td> <!-- ScaLA-is -->
   <td class="is qa">30.93 ± 0.96 / 56.17 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">88.60 ± 0.60 / 89.37 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">46.81 ± 2.12 / 72.76 ± 1.40</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">3</td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,446 ± 2,845 / 3,199 ± 1,038</td> <!-- Model inference speed -->
   <td class="score">57.14 ± 4.09</td> <!-- ScandEval score -->
   <td class="is-score">46.53 ± 2.06</td> <!-- Icelandic score -->
   <td class="fo-score">67.75 ± 6.12</td> <!-- Faroese score -->
   <td class="is ner">81.83 ± 1.65 / 82.24 ± 1.04</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.09 ± 3.83 / 73.24 ± 2.23</td> <!-- ScaLA-is -->
   <td class="is qa">6.66 ± 0.69 / 33.95 ± 0.75</td> <!-- NQiI -->
   <td class="fo ner">90.52 ± 0.47 / 90.83 ± 0.40</td> <!-- FoNE -->
   <td class="fo la">44.99 ± 11.76 / 71.54 ± 5.83</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">4</td> <!-- Rank -->
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,126 ± 1,911 / 2,280 ± 740</td> <!-- Model inference speed -->
   <td class="score">55.57 ± 3.71</td> <!-- ScandEval score -->
   <td class="is-score">56.50 ± 1.37</td> <!-- Icelandic score -->
   <td class="fo-score">54.64 ± 6.05</td> <!-- Faroese score -->
   <td class="is ner">84.08 ± 0.93 / 84.85 ± 0.84</td> <!-- MIM-GOLD-NER -->
   <td class="is la">57.27 ± 2.13 / 77.76 ± 1.43</td> <!-- ScaLA-is -->
   <td class="is qa">28.16 ± 1.04 / 50.58 ± 1.21</td> <!-- NQiI -->
   <td class="fo ner">88.14 ± 0.58 / 88.89 ± 0.52</td> <!-- FoNE -->
   <td class="fo la">21.15 ± 11.53 / 56.84 ± 8.97</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">5</td> <!-- Rank -->
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,656 ± 2,894 / 3,246 ± 1,051</td> <!-- Model inference speed -->
   <td class="score">53.36 ± 3.84</td> <!-- ScandEval score -->
   <td class="is-score">50.29 ± 1.54</td> <!-- Icelandic score -->
   <td class="fo-score">56.43 ± 6.14</td> <!-- Faroese score -->
   <td class="is ner">82.83 ± 1.33 / 83.39 ± 1.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">55.99 ± 2.32 / 75.49 ± 1.72</td> <!-- ScaLA-is -->
   <td class="is qa">12.06 ± 0.96 / 44.52 ± 2.84</td> <!-- NQiI -->
   <td class="fo ner">87.79 ± 0.40 / 88.46 ± 0.31</td> <!-- FoNE -->
   <td class="fo la">25.07 ± 11.88 / 59.43 ± 7.78</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">6</td> <!-- Rank -->
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,695 ± 77 / 2,369 ± 772</td> <!-- Model inference speed -->
   <td class="score">53.26 ± 1.25</td> <!-- ScandEval score -->
   <td class="is-score">48.18 ± 1.20</td> <!-- Icelandic score -->
   <td class="fo-score">58.34 ± 1.30</td> <!-- Faroese score -->
   <td class="is ner">77.40 ± 0.48 / 78.58 ± 0.56</td> <!-- MIM-GOLD-NER -->
   <td class="is la">60.64 ± 1.44 / 79.20 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is qa">6.51 ± 1.69 / 22.61 ± 5.24</td> <!-- NQiI -->
   <td class="fo ner">85.80 ± 0.25 / 86.58 ± 0.26</td> <!-- FoNE -->
   <td class="fo la">30.88 ± 2.36 / 63.79 ± 1.33</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">7</td> <!-- Rank -->
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,196 ± 3,299 / 2,383 ± 768</td> <!-- Model inference speed -->
   <td class="score">53.17 ± 3.45</td> <!-- ScandEval score -->
   <td class="is-score">45.52 ± 1.81</td> <!-- Icelandic score -->
   <td class="fo-score">60.83 ± 5.09</td> <!-- Faroese score -->
   <td class="is ner">80.91 ± 1.24 / 81.30 ± 0.97</td> <!-- MIM-GOLD-NER -->
   <td class="is la">41.91 ± 3.45 / 67.96 ± 2.53</td> <!-- ScaLA-is -->
   <td class="is qa">13.73 ± 0.73 / 52.73 ± 0.85</td> <!-- NQiI -->
   <td class="fo ner">88.81 ± 0.65 / 89.12 ± 0.56</td> <!-- FoNE -->
   <td class="fo la">32.85 ± 9.54 / 63.53 ± 5.62</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">8</td> <!-- Rank -->
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,052 ± 3,261 / 2,357 ± 761</td> <!-- Model inference speed -->
   <td class="score">51.81 ± 3.41</td> <!-- ScandEval score -->
   <td class="is-score">43.04 ± 3.19</td> <!-- Icelandic score -->
   <td class="fo-score">60.59 ± 3.62</td> <!-- Faroese score -->
   <td class="is ner">80.45 ± 1.29 / 81.01 ± 1.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">36.92 ± 7.62 / 66.07 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is qa">11.75 ± 0.66 / 46.17 ± 1.42</td> <!-- NQiI -->
   <td class="fo ner">89.29 ± 0.63 / 89.58 ± 0.61</td> <!-- FoNE -->
   <td class="fo la">31.89 ± 6.62 / 64.32 ± 4.10</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">9</td> <!-- Rank -->
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,270 ± 467 / 972 ± 303</td> <!-- Model inference speed -->
   <td class="score">51.45 ± 4.03</td> <!-- ScandEval score -->
   <td class="is-score">51.91 ± 2.04</td> <!-- Icelandic score -->
   <td class="fo-score">51.00 ± 6.03</td> <!-- Faroese score -->
   <td class="is ner">78.05 ± 1.72 / 78.74 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">48.29 ± 2.59 / 73.54 ± 1.99</td> <!-- ScaLA-is -->
   <td class="is qa">29.38 ± 1.81 / 52.42 ± 3.00</td> <!-- NQiI -->
   <td class="fo ner">87.35 ± 0.94 / 87.65 ± 0.94</td> <!-- FoNE -->
   <td class="fo la">14.65 ± 11.12 / 46.36 ± 10.23</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">10</td> <!-- Rank -->
   <td>mideind/IceBERT-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,338 ± 907 / 2,575 ± 812</td> <!-- Model inference speed -->
   <td class="score">49.40 ± 2.46</td> <!-- ScandEval score -->
   <td class="is-score">52.05 ± 2.00</td> <!-- Icelandic score -->
   <td class="fo-score">46.76 ± 2.92</td> <!-- Faroese score -->
   <td class="is ner">84.07 ± 1.71 / 83.41 ± 1.21</td> <!-- MIM-GOLD-NER -->
   <td class="is la">57.71 ± 3.37 / 77.39 ± 1.67</td> <!-- ScaLA-is -->
   <td class="is qa">14.38 ± 0.93 / 49.68 ± 0.63</td> <!-- NQiI -->
   <td class="fo ner">86.84 ± 0.77 / 87.51 ± 0.72</td> <!-- FoNE -->
   <td class="fo la">6.67 ± 5.07 / 47.16 ± 5.02</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">11</td> <!-- Rank -->
   <td>vesteinn/XLMR-ENIS</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,060 ± 2,967 / 2,958 ± 944</td> <!-- Model inference speed -->
   <td class="score">48.55 ± 2.46</td> <!-- ScandEval score -->
   <td class="is-score">52.67 ± 3.37</td> <!-- Icelandic score -->
   <td class="fo-score">44.44 ± 1.54</td> <!-- Faroese score -->
   <td class="is ner">82.65 ± 1.43 / 83.27 ± 1.05</td> <!-- MIM-GOLD-NER -->
   <td class="is la">48.40 ± 7.64 / 71.25 ± 4.65</td> <!-- ScaLA-is -->
   <td class="is qa">26.95 ± 1.04 / 51.18 ± 1.16</td> <!-- NQiI -->
   <td class="fo ner">87.09 ± 0.76 / 87.71 ± 0.73</td> <!-- FoNE -->
   <td class="fo la">1.79 ± 2.32 / 41.08 ± 4.14</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">12=</td> <!-- Rank -->
   <td>vesteinn/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,147 ± 2,182 / 5,325 ± 1,725</td> <!-- Model inference speed -->
   <td class="score">48.23 ± 2.61</td> <!-- ScandEval score -->
   <td class="is-score">50.97 ± 3.63</td> <!-- Icelandic score -->
   <td class="fo-score">45.48 ± 1.59</td> <!-- Faroese score -->
   <td class="is ner">84.31 ± 1.70 / 84.16 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">54.98 ± 8.26 / 74.40 ± 6.38</td> <!-- ScaLA-is -->
   <td class="is qa">13.63 ± 0.92 / 49.04 ± 1.39</td> <!-- NQiI -->
   <td class="fo ner">87.13 ± 0.58 / 87.70 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">3.83 ± 2.60 / 42.67 ± 4.55</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">12=</td> <!-- Rank -->
   <td>mideind/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,236 ± 1,482 / 3,412 ± 1,114</td> <!-- Model inference speed -->
   <td class="score">47.46 ± 3.18</td> <!-- ScandEval score -->
   <td class="is-score">49.82 ± 4.54</td> <!-- Icelandic score -->
   <td class="fo-score">45.10 ± 1.82</td> <!-- Faroese score -->
   <td class="is ner">85.08 ± 1.64 / 85.04 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">50.69 ± 10.67 / 70.79 ± 7.79</td> <!-- ScaLA-is -->
   <td class="is qa">13.69 ± 1.30 / 50.12 ± 1.24</td> <!-- NQiI -->
   <td class="fo ner">86.50 ± 0.96 / 87.11 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">3.70 ± 2.69 / 44.11 ± 4.60</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">13=</td> <!-- Rank -->
   <td>mideind/IceBERT-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,034 ± 2,028 / 5,237 ± 1,692</td> <!-- Model inference speed -->
   <td class="score">46.56 ± 3.37</td> <!-- ScandEval score -->
   <td class="is-score">47.79 ± 5.09</td> <!-- Icelandic score -->
   <td class="fo-score">45.33 ± 1.64</td> <!-- Faroese score -->
   <td class="is ner">85.58 ± 0.62 / 85.38 ± 0.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">46.52 ± 13.11 / 71.02 ± 6.34</td> <!-- ScaLA-is -->
   <td class="is qa">11.28 ± 1.55 / 42.98 ± 3.10</td> <!-- NQiI -->
   <td class="fo ner">87.22 ± 0.68 / 87.92 ± 0.59</td> <!-- FoNE -->
   <td class="fo la">3.44 ± 2.60 / 44.91 ± 4.11</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">13=</td> <!-- Rank -->
   <td>mideind/IceBERT-igc</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,855 ± 2,025 / 5,197 ± 1,682</td> <!-- Model inference speed -->
   <td class="score">46.10 ± 1.69</td> <!-- ScandEval score -->
   <td class="is-score">49.59 ± 1.32</td> <!-- Icelandic score -->
   <td class="fo-score">42.60 ± 2.05</td> <!-- Faroese score -->
   <td class="is ner">81.52 ± 0.72 / 80.56 ± 0.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">56.92 ± 2.63 / 76.46 ± 1.88</td> <!-- ScaLA-is -->
   <td class="is qa">10.33 ± 0.62 / 40.68 ± 1.78</td> <!-- NQiI -->
   <td class="fo ner">83.82 ± 0.98 / 84.34 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">1.39 ± 3.13 / 47.27 ± 3.55</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">14</td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,744 ± 947 / 1,059 ± 347</td> <!-- Model inference speed -->
   <td class="score">45.49 ± 3.45</td> <!-- ScandEval score -->
   <td class="is-score">46.01 ± 4.61</td> <!-- Icelandic score -->
   <td class="fo-score">44.97 ± 2.29</td> <!-- Faroese score -->
   <td class="is ner">83.42 ± 1.18 / 83.78 ± 0.99</td> <!-- MIM-GOLD-NER -->
   <td class="is la">37.09 ± 11.29 / 64.92 ± 8.32</td> <!-- ScaLA-is -->
   <td class="is qa">17.53 ± 1.36 / 54.28 ± 0.94</td> <!-- NQiI -->
   <td class="fo ner">87.85 ± 0.95 / 88.21 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">2.09 ± 3.64 / 43.63 ± 5.33</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">15=</td> <!-- Rank -->
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,105 ± 2,072 / 2,126 ± 699</td> <!-- Model inference speed -->
   <td class="score">44.94 ± 5.06</td> <!-- ScandEval score -->
   <td class="is-score">38.44 ± 4.83</td> <!-- Icelandic score -->
   <td class="fo-score">51.44 ± 5.29</td> <!-- Faroese score -->
   <td class="is ner">83.20 ± 0.88 / 83.54 ± 0.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">24.42 ± 12.95 / 57.63 ± 7.71</td> <!-- ScaLA-is -->
   <td class="is qa">7.70 ± 0.65 / 33.44 ± 0.61</td> <!-- NQiI -->
   <td class="fo ner">90.60 ± 0.45 / 90.78 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">12.29 ± 10.13 / 53.62 ± 5.94</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">15=</td> <!-- Rank -->
   <td>mideind/IceBERT-mC4-is</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,986 ± 2,086 / 5,282 ± 1,691</td> <!-- Model inference speed -->
   <td class="score">42.83 ± 2.67</td> <!-- ScandEval score -->
   <td class="is-score">35.52 ± 2.72</td> <!-- Icelandic score -->
   <td class="fo-score">50.13 ± 2.62</td> <!-- Faroese score -->
   <td class="is ner">79.19 ± 0.96 / 80.35 ± 0.69</td> <!-- MIM-GOLD-NER -->
   <td class="is la">20.95 ± 5.57 / 50.96 ± 5.04</td> <!-- ScaLA-is -->
   <td class="is qa">6.42 ± 1.63 / 32.41 ± 3.19</td> <!-- NQiI -->
   <td class="fo ner">88.44 ± 0.35 / 89.11 ± 0.38</td> <!-- FoNE -->
   <td class="fo la">11.83 ± 4.90 / 48.95 ± 6.81</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">16</td> <!-- Rank -->
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,714 ± 932 / 1,032 ± 335</td> <!-- Model inference speed -->
   <td class="score">39.98 ± 2.13</td> <!-- ScandEval score -->
   <td class="is-score">34.33 ± 3.18</td> <!-- Icelandic score -->
   <td class="fo-score">45.62 ± 1.09</td> <!-- Faroese score -->
   <td class="is ner">78.43 ± 1.53 / 79.30 ± 1.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">10.78 ± 7.04 / 53.28 ± 3.97</td> <!-- ScaLA-is -->
   <td class="is qa">13.79 ± 0.96 / 54.20 ± 1.31</td> <!-- NQiI -->
   <td class="fo ner">88.39 ± 0.86 / 88.75 ± 0.75</td> <!-- FoNE -->
   <td class="fo la">2.85 ± 1.32 / 48.43 ± 2.29</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">17=</td> <!-- Rank -->
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,359 ± 2,224 / 1,712 ± 558</td> <!-- Model inference speed -->
   <td class="score">39.80 ± 2.85</td> <!-- ScandEval score -->
   <td class="is-score">28.94 ± 1.77</td> <!-- Icelandic score -->
   <td class="fo-score">50.66 ± 3.94</td> <!-- Faroese score -->
   <td class="is ner">74.65 ± 1.65 / 75.83 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.89 ± 3.00 / 44.63 ± 4.01</td> <!-- ScaLA-is -->
   <td class="is qa">9.29 ± 0.66 / 41.76 ± 1.89</td> <!-- NQiI -->
   <td class="fo ner">86.09 ± 1.03 / 86.85 ± 1.02</td> <!-- FoNE -->
   <td class="fo la">15.24 ± 6.84 / 50.54 ± 4.85</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">17=</td> <!-- Rank -->
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,116 ± 2,084 / 2,119 ± 696</td> <!-- Model inference speed -->
   <td class="score">39.65 ± 2.01</td> <!-- ScandEval score -->
   <td class="is-score">36.62 ± 2.20</td> <!-- Icelandic score -->
   <td class="fo-score">42.68 ± 1.81</td> <!-- Faroese score -->
   <td class="is ner">72.69 ± 0.79 / 73.57 ± 1.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">28.72 ± 5.29 / 60.29 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">8.46 ± 0.51 / 31.01 ± 0.72</td> <!-- NQiI -->
   <td class="fo ner">83.96 ± 0.80 / 84.63 ± 0.76</td> <!-- FoNE -->
   <td class="fo la">1.40 ± 2.83 / 40.57 ± 4.05</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">18</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">37.75 ± 3.82</td> <!-- ScandEval score -->
   <td class="is-score">35.12 ± 3.48</td> <!-- Icelandic score -->
   <td class="fo-score">40.39 ± 4.16</td> <!-- Faroese score -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">19=</td> <!-- Rank -->
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,880 ± 2,705 / 3,529 ± 1,145</td> <!-- Model inference speed -->
   <td class="score">37.67 ± 1.83</td> <!-- ScandEval score -->
   <td class="is-score">30.20 ± 1.53</td> <!-- Icelandic score -->
   <td class="fo-score">45.13 ± 2.12</td> <!-- Faroese score -->
   <td class="is ner">73.81 ± 0.85 / 75.02 ± 0.89</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.23 ± 2.63 / 45.40 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">10.57 ± 1.12 / 42.39 ± 1.52</td> <!-- NQiI -->
   <td class="fo ner">86.62 ± 0.43 / 87.31 ± 0.44</td> <!-- FoNE -->
   <td class="fo la">3.64 ± 3.82 / 49.77 ± 2.26</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">19=</td> <!-- Rank -->
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,943 ± 2,072 / 2,074 ± 707</td> <!-- Model inference speed -->
   <td class="score">37.39 ± 1.81</td> <!-- ScandEval score -->
   <td class="is-score">31.47 ± 1.84</td> <!-- Icelandic score -->
   <td class="fo-score">43.32 ± 1.79</td> <!-- Faroese score -->
   <td class="is ner">78.01 ± 2.18 / 79.20 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.92 ± 1.91 / 46.95 ± 3.38</td> <!-- ScaLA-is -->
   <td class="is qa">10.47 ± 1.42 / 43.32 ± 3.55</td> <!-- NQiI -->
   <td class="fo ner">85.97 ± 1.12 / 86.52 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.67 ± 2.46 / 45.51 ± 4.09</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">20=</td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,735 ± 3,187 / 2,618 ± 865</td> <!-- Model inference speed -->
   <td class="score">36.35 ± 1.48</td> <!-- ScandEval score -->
   <td class="is-score">26.52 ± 1.43</td> <!-- Icelandic score -->
   <td class="fo-score">46.19 ± 1.53</td> <!-- Faroese score -->
   <td class="is ner">69.04 ± 1.65 / 71.18 ± 1.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.34 ± 1.87 / 44.43 ± 4.20</td> <!-- ScaLA-is -->
   <td class="is qa">7.17 ± 0.77 / 30.71 ± 1.15</td> <!-- NQiI -->
   <td class="fo ner">86.10 ± 0.64 / 86.75 ± 0.57</td> <!-- FoNE -->
   <td class="fo la">6.28 ± 2.41 / 49.62 ± 2.08</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">20=</td> <!-- Rank -->
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,814 ± 2,015 / 2,093 ± 695</td> <!-- Model inference speed -->
   <td class="score">36.07 ± 1.98</td> <!-- ScandEval score -->
   <td class="is-score">29.12 ± 2.33</td> <!-- Icelandic score -->
   <td class="fo-score">43.02 ± 1.64</td> <!-- Faroese score -->
   <td class="is ner">77.09 ± 2.00 / 78.38 ± 1.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.71 ± 3.02 / 42.83 ± 4.18</td> <!-- ScaLA-is -->
   <td class="is qa">8.56 ± 1.96 / 37.41 ± 5.69</td> <!-- NQiI -->
   <td class="fo ner">85.58 ± 1.04 / 86.23 ± 1.03</td> <!-- FoNE -->
   <td class="fo la">0.45 ± 2.24 / 46.54 ± 2.82</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">21</td> <!-- Rank -->
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,028 ± 868 / 1,342 ± 432</td> <!-- Model inference speed -->
   <td class="score">36.06 ± 1.34</td> <!-- ScandEval score -->
   <td class="is-score">28.41 ± 1.13</td> <!-- Icelandic score -->
   <td class="fo-score">43.72 ± 1.55</td> <!-- Faroese score -->
   <td class="is ner">72.94 ± 1.39 / 74.60 ± 1.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.17 ± 1.27 / 42.59 ± 4.67</td> <!-- ScaLA-is -->
   <td class="is qa">10.11 ± 0.73 / 34.64 ± 2.04</td> <!-- NQiI -->
   <td class="fo ner">86.07 ± 0.65 / 86.54 ± 0.58</td> <!-- FoNE -->
   <td class="fo la">1.37 ± 2.46 / 39.78 ± 3.24</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">22=</td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,093 ± 825 / 1,358 ± 442</td> <!-- Model inference speed -->
   <td class="score">35.14 ± 1.85</td> <!-- ScandEval score -->
   <td class="is-score">25.10 ± 1.44</td> <!-- Icelandic score -->
   <td class="fo-score">45.17 ± 2.25</td> <!-- Faroese score -->
   <td class="is ner">63.35 ± 1.41 / 66.01 ± 1.32</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.94 ± 2.20 / 46.79 ± 2.19</td> <!-- ScaLA-is -->
   <td class="is qa">7.02 ± 0.72 / 34.05 ± 1.35</td> <!-- NQiI -->
   <td class="fo ner">82.76 ± 0.95 / 83.43 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">7.58 ± 3.56 / 52.05 ± 1.14</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">22=</td> <!-- Rank -->
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,705 ± 1,913 / 2,554 ± 829</td> <!-- Model inference speed -->
   <td class="score">34.93 ± 1.55</td> <!-- ScandEval score -->
   <td class="is-score">25.89 ± 1.72</td> <!-- Icelandic score -->
   <td class="fo-score">43.97 ± 1.39</td> <!-- Faroese score -->
   <td class="is ner">65.22 ± 1.51 / 67.74 ± 1.51</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.97 ± 0.94 / 41.31 ± 4.15</td> <!-- ScaLA-is -->
   <td class="is qa">10.49 ± 2.71 / 26.84 ± 3.93</td> <!-- NQiI -->
   <td class="fo ner">85.04 ± 0.57 / 85.72 ± 0.50</td> <!-- FoNE -->
   <td class="fo la">2.90 ± 2.21 / 43.42 ± 4.67</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">23=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-2</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,366 ± 2,669 / 3,906 ± 1,247</td> <!-- Model inference speed -->
   <td class="score">34.83 ± 1.29</td> <!-- ScandEval score -->
   <td class="is-score">25.40 ± 1.24</td> <!-- Icelandic score -->
   <td class="fo-score">44.26 ± 1.33</td> <!-- Faroese score -->
   <td class="is ner">64.57 ± 1.62 / 67.12 ± 1.47</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.86 ± 1.11 / 43.33 ± 2.97</td> <!-- ScaLA-is -->
   <td class="is qa">10.76 ± 1.00 / 27.29 ± 2.41</td> <!-- NQiI -->
   <td class="fo ner">84.72 ± 0.84 / 85.44 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">3.79 ± 1.83 / 49.66 ± 2.54</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">23=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,991 ± 2,534 / 3,797 ± 1,216</td> <!-- Model inference speed -->
   <td class="score">34.75 ± 1.50</td> <!-- ScandEval score -->
   <td class="is-score">25.56 ± 1.32</td> <!-- Icelandic score -->
   <td class="fo-score">43.94 ± 1.68</td> <!-- Faroese score -->
   <td class="is ner">64.88 ± 1.32 / 67.55 ± 1.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.60 ± 0.90 / 40.52 ± 3.55</td> <!-- ScaLA-is -->
   <td class="is qa">12.39 ± 1.75 / 29.86 ± 2.90</td> <!-- NQiI -->
   <td class="fo ner">84.92 ± 0.70 / 85.65 ± 0.67</td> <!-- FoNE -->
   <td class="fo la">2.96 ± 2.66 / 45.42 ± 4.03</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">24</td> <!-- Rank -->
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,703 ± 1,837 / 2,637 ± 873</td> <!-- Model inference speed -->
   <td class="score">34.63 ± 1.26</td> <!-- ScandEval score -->
   <td class="is-score">23.92 ± 1.21</td> <!-- Icelandic score -->
   <td class="fo-score">45.34 ± 1.32</td> <!-- Faroese score -->
   <td class="is ner">63.31 ± 1.41 / 65.79 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.47 ± 1.56 / 49.04 ± 2.54</td> <!-- ScaLA-is -->
   <td class="is qa">5.99 ± 0.66 / 25.32 ± 0.78</td> <!-- NQiI -->
   <td class="fo ner">82.64 ± 0.63 / 83.27 ± 0.65</td> <!-- FoNE -->
   <td class="fo la">8.03 ± 2.01 / 51.96 ± 1.87</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">25</td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,040 ± 833 / 1,346 ± 439</td> <!-- Model inference speed -->
   <td class="score">34.28 ± 1.44</td> <!-- ScandEval score -->
   <td class="is-score">24.78 ± 1.09</td> <!-- Icelandic score -->
   <td class="fo-score">43.78 ± 1.79</td> <!-- Faroese score -->
   <td class="is ner">63.11 ± 1.31 / 65.36 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.47 ± 1.38 / 48.04 ± 2.34</td> <!-- ScaLA-is -->
   <td class="is qa">7.76 ± 0.57 / 36.28 ± 1.35</td> <!-- NQiI -->
   <td class="fo ner">82.36 ± 0.91 / 82.94 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">5.20 ± 2.67 / 50.88 ± 1.55</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">26=</td> <!-- Rank -->
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="score">34.19 ± 1.20</td> <!-- ScandEval score -->
   <td class="is-score">25.44 ± 1.00</td> <!-- Icelandic score -->
   <td class="fo-score">42.95 ± 1.40</td> <!-- Faroese score -->
   <td class="is ner">66.23 ± 1.24 / 67.76 ± 1.08</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.04 ± 0.78 / 45.96 ± 2.83</td> <!-- ScaLA-is -->
   <td class="is qa">10.04 ± 0.99 / 28.66 ± 0.92</td> <!-- NQiI -->
   <td class="fo ner">82.97 ± 0.83 / 83.62 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 1.96 / 46.51 ± 4.19</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">26=</td> <!-- Rank -->
   <td>bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,363 ± 2,211 / 1,733 ± 565</td> <!-- Model inference speed -->
   <td class="score">33.87 ± 2.80</td> <!-- ScandEval score -->
   <td class="is-score">28.01 ± 3.13</td> <!-- Icelandic score -->
   <td class="fo-score">39.73 ± 2.46</td> <!-- Faroese score -->
   <td class="is ner">60.88 ± 1.42 / 59.11 ± 1.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">13.50 ± 7.64 / 52.75 ± 5.19</td> <!-- ScaLA-is -->
   <td class="is qa">9.65 ± 0.34 / 42.51 ± 1.87</td> <!-- NQiI -->
   <td class="fo ner">73.06 ± 1.51 / 72.61 ± 1.40</td> <!-- FoNE -->
   <td class="fo la">6.41 ± 3.41 / 45.04 ± 4.45</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">27=</td> <!-- Rank -->
   <td>patrickvonplaten/norwegian-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,461 ± 1,880 / 2,441 ± 803</td> <!-- Model inference speed -->
   <td class="score">33.76 ± 1.75</td> <!-- ScandEval score -->
   <td class="is-score">23.20 ± 1.80</td> <!-- Icelandic score -->
   <td class="fo-score">44.32 ± 1.69</td> <!-- Faroese score -->
   <td class="is ner">60.79 ± 1.85 / 63.65 ± 1.78</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.18 ± 2.84 / 46.69 ± 2.90</td> <!-- ScaLA-is -->
   <td class="is qa">6.64 ± 0.72 / 26.52 ± 0.97</td> <!-- NQiI -->
   <td class="fo ner">82.57 ± 0.93 / 83.35 ± 0.91</td> <!-- FoNE -->
   <td class="fo la">6.07 ± 2.45 / 51.19 ± 2.26</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">27=</td> <!-- Rank -->
   <td>DeepPavlov/rubert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,268 ± 1,834 / 2,457 ± 810</td> <!-- Model inference speed -->
   <td class="score">33.51 ± 1.47</td> <!-- ScandEval score -->
   <td class="is-score">23.78 ± 1.04</td> <!-- Icelandic score -->
   <td class="fo-score">43.24 ± 1.91</td> <!-- Faroese score -->
   <td class="is ner">62.61 ± 0.77 / 65.19 ± 0.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.68 ± 1.80 / 40.27 ± 2.94</td> <!-- ScaLA-is -->
   <td class="is qa">6.04 ± 0.56 / 29.39 ± 0.76</td> <!-- NQiI -->
   <td class="fo ner">83.15 ± 0.73 / 83.90 ± 0.74</td> <!-- FoNE -->
   <td class="fo la">3.33 ± 3.08 / 43.85 ± 2.55</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">28</td> <!-- Rank -->
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,400 ± 1,857 / 2,405 ± 803</td> <!-- Model inference speed -->
   <td class="score">33.29 ± 1.68</td> <!-- ScandEval score -->
   <td class="is-score">23.07 ± 1.18</td> <!-- Icelandic score -->
   <td class="fo-score">43.52 ± 2.18</td> <!-- Faroese score -->
   <td class="is ner">62.23 ± 1.24 / 64.45 ± 1.23</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.45 ± 1.74 / 48.21 ± 1.91</td> <!-- ScaLA-is -->
   <td class="is qa">5.52 ± 0.55 / 26.85 ± 1.03</td> <!-- NQiI -->
   <td class="fo ner">80.52 ± 0.76 / 81.35 ± 0.69</td> <!-- FoNE -->
   <td class="fo la">6.51 ± 3.60 / 51.81 ± 1.95</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">29</td> <!-- Rank -->
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,901 ± 3,973 / 3,150 ± 1,061</td> <!-- Model inference speed -->
   <td class="score">32.63 ± 1.21</td> <!-- ScandEval score -->
   <td class="is-score">23.62 ± 0.76</td> <!-- Icelandic score -->
   <td class="fo-score">41.64 ± 1.66</td> <!-- Faroese score -->
   <td class="is ner">63.36 ± 0.96 / 65.24 ± 0.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.02 ± 0.94 / 47.05 ± 2.13</td> <!-- ScaLA-is -->
   <td class="is qa">6.48 ± 0.37 / 27.44 ± 0.44</td> <!-- NQiI -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">0.38 ± 2.42 / 46.11 ± 2.65</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">30</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="score">32.61 ± 1.01</td> <!-- ScandEval score -->
   <td class="is-score">22.68 ± 0.90</td> <!-- Icelandic score -->
   <td class="fo-score">42.54 ± 1.13</td> <!-- Faroese score -->
   <td class="is ner">62.44 ± 1.07 / 64.98 ± 0.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.91 ± 1.14 / 46.54 ± 2.46</td> <!-- ScaLA-is -->
   <td class="is qa">3.69 ± 0.48 / 27.48 ± 0.49</td> <!-- NQiI -->
   <td class="fo ner">82.24 ± 0.85 / 82.84 ± 0.78</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.41 / 50.47 ± 1.13</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">31</td> <!-- Rank -->
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,778 ± 1,694 / 2,895 ± 952</td> <!-- Model inference speed -->
   <td class="score">32.50 ± 1.51</td> <!-- ScandEval score -->
   <td class="is-score">21.74 ± 1.32</td> <!-- Icelandic score -->
   <td class="fo-score">43.26 ± 1.70</td> <!-- Faroese score -->
   <td class="is ner">59.11 ± 1.26 / 60.95 ± 1.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.53 ± 1.93 / 46.17 ± 3.31</td> <!-- ScaLA-is -->
   <td class="is qa">5.57 ± 0.78 / 28.89 ± 1.29</td> <!-- NQiI -->
   <td class="fo ner">82.76 ± 1.26 / 83.50 ± 1.20</td> <!-- FoNE -->
   <td class="fo la">3.75 ± 2.14 / 47.58 ± 2.57</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">32=</td> <!-- Rank -->
   <td>roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,946 ± 2,319 / 1,547 ± 493</td> <!-- Model inference speed -->
   <td class="score">32.33 ± 1.23</td> <!-- ScandEval score -->
   <td class="is-score">22.98 ± 1.28</td> <!-- Icelandic score -->
   <td class="fo-score">41.69 ± 1.19</td> <!-- Faroese score -->
   <td class="is ner">62.32 ± 1.32 / 65.06 ± 1.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.05 ± 1.86 / 41.52 ± 5.04</td> <!-- ScaLA-is -->
   <td class="is qa">6.66 ± 0.67 / 32.13 ± 1.93</td> <!-- NQiI -->
   <td class="fo ner">81.78 ± 0.95 / 82.55 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">1.59 ± 1.42 / 43.43 ± 3.88</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">32=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,486 ± 1,313 / 1,468 ± 469</td> <!-- Model inference speed -->
   <td class="score">31.50 ± 2.88</td> <!-- ScandEval score -->
   <td class="is-score">19.81 ± 1.08</td> <!-- Icelandic score -->
   <td class="fo-score">43.20 ± 4.67</td> <!-- Faroese score -->
   <td class="is ner">48.31 ± 1.22 / 47.65 ± 1.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.18 ± 1.21 / 46.35 ± 3.68</td> <!-- ScaLA-is -->
   <td class="is qa">7.94 ± 0.81 / 36.61 ± 1.41</td> <!-- NQiI -->
   <td class="fo ner">72.99 ± 1.55 / 72.45 ± 1.56</td> <!-- FoNE -->
   <td class="fo la">13.40 ± 7.79 / 54.18 ± 5.13</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">33=</td> <!-- Rank -->
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,665 ± 2,882 / 3,196 ± 1,041</td> <!-- Model inference speed -->
   <td class="score">31.48 ± 1.40</td> <!-- ScandEval score -->
   <td class="is-score">22.31 ± 1.11</td> <!-- Icelandic score -->
   <td class="fo-score">40.65 ± 1.69</td> <!-- Faroese score -->
   <td class="is ner">59.63 ± 1.40 / 61.65 ± 1.33</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.23 / 49.36 ± 1.58</td> <!-- ScaLA-is -->
   <td class="is qa">5.55 ± 0.70 / 27.22 ± 1.06</td> <!-- NQiI -->
   <td class="fo ner">80.21 ± 0.95 / 80.80 ± 0.97</td> <!-- FoNE -->
   <td class="fo la">1.10 ± 2.44 / 48.16 ± 1.47</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">33=</td> <!-- Rank -->
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="score">31.38 ± 1.22</td> <!-- ScandEval score -->
   <td class="is-score">21.69 ± 1.05</td> <!-- Icelandic score -->
   <td class="fo-score">41.08 ± 1.40</td> <!-- Faroese score -->
   <td class="is ner">58.90 ± 1.06 / 62.01 ± 0.98</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.27 ± 1.53 / 43.40 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is qa">5.90 ± 0.57 / 27.22 ± 1.18</td> <!-- NQiI -->
   <td class="fo ner">80.58 ± 0.45 / 81.29 ± 0.46</td> <!-- FoNE -->
   <td class="fo la">1.58 ± 2.34 / 49.16 ± 2.33</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">34</td> <!-- Rank -->
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,570 ± 1,759 / 2,635 ± 894</td> <!-- Model inference speed -->
   <td class="score">31.02 ± 1.26</td> <!-- ScandEval score -->
   <td class="is-score">21.35 ± 1.21</td> <!-- Icelandic score -->
   <td class="fo-score">40.69 ± 1.31</td> <!-- Faroese score -->
   <td class="is ner">56.38 ± 1.62 / 57.44 ± 1.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.98 ± 1.37 / 42.57 ± 3.49</td> <!-- ScaLA-is -->
   <td class="is qa">6.69 ± 0.63 / 32.15 ± 1.11</td> <!-- NQiI -->
   <td class="fo ner">80.48 ± 0.91 / 81.17 ± 0.85</td> <!-- FoNE -->
   <td class="fo la">0.89 ± 1.71 / 46.19 ± 3.11</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">35</td> <!-- Rank -->
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,249 ± 1,947 / 2,297 ± 753</td> <!-- Model inference speed -->
   <td class="score">30.45 ± 1.21</td> <!-- ScandEval score -->
   <td class="is-score">21.04 ± 1.04</td> <!-- Icelandic score -->
   <td class="fo-score">39.86 ± 1.38</td> <!-- Faroese score -->
   <td class="is ner">58.15 ± 1.49 / 60.86 ± 1.43</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.45 ± 1.11 / 43.99 ± 2.92</td> <!-- ScaLA-is -->
   <td class="is qa">5.42 ± 0.52 / 26.08 ± 0.59</td> <!-- NQiI -->
   <td class="fo ner">78.59 ± 1.16 / 79.35 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">1.13 ± 1.60 / 46.79 ± 3.40</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">36</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">28.84 ± 2.84</td> <!-- ScandEval score -->
   <td class="is-score">24.95 ± 3.04</td> <!-- Icelandic score -->
   <td class="fo-score">32.73 ± 2.64</td> <!-- Faroese score -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">37</td> <!-- Rank -->
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,531 ± 962 / 945 ± 308</td> <!-- Model inference speed -->
   <td class="score">28.73 ± 1.79</td> <!-- ScandEval score -->
   <td class="is-score">19.77 ± 1.51</td> <!-- Icelandic score -->
   <td class="fo-score">37.70 ± 2.07</td> <!-- Faroese score -->
   <td class="is ner">49.68 ± 2.20 / 48.34 ± 1.96</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.33 ± 1.39 / 47.30 ± 2.09</td> <!-- ScaLA-is -->
   <td class="is qa">9.30 ± 0.95 / 36.88 ± 0.75</td> <!-- NQiI -->
   <td class="fo ner">72.46 ± 0.87 / 71.83 ± 0.83</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 3.27 / 48.20 ± 1.50</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">38</td> <!-- Rank -->
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,936 ± 1,593 / 3,120 ± 1,015</td> <!-- Model inference speed -->
   <td class="score">26.93 ± 1.80</td> <!-- ScandEval score -->
   <td class="is-score">16.56 ± 1.66</td> <!-- Icelandic score -->
   <td class="fo-score">37.30 ± 1.94</td> <!-- Faroese score -->
   <td class="is ner">42.07 ± 2.27 / 43.57 ± 2.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.27 ± 2.04 / 48.20 ± 1.32</td> <!-- ScaLA-is -->
   <td class="is qa">7.35 ± 0.66 / 20.44 ± 1.46</td> <!-- NQiI -->
   <td class="fo ner">73.80 ± 0.98 / 74.58 ± 0.92</td> <!-- FoNE -->
   <td class="fo la">0.81 ± 2.90 / 48.11 ± 2.18</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">39</td> <!-- Rank -->
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,786 ± 2,060 / 2,012 ± 673</td> <!-- Model inference speed -->
   <td class="score">25.75 ± 7.95</td> <!-- ScandEval score -->
   <td class="is-score">19.20 ± 4.41</td> <!-- Icelandic score -->
   <td class="fo-score">32.30 ± 11.50</td> <!-- Faroese score -->
   <td class="is ner">51.53 ± 10.96 / 53.86 ± 11.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.89 ± 1.79 / 47.82 ± 2.03</td> <!-- ScaLA-is -->
   <td class="is qa">5.19 ± 0.47 / 27.71 ± 0.76</td> <!-- NQiI -->
   <td class="fo ner">63.86 ± 20.89 / 64.42 ± 21.07</td> <!-- FoNE -->
   <td class="fo la">0.73 ± 2.11 / 49.36 ± 1.78</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">40</td> <!-- Rank -->
   <td>danish-foundation-models/encoder-small-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,882 ± 131 / 3,765 ± 1,218</td> <!-- Model inference speed -->
   <td class="score">25.10 ± 3.36</td> <!-- ScandEval score -->
   <td class="is-score">9.75 ± 4.64</td> <!-- Icelandic score -->
   <td class="fo-score">40.45 ± 2.08</td> <!-- Faroese score -->
   <td class="is ner">28.99 ± 12.22 / 28.98 ± 12.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.17 ± 1.37 / 38.53 ± 3.43</td> <!-- ScaLA-is -->
   <td class="is qa">0.42 ± 0.33 / 1.20 ± 1.50</td> <!-- NQiI -->
   <td class="fo ner">79.97 ± 1.24 / 80.28 ± 1.24</td> <!-- FoNE -->
   <td class="fo la">0.93 ± 2.91 / 45.79 ± 3.78</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">41</td> <!-- Rank -->
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,538 ± 137 / 2,293 ± 734</td> <!-- Model inference speed -->
   <td class="score">22.49 ± 1.83</td> <!-- ScandEval score -->
   <td class="is-score">11.38 ± 1.17</td> <!-- Icelandic score -->
   <td class="fo-score">33.59 ± 2.49</td> <!-- Faroese score -->
   <td class="is ner">30.50 ± 1.95 / 30.08 ± 1.90</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.59 ± 1.49 / 46.53 ± 4.34</td> <!-- ScaLA-is -->
   <td class="is qa">0.06 ± 0.07 / 0.12 ± 0.11</td> <!-- NQiI -->
   <td class="fo ner">62.07 ± 1.18 / 61.72 ± 1.18</td> <!-- FoNE -->
   <td class="fo la">5.11 ± 3.80 / 47.64 ± 4.52</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">42</td> <!-- Rank -->
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,299 ± 1,329 / 2,110 ± 704</td> <!-- Model inference speed -->
   <td class="score">22.34 ± 1.22</td> <!-- ScandEval score -->
   <td class="is-score">10.71 ± 0.82</td> <!-- Icelandic score -->
   <td class="fo-score">33.97 ± 1.63</td> <!-- Faroese score -->
   <td class="is ner">25.35 ± 0.77 / 26.08 ± 0.62</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.40 ± 0.99 / 46.51 ± 3.33</td> <!-- ScaLA-is -->
   <td class="is qa">5.37 ± 0.70 / 24.09 ± 1.52</td> <!-- NQiI -->
   <td class="fo ner">59.66 ± 0.63 / 59.39 ± 0.60</td> <!-- FoNE -->
   <td class="fo la">8.28 ± 2.63 / 51.70 ± 3.23</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">43</td> <!-- Rank -->
   <td>ltg/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,973 ± 2,733 / 3,532 ± 1,147</td> <!-- Model inference speed -->
   <td class="score">22.05 ± 1.43</td> <!-- ScandEval score -->
   <td class="is-score">11.74 ± 1.12</td> <!-- Icelandic score -->
   <td class="fo-score">32.37 ± 1.74</td> <!-- Faroese score -->
   <td class="is ner">28.74 ± 1.77 / 28.47 ± 1.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.00 ± 0.94 / 47.57 ± 3.24</td> <!-- ScaLA-is -->
   <td class="is qa">3.47 ± 0.65 / 19.93 ± 2.77</td> <!-- NQiI -->
   <td class="fo ner">60.57 ± 0.86 / 60.42 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">4.16 ± 2.63 / 47.13 ± 3.43</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">44=</td> <!-- Rank -->
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,468 ± 1,421 / 2,067 ± 684</td> <!-- Model inference speed -->
   <td class="score">21.44 ± 1.10</td> <!-- ScandEval score -->
   <td class="is-score">10.64 ± 0.87</td> <!-- Icelandic score -->
   <td class="fo-score">32.23 ± 1.33</td> <!-- Faroese score -->
   <td class="is ner">24.18 ± 0.86 / 24.86 ± 0.96</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.47 ± 1.12 / 43.26 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is qa">5.28 ± 0.62 / 22.50 ± 0.83</td> <!-- NQiI -->
   <td class="fo ner">58.50 ± 0.63 / 58.33 ± 0.70</td> <!-- FoNE -->
   <td class="fo la">5.96 ± 2.04 / 51.99 ± 1.53</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">44=</td> <!-- Rank -->
   <td>TurkuNLP/bert-base-finnish-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,029 ± 1,446 / 3,408 ± 1,126</td> <!-- Model inference speed -->
   <td class="score">18.79 ± 1.54</td> <!-- ScandEval score -->
   <td class="is-score">12.35 ± 1.31</td> <!-- Icelandic score -->
   <td class="fo-score">25.23 ± 1.78</td> <!-- Faroese score -->
   <td class="is ner">30.96 ± 1.65 / 32.26 ± 1.65</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.02 ± 1.74 / 45.92 ± 2.69</td> <!-- ScaLA-is -->
   <td class="is qa">5.07 ± 0.53 / 24.32 ± 2.07</td> <!-- NQiI -->
   <td class="fo ner">51.26 ± 1.05 / 51.07 ± 1.06</td> <!-- FoNE -->
   <td class="fo la">-0.79 ± 2.51 / 47.29 ± 2.29</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">44=</td> <!-- Rank -->
   <td>asafaya/bert-base-arabic</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,876 ± 1,516 / 3,228 ± 1,077</td> <!-- Model inference speed -->
   <td class="score">17.11 ± 1.44</td> <!-- ScandEval score -->
   <td class="is-score">8.14 ± 1.23</td> <!-- Icelandic score -->
   <td class="fo-score">26.08 ± 1.66</td> <!-- Faroese score -->
   <td class="is ner">18.12 ± 1.64 / 17.32 ± 1.56</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 1.37 / 45.21 ± 2.42</td> <!-- ScaLA-is -->
   <td class="is qa">5.05 ± 0.67 / 24.09 ± 1.66</td> <!-- NQiI -->
   <td class="fo ner">50.44 ± 1.82 / 49.80 ± 1.76</td> <!-- FoNE -->
   <td class="fo la">1.73 ± 1.50 / 41.87 ± 3.79</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">45</td> <!-- Rank -->
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,285 ± 87 / 610 ± 164</td> <!-- Model inference speed -->
   <td class="score">15.16 ± 1.15</td> <!-- ScandEval score -->
   <td class="is-score">6.10 ± 0.81</td> <!-- Icelandic score -->
   <td class="fo-score">24.21 ± 1.50</td> <!-- Faroese score -->
   <td class="is ner">17.34 ± 1.13 / 16.43 ± 1.26</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.06 ± 0.99 / 36.73 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is qa">1.02 ± 0.30 / 21.61 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">48.70 ± 1.57 / 48.51 ± 1.57</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 1.43 / 36.05 ± 3.05</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">46</td> <!-- Rank -->
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,866 ± 1,697 / 2,906 ± 954</td> <!-- Model inference speed -->
   <td class="score">14.69 ± 1.56</td> <!-- ScandEval score -->
   <td class="is-score">5.79 ± 1.21</td> <!-- Icelandic score -->
   <td class="fo-score">23.59 ± 1.91</td> <!-- Faroese score -->
   <td class="is ner">12.43 ± 1.33 / 11.85 ± 1.53</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.16 ± 1.91 / 47.41 ± 2.41</td> <!-- ScaLA-is -->
   <td class="is qa">4.77 ± 0.39 / 27.98 ± 1.03</td> <!-- NQiI -->
   <td class="fo ner">43.59 ± 0.80 / 42.84 ± 0.86</td> <!-- FoNE -->
   <td class="fo la">3.58 ± 3.02 / 49.80 ± 2.36</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">47</td> <!-- Rank -->
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,371 ± 2,916 / 5,362 ± 1,766</td> <!-- Model inference speed -->
   <td class="score">14.47 ± 1.68</td> <!-- ScandEval score -->
   <td class="is-score">5.24 ± 1.44</td> <!-- Icelandic score -->
   <td class="fo-score">23.70 ± 1.92</td> <!-- Faroese score -->
   <td class="is ner">12.39 ± 2.20 / 11.68 ± 2.17</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.63 ± 1.66 / 43.64 ± 4.69</td> <!-- ScaLA-is -->
   <td class="is qa">1.70 ± 0.45 / 16.29 ± 1.59</td> <!-- NQiI -->
   <td class="fo ner">45.16 ± 2.00 / 44.76 ± 2.01</td> <!-- FoNE -->
   <td class="fo la">2.24 ± 1.83 / 43.57 ± 4.41</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">48</td> <!-- Rank -->
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,237 ± 120 / 1,441 ± 325</td> <!-- Model inference speed -->
   <td class="score">4.85 ± 1.22</td> <!-- ScandEval score -->
   <td class="is-score">3.33 ± 0.89</td> <!-- Icelandic score -->
   <td class="fo-score">6.37 ± 1.54</td> <!-- Faroese score -->
   <td class="is ner">9.96 ± 1.11 / 8.96 ± 1.05</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.10 ± 1.46 / 35.81 ± 3.45</td> <!-- ScaLA-is -->
   <td class="is qa">0.12 ± 0.10 / 4.48 ± 1.39</td> <!-- NQiI -->
   <td class="fo ner">12.10 ± 1.51 / 11.83 ± 1.50</td> <!-- FoNE -->
   <td class="fo la">0.64 ± 1.57 / 38.69 ± 3.19</td> <!-- ScaLA-fo -->
  </tr>
  <tr>
   <td class="rank">49</td> <!-- Rank -->
   <td>ltg/norbert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,989 ± 2,295 / 4,771 ± 1,550</td> <!-- Model inference speed -->
   <td class="score">-0.03 ± 1.04</td> <!-- ScandEval score -->
   <td class="is-score">0.55 ± 0.67</td> <!-- Icelandic score -->
   <td class="fo-score">-0.60 ± 1.41</td> <!-- Faroese score -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.03 ± 1.29 / 46.72 ± 2.28</td> <!-- ScaLA-is -->
   <td class="is qa">1.68 ± 0.72 / 13.50 ± 4.66</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-1.21 ± 2.82 / 44.15 ± 3.47</td> <!-- ScaLA-fo -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlu.csv" target="_blank">Download as CSV</a>
</div>