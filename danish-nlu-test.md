---
layout: leaderboard
title: Danish NLU
---

<center>Last updated: 15/04/2024 15:31:45 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="danish-nlu-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">DANSK</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Angry Tweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on DANSK">DANSK version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Angry Tweets">Angry Tweets version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-da">ScaLA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-da">ScandiQA-da version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">1.33</td> <!-- ScandEval rank -->
   <td class="da ner">74.60 ± 1.94 / 69.95 ± 2.01</td> <!-- DANSK -->
   <td class="da sent">51.42 ± 2.30 / 67.07 ± 1.97</td> <!-- Angry Tweets -->
   <td class="da la">76.11 ± 1.17 / 87.41 ± 0.67</td> <!-- ScaLA-da -->
   <td class="da qa">47.42 ± 1.86 / 53.06 ± 1.68</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.33</td> <!-- ScandEval rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">49.82 ± 1.79 / 60.78 ± 1.18</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="da ner">74.16 ± 1.73 / 70.93 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">51.20 ± 1.67 / 66.62 ± 1.58</td> <!-- Angry Tweets -->
   <td class="da la">73.87 ± 2.13 / 86.61 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">49.34 ± 1.14 / 55.06 ± 1.21</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="da ner">74.99 ± 1.65 / 70.34 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">53.85 ± 1.39 / 68.94 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">75.71 ± 1.95 / 87.29 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">44.85 ± 4.12 / 50.40 ± 4.01</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="da ner">75.30 ± 1.02 / 70.13 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">55.12 ± 1.58 / 69.99 ± 1.09</td> <!-- Angry Tweets -->
   <td class="da la">76.34 ± 2.35 / 87.56 ± 1.48</td> <!-- ScaLA-da -->
   <td class="da qa">45.15 ± 3.33 / 50.82 ± 3.13</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.40</td> <!-- ScandEval rank -->
   <td class="da ner">75.22 ± 1.64 / 71.57 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">49.94 ± 3.25 / 65.66 ± 2.73</td> <!-- Angry Tweets -->
   <td class="da la">72.59 ± 1.38 / 85.58 ± 0.97</td> <!-- ScaLA-da -->
   <td class="da qa">48.97 ± 1.22 / 54.79 ± 1.18</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="rank">1.45</td> <!-- ScandEval rank -->
   <td class="da ner">73.62 ± 1.06 / 68.91 ± 1.04</td> <!-- DANSK -->
   <td class="da sent">48.29 ± 2.60 / 64.67 ± 2.10</td> <!-- Angry Tweets -->
   <td class="da la">71.55 ± 1.81 / 85.17 ± 1.13</td> <!-- ScaLA-da -->
   <td class="da qa">48.59 ± 1.35 / 53.54 ± 1.23</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,343 ± 1,236 / 1,444 ± 456</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
   <td class="da ner">70.38 ± 1.58 / 65.70 ± 1.23</td> <!-- DANSK -->
   <td class="da sent">49.07 ± 1.23 / 65.38 ± 1.16</td> <!-- Angry Tweets -->
   <td class="da la">72.02 ± 2.15 / 85.74 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">45.72 ± 1.86 / 51.32 ± 1.81</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="da ner">72.55 ± 2.08 / 69.31 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">52.86 ± 1.08 / 68.19 ± 1.02</td> <!-- Angry Tweets -->
   <td class="da la">75.20 ± 1.73 / 86.99 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">37.65 ± 0.96 / 43.48 ± 1.14</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="da ner">70.19 ± 3.34 / 66.64 ± 2.68</td> <!-- DANSK -->
   <td class="da sent">50.19 ± 1.82 / 66.32 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">69.72 ± 2.25 / 84.30 ± 1.64</td> <!-- ScaLA-da -->
   <td class="da qa">39.85 ± 8.97 / 44.44 ± 9.99</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
   <td class="da ner">69.50 ± 1.78 / 65.03 ± 1.31</td> <!-- DANSK -->
   <td class="da sent">55.07 ± 1.53 / 69.43 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">57.67 ± 2.56 / 78.48 ± 1.32</td> <!-- ScaLA-da -->
   <td class="da qa">46.71 ± 1.25 / 52.84 ± 1.18</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">837 ± 294 / 126 ± 43</td> <!-- Model inference speed -->
   <td class="rank">1.62</td> <!-- ScandEval rank -->
   <td class="da ner">59.40 ± 1.99 / 43.10 ± 1.97</td> <!-- DANSK -->
   <td class="da sent">51.80 ± 1.29 / 68.17 ± 0.86</td> <!-- Angry Tweets -->
   <td class="da la">54.22 ± 1.49 / 74.13 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">56.55 ± 1.12 / 65.84 ± 0.86</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="da ner">73.28 ± 1.37 / 68.37 ± 1.73</td> <!-- DANSK -->
   <td class="da sent">52.08 ± 1.06 / 67.98 ± 0.77</td> <!-- Angry Tweets -->
   <td class="da la">67.99 ± 2.28 / 83.02 ± 1.44</td> <!-- ScaLA-da -->
   <td class="da qa">32.39 ± 0.87 / 37.27 ± 0.79</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="da ner">72.74 ± 2.58 / 67.15 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">48.33 ± 4.44 / 63.94 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">57.30 ± 14.90 / 76.82 ± 8.67</td> <!-- ScaLA-da -->
   <td class="da qa">43.57 ± 3.28 / 49.29 ± 3.35</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="da ner">71.21 ± 1.46 / 67.27 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">47.55 ± 1.25 / 64.66 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">68.72 ± 1.40 / 83.85 ± 0.85</td> <!-- ScaLA-da -->
   <td class="da qa">38.33 ± 1.25 / 43.90 ± 1.45</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="da ner">59.61 ± 2.65 / 47.73 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">50.54 ± 3.00 / 66.79 ± 1.87</td> <!-- Angry Tweets -->
   <td class="da la">57.57 ± 3.30 / 77.07 ± 1.91</td> <!-- ScaLA-da -->
   <td class="da qa">51.09 ± 1.97 / 59.01 ± 1.20</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="da ner">72.90 ± 2.53 / 67.41 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">43.38 ± 3.20 / 60.05 ± 4.33</td> <!-- Angry Tweets -->
   <td class="da la">67.05 ± 1.41 / 83.18 ± 0.80</td> <!-- ScaLA-da -->
   <td class="da qa">42.15 ± 2.12 / 47.97 ± 1.99</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="da ner">70.36 ± 1.61 / 66.92 ± 1.70</td> <!-- DANSK -->
   <td class="da sent">46.32 ± 1.22 / 64.13 ± 0.85</td> <!-- Angry Tweets -->
   <td class="da la">66.41 ± 1.89 / 82.44 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da qa">36.42 ± 1.11 / 41.53 ± 1.29</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="da ner">72.16 ± 2.09 / 68.01 ± 1.69</td> <!-- DANSK -->
   <td class="da sent">51.70 ± 1.98 / 67.54 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">62.03 ± 11.56 / 80.01 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.95 ± 2.38 / 35.36 ± 1.79</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="da ner">71.34 ± 1.56 / 66.53 ± 1.53</td> <!-- DANSK -->
   <td class="da sent">49.77 ± 0.92 / 66.38 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">64.31 ± 2.24 / 80.70 ± 1.53</td> <!-- ScaLA-da -->
   <td class="da qa">31.86 ± 1.88 / 37.00 ± 1.79</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="da ner">69.17 ± 2.07 / 65.80 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">48.03 ± 0.74 / 65.34 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">55.31 ± 2.29 / 76.29 ± 1.57</td> <!-- ScaLA-da -->
   <td class="da qa">42.34 ± 3.05 / 47.57 ± 3.10</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="da ner">69.65 ± 2.04 / 65.80 ± 1.79</td> <!-- DANSK -->
   <td class="da sent">49.18 ± 1.55 / 65.94 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">65.45 ± 1.97 / 81.55 ± 1.33</td> <!-- ScaLA-da -->
   <td class="da qa">32.40 ± 2.41 / 37.33 ± 2.34</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="rank">1.80</td> <!-- ScandEval rank -->
   <td class="da ner">71.24 ± 1.63 / 66.41 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">46.50 ± 1.57 / 64.31 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">52.92 ± 4.42 / 75.11 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">40.08 ± 1.22 / 45.40 ± 1.14</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">1.80</td> <!-- ScandEval rank -->
   <td class="da ner">69.79 ± 2.03 / 65.20 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.45 / 64.85 ± 1.13</td> <!-- Angry Tweets -->
   <td class="da la">68.28 ± 1.77 / 83.52 ± 1.02</td> <!-- ScaLA-da -->
   <td class="da qa">31.90 ± 2.50 / 37.07 ± 2.36</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="da ner">68.46 ± 2.31 / 64.34 ± 2.02</td> <!-- DANSK -->
   <td class="da sent">50.48 ± 0.68 / 66.71 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">64.34 ± 2.43 / 80.92 ± 1.67</td> <!-- ScaLA-da -->
   <td class="da qa">30.30 ± 1.40 / 35.30 ± 1.16</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="da ner">68.77 ± 2.07 / 64.77 ± 1.86</td> <!-- DANSK -->
   <td class="da sent">49.66 ± 0.99 / 66.21 ± 0.72</td> <!-- Angry Tweets -->
   <td class="da la">60.13 ± 13.57 / 78.92 ± 6.96</td> <!-- ScaLA-da -->
   <td class="da qa">32.60 ± 0.75 / 37.37 ± 0.72</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="da ner">73.26 ± 1.37 / 67.83 ± 1.48</td> <!-- DANSK -->
   <td class="da sent">43.94 ± 1.37 / 61.91 ± 0.97</td> <!-- Angry Tweets -->
   <td class="da la">51.62 ± 15.51 / 73.99 ± 9.26</td> <!-- ScaLA-da -->
   <td class="da qa">40.70 ± 0.86 / 45.68 ± 0.80</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="da ner">51.08 ± 1.60 / 35.83 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">54.69 ± 0.99 / 69.50 ± 0.93</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 1.48 / 62.15 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da qa">56.56 ± 0.76 / 64.32 ± 0.40</td> <!-- ScandiQA-da -->
   <td>12.0.0</td> <!-- DANSK version -->
   <td>12.0.0</td> <!-- Angry Tweets version -->
   <td>12.0.0</td> <!-- ScaLA-da version -->
   <td>12.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">1.93</td> <!-- ScandEval rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da qa">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="da ner">71.81 ± 1.72 / 66.85 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.22 / 64.90 ± 0.81</td> <!-- Angry Tweets -->
   <td class="da la">54.99 ± 11.90 / 75.82 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.92 ± 0.98 / 34.74 ± 0.91</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="da ner">71.90 ± 1.08 / 67.25 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">51.33 ± 1.24 / 67.04 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">44.45 ± 19.17 / 70.51 ± 10.21</td> <!-- ScaLA-da -->
   <td class="da qa">32.51 ± 0.79 / 37.00 ± 0.78</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">56.51 ± 1.80 / 64.01 ± 1.12</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">58.17 ± 1.71 / 63.79 ± 1.42</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="da ner">45.94 ± 3.62 / 35.68 ± 3.35</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 4.52 / 62.28 ± 4.29</td> <!-- Angry Tweets -->
   <td class="da la">28.04 ± 3.83 / 58.31 ± 5.00</td> <!-- ScaLA-da -->
   <td class="da qa">57.65 ± 1.66 / 62.03 ± 1.50</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="da ner">46.06 ± 3.28 / 35.43 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 4.23 / 61.68 ± 4.43</td> <!-- Angry Tweets -->
   <td class="da la">27.68 ± 4.25 / 57.59 ± 5.15</td> <!-- ScaLA-da -->
   <td class="da qa">57.78 ± 1.43 / 62.26 ± 1.36</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da qa">57.26 ± 1.76 / 63.60 ± 1.40</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da qa">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da qa">56.82 ± 1.75 / 62.40 ± 1.40</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="da ner">67.40 ± 1.01 / 62.44 ± 1.32</td> <!-- DANSK -->
   <td class="da sent">41.53 ± 1.91 / 59.82 ± 1.67</td> <!-- Angry Tweets -->
   <td class="da la">41.62 ± 10.78 / 68.99 ± 5.73</td> <!-- ScaLA-da -->
   <td class="da qa">37.30 ± 1.59 / 42.46 ± 1.75</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="da ner">45.61 ± 3.06 / 35.04 ± 2.94</td> <!-- DANSK -->
   <td class="da sent">53.73 ± 3.06 / 67.51 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">17.08 ± 5.36 / 52.62 ± 5.62</td> <!-- ScaLA-da -->
   <td class="da qa">56.67 ± 1.19 / 61.18 ± 1.07</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da qa">56.46 ± 1.48 / 61.69 ± 1.28</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da qa">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da ner">70.10 ± 1.16 / 64.54 ± 1.00</td> <!-- DANSK -->
   <td class="da sent">45.30 ± 2.03 / 63.22 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">51.74 ± 2.53 / 74.31 ± 1.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.01 ± 2.50 / 27.76 ± 2.44</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="da ner">67.89 ± 2.14 / 64.13 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">39.34 ± 2.85 / 58.37 ± 3.66</td> <!-- Angry Tweets -->
   <td class="da la">50.90 ± 1.26 / 74.15 ± 0.81</td> <!-- ScaLA-da -->
   <td class="da qa">34.82 ± 1.33 / 39.58 ± 1.59</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="da ner">45.39 ± 2.46 / 34.45 ± 2.56</td> <!-- DANSK -->
   <td class="da sent">51.95 ± 2.65 / 65.69 ± 2.11</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 6.27 / 45.66 ± 5.58</td> <!-- ScaLA-da -->
   <td class="da qa">58.51 ± 1.35 / 62.73 ± 1.19</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">59.90 ± 0.84 / 65.47 ± 0.43</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 1.98 / 64.33 ± 1.60</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da qa">57.87 ± 2.32 / 64.53 ± 1.73</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da qa">57.96 ± 0.80 / 63.50 ± 0.73</td> <!-- ScandiQA-da -->
   <td>9.3.0</td> <!-- DANSK version -->
   <td>9.3.0</td> <!-- Angry Tweets version -->
   <td>9.3.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da ner">71.42 ± 2.68 / 66.61 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">31.86 ± 8.76 / 47.51 ± 8.94</td> <!-- Angry Tweets -->
   <td class="da la">52.95 ± 11.68 / 73.96 ± 8.89</td> <!-- ScaLA-da -->
   <td class="da qa">34.66 ± 1.64 / 40.58 ± 1.63</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da ner">47.01 ± 2.76 / 36.47 ± 3.27</td> <!-- DANSK -->
   <td class="da sent">50.60 ± 3.33 / 65.49 ± 2.38</td> <!-- Angry Tweets -->
   <td class="da la">13.73 ± 3.33 / 52.15 ± 3.17</td> <!-- ScaLA-da -->
   <td class="da qa">56.35 ± 1.68 / 61.63 ± 1.33</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da ner">63.38 ± 2.39 / 59.20 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">34.78 ± 1.49 / 55.59 ± 0.92</td> <!-- Angry Tweets -->
   <td class="da la">41.08 ± 7.28 / 69.77 ± 3.75</td> <!-- ScaLA-da -->
   <td class="da qa">40.32 ± 0.81 / 44.89 ± 0.76</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da ner">66.71 ± 1.80 / 61.55 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">43.79 ± 1.76 / 62.26 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">45.96 ± 2.91 / 69.62 ± 1.72</td> <!-- ScaLA-da -->
   <td class="da qa">26.29 ± 2.34 / 32.91 ± 2.60</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="da ner">64.28 ± 1.74 / 59.29 ± 1.54</td> <!-- DANSK -->
   <td class="da sent">36.85 ± 3.28 / 56.27 ± 3.98</td> <!-- Angry Tweets -->
   <td class="da la">63.55 ± 1.19 / 81.41 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">24.52 ± 1.11 / 29.88 ± 1.13</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="da ner">46.03 ± 3.93 / 34.23 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">49.59 ± 3.26 / 63.45 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">12.72 ± 3.51 / 46.56 ± 5.33</td> <!-- ScaLA-da -->
   <td class="da qa">57.03 ± 1.13 / 61.58 ± 1.01</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="da ner">63.42 ± 1.89 / 58.69 ± 2.54</td> <!-- DANSK -->
   <td class="da sent">39.91 ± 1.78 / 58.47 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">51.01 ± 10.50 / 74.54 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da qa">25.76 ± 2.11 / 31.49 ± 1.94</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da ner">64.64 ± 1.72 / 59.54 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.38 / 62.33 ± 1.20</td> <!-- Angry Tweets -->
   <td class="da la">47.47 ± 8.03 / 70.55 ± 4.26</td> <!-- ScaLA-da -->
   <td class="da qa">23.14 ± 1.59 / 29.91 ± 1.40</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da ner">46.70 ± 3.49 / 36.30 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 3.90 / 55.98 ± 4.69</td> <!-- Angry Tweets -->
   <td class="da la">8.04 ± 5.32 / 36.02 ± 2.59</td> <!-- ScaLA-da -->
   <td class="da qa">60.05 ± 1.30 / 64.15 ± 1.20</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.1</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da qa">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.1</td> <!-- Angry Tweets version -->
   <td>12.5.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da ner">74.42 ± 1.81 / 69.54 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">37.94 ± 10.08 / 55.77 ± 9.21</td> <!-- Angry Tweets -->
   <td class="da la">15.26 ± 10.94 / 48.92 ± 8.26</td> <!-- ScaLA-da -->
   <td class="da qa">44.25 ± 2.55 / 50.10 ± 2.75</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da ner">62.66 ± 1.84 / 58.60 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">33.91 ± 1.43 / 54.87 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">40.96 ± 4.05 / 69.68 ± 2.12</td> <!-- ScaLA-da -->
   <td class="da qa">39.93 ± 2.55 / 44.63 ± 2.71</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da ner">64.92 ± 2.17 / 60.82 ± 1.86</td> <!-- DANSK -->
   <td class="da sent">33.50 ± 2.57 / 54.63 ± 2.14</td> <!-- Angry Tweets -->
   <td class="da la">46.75 ± 3.43 / 72.71 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">37.09 ± 2.08 / 41.77 ± 2.25</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da qa">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da qa">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">52.78 ± 1.15 / 60.80 ± 0.59</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,419 ± 1,274 / 1,133 ± 363</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da ner">34.79 ± 3.04 / 26.18 ± 1.58</td> <!-- DANSK -->
   <td class="da sent">48.15 ± 1.73 / 63.31 ± 2.08</td> <!-- Angry Tweets -->
   <td class="da la">20.75 ± 5.25 / 47.57 ± 6.14</td> <!-- ScaLA-da -->
   <td class="da qa">57.11 ± 1.16 / 62.80 ± 0.91</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da qa">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 0.73 / 64.76 ± 0.47</td> <!-- ScandiQA-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da ner">58.50 ± 4.21 / 55.82 ± 3.50</td> <!-- DANSK -->
   <td class="da sent">41.02 ± 1.64 / 60.13 ± 1.52</td> <!-- Angry Tweets -->
   <td class="da la">27.10 ± 3.59 / 61.03 ± 2.41</td> <!-- ScaLA-da -->
   <td class="da qa">39.99 ± 1.25 / 45.72 ± 1.27</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da ner">40.60 ± 2.25 / 28.71 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">36.89 ± 2.27 / 43.77 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">26.41 ± 5.40 / 53.03 ± 6.56</td> <!-- ScaLA-da -->
   <td class="da qa">57.81 ± 1.11 / 63.44 ± 0.81</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="da ner">62.57 ± 1.98 / 59.39 ± 2.04</td> <!-- DANSK -->
   <td class="da sent">33.67 ± 1.54 / 54.48 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">35.79 ± 9.58 / 65.87 ± 5.46</td> <!-- ScaLA-da -->
   <td class="da qa">38.77 ± 2.23 / 43.26 ± 2.39</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da ner">44.90 ± 3.15 / 31.91 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">42.61 ± 1.79 / 53.47 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 3.44 / 38.18 ± 4.21</td> <!-- ScaLA-da -->
   <td class="da qa">59.62 ± 1.12 / 64.70 ± 0.75</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da ner">70.36 ± 2.14 / 65.91 ± 2.15</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.46 / 65.49 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">11.87 ± 5.47 / 48.82 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da qa">29.87 ± 3.18 / 35.11 ± 2.73</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">61.17 ± 2.09 / 58.41 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">46.39 ± 1.25 / 63.97 ± 1.08</td> <!-- Angry Tweets -->
   <td class="da la">38.61 ± 1.86 / 67.08 ± 1.08</td> <!-- ScaLA-da -->
   <td class="da qa">19.90 ± 1.09 / 25.77 ± 1.12</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da ner">62.53 ± 2.60 / 58.99 ± 2.88</td> <!-- DANSK -->
   <td class="da sent">32.88 ± 1.24 / 53.56 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">29.01 ± 11.25 / 61.89 ± 6.94</td> <!-- ScaLA-da -->
   <td class="da qa">39.51 ± 1.53 / 44.11 ± 1.58</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da ner">60.18 ± 2.71 / 57.15 ± 2.47</td> <!-- DANSK -->
   <td class="da sent">39.20 ± 1.69 / 59.33 ± 1.23</td> <!-- Angry Tweets -->
   <td class="da la">26.68 ± 3.38 / 59.41 ± 2.16</td> <!-- ScaLA-da -->
   <td class="da qa">39.34 ± 0.84 / 44.87 ± 0.79</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da ner">60.66 ± 1.45 / 56.95 ± 1.66</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 1.17 / 58.16 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.29 ± 5.92 / 63.74 ± 3.44</td> <!-- ScaLA-da -->
   <td class="da qa">37.68 ± 1.06 / 43.21 ± 1.09</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da ner">40.14 ± 2.41 / 28.08 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">39.38 ± 1.56 / 49.16 ± 2.84</td> <!-- Angry Tweets -->
   <td class="da la">21.85 ± 3.24 / 53.75 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">58.07 ± 1.13 / 63.63 ± 0.69</td> <!-- ScandiQA-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da ner">39.12 ± 4.28 / 28.74 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">36.47 ± 4.90 / 50.72 ± 6.21</td> <!-- Angry Tweets -->
   <td class="da la">26.76 ± 4.78 / 57.02 ± 5.13</td> <!-- ScaLA-da -->
   <td class="da qa">58.75 ± 1.19 / 64.41 ± 0.77</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da ner">61.18 ± 1.22 / 57.94 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">49.13 ± 0.82 / 65.84 ± 0.66</td> <!-- Angry Tweets -->
   <td class="da la">29.66 ± 7.69 / 63.05 ± 4.35</td> <!-- ScaLA-da -->
   <td class="da qa">19.99 ± 1.65 / 26.42 ± 1.77</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da ner">43.17 ± 2.78 / 31.37 ± 2.95</td> <!-- DANSK -->
   <td class="da sent">43.40 ± 2.20 / 57.24 ± 3.52</td> <!-- Angry Tweets -->
   <td class="da la">11.08 ± 2.98 / 43.40 ± 4.66</td> <!-- ScaLA-da -->
   <td class="da qa">56.81 ± 0.70 / 63.10 ± 0.35</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da ner">62.76 ± 1.92 / 58.88 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">32.06 ± 1.44 / 52.57 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 11.93 / 63.72 ± 6.84</td> <!-- ScaLA-da -->
   <td class="da qa">37.79 ± 2.37 / 42.36 ± 2.56</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="da ner">63.17 ± 2.79 / 59.45 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">32.38 ± 1.72 / 53.30 ± 1.79</td> <!-- Angry Tweets -->
   <td class="da la">27.93 ± 11.48 / 61.91 ± 6.69</td> <!-- ScaLA-da -->
   <td class="da qa">39.57 ± 1.18 / 44.06 ± 1.25</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da ner">61.98 ± 2.00 / 58.30 ± 2.12</td> <!-- DANSK -->
   <td class="da sent">47.20 ± 1.34 / 64.51 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">40.52 ± 7.38 / 67.99 ± 3.84</td> <!-- ScaLA-da -->
   <td class="da qa">13.53 ± 4.79 / 15.93 ± 5.58</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da ner">68.49 ± 2.09 / 64.72 ± 2.02</td> <!-- DANSK -->
   <td class="da sent">45.60 ± 1.76 / 63.53 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">28.26 ± 11.88 / 55.28 ± 7.93</td> <!-- ScaLA-da -->
   <td class="da qa">14.34 ± 3.95 / 18.60 ± 5.02</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da ner">60.82 ± 2.03 / 57.64 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 0.78 / 55.56 ± 0.68</td> <!-- Angry Tweets -->
   <td class="da la">41.89 ± 9.80 / 70.04 ± 5.10</td> <!-- ScaLA-da -->
   <td class="da qa">26.83 ± 1.26 / 31.55 ± 1.26</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da ner">69.78 ± 1.59 / 65.83 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">46.78 ± 1.57 / 64.46 ± 1.17</td> <!-- Angry Tweets -->
   <td class="da la">11.27 ± 2.21 / 51.47 ± 2.07</td> <!-- ScaLA-da -->
   <td class="da qa">28.28 ± 4.63 / 33.33 ± 4.10</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da ner">65.40 ± 2.02 / 60.53 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">34.43 ± 4.13 / 51.90 ± 6.17</td> <!-- Angry Tweets -->
   <td class="da la">67.27 ± 1.04 / 83.37 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">6.60 ± 2.98 / 7.09 ± 3.29</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da ner">38.39 ± 3.57 / 24.87 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">49.44 ± 1.03 / 66.00 ± 0.88</td> <!-- Angry Tweets -->
   <td class="da la">7.50 ± 2.07 / 47.53 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">51.24 ± 1.09 / 57.72 ± 0.98</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da ner">41.63 ± 2.33 / 28.51 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.52 / 60.64 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">54.25 ± 0.85 / 61.70 ± 0.71</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da ner">60.63 ± 1.32 / 56.90 ± 1.49</td> <!-- DANSK -->
   <td class="da sent">24.38 ± 1.74 / 40.85 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">68.58 ± 1.38 / 84.12 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">21.03 ± 1.09 / 27.53 ± 0.88</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da ner">60.59 ± 1.84 / 57.31 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">29.52 ± 2.89 / 47.81 ± 4.54</td> <!-- Angry Tweets -->
   <td class="da la">57.10 ± 2.02 / 78.14 ± 1.10</td> <!-- ScaLA-da -->
   <td class="da qa">20.16 ± 0.73 / 25.69 ± 0.60</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da ner">63.84 ± 1.73 / 59.85 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">43.90 ± 1.50 / 62.31 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">17.16 ± 13.94 / 56.47 ± 7.34</td> <!-- ScaLA-da -->
   <td class="da qa">26.94 ± 1.16 / 31.50 ± 1.03</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">57.26 ± 0.79 / 63.80 ± 0.52</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da ner">43.90 ± 15.70 / 41.25 ± 14.74</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 5.85 / 62.62 ± 4.55</td> <!-- Angry Tweets -->
   <td class="da la">30.37 ± 17.09 / 63.92 ± 8.38</td> <!-- ScaLA-da -->
   <td class="da qa">28.89 ± 1.91 / 33.71 ± 1.54</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da ner">30.16 ± 4.47 / 25.03 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">48.49 ± 2.41 / 63.06 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">5.52 ± 4.66 / 38.81 ± 4.27</td> <!-- ScaLA-da -->
   <td class="da qa">52.44 ± 1.32 / 57.22 ± 1.44</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="da ner">61.74 ± 1.46 / 58.09 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">33.28 ± 1.65 / 54.37 ± 1.44</td> <!-- Angry Tweets -->
   <td class="da la">33.15 ± 7.14 / 64.69 ± 4.47</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="da ner">61.74 ± 1.46 / 58.09 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">33.31 ± 1.49 / 54.09 ± 1.49</td> <!-- Angry Tweets -->
   <td class="da la">33.35 ± 7.32 / 64.61 ± 4.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="da ner">58.52 ± 1.78 / 55.04 ± 1.60</td> <!-- DANSK -->
   <td class="da sent">42.26 ± 1.13 / 61.41 ± 0.76</td> <!-- Angry Tweets -->
   <td class="da la">34.80 ± 5.89 / 64.51 ± 4.90</td> <!-- ScaLA-da -->
   <td class="da qa">19.60 ± 1.60 / 25.68 ± 1.48</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da ner">57.97 ± 1.64 / 54.71 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">39.40 ± 1.14 / 59.02 ± 0.60</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 1.86 / 59.54 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">31.87 ± 2.77 / 36.99 ± 2.78</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da ner">62.52 ± 1.33 / 57.14 ± 1.29</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 3.16 / 51.40 ± 5.12</td> <!-- Angry Tweets -->
   <td class="da la">65.15 ± 0.81 / 82.32 ± 0.45</td> <!-- ScaLA-da -->
   <td class="da qa">2.51 ± 2.06 / 2.75 ± 2.29</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da ner">66.39 ± 1.42 / 62.24 ± 1.29</td> <!-- DANSK -->
   <td class="da sent">39.36 ± 3.13 / 58.64 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">7.06 ± 6.11 / 49.71 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">33.88 ± 4.27 / 38.42 ± 4.16</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.2.0</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da ner">37.02 ± 5.66 / 27.64 ± 3.92</td> <!-- DANSK -->
   <td class="da sent">40.65 ± 2.10 / 57.47 ± 2.56</td> <!-- Angry Tweets -->
   <td class="da la">7.48 ± 2.51 / 46.56 ± 4.52</td> <!-- ScaLA-da -->
   <td class="da qa">52.71 ± 0.70 / 59.07 ± 0.65</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da qa">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da ner">60.78 ± 1.12 / 55.74 ± 1.15</td> <!-- DANSK -->
   <td class="da sent">39.65 ± 1.31 / 59.23 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">37.67 ± 7.20 / 65.47 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">15.41 ± 3.05 / 22.46 ± 2.81</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="da ner">59.50 ± 1.45 / 56.28 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">31.89 ± 1.59 / 53.99 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">36.00 ± 2.27 / 67.38 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.41 ± 1.26 / 33.19 ± 1.40</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="da ner">63.31 ± 1.75 / 58.18 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">32.72 ± 2.91 / 49.84 ± 4.90</td> <!-- Angry Tweets -->
   <td class="da la">67.74 ± 1.33 / 83.32 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da ner">58.44 ± 2.08 / 55.32 ± 1.81</td> <!-- DANSK -->
   <td class="da sent">31.81 ± 1.65 / 53.25 ± 1.65</td> <!-- Angry Tweets -->
   <td class="da la">34.13 ± 2.81 / 65.98 ± 2.30</td> <!-- ScaLA-da -->
   <td class="da qa">27.60 ± 1.58 / 32.18 ± 1.64</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da ner">58.36 ± 1.69 / 55.30 ± 1.49</td> <!-- DANSK -->
   <td class="da sent">32.13 ± 1.52 / 53.89 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">34.75 ± 1.55 / 65.89 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">27.50 ± 1.21 / 32.16 ± 1.28</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da ner">58.78 ± 1.75 / 55.50 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">31.30 ± 1.80 / 52.43 ± 1.61</td> <!-- Angry Tweets -->
   <td class="da la">34.92 ± 2.74 / 66.69 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">27.86 ± 1.51 / 32.53 ± 1.36</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da ner">58.12 ± 1.30 / 54.97 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">32.53 ± 1.39 / 54.09 ± 1.00</td> <!-- Angry Tweets -->
   <td class="da la">35.53 ± 2.54 / 66.86 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">28.19 ± 1.93 / 32.96 ± 1.90</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da ner">56.75 ± 1.91 / 53.43 ± 1.87</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 1.32 / 63.11 ± 0.83</td> <!-- Angry Tweets -->
   <td class="da la">26.74 ± 1.94 / 62.19 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da qa">17.89 ± 1.00 / 25.53 ± 1.05</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da ner">57.53 ± 1.89 / 54.43 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">32.95 ± 0.82 / 54.57 ± 0.80</td> <!-- Angry Tweets -->
   <td class="da la">33.63 ± 2.63 / 65.69 ± 1.82</td> <!-- ScaLA-da -->
   <td class="da qa">27.21 ± 1.31 / 32.05 ± 1.23</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da ner">37.80 ± 2.75 / 24.74 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">40.51 ± 1.75 / 55.84 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">3.35 ± 1.84 / 44.60 ± 4.67</td> <!-- ScaLA-da -->
   <td class="da qa">49.08 ± 1.74 / 55.58 ± 1.57</td> <!-- ScandiQA-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da qa">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da ner">53.93 ± 1.88 / 52.04 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">36.31 ± 1.60 / 57.37 ± 1.15</td> <!-- Angry Tweets -->
   <td class="da la">23.46 ± 1.17 / 58.91 ± 1.36</td> <!-- ScaLA-da -->
   <td class="da qa">27.85 ± 2.53 / 34.34 ± 2.51</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da ner">55.98 ± 2.24 / 52.41 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">36.66 ± 1.27 / 57.48 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">22.69 ± 5.37 / 59.46 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">24.81 ± 1.85 / 29.08 ± 1.74</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da ner">59.94 ± 2.06 / 58.86 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">39.16 ± 1.75 / 58.91 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.16 ± 1.61 / 48.93 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">24.69 ± 1.58 / 28.57 ± 1.42</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,480 ± 727 / 822 ± 274</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="da ner">28.80 ± 2.60 / 20.50 ± 2.40</td> <!-- DANSK -->
   <td class="da sent">37.20 ± 3.92 / 53.62 ± 4.07</td> <!-- Angry Tweets -->
   <td class="da la">2.94 ± 1.76 / 46.66 ± 3.18</td> <!-- ScaLA-da -->
   <td class="da qa">49.57 ± 1.52 / 54.84 ± 1.68</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="da ner">59.37 ± 1.94 / 57.15 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 0.77 / 58.57 ± 0.67</td> <!-- Angry Tweets -->
   <td class="da la">4.61 ± 2.95 / 49.70 ± 2.34</td> <!-- ScaLA-da -->
   <td class="da qa">23.13 ± 2.72 / 28.47 ± 2.30</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.24 ± 3.46 / 41.07 ± 4.41</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da qa">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da ner">56.36 ± 1.95 / 53.98 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">31.16 ± 2.06 / 52.25 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">21.08 ± 2.54 / 56.96 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">19.63 ± 2.13 / 23.61 ± 2.07</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="da ner">49.22 ± 1.85 / 47.83 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">33.51 ± 1.46 / 54.93 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">12.08 ± 8.71 / 54.24 ± 4.71</td> <!-- ScaLA-da -->
   <td class="da qa">24.49 ± 1.67 / 28.88 ± 1.71</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="da ner">57.84 ± 1.47 / 54.75 ± 1.23</td> <!-- DANSK -->
   <td class="da sent">31.18 ± 0.94 / 53.05 ± 1.16</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 3.71 / 53.61 ± 2.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.73 ± 1.16 / 27.50 ± 1.00</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="da ner">21.98 ± 3.33 / 18.42 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">37.77 ± 3.06 / 55.35 ± 4.51</td> <!-- Angry Tweets -->
   <td class="da la">1.26 ± 1.86 / 34.03 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">46.03 ± 1.44 / 52.54 ± 1.95</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">15.42 ± 1.70 / 21.36 ± 1.94</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">13.97 ± 1.75 / 19.76 ± 2.26</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,723 ± 1,025 / 1,670 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="da ner">16.67 ± 3.76 / 14.91 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">38.36 ± 2.27 / 57.74 ± 2.76</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 1.77 / 37.76 ± 2.76</td> <!-- ScaLA-da -->
   <td class="da qa">47.53 ± 1.25 / 54.08 ± 1.20</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,572 ± 1,018 / 1,068 ± 331</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="da ner">15.94 ± 1.59 / 14.05 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">32.78 ± 4.04 / 47.79 ± 5.25</td> <!-- Angry Tweets -->
   <td class="da la">7.86 ± 1.87 / 41.91 ± 2.25</td> <!-- ScaLA-da -->
   <td class="da qa">52.16 ± 0.84 / 60.27 ± 0.51</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da qa">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da qa">41.82 ± 2.07 / 48.91 ± 2.47</td> <!-- ScandiQA-da -->
   <td>9.1.2</td> <!-- DANSK version -->
   <td>9.1.2</td> <!-- Angry Tweets version -->
   <td>9.1.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="da ner">49.88 ± 2.14 / 46.74 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">27.93 ± 0.66 / 50.86 ± 0.42</td> <!-- Angry Tweets -->
   <td class="da la">5.42 ± 2.85 / 48.29 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">22.93 ± 0.81 / 28.62 ± 0.62</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="da ner">47.61 ± 1.71 / 45.91 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">24.17 ± 1.92 / 43.75 ± 2.75</td> <!-- Angry Tweets -->
   <td class="da la">8.14 ± 3.76 / 51.78 ± 1.81</td> <!-- ScaLA-da -->
   <td class="da qa">25.19 ± 1.29 / 30.51 ± 1.06</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.27</td> <!-- ScandEval rank -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da qa">51.22 ± 0.94 / 57.23 ± 0.68</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="da ner">18.23 ± 5.87 / 14.77 ± 3.36</td> <!-- DANSK -->
   <td class="da sent">22.71 ± 5.21 / 35.11 ± 6.59</td> <!-- Angry Tweets -->
   <td class="da la">5.03 ± 2.51 / 49.00 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da qa">49.11 ± 1.16 / 55.56 ± 1.21</td> <!-- ScandiQA-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="da ner">14.88 ± 3.92 / 14.02 ± 2.63</td> <!-- DANSK -->
   <td class="da sent">34.66 ± 1.82 / 46.40 ± 1.53</td> <!-- Angry Tweets -->
   <td class="da la">0.29 ± 1.86 / 41.01 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da qa">42.16 ± 0.88 / 47.49 ± 0.98</td> <!-- ScandiQA-da -->
   <td>10.0.0</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>10.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="da ner">14.73 ± 1.84 / 14.44 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">27.14 ± 1.93 / 42.34 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">2.65 ± 1.66 / 40.63 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">46.38 ± 0.61 / 54.18 ± 0.52</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da qa">45.34 ± 0.88 / 51.59 ± 0.80</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da ner">11.28 ± 0.96 / 11.02 ± 0.85</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 3.80 / 49.66 ± 3.96</td> <!-- Angry Tweets -->
   <td class="da la">2.08 ± 1.48 / 45.41 ± 3.83</td> <!-- ScaLA-da -->
   <td class="da qa">36.59 ± 1.41 / 42.03 ± 1.44</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da qa">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da ner">46.78 ± 1.50 / 44.41 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">27.78 ± 2.22 / 49.38 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">3.04 ± 1.85 / 46.85 ± 3.03</td> <!-- ScaLA-da -->
   <td class="da qa">15.52 ± 0.98 / 23.22 ± 0.86</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da qa">38.60 ± 0.65 / 47.40 ± 0.64</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da qa">34.79 ± 1.52 / 39.67 ± 1.69</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">3.53</td> <!-- ScandEval rank -->
   <td class="da ner">33.05 ± 1.28 / 31.68 ± 1.05</td> <!-- DANSK -->
   <td class="da sent">30.67 ± 1.28 / 51.76 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">13.01 ± 5.22 / 55.11 ± 3.40</td> <!-- ScaLA-da -->
   <td class="da qa">1.56 ± 0.88 / 5.30 ± 2.21</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="da ner">41.70 ± 1.80 / 38.74 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">26.03 ± 0.90 / 48.46 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.19 ± 1.92 / 49.80 ± 1.39</td> <!-- ScaLA-da -->
   <td class="da qa">13.82 ± 0.82 / 20.76 ± 0.91</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da qa">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">32.12 ± 1.62 / 38.99 ± 1.42</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="da ner">32.63 ± 1.06 / 32.76 ± 1.02</td> <!-- DANSK -->
   <td class="da sent">24.11 ± 1.74 / 44.78 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">2.91 ± 1.07 / 46.98 ± 3.78</td> <!-- ScaLA-da -->
   <td class="da qa">15.37 ± 1.22 / 22.17 ± 1.24</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">3.66</td> <!-- ScandEval rank -->
   <td class="da ner">29.90 ± 7.25 / 28.27 ± 6.86</td> <!-- DANSK -->
   <td class="da sent">19.79 ± 1.67 / 42.09 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">6.15 ± 1.66 / 52.04 ± 1.49</td> <!-- ScaLA-da -->
   <td class="da qa">15.96 ± 2.06 / 21.55 ± 2.17</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da qa">50.51 ± 0.90 / 58.22 ± 0.76</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da ner">36.51 ± 2.44 / 36.31 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">22.07 ± 2.24 / 44.70 ± 3.72</td> <!-- Angry Tweets -->
   <td class="da la">1.63 ± 1.49 / 45.36 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da qa">3.09 ± 1.00 / 9.48 ± 1.61</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da qa">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da qa">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="da ner">22.21 ± 0.75 / 21.70 ± 0.70</td> <!-- DANSK -->
   <td class="da sent">20.33 ± 1.89 / 40.95 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">0.90 ± 1.40 / 48.85 ± 2.60</td> <!-- ScaLA-da -->
   <td class="da qa">2.73 ± 0.64 / 7.23 ± 1.45</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="da ner">16.04 ± 2.47 / 15.60 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">17.37 ± 3.82 / 36.83 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">1.34 ± 0.97 / 35.45 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da qa">1.58 ± 0.51 / 6.64 ± 1.56</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da qa">6.84 ± 6.83 / 21.33 ± 6.27</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="da ner">13.98 ± 1.54 / 13.46 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">6.37 ± 3.38 / 25.43 ± 4.09</td> <!-- Angry Tweets -->
   <td class="da la">0.41 ± 0.80 / 33.31 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">20.46 ± 2.90 / 24.27 ± 3.23</td> <!-- ScandiQA-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da qa">16.64 ± 3.32 / 19.46 ± 3.63</td> <!-- ScandiQA-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,561 ± 1,367 / 3,059 ± 386</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="da ner">12.87 ± 1.63 / 13.23 ± 1.55</td> <!-- DANSK -->
   <td class="da sent">18.61 ± 4.17 / 35.23 ± 3.90</td> <!-- Angry Tweets -->
   <td class="da la">0.30 ± 1.39 / 37.84 ± 3.88</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.43</td> <!-- ScandEval rank -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">5.15 ± 6.60 / 17.35 ± 5.86</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 12.39 ± 1.52</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da ner">1.13 ± 1.19 / 0.97 ± 1.03</td> <!-- DANSK -->
   <td class="da sent">2.06 ± 2.30 / 20.38 ± 2.71</td> <!-- Angry Tweets -->
   <td class="da la">-0.36 ± 0.97 / 41.52 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da qa">0.32 ± 0.12 / 4.20 ± 0.61</td> <!-- ScandiQA-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da qa">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.81 ± 2.69 / 19.31 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 30.05 ± 4.99</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="da ner">0.64 ± 0.89 / 0.52 ± 0.69</td> <!-- DANSK -->
   <td class="da sent">-0.52 ± 1.72 / 28.55 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">-0.02 ± 1.55 / 36.82 ± 2.52</td> <!-- ScaLA-da -->
   <td class="da qa">0.48 ± 0.27 / 2.89 ± 0.53</td> <!-- ScandiQA-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/danish-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Danish NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-K2hEb&quot; src=&quot;https://datawrapper.dwcdn.net/K2hEb/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
