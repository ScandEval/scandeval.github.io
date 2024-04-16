---
layout: leaderboard
title: Norwegian NLU 🇳🇴
---

<center>Last updated: 16/04/2024 17:03:09 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="norwegian-nlu-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nb">NorNE-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nn">NorNE-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NoReC">NoReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nb">ScaLA-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nn">ScaLA-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorQuAD">NorQuAD version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="rank">1.15</td> <!-- ScandEval rank -->
   <td class="no ner">93.12 ± 0.83 / 90.13 ± 1.02</td> <!-- NorNE-nb -->
   <td class="no ner">89.39 ± 0.52 / 86.03 ± 0.65</td> <!-- NorNE-nn -->
   <td class="no sent">64.62 ± 1.36 / 75.40 ± 0.97</td> <!-- NoReC -->
   <td class="no la">77.97 ± 3.04 / 88.19 ± 1.89</td> <!-- ScaLA-nb -->
   <td class="no la">76.30 ± 1.56 / 87.68 ± 0.86</td> <!-- ScaLA-nn -->
   <td class="no qa">66.03 ± 1.19 / 79.64 ± 1.09</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,343 ± 1,236 / 1,444 ± 456</td> <!-- Model inference speed -->
   <td class="rank">1.24</td> <!-- ScandEval rank -->
   <td class="no ner">91.32 ± 0.90 / 87.09 ± 1.01</td> <!-- NorNE-nb -->
   <td class="no ner">87.29 ± 0.74 / 83.06 ± 1.22</td> <!-- NorNE-nn -->
   <td class="no sent">63.40 ± 1.38 / 74.60 ± 1.12</td> <!-- NoReC -->
   <td class="no la">78.43 ± 1.47 / 88.75 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">79.59 ± 1.72 / 89.56 ± 0.88</td> <!-- ScaLA-nn -->
   <td class="no qa">59.20 ± 1.13 / 73.80 ± 1.05</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">1.35</td> <!-- ScandEval rank -->
   <td class="no ner">92.36 ± 0.55 / 89.79 ± 0.73</td> <!-- NorNE-nb -->
   <td class="no ner">88.49 ± 0.97 / 85.45 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">59.73 ± 2.46 / 70.77 ± 3.26</td> <!-- NoReC -->
   <td class="no la">74.40 ± 2.03 / 86.34 ± 1.28</td> <!-- ScaLA-nb -->
   <td class="no la">68.85 ± 3.21 / 83.17 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">57.67 ± 1.86 / 72.51 ± 1.52</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="no ner">92.01 ± 0.98 / 92.36 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">87.17 ± 1.24 / 88.75 ± 0.89</td> <!-- NorNE-nn -->
   <td class="no sent">60.11 ± 2.96 / 70.55 ± 3.99</td> <!-- NoReC -->
   <td class="no la">72.85 ± 5.60 / 85.73 ± 3.14</td> <!-- ScaLA-nb -->
   <td class="no la">65.56 ± 1.91 / 82.23 ± 0.97</td> <!-- ScaLA-nn -->
   <td class="no qa">60.38 ± 0.95 / 75.42 ± 1.16</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.38</td> <!-- ScandEval rank -->
   <td class="no ner">92.49 ± 0.81 / 92.58 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">87.22 ± 1.19 / 88.71 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">58.77 ± 3.69 / 69.56 ± 4.55</td> <!-- NoReC -->
   <td class="no la">76.30 ± 2.09 / 87.19 ± 1.40</td> <!-- ScaLA-nb -->
   <td class="no la">64.11 ± 5.18 / 80.68 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">60.69 ± 1.15 / 75.73 ± 1.06</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.46</td> <!-- ScandEval rank -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">49.93 ± 3.13 / 77.72 ± 1.70</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">1.49</td> <!-- ScandEval rank -->
   <td class="no ner">86.39 ± 1.06 / 85.20 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">83.22 ± 1.44 / 82.50 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">59.61 ± 1.28 / 71.40 ± 1.68</td> <!-- NoReC -->
   <td class="no la">67.88 ± 7.37 / 82.75 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">62.44 ± 4.39 / 80.43 ± 2.39</td> <!-- ScaLA-nn -->
   <td class="no qa">55.69 ± 1.60 / 70.77 ± 1.64</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="rank">1.53</td> <!-- ScandEval rank -->
   <td class="no ner">86.78 ± 0.95 / 85.37 ± 0.78</td> <!-- NorNE-nb -->
   <td class="no ner">83.28 ± 1.29 / 82.22 ± 1.30</td> <!-- NorNE-nn -->
   <td class="no sent">58.73 ± 2.31 / 70.10 ± 2.66</td> <!-- NoReC -->
   <td class="no la">70.73 ± 3.19 / 84.71 ± 1.82</td> <!-- ScaLA-nb -->
   <td class="no la">59.58 ± 7.22 / 78.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">56.04 ± 1.56 / 71.02 ± 1.42</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">1.54</td> <!-- ScandEval rank -->
   <td class="no ner">92.09 ± 0.51 / 89.67 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">86.85 ± 1.94 / 83.35 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">59.84 ± 1.40 / 72.11 ± 1.25</td> <!-- NoReC -->
   <td class="no la">73.33 ± 2.17 / 85.89 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">71.06 ± 1.62 / 84.78 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">43.67 ± 1.71 / 57.42 ± 1.56</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="rank">1.56</td> <!-- ScandEval rank -->
   <td class="no ner">92.24 ± 0.44 / 89.66 ± 0.60</td> <!-- NorNE-nb -->
   <td class="no ner">87.58 ± 0.68 / 84.23 ± 0.85</td> <!-- NorNE-nn -->
   <td class="no sent">59.98 ± 1.33 / 71.70 ± 1.69</td> <!-- NoReC -->
   <td class="no la">70.18 ± 1.41 / 83.83 ± 0.91</td> <!-- ScaLA-nb -->
   <td class="no la">70.81 ± 1.50 / 84.45 ± 0.95</td> <!-- ScaLA-nn -->
   <td class="no qa">44.27 ± 1.46 / 58.30 ± 1.82</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="no ner">88.66 ± 1.23 / 84.60 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">84.59 ± 1.98 / 80.07 ± 2.11</td> <!-- NorNE-nn -->
   <td class="no sent">55.59 ± 10.43 / 67.82 ± 9.45</td> <!-- NoReC -->
   <td class="no la">71.43 ± 1.67 / 84.61 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">53.30 ± 13.11 / 74.52 ± 7.96</td> <!-- ScaLA-nn -->
   <td class="no qa">57.38 ± 1.41 / 72.48 ± 1.49</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="no ner">88.70 ± 2.05 / 84.95 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.11 ± 1.67 / 82.16 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">54.19 ± 3.15 / 65.18 ± 4.55</td> <!-- NoReC -->
   <td class="no la">69.83 ± 2.01 / 84.72 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">54.84 ± 12.59 / 75.13 ± 9.44</td> <!-- ScaLA-nn -->
   <td class="no qa">58.18 ± 1.84 / 71.29 ± 1.51</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="rank">1.64</td> <!-- ScandEval rank -->
   <td class="no ner">88.99 ± 0.96 / 86.13 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">82.99 ± 1.53 / 78.66 ± 1.85</td> <!-- NorNE-nn -->
   <td class="no sent">57.37 ± 1.31 / 70.45 ± 1.13</td> <!-- NoReC -->
   <td class="no la">69.92 ± 2.01 / 83.51 ± 1.33</td> <!-- ScaLA-nb -->
   <td class="no la">70.05 ± 1.76 / 84.13 ± 1.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.98 ± 3.70 / 55.88 ± 3.70</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="no ner">93.01 ± 0.68 / 89.36 ± 0.86</td> <!-- NorNE-nb -->
   <td class="no ner">88.43 ± 0.78 / 84.38 ± 0.81</td> <!-- NorNE-nn -->
   <td class="no sent">60.84 ± 1.48 / 72.16 ± 1.38</td> <!-- NoReC -->
   <td class="no la">73.89 ± 1.31 / 86.19 ± 0.93</td> <!-- ScaLA-nb -->
   <td class="no la">72.10 ± 2.07 / 85.37 ± 1.33</td> <!-- ScaLA-nn -->
   <td class="no qa">33.01 ± 3.06 / 45.28 ± 3.64</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="no ner">91.90 ± 0.54 / 89.55 ± 0.57</td> <!-- NorNE-nb -->
   <td class="no ner">86.81 ± 1.35 / 83.46 ± 1.68</td> <!-- NorNE-nn -->
   <td class="no sent">53.69 ± 4.28 / 63.69 ± 6.95</td> <!-- NoReC -->
   <td class="no la">70.55 ± 1.64 / 84.79 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">61.21 ± 1.20 / 79.87 ± 0.76</td> <!-- ScaLA-nn -->
   <td class="no qa">48.82 ± 1.20 / 63.72 ± 1.06</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="no ner">91.09 ± 0.65 / 88.45 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">85.72 ± 1.92 / 81.88 ± 2.16</td> <!-- NorNE-nn -->
   <td class="no sent">50.90 ± 3.01 / 60.96 ± 5.41</td> <!-- NoReC -->
   <td class="no la">69.34 ± 3.13 / 83.11 ± 2.17</td> <!-- ScaLA-nb -->
   <td class="no la">66.24 ± 2.41 / 82.36 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">48.45 ± 0.63 / 62.96 ± 0.80</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="no ner">91.66 ± 0.74 / 89.26 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">87.74 ± 0.77 / 84.51 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">57.43 ± 1.55 / 70.43 ± 1.41</td> <!-- NoReC -->
   <td class="no la">63.31 ± 11.58 / 80.18 ± 5.59</td> <!-- ScaLA-nb -->
   <td class="no la">62.79 ± 11.35 / 79.65 ± 6.48</td> <!-- ScaLA-nn -->
   <td class="no qa">41.05 ± 2.59 / 54.44 ± 3.33</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="no ner">91.17 ± 0.52 / 91.04 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">87.30 ± 1.07 / 88.83 ± 0.84</td> <!-- NorNE-nn -->
   <td class="no sent">59.10 ± 1.47 / 70.50 ± 2.06</td> <!-- NoReC -->
   <td class="no la">74.32 ± 1.76 / 86.47 ± 1.18</td> <!-- ScaLA-nb -->
   <td class="no la">72.94 ± 1.63 / 86.07 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">34.06 ± 2.05 / 45.46 ± 2.65</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="no ner">89.86 ± 0.93 / 90.64 ± 0.80</td> <!-- NorNE-nb -->
   <td class="no ner">84.32 ± 1.08 / 86.52 ± 0.94</td> <!-- NorNE-nn -->
   <td class="no sent">61.52 ± 1.87 / 72.72 ± 1.95</td> <!-- NoReC -->
   <td class="no la">62.34 ± 2.48 / 79.94 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">34.88 ± 11.23 / 66.51 ± 5.72</td> <!-- ScaLA-nn -->
   <td class="no qa">53.01 ± 1.05 / 70.46 ± 0.86</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="no ner">90.08 ± 0.76 / 87.12 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">86.04 ± 0.78 / 81.89 ± 0.98</td> <!-- NorNE-nn -->
   <td class="no sent">56.35 ± 1.25 / 69.31 ± 1.02</td> <!-- NoReC -->
   <td class="no la">59.38 ± 2.52 / 78.02 ± 1.71</td> <!-- ScaLA-nb -->
   <td class="no la">46.54 ± 3.21 / 71.78 ± 2.00</td> <!-- ScaLA-nn -->
   <td class="no qa">55.05 ± 1.24 / 70.46 ± 1.22</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="no ner">91.16 ± 0.71 / 88.71 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">84.75 ± 1.23 / 80.56 ± 1.59</td> <!-- NorNE-nn -->
   <td class="no sent">55.25 ± 2.36 / 66.95 ± 2.79</td> <!-- NoReC -->
   <td class="no la">68.03 ± 2.37 / 82.12 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">66.90 ± 2.07 / 82.33 ± 1.34</td> <!-- ScaLA-nn -->
   <td class="no qa">41.65 ± 1.17 / 55.71 ± 1.73</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="no ner">90.65 ± 0.66 / 88.03 ± 0.77</td> <!-- NorNE-nb -->
   <td class="no ner">84.88 ± 1.55 / 81.01 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">52.44 ± 2.90 / 62.48 ± 4.62</td> <!-- NoReC -->
   <td class="no la">68.77 ± 2.01 / 83.10 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">65.40 ± 2.43 / 81.72 ± 1.68</td> <!-- ScaLA-nn -->
   <td class="no qa">43.13 ± 2.05 / 56.76 ± 2.21</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="no ner">91.66 ± 1.24 / 89.34 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">86.19 ± 0.97 / 82.86 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">50.25 ± 15.36 / 63.55 ± 13.05</td> <!-- NoReC -->
   <td class="no la">55.51 ± 18.28 / 74.00 ± 13.38</td> <!-- ScaLA-nb -->
   <td class="no la">43.89 ± 14.81 / 68.88 ± 10.32</td> <!-- ScaLA-nn -->
   <td class="no qa">57.57 ± 2.43 / 72.69 ± 2.22</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="no ner">90.02 ± 0.72 / 86.99 ± 0.87</td> <!-- NorNE-nb -->
   <td class="no ner">86.52 ± 1.17 / 83.03 ± 1.53</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 3.24 / 61.35 ± 5.46</td> <!-- NoReC -->
   <td class="no la">67.29 ± 2.13 / 82.23 ± 1.36</td> <!-- ScaLA-nb -->
   <td class="no la">56.67 ± 2.29 / 76.74 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no qa">48.63 ± 1.31 / 63.28 ± 1.09</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="no ner">89.07 ± 1.19 / 85.81 ± 1.57</td> <!-- NorNE-nb -->
   <td class="no ner">83.27 ± 1.68 / 78.80 ± 2.22</td> <!-- NorNE-nn -->
   <td class="no sent">53.23 ± 1.67 / 65.23 ± 2.65</td> <!-- NoReC -->
   <td class="no la">70.06 ± 2.33 / 83.61 ± 1.61</td> <!-- ScaLA-nb -->
   <td class="no la">66.81 ± 1.83 / 82.19 ± 1.20</td> <!-- ScaLA-nn -->
   <td class="no qa">34.17 ± 2.16 / 47.61 ± 2.55</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="no ner">90.58 ± 0.91 / 87.84 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">85.21 ± 1.05 / 81.57 ± 1.30</td> <!-- NorNE-nn -->
   <td class="no sent">54.26 ± 1.75 / 67.25 ± 1.47</td> <!-- NoReC -->
   <td class="no la">59.44 ± 1.47 / 78.80 ± 1.00</td> <!-- ScaLA-nb -->
   <td class="no la">49.30 ± 1.39 / 74.02 ± 1.04</td> <!-- ScaLA-nn -->
   <td class="no qa">46.42 ± 1.44 / 61.82 ± 1.47</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.01</td> <!-- ScandEval rank -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">46.44 ± 1.55 / 72.64 ± 1.26</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="no ner">90.60 ± 1.16 / 87.83 ± 1.34</td> <!-- NorNE-nb -->
   <td class="no ner">86.76 ± 0.82 / 83.48 ± 0.98</td> <!-- NorNE-nn -->
   <td class="no sent">52.19 ± 2.87 / 65.60 ± 2.58</td> <!-- NoReC -->
   <td class="no la">54.98 ± 14.19 / 75.67 ± 6.70</td> <!-- ScaLA-nb -->
   <td class="no la">58.33 ± 10.94 / 77.88 ± 5.29</td> <!-- ScaLA-nn -->
   <td class="no qa">29.17 ± 1.36 / 41.75 ± 1.59</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">837 ± 294 / 126 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="no ner">74.92 ± 1.24 / 64.00 ± 2.37</td> <!-- NorNE-nb -->
   <td class="no ner">75.34 ± 1.15 / 68.02 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">57.64 ± 1.33 / 71.34 ± 1.15</td> <!-- NoReC -->
   <td class="no la">49.93 ± 1.78 / 69.26 ± 1.76</td> <!-- ScaLA-nb -->
   <td class="no la">34.22 ± 2.98 / 57.61 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 1.06 / 71.71 ± 0.83</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="no ner">86.82 ± 0.53 / 84.15 ± 0.59</td> <!-- NorNE-nb -->
   <td class="no ner">79.91 ± 1.17 / 76.65 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">47.84 ± 2.44 / 60.67 ± 3.47</td> <!-- NoReC -->
   <td class="no la">51.99 ± 11.45 / 72.87 ± 8.55</td> <!-- ScaLA-nb -->
   <td class="no la">30.57 ± 8.63 / 62.90 ± 7.32</td> <!-- ScaLA-nn -->
   <td class="no qa">36.75 ± 2.18 / 50.77 ± 2.11</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="no ner">87.50 ± 0.53 / 87.45 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">80.57 ± 1.41 / 82.71 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">47.11 ± 2.05 / 60.70 ± 3.19</td> <!-- NoReC -->
   <td class="no la">52.62 ± 3.99 / 75.01 ± 2.43</td> <!-- ScaLA-nb -->
   <td class="no la">25.06 ± 6.94 / 60.75 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">38.40 ± 2.57 / 50.51 ± 3.52</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="no ner">88.26 ± 1.11 / 89.24 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">81.37 ± 1.67 / 83.89 ± 1.34</td> <!-- NorNE-nn -->
   <td class="no sent">54.61 ± 1.51 / 67.19 ± 1.65</td> <!-- NoReC -->
   <td class="no la">50.35 ± 1.78 / 73.06 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">22.15 ± 9.02 / 58.20 ± 5.38</td> <!-- ScaLA-nn -->
   <td class="no qa">31.77 ± 1.55 / 45.47 ± 2.02</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="no ner">90.07 ± 1.08 / 87.56 ± 1.39</td> <!-- NorNE-nb -->
   <td class="no ner">85.65 ± 0.96 / 82.40 ± 1.16</td> <!-- NorNE-nn -->
   <td class="no sent">54.46 ± 1.16 / 68.25 ± 0.76</td> <!-- NoReC -->
   <td class="no la">12.16 ± 5.91 / 50.55 ± 4.73</td> <!-- ScaLA-nb -->
   <td class="no la">8.99 ± 2.25 / 48.57 ± 3.67</td> <!-- ScaLA-nn -->
   <td class="no qa">49.24 ± 1.30 / 64.35 ± 1.24</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="no ner">87.70 ± 0.66 / 85.32 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">81.41 ± 1.46 / 77.41 ± 1.57</td> <!-- NorNE-nn -->
   <td class="no sent">48.34 ± 2.10 / 60.68 ± 3.61</td> <!-- NoReC -->
   <td class="no la">55.30 ± 2.89 / 75.77 ± 1.87</td> <!-- ScaLA-nb -->
   <td class="no la">37.46 ± 2.69 / 67.68 ± 1.66</td> <!-- ScaLA-nn -->
   <td class="no qa">24.49 ± 6.03 / 35.93 ± 8.56</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="no ner">87.99 ± 1.24 / 84.84 ± 1.42</td> <!-- NorNE-nb -->
   <td class="no ner">83.10 ± 1.12 / 79.18 ± 1.45</td> <!-- NorNE-nn -->
   <td class="no sent">36.21 ± 1.82 / 49.48 ± 2.69</td> <!-- NoReC -->
   <td class="no la">46.43 ± 1.81 / 71.65 ± 1.39</td> <!-- ScaLA-nb -->
   <td class="no la">39.82 ± 2.81 / 68.68 ± 1.81</td> <!-- ScaLA-nn -->
   <td class="no qa">40.01 ± 1.58 / 53.12 ± 1.81</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="no ner">82.90 ± 1.44 / 79.06 ± 1.52</td> <!-- NorNE-nb -->
   <td class="no ner">77.33 ± 2.00 / 72.83 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">37.28 ± 2.13 / 48.69 ± 3.26</td> <!-- NoReC -->
   <td class="no la">49.41 ± 1.57 / 73.96 ± 0.87</td> <!-- ScaLA-nb -->
   <td class="no la">43.58 ± 2.23 / 71.20 ± 1.61</td> <!-- ScaLA-nn -->
   <td class="no qa">40.35 ± 2.26 / 54.01 ± 2.42</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="no ner">68.11 ± 1.83 / 57.57 ± 3.10</td> <!-- NorNE-nb -->
   <td class="no ner">68.19 ± 1.01 / 56.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">55.33 ± 1.95 / 69.71 ± 1.56</td> <!-- NoReC -->
   <td class="no la">10.15 ± 3.24 / 36.27 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">7.51 ± 2.97 / 35.89 ± 1.30</td> <!-- ScaLA-nn -->
   <td class="no qa">55.33 ± 3.29 / 80.42 ± 1.68</td> <!-- NorQuAD -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="no ner">66.22 ± 2.15 / 48.98 ± 4.65</td> <!-- NorNE-nb -->
   <td class="no ner">64.14 ± 1.26 / 49.59 ± 4.31</td> <!-- NorNE-nn -->
   <td class="no sent">55.48 ± 1.77 / 69.68 ± 1.45</td> <!-- NoReC -->
   <td class="no la">26.13 ± 1.28 / 56.08 ± 2.05</td> <!-- ScaLA-nb -->
   <td class="no la">17.32 ± 0.77 / 54.57 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="no ner">84.95 ± 0.58 / 81.68 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">79.57 ± 1.49 / 74.62 ± 1.92</td> <!-- NorNE-nn -->
   <td class="no sent">40.15 ± 1.15 / 46.26 ± 0.47</td> <!-- NoReC -->
   <td class="no la">72.87 ± 1.11 / 85.86 ± 0.63</td> <!-- ScaLA-nb -->
   <td class="no la">63.77 ± 1.27 / 81.62 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">14.16 ± 4.55 / 19.70 ± 6.40</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="no ner">88.72 ± 0.76 / 85.49 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">83.08 ± 1.22 / 79.36 ± 1.38</td> <!-- NorNE-nn -->
   <td class="no sent">35.87 ± 1.85 / 48.94 ± 3.37</td> <!-- NoReC -->
   <td class="no la">44.22 ± 3.29 / 70.31 ± 2.86</td> <!-- ScaLA-nb -->
   <td class="no la">39.55 ± 7.01 / 68.65 ± 3.36</td> <!-- ScaLA-nn -->
   <td class="no qa">40.55 ± 2.19 / 53.62 ± 2.68</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="no ner">89.07 ± 1.08 / 85.89 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">82.69 ± 0.90 / 79.22 ± 0.93</td> <!-- NorNE-nn -->
   <td class="no sent">34.97 ± 1.74 / 48.21 ± 2.02</td> <!-- NoReC -->
   <td class="no la">39.58 ± 5.70 / 67.91 ± 3.00</td> <!-- ScaLA-nb -->
   <td class="no la">31.27 ± 9.57 / 62.81 ± 7.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.89 ± 1.64 / 55.17 ± 2.07</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="no ner">88.05 ± 0.85 / 84.88 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">83.08 ± 1.50 / 79.06 ± 1.70</td> <!-- NorNE-nn -->
   <td class="no sent">35.34 ± 1.88 / 48.31 ± 2.28</td> <!-- NoReC -->
   <td class="no la">31.45 ± 12.12 / 63.68 ± 6.21</td> <!-- ScaLA-nb -->
   <td class="no la">36.12 ± 8.59 / 66.98 ± 4.91</td> <!-- ScaLA-nn -->
   <td class="no qa">41.59 ± 2.45 / 54.67 ± 2.65</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no qa">49.03 ± 4.22 / 74.38 ± 3.92</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="no ner">90.14 ± 0.97 / 87.71 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">84.12 ± 1.85 / 80.21 ± 2.19</td> <!-- NorNE-nn -->
   <td class="no sent">44.42 ± 13.10 / 57.73 ± 11.86</td> <!-- NoReC -->
   <td class="no la">11.20 ± 2.99 / 48.77 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">7.12 ± 2.39 / 49.23 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">47.69 ± 1.95 / 62.39 ± 1.74</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="no ner">88.55 ± 0.85 / 85.29 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">83.09 ± 1.06 / 79.27 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">35.16 ± 1.75 / 48.41 ± 2.71</td> <!-- NoReC -->
   <td class="no la">31.82 ± 8.92 / 62.98 ± 6.52</td> <!-- ScaLA-nb -->
   <td class="no la">32.94 ± 5.88 / 64.36 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no qa">39.46 ± 1.70 / 52.33 ± 1.94</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="no ner">91.90 ± 0.62 / 89.48 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.59 ± 1.49 / 82.92 ± 1.66</td> <!-- NorNE-nn -->
   <td class="no sent">30.56 ± 13.68 / 45.96 ± 11.45</td> <!-- NoReC -->
   <td class="no la">9.79 ± 5.13 / 46.75 ± 6.05</td> <!-- ScaLA-nb -->
   <td class="no la">6.36 ± 2.82 / 48.52 ± 4.11</td> <!-- ScaLA-nn -->
   <td class="no qa">60.47 ± 1.01 / 74.70 ± 0.92</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="no ner">61.18 ± 2.76 / 56.36 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">65.16 ± 3.97 / 55.74 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">55.61 ± 4.02 / 68.27 ± 3.49</td> <!-- NoReC -->
   <td class="no la">20.84 ± 5.41 / 49.36 ± 4.98</td> <!-- ScaLA-nb -->
   <td class="no la">9.12 ± 3.51 / 43.06 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no qa">42.92 ± 3.08 / 69.13 ± 2.85</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="no ner">85.99 ± 0.83 / 83.09 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">79.47 ± 1.14 / 75.61 ± 1.34</td> <!-- NorNE-nn -->
   <td class="no sent">39.53 ± 0.99 / 50.90 ± 2.17</td> <!-- NoReC -->
   <td class="no la">27.39 ± 2.48 / 61.03 ± 2.27</td> <!-- ScaLA-nb -->
   <td class="no la">23.56 ± 2.23 / 60.05 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">39.01 ± 1.18 / 51.83 ± 1.58</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no qa">42.42 ± 2.92 / 69.53 ± 3.17</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="no ner">83.32 ± 0.99 / 80.48 ± 0.89</td> <!-- NorNE-nb -->
   <td class="no ner">77.97 ± 1.09 / 74.84 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">38.44 ± 1.67 / 52.60 ± 1.95</td> <!-- NoReC -->
   <td class="no la">37.54 ± 1.13 / 64.46 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">23.10 ± 3.66 / 58.14 ± 3.65</td> <!-- ScaLA-nn -->
   <td class="no qa">39.97 ± 0.84 / 51.67 ± 1.11</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="no ner">87.52 ± 0.63 / 83.86 ± 0.68</td> <!-- NorNE-nb -->
   <td class="no ner">82.66 ± 1.64 / 78.65 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">32.73 ± 1.37 / 46.52 ± 1.86</td> <!-- NoReC -->
   <td class="no la">36.41 ± 8.89 / 65.20 ± 6.41</td> <!-- ScaLA-nb -->
   <td class="no la">30.37 ± 5.50 / 62.12 ± 5.66</td> <!-- ScaLA-nn -->
   <td class="no qa">37.71 ± 1.11 / 49.90 ± 1.47</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="no ner">48.24 ± 3.18 / 42.53 ± 3.52</td> <!-- NorNE-nb -->
   <td class="no ner">61.50 ± 1.54 / 50.90 ± 4.58</td> <!-- NorNE-nn -->
   <td class="no sent">49.40 ± 3.40 / 60.71 ± 3.33</td> <!-- NoReC -->
   <td class="no la">24.12 ± 3.24 / 59.38 ± 2.25</td> <!-- ScaLA-nb -->
   <td class="no la">13.20 ± 3.16 / 54.42 ± 3.04</td> <!-- ScaLA-nn -->
   <td class="no qa">47.93 ± 3.46 / 69.52 ± 3.06</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="no ner">61.41 ± 1.71 / 52.32 ± 2.63</td> <!-- NorNE-nb -->
   <td class="no ner">59.49 ± 1.26 / 49.45 ± 3.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.19 ± 1.64 / 63.36 ± 1.52</td> <!-- NoReC -->
   <td class="no la">15.17 ± 2.64 / 50.25 ± 4.51</td> <!-- ScaLA-nb -->
   <td class="no la">10.78 ± 1.99 / 50.08 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">48.99 ± 2.91 / 73.08 ± 2.26</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="no ner">51.82 ± 4.16 / 44.64 ± 4.66</td> <!-- NorNE-nb -->
   <td class="no ner">62.55 ± 3.84 / 49.66 ± 5.87</td> <!-- NorNE-nn -->
   <td class="no sent">56.37 ± 4.27 / 69.55 ± 4.52</td> <!-- NoReC -->
   <td class="no la">6.04 ± 5.92 / 36.34 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">-0.02 ± 0.04 / 33.47 ± 0.88</td> <!-- ScaLA-nn -->
   <td class="no qa">48.85 ± 4.11 / 70.75 ± 3.73</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.1</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="no ner">54.04 ± 2.86 / 48.50 ± 2.85</td> <!-- NorNE-nb -->
   <td class="no ner">62.21 ± 3.31 / 50.38 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">54.74 ± 3.71 / 67.81 ± 2.80</td> <!-- NoReC -->
   <td class="no la">14.51 ± 1.97 / 40.94 ± 1.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.38 ± 4.69 / 37.62 ± 2.92</td> <!-- ScaLA-nn -->
   <td class="no qa">42.83 ± 3.31 / 69.15 ± 2.50</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="no ner">89.46 ± 1.18 / 86.62 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">79.71 ± 1.02 / 75.64 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">52.91 ± 2.29 / 64.64 ± 3.28</td> <!-- NoReC -->
   <td class="no la">27.55 ± 12.16 / 53.28 ± 8.27</td> <!-- ScaLA-nb -->
   <td class="no la">15.20 ± 9.06 / 51.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">12.36 ± 8.54 / 17.38 ± 11.78</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,391 ± 1,270 / 1,125 ± 360</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="no ner">49.09 ± 2.27 / 37.11 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">51.55 ± 2.46 / 39.66 ± 3.21</td> <!-- NorNE-nn -->
   <td class="no sent">44.22 ± 2.00 / 60.67 ± 1.17</td> <!-- NoReC -->
   <td class="no la">31.41 ± 2.60 / 59.70 ± 4.40</td> <!-- ScaLA-nb -->
   <td class="no la">21.57 ± 2.90 / 55.55 ± 3.92</td> <!-- ScaLA-nn -->
   <td class="no qa">48.08 ± 4.60 / 71.27 ± 3.86</td> <!-- NorQuAD -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="no ner">47.26 ± 3.76 / 40.22 ± 3.43</td> <!-- NorNE-nb -->
   <td class="no ner">59.35 ± 2.82 / 45.26 ± 3.91</td> <!-- NorNE-nn -->
   <td class="no sent">54.93 ± 3.49 / 68.45 ± 2.61</td> <!-- NoReC -->
   <td class="no la">9.00 ± 2.87 / 37.53 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">5.26 ± 3.15 / 39.01 ± 3.54</td> <!-- ScaLA-nn -->
   <td class="no qa">45.95 ± 3.12 / 68.00 ± 3.07</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="no ner">62.43 ± 0.94 / 51.64 ± 2.45</td> <!-- NorNE-nb -->
   <td class="no ner">60.68 ± 0.74 / 48.91 ± 2.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.41 ± 1.46 / 69.49 ± 1.05</td> <!-- NoReC -->
   <td class="no la">-1.16 ± 1.31 / 33.56 ± 0.43</td> <!-- ScaLA-nb -->
   <td class="no la">0.30 ± 0.71 / 34.08 ± 0.32</td> <!-- ScaLA-nn -->
   <td class="no qa">49.15 ± 2.79 / 76.77 ± 1.59</td> <!-- NorQuAD -->
   <td>12.0.0</td> <!-- NorNE-nb version -->
   <td>12.0.0</td> <!-- NorNE-nn version -->
   <td>12.0.0</td> <!-- NoReC version -->
   <td>12.0.0</td> <!-- ScaLA-nb version -->
   <td>12.0.0</td> <!-- ScaLA-nn version -->
   <td>12.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no qa">34.48 ± 2.13 / 65.43 ± 2.07</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="no ner">82.20 ± 1.19 / 79.13 ± 1.26</td> <!-- NorNE-nb -->
   <td class="no ner">76.64 ± 1.10 / 72.90 ± 1.43</td> <!-- NorNE-nn -->
   <td class="no sent">40.20 ± 1.56 / 54.68 ± 2.46</td> <!-- NoReC -->
   <td class="no la">24.45 ± 2.21 / 58.75 ± 1.80</td> <!-- ScaLA-nb -->
   <td class="no la">19.18 ± 3.55 / 57.93 ± 2.05</td> <!-- ScaLA-nn -->
   <td class="no qa">30.69 ± 1.64 / 42.59 ± 1.94</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="no ner">84.03 ± 0.79 / 80.97 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">77.98 ± 1.36 / 74.25 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">39.15 ± 3.29 / 53.00 ± 3.85</td> <!-- NoReC -->
   <td class="no la">21.39 ± 2.73 / 58.08 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 3.43 / 57.00 ± 1.86</td> <!-- ScaLA-nn -->
   <td class="no qa">35.32 ± 1.71 / 47.41 ± 2.25</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">40.64 ± 2.58 / 66.46 ± 2.62</td> <!-- NorQuAD -->
   <td>9.3.0</td> <!-- NorNE-nb version -->
   <td>9.3.0</td> <!-- NorNE-nn version -->
   <td>9.3.0</td> <!-- NoReC version -->
   <td>9.3.0</td> <!-- ScaLA-nb version -->
   <td>9.3.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="no ner">47.61 ± 2.50 / 42.16 ± 2.82</td> <!-- NorNE-nb -->
   <td class="no ner">60.57 ± 2.02 / 48.89 ± 4.48</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 4.10 / 52.31 ± 4.53</td> <!-- NoReC -->
   <td class="no la">23.99 ± 5.54 / 60.60 ± 2.74</td> <!-- ScaLA-nb -->
   <td class="no la">11.60 ± 3.18 / 53.40 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">47.02 ± 3.37 / 69.07 ± 2.64</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no qa">41.43 ± 3.34 / 67.26 ± 2.73</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">39.21 ± 3.48 / 64.09 ± 3.49</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="no ner">52.52 ± 1.85 / 43.46 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.60 ± 3.22 / 45.25 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">48.23 ± 3.31 / 65.51 ± 3.01</td> <!-- NoReC -->
   <td class="no la">8.53 ± 3.72 / 38.61 ± 3.22</td> <!-- ScaLA-nb -->
   <td class="no la">6.65 ± 1.40 / 39.32 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">46.89 ± 3.29 / 70.96 ± 2.84</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="no ner">49.67 ± 3.12 / 43.26 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">61.11 ± 1.93 / 50.15 ± 4.14</td> <!-- NorNE-nn -->
   <td class="no sent">56.07 ± 5.22 / 68.93 ± 4.07</td> <!-- NoReC -->
   <td class="no la">3.81 ± 3.09 / 34.47 ± 1.22</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.98 ± 4.12 / 68.18 ± 3.39</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="no ner">49.69 ± 2.90 / 43.57 ± 2.90</td> <!-- NorNE-nb -->
   <td class="no ner">61.78 ± 2.03 / 49.91 ± 4.24</td> <!-- NorNE-nn -->
   <td class="no sent">55.87 ± 5.21 / 68.97 ± 3.95</td> <!-- NoReC -->
   <td class="no la">2.99 ± 3.04 / 34.16 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.62 ± 4.06 / 68.17 ± 3.48</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="no ner">55.93 ± 2.70 / 50.51 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">63.85 ± 2.45 / 53.11 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">50.41 ± 5.49 / 64.49 ± 4.37</td> <!-- NoReC -->
   <td class="no la">15.74 ± 4.15 / 41.16 ± 2.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.23 ± 4.69 / 34.70 ± 1.39</td> <!-- ScaLA-nn -->
   <td class="no qa">39.81 ± 2.81 / 65.65 ± 2.64</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="no ner">85.91 ± 0.98 / 83.05 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">79.67 ± 1.62 / 76.00 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">38.70 ± 2.53 / 50.88 ± 3.38</td> <!-- NoReC -->
   <td class="no la">39.13 ± 2.97 / 67.97 ± 1.68</td> <!-- ScaLA-nb -->
   <td class="no la">24.13 ± 6.88 / 60.76 ± 3.29</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">46.86 ± 3.27 / 70.86 ± 2.79</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="no ner">50.43 ± 2.27 / 42.19 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">54.20 ± 1.81 / 43.92 ± 2.94</td> <!-- NorNE-nn -->
   <td class="no sent">39.21 ± 5.64 / 56.54 ± 6.43</td> <!-- NoReC -->
   <td class="no la">20.51 ± 4.43 / 52.48 ± 5.96</td> <!-- ScaLA-nb -->
   <td class="no la">11.66 ± 4.10 / 48.13 ± 6.13</td> <!-- ScaLA-nn -->
   <td class="no qa">51.57 ± 3.87 / 73.95 ± 3.51</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="no ner">71.73 ± 15.69 / 68.50 ± 15.04</td> <!-- NorNE-nb -->
   <td class="no ner">79.80 ± 0.72 / 75.76 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">46.74 ± 5.96 / 60.25 ± 6.04</td> <!-- NoReC -->
   <td class="no la">8.02 ± 12.19 / 50.30 ± 7.19</td> <!-- ScaLA-nb -->
   <td class="no la">17.04 ± 13.78 / 56.87 ± 7.06</td> <!-- ScaLA-nn -->
   <td class="no qa">29.26 ± 1.27 / 42.50 ± 1.17</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="no ner">61.90 ± 2.57 / 57.16 ± 2.81</td> <!-- NorNE-nb -->
   <td class="no ner">66.92 ± 2.52 / 57.81 ± 3.54</td> <!-- NorNE-nn -->
   <td class="no sent">48.80 ± 4.56 / 63.38 ± 3.06</td> <!-- NoReC -->
   <td class="no la">19.53 ± 5.49 / 51.96 ± 4.90</td> <!-- ScaLA-nb -->
   <td class="no la">9.83 ± 4.57 / 47.95 ± 2.22</td> <!-- ScaLA-nn -->
   <td class="no qa">30.27 ± 2.28 / 62.04 ± 2.19</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="no ner">58.60 ± 4.42 / 52.72 ± 4.93</td> <!-- NorNE-nb -->
   <td class="no ner">63.15 ± 2.29 / 54.03 ± 4.33</td> <!-- NorNE-nn -->
   <td class="no sent">51.85 ± 3.51 / 64.28 ± 2.54</td> <!-- NoReC -->
   <td class="no la">0.66 ± 1.29 / 33.42 ± 0.80</td> <!-- ScaLA-nb -->
   <td class="no la">0.53 ± 1.05 / 33.42 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">43.22 ± 2.24 / 68.55 ± 2.42</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="no ner">85.33 ± 1.01 / 82.13 ± 1.28</td> <!-- NorNE-nb -->
   <td class="no ner">79.44 ± 1.66 / 75.74 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">38.17 ± 2.21 / 50.44 ± 3.11</td> <!-- NoReC -->
   <td class="no la">39.49 ± 3.36 / 68.13 ± 2.13</td> <!-- ScaLA-nb -->
   <td class="no la">22.17 ± 7.22 / 60.16 ± 3.80</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="no ner">56.18 ± 3.05 / 49.39 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">56.96 ± 1.64 / 48.30 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">50.94 ± 1.41 / 66.55 ± 1.06</td> <!-- NoReC -->
   <td class="no la">8.19 ± 1.95 / 45.17 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">5.55 ± 1.71 / 48.92 ± 2.94</td> <!-- ScaLA-nn -->
   <td class="no qa">41.35 ± 2.33 / 69.72 ± 2.52</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="no ner">89.99 ± 1.32 / 87.51 ± 1.20</td> <!-- NorNE-nb -->
   <td class="no ner">78.60 ± 3.17 / 74.97 ± 3.56</td> <!-- NorNE-nn -->
   <td class="no sent">17.93 ± 14.48 / 34.24 ± 10.14</td> <!-- NoReC -->
   <td class="no la">43.46 ± 17.47 / 66.52 ± 12.26</td> <!-- ScaLA-nb -->
   <td class="no la">10.97 ± 10.84 / 43.47 ± 9.81</td> <!-- ScaLA-nn -->
   <td class="no qa">43.74 ± 2.17 / 59.80 ± 1.86</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="no ner">53.68 ± 2.01 / 49.22 ± 2.67</td> <!-- NorNE-nb -->
   <td class="no ner">61.92 ± 4.06 / 49.03 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.19 / 57.76 ± 2.55</td> <!-- NoReC -->
   <td class="no la">0.91 ± 1.78 / 33.51 ± 0.85</td> <!-- ScaLA-nb -->
   <td class="no la">1.24 ± 1.66 / 33.71 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no qa">47.76 ± 2.93 / 70.99 ± 2.39</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="no ner">84.11 ± 1.13 / 81.19 ± 1.37</td> <!-- NorNE-nb -->
   <td class="no ner">77.82 ± 1.28 / 73.93 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">39.63 ± 1.06 / 49.23 ± 2.13</td> <!-- NoReC -->
   <td class="no la">45.75 ± 3.27 / 71.33 ± 1.67</td> <!-- ScaLA-nb -->
   <td class="no la">33.74 ± 2.91 / 63.89 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 3.79 / 7.65 ± 5.41</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="no ner">48.97 ± 2.42 / 39.15 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">51.52 ± 2.96 / 40.17 ± 3.62</td> <!-- NorNE-nn -->
   <td class="no sent">49.05 ± 2.73 / 63.94 ± 2.42</td> <!-- NoReC -->
   <td class="no la">14.37 ± 2.18 / 47.80 ± 4.36</td> <!-- ScaLA-nb -->
   <td class="no la">9.96 ± 1.34 / 48.97 ± 3.77</td> <!-- ScaLA-nn -->
   <td class="no qa">44.07 ± 3.40 / 68.49 ± 2.97</td> <!-- NorQuAD -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="no ner">51.99 ± 1.85 / 37.40 ± 2.95</td> <!-- NorNE-nb -->
   <td class="no ner">52.74 ± 1.13 / 36.83 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">50.39 ± 1.38 / 66.42 ± 1.20</td> <!-- NoReC -->
   <td class="no la">0.99 ± 1.03 / 33.56 ± 0.25</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 1.30 / 34.04 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">47.95 ± 3.19 / 72.60 ± 2.57</td> <!-- NorQuAD -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="no ner">87.63 ± 0.64 / 84.17 ± 0.81</td> <!-- NorNE-nb -->
   <td class="no ner">80.19 ± 2.00 / 75.70 ± 2.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.92 ± 1.44 / 63.75 ± 1.45</td> <!-- NoReC -->
   <td class="no la">7.93 ± 4.24 / 50.87 ± 2.29</td> <!-- ScaLA-nb -->
   <td class="no la">5.06 ± 0.83 / 51.44 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">22.46 ± 5.97 / 34.67 ± 8.87</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="no ner">84.11 ± 1.00 / 81.35 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">77.22 ± 1.99 / 73.67 ± 2.26</td> <!-- NorNE-nn -->
   <td class="no sent">37.02 ± 1.09 / 47.88 ± 2.50</td> <!-- NoReC -->
   <td class="no la">35.42 ± 12.32 / 66.30 ± 6.78</td> <!-- ScaLA-nb -->
   <td class="no la">6.87 ± 6.85 / 50.70 ± 3.62</td> <!-- ScaLA-nn -->
   <td class="no qa">25.98 ± 2.87 / 36.16 ± 3.35</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="no ner">81.94 ± 0.73 / 78.39 ± 0.86</td> <!-- NorNE-nb -->
   <td class="no ner">75.56 ± 1.01 / 71.27 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">55.53 ± 1.05 / 68.89 ± 1.16</td> <!-- NoReC -->
   <td class="no la">36.01 ± 2.02 / 64.39 ± 1.49</td> <!-- ScaLA-nb -->
   <td class="no la">14.99 ± 8.03 / 54.08 ± 5.71</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="no ner">50.10 ± 2.16 / 41.80 ± 2.77</td> <!-- NorNE-nb -->
   <td class="no ner">54.81 ± 1.88 / 45.95 ± 3.21</td> <!-- NorNE-nn -->
   <td class="no sent">48.64 ± 2.14 / 66.06 ± 1.47</td> <!-- NoReC -->
   <td class="no la">10.31 ± 3.46 / 43.68 ± 5.10</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.48 / 36.52 ± 2.31</td> <!-- ScaLA-nn -->
   <td class="no qa">42.20 ± 3.02 / 65.18 ± 2.86</td> <!-- NorQuAD -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="no ner">83.62 ± 0.75 / 80.61 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">80.69 ± 0.69 / 76.61 ± 0.81</td> <!-- NorNE-nn -->
   <td class="no sent">33.16 ± 2.13 / 46.93 ± 2.66</td> <!-- NoReC -->
   <td class="no la">36.10 ± 2.45 / 66.11 ± 1.85</td> <!-- ScaLA-nb -->
   <td class="no la">30.10 ± 2.50 / 64.29 ± 1.69</td> <!-- ScaLA-nn -->
   <td class="no qa">19.26 ± 1.57 / 30.04 ± 2.13</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="no ner">83.93 ± 0.95 / 81.01 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">79.39 ± 1.03 / 75.07 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">32.32 ± 2.30 / 47.12 ± 2.85</td> <!-- NoReC -->
   <td class="no la">36.15 ± 1.99 / 66.57 ± 1.11</td> <!-- ScaLA-nb -->
   <td class="no la">30.17 ± 1.72 / 63.98 ± 1.36</td> <!-- ScaLA-nn -->
   <td class="no qa">19.71 ± 1.41 / 30.26 ± 1.56</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="no ner">81.26 ± 1.25 / 77.69 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.05 ± 1.72 / 69.84 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">49.93 ± 1.46 / 62.37 ± 2.34</td> <!-- NoReC -->
   <td class="no la">38.26 ± 7.56 / 66.01 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">25.17 ± 5.32 / 61.27 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="no ner">83.59 ± 1.36 / 80.55 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">80.29 ± 1.02 / 76.08 ± 1.06</td> <!-- NorNE-nn -->
   <td class="no sent">33.19 ± 1.75 / 46.63 ± 2.55</td> <!-- NoReC -->
   <td class="no la">32.60 ± 6.93 / 65.19 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">24.97 ± 6.47 / 61.39 ± 3.34</td> <!-- ScaLA-nn -->
   <td class="no qa">19.93 ± 1.76 / 30.69 ± 2.36</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="no ner">83.49 ± 0.83 / 80.32 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">80.23 ± 1.09 / 76.10 ± 1.23</td> <!-- NorNE-nn -->
   <td class="no sent">32.66 ± 1.96 / 46.26 ± 3.19</td> <!-- NoReC -->
   <td class="no la">33.65 ± 6.63 / 65.22 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">29.07 ± 2.20 / 63.35 ± 1.54</td> <!-- ScaLA-nn -->
   <td class="no qa">19.29 ± 1.27 / 29.94 ± 1.81</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="no ner">50.63 ± 2.12 / 44.59 ± 1.80</td> <!-- NorNE-nb -->
   <td class="no ner">52.69 ± 2.30 / 46.51 ± 3.63</td> <!-- NorNE-nn -->
   <td class="no sent">44.05 ± 2.51 / 61.80 ± 2.28</td> <!-- NoReC -->
   <td class="no la">11.60 ± 4.10 / 43.01 ± 5.07</td> <!-- ScaLA-nb -->
   <td class="no la">9.26 ± 1.14 / 46.28 ± 3.60</td> <!-- ScaLA-nn -->
   <td class="no qa">45.23 ± 3.73 / 68.68 ± 3.29</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.1</td> <!-- NoReC version -->
   <td>12.5.1</td> <!-- ScaLA-nb version -->
   <td>12.5.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="no ner">80.08 ± 1.46 / 75.93 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">74.59 ± 1.98 / 70.26 ± 2.24</td> <!-- NorNE-nn -->
   <td class="no sent">52.16 ± 0.99 / 66.79 ± 0.98</td> <!-- NoReC -->
   <td class="no la">36.30 ± 6.44 / 65.52 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">14.21 ± 6.44 / 52.78 ± 5.69</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="no ner">82.84 ± 0.61 / 79.91 ± 0.64</td> <!-- NorNE-nb -->
   <td class="no ner">78.83 ± 1.18 / 74.64 ± 1.40</td> <!-- NorNE-nn -->
   <td class="no sent">30.70 ± 2.63 / 43.77 ± 2.62</td> <!-- NoReC -->
   <td class="no la">34.24 ± 2.30 / 65.60 ± 1.50</td> <!-- ScaLA-nb -->
   <td class="no la">27.20 ± 2.61 / 62.87 ± 1.41</td> <!-- ScaLA-nn -->
   <td class="no qa">16.44 ± 1.76 / 26.22 ± 2.65</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="no ner">83.27 ± 1.20 / 80.29 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">79.59 ± 0.97 / 75.31 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">29.37 ± 2.58 / 44.05 ± 3.33</td> <!-- NoReC -->
   <td class="no la">31.50 ± 6.37 / 64.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">24.06 ± 7.24 / 61.01 ± 3.82</td> <!-- ScaLA-nn -->
   <td class="no qa">18.62 ± 0.81 / 29.69 ± 1.81</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="no ner">85.42 ± 0.61 / 82.31 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">78.92 ± 1.42 / 74.86 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">36.27 ± 1.57 / 50.95 ± 1.70</td> <!-- NoReC -->
   <td class="no la">48.07 ± 5.64 / 72.00 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">29.81 ± 3.52 / 64.03 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no qa">0.44 ± 0.41 / 1.08 ± 0.99</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="no ner">71.69 ± 0.92 / 68.09 ± 0.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.00 ± 1.99 / 56.64 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">38.94 ± 2.59 / 53.58 ± 3.33</td> <!-- NoReC -->
   <td class="no la">30.32 ± 4.68 / 62.42 ± 3.11</td> <!-- ScaLA-nb -->
   <td class="no la">7.99 ± 3.34 / 53.24 ± 1.64</td> <!-- ScaLA-nn -->
   <td class="no qa">24.02 ± 1.35 / 37.28 ± 1.24</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="no ner">45.50 ± 2.71 / 40.02 ± 3.16</td> <!-- NorNE-nb -->
   <td class="no ner">45.96 ± 2.67 / 41.28 ± 2.25</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 3.40 / 62.00 ± 2.71</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">52.19 ± 2.88 / 74.97 ± 2.11</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.2.0</td> <!-- NoReC version -->
   <td>12.3.1</td> <!-- ScaLA-nb version -->
   <td>12.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="no ner">77.98 ± 1.58 / 75.03 ± 1.70</td> <!-- NorNE-nb -->
   <td class="no ner">75.00 ± 1.28 / 71.00 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">33.88 ± 1.40 / 49.21 ± 1.98</td> <!-- NoReC -->
   <td class="no la">24.23 ± 1.83 / 58.89 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">18.18 ± 2.65 / 57.28 ± 1.84</td> <!-- ScaLA-nn -->
   <td class="no qa">20.56 ± 1.82 / 30.08 ± 2.54</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="no ner">58.61 ± 1.58 / 47.74 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">60.40 ± 1.25 / 47.53 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">41.36 ± 3.50 / 58.47 ± 3.79</td> <!-- NoReC -->
   <td class="no la">6.52 ± 2.11 / 38.10 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 2.52 / 42.37 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">38.93 ± 2.43 / 65.76 ± 3.07</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no qa">35.74 ± 2.44 / 64.27 ± 2.42</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.23 ± 3.15 / 63.67 ± 2.98</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="no ner">45.28 ± 3.06 / 41.73 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">46.00 ± 4.26 / 42.96 ± 3.38</td> <!-- NorNE-nn -->
   <td class="no sent">44.95 ± 3.19 / 61.88 ± 2.88</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">32.75 ± 1.68 / 59.21 ± 2.11</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="no ner">83.23 ± 1.19 / 80.34 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">79.16 ± 1.50 / 75.55 ± 1.69</td> <!-- NorNE-nn -->
   <td class="no sent">33.94 ± 3.74 / 47.96 ± 4.12</td> <!-- NoReC -->
   <td class="no la">9.56 ± 5.01 / 52.24 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">4.16 ± 2.97 / 50.07 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">22.84 ± 2.52 / 33.72 ± 3.11</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="no ner">79.50 ± 0.70 / 76.09 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">73.03 ± 1.28 / 68.84 ± 1.39</td> <!-- NorNE-nn -->
   <td class="no sent">32.40 ± 1.48 / 44.59 ± 1.66</td> <!-- NoReC -->
   <td class="no la">41.65 ± 1.95 / 70.35 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">25.53 ± 2.31 / 62.04 ± 1.19</td> <!-- ScaLA-nn -->
   <td class="no qa">5.41 ± 2.79 / 8.15 ± 4.18</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="no ner">68.66 ± 1.05 / 65.08 ± 1.07</td> <!-- NorNE-nb -->
   <td class="no ner">61.77 ± 2.03 / 57.87 ± 2.08</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 1.53 / 51.54 ± 2.45</td> <!-- NoReC -->
   <td class="no la">31.23 ± 6.86 / 63.55 ± 5.48</td> <!-- ScaLA-nb -->
   <td class="no la">5.40 ± 4.63 / 44.64 ± 6.37</td> <!-- ScaLA-nn -->
   <td class="no qa">22.56 ± 0.95 / 34.52 ± 1.15</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="no ner">78.31 ± 1.22 / 74.65 ± 1.36</td> <!-- NorNE-nb -->
   <td class="no ner">72.13 ± 0.90 / 67.28 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">47.53 ± 0.94 / 62.73 ± 1.07</td> <!-- NoReC -->
   <td class="no la">26.92 ± 3.12 / 61.93 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.63 ± 4.00 / 56.24 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="no ner">86.26 ± 0.71 / 83.48 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">80.10 ± 2.44 / 76.17 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">34.17 ± 2.42 / 43.74 ± 2.19</td> <!-- NoReC -->
   <td class="no la">12.11 ± 10.47 / 50.33 ± 7.16</td> <!-- ScaLA-nb -->
   <td class="no la">4.28 ± 4.18 / 45.75 ± 4.32</td> <!-- ScaLA-nn -->
   <td class="no qa">11.74 ± 10.45 / 16.38 ± 14.33</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.28 ± 3.58 / 62.78 ± 3.34</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="no ner">35.98 ± 3.79 / 27.51 ± 2.13</td> <!-- NorNE-nb -->
   <td class="no ner">47.39 ± 2.31 / 36.42 ± 2.87</td> <!-- NorNE-nn -->
   <td class="no sent">38.98 ± 5.51 / 58.23 ± 4.01</td> <!-- NoReC -->
   <td class="no la">11.54 ± 5.04 / 49.91 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">5.20 ± 3.47 / 46.19 ± 5.23</td> <!-- ScaLA-nn -->
   <td class="no qa">37.54 ± 3.00 / 56.56 ± 2.96</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">44.19 ± 4.13 / 66.18 ± 4.05</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="no ner">38.82 ± 5.36 / 30.48 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">43.28 ± 3.13 / 33.87 ± 3.30</td> <!-- NorNE-nn -->
   <td class="no sent">38.05 ± 1.85 / 47.06 ± 3.97</td> <!-- NoReC -->
   <td class="no la">8.45 ± 2.47 / 46.75 ± 3.97</td> <!-- ScaLA-nb -->
   <td class="no la">7.50 ± 1.65 / 48.14 ± 4.65</td> <!-- ScaLA-nn -->
   <td class="no qa">40.47 ± 2.77 / 64.21 ± 2.94</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="no ner">82.98 ± 1.32 / 79.80 ± 1.69</td> <!-- NorNE-nb -->
   <td class="no ner">76.65 ± 1.24 / 72.29 ± 1.44</td> <!-- NorNE-nn -->
   <td class="no sent">30.38 ± 2.29 / 42.84 ± 2.38</td> <!-- NoReC -->
   <td class="no la">21.99 ± 6.74 / 54.54 ± 7.12</td> <!-- ScaLA-nb -->
   <td class="no la">19.06 ± 4.26 / 56.45 ± 5.24</td> <!-- ScaLA-nn -->
   <td class="no qa">9.47 ± 5.36 / 15.24 ± 8.64</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.51 ± 1.27 / 42.18 ± 1.39</td> <!-- NoReC -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no qa">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="no ner">79.25 ± 1.22 / 76.73 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">75.39 ± 1.03 / 71.63 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 3.06 / 51.25 ± 3.01</td> <!-- NoReC -->
   <td class="no la">22.02 ± 5.34 / 57.45 ± 3.59</td> <!-- ScaLA-nb -->
   <td class="no la">19.72 ± 3.67 / 56.70 ± 2.89</td> <!-- ScaLA-nn -->
   <td class="no qa">0.78 ± 0.74 / 1.49 ± 1.32</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.77 ± 2.11 / 61.99 ± 2.34</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="no ner">76.07 ± 1.18 / 72.78 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">70.94 ± 1.19 / 66.73 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">32.49 ± 1.55 / 43.12 ± 0.71</td> <!-- NoReC -->
   <td class="no la">35.43 ± 2.39 / 66.84 ± 1.17</td> <!-- ScaLA-nb -->
   <td class="no la">21.11 ± 1.97 / 60.09 ± 0.93</td> <!-- ScaLA-nn -->
   <td class="no qa">1.84 ± 2.41 / 2.78 ± 3.65</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,572 ± 1,018 / 1,068 ± 331</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="no ner">23.95 ± 1.93 / 21.43 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">26.55 ± 1.50 / 25.06 ± 1.61</td> <!-- NorNE-nn -->
   <td class="no sent">40.89 ± 3.60 / 59.86 ± 3.59</td> <!-- NoReC -->
   <td class="no la">9.45 ± 1.58 / 44.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">8.32 ± 1.89 / 42.30 ± 2.78</td> <!-- ScaLA-nn -->
   <td class="no qa">43.19 ± 1.82 / 67.93 ± 1.55</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="no ner">76.14 ± 2.58 / 72.24 ± 2.54</td> <!-- NorNE-nb -->
   <td class="no ner">72.88 ± 1.50 / 68.61 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 9.23 / 49.08 ± 8.36</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.61 / 49.14 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">-0.08 ± 1.79 / 45.89 ± 3.49</td> <!-- ScaLA-nn -->
   <td class="no qa">23.91 ± 2.24 / 36.47 ± 2.77</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="no ner">73.15 ± 1.21 / 70.05 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">66.34 ± 1.25 / 62.07 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">29.97 ± 0.99 / 42.12 ± 0.47</td> <!-- NoReC -->
   <td class="no la">40.79 ± 2.06 / 69.48 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">25.08 ± 1.86 / 61.74 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">1.93 ± 2.05 / 3.62 ± 3.99</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no qa">44.62 ± 3.31 / 67.57 ± 3.03</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="no ner">44.83 ± 1.58 / 40.11 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 1.65 / 41.63 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.59 / 45.73 ± 2.82</td> <!-- NoReC -->
   <td class="no la">3.57 ± 1.55 / 37.05 ± 2.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.61 ± 2.11 / 37.85 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="no ner">32.12 ± 5.17 / 32.01 ± 2.80</td> <!-- NorNE-nb -->
   <td class="no ner">36.86 ± 3.53 / 35.46 ± 3.07</td> <!-- NorNE-nn -->
   <td class="no sent">36.97 ± 1.94 / 55.08 ± 2.30</td> <!-- NoReC -->
   <td class="no la">5.27 ± 3.31 / 40.91 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">1.40 ± 1.87 / 33.64 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no qa">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="no ner">48.89 ± 3.42 / 35.46 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">51.95 ± 1.59 / 36.45 ± 2.57</td> <!-- NorNE-nn -->
   <td class="no sent">20.54 ± 6.01 / 36.30 ± 6.77</td> <!-- NoReC -->
   <td class="no la">4.39 ± 3.94 / 35.23 ± 2.81</td> <!-- ScaLA-nb -->
   <td class="no la">1.20 ± 1.64 / 34.54 ± 1.31</td> <!-- ScaLA-nn -->
   <td class="no qa">47.16 ± 4.15 / 70.08 ± 3.96</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="no ner">72.62 ± 0.81 / 69.33 ± 0.93</td> <!-- NorNE-nb -->
   <td class="no ner">58.73 ± 1.81 / 55.12 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">40.65 ± 1.63 / 55.20 ± 2.63</td> <!-- NoReC -->
   <td class="no la">29.47 ± 2.30 / 62.25 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">12.95 ± 3.01 / 55.31 ± 1.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.91 ± 0.93 / 2.56 ± 2.15</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="no ner">81.82 ± 0.85 / 78.30 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">75.89 ± 1.11 / 72.08 ± 1.15</td> <!-- NorNE-nn -->
   <td class="no sent">33.42 ± 1.96 / 48.63 ± 3.34</td> <!-- NoReC -->
   <td class="no la">14.99 ± 4.11 / 52.87 ± 4.48</td> <!-- ScaLA-nb -->
   <td class="no la">13.63 ± 4.52 / 53.34 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="no ner">71.85 ± 1.11 / 68.20 ± 1.23</td> <!-- NorNE-nb -->
   <td class="no ner">67.14 ± 1.18 / 62.61 ± 1.22</td> <!-- NorNE-nn -->
   <td class="no sent">29.00 ± 1.28 / 41.72 ± 0.52</td> <!-- NoReC -->
   <td class="no la">33.57 ± 2.58 / 65.22 ± 1.59</td> <!-- ScaLA-nb -->
   <td class="no la">21.79 ± 1.60 / 60.32 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">0.03 ± 0.07 / 0.05 ± 0.10</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="no ner">42.29 ± 4.36 / 31.45 ± 1.88</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 3.44 / 35.99 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">27.05 ± 3.33 / 45.30 ± 3.46</td> <!-- NoReC -->
   <td class="no la">1.63 ± 2.58 / 38.29 ± 4.05</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 40.92 ± 4.00</td> <!-- ScaLA-nn -->
   <td class="no qa">39.18 ± 2.84 / 61.85 ± 3.07</td> <!-- NorQuAD -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="rank">3.33</td> <!-- ScandEval rank -->
   <td class="no ner">68.63 ± 1.64 / 64.83 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">67.70 ± 2.68 / 63.70 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">25.68 ± 2.17 / 41.65 ± 2.77</td> <!-- NoReC -->
   <td class="no la">6.73 ± 5.40 / 48.20 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">3.35 ± 2.61 / 47.52 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">22.57 ± 1.57 / 34.64 ± 1.94</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">42.52 ± 2.05 / 68.98 ± 2.23</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="no ner">33.08 ± 2.22 / 34.51 ± 2.24</td> <!-- NorNE-nb -->
   <td class="no ner">38.28 ± 2.63 / 40.50 ± 2.72</td> <!-- NorNE-nn -->
   <td class="no sent">35.58 ± 2.13 / 44.49 ± 2.52</td> <!-- NoReC -->
   <td class="no la">0.82 ± 1.46 / 34.78 ± 1.54</td> <!-- ScaLA-nb -->
   <td class="no la">1.43 ± 1.70 / 34.19 ± 1.10</td> <!-- ScaLA-nn -->
   <td class="no qa">36.06 ± 1.76 / 58.71 ± 1.63</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="no ner">59.76 ± 3.01 / 55.95 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">51.44 ± 2.28 / 48.14 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">33.41 ± 1.40 / 45.12 ± 1.87</td> <!-- NoReC -->
   <td class="no la">32.87 ± 1.49 / 65.82 ± 0.78</td> <!-- ScaLA-nb -->
   <td class="no la">20.09 ± 1.88 / 59.27 ± 1.08</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="no ner">69.65 ± 1.48 / 66.15 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">66.78 ± 1.28 / 62.75 ± 1.40</td> <!-- NorNE-nn -->
   <td class="no sent">26.33 ± 1.84 / 40.67 ± 0.71</td> <!-- NoReC -->
   <td class="no la">6.62 ± 3.40 / 48.37 ± 4.02</td> <!-- ScaLA-nb -->
   <td class="no la">5.16 ± 3.07 / 45.99 ± 4.76</td> <!-- ScaLA-nn -->
   <td class="no qa">15.75 ± 1.30 / 27.15 ± 1.91</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="no ner">72.74 ± 2.03 / 69.79 ± 2.34</td> <!-- NorNE-nb -->
   <td class="no ner">69.74 ± 1.81 / 65.59 ± 2.06</td> <!-- NorNE-nn -->
   <td class="no sent">29.68 ± 1.91 / 43.64 ± 2.18</td> <!-- NoReC -->
   <td class="no la">15.83 ± 10.06 / 55.51 ± 5.25</td> <!-- ScaLA-nb -->
   <td class="no la">8.70 ± 4.78 / 52.69 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">1.04 ± 1.17 / 1.93 ± 2.12</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="no ner">50.34 ± 3.17 / 45.09 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">52.06 ± 2.41 / 46.88 ± 2.39</td> <!-- NorNE-nn -->
   <td class="no sent">32.19 ± 2.52 / 43.19 ± 4.63</td> <!-- NoReC -->
   <td class="no la">-0.22 ± 0.43 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">20.57 ± 0.64 / 40.19 ± 1.13</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="no ner">65.95 ± 0.72 / 62.62 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">55.29 ± 1.26 / 51.50 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">33.31 ± 2.87 / 48.75 ± 3.38</td> <!-- NoReC -->
   <td class="no la">20.34 ± 4.81 / 58.57 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">8.07 ± 2.44 / 53.43 ± 1.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.14 ± 0.16</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="no ner">39.78 ± 2.67 / 31.15 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">43.58 ± 2.49 / 36.60 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">22.01 ± 3.00 / 40.48 ± 2.81</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.35 / 44.34 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">1.45 ± 1.35 / 39.55 ± 3.53</td> <!-- ScaLA-nn -->
   <td class="no qa">32.42 ± 1.72 / 56.65 ± 0.92</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,480 ± 727 / 822 ± 274</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="no ner">28.87 ± 5.63 / 27.09 ± 4.90</td> <!-- NorNE-nb -->
   <td class="no ner">34.01 ± 5.51 / 30.65 ± 4.07</td> <!-- NorNE-nn -->
   <td class="no sent">27.31 ± 3.11 / 38.30 ± 2.19</td> <!-- NoReC -->
   <td class="no la">1.53 ± 1.06 / 49.09 ± 1.02</td> <!-- ScaLA-nb -->
   <td class="no la">-0.63 ± 1.33 / 45.92 ± 2.34</td> <!-- ScaLA-nn -->
   <td class="no qa">25.53 ± 4.94 / 40.76 ± 7.49</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="no ner">15.53 ± 5.69 / 15.49 ± 5.08</td> <!-- NorNE-nb -->
   <td class="no ner">19.78 ± 4.54 / 18.86 ± 4.22</td> <!-- NorNE-nn -->
   <td class="no sent">32.89 ± 1.65 / 42.58 ± 3.16</td> <!-- NoReC -->
   <td class="no la">1.18 ± 1.00 / 33.34 ± 0.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,807 ± 4,171 / 3,323 ± 1,083</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.66</td> <!-- ScandEval rank -->
   <td class="no ner">27.37 ± 4.07 / 27.94 ± 4.04</td> <!-- NorNE-nb -->
   <td class="no ner">31.22 ± 3.87 / 31.39 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">34.21 ± 1.63 / 47.17 ± 2.76</td> <!-- NoReC -->
   <td class="no la">0.92 ± 1.55 / 40.71 ± 2.58</td> <!-- ScaLA-nb -->
   <td class="no la">1.25 ± 2.30 / 43.49 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">18.52 ± 2.78 / 32.10 ± 4.23</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">34.91 ± 2.65 / 54.30 ± 2.96</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="no ner">24.38 ± 2.13 / 25.79 ± 2.29</td> <!-- NorNE-nb -->
   <td class="no ner">31.28 ± 1.60 / 33.48 ± 1.60</td> <!-- NorNE-nn -->
   <td class="no sent">30.88 ± 2.75 / 46.07 ± 3.07</td> <!-- NoReC -->
   <td class="no la">-0.30 ± 1.46 / 34.93 ± 1.25</td> <!-- ScaLA-nb -->
   <td class="no la">0.45 ± 0.57 / 33.74 ± 1.25</td> <!-- ScaLA-nn -->
   <td class="no qa">23.99 ± 1.59 / 42.69 ± 1.94</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="no ner">22.35 ± 7.84 / 23.89 ± 4.74</td> <!-- NorNE-nb -->
   <td class="no ner">21.98 ± 7.52 / 27.22 ± 4.97</td> <!-- NorNE-nn -->
   <td class="no sent">18.23 ± 9.28 / 38.93 ± 6.44</td> <!-- NoReC -->
   <td class="no la">1.68 ± 1.35 / 39.93 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">2.49 ± 1.88 / 40.26 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">41.80 ± 3.14 / 64.25 ± 3.13</td> <!-- NorQuAD -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,723 ± 1,025 / 1,670 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="no ner">20.17 ± 4.56 / 19.89 ± 3.61</td> <!-- NorNE-nb -->
   <td class="no ner">24.06 ± 6.19 / 22.95 ± 5.53</td> <!-- NorNE-nn -->
   <td class="no sent">33.84 ± 2.91 / 54.38 ± 2.61</td> <!-- NoReC -->
   <td class="no la">1.05 ± 1.41 / 46.50 ± 2.79</td> <!-- ScaLA-nb -->
   <td class="no la">-0.47 ± 2.02 / 45.21 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">22.58 ± 3.26 / 41.07 ± 4.94</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">3.69</td> <!-- ScandEval rank -->
   <td class="no ner">61.55 ± 1.55 / 58.24 ± 1.47</td> <!-- NorNE-nb -->
   <td class="no ner">59.90 ± 1.56 / 56.03 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">24.59 ± 1.57 / 40.34 ± 0.99</td> <!-- NoReC -->
   <td class="no la">3.45 ± 2.10 / 50.80 ± 1.16</td> <!-- ScaLA-nb -->
   <td class="no la">2.72 ± 1.56 / 48.79 ± 1.92</td> <!-- ScaLA-nn -->
   <td class="no qa">3.99 ± 2.02 / 7.49 ± 3.66</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="no ner">23.82 ± 4.25 / 22.08 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">26.04 ± 6.38 / 24.47 ± 3.69</td> <!-- NorNE-nn -->
   <td class="no sent">32.60 ± 1.84 / 47.47 ± 3.33</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.43 / 44.47 ± 2.44</td> <!-- ScaLA-nb -->
   <td class="no la">2.26 ± 2.27 / 45.41 ± 3.25</td> <!-- ScaLA-nn -->
   <td class="no qa">21.33 ± 0.98 / 42.76 ± 1.02</td> <!-- NorQuAD -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="no ner">14.58 ± 6.07 / 15.44 ± 5.52</td> <!-- NorNE-nb -->
   <td class="no ner">21.06 ± 7.77 / 21.99 ± 7.14</td> <!-- NorNE-nn -->
   <td class="no sent">32.02 ± 1.59 / 36.85 ± 2.01</td> <!-- NoReC -->
   <td class="no la">1.49 ± 1.40 / 35.35 ± 1.51</td> <!-- ScaLA-nb -->
   <td class="no la">0.98 ± 1.85 / 35.28 ± 2.43</td> <!-- ScaLA-nn -->
   <td class="no qa">22.87 ± 1.85 / 38.93 ± 2.59</td> <!-- NorQuAD -->
   <td>10.0.0</td> <!-- NorNE-nb version -->
   <td>10.0.0</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>10.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="no ner">49.92 ± 0.61 / 49.17 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">44.37 ± 1.15 / 43.43 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">19.81 ± 2.15 / 40.90 ± 2.60</td> <!-- NoReC -->
   <td class="no la">8.64 ± 3.57 / 53.17 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">3.11 ± 1.16 / 50.44 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">15.89 ± 1.29 / 26.33 ± 2.41</td> <!-- NorQuAD -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">19.10 ± 2.33 / 38.96 ± 2.78</td> <!-- NorQuAD -->
   <td>9.1.2</td> <!-- NorNE-nb version -->
   <td>9.1.2</td> <!-- NorNE-nn version -->
   <td>9.1.2</td> <!-- NoReC version -->
   <td>9.1.2</td> <!-- ScaLA-nb version -->
   <td>9.1.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="no ner">60.76 ± 1.53 / 58.35 ± 1.41</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.19 / 55.90 ± 1.12</td> <!-- NorNE-nn -->
   <td class="no sent">25.98 ± 1.33 / 40.58 ± 0.60</td> <!-- NoReC -->
   <td class="no la">2.65 ± 2.08 / 48.09 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">3.47 ± 1.47 / 48.98 ± 1.75</td> <!-- ScaLA-nn -->
   <td class="no qa">0.20 ± 0.09 / 0.82 ± 0.39</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="no ner">66.97 ± 1.30 / 62.99 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">63.90 ± 2.54 / 59.95 ± 2.51</td> <!-- NorNE-nn -->
   <td class="no sent">18.85 ± 4.01 / 36.76 ± 2.79</td> <!-- NoReC -->
   <td class="no la">5.83 ± 2.36 / 51.59 ± 1.57</td> <!-- ScaLA-nb -->
   <td class="no la">4.02 ± 2.29 / 51.66 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="no ner">42.18 ± 1.03 / 39.53 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">37.39 ± 1.81 / 34.88 ± 1.76</td> <!-- NorNE-nn -->
   <td class="no sent">24.39 ± 1.60 / 40.44 ± 1.78</td> <!-- NoReC -->
   <td class="no la">7.29 ± 2.49 / 49.37 ± 3.58</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 46.00 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="no ner">20.25 ± 6.26 / 20.45 ± 5.54</td> <!-- NorNE-nb -->
   <td class="no ner">28.99 ± 5.03 / 27.50 ± 4.36</td> <!-- NorNE-nn -->
   <td class="no sent">17.44 ± 3.49 / 35.51 ± 4.10</td> <!-- NoReC -->
   <td class="no la">3.20 ± 1.84 / 34.58 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">2.61 ± 1.80 / 34.49 ± 1.46</td> <!-- ScaLA-nn -->
   <td class="no qa">21.50 ± 2.60 / 40.73 ± 3.86</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="no ner">49.30 ± 0.97 / 46.11 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">46.11 ± 2.15 / 43.01 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">23.21 ± 2.32 / 44.26 ± 2.95</td> <!-- NoReC -->
   <td class="no la">2.26 ± 1.47 / 45.07 ± 4.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.66 ± 1.81 / 44.50 ± 3.45</td> <!-- ScaLA-nn -->
   <td class="no qa">0.68 ± 0.32 / 1.50 ± 0.80</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="rank">3.98</td> <!-- ScandEval rank -->
   <td class="no ner">55.55 ± 3.71 / 52.52 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">53.53 ± 3.03 / 50.23 ± 3.00</td> <!-- NorNE-nn -->
   <td class="no sent">12.69 ± 4.51 / 32.23 ± 3.53</td> <!-- NoReC -->
   <td class="no la">2.79 ± 1.16 / 47.71 ± 2.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.66 ± 2.18 / 46.60 ± 2.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.60 ± 0.72</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="no ner">26.99 ± 3.92 / 24.61 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">25.74 ± 3.76 / 24.51 ± 2.96</td> <!-- NorNE-nn -->
   <td class="no sent">19.85 ± 1.97 / 35.75 ± 1.74</td> <!-- NoReC -->
   <td class="no la">1.96 ± 1.33 / 44.22 ± 2.93</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.39 / 39.57 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no qa">16.33 ± 2.17 / 31.16 ± 3.40</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.03</td> <!-- ScandEval rank -->
   <td class="no ner">12.10 ± 5.58 / 12.85 ± 4.80</td> <!-- NorNE-nb -->
   <td class="no ner">13.42 ± 6.02 / 13.82 ± 5.16</td> <!-- NorNE-nn -->
   <td class="no sent">22.82 ± 3.11 / 43.88 ± 3.10</td> <!-- NoReC -->
   <td class="no la">2.70 ± 2.16 / 47.68 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">2.21 ± 1.46 / 42.80 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="no ner">46.11 ± 3.68 / 43.54 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">35.18 ± 4.90 / 33.22 ± 4.64</td> <!-- NorNE-nn -->
   <td class="no sent">19.19 ± 2.87 / 37.36 ± 1.97</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.42 / 50.99 ± 0.83</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 1.04 / 49.39 ± 0.80</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="no ner">34.42 ± 3.22 / 27.79 ± 2.40</td> <!-- NorNE-nb -->
   <td class="no ner">35.17 ± 4.05 / 30.70 ± 3.37</td> <!-- NorNE-nn -->
   <td class="no sent">21.46 ± 5.63 / 38.36 ± 6.18</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.25 / 33.60 ± 0.50</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.58 / 34.69 ± 3.11</td> <!-- ScaLA-nn -->
   <td class="no qa">0.12 ± 0.04 / 9.85 ± 0.17</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.09</td> <!-- ScandEval rank -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.86 ± 1.65 / 50.11 ± 1.80</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no qa">5.84 ± 1.36 / 16.14 ± 2.48</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="no ner">29.52 ± 1.48 / 29.79 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">31.27 ± 1.30 / 31.91 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">11.49 ± 1.38 / 27.12 ± 1.98</td> <!-- NoReC -->
   <td class="no la">0.29 ± 1.58 / 40.21 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">-0.12 ± 1.48 / 39.92 ± 3.90</td> <!-- ScaLA-nn -->
   <td class="no qa">7.80 ± 1.19 / 17.09 ± 2.72</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="no ner">9.06 ± 6.86 / 8.39 ± 6.41</td> <!-- NorNE-nb -->
   <td class="no ner">17.16 ± 6.21 / 16.00 ± 5.94</td> <!-- NorNE-nn -->
   <td class="no sent">25.52 ± 3.72 / 41.44 ± 4.44</td> <!-- NoReC -->
   <td class="no la">0.68 ± 1.54 / 45.09 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">0.17 ± 2.27 / 42.02 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.46 ± 0.07 / 6.96 ± 0.13</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="no ner">31.87 ± 2.26 / 30.31 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">32.47 ± 1.48 / 30.59 ± 1.43</td> <!-- NorNE-nn -->
   <td class="no sent">15.07 ± 1.97 / 35.80 ± 1.15</td> <!-- NoReC -->
   <td class="no la">1.26 ± 1.26 / 48.42 ± 1.75</td> <!-- ScaLA-nb -->
   <td class="no la">0.49 ± 1.58 / 45.93 ± 3.88</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="no ner">34.46 ± 2.01 / 33.09 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">33.41 ± 2.21 / 33.91 ± 2.33</td> <!-- NorNE-nn -->
   <td class="no sent">6.31 ± 3.46 / 20.67 ± 2.69</td> <!-- NoReC -->
   <td class="no la">-1.59 ± 1.08 / 36.27 ± 3.71</td> <!-- ScaLA-nb -->
   <td class="no la">0.61 ± 1.41 / 38.84 ± 5.10</td> <!-- ScaLA-nn -->
   <td class="no qa">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="no ner">27.66 ± 2.00 / 28.61 ± 2.15</td> <!-- NorNE-nb -->
   <td class="no ner">30.88 ± 2.13 / 31.97 ± 2.10</td> <!-- NorNE-nn -->
   <td class="no sent">5.13 ± 3.33 / 20.41 ± 3.12</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">7.55 ± 1.17 / 15.63 ± 2.64</td> <!-- NorQuAD -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.29</td> <!-- ScandEval rank -->
   <td class="no ner">25.49 ± 3.39 / 23.54 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">25.94 ± 1.70 / 24.10 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">12.60 ± 2.97 / 32.27 ± 3.43</td> <!-- NoReC -->
   <td class="no la">0.50 ± 1.27 / 36.93 ± 4.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.83 ± 1.64 / 37.67 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="no ner">30.79 ± 1.95 / 32.18 ± 1.98</td> <!-- NorNE-nb -->
   <td class="no ner">31.12 ± 2.36 / 33.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">9.95 ± 3.92 / 29.01 ± 2.80</td> <!-- NoReC -->
   <td class="no la">-0.95 ± 1.87 / 39.37 ± 3.33</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 1.73 / 42.36 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,561 ± 1,367 / 3,059 ± 386</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="no ner">18.38 ± 2.01 / 17.08 ± 1.97</td> <!-- NorNE-nb -->
   <td class="no ner">12.76 ± 1.29 / 11.65 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">15.29 ± 5.37 / 34.15 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.17 ± 0.84 / 36.29 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.37 ± 0.69 / 35.08 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.34</td> <!-- ScandEval rank -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">20.84 ± 6.06 / 35.78 ± 5.94</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.09 / 34.65 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">0.48 ± 0.66 / 32.86 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">2.43 ± 0.61 / 22.78 ± 2.29</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.45</td> <!-- ScandEval rank -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">20.64 ± 5.63 / 36.75 ± 3.29</td> <!-- NoReC -->
   <td class="no la">-0.99 ± 0.88 / 33.37 ± 0.27</td> <!-- ScaLA-nb -->
   <td class="no la">-0.15 ± 0.72 / 32.83 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.53 ± 0.31 / 22.14 ± 2.25</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no qa">2.32 ± 0.68 / 6.65 ± 1.90</td> <!-- NorQuAD -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">4.70</td> <!-- ScandEval rank -->
   <td class="no ner">3.14 ± 2.12 / 2.91 ± 2.02</td> <!-- NorNE-nb -->
   <td class="no ner">3.00 ± 1.58 / 2.65 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">3.41 ± 2.11 / 14.87 ± 2.38</td> <!-- NoReC -->
   <td class="no la">0.22 ± 0.42 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.27 ± 0.79 / 38.20 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 2.27 ± 0.89</td> <!-- NorQuAD -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.70</td> <!-- ScandEval rank -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.74 ± 0.05</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.27 ± 1.21 / 9.77 ± 0.51</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 32.25 ± 0.29</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.81</td> <!-- ScandEval rank -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 33.45 ± 0.27</td> <!-- NorQuAD -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="no ner">0.29 ± 0.29 / 0.29 ± 0.27</td> <!-- NorNE-nb -->
   <td class="no ner">0.25 ± 0.17 / 0.27 ± 0.21</td> <!-- NorNE-nn -->
   <td class="no sent">-1.43 ± 1.45 / 20.90 ± 4.96</td> <!-- NoReC -->
   <td class="no la">-0.42 ± 1.10 / 35.77 ± 3.09</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.21 / 39.28 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.15 ± 0.55</td> <!-- NorQuAD -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/norwegian-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Norwegian NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-DJDSB&quot; src=&quot;https://datawrapper.dwcdn.net/DJDSB/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
