---
layout: leaderboard
title: Faroese NLU 🇫🇴
---

<center>Last updated: 31/10/2024 09:54:15 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="faroese-nlu-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoNE">FoNE version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-fo">ScaLA-fo version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.00</td> <!-- ScandEval rank -->
   <td class="fo ner">91.31 ± 0.69 / 91.79 ± 0.47</td> <!-- FoNE -->
   <td class="fo la">64.39 ± 1.55 / 81.38 ± 1.04</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="fo ner">90.52 ± 0.47 / 90.83 ± 0.40</td> <!-- FoNE -->
   <td class="fo la">44.99 ± 11.76 / 71.54 ± 5.83</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="fo ner">88.60 ± 0.60 / 89.37 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">46.81 ± 2.12 / 72.76 ± 1.40</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="fo ner">90.60 ± 0.45 / 90.78 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">22.86 ± 13.14 / 59.92 ± 6.74</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,231 ± 8,171 / 4,863 ± 1,598</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="fo ner">88.81 ± 0.65 / 89.12 ± 0.56</td> <!-- FoNE -->
   <td class="fo la">30.92 ± 8.65 / 63.05 ± 4.66</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="fo ner">88.14 ± 0.58 / 88.89 ± 0.52</td> <!-- FoNE -->
   <td class="fo la">27.71 ± 9.67 / 61.60 ± 5.69</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="fo ner">86.51 ± 2.01 / 85.01 ± 2.45</td> <!-- FoNE -->
   <td class="fo la">35.09 ± 5.70 / 65.72 ± 3.27</td> <!-- ScaLA-fo -->
   <td>12.5.1</td> <!-- FoNE version -->
   <td>12.5.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="fo ner">85.80 ± 0.25 / 86.58 ± 0.26</td> <!-- FoNE -->
   <td class="fo la">30.88 ± 2.36 / 63.79 ± 1.33</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="fo ner">89.16 ± 0.66 / 89.62 ± 0.62</td> <!-- FoNE -->
   <td class="fo la">22.76 ± 10.57 / 60.04 ± 5.76</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="fo ner">87.35 ± 0.94 / 87.65 ± 0.94</td> <!-- FoNE -->
   <td class="fo la">14.65 ± 11.12 / 46.36 ± 10.23</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,004 ± 2,244 / 2,324 ± 761</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="fo ner">87.79 ± 0.40 / 88.46 ± 0.31</td> <!-- FoNE -->
   <td class="fo la">22.51 ± 10.65 / 55.58 ± 8.05</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="fo ner">86.94 ± 0.47 / 87.58 ± 0.46</td> <!-- FoNE -->
   <td class="fo la">12.35 ± 8.96 / 53.00 ± 5.17</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="fo ner">86.09 ± 1.03 / 86.85 ± 1.02</td> <!-- FoNE -->
   <td class="fo la">15.24 ± 6.84 / 50.54 ± 4.85</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8316</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="fo ner">81.62 ± 2.00 / 71.11 ± 2.84</td> <!-- FoNE -->
   <td class="fo la">13.49 ± 4.68 / 43.21 ± 3.64</td> <!-- ScaLA-fo -->
   <td>12.10.0</td> <!-- FoNE version -->
   <td>12.10.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128126</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="fo ner">77.59 ± 2.14 / 63.75 ± 5.57</td> <!-- FoNE -->
   <td class="fo la">14.58 ± 2.56 / 51.54 ± 2.48</td> <!-- ScaLA-fo -->
   <td>12.11.0</td> <!-- FoNE version -->
   <td>12.11.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">3.85</td> <!-- ScandEval rank -->
   <td class="fo ner">72.99 ± 1.55 / 72.45 ± 1.56</td> <!-- FoNE -->
   <td class="fo la">13.40 ± 7.79 / 54.18 ± 5.13</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-mC4-is</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,308 ± 1,614 / 3,851 ± 1,254</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="fo ner">88.44 ± 0.35 / 89.11 ± 0.38</td> <!-- FoNE -->
   <td class="fo la">11.83 ± 4.90 / 48.95 ± 6.81</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="fo ner">87.44 ± 0.35 / 88.01 ± 0.28</td> <!-- FoNE -->
   <td class="fo la">7.38 ± 6.28 / 47.69 ± 4.51</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-large</td> <!-- Model ID -->
   <td class="num_model_parameters">406</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,677 ± 719 / 1,886 ± 604</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="fo ner">86.84 ± 0.77 / 87.51 ± 0.72</td> <!-- FoNE -->
   <td class="fo la">9.82 ± 3.95 / 50.49 ± 3.45</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,697 ± 2,113 / 5,432 ± 1,749</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="fo ner">86.50 ± 0.96 / 87.11 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">10.13 ± 8.55 / 47.31 ± 7.04</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-sbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,757 ± 3,883 / 3,864 ± 1,237</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="fo ner">86.20 ± 0.50 / 86.91 ± 0.46</td> <!-- FoNE -->
   <td class="fo la">11.80 ± 7.52 / 53.06 ± 5.04</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.5</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="fo ner">82.76 ± 0.95 / 83.43 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">7.58 ± 3.56 / 52.05 ± 1.14</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="fo ner">82.64 ± 0.63 / 83.27 ± 0.65</td> <!-- FoNE -->
   <td class="fo la">8.03 ± 2.01 / 51.96 ± 1.87</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="fo ner">80.61 ± 0.91 / 81.31 ± 0.89</td> <!-- FoNE -->
   <td class="fo la">9.60 ± 3.82 / 52.30 ± 1.73</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="fo ner">77.06 ± 2.00 / 72.16 ± 2.64</td> <!-- FoNE -->
   <td class="fo la">8.00 ± 4.87 / 44.90 ± 5.26</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">4.51</td> <!-- ScandEval rank -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,119 ± 1,576 / 3,812 ± 1,242</td> <!-- Model inference speed -->
   <td class="rank">4.51</td> <!-- ScandEval rank -->
   <td class="fo ner">87.22 ± 0.68 / 87.92 ± 0.59</td> <!-- FoNE -->
   <td class="fo la">6.23 ± 6.96 / 48.55 ± 4.87</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,051 ± 3,289 / 2,704 ± 897</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="fo ner">86.10 ± 0.64 / 86.75 ± 0.57</td> <!-- FoNE -->
   <td class="fo la">6.28 ± 2.41 / 49.62 ± 2.08</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="fo ner">86.36 ± 0.57 / 87.14 ± 0.52</td> <!-- FoNE -->
   <td class="fo la">6.08 ± 4.57 / 48.47 ± 3.93</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="fo ner">84.02 ± 0.86 / 84.66 ± 0.82</td> <!-- FoNE -->
   <td class="fo la">5.65 ± 3.07 / 49.17 ± 3.05</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-igc</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,551 ± 1,656 / 3,918 ± 1,274</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="fo ner">83.82 ± 0.98 / 84.34 ± 0.88</td> <!-- FoNE -->
   <td class="fo la">4.93 ± 3.16 / 45.85 ± 3.66</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="fo ner">83.22 ± 0.71 / 83.91 ± 0.66</td> <!-- FoNE -->
   <td class="fo la">6.78 ± 3.31 / 51.53 ± 2.36</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="fo ner">82.36 ± 0.91 / 82.94 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">5.20 ± 2.67 / 50.88 ± 1.55</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>patrickvonplaten/norwegian-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,698 ± 2,699 / 3,891 ± 1,278</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="fo ner">82.57 ± 0.93 / 83.35 ± 0.91</td> <!-- FoNE -->
   <td class="fo la">5.74 ± 3.53 / 48.75 ± 3.22</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="fo ner">88.21 ± 0.97 / 88.63 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">3.16 ± 2.26 / 38.93 ± 4.61</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="fo ner">80.52 ± 0.76 / 81.35 ± 0.69</td> <!-- FoNE -->
   <td class="fo la">6.51 ± 3.60 / 51.81 ± 1.95</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="fo ner">88.39 ± 0.86 / 88.75 ± 0.75</td> <!-- FoNE -->
   <td class="fo la">2.85 ± 1.32 / 48.43 ± 2.29</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">103</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="fo ner">86.62 ± 0.43 / 87.31 ± 0.44</td> <!-- FoNE -->
   <td class="fo la">3.64 ± 3.82 / 49.77 ± 2.26</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,360 ± 1,611 / 3,858 ± 1,246</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="fo ner">87.13 ± 0.58 / 87.70 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">3.66 ± 3.33 / 40.81 ± 4.34</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/XLMR-ENIS</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,711 ± 2,333 / 2,141 ± 689</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="fo ner">87.09 ± 0.76 / 87.71 ± 0.73</td> <!-- FoNE -->
   <td class="fo la">3.09 ± 1.98 / 39.41 ± 4.45</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-2</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,550 / 3,798 ± 1,216</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="fo ner">84.72 ± 0.84 / 85.44 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">3.79 ± 1.83 / 49.66 ± 2.54</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,998 ± 2,549 / 3,833 ± 1,223</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="fo ner">84.92 ± 0.70 / 85.65 ± 0.67</td> <!-- FoNE -->
   <td class="fo la">2.96 ± 2.66 / 45.42 ± 4.03</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="fo ner">84.80 ± 0.85 / 85.49 ± 0.80</td> <!-- FoNE -->
   <td class="fo la">4.41 ± 4.92 / 50.84 ± 1.97</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="fo ner">85.04 ± 0.57 / 85.72 ± 0.50</td> <!-- FoNE -->
   <td class="fo la">4.48 ± 1.63 / 44.45 ± 4.77</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DeepPavlov/rubert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,785 ± 2,658 / 3,983 ± 1,289</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="fo ner">83.15 ± 0.73 / 83.90 ± 0.74</td> <!-- FoNE -->
   <td class="fo la">3.21 ± 2.89 / 47.97 ± 3.56</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="fo ner">83.21 ± 0.53 / 83.81 ± 0.45</td> <!-- FoNE -->
   <td class="fo la">2.37 ± 4.63 / 48.46 ± 3.19</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="fo ner">82.76 ± 1.26 / 83.50 ± 1.20</td> <!-- FoNE -->
   <td class="fo la">3.98 ± 2.70 / 47.46 ± 2.35</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="fo ner">82.97 ± 0.83 / 83.62 ± 0.81</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 1.96 / 46.51 ± 4.19</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">4.76</td> <!-- ScandEval rank -->
   <td class="fo ner">88.64 ± 0.34 / 89.11 ± 0.29</td> <!-- FoNE -->
   <td class="fo la">2.05 ± 2.30 / 47.88 ± 2.17</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="fo ner">82.05 ± 0.46 / 82.67 ± 0.43</td> <!-- FoNE -->
   <td class="fo la">3.98 ± 2.94 / 50.53 ± 1.83</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="fo ner">60.57 ± 2.87 / 55.05 ± 3.85</td> <!-- FoNE -->
   <td class="fo la">11.09 ± 2.47 / 51.49 ± 2.26</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="fo ner">82.24 ± 0.85 / 82.84 ± 0.78</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.41 / 50.47 ± 1.13</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">4.78</td> <!-- ScandEval rank -->
   <td class="fo ner">88.24 ± 0.58 / 88.48 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">1.73 ± 1.70 / 42.32 ± 5.16</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">4.78</td> <!-- ScandEval rank -->
   <td class="fo ner">87.85 ± 0.95 / 88.21 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">1.17 ± 2.11 / 40.94 ± 5.07</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">4.80</td> <!-- ScandEval rank -->
   <td class="fo ner">81.02 ± 0.75 / 81.74 ± 0.75</td> <!-- FoNE -->
   <td class="fo la">4.00 ± 2.04 / 50.51 ± 1.11</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">4.80</td> <!-- ScandEval rank -->
   <td class="fo ner">80.45 ± 1.48 / 81.32 ± 1.42</td> <!-- FoNE -->
   <td class="fo la">2.52 ± 1.88 / 47.78 ± 1.67</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">4.80</td> <!-- ScandEval rank -->
   <td class="fo ner">73.06 ± 1.51 / 72.61 ± 1.40</td> <!-- FoNE -->
   <td class="fo la">5.48 ± 2.42 / 49.18 ± 3.63</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32889</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="fo ner">71.89 ± 2.22 / 68.00 ± 2.95</td> <!-- FoNE -->
   <td class="fo la">4.76 ± 2.91 / 46.92 ± 3.94</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="fo ner">85.86 ± 0.51 / 86.55 ± 0.49</td> <!-- FoNE -->
   <td class="fo la">0.80 ± 2.32 / 42.37 ± 4.42</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,735 ± 7,558 / 6,846 ± 2,312</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="fo ner">85.58 ± 1.04 / 86.23 ± 1.03</td> <!-- FoNE -->
   <td class="fo la">0.35 ± 2.36 / 43.55 ± 4.58</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">4.85</td> <!-- ScandEval rank -->
   <td class="fo ner">84.73 ± 1.49 / 85.19 ± 1.59</td> <!-- FoNE -->
   <td class="fo la">1.37 ± 2.46 / 39.78 ± 3.24</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">4.87</td> <!-- ScandEval rank -->
   <td class="fo ner">84.00 ± 1.30 / 84.83 ± 1.28</td> <!-- FoNE -->
   <td class="fo la">1.94 ± 2.58 / 46.27 ± 2.74</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">4.87</td> <!-- ScandEval rank -->
   <td class="fo ner">84.14 ± 0.67 / 84.82 ± 0.64</td> <!-- FoNE -->
   <td class="fo la">1.33 ± 2.18 / 48.85 ± 1.23</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">4.87</td> <!-- ScandEval rank -->
   <td class="fo ner">83.96 ± 0.80 / 84.63 ± 0.76</td> <!-- FoNE -->
   <td class="fo la">1.05 ± 1.66 / 41.31 ± 4.91</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">4.88</td> <!-- ScandEval rank -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">4.88</td> <!-- ScandEval rank -->
   <td class="fo ner">77.00 ± 1.08 / 77.85 ± 1.05</td> <!-- FoNE -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">4.88</td> <!-- ScandEval rank -->
   <td class="fo ner">77.16 ± 0.93 / 78.00 ± 0.91</td> <!-- FoNE -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">4.88</td> <!-- ScandEval rank -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">4.90</td> <!-- ScandEval rank -->
   <td class="fo ner">66.98 ± 1.97 / 60.82 ± 2.81</td> <!-- FoNE -->
   <td class="fo la">5.80 ± 2.04 / 42.89 ± 2.71</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">4.90</td> <!-- ScandEval rank -->
   <td class="fo ner">67.42 ± 2.21 / 60.87 ± 3.22</td> <!-- FoNE -->
   <td class="fo la">7.02 ± 1.56 / 49.32 ± 2.91</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">4.91</td> <!-- ScandEval rank -->
   <td class="fo ner">75.63 ± 1.41 / 76.23 ± 1.36</td> <!-- FoNE -->
   <td class="fo la">3.65 ± 1.93 / 48.34 ± 1.78</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">80.21 ± 0.95 / 80.80 ± 0.97</td> <!-- FoNE -->
   <td class="fo la">1.10 ± 2.44 / 48.16 ± 1.47</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">79.99 ± 1.13 / 80.76 ± 1.10</td> <!-- FoNE -->
   <td class="fo la">1.32 ± 2.66 / 49.75 ± 1.50</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-small-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,002 ± 129 / 3,832 ± 1,242</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">79.97 ± 1.24 / 80.28 ± 1.24</td> <!-- FoNE -->
   <td class="fo la">0.93 ± 2.91 / 45.79 ± 3.78</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">80.58 ± 0.45 / 81.29 ± 0.46</td> <!-- FoNE -->
   <td class="fo la">1.58 ± 2.34 / 49.16 ± 2.33</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">37,268 ± 6,577 / 8,719 ± 2,865</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">80.48 ± 0.91 / 81.17 ± 0.85</td> <!-- FoNE -->
   <td class="fo la">0.60 ± 2.08 / 45.78 ± 2.54</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">50.34 ± 1.82 / 43.26 ± 1.69</td> <!-- FoNE -->
   <td class="fo la">8.01 ± 2.27 / 49.35 ± 3.81</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">4.93</td> <!-- ScandEval rank -->
   <td class="fo ner">80.92 ± 0.59 / 81.63 ± 0.56</td> <!-- FoNE -->
   <td class="fo la">1.19 ± 2.37 / 43.13 ± 4.70</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">4.94</td> <!-- ScandEval rank -->
   <td class="fo ner">85.97 ± 1.12 / 86.52 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.02 ± 1.38 / 44.65 ± 2.65</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">4.95</td> <!-- ScandEval rank -->
   <td class="fo ner">73.76 ± 1.34 / 70.21 ± 2.63</td> <!-- FoNE -->
   <td class="fo la">3.47 ± 1.97 / 49.04 ± 1.89</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">4.98</td> <!-- ScandEval rank -->
   <td class="fo ner">72.46 ± 0.87 / 71.83 ± 0.83</td> <!-- FoNE -->
   <td class="fo la">2.93 ± 3.27 / 48.20 ± 1.50</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">4.98</td> <!-- ScandEval rank -->
   <td class="fo ner">72.08 ± 1.25 / 72.93 ± 1.20</td> <!-- FoNE -->
   <td class="fo la">2.65 ± 2.40 / 48.48 ± 1.87</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="rank">4.98</td> <!-- ScandEval rank -->
   <td class="fo ner">78.59 ± 1.16 / 79.35 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.65 ± 2.63 / 47.40 ± 3.23</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">4.99</td> <!-- ScandEval rank -->
   <td class="fo ner">62.07 ± 1.18 / 61.72 ± 1.18</td> <!-- FoNE -->
   <td class="fo la">5.11 ± 3.80 / 47.64 ± 4.52</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">4.99</td> <!-- ScandEval rank -->
   <td class="fo ner">62.82 ± 3.50 / 58.05 ± 3.79</td> <!-- FoNE -->
   <td class="fo la">4.96 ± 2.36 / 43.40 ± 4.95</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">4.99</td> <!-- ScandEval rank -->
   <td class="fo ner">64.39 ± 3.14 / 59.80 ± 3.68</td> <!-- FoNE -->
   <td class="fo la">4.74 ± 4.59 / 48.96 ± 4.16</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">5.00</td> <!-- ScandEval rank -->
   <td class="fo ner">82.42 ± 1.60 / 78.22 ± 3.29</td> <!-- FoNE -->
   <td class="fo la">-0.38 ± 1.62 / 43.21 ± 3.75</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="rank">5.02</td> <!-- ScandEval rank -->
   <td class="fo ner">81.78 ± 0.95 / 82.55 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">-1.18 ± 2.36 / 37.68 ± 3.64</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">5.02</td> <!-- ScandEval rank -->
   <td class="fo ner">81.86 ± 2.08 / 67.98 ± 3.64</td> <!-- FoNE -->
   <td class="fo la">-0.97 ± 2.82 / 33.64 ± 0.85</td> <!-- ScaLA-fo -->
   <td>12.10.0</td> <!-- FoNE version -->
   <td>12.10.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">5.02</td> <!-- ScandEval rank -->
   <td class="fo ner">81.70 ± 0.58 / 82.18 ± 0.53</td> <!-- FoNE -->
   <td class="fo la">0.25 ± 2.87 / 44.81 ± 2.90</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="fo ner">67.52 ± 2.82 / 61.64 ± 3.39</td> <!-- FoNE -->
   <td class="fo la">3.35 ± 2.55 / 46.55 ± 3.36</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="fo ner">59.66 ± 0.63 / 59.39 ± 0.60</td> <!-- FoNE -->
   <td class="fo la">4.58 ± 3.90 / 50.83 ± 2.59</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">5.08</td> <!-- ScandEval rank -->
   <td class="fo ner">73.34 ± 1.57 / 74.24 ± 1.56</td> <!-- FoNE -->
   <td class="fo la">0.97 ± 2.25 / 44.25 ± 3.12</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">5.08</td> <!-- ScandEval rank -->
   <td class="fo ner">73.80 ± 0.98 / 74.58 ± 0.92</td> <!-- FoNE -->
   <td class="fo la">0.81 ± 2.90 / 48.11 ± 2.18</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">5.08</td> <!-- ScandEval rank -->
   <td class="fo ner">72.85 ± 1.76 / 65.14 ± 3.11</td> <!-- FoNE -->
   <td class="fo la">2.31 ± 1.58 / 46.15 ± 3.36</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="fo ner">71.10 ± 6.05 / 71.10 ± 6.05</td> <!-- FoNE -->
   <td class="fo la">2.29 ± 2.11 / 48.81 ± 1.33</td> <!-- ScaLA-fo -->
   <td>12.10.1</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/canine-c</td> <!-- Model ID -->
   <td class="num_model_parameters">132</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">1114</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">32,383 ± 4,831 / 9,953 ± 3,100</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="fo ner">72.41 ± 1.02 / 73.35 ± 1.01</td> <!-- FoNE -->
   <td class="fo la">1.20 ± 1.46 / 47.36 ± 1.53</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="fo ner">71.04 ± 1.85 / 70.33 ± 2.15</td> <!-- FoNE -->
   <td class="fo la">1.59 ± 1.29 / 33.68 ± 0.38</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="fo ner">58.50 ± 0.63 / 58.33 ± 0.70</td> <!-- FoNE -->
   <td class="fo la">5.96 ± 2.04 / 51.99 ± 1.53</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">5.14</td> <!-- ScandEval rank -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td>9.1.2</td> <!-- FoNE version -->
   <td>9.1.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">5.14</td> <!-- ScandEval rank -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>9.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">5.18</td> <!-- ScandEval rank -->
   <td class="fo ner">68.63 ± 1.70 / 41.26 ± 2.21</td> <!-- FoNE -->
   <td class="fo la">1.95 ± 2.22 / 42.77 ± 3.69</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">5.18</td> <!-- ScandEval rank -->
   <td class="fo ner">68.27 ± 3.22 / 62.82 ± 3.53</td> <!-- FoNE -->
   <td class="fo la">0.58 ± 1.85 / 36.79 ± 4.40</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">5.18</td> <!-- ScandEval rank -->
   <td class="fo ner">65.43 ± 3.19 / 63.09 ± 4.04</td> <!-- FoNE -->
   <td class="fo la">1.12 ± 2.01 / 35.45 ± 2.25</td> <!-- ScaLA-fo -->
   <td>12.11.0</td> <!-- FoNE version -->
   <td>12.11.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">5.21</td> <!-- ScandEval rank -->
   <td class="fo ner">59.50 ± 1.56 / 58.98 ± 1.55</td> <!-- FoNE -->
   <td class="fo la">3.25 ± 2.04 / 49.77 ± 1.40</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,523 ± 2,863 / 3,690 ± 1,195</td> <!-- Model inference speed -->
   <td class="rank">5.21</td> <!-- ScandEval rank -->
   <td class="fo ner">60.57 ± 0.86 / 60.42 ± 0.90</td> <!-- FoNE -->
   <td class="fo la">4.16 ± 2.63 / 47.13 ± 3.43</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">5.23</td> <!-- ScandEval rank -->
   <td class="fo ner">71.15 ± 1.89 / 69.19 ± 1.84</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.3</td> <!-- FoNE version -->
   <td>12.5.3</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">63.86 ± 20.89 / 64.42 ± 21.07</td> <!-- FoNE -->
   <td class="fo la">0.73 ± 2.11 / 49.36 ± 1.78</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">63.40 ± 2.78 / 59.96 ± 2.91</td> <!-- FoNE -->
   <td class="fo la">2.16 ± 2.25 / 39.38 ± 4.12</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">61.26 ± 4.22 / 59.21 ± 4.36</td> <!-- FoNE -->
   <td class="fo la">1.66 ± 1.37 / 45.22 ± 3.21</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">61.47 ± 1.57 / 58.60 ± 2.31</td> <!-- FoNE -->
   <td class="fo la">1.44 ± 1.85 / 34.71 ± 1.84</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">61.11 ± 4.21 / 58.55 ± 4.19</td> <!-- FoNE -->
   <td class="fo la">2.02 ± 1.68 / 39.88 ± 3.56</td> <!-- ScaLA-fo -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="fo ner">61.32 ± 4.26 / 59.28 ± 4.43</td> <!-- FoNE -->
   <td class="fo la">1.30 ± 1.64 / 45.10 ± 3.27</td> <!-- ScaLA-fo -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">5.30</td> <!-- ScandEval rank -->
   <td class="fo ner">47.88 ± 2.68 / 43.13 ± 2.36</td> <!-- FoNE -->
   <td class="fo la">5.79 ± 1.68 / 49.03 ± 2.13</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">5.30</td> <!-- ScandEval rank -->
   <td class="fo ner">66.82 ± 2.36 / 65.84 ± 2.35</td> <!-- FoNE -->
   <td class="fo la">-0.36 ± 1.67 / 37.57 ± 3.35</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">5.30</td> <!-- ScandEval rank -->
   <td class="fo ner">66.95 ± 5.19 / 65.92 ± 4.57</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.10 ± 0.80</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">5.30</td> <!-- ScandEval rank -->
   <td class="fo ner">67.89 ± 2.21 / 59.99 ± 1.84</td> <!-- FoNE -->
   <td class="fo la">-0.41 ± 1.64 / 38.95 ± 2.98</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">5.34</td> <!-- ScandEval rank -->
   <td class="fo ner">58.52 ± 3.91 / 59.67 ± 3.83</td> <!-- FoNE -->
   <td class="fo la">1.09 ± 2.20 / 33.70 ± 0.56</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">5.34</td> <!-- ScandEval rank -->
   <td class="fo ner">59.96 ± 2.42 / 58.61 ± 2.57</td> <!-- FoNE -->
   <td class="fo la">2.24 ± 1.78 / 41.32 ± 3.70</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">5.37</td> <!-- ScandEval rank -->
   <td class="fo ner">53.08 ± 1.92 / 52.63 ± 1.65</td> <!-- FoNE -->
   <td class="fo la">2.39 ± 2.27 / 48.60 ± 2.21</td> <!-- ScaLA-fo -->
   <td>12.10.0</td> <!-- FoNE version -->
   <td>12.10.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">5.39</td> <!-- ScandEval rank -->
   <td class="fo ner">62.22 ± 2.10 / 58.79 ± 2.20</td> <!-- FoNE -->
   <td class="fo la">0.01 ± 2.43 / 37.74 ± 4.20</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">5.39</td> <!-- ScandEval rank -->
   <td class="fo ner">62.97 ± 2.53 / 56.13 ± 2.99</td> <!-- FoNE -->
   <td class="fo la">0.14 ± 1.72 / 35.26 ± 1.84</td> <!-- ScaLA-fo -->
   <td>12.11.0</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">5.39</td> <!-- ScandEval rank -->
   <td class="fo ner">58.24 ± 3.73 / 47.44 ± 4.83</td> <!-- FoNE -->
   <td class="fo la">1.77 ± 2.13 / 45.44 ± 4.00</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">5.43</td> <!-- ScandEval rank -->
   <td class="fo ner">53.38 ± 3.96 / 53.04 ± 3.85</td> <!-- FoNE -->
   <td class="fo la">0.46 ± 2.01 / 44.83 ± 3.28</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">5.43</td> <!-- ScandEval rank -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">5.45</td> <!-- ScandEval rank -->
   <td class="fo ner">46.50 ± 3.24 / 45.65 ± 2.54</td> <!-- FoNE -->
   <td class="fo la">3.95 ± 2.03 / 46.57 ± 3.18</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">5.45</td> <!-- ScandEval rank -->
   <td class="fo ner">48.70 ± 1.57 / 48.51 ± 1.57</td> <!-- FoNE -->
   <td class="fo la">2.37 ± 2.06 / 37.68 ± 3.25</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">60.21 ± 3.50 / 58.44 ± 3.67</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.10 ± 0.80</td> <!-- ScaLA-fo -->
   <td>12.3.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">60.54 ± 2.28 / 58.62 ± 1.89</td> <!-- FoNE -->
   <td class="fo la">-0.33 ± 1.12 / 37.78 ± 3.09</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">60.88 ± 2.03 / 60.02 ± 1.84</td> <!-- FoNE -->
   <td class="fo la">-0.35 ± 1.18 / 34.50 ± 1.25</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">60.37 ± 3.60 / 59.38 ± 3.85</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">58.67 ± 3.95 / 58.47 ± 3.96</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">5.46</td> <!-- ScandEval rank -->
   <td class="fo ner">58.96 ± 2.05 / 52.20 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.3</td> <!-- FoNE version -->
   <td>12.5.3</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>TurkuNLP/bert-base-finnish-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,701 ± 2,104 / 5,450 ± 1,778</td> <!-- Model inference speed -->
   <td class="rank">5.50</td> <!-- ScandEval rank -->
   <td class="fo ner">51.26 ± 1.05 / 51.07 ± 1.06</td> <!-- FoNE -->
   <td class="fo la">1.77 ± 1.36 / 46.91 ± 2.77</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">5.50</td> <!-- ScandEval rank -->
   <td class="fo ner">53.06 ± 2.86 / 52.07 ± 2.88</td> <!-- FoNE -->
   <td class="fo la">2.01 ± 1.60 / 44.77 ± 3.74</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">5.50</td> <!-- ScandEval rank -->
   <td class="fo ner">52.91 ± 1.95 / 53.34 ± 1.93</td> <!-- FoNE -->
   <td class="fo la">1.67 ± 2.38 / 43.96 ± 3.66</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.5</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">5.51</td> <!-- ScandEval rank -->
   <td class="fo ner">56.88 ± 2.51 / 57.68 ± 2.14</td> <!-- FoNE -->
   <td class="fo la">-0.21 ± 2.20 / 34.20 ± 1.19</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">5.51</td> <!-- ScandEval rank -->
   <td class="fo ner">57.74 ± 3.24 / 57.86 ± 3.03</td> <!-- FoNE -->
   <td class="fo la">-0.57 ± 2.20 / 34.97 ± 1.92</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">5.55</td> <!-- ScandEval rank -->
   <td class="fo ner">54.65 ± 1.45 / 44.64 ± 2.43</td> <!-- FoNE -->
   <td class="fo la">-0.67 ± 3.41 / 38.53 ± 4.31</td> <!-- ScaLA-fo -->
   <td>12.9.1</td> <!-- FoNE version -->
   <td>12.9.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">5.55</td> <!-- ScandEval rank -->
   <td class="fo ner">56.61 ± 1.75 / 47.94 ± 1.94</td> <!-- FoNE -->
   <td class="fo la">-0.19 ± 1.95 / 36.90 ± 2.70</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.5</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">5.55</td> <!-- ScandEval rank -->
   <td class="fo ner">54.03 ± 3.25 / 50.83 ± 3.50</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 2.33 / 44.23 ± 3.90</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">5.57</td> <!-- ScandEval rank -->
   <td class="fo ner">43.59 ± 0.80 / 42.84 ± 0.86</td> <!-- FoNE -->
   <td class="fo la">3.13 ± 1.29 / 49.29 ± 1.28</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">5.57</td> <!-- ScandEval rank -->
   <td class="fo ner">43.32 ± 4.46 / 42.17 ± 4.06</td> <!-- FoNE -->
   <td class="fo la">4.28 ± 3.46 / 49.12 ± 2.54</td> <!-- ScaLA-fo -->
   <td>12.9.1</td> <!-- FoNE version -->
   <td>12.9.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">5.58</td> <!-- ScandEval rank -->
   <td class="fo ner">49.32 ± 2.20 / 46.86 ± 2.03</td> <!-- FoNE -->
   <td class="fo la">1.70 ± 2.41 / 37.62 ± 2.87</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.5</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">5.58</td> <!-- ScandEval rank -->
   <td class="fo ner">48.39 ± 4.46 / 49.13 ± 4.10</td> <!-- FoNE -->
   <td class="fo la">1.35 ± 2.97 / 47.85 ± 1.89</td> <!-- ScaLA-fo -->
   <td>12.10.8</td> <!-- FoNE version -->
   <td>12.10.8</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>asafaya/bert-base-arabic</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,347 ± 2,191 / 5,125 ± 1,672</td> <!-- Model inference speed -->
   <td class="rank">5.62</td> <!-- ScandEval rank -->
   <td class="fo ner">50.44 ± 1.82 / 49.80 ± 1.76</td> <!-- FoNE -->
   <td class="fo la">-0.06 ± 2.46 / 45.46 ± 4.05</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">5.62</td> <!-- ScandEval rank -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>9.2.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">5.62</td> <!-- ScandEval rank -->
   <td class="fo ner">53.24 ± 2.75 / 50.65 ± 2.85</td> <!-- FoNE -->
   <td class="fo la">-0.52 ± 1.71 / 42.25 ± 3.52</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">5.66</td> <!-- ScandEval rank -->
   <td class="fo ner">45.16 ± 2.00 / 44.76 ± 2.01</td> <!-- FoNE -->
   <td class="fo la">2.24 ± 1.83 / 43.57 ± 4.41</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">5.66</td> <!-- ScandEval rank -->
   <td class="fo ner">45.56 ± 1.92 / 42.78 ± 1.78</td> <!-- FoNE -->
   <td class="fo la">0.92 ± 2.19 / 40.29 ± 3.87</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">5.66</td> <!-- ScandEval rank -->
   <td class="fo ner">56.41 ± 1.60 / 48.01 ± 3.42</td> <!-- FoNE -->
   <td class="fo la">-1.45 ± 1.60 / 35.04 ± 2.81</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">5.70</td> <!-- ScandEval rank -->
   <td class="fo ner">47.90 ± 4.35 / 47.09 ± 3.68</td> <!-- FoNE -->
   <td class="fo la">-0.20 ± 1.73 / 34.85 ± 2.14</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">5.70</td> <!-- ScandEval rank -->
   <td class="fo ner">43.13 ± 3.96 / 42.16 ± 3.93</td> <!-- FoNE -->
   <td class="fo la">0.88 ± 1.93 / 34.15 ± 0.71</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">5.70</td> <!-- ScandEval rank -->
   <td class="fo ner">48.77 ± 2.56 / 48.35 ± 2.59</td> <!-- FoNE -->
   <td class="fo la">0.30 ± 1.20 / 34.30 ± 0.82</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">5.70</td> <!-- ScandEval rank -->
   <td class="fo ner">43.50 ± 5.67 / 44.70 ± 4.93</td> <!-- FoNE -->
   <td class="fo la">1.18 ± 1.97 / 37.59 ± 3.12</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">5.70</td> <!-- ScandEval rank -->
   <td class="fo ner">43.52 ± 3.97 / 44.38 ± 3.42</td> <!-- FoNE -->
   <td class="fo la">1.82 ± 2.08 / 34.03 ± 0.66</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">5.73</td> <!-- ScandEval rank -->
   <td class="fo ner">42.14 ± 1.37 / 42.12 ± 1.38</td> <!-- FoNE -->
   <td class="fo la">0.72 ± 1.51 / 37.81 ± 3.14</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">5.78</td> <!-- ScandEval rank -->
   <td class="fo ner">43.80 ± 4.46 / 44.36 ± 3.59</td> <!-- FoNE -->
   <td class="fo la">-0.42 ± 2.18 / 34.33 ± 1.47</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">5.82</td> <!-- ScandEval rank -->
   <td class="fo ner">43.45 ± 5.46 / 42.27 ± 5.19</td> <!-- FoNE -->
   <td class="fo la">-0.80 ± 2.08 / 40.32 ± 3.46</td> <!-- ScaLA-fo -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">5.83</td> <!-- ScandEval rank -->
   <td class="fo ner">36.20 ± 7.60 / 37.70 ± 5.04</td> <!-- FoNE -->
   <td class="fo la">0.91 ± 1.92 / 43.11 ± 3.81</td> <!-- ScaLA-fo -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">5.85</td> <!-- ScandEval rank -->
   <td class="fo ner">40.18 ± 3.60 / 39.95 ± 3.38</td> <!-- FoNE -->
   <td class="fo la">0.31 ± 1.71 / 41.35 ± 4.05</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">5.85</td> <!-- ScandEval rank -->
   <td class="fo ner">40.39 ± 5.42 / 38.39 ± 5.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">5.85</td> <!-- ScandEval rank -->
   <td class="fo ner">41.27 ± 4.31 / 40.85 ± 4.31</td> <!-- FoNE -->
   <td class="fo la">-0.20 ± 2.17 / 43.01 ± 3.39</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">5.91</td> <!-- ScandEval rank -->
   <td class="fo ner">39.50 ± 1.68 / 35.80 ± 1.50</td> <!-- FoNE -->
   <td class="fo la">-0.04 ± 1.87 / 33.86 ± 0.53</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">5.94</td> <!-- ScandEval rank -->
   <td class="fo ner">31.84 ± 5.22 / 34.80 ± 3.88</td> <!-- FoNE -->
   <td class="fo la">1.01 ± 2.39 / 39.75 ± 4.10</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">5.95</td> <!-- ScandEval rank -->
   <td class="fo ner">37.33 ± 1.14 / 37.83 ± 1.08</td> <!-- FoNE -->
   <td class="fo la">0.31 ± 0.60 / 33.42 ± 0.32</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">5.95</td> <!-- ScandEval rank -->
   <td class="fo ner">34.20 ± 5.85 / 35.35 ± 5.04</td> <!-- FoNE -->
   <td class="fo la">-0.36 ± 1.07 / 35.09 ± 1.96</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">6.01</td> <!-- ScandEval rank -->
   <td class="fo ner">37.60 ± 2.86 / 36.37 ± 2.61</td> <!-- FoNE -->
   <td class="fo la">-1.62 ± 2.08 / 43.25 ± 3.61</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">6.04</td> <!-- ScandEval rank -->
   <td class="fo ner">26.54 ± 5.30 / 26.05 ± 5.17</td> <!-- FoNE -->
   <td class="fo la">0.59 ± 2.72 / 45.88 ± 2.69</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">6.04</td> <!-- ScandEval rank -->
   <td class="fo ner">25.08 ± 6.04 / 25.94 ± 6.17</td> <!-- FoNE -->
   <td class="fo la">1.69 ± 2.72 / 36.58 ± 2.95</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">6.04</td> <!-- ScandEval rank -->
   <td class="fo ner">24.45 ± 3.09 / 24.45 ± 2.84</td> <!-- FoNE -->
   <td class="fo la">0.75 ± 1.18 / 45.44 ± 2.95</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">6.06</td> <!-- ScandEval rank -->
   <td class="fo ner">32.16 ± 4.25 / 31.47 ± 4.12</td> <!-- FoNE -->
   <td class="fo la">-0.48 ± 2.65 / 38.61 ± 2.83</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32896</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">6.06</td> <!-- ScandEval rank -->
   <td class="fo ner">27.72 ± 2.64 / 34.07 ± 1.05</td> <!-- FoNE -->
   <td class="fo la">0.30 ± 1.58 / 36.35 ± 3.68</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">6.14</td> <!-- ScandEval rank -->
   <td class="fo ner">18.65 ± 5.84 / 20.64 ± 4.75</td> <!-- FoNE -->
   <td class="fo la">1.14 ± 1.66 / 37.04 ± 3.83</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">6.14</td> <!-- ScandEval rank -->
   <td class="fo ner">19.57 ± 7.44 / 20.21 ± 6.81</td> <!-- FoNE -->
   <td class="fo la">0.70 ± 1.76 / 42.12 ± 4.88</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">6.14</td> <!-- ScandEval rank -->
   <td class="fo ner">19.87 ± 2.97 / 20.57 ± 3.02</td> <!-- FoNE -->
   <td class="fo la">1.15 ± 1.31 / 34.80 ± 1.23</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">6.14</td> <!-- ScandEval rank -->
   <td class="fo ner">20.15 ± 4.19 / 19.76 ± 4.13</td> <!-- FoNE -->
   <td class="fo la">1.28 ± 1.43 / 39.41 ± 3.29</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">6.16</td> <!-- ScandEval rank -->
   <td class="fo ner">29.34 ± 1.57 / 30.91 ± 1.51</td> <!-- FoNE -->
   <td class="fo la">-1.47 ± 1.54 / 35.84 ± 1.76</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">6.16</td> <!-- ScandEval rank -->
   <td class="fo ner">26.11 ± 3.40 / 27.37 ± 2.80</td> <!-- FoNE -->
   <td class="fo la">0.15 ± 2.21 / 34.34 ± 0.53</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">6.16</td> <!-- ScandEval rank -->
   <td class="fo ner">24.82 ± 5.78 / 24.93 ± 5.16</td> <!-- FoNE -->
   <td class="fo la">-0.23 ± 1.50 / 45.07 ± 4.44</td> <!-- ScaLA-fo -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">6.26</td> <!-- ScandEval rank -->
   <td class="fo ner">14.50 ± 8.39 / 14.37 ± 8.27</td> <!-- FoNE -->
   <td class="fo la">-0.30 ± 0.59 / 33.39 ± 0.33</td> <!-- ScaLA-fo -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">6.26</td> <!-- ScandEval rank -->
   <td class="fo ner">22.30 ± 2.37 / 22.37 ± 2.40</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.72 / 36.22 ± 2.35</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">6.26</td> <!-- ScandEval rank -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">6.27</td> <!-- ScandEval rank -->
   <td class="fo ner">27.10 ± 1.40 / 27.13 ± 1.63</td> <!-- FoNE -->
   <td class="fo la">-1.52 ± 2.13 / 37.81 ± 1.56</td> <!-- ScaLA-fo -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">6.35</td> <!-- ScandEval rank -->
   <td class="fo ner">12.10 ± 1.51 / 11.83 ± 1.50</td> <!-- FoNE -->
   <td class="fo la">0.64 ± 1.57 / 38.69 ± 3.19</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">6.55</td> <!-- ScandEval rank -->
   <td class="fo ner">2.64 ± 1.41 / 2.99 ± 1.54</td> <!-- FoNE -->
   <td class="fo la">0.53 ± 1.90 / 36.70 ± 3.80</td> <!-- ScaLA-fo -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">6.67</td> <!-- ScandEval rank -->
   <td class="fo ner">1.84 ± 1.25 / 1.80 ± 1.23</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 0.79 / 33.70 ± 0.64</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- FoNE version -->
   <td>10.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icechat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">49,558 ± 7,930 / 13,921 ± 4,425</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/jonas-hallgrimsson-gpt2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">32,644 ± 3,887 / 11,289 ± 3,585</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/qa-icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">44,889 ± 6,944 / 13,506 ± 4,256</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>12.5.2</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.24 ± 0.93 / 43.16 ± 3.72</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>11.0.0</td> <!-- ScaLA-fo version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert</td> <!-- Model ID -->
   <td class="num_model_parameters">112</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,280 ± 2,296 / 4,838 ± 1,583</td> <!-- Model inference speed -->
   <td class="rank">6.72</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-1.21 ± 2.82 / 44.15 ± 3.47</td> <!-- ScaLA-fo -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/faroese-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Faroese NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-UBxi4&quot; src=&quot;https://datawrapper.dwcdn.net/UBxi4/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
