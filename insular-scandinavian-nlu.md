---
layout: leaderboard
title: Insular Scandinavian NLU
---

<center>Last updated: 31/03/2024 19:08:47 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="insular-scandinavian-nlu" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoNE">FoNE version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-fo">ScaLA-fo version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="is-rank">1.62</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.00</td> <!-- Faroese rank -->
   <td class="is ner">85.04 ± 0.95 / 80.51 ± 1.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">50.78 ± 2.21 / 73.10 ± 1.10</td> <!-- ScaLA-is -->
   <td class="is qa">17.76 ± 2.33 / 36.98 ± 3.29</td> <!-- NQiI -->
   <td class="fo ner">91.31 ± 0.69 / 91.79 ± 0.47</td> <!-- FoNE -->
   <td class="fo la">64.39 ± 1.55 / 81.38 ± 1.04</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">1.49</td> <!-- ScandEval rank -->
   <td class="is-rank">1.13</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.85</td> <!-- Faroese rank -->
   <td class="is ner">81.12 ± 2.02 / 81.48 ± 1.69</td> <!-- MIM-GOLD-NER -->
   <td class="is la">54.11 ± 2.40 / 76.46 ± 1.28</td> <!-- ScaLA-is -->
   <td class="is qa">30.93 ± 0.96 / 56.17 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">88.60 ± 0.60 / 89.37 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">46.81 ± 2.12 / 72.76 ± 1.40</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="is-rank">1.30</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.59</td> <!-- Faroese rank -->
   <td class="is ner">83.94 ± 1.34 / 84.66 ± 0.91</td> <!-- MIM-GOLD-NER -->
   <td class="is la">58.64 ± 1.69 / 78.30 ± 1.26</td> <!-- ScaLA-is -->
   <td class="is qa">25.35 ± 1.34 / 48.61 ± 1.71</td> <!-- NQiI -->
   <td class="fo ner">88.14 ± 0.58 / 88.89 ± 0.52</td> <!-- FoNE -->
   <td class="fo la">27.71 ± 9.67 / 61.60 ± 5.69</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="is-rank">2.27</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.82</td> <!-- Faroese rank -->
   <td class="is ner">81.83 ± 1.65 / 82.24 ± 1.04</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.09 ± 3.83 / 73.24 ± 2.23</td> <!-- ScaLA-is -->
   <td class="is qa">6.66 ± 0.69 / 33.95 ± 0.75</td> <!-- NQiI -->
   <td class="fo ner">90.52 ± 0.47 / 90.83 ± 0.40</td> <!-- FoNE -->
   <td class="fo la">44.99 ± 11.76 / 71.54 ± 5.83</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,004 ± 2,244 / 2,324 ± 761</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="is-rank">1.84</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.60</td> <!-- Faroese rank -->
   <td class="is ner">84.35 ± 1.14 / 85.07 ± 1.09</td> <!-- MIM-GOLD-NER -->
   <td class="is la">59.12 ± 1.94 / 78.14 ± 1.24</td> <!-- ScaLA-is -->
   <td class="is qa">11.18 ± 1.04 / 44.02 ± 2.30</td> <!-- NQiI -->
   <td class="fo ner">87.79 ± 0.40 / 88.46 ± 0.31</td> <!-- FoNE -->
   <td class="fo la">22.51 ± 10.65 / 55.58 ± 8.05</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="is-rank">1.26</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.32</td> <!-- Faroese rank -->
   <td class="is ner">78.05 ± 1.72 / 78.74 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">48.29 ± 2.59 / 73.54 ± 1.99</td> <!-- ScaLA-is -->
   <td class="is qa">29.38 ± 1.81 / 52.42 ± 3.00</td> <!-- NQiI -->
   <td class="fo ner">87.35 ± 0.94 / 87.65 ± 0.94</td> <!-- FoNE -->
   <td class="fo la">14.65 ± 11.12 / 46.36 ± 10.23</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="is-rank">2.02</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.58</td> <!-- Faroese rank -->
   <td class="is ner">80.91 ± 1.24 / 81.30 ± 0.97</td> <!-- MIM-GOLD-NER -->
   <td class="is la">41.91 ± 3.45 / 67.96 ± 2.53</td> <!-- ScaLA-is -->
   <td class="is qa">13.73 ± 0.73 / 52.73 ± 0.85</td> <!-- NQiI -->
   <td class="fo ner">88.81 ± 0.65 / 89.12 ± 0.56</td> <!-- FoNE -->
   <td class="fo la">30.92 ± 8.65 / 63.05 ± 4.66</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="is-rank">2.15</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.63</td> <!-- Faroese rank -->
   <td class="is ner">77.40 ± 0.48 / 78.58 ± 0.56</td> <!-- MIM-GOLD-NER -->
   <td class="is la">60.64 ± 1.44 / 79.20 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is qa">6.51 ± 1.69 / 22.61 ± 5.24</td> <!-- NQiI -->
   <td class="fo ner">85.80 ± 0.25 / 86.58 ± 0.26</td> <!-- FoNE -->
   <td class="fo la">30.88 ± 2.36 / 63.79 ± 1.33</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="is-rank">2.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.58</td> <!-- Faroese rank -->
   <td class="is ner">80.45 ± 1.29 / 81.01 ± 1.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">36.92 ± 7.62 / 66.07 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is qa">11.75 ± 0.66 / 46.17 ± 1.42</td> <!-- NQiI -->
   <td class="fo ner">89.16 ± 0.66 / 89.62 ± 0.62</td> <!-- FoNE -->
   <td class="fo la">22.76 ± 10.57 / 60.04 ± 5.76</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-large</td> <!-- Model ID -->
   <td class="num_model_parameters">406</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,677 ± 719 / 1,886 ± 604</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="is-rank">1.77</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.33</td> <!-- Faroese rank -->
   <td class="is ner">85.14 ± 1.31 / 84.37 ± 1.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">59.31 ± 2.97 / 78.19 ± 1.97</td> <!-- ScaLA-is -->
   <td class="is qa">12.84 ± 1.51 / 49.01 ± 3.34</td> <!-- NQiI -->
   <td class="fo ner">86.84 ± 0.77 / 87.51 ± 0.72</td> <!-- FoNE -->
   <td class="fo la">9.82 ± 3.95 / 50.49 ± 3.45</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,697 ± 2,113 / 5,432 ± 1,749</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="is-rank">1.77</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.33</td> <!-- Faroese rank -->
   <td class="is ner">85.32 ± 1.11 / 81.56 ± 1.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">60.44 ± 1.93 / 78.11 ± 1.40</td> <!-- ScaLA-is -->
   <td class="is qa">13.31 ± 0.95 / 49.21 ± 1.36</td> <!-- NQiI -->
   <td class="fo ner">86.50 ± 0.96 / 87.11 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">10.13 ± 8.55 / 47.31 ± 7.04</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="is-rank">2.56</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.54</td> <!-- Faroese rank -->
   <td class="is ner">83.57 ± 0.96 / 83.52 ± 0.76</td> <!-- MIM-GOLD-NER -->
   <td class="is la">23.07 ± 13.28 / 57.26 ± 6.91</td> <!-- ScaLA-is -->
   <td class="is qa">7.81 ± 1.01 / 34.12 ± 1.47</td> <!-- NQiI -->
   <td class="fo ner">90.60 ± 0.45 / 90.78 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">22.86 ± 13.14 / 59.92 ± 6.74</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/XLMR-ENIS</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,711 ± 2,333 / 2,141 ± 689</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="is-rank">1.29</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.81</td> <!-- Faroese rank -->
   <td class="is ner">82.20 ± 1.83 / 82.70 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">48.51 ± 5.94 / 71.40 ± 4.38</td> <!-- ScaLA-is -->
   <td class="is qa">27.06 ± 1.18 / 51.37 ± 1.42</td> <!-- NQiI -->
   <td class="fo ner">87.09 ± 0.76 / 87.71 ± 0.73</td> <!-- FoNE -->
   <td class="fo la">3.09 ± 1.98 / 39.41 ± 4.45</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,119 ± 1,576 / 3,812 ± 1,242</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="is-rank">2.00</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.65</td> <!-- Faroese rank -->
   <td class="is ner">85.03 ± 0.86 / 85.01 ± 0.93</td> <!-- MIM-GOLD-NER -->
   <td class="is la">45.06 ± 11.13 / 67.74 ± 7.92</td> <!-- ScaLA-is -->
   <td class="is qa">10.82 ± 1.12 / 42.82 ± 2.91</td> <!-- NQiI -->
   <td class="fo ner">87.22 ± 0.68 / 87.92 ± 0.59</td> <!-- FoNE -->
   <td class="fo la">6.23 ± 6.96 / 48.55 ± 4.87</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,360 ± 1,611 / 3,858 ± 1,246</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="is-rank">1.86</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.81</td> <!-- Faroese rank -->
   <td class="is ner">85.34 ± 0.66 / 84.80 ± 0.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">55.88 ± 2.20 / 74.91 ± 1.96</td> <!-- ScaLA-is -->
   <td class="is qa">13.31 ± 0.95 / 49.21 ± 1.36</td> <!-- NQiI -->
   <td class="fo ner">87.13 ± 0.58 / 87.70 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">3.66 ± 3.33 / 40.81 ± 4.34</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="is-rank">2.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.59</td> <!-- Faroese rank -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-igc</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,551 ± 1,656 / 3,918 ± 1,274</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="is-rank">2.07</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="is ner">79.85 ± 0.94 / 79.32 ± 0.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">54.38 ± 3.78 / 75.08 ± 2.62</td> <!-- ScaLA-is -->
   <td class="is qa">9.91 ± 0.65 / 42.34 ± 1.46</td> <!-- NQiI -->
   <td class="fo ner">83.82 ± 0.98 / 84.34 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">4.93 ± 3.16 / 45.85 ± 3.66</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="is-rank">2.22</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.91</td> <!-- Faroese rank -->
   <td class="is ner">82.83 ± 1.09 / 83.16 ± 1.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">22.78 ± 12.25 / 57.07 ± 8.18</td> <!-- ScaLA-is -->
   <td class="is qa">15.72 ± 1.39 / 55.29 ± 1.30</td> <!-- NQiI -->
   <td class="fo ner">87.85 ± 0.95 / 88.21 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">1.17 ± 2.11 / 40.94 ± 5.07</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="is-rank">2.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.78</td> <!-- Faroese rank -->
   <td class="is ner">78.43 ± 1.53 / 79.30 ± 1.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">10.78 ± 7.04 / 53.28 ± 3.97</td> <!-- ScaLA-is -->
   <td class="is qa">13.79 ± 0.96 / 54.20 ± 1.31</td> <!-- NQiI -->
   <td class="fo ner">88.39 ± 0.86 / 88.75 ± 0.75</td> <!-- FoNE -->
   <td class="fo la">2.85 ± 1.32 / 48.43 ± 2.29</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="is-rank">3.05</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.35</td> <!-- Faroese rank -->
   <td class="is ner">74.65 ± 1.65 / 75.83 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.89 ± 3.00 / 44.63 ± 4.01</td> <!-- ScaLA-is -->
   <td class="is qa">9.29 ± 0.66 / 41.76 ± 1.89</td> <!-- NQiI -->
   <td class="fo ner">86.09 ± 1.03 / 86.85 ± 1.02</td> <!-- FoNE -->
   <td class="fo la">15.24 ± 6.84 / 50.54 ± 4.85</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-mC4-is</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,308 ± 1,614 / 3,851 ± 1,254</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="is-rank">3.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.31</td> <!-- Faroese rank -->
   <td class="is ner">79.19 ± 0.96 / 80.35 ± 0.69</td> <!-- MIM-GOLD-NER -->
   <td class="is la">20.95 ± 5.57 / 50.96 ± 5.04</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NQiI -->
   <td class="fo ner">88.44 ± 0.35 / 89.11 ± 0.38</td> <!-- FoNE -->
   <td class="fo la">11.83 ± 4.90 / 48.95 ± 6.81</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="is-rank">2.82</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.78</td> <!-- Faroese rank -->
   <td class="is ner">73.92 ± 1.40 / 75.86 ± 1.21</td> <!-- MIM-GOLD-NER -->
   <td class="is la">11.77 ± 5.19 / 43.60 ± 7.11</td> <!-- ScaLA-is -->
   <td class="is qa">11.84 ± 1.07 / 48.30 ± 1.02</td> <!-- NQiI -->
   <td class="fo ner">88.21 ± 0.97 / 88.63 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">3.16 ± 2.26 / 38.93 ± 4.61</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.1</td> <!-- ScaLA-is version -->
   <td>10.0.1</td> <!-- NQiI version -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="is-rank">2.70</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.99</td> <!-- Faroese rank -->
   <td class="is ner">72.69 ± 0.79 / 73.57 ± 1.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">28.72 ± 5.29 / 60.29 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">8.46 ± 0.51 / 31.01 ± 0.72</td> <!-- NQiI -->
   <td class="fo ner">83.96 ± 0.80 / 84.63 ± 0.76</td> <!-- FoNE -->
   <td class="fo la">1.05 ± 1.66 / 41.31 ± 4.91</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">103</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="is-rank">2.92</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.81</td> <!-- Faroese rank -->
   <td class="is ner">73.81 ± 0.85 / 75.02 ± 0.89</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.23 ± 2.63 / 45.40 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">10.57 ± 1.12 / 42.39 ± 1.52</td> <!-- NQiI -->
   <td class="fo ner">86.62 ± 0.43 / 87.31 ± 0.44</td> <!-- FoNE -->
   <td class="fo la">3.64 ± 3.82 / 49.77 ± 2.26</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="is-rank">2.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.25</td> <!-- Faroese rank -->
   <td class="is ner">49.85 ± 3.05 / 39.50 ± 4.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.99 ± 1.54 / 39.38 ± 3.81</td> <!-- ScaLA-is -->
   <td class="is qa">25.74 ± 5.44 / 49.45 ± 5.29</td> <!-- NQiI -->
   <td class="fo ner">63.66 ± 2.09 / 59.77 ± 2.57</td> <!-- FoNE -->
   <td class="fo la">4.96 ± 2.36 / 43.40 ± 4.95</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="is-rank">2.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.25</td> <!-- Faroese rank -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td>9.1.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.1.2</td> <!-- ScaLA-is version -->
   <td>9.1.2</td> <!-- NQiI version -->
   <td>9.1.2</td> <!-- FoNE version -->
   <td>9.1.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="is-rank">2.91</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.92</td> <!-- Faroese rank -->
   <td class="is ner">60.88 ± 1.42 / 59.11 ± 1.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">13.50 ± 7.64 / 52.75 ± 5.19</td> <!-- ScaLA-is -->
   <td class="is qa">9.65 ± 0.34 / 42.51 ± 1.87</td> <!-- NQiI -->
   <td class="fo ner">73.06 ± 1.51 / 72.61 ± 1.40</td> <!-- FoNE -->
   <td class="fo la">5.48 ± 2.42 / 49.18 ± 3.63</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">3.44</td> <!-- ScandEval rank -->
   <td class="is-rank">2.97</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.91</td> <!-- Faroese rank -->
   <td class="is ner">74.30 ± 2.15 / 76.10 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.06 ± 2.43 / 37.04 ± 4.14</td> <!-- ScaLA-is -->
   <td class="is qa">11.47 ± 0.96 / 48.11 ± 0.94</td> <!-- NQiI -->
   <td class="fo ner">88.24 ± 0.58 / 88.48 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">1.73 ± 1.70 / 42.32 ± 5.16</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.1</td> <!-- ScaLA-is version -->
   <td>10.0.1</td> <!-- NQiI version -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,051 ± 3,289 / 2,704 ± 897</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="is-rank">3.22</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.68</td> <!-- Faroese rank -->
   <td class="is ner">69.04 ± 1.65 / 71.18 ± 1.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.34 ± 1.87 / 44.43 ± 4.20</td> <!-- ScaLA-is -->
   <td class="is qa">7.17 ± 0.77 / 30.71 ± 1.15</td> <!-- NQiI -->
   <td class="fo ner">86.10 ± 0.64 / 86.75 ± 0.57</td> <!-- FoNE -->
   <td class="fo la">6.28 ± 2.41 / 49.62 ± 2.08</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,998 ± 2,549 / 3,833 ± 1,223</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="is-rank">3.06</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.85</td> <!-- Faroese rank -->
   <td class="is ner">64.88 ± 1.32 / 67.55 ± 1.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.60 ± 0.90 / 40.52 ± 3.55</td> <!-- ScaLA-is -->
   <td class="is qa">12.39 ± 1.75 / 29.86 ± 2.90</td> <!-- NQiI -->
   <td class="fo ner">84.92 ± 0.70 / 85.65 ± 0.67</td> <!-- FoNE -->
   <td class="fo la">2.96 ± 2.66 / 45.42 ± 4.03</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="is-rank">2.88</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.05</td> <!-- Faroese rank -->
   <td class="is ner">78.01 ± 2.18 / 79.20 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.92 ± 1.91 / 46.95 ± 3.38</td> <!-- ScaLA-is -->
   <td class="is qa">10.47 ± 1.42 / 43.32 ± 3.55</td> <!-- NQiI -->
   <td class="fo ner">85.97 ± 1.12 / 86.52 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.02 ± 1.38 / 44.65 ± 2.65</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-2</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,965 ± 2,550 / 3,798 ± 1,216</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="is-rank">3.10</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.85</td> <!-- Faroese rank -->
   <td class="is ner">64.57 ± 1.62 / 67.12 ± 1.47</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.86 ± 1.11 / 43.33 ± 2.97</td> <!-- ScaLA-is -->
   <td class="is qa">10.76 ± 1.00 / 27.29 ± 2.41</td> <!-- NQiI -->
   <td class="fo ner">84.72 ± 0.84 / 85.44 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">3.79 ± 1.83 / 49.66 ± 2.54</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="is-rank">2.70</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.25</td> <!-- Faroese rank -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.42 ± 4.37 / 55.49 ± 2.89</td> <!-- NQiI -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.2</td> <!-- ScaLA-is version -->
   <td>9.3.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>9.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="is-rank">3.13</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.85</td> <!-- Faroese rank -->
   <td class="is ner">65.29 ± 1.46 / 60.81 ± 1.38</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.03 ± 1.72 / 42.37 ± 4.10</td> <!-- ScaLA-is -->
   <td class="is qa">10.49 ± 2.71 / 26.84 ± 3.93</td> <!-- NQiI -->
   <td class="fo ner">85.04 ± 0.57 / 85.72 ± 0.50</td> <!-- FoNE -->
   <td class="fo la">4.48 ± 1.63 / 44.45 ± 4.77</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="is-rank">3.24</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="is ner">63.35 ± 1.41 / 66.01 ± 1.32</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.94 ± 2.20 / 46.79 ± 2.19</td> <!-- ScaLA-is -->
   <td class="is qa">7.02 ± 0.72 / 34.05 ± 1.35</td> <!-- NQiI -->
   <td class="fo ner">82.76 ± 0.95 / 83.43 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">7.58 ± 3.56 / 52.05 ± 1.14</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="is-rank">3.41</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.59</td> <!-- Faroese rank -->
   <td class="is ner">48.31 ± 1.22 / 47.65 ± 1.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.18 ± 1.21 / 46.35 ± 3.68</td> <!-- ScaLA-is -->
   <td class="is qa">7.94 ± 0.81 / 36.61 ± 1.41</td> <!-- NQiI -->
   <td class="fo ner">72.99 ± 1.55 / 72.45 ± 1.56</td> <!-- FoNE -->
   <td class="fo la">13.40 ± 7.79 / 54.18 ± 5.13</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="is-rank">3.04</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.95</td> <!-- Faroese rank -->
   <td class="is ner">77.09 ± 2.00 / 78.38 ± 1.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.71 ± 3.02 / 42.83 ± 4.18</td> <!-- ScaLA-is -->
   <td class="is qa">8.56 ± 1.96 / 37.41 ± 5.69</td> <!-- NQiI -->
   <td class="fo ner">85.58 ± 1.04 / 86.23 ± 1.03</td> <!-- FoNE -->
   <td class="fo la">0.35 ± 2.36 / 43.55 ± 4.58</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="is-rank">3.29</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="is ner">63.11 ± 1.31 / 65.36 ± 1.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.47 ± 1.38 / 48.04 ± 2.34</td> <!-- ScaLA-is -->
   <td class="is qa">7.76 ± 0.57 / 36.28 ± 1.35</td> <!-- NQiI -->
   <td class="fo ner">82.36 ± 0.91 / 82.94 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">5.20 ± 2.67 / 50.88 ± 1.55</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="is-rank">3.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="is ner">63.31 ± 1.41 / 65.79 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.47 ± 1.56 / 49.04 ± 2.54</td> <!-- ScaLA-is -->
   <td class="is qa">5.99 ± 0.66 / 25.32 ± 0.78</td> <!-- NQiI -->
   <td class="fo ner">82.64 ± 0.63 / 83.27 ± 0.65</td> <!-- FoNE -->
   <td class="fo la">8.03 ± 2.01 / 51.96 ± 1.87</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="is-rank">3.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="is ner">66.23 ± 1.24 / 67.76 ± 1.08</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.04 ± 0.78 / 45.96 ± 2.83</td> <!-- ScaLA-is -->
   <td class="is qa">10.04 ± 0.99 / 28.66 ± 0.92</td> <!-- NQiI -->
   <td class="fo ner">82.97 ± 0.83 / 83.62 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 1.96 / 46.51 ± 4.19</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="is-rank">3.14</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.97</td> <!-- Faroese rank -->
   <td class="is ner">71.48 ± 1.97 / 73.71 ± 1.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.20 ± 2.00 / 43.42 ± 4.87</td> <!-- ScaLA-is -->
   <td class="is qa">8.19 ± 0.76 / 33.02 ± 1.85</td> <!-- NQiI -->
   <td class="fo ner">84.73 ± 1.49 / 85.19 ± 1.59</td> <!-- FoNE -->
   <td class="fo la">1.37 ± 2.46 / 39.78 ± 3.24</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>patrickvonplaten/norwegian-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,698 ± 2,699 / 3,891 ± 1,278</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="is-rank">3.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="is ner">60.79 ± 1.66 / 56.41 ± 1.53</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.29 ± 1.37 / 44.71 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is qa">6.64 ± 0.72 / 26.52 ± 0.97</td> <!-- NQiI -->
   <td class="fo ner">82.57 ± 0.93 / 83.35 ± 0.91</td> <!-- FoNE -->
   <td class="fo la">5.74 ± 3.53 / 48.75 ± 3.22</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="is-rank">3.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.79</td> <!-- Faroese rank -->
   <td class="is ner">62.23 ± 1.24 / 64.45 ± 1.23</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.45 ± 1.74 / 48.21 ± 1.91</td> <!-- ScaLA-is -->
   <td class="is qa">5.52 ± 0.55 / 26.85 ± 1.03</td> <!-- NQiI -->
   <td class="fo ner">80.52 ± 0.76 / 81.35 ± 0.69</td> <!-- FoNE -->
   <td class="fo la">6.51 ± 3.60 / 51.81 ± 1.95</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DeepPavlov/rubert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,785 ± 2,658 / 3,983 ± 1,289</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="is-rank">3.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="is ner">61.95 ± 1.77 / 57.52 ± 1.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.40 ± 1.34 / 43.49 ± 3.76</td> <!-- ScaLA-is -->
   <td class="is qa">6.04 ± 0.56 / 29.39 ± 0.76</td> <!-- NQiI -->
   <td class="fo ner">83.15 ± 0.73 / 83.90 ± 0.74</td> <!-- FoNE -->
   <td class="fo la">3.21 ± 2.89 / 47.97 ± 3.56</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="is-rank">2.73</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">50.64 ± 5.79 / 43.64 ± 5.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.06 ± 3.83 / 38.01 ± 2.85</td> <!-- ScaLA-is -->
   <td class="is qa">23.36 ± 4.19 / 46.70 ± 2.79</td> <!-- NQiI -->
   <td class="fo ner">60.21 ± 3.50 / 58.44 ± 3.67</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.10 ± 0.80</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="is-rank">2.77</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">27.54 ± 3.01 / 23.54 ± 2.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.61 ± 1.64 / 41.57 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">28.12 ± 3.77 / 54.61 ± 3.42</td> <!-- NQiI -->
   <td class="fo ner">46.50 ± 3.24 / 45.65 ± 2.54</td> <!-- FoNE -->
   <td class="fo la">3.95 ± 2.03 / 46.57 ± 3.18</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="is-rank">3.43</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="is ner">60.09 ± 1.69 / 55.62 ± 1.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.61 / 44.34 ± 3.01</td> <!-- ScaLA-is -->
   <td class="is qa">5.57 ± 0.78 / 28.89 ± 1.29</td> <!-- NQiI -->
   <td class="fo ner">82.76 ± 1.26 / 83.50 ± 1.20</td> <!-- FoNE -->
   <td class="fo la">3.98 ± 2.70 / 47.46 ± 2.35</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="is-rank">2.97</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.37</td> <!-- Faroese rank -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is qa">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="is-rank">3.36</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.99</td> <!-- Faroese rank -->
   <td class="is ner">63.36 ± 0.96 / 65.24 ± 0.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.02 ± 0.94 / 47.05 ± 2.13</td> <!-- ScaLA-is -->
   <td class="is qa">6.48 ± 0.37 / 27.44 ± 0.44</td> <!-- NQiI -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.89</td> <!-- Faroese rank -->
   <td class="is ner">62.44 ± 1.07 / 64.98 ± 0.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.91 ± 1.14 / 46.54 ± 2.46</td> <!-- ScaLA-is -->
   <td class="is qa">3.69 ± 0.48 / 27.48 ± 0.49</td> <!-- NQiI -->
   <td class="fo ner">82.24 ± 0.85 / 82.84 ± 0.78</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.41 / 50.47 ± 1.13</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="is-rank">3.38</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.08</td> <!-- Faroese rank -->
   <td class="is ner">49.68 ± 2.20 / 48.34 ± 1.96</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.33 ± 1.39 / 47.30 ± 2.09</td> <!-- ScaLA-is -->
   <td class="is qa">9.30 ± 0.95 / 36.88 ± 0.75</td> <!-- NQiI -->
   <td class="fo ner">72.46 ± 0.87 / 71.83 ± 0.83</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 3.27 / 48.20 ± 1.50</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="is-rank">3.00</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.47</td> <!-- Faroese rank -->
   <td class="is ner">36.79 ± 8.13 / 30.81 ± 7.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is qa">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="fo ner">61.90 ± 2.44 / 61.08 ± 2.76</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="is-rank">3.43</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.05</td> <!-- Faroese rank -->
   <td class="is ner">59.63 ± 1.40 / 61.65 ± 1.33</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.23 / 49.36 ± 1.58</td> <!-- ScaLA-is -->
   <td class="is qa">5.55 ± 0.70 / 27.22 ± 1.06</td> <!-- NQiI -->
   <td class="fo ner">80.21 ± 0.95 / 80.80 ± 0.97</td> <!-- FoNE -->
   <td class="fo la">1.10 ± 2.44 / 48.16 ± 1.47</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="is-rank">3.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.11</td> <!-- Faroese rank -->
   <td class="is ner">60.18 ± 3.20 / 55.70 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.07 ± 1.62 / 42.87 ± 4.48</td> <!-- ScaLA-is -->
   <td class="is qa">6.66 ± 0.67 / 32.13 ± 1.93</td> <!-- NQiI -->
   <td class="fo ner">81.78 ± 0.95 / 82.55 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">-1.18 ± 2.36 / 37.68 ± 3.64</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="is-rank">3.45</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.05</td> <!-- Faroese rank -->
   <td class="is ner">58.90 ± 1.06 / 62.01 ± 0.98</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.27 ± 1.53 / 43.40 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is qa">5.90 ± 0.57 / 27.22 ± 1.18</td> <!-- NQiI -->
   <td class="fo ner">80.58 ± 0.45 / 81.29 ± 0.46</td> <!-- FoNE -->
   <td class="fo la">1.58 ± 2.34 / 49.16 ± 2.33</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,043 ± 2,590 / 4,268 ± 1,377</td> <!-- Model inference speed -->
   <td class="rank">3.76</td> <!-- ScandEval rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.05</td> <!-- Faroese rank -->
   <td class="is ner">56.89 ± 1.71 / 52.39 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.13 ± 1.55 / 45.48 ± 2.51</td> <!-- ScaLA-is -->
   <td class="is qa">6.69 ± 0.63 / 32.15 ± 1.11</td> <!-- NQiI -->
   <td class="fo ner">80.48 ± 0.91 / 81.17 ± 0.85</td> <!-- FoNE -->
   <td class="fo la">0.60 ± 2.08 / 45.78 ± 2.54</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="is-rank">3.48</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.09</td> <!-- Faroese rank -->
   <td class="is ner">55.54 ± 2.48 / 51.36 ± 2.29</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.06 ± 1.29 / 43.27 ± 3.33</td> <!-- ScaLA-is -->
   <td class="is qa">5.42 ± 0.52 / 26.08 ± 0.59</td> <!-- NQiI -->
   <td class="fo ner">78.59 ± 1.16 / 79.35 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.65 ± 2.63 / 47.40 ± 3.23</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="is-rank">3.13</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">28.35 ± 2.89 / 26.44 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.14 ± 1.74 / 44.57 ± 3.85</td> <!-- ScaLA-is -->
   <td class="is qa">19.80 ± 2.66 / 43.44 ± 1.74</td> <!-- NQiI -->
   <td class="fo ner">60.54 ± 2.28 / 58.62 ± 1.89</td> <!-- FoNE -->
   <td class="fo la">-0.33 ± 1.12 / 37.78 ± 3.09</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="is-rank">3.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">34.48 ± 4.63 / 33.19 ± 4.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.24 ± 1.43 / 33.75 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is qa">18.10 ± 1.85 / 43.52 ± 0.87</td> <!-- NQiI -->
   <td class="fo ner">52.57 ± 3.85 / 51.44 ± 3.61</td> <!-- FoNE -->
   <td class="fo la">0.46 ± 2.01 / 44.83 ± 3.28</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="is-rank">3.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="is-rank">3.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.21</td> <!-- Faroese rank -->
   <td class="is ner">51.53 ± 10.96 / 53.86 ± 11.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.89 ± 1.79 / 47.82 ± 2.03</td> <!-- ScaLA-is -->
   <td class="is qa">5.19 ± 0.47 / 27.71 ± 0.76</td> <!-- NQiI -->
   <td class="fo ner">63.86 ± 20.89 / 64.42 ± 21.07</td> <!-- FoNE -->
   <td class="fo la">0.73 ± 2.11 / 49.36 ± 1.78</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="is-rank">3.09</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.63</td> <!-- Faroese rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.31 ± 3.62 / 40.78 ± 4.26</td> <!-- NQiI -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>9.2.0</td> <!-- NQiI version -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.2.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.87</td> <!-- ScandEval rank -->
   <td class="is-rank">3.20</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">36.10 ± 7.99 / 33.23 ± 7.96</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="fo ner">58.74 ± 3.04 / 58.94 ± 2.99</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="is-rank">3.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.18</td> <!-- Faroese rank -->
   <td class="is ner">42.07 ± 2.27 / 43.57 ± 2.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.27 ± 2.04 / 48.20 ± 1.32</td> <!-- ScaLA-is -->
   <td class="is qa">7.35 ± 0.66 / 20.44 ± 1.46</td> <!-- NQiI -->
   <td class="fo ner">73.80 ± 0.98 / 74.58 ± 0.92</td> <!-- FoNE -->
   <td class="fo la">0.81 ± 2.90 / 48.11 ± 2.18</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="is-rank">3.23</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.12 ± 2.50 / 39.44 ± 1.99</td> <!-- NQiI -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="is-rank">3.97</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.11</td> <!-- Faroese rank -->
   <td class="is ner">30.50 ± 1.95 / 30.08 ± 1.90</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.59 ± 1.49 / 46.53 ± 4.34</td> <!-- ScaLA-is -->
   <td class="is qa">0.06 ± 0.07 / 0.12 ± 0.11</td> <!-- NQiI -->
   <td class="fo ner">62.07 ± 1.18 / 61.72 ± 1.18</td> <!-- FoNE -->
   <td class="fo la">5.11 ± 3.80 / 47.64 ± 4.52</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="is-rank">3.87</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.21</td> <!-- Faroese rank -->
   <td class="is ner">25.49 ± 2.22 / 23.07 ± 2.05</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.63 ± 1.91 / 45.09 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">5.28 ± 0.62 / 22.50 ± 0.83</td> <!-- NQiI -->
   <td class="fo ner">58.50 ± 0.63 / 58.33 ± 0.70</td> <!-- FoNE -->
   <td class="fo la">5.96 ± 2.04 / 51.99 ± 1.53</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-small-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,002 ± 129 / 3,832 ± 1,242</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="is-rank">4.07</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.05</td> <!-- Faroese rank -->
   <td class="is ner">28.99 ± 12.22 / 28.98 ± 12.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.17 ± 1.37 / 38.53 ± 3.43</td> <!-- ScaLA-is -->
   <td class="is qa">0.42 ± 0.33 / 1.20 ± 1.50</td> <!-- NQiI -->
   <td class="fo ner">79.97 ± 1.24 / 80.28 ± 1.24</td> <!-- FoNE -->
   <td class="fo la">0.93 ± 2.91 / 45.79 ± 3.78</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="is-rank">3.81</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.31</td> <!-- Faroese rank -->
   <td class="is ner">28.16 ± 1.78 / 25.72 ± 1.72</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.05 ± 1.54 / 47.80 ± 2.45</td> <!-- ScaLA-is -->
   <td class="is qa">5.37 ± 0.70 / 24.09 ± 1.52</td> <!-- NQiI -->
   <td class="fo ner">59.66 ± 0.63 / 59.39 ± 0.60</td> <!-- FoNE -->
   <td class="fo la">4.58 ± 3.90 / 50.83 ± 2.59</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="is-rank">3.41</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.71</td> <!-- Faroese rank -->
   <td class="is ner">34.66 ± 4.29 / 23.47 ± 2.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.77 ± 1.05 / 39.63 ± 2.41</td> <!-- ScaLA-is -->
   <td class="is qa">12.80 ± 2.37 / 30.77 ± 2.12</td> <!-- NQiI -->
   <td class="fo ner">50.63 ± 2.20 / 47.73 ± 2.11</td> <!-- FoNE -->
   <td class="fo la">-0.52 ± 1.71 / 42.25 ± 3.52</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,523 ± 2,863 / 3,690 ± 1,195</td> <!-- Model inference speed -->
   <td class="rank">4.09</td> <!-- ScandEval rank -->
   <td class="is-rank">3.87</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.31</td> <!-- Faroese rank -->
   <td class="is ner">28.74 ± 1.77 / 28.47 ± 1.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.00 ± 0.94 / 47.57 ± 3.24</td> <!-- ScaLA-is -->
   <td class="is qa">3.47 ± 0.65 / 19.93 ± 2.77</td> <!-- NQiI -->
   <td class="fo ner">60.57 ± 0.86 / 60.42 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">4.16 ± 2.63 / 47.13 ± 3.43</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>TurkuNLP/bert-base-finnish-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,701 ± 2,104 / 5,450 ± 1,778</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="is-rank">3.77</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.61</td> <!-- Faroese rank -->
   <td class="is ner">34.58 ± 2.44 / 32.10 ± 2.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.55 ± 1.58 / 46.24 ± 3.27</td> <!-- ScaLA-is -->
   <td class="is qa">5.07 ± 0.53 / 24.32 ± 2.07</td> <!-- NQiI -->
   <td class="fo ner">51.26 ± 1.05 / 51.07 ± 1.06</td> <!-- FoNE -->
   <td class="fo la">1.77 ± 1.36 / 46.91 ± 2.77</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="is-rank">3.69</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.72</td> <!-- Faroese rank -->
   <td class="is ner">24.28 ± 6.08 / 24.83 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.18 ± 1.09 / 39.01 ± 2.76</td> <!-- ScaLA-is -->
   <td class="is qa">8.52 ± 2.30 / 21.32 ± 2.25</td> <!-- NQiI -->
   <td class="fo ner">44.60 ± 3.41 / 45.49 ± 3.40</td> <!-- FoNE -->
   <td class="fo la">1.82 ± 2.08 / 34.03 ± 0.66</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>asafaya/bert-base-arabic</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,347 ± 2,191 / 5,125 ± 1,672</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="is-rank">3.93</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.71</td> <!-- Faroese rank -->
   <td class="is ner">22.51 ± 3.32 / 20.42 ± 3.17</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.23 ± 1.20 / 43.22 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">5.05 ± 0.67 / 24.09 ± 1.66</td> <!-- NQiI -->
   <td class="fo ner">50.44 ± 1.82 / 49.80 ± 1.76</td> <!-- FoNE -->
   <td class="fo la">-0.06 ± 2.46 / 45.46 ± 4.05</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="is-rank">4.07</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.60</td> <!-- Faroese rank -->
   <td class="is ner">12.64 ± 2.49 / 11.10 ± 2.21</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.06 ± 1.76 / 47.57 ± 1.77</td> <!-- ScaLA-is -->
   <td class="is qa">4.77 ± 0.39 / 27.98 ± 1.03</td> <!-- NQiI -->
   <td class="fo ner">43.59 ± 0.80 / 42.84 ± 0.86</td> <!-- FoNE -->
   <td class="fo la">3.13 ± 1.29 / 49.29 ± 1.28</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="is-rank">3.61</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.09</td> <!-- Faroese rank -->
   <td class="is ner">9.04 ± 5.81 / 9.92 ± 4.55</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="fo ner">22.37 ± 5.43 / 21.93 ± 5.43</td> <!-- FoNE -->
   <td class="fo la">1.28 ± 1.43 / 39.41 ± 3.29</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="is-rank">3.70</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.02</td> <!-- Faroese rank -->
   <td class="is ner">20.60 ± 2.28 / 18.43 ± 1.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is qa">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="fo ner">34.58 ± 3.41 / 34.19 ± 2.69</td> <!-- FoNE -->
   <td class="fo la">-1.62 ± 2.08 / 43.25 ± 3.61</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,319 ± 94 / 656 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="is-rank">4.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.53</td> <!-- Faroese rank -->
   <td class="is ner">17.34 ± 1.13 / 16.43 ± 1.26</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.06 ± 0.99 / 36.73 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is qa">1.02 ± 0.30 / 21.61 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">48.70 ± 1.57 / 48.51 ± 1.57</td> <!-- FoNE -->
   <td class="fo la">2.37 ± 2.06 / 37.68 ± 3.25</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">4.46</td> <!-- ScandEval rank -->
   <td class="is-rank">3.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.60</td> <!-- Faroese rank -->
   <td class="is ner">3.90 ± 1.14 / 3.52 ± 0.94</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.00 ± 1.28 / 35.53 ± 1.87</td> <!-- ScaLA-is -->
   <td class="is qa">23.17 ± 2.78 / 44.72 ± 2.82</td> <!-- NQiI -->
   <td class="fo ner">4.00 ± 1.18 / 3.88 ± 1.17</td> <!-- FoNE -->
   <td class="fo la">-0.48 ± 2.65 / 38.61 ± 2.83</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.2</td> <!-- ScaLA-is version -->
   <td>12.3.2</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">4.46</td> <!-- ScandEval rank -->
   <td class="is-rank">4.19</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.72</td> <!-- Faroese rank -->
   <td class="is ner">12.39 ± 2.20 / 11.68 ± 2.17</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.63 ± 1.66 / 43.64 ± 4.69</td> <!-- ScaLA-is -->
   <td class="is qa">1.70 ± 0.45 / 16.29 ± 1.59</td> <!-- NQiI -->
   <td class="fo ner">45.16 ± 2.00 / 44.76 ± 2.01</td> <!-- FoNE -->
   <td class="fo la">2.24 ± 1.83 / 43.57 ± 4.41</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">4.50</td> <!-- ScandEval rank -->
   <td class="is-rank">3.90</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.09</td> <!-- Faroese rank -->
   <td class="is ner">14.13 ± 2.19 / 14.92 ± 2.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">7.92 ± 1.32 / 23.57 ± 1.69</td> <!-- NQiI -->
   <td class="fo ner">25.82 ± 3.98 / 27.68 ± 3.11</td> <!-- FoNE -->
   <td class="fo la">0.15 ± 2.21 / 34.34 ± 0.53</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="is-rank">3.98</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.09</td> <!-- Faroese rank -->
   <td class="is ner">12.21 ± 4.08 / 12.70 ± 3.62</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is qa">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="fo ner">19.56 ± 5.86 / 21.11 ± 5.19</td> <!-- FoNE -->
   <td class="fo la">1.14 ± 1.66 / 37.04 ± 3.83</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="is-rank">3.64</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.44</td> <!-- Faroese rank -->
   <td class="is ner">7.94 ± 3.03 / 7.63 ± 2.42</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is qa">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="fo ner">11.62 ± 2.48 / 12.09 ± 2.29</td> <!-- FoNE -->
   <td class="fo la">-0.42 ± 2.18 / 34.33 ± 1.47</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.59</td> <!-- ScandEval rank -->
   <td class="is-rank">3.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.67</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">16.85 ± 2.51 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 0.79 / 33.70 ± 0.64</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.0</td> <!-- ScaLA-is version -->
   <td>9.3.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>10.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="is-rank">4.09</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.11</td> <!-- Faroese rank -->
   <td class="is ner">16.02 ± 1.53 / 16.74 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="fo ner">29.84 ± 1.13 / 31.73 ± 1.44</td> <!-- FoNE -->
   <td class="fo la">-1.47 ± 1.54 / 35.84 ± 1.76</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">4.62</td> <!-- ScandEval rank -->
   <td class="is-rank">3.71</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.53</td> <!-- Faroese rank -->
   <td class="is ner">4.16 ± 2.70 / 4.70 ± 2.17</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is qa">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="fo ner">7.72 ± 1.73 / 8.30 ± 1.61</td> <!-- FoNE -->
   <td class="fo la">-0.36 ± 1.07 / 35.09 ± 1.96</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.62</td> <!-- ScandEval rank -->
   <td class="is-rank">4.22</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.01</td> <!-- Faroese rank -->
   <td class="is ner">13.58 ± 2.41 / 14.34 ± 2.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.04 ± 0.90 / 34.46 ± 1.41</td> <!-- ScaLA-is -->
   <td class="is qa">1.51 ± 0.68 / 13.16 ± 3.12</td> <!-- NQiI -->
   <td class="fo ner">29.22 ± 3.72 / 32.05 ± 2.71</td> <!-- FoNE -->
   <td class="fo la">1.01 ± 2.39 / 39.75 ± 4.10</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="is-rank">4.16</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.18</td> <!-- Faroese rank -->
   <td class="is ner">9.48 ± 3.08 / 9.33 ± 3.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is qa">3.10 ± 0.76 / 17.78 ± 2.28</td> <!-- NQiI -->
   <td class="fo ner">24.00 ± 1.89 / 24.07 ± 1.93</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.72 / 36.22 ± 2.35</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.79</td> <!-- ScandEval rank -->
   <td class="is-rank">4.27</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.32</td> <!-- Faroese rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.36 ± 3.51</td> <!-- NQiI -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,219 ± 712 / 3,276 ± 803</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="is-rank">4.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.35</td> <!-- Faroese rank -->
   <td class="is ner">9.96 ± 1.11 / 8.96 ± 1.05</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.10 ± 1.46 / 35.81 ± 3.45</td> <!-- ScaLA-is -->
   <td class="is qa">0.12 ± 0.10 / 4.48 ± 1.39</td> <!-- NQiI -->
   <td class="fo ner">12.10 ± 1.51 / 11.83 ± 1.50</td> <!-- FoNE -->
   <td class="fo la">0.64 ± 1.57 / 38.69 ± 3.19</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert</td> <!-- Model ID -->
   <td class="num_model_parameters">112</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,280 ± 2,296 / 4,838 ± 1,583</td> <!-- Model inference speed -->
   <td class="rank">5.04</td> <!-- ScandEval rank -->
   <td class="is-rank">4.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.67</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.03 ± 1.29 / 46.72 ± 2.28</td> <!-- ScaLA-is -->
   <td class="is qa">1.68 ± 0.72 / 13.50 ± 4.66</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-1.21 ± 2.82 / 44.15 ± 3.47</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">5.07</td> <!-- ScandEval rank -->
   <td class="is-rank">4.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.67</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 11.90 ± 2.74</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">5.07</td> <!-- ScandEval rank -->
   <td class="is-rank">4.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.67</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.24 ± 0.93 / 43.16 ± 3.72</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>11.0.0</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>11.0.0</td> <!-- ScaLA-fo version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Insular Scandinavian NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-UgWP5&quot; src=&quot;https://datawrapper.dwcdn.net/UgWP5/570/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
