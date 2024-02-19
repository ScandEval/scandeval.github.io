---
layout: leaderboard
title: Mainland Scandinavian NLU
---

<center>Last updated: 19/02/2024 17:44:27 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="mainland-scandinavian-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score">SV</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">DANSK</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Angry Tweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact Match / F1-score">ScandiQA-sv</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1=</td> <!-- Rank -->
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="score">67.78 ± 1.45</td> <!-- ScandEval score -->
   <td class="da-score">60.51 ± 1.71</td> <!-- Danish score -->
   <td class="no-score">74.76 ± 1.38</td> <!-- Norwegian score -->
   <td class="sv-score">68.08 ± 1.26</td> <!-- Swedish score -->
   <td class="da ner">73.62 ± 1.06 / 68.91 ± 1.04</td> <!-- DANSK -->
   <td class="da sent">48.29 ± 2.60 / 64.67 ± 2.10</td> <!-- Angry Tweets -->
   <td class="da la">71.55 ± 1.81 / 85.17 ± 1.13</td> <!-- ScaLA-da -->
   <td class="da qa">48.59 ± 1.35 / 53.54 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">93.12 ± 0.83 / 90.13 ± 1.02</td> <!-- NorNE-nb -->
   <td class="no ner">89.39 ± 0.52 / 86.03 ± 0.65</td> <!-- NorNE-nn -->
   <td class="no sent">64.62 ± 1.36 / 75.40 ± 0.97</td> <!-- NoReC -->
   <td class="no la">77.97 ± 3.04 / 88.19 ± 1.89</td> <!-- ScaLA-nb -->
   <td class="no la">76.30 ± 1.56 / 87.68 ± 0.86</td> <!-- ScaLA-nn -->
   <td class="no qa">66.03 ± 1.19 / 79.64 ± 1.09</td> <!-- NorQuAD -->
   <td class="sv ner">79.01 ± 1.13 / 73.76 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">75.32 ± 1.55 / 69.39 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">69.11 ± 1.50 / 84.32 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.88 ± 0.87 / 54.15 ± 0.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">1=</td> <!-- Rank -->
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,244 ± 510 / 3,515 ± 848</td> <!-- Model inference speed -->
   <td class="score">67.34 ± 2.44</td> <!-- ScandEval score -->
   <td class="da-score">61.57 ± 2.22</td> <!-- Danish score -->
   <td class="no-score">67.09 ± 3.31</td> <!-- Norwegian score -->
   <td class="sv-score">73.37 ± 1.79</td> <!-- Swedish score -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">49.82 ± 1.79 / 60.78 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">49.93 ± 3.13 / 77.72 ± 1.70</td> <!-- NorQuAD -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.50 ± 1.74 / 67.22 ± 1.24</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="score">64.31 ± 3.02</td> <!-- ScandEval score -->
   <td class="da-score">62.39 ± 1.82</td> <!-- Danish score -->
   <td class="no-score">65.49 ± 5.21</td> <!-- Norwegian score -->
   <td class="sv-score">65.05 ± 2.02</td> <!-- Swedish score -->
   <td class="da ner">74.60 ± 1.94 / 69.95 ± 2.01</td> <!-- DANSK -->
   <td class="da sent">51.42 ± 2.30 / 67.07 ± 1.97</td> <!-- Angry Tweets -->
   <td class="da la">76.11 ± 1.17 / 87.41 ± 0.67</td> <!-- ScaLA-da -->
   <td class="da qa">47.42 ± 1.86 / 53.06 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">88.66 ± 1.23 / 84.60 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">84.59 ± 1.98 / 80.07 ± 2.11</td> <!-- NorNE-nn -->
   <td class="no sent">55.59 ± 10.43 / 67.82 ± 9.45</td> <!-- NoReC -->
   <td class="no la">71.43 ± 1.67 / 84.61 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">53.30 ± 13.11 / 74.52 ± 7.96</td> <!-- ScaLA-nn -->
   <td class="no qa">57.38 ± 1.41 / 72.48 ± 1.49</td> <!-- NorQuAD -->
   <td class="sv ner">74.18 ± 2.01 / 68.89 ± 2.46</td> <!-- SUC3 -->
   <td class="sv sent">75.11 ± 1.19 / 74.74 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">64.11 ± 3.27 / 81.63 ± 1.66</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.79 ± 1.61 / 52.40 ± 1.77</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="score">64.24 ± 2.08</td> <!-- ScandEval score -->
   <td class="da-score">62.35 ± 2.28</td> <!-- Danish score -->
   <td class="no-score">66.32 ± 2.50</td> <!-- Norwegian score -->
   <td class="sv-score">64.05 ± 1.47</td> <!-- Swedish score -->
   <td class="da ner">74.99 ± 1.65 / 70.34 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">53.85 ± 1.39 / 68.94 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">75.71 ± 1.95 / 87.29 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">44.85 ± 4.12 / 50.40 ± 4.01</td> <!-- ScandiQA-da -->
   <td class="no ner">86.39 ± 1.06 / 85.20 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">83.22 ± 1.44 / 82.50 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">59.61 ± 1.28 / 71.40 ± 1.68</td> <!-- NoReC -->
   <td class="no la">67.88 ± 7.37 / 82.75 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">62.44 ± 4.39 / 80.43 ± 2.39</td> <!-- ScaLA-nn -->
   <td class="no qa">55.69 ± 1.60 / 70.77 ± 1.64</td> <!-- NorQuAD -->
   <td class="sv ner">71.65 ± 1.55 / 69.08 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">74.92 ± 0.98 / 72.01 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">63.43 ± 2.30 / 81.00 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.20 ± 1.03 / 51.94 ± 0.92</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="score">64.24 ± 2.32</td> <!-- ScandEval score -->
   <td class="da-score">62.98 ± 2.07</td> <!-- Danish score -->
   <td class="no-score">66.24 ± 2.55</td> <!-- Norwegian score -->
   <td class="sv-score">63.52 ± 2.34</td> <!-- Swedish score -->
   <td class="da ner">75.30 ± 1.02 / 70.13 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">55.12 ± 1.58 / 69.99 ± 1.09</td> <!-- Angry Tweets -->
   <td class="da la">76.34 ± 2.35 / 87.56 ± 1.48</td> <!-- ScaLA-da -->
   <td class="da qa">45.15 ± 3.33 / 50.82 ± 3.13</td> <!-- ScandiQA-da -->
   <td class="no ner">86.78 ± 0.95 / 85.37 ± 0.78</td> <!-- NorNE-nb -->
   <td class="no ner">83.28 ± 1.29 / 82.22 ± 1.30</td> <!-- NorNE-nn -->
   <td class="no sent">58.73 ± 2.31 / 70.10 ± 2.66</td> <!-- NoReC -->
   <td class="no la">70.73 ± 3.19 / 84.71 ± 1.82</td> <!-- ScaLA-nb -->
   <td class="no la">59.58 ± 7.22 / 78.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">56.04 ± 1.56 / 71.02 ± 1.42</td> <!-- NorQuAD -->
   <td class="sv ner">71.86 ± 1.73 / 69.05 ± 1.65</td> <!-- SUC3 -->
   <td class="sv sent">74.67 ± 1.43 / 71.15 ± 3.57</td> <!-- SweReC -->
   <td class="sv la">62.77 ± 3.14 / 80.75 ± 1.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.77 ± 3.06 / 50.58 ± 2.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="score">63.70 ± 3.02</td> <!-- ScandEval score -->
   <td class="da-score">57.49 ± 4.10</td> <!-- Danish score -->
   <td class="no-score">65.53 ± 3.54</td> <!-- Norwegian score -->
   <td class="sv-score">68.10 ± 1.44</td> <!-- Swedish score -->
   <td class="da ner">70.19 ± 3.34 / 66.64 ± 2.68</td> <!-- DANSK -->
   <td class="da sent">50.19 ± 1.82 / 66.32 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">69.72 ± 2.25 / 84.30 ± 1.64</td> <!-- ScaLA-da -->
   <td class="da qa">39.85 ± 8.97 / 44.44 ± 9.99</td> <!-- ScandiQA-da -->
   <td class="no ner">88.70 ± 2.05 / 84.95 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.11 ± 1.67 / 82.16 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">54.19 ± 3.15 / 65.18 ± 4.55</td> <!-- NoReC -->
   <td class="no la">69.83 ± 2.01 / 84.72 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">54.84 ± 12.59 / 75.13 ± 9.44</td> <!-- ScaLA-nn -->
   <td class="no qa">58.18 ± 1.84 / 71.29 ± 1.51</td> <!-- NorQuAD -->
   <td class="sv ner">78.23 ± 1.53 / 72.58 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">75.99 ± 1.15 / 71.01 ± 4.17</td> <!-- SweReC -->
   <td class="sv la">72.17 ± 0.94 / 85.94 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.00 ± 2.13 / 51.05 ± 2.40</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score">62.86 ± 1.86</td> <!-- ScandEval score -->
   <td class="da-score">56.37 ± 2.32</td> <!-- Danish score -->
   <td class="no-score">64.44 ± 1.96</td> <!-- Norwegian score -->
   <td class="sv-score">67.78 ± 1.31</td> <!-- Swedish score -->
   <td class="da ner">72.90 ± 2.53 / 67.41 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">43.38 ± 3.20 / 60.05 ± 4.33</td> <!-- Angry Tweets -->
   <td class="da la">67.05 ± 1.41 / 83.18 ± 0.80</td> <!-- ScaLA-da -->
   <td class="da qa">42.15 ± 2.12 / 47.97 ± 1.99</td> <!-- ScandiQA-da -->
   <td class="no ner">91.90 ± 0.54 / 89.55 ± 0.57</td> <!-- NorNE-nb -->
   <td class="no ner">86.81 ± 1.35 / 83.46 ± 1.68</td> <!-- NorNE-nn -->
   <td class="no sent">53.69 ± 4.28 / 63.69 ± 6.95</td> <!-- NoReC -->
   <td class="no la">70.55 ± 1.64 / 84.79 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">61.21 ± 1.20 / 79.87 ± 0.76</td> <!-- ScaLA-nn -->
   <td class="no qa">48.82 ± 1.20 / 63.72 ± 1.06</td> <!-- NorQuAD -->
   <td class="sv ner">78.84 ± 2.19 / 72.86 ± 2.04</td> <!-- SUC3 -->
   <td class="sv sent">75.24 ± 0.99 / 72.06 ± 2.67</td> <!-- SweReC -->
   <td class="sv la">72.30 ± 1.04 / 85.77 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.74 ± 1.04 / 50.62 ± 0.85</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="score">62.70 ± 1.29</td> <!-- ScandEval score -->
   <td class="da-score">56.44 ± 1.40</td> <!-- Danish score -->
   <td class="no-score">66.16 ± 1.20</td> <!-- Norwegian score -->
   <td class="sv-score">65.49 ± 1.27</td> <!-- Swedish score -->
   <td class="da ner">73.28 ± 1.37 / 68.37 ± 1.73</td> <!-- DANSK -->
   <td class="da sent">52.08 ± 1.06 / 67.98 ± 0.77</td> <!-- Angry Tweets -->
   <td class="da la">67.99 ± 2.28 / 83.02 ± 1.44</td> <!-- ScaLA-da -->
   <td class="da qa">32.39 ± 0.87 / 37.27 ± 0.79</td> <!-- ScandiQA-da -->
   <td class="no ner">92.24 ± 0.44 / 89.66 ± 0.60</td> <!-- NorNE-nb -->
   <td class="no ner">87.58 ± 0.68 / 84.23 ± 0.85</td> <!-- NorNE-nn -->
   <td class="no sent">59.98 ± 1.33 / 71.70 ± 1.69</td> <!-- NoReC -->
   <td class="no la">70.18 ± 1.41 / 83.83 ± 0.91</td> <!-- ScaLA-nb -->
   <td class="no la">70.81 ± 1.50 / 84.45 ± 0.95</td> <!-- ScaLA-nn -->
   <td class="no qa">44.27 ± 1.46 / 58.30 ± 1.82</td> <!-- NorQuAD -->
   <td class="sv ner">80.02 ± 1.62 / 74.04 ± 1.75</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 1.60 / 73.41 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">71.92 ± 1.07 / 85.01 ± 0.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.80 ± 0.78 / 38.58 ± 0.70</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="score">62.44 ± 1.91</td> <!-- ScandEval score -->
   <td class="da-score">57.24 ± 1.78</td> <!-- Danish score -->
   <td class="no-score">62.56 ± 2.70</td> <!-- Norwegian score -->
   <td class="sv-score">67.54 ± 1.25</td> <!-- Swedish score -->
   <td class="da ner">69.50 ± 1.78 / 65.03 ± 1.31</td> <!-- DANSK -->
   <td class="da sent">55.07 ± 1.53 / 69.43 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">57.67 ± 2.56 / 78.48 ± 1.32</td> <!-- ScaLA-da -->
   <td class="da qa">46.71 ± 1.25 / 52.84 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">89.86 ± 0.93 / 90.64 ± 0.80</td> <!-- NorNE-nb -->
   <td class="no ner">84.32 ± 1.08 / 86.52 ± 0.94</td> <!-- NorNE-nn -->
   <td class="no sent">61.52 ± 1.87 / 72.72 ± 1.95</td> <!-- NoReC -->
   <td class="no la">62.34 ± 2.48 / 79.94 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">34.88 ± 11.23 / 66.51 ± 5.72</td> <!-- ScaLA-nn -->
   <td class="no qa">53.01 ± 1.05 / 70.46 ± 0.86</td> <!-- NorQuAD -->
   <td class="sv ner">80.36 ± 1.12 / 78.57 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">79.65 ± 1.05 / 78.90 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">63.15 ± 1.65 / 81.06 ± 0.95</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.99 ± 1.18 / 53.49 ± 0.89</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="score">61.93 ± 2.43</td> <!-- ScandEval score -->
   <td class="da-score">53.96 ± 4.50</td> <!-- Danish score -->
   <td class="no-score">66.29 ± 1.56</td> <!-- Norwegian score -->
   <td class="sv-score">65.53 ± 1.24</td> <!-- Swedish score -->
   <td class="da ner">72.16 ± 2.09 / 68.01 ± 1.69</td> <!-- DANSK -->
   <td class="da sent">51.70 ± 1.98 / 67.54 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">62.03 ± 11.56 / 80.01 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.95 ± 2.38 / 35.36 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">92.09 ± 0.51 / 89.67 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">86.85 ± 1.94 / 83.35 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">59.84 ± 1.40 / 72.11 ± 1.25</td> <!-- NoReC -->
   <td class="no la">73.33 ± 2.17 / 85.89 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">71.06 ± 1.62 / 84.78 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">43.67 ± 1.71 / 57.42 ± 1.56</td> <!-- NorQuAD -->
   <td class="sv ner">79.90 ± 1.41 / 73.80 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">76.20 ± 1.16 / 74.01 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">73.62 ± 1.17 / 86.19 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.38 ± 1.23 / 37.12 ± 1.20</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="score">61.40 ± 2.78</td> <!-- ScandEval score -->
   <td class="da-score">52.38 ± 4.78</td> <!-- Danish score -->
   <td class="no-score">69.86 ± 1.93</td> <!-- Norwegian score -->
   <td class="sv-score">61.95 ± 1.64</td> <!-- Swedish score -->
   <td class="da ner">73.26 ± 1.37 / 67.83 ± 1.48</td> <!-- DANSK -->
   <td class="da sent">43.94 ± 1.37 / 61.91 ± 0.97</td> <!-- Angry Tweets -->
   <td class="da la">51.62 ± 15.51 / 73.99 ± 9.26</td> <!-- ScaLA-da -->
   <td class="da qa">40.70 ± 0.86 / 45.68 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="no ner">92.36 ± 0.55 / 89.79 ± 0.73</td> <!-- NorNE-nb -->
   <td class="no ner">88.49 ± 0.97 / 85.45 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">59.73 ± 2.46 / 70.77 ± 3.26</td> <!-- NoReC -->
   <td class="no la">74.40 ± 2.03 / 86.34 ± 1.28</td> <!-- ScaLA-nb -->
   <td class="no la">68.85 ± 3.21 / 83.17 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">57.67 ± 1.86 / 72.51 ± 1.52</td> <!-- NorQuAD -->
   <td class="sv ner">78.21 ± 0.92 / 72.63 ± 0.98</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 1.70 / 70.72 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">56.02 ± 2.92 / 77.31 ± 1.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.52 ± 1.02 / 47.31 ± 0.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="score">61.28 ± 1.42</td> <!-- ScandEval score -->
   <td class="da-score">56.45 ± 1.34</td> <!-- Danish score -->
   <td class="no-score">64.01 ± 1.50</td> <!-- Norwegian score -->
   <td class="sv-score">63.39 ± 1.42</td> <!-- Swedish score -->
   <td class="da ner">71.21 ± 1.46 / 67.27 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">47.55 ± 1.25 / 64.66 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">68.72 ± 1.40 / 83.85 ± 0.85</td> <!-- ScaLA-da -->
   <td class="da qa">38.33 ± 1.25 / 43.90 ± 1.45</td> <!-- ScandiQA-da -->
   <td class="no ner">91.17 ± 0.52 / 91.04 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">87.30 ± 1.07 / 88.83 ± 0.84</td> <!-- NorNE-nn -->
   <td class="no sent">59.10 ± 1.47 / 70.50 ± 2.06</td> <!-- NoReC -->
   <td class="no la">74.32 ± 1.76 / 86.47 ± 1.18</td> <!-- ScaLA-nb -->
   <td class="no la">72.94 ± 1.63 / 86.07 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">34.06 ± 2.05 / 45.46 ± 2.65</td> <!-- NorQuAD -->
   <td class="sv ner">81.35 ± 1.26 / 79.18 ± 1.23</td> <!-- SUC3 -->
   <td class="sv sent">71.16 ± 1.21 / 69.78 ± 3.24</td> <!-- SweReC -->
   <td class="sv la">63.89 ± 1.18 / 81.45 ± 0.75</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.18 ± 2.04 / 42.09 ± 2.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="score">61.23 ± 1.87</td> <!-- ScandEval score -->
   <td class="da-score">54.43 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">63.89 ± 1.92</td> <!-- Norwegian score -->
   <td class="sv-score">65.39 ± 1.74</td> <!-- Swedish score -->
   <td class="da ner">69.79 ± 2.03 / 65.20 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.45 / 64.85 ± 1.13</td> <!-- Angry Tweets -->
   <td class="da la">68.28 ± 1.77 / 83.52 ± 1.02</td> <!-- ScaLA-da -->
   <td class="da qa">31.90 ± 2.50 / 37.07 ± 2.36</td> <!-- ScandiQA-da -->
   <td class="no ner">91.09 ± 0.65 / 88.45 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">85.72 ± 1.92 / 81.88 ± 2.16</td> <!-- NorNE-nn -->
   <td class="no sent">50.90 ± 3.01 / 60.96 ± 5.41</td> <!-- NoReC -->
   <td class="no la">69.34 ± 3.13 / 83.11 ± 2.17</td> <!-- ScaLA-nb -->
   <td class="no la">66.24 ± 2.41 / 82.36 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">48.45 ± 0.63 / 62.96 ± 0.80</td> <!-- NorQuAD -->
   <td class="sv ner">79.08 ± 2.32 / 73.06 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">72.53 ± 0.98 / 67.74 ± 3.02</td> <!-- SweReC -->
   <td class="sv la">73.01 ± 1.43 / 85.98 ± 0.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.92 ± 2.25 / 41.99 ± 2.38</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="score">60.83 ± 1.59</td> <!-- ScandEval score -->
   <td class="da-score">53.71 ± 2.04</td> <!-- Danish score -->
   <td class="no-score">63.11 ± 1.53</td> <!-- Norwegian score -->
   <td class="sv-score">65.66 ± 1.21</td> <!-- Swedish score -->
   <td class="da ner">69.17 ± 2.07 / 65.80 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">48.03 ± 0.74 / 65.34 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">55.31 ± 2.29 / 76.29 ± 1.57</td> <!-- ScaLA-da -->
   <td class="da qa">42.34 ± 3.05 / 47.57 ± 3.10</td> <!-- ScandiQA-da -->
   <td class="no ner">90.08 ± 0.76 / 87.12 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">86.04 ± 0.78 / 81.89 ± 0.98</td> <!-- NorNE-nn -->
   <td class="no sent">56.35 ± 1.25 / 69.31 ± 1.02</td> <!-- NoReC -->
   <td class="no la">59.38 ± 2.52 / 78.02 ± 1.71</td> <!-- ScaLA-nb -->
   <td class="no la">46.54 ± 3.21 / 71.78 ± 2.00</td> <!-- ScaLA-nn -->
   <td class="no qa">55.05 ± 1.24 / 70.46 ± 1.22</td> <!-- NorQuAD -->
   <td class="sv ner">80.05 ± 1.13 / 74.21 ± 1.26</td> <!-- SUC3 -->
   <td class="sv sent">75.09 ± 1.30 / 72.93 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">61.83 ± 1.28 / 79.96 ± 0.82</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.69 ± 1.11 / 51.07 ± 1.04</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="score">60.67 ± 1.59</td> <!-- ScandEval score -->
   <td class="da-score">54.88 ± 1.46</td> <!-- Danish score -->
   <td class="no-score">64.39 ± 1.74</td> <!-- Norwegian score -->
   <td class="sv-score">62.74 ± 1.57</td> <!-- Swedish score -->
   <td class="da ner">70.36 ± 1.61 / 66.92 ± 1.70</td> <!-- DANSK -->
   <td class="da sent">46.32 ± 1.22 / 64.13 ± 0.85</td> <!-- Angry Tweets -->
   <td class="da la">66.41 ± 1.89 / 82.44 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da qa">36.42 ± 1.11 / 41.53 ± 1.29</td> <!-- ScandiQA-da -->
   <td class="no ner">93.01 ± 0.68 / 89.36 ± 0.86</td> <!-- NorNE-nb -->
   <td class="no ner">88.43 ± 0.78 / 84.38 ± 0.81</td> <!-- NorNE-nn -->
   <td class="no sent">60.84 ± 1.48 / 72.16 ± 1.38</td> <!-- NoReC -->
   <td class="no la">73.89 ± 1.31 / 86.19 ± 0.93</td> <!-- ScaLA-nb -->
   <td class="no la">72.10 ± 2.07 / 85.37 ± 1.33</td> <!-- ScaLA-nn -->
   <td class="no qa">33.01 ± 3.06 / 45.28 ± 3.64</td> <!-- NorQuAD -->
   <td class="sv ner">80.38 ± 0.99 / 75.35 ± 0.88</td> <!-- SUC3 -->
   <td class="sv sent">71.21 ± 1.11 / 67.49 ± 2.90</td> <!-- SweReC -->
   <td class="sv la">64.03 ± 1.94 / 81.39 ± 1.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.33 ± 2.25 / 39.61 ± 2.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="score">60.15 ± 1.81</td> <!-- ScandEval score -->
   <td class="da-score">54.17 ± 1.99</td> <!-- Danish score -->
   <td class="no-score">62.60 ± 2.07</td> <!-- Norwegian score -->
   <td class="sv-score">63.69 ± 1.37</td> <!-- Swedish score -->
   <td class="da ner">69.65 ± 2.04 / 65.80 ± 1.79</td> <!-- DANSK -->
   <td class="da sent">49.18 ± 1.55 / 65.94 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">65.45 ± 1.97 / 81.55 ± 1.33</td> <!-- ScaLA-da -->
   <td class="da qa">32.40 ± 2.41 / 37.33 ± 2.34</td> <!-- ScandiQA-da -->
   <td class="no ner">90.65 ± 0.66 / 88.03 ± 0.77</td> <!-- NorNE-nb -->
   <td class="no ner">84.88 ± 1.55 / 81.01 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">52.44 ± 2.90 / 62.48 ± 4.62</td> <!-- NoReC -->
   <td class="no la">68.77 ± 2.01 / 83.10 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">65.40 ± 2.43 / 81.72 ± 1.68</td> <!-- ScaLA-nn -->
   <td class="no qa">43.13 ± 2.05 / 56.76 ± 2.21</td> <!-- NorQuAD -->
   <td class="sv ner">78.58 ± 1.52 / 72.45 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">73.41 ± 0.98 / 68.72 ± 3.80</td> <!-- SweReC -->
   <td class="sv la">71.14 ± 1.62 / 84.55 ± 0.97</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.62 ± 1.35 / 36.20 ± 1.16</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="score">60.14 ± 7.12</td> <!-- ScandEval score -->
   <td class="da-score">55.48 ± 6.30</td> <!-- Danish score -->
   <td class="no-score">61.61 ± 8.86</td> <!-- Norwegian score -->
   <td class="sv-score">63.33 ± 6.20</td> <!-- Swedish score -->
   <td class="da ner">72.74 ± 2.58 / 67.15 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">48.33 ± 4.44 / 63.94 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">57.30 ± 14.90 / 76.82 ± 8.67</td> <!-- ScaLA-da -->
   <td class="da qa">43.57 ± 3.28 / 49.29 ± 3.35</td> <!-- ScandiQA-da -->
   <td class="no ner">91.66 ± 1.24 / 89.34 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">86.19 ± 0.97 / 82.86 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">50.25 ± 15.36 / 63.55 ± 13.05</td> <!-- NoReC -->
   <td class="no la">55.51 ± 18.28 / 74.00 ± 13.38</td> <!-- ScaLA-nb -->
   <td class="no la">43.89 ± 14.81 / 68.88 ± 10.32</td> <!-- ScaLA-nn -->
   <td class="no qa">57.57 ± 2.43 / 72.69 ± 2.22</td> <!-- NorQuAD -->
   <td class="sv ner">80.33 ± 2.50 / 75.03 ± 3.79</td> <!-- SUC3 -->
   <td class="sv sent">76.63 ± 0.98 / 74.25 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">49.72 ± 19.88 / 69.94 ± 13.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.64 ± 1.42 / 52.21 ± 1.45</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="score">59.95 ± 1.70</td> <!-- ScandEval score -->
   <td class="da-score">54.32 ± 1.65</td> <!-- Danish score -->
   <td class="no-score">63.08 ± 1.68</td> <!-- Norwegian score -->
   <td class="sv-score">62.45 ± 1.76</td> <!-- Swedish score -->
   <td class="da ner">71.34 ± 1.56 / 66.53 ± 1.53</td> <!-- DANSK -->
   <td class="da sent">49.77 ± 0.92 / 66.38 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">64.31 ± 2.24 / 80.70 ± 1.53</td> <!-- ScaLA-da -->
   <td class="da qa">31.86 ± 1.88 / 37.00 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">91.16 ± 0.71 / 88.71 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">84.75 ± 1.23 / 80.56 ± 1.59</td> <!-- NorNE-nn -->
   <td class="no sent">55.25 ± 2.36 / 66.95 ± 2.79</td> <!-- NoReC -->
   <td class="no la">68.03 ± 2.37 / 82.12 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">66.90 ± 2.07 / 82.33 ± 1.34</td> <!-- ScaLA-nn -->
   <td class="no qa">41.65 ± 1.17 / 55.71 ± 1.73</td> <!-- NorQuAD -->
   <td class="sv ner">74.48 ± 2.35 / 67.89 ± 2.16</td> <!-- SUC3 -->
   <td class="sv sent">74.58 ± 1.29 / 70.97 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">69.07 ± 2.22 / 83.17 ± 1.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.66 ± 1.18 / 37.05 ± 1.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="score">58.93 ± 1.80</td> <!-- ScandEval score -->
   <td class="da-score">52.69 ± 2.21</td> <!-- Danish score -->
   <td class="no-score">60.74 ± 1.40</td> <!-- Norwegian score -->
   <td class="sv-score">63.36 ± 1.78</td> <!-- Swedish score -->
   <td class="da ner">71.24 ± 1.63 / 66.41 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">46.50 ± 1.57 / 64.31 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">52.92 ± 4.42 / 75.11 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">40.08 ± 1.22 / 45.40 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">90.58 ± 0.91 / 87.84 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">85.21 ± 1.05 / 81.57 ± 1.30</td> <!-- NorNE-nn -->
   <td class="no sent">54.26 ± 1.75 / 67.25 ± 1.47</td> <!-- NoReC -->
   <td class="no la">59.44 ± 1.47 / 78.80 ± 1.00</td> <!-- ScaLA-nb -->
   <td class="no la">49.30 ± 1.39 / 74.02 ± 1.04</td> <!-- ScaLA-nn -->
   <td class="no qa">46.42 ± 1.44 / 61.82 ± 1.47</td> <!-- NorQuAD -->
   <td class="sv ner">77.78 ± 1.69 / 72.08 ± 1.81</td> <!-- SUC3 -->
   <td class="sv sent">73.58 ± 1.37 / 70.43 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">60.36 ± 2.98 / 79.72 ± 1.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.71 ± 1.08 / 47.07 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">58.75 ± 2.79</td> <!-- ScandEval score -->
   <td class="da-score">54.70 ± 2.73</td> <!-- Danish score -->
   <td class="no-score">56.17 ± 2.80</td> <!-- Norwegian score -->
   <td class="sv-score">65.37 ± 2.83</td> <!-- Swedish score -->
   <td class="da ner">59.61 ± 2.65 / 47.73 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">50.54 ± 3.00 / 66.79 ± 1.87</td> <!-- Angry Tweets -->
   <td class="da la">57.57 ± 3.30 / 77.07 ± 1.91</td> <!-- ScaLA-da -->
   <td class="da qa">51.09 ± 1.97 / 59.01 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">46.44 ± 1.55 / 72.64 ± 1.26</td> <!-- NorQuAD -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.59 ± 2.08 / 65.53 ± 1.76</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="score">58.74 ± 4.03</td> <!-- ScandEval score -->
   <td class="da-score">52.79 ± 4.34</td> <!-- Danish score -->
   <td class="no-score">63.83 ± 2.04</td> <!-- Norwegian score -->
   <td class="sv-score">59.59 ± 5.71</td> <!-- Swedish score -->
   <td class="da ner">68.77 ± 2.07 / 64.77 ± 1.86</td> <!-- DANSK -->
   <td class="da sent">49.66 ± 0.99 / 66.21 ± 0.72</td> <!-- Angry Tweets -->
   <td class="da la">60.13 ± 13.57 / 78.92 ± 6.96</td> <!-- ScaLA-da -->
   <td class="da qa">32.60 ± 0.75 / 37.37 ± 0.72</td> <!-- ScandiQA-da -->
   <td class="no ner">88.99 ± 0.96 / 86.13 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">82.99 ± 1.53 / 78.66 ± 1.85</td> <!-- NorNE-nn -->
   <td class="no sent">57.37 ± 1.31 / 70.45 ± 1.13</td> <!-- NoReC -->
   <td class="no la">69.92 ± 2.01 / 83.51 ± 1.33</td> <!-- ScaLA-nb -->
   <td class="no la">70.05 ± 1.76 / 84.13 ± 1.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.98 ± 3.70 / 55.88 ± 3.70</td> <!-- NorQuAD -->
   <td class="sv ner">73.44 ± 2.81 / 67.31 ± 3.11</td> <!-- SUC3 -->
   <td class="sv sent">73.63 ± 1.53 / 68.42 ± 4.24</td> <!-- SweReC -->
   <td class="sv la">58.91 ± 17.49 / 77.13 ± 10.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.39 ± 1.02 / 37.33 ± 0.86</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="score">58.74 ± 1.66</td> <!-- ScandEval score -->
   <td class="da-score">53.40 ± 1.71</td> <!-- Danish score -->
   <td class="no-score">60.50 ± 1.84</td> <!-- Norwegian score -->
   <td class="sv-score">62.34 ± 1.43</td> <!-- Swedish score -->
   <td class="da ner">68.46 ± 2.31 / 64.34 ± 2.02</td> <!-- DANSK -->
   <td class="da sent">50.48 ± 0.68 / 66.71 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">64.34 ± 2.43 / 80.92 ± 1.67</td> <!-- ScaLA-da -->
   <td class="da qa">30.30 ± 1.40 / 35.30 ± 1.16</td> <!-- ScandiQA-da -->
   <td class="no ner">89.07 ± 1.19 / 85.81 ± 1.57</td> <!-- NorNE-nb -->
   <td class="no ner">83.27 ± 1.68 / 78.80 ± 2.22</td> <!-- NorNE-nn -->
   <td class="no sent">53.23 ± 1.67 / 65.23 ± 2.65</td> <!-- NoReC -->
   <td class="no la">70.06 ± 2.33 / 83.61 ± 1.61</td> <!-- ScaLA-nb -->
   <td class="no la">66.81 ± 1.83 / 82.19 ± 1.20</td> <!-- ScaLA-nn -->
   <td class="no qa">34.17 ± 2.16 / 47.61 ± 2.55</td> <!-- NorQuAD -->
   <td class="sv ner">72.25 ± 2.16 / 65.94 ± 2.04</td> <!-- SUC3 -->
   <td class="sv sent">75.04 ± 1.08 / 72.35 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">70.16 ± 1.47 / 84.29 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.89 ± 0.99 / 36.93 ± 0.90</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">58.47 ± 1.54</td> <!-- ScandEval score -->
   <td class="da-score">55.49 ± 1.47</td> <!-- Danish score -->
   <td class="no-score">54.81 ± 1.49</td> <!-- Norwegian score -->
   <td class="sv-score">65.09 ± 1.67</td> <!-- Swedish score -->
   <td class="da ner">59.40 ± 1.99 / 43.10 ± 1.97</td> <!-- DANSK -->
   <td class="da sent">51.80 ± 1.29 / 68.17 ± 0.86</td> <!-- Angry Tweets -->
   <td class="da la">54.22 ± 1.49 / 74.13 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">56.55 ± 1.12 / 65.84 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">74.92 ± 1.24 / 64.00 ± 2.37</td> <!-- NorNE-nb -->
   <td class="no ner">75.34 ± 1.15 / 68.02 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">57.64 ± 1.33 / 71.34 ± 1.15</td> <!-- NoReC -->
   <td class="no la">49.93 ± 1.78 / 69.26 ± 1.76</td> <!-- ScaLA-nb -->
   <td class="no la">34.22 ± 2.98 / 57.61 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 1.06 / 71.71 ± 0.83</td> <!-- NorQuAD -->
   <td class="sv ner">71.43 ± 1.58 / 58.93 ± 3.29</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 1.54 / 76.51 ± 1.63</td> <!-- SweReC -->
   <td class="sv la">55.99 ± 2.64 / 75.08 ± 2.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.46 ± 0.90 / 64.95 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="score">57.64 ± 4.86</td> <!-- ScandEval score -->
   <td class="da-score">50.05 ± 5.57</td> <!-- Danish score -->
   <td class="no-score">62.81 ± 4.09</td> <!-- Norwegian score -->
   <td class="sv-score">60.06 ± 4.91</td> <!-- Swedish score -->
   <td class="da ner">71.90 ± 1.08 / 67.25 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">51.33 ± 1.24 / 67.04 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">44.45 ± 19.17 / 70.51 ± 10.21</td> <!-- ScaLA-da -->
   <td class="da qa">32.51 ± 0.79 / 37.00 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="no ner">91.66 ± 0.74 / 89.26 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">87.74 ± 0.77 / 84.51 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">57.43 ± 1.55 / 70.43 ± 1.41</td> <!-- NoReC -->
   <td class="no la">63.31 ± 11.58 / 80.18 ± 5.59</td> <!-- ScaLA-nb -->
   <td class="no la">62.79 ± 11.35 / 79.65 ± 6.48</td> <!-- ScaLA-nn -->
   <td class="no qa">41.05 ± 2.59 / 54.44 ± 3.33</td> <!-- NorQuAD -->
   <td class="sv ner">79.75 ± 0.94 / 73.45 ± 0.86</td> <!-- SUC3 -->
   <td class="sv sent">74.73 ± 1.15 / 70.83 ± 3.72</td> <!-- SweReC -->
   <td class="sv la">53.55 ± 16.68 / 75.79 ± 8.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.20 ± 0.86 / 36.88 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="score">56.03 ± 2.67</td> <!-- ScandEval score -->
   <td class="da-score">46.96 ± 3.82</td> <!-- Danish score -->
   <td class="no-score">52.10 ± 2.76</td> <!-- Norwegian score -->
   <td class="sv-score">69.05 ± 1.44</td> <!-- Swedish score -->
   <td class="da ner">67.40 ± 1.01 / 62.44 ± 1.32</td> <!-- DANSK -->
   <td class="da sent">41.53 ± 1.91 / 59.82 ± 1.67</td> <!-- Angry Tweets -->
   <td class="da la">41.62 ± 10.78 / 68.99 ± 5.73</td> <!-- ScaLA-da -->
   <td class="da qa">37.30 ± 1.59 / 42.46 ± 1.75</td> <!-- ScandiQA-da -->
   <td class="no ner">87.50 ± 0.53 / 87.45 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">80.57 ± 1.41 / 82.71 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">47.11 ± 2.05 / 60.70 ± 3.19</td> <!-- NoReC -->
   <td class="no la">52.62 ± 3.99 / 75.01 ± 2.43</td> <!-- ScaLA-nb -->
   <td class="no la">25.06 ± 6.94 / 60.75 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">38.40 ± 2.57 / 50.51 ± 3.52</td> <!-- NorQuAD -->
   <td class="sv ner">80.65 ± 2.12 / 78.69 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">77.43 ± 1.07 / 75.95 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">76.56 ± 1.06 / 87.86 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.54 ± 1.50 / 46.79 ± 1.60</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="score">55.06 ± 4.37</td> <!-- ScandEval score -->
   <td class="da-score">51.14 ± 3.96</td> <!-- Danish score -->
   <td class="no-score">56.67 ± 4.45</td> <!-- Norwegian score -->
   <td class="sv-score">57.38 ± 4.72</td> <!-- Swedish score -->
   <td class="da ner">71.81 ± 1.72 / 66.85 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.22 / 64.90 ± 0.81</td> <!-- Angry Tweets -->
   <td class="da la">54.99 ± 11.90 / 75.82 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.92 ± 0.98 / 34.74 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">90.60 ± 1.16 / 87.83 ± 1.34</td> <!-- NorNE-nb -->
   <td class="no ner">86.76 ± 0.82 / 83.48 ± 0.98</td> <!-- NorNE-nn -->
   <td class="no sent">52.19 ± 2.87 / 65.60 ± 2.58</td> <!-- NoReC -->
   <td class="no la">54.98 ± 14.19 / 75.67 ± 6.70</td> <!-- ScaLA-nb -->
   <td class="no la">58.33 ± 10.94 / 77.88 ± 5.29</td> <!-- ScaLA-nn -->
   <td class="no qa">29.17 ± 1.36 / 41.75 ± 1.59</td> <!-- NorQuAD -->
   <td class="sv ner">77.97 ± 0.82 / 72.10 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">73.27 ± 0.75 / 71.87 ± 1.30</td> <!-- SweReC -->
   <td class="sv la">47.19 ± 16.37 / 72.10 ± 8.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.07 ± 0.93 / 36.17 ± 0.73</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="score">54.51 ± 2.65</td> <!-- ScandEval score -->
   <td class="da-score">59.57 ± 1.46</td> <!-- Danish score -->
   <td class="no-score">52.31 ± 3.88</td> <!-- Norwegian score -->
   <td class="sv-score">51.65 ± 2.60</td> <!-- Swedish score -->
   <td class="da ner">72.55 ± 2.08 / 69.31 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">52.86 ± 1.08 / 68.19 ± 1.02</td> <!-- Angry Tweets -->
   <td class="da la">75.20 ± 1.73 / 86.99 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">37.65 ± 0.96 / 43.48 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">86.82 ± 0.53 / 84.15 ± 0.59</td> <!-- NorNE-nb -->
   <td class="no ner">79.91 ± 1.17 / 76.65 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">47.84 ± 2.44 / 60.67 ± 3.47</td> <!-- NoReC -->
   <td class="no la">51.99 ± 11.45 / 72.87 ± 8.55</td> <!-- ScaLA-nb -->
   <td class="no la">30.57 ± 8.63 / 62.90 ± 7.32</td> <!-- ScaLA-nn -->
   <td class="no qa">36.75 ± 2.18 / 50.77 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">72.33 ± 0.82 / 67.15 ± 0.85</td> <!-- SUC3 -->
   <td class="sv sent">67.77 ± 1.19 / 62.98 ± 2.57</td> <!-- SweReC -->
   <td class="sv la">33.79 ± 7.61 / 64.01 ± 6.84</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.71 ± 0.77 / 37.46 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="score">54.20 ± 2.03</td> <!-- ScandEval score -->
   <td class="da-score">48.24 ± 1.90</td> <!-- Danish score -->
   <td class="no-score">62.56 ± 1.93</td> <!-- Norwegian score -->
   <td class="sv-score">51.81 ± 2.26</td> <!-- Swedish score -->
   <td class="da ner">67.89 ± 2.14 / 64.13 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">39.34 ± 2.85 / 58.37 ± 3.66</td> <!-- Angry Tweets -->
   <td class="da la">50.90 ± 1.26 / 74.15 ± 0.81</td> <!-- ScaLA-da -->
   <td class="da qa">34.82 ± 1.33 / 39.58 ± 1.59</td> <!-- ScandiQA-da -->
   <td class="no ner">90.02 ± 0.72 / 86.99 ± 0.87</td> <!-- NorNE-nb -->
   <td class="no ner">86.52 ± 1.17 / 83.03 ± 1.53</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 3.24 / 61.35 ± 5.46</td> <!-- NoReC -->
   <td class="no la">67.29 ± 2.13 / 82.23 ± 1.36</td> <!-- ScaLA-nb -->
   <td class="no la">56.67 ± 2.29 / 76.74 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no qa">48.63 ± 1.31 / 63.28 ± 1.09</td> <!-- NorQuAD -->
   <td class="sv ner">74.22 ± 1.37 / 68.68 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">63.80 ± 1.56 / 57.65 ± 2.24</td> <!-- SweReC -->
   <td class="sv la">37.77 ± 5.16 / 65.87 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.45 ± 0.94 / 35.81 ± 0.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="score">52.91 ± 1.77</td> <!-- ScandEval score -->
   <td class="da-score">41.65 ± 2.67</td> <!-- Danish score -->
   <td class="no-score">46.69 ± 1.38</td> <!-- Norwegian score -->
   <td class="sv-score">70.39 ± 1.25</td> <!-- Swedish score -->
   <td class="da ner">58.50 ± 4.21 / 55.82 ± 3.50</td> <!-- DANSK -->
   <td class="da sent">41.02 ± 1.64 / 60.13 ± 1.52</td> <!-- Angry Tweets -->
   <td class="da la">27.10 ± 3.59 / 61.03 ± 2.41</td> <!-- ScaLA-da -->
   <td class="da qa">39.99 ± 1.25 / 45.72 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="no ner">85.99 ± 0.83 / 83.09 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">79.47 ± 1.14 / 75.61 ± 1.34</td> <!-- NorNE-nn -->
   <td class="no sent">39.53 ± 0.99 / 50.90 ± 2.17</td> <!-- NoReC -->
   <td class="no la">27.39 ± 2.48 / 61.03 ± 2.27</td> <!-- ScaLA-nb -->
   <td class="no la">23.56 ± 2.23 / 60.05 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">39.01 ± 1.18 / 51.83 ± 1.58</td> <!-- NorQuAD -->
   <td class="sv ner">81.05 ± 1.34 / 76.08 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">78.00 ± 0.89 / 75.01 ± 2.18</td> <!-- SweReC -->
   <td class="sv la">76.79 ± 1.70 / 87.59 ± 1.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.71 ± 1.09 / 51.70 ± 0.89</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="score">52.54 ± 1.76</td> <!-- ScandEval score -->
   <td class="da-score">42.27 ± 2.40</td> <!-- Danish score -->
   <td class="no-score">47.34 ± 1.49</td> <!-- Norwegian score -->
   <td class="sv-score">68.02 ± 1.40</td> <!-- Swedish score -->
   <td class="da ner">60.66 ± 1.45 / 56.95 ± 1.66</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 1.17 / 58.16 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.29 ± 5.92 / 63.74 ± 3.44</td> <!-- ScaLA-da -->
   <td class="da qa">37.68 ± 1.06 / 43.21 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">83.32 ± 0.99 / 80.48 ± 0.89</td> <!-- NorNE-nb -->
   <td class="no ner">77.97 ± 1.09 / 74.84 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">38.44 ± 1.67 / 52.60 ± 1.95</td> <!-- NoReC -->
   <td class="no la">37.54 ± 1.13 / 64.46 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">23.10 ± 3.66 / 58.14 ± 3.65</td> <!-- ScaLA-nn -->
   <td class="no qa">39.97 ± 0.84 / 51.67 ± 1.11</td> <!-- NorQuAD -->
   <td class="sv ner">78.61 ± 1.45 / 72.84 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 0.80 / 75.77 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">72.87 ± 2.36 / 85.57 ± 1.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.11 ± 0.99 / 49.29 ± 1.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="score">52.05 ± 2.34</td> <!-- ScandEval score -->
   <td class="da-score">47.29 ± 2.05</td> <!-- Danish score -->
   <td class="no-score">50.94 ± 3.00</td> <!-- Norwegian score -->
   <td class="sv-score">57.92 ± 1.97</td> <!-- Swedish score -->
   <td class="da ner">70.10 ± 1.16 / 64.54 ± 1.00</td> <!-- DANSK -->
   <td class="da sent">45.30 ± 2.03 / 63.22 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">51.74 ± 2.53 / 74.31 ± 1.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.01 ± 2.50 / 27.76 ± 2.44</td> <!-- ScandiQA-da -->
   <td class="no ner">87.70 ± 0.66 / 85.32 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">81.41 ± 1.46 / 77.41 ± 1.57</td> <!-- NorNE-nn -->
   <td class="no sent">48.34 ± 2.10 / 60.68 ± 3.61</td> <!-- NoReC -->
   <td class="no la">55.30 ± 2.89 / 75.77 ± 1.87</td> <!-- ScaLA-nb -->
   <td class="no la">37.46 ± 2.69 / 67.68 ± 1.66</td> <!-- ScaLA-nn -->
   <td class="no qa">24.49 ± 6.03 / 35.93 ± 8.56</td> <!-- NorQuAD -->
   <td class="sv ner">72.49 ± 1.68 / 67.03 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">70.69 ± 1.08 / 67.03 ± 3.40</td> <!-- SweReC -->
   <td class="sv la">56.60 ± 3.25 / 76.70 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.89 ± 1.88 / 37.63 ± 1.86</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="score">51.65 ± 1.86</td> <!-- ScandEval score -->
   <td class="da-score">41.35 ± 2.16</td> <!-- Danish score -->
   <td class="no-score">43.68 ± 2.29</td> <!-- Norwegian score -->
   <td class="sv-score">69.92 ± 1.13</td> <!-- Swedish score -->
   <td class="da ner">60.18 ± 2.71 / 57.15 ± 2.47</td> <!-- DANSK -->
   <td class="da sent">39.20 ± 1.69 / 59.33 ± 1.23</td> <!-- Angry Tweets -->
   <td class="da la">26.68 ± 3.38 / 59.41 ± 2.16</td> <!-- ScaLA-da -->
   <td class="da qa">39.34 ± 0.84 / 44.87 ± 0.79</td> <!-- ScandiQA-da -->
   <td class="no ner">84.03 ± 0.79 / 80.97 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">77.98 ± 1.36 / 74.25 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">39.15 ± 3.29 / 53.00 ± 3.85</td> <!-- NoReC -->
   <td class="no la">21.39 ± 2.73 / 58.08 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 3.43 / 57.00 ± 1.86</td> <!-- ScaLA-nn -->
   <td class="no qa">35.32 ± 1.71 / 47.41 ± 2.25</td> <!-- NorQuAD -->
   <td class="sv ner">80.39 ± 1.34 / 74.83 ± 1.44</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 0.79 / 77.12 ± 0.86</td> <!-- SweReC -->
   <td class="sv la">76.28 ± 1.86 / 87.37 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.56 ± 0.52 / 50.85 ± 0.56</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8</td> <!-- Rank -->
   <td>bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="score">50.63 ± 1.95</td> <!-- ScandEval score -->
   <td class="da-score">45.57 ± 2.56</td> <!-- Danish score -->
   <td class="no-score">51.06 ± 2.00</td> <!-- Norwegian score -->
   <td class="sv-score">55.28 ± 1.29</td> <!-- Swedish score -->
   <td class="da ner">64.92 ± 2.17 / 60.82 ± 1.86</td> <!-- DANSK -->
   <td class="da sent">33.50 ± 2.57 / 54.63 ± 2.14</td> <!-- Angry Tweets -->
   <td class="da la">46.75 ± 3.43 / 72.71 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">37.09 ± 2.08 / 41.77 ± 2.25</td> <!-- ScandiQA-da -->
   <td class="no ner">82.90 ± 1.44 / 79.06 ± 1.52</td> <!-- NorNE-nb -->
   <td class="no ner">77.33 ± 2.00 / 72.83 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">37.28 ± 2.13 / 48.69 ± 3.26</td> <!-- NoReC -->
   <td class="no la">49.41 ± 1.57 / 73.96 ± 0.87</td> <!-- ScaLA-nb -->
   <td class="no la">43.58 ± 2.23 / 71.20 ± 1.61</td> <!-- ScaLA-nn -->
   <td class="no qa">40.35 ± 2.26 / 54.01 ± 2.42</td> <!-- NorQuAD -->
   <td class="sv ner">70.85 ± 1.56 / 65.50 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">63.30 ± 0.93 / 59.96 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">48.97 ± 1.14 / 73.78 ± 0.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.00 ± 1.52 / 42.69 ± 1.62</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="score">50.33 ± 2.46</td> <!-- ScandEval score -->
   <td class="da-score">39.21 ± 2.76</td> <!-- Danish score -->
   <td class="no-score">43.04 ± 3.35</td> <!-- Norwegian score -->
   <td class="sv-score">68.74 ± 1.27</td> <!-- Swedish score -->
   <td class="da ner">61.74 ± 1.46 / 58.09 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">33.28 ± 1.65 / 54.37 ± 1.44</td> <!-- Angry Tweets -->
   <td class="da la">33.15 ± 7.14 / 64.69 ± 4.47</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td class="no ner">85.91 ± 0.98 / 83.05 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">79.67 ± 1.62 / 76.00 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">38.70 ± 2.53 / 50.88 ± 3.38</td> <!-- NoReC -->
   <td class="no la">39.13 ± 2.97 / 67.97 ± 1.68</td> <!-- ScaLA-nb -->
   <td class="no la">24.13 ± 6.88 / 60.76 ± 3.29</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td class="sv ner">81.95 ± 1.55 / 76.66 ± 1.60</td> <!-- SUC3 -->
   <td class="sv sent">75.58 ± 1.17 / 73.35 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">78.86 ± 0.83 / 89.07 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="score">50.13 ± 2.44</td> <!-- ScandEval score -->
   <td class="da-score">39.27 ± 2.76</td> <!-- Danish score -->
   <td class="no-score">42.61 ± 3.37</td> <!-- Norwegian score -->
   <td class="sv-score">68.53 ± 1.20</td> <!-- Swedish score -->
   <td class="da ner">61.74 ± 1.46 / 58.09 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">33.31 ± 1.49 / 54.09 ± 1.49</td> <!-- Angry Tweets -->
   <td class="da la">33.35 ± 7.32 / 64.61 ± 4.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td class="no ner">85.33 ± 1.01 / 82.13 ± 1.28</td> <!-- NorNE-nb -->
   <td class="no ner">79.44 ± 1.66 / 75.74 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">38.17 ± 2.21 / 50.44 ± 3.11</td> <!-- NoReC -->
   <td class="no la">39.49 ± 3.36 / 68.13 ± 2.13</td> <!-- ScaLA-nb -->
   <td class="no la">22.17 ± 7.22 / 60.16 ± 3.80</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td class="sv ner">81.23 ± 1.58 / 75.95 ± 1.72</td> <!-- SUC3 -->
   <td class="sv sent">75.73 ± 0.72 / 73.61 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">78.60 ± 0.98 / 88.95 ± 0.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="score">49.76 ± 2.17</td> <!-- ScandEval score -->
   <td class="da-score">43.43 ± 2.54</td> <!-- Danish score -->
   <td class="no-score">51.22 ± 1.98</td> <!-- Norwegian score -->
   <td class="sv-score">54.63 ± 1.98</td> <!-- Swedish score -->
   <td class="da ner">65.40 ± 2.02 / 60.53 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">34.43 ± 4.13 / 51.90 ± 6.17</td> <!-- Angry Tweets -->
   <td class="da la">67.27 ± 1.04 / 83.37 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">6.60 ± 2.98 / 7.09 ± 3.29</td> <!-- ScandiQA-da -->
   <td class="no ner">84.95 ± 0.58 / 81.68 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">79.57 ± 1.49 / 74.62 ± 1.92</td> <!-- NorNE-nn -->
   <td class="no sent">40.15 ± 1.15 / 46.26 ± 0.47</td> <!-- NoReC -->
   <td class="no la">72.87 ± 1.11 / 85.86 ± 0.63</td> <!-- ScaLA-nb -->
   <td class="no la">63.77 ± 1.27 / 81.62 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">14.16 ± 4.55 / 19.70 ± 6.40</td> <!-- NorQuAD -->
   <td class="sv ner">71.07 ± 1.59 / 65.46 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">66.42 ± 0.72 / 57.57 ± 1.23</td> <!-- SweReC -->
   <td class="sv la">69.19 ± 0.66 / 84.26 ± 0.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">11.85 ± 4.94 / 13.02 ± 5.55</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="score">49.52 ± 3.21</td> <!-- ScandEval score -->
   <td class="da-score">40.76 ± 4.29</td> <!-- Danish score -->
   <td class="no-score">51.05 ± 2.54</td> <!-- Norwegian score -->
   <td class="sv-score">56.75 ± 2.80</td> <!-- Swedish score -->
   <td class="da ner">63.17 ± 2.79 / 59.45 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">32.38 ± 1.72 / 53.30 ± 1.79</td> <!-- Angry Tweets -->
   <td class="da la">27.93 ± 11.48 / 61.91 ± 6.69</td> <!-- ScaLA-da -->
   <td class="da qa">39.57 ± 1.18 / 44.06 ± 1.25</td> <!-- ScandiQA-da -->
   <td class="no ner">88.72 ± 0.76 / 85.49 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">83.08 ± 1.22 / 79.36 ± 1.38</td> <!-- NorNE-nn -->
   <td class="no sent">35.87 ± 1.85 / 48.94 ± 3.37</td> <!-- NoReC -->
   <td class="no la">44.22 ± 3.29 / 70.31 ± 2.86</td> <!-- ScaLA-nb -->
   <td class="no la">39.55 ± 7.01 / 68.65 ± 3.36</td> <!-- ScaLA-nn -->
   <td class="no qa">40.55 ± 2.19 / 53.62 ± 2.68</td> <!-- NorQuAD -->
   <td class="sv ner">76.29 ± 1.28 / 70.33 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">61.78 ± 1.21 / 60.94 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">47.74 ± 7.69 / 72.98 ± 4.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.17 ± 1.01 / 46.07 ± 1.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="score">49.26 ± 1.66</td> <!-- ScandEval score -->
   <td class="da-score">38.19 ± 1.85</td> <!-- Danish score -->
   <td class="no-score">43.03 ± 1.81</td> <!-- Norwegian score -->
   <td class="sv-score">66.55 ± 1.33</td> <!-- Swedish score -->
   <td class="da ner">57.97 ± 1.64 / 54.71 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">39.40 ± 1.14 / 59.02 ± 0.60</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 1.86 / 59.54 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">31.87 ± 2.77 / 36.99 ± 2.78</td> <!-- ScandiQA-da -->
   <td class="no ner">82.20 ± 1.19 / 79.13 ± 1.26</td> <!-- NorNE-nb -->
   <td class="no ner">76.64 ± 1.10 / 72.90 ± 1.43</td> <!-- NorNE-nn -->
   <td class="no sent">40.20 ± 1.56 / 54.68 ± 2.46</td> <!-- NoReC -->
   <td class="no la">24.45 ± 2.21 / 58.75 ± 1.80</td> <!-- ScaLA-nb -->
   <td class="no la">19.18 ± 3.55 / 57.93 ± 2.05</td> <!-- ScaLA-nn -->
   <td class="no qa">30.69 ± 1.64 / 42.59 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">78.91 ± 1.24 / 72.93 ± 1.08</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 0.81 / 72.74 ± 2.11</td> <!-- SweReC -->
   <td class="sv la">70.08 ± 2.11 / 83.40 ± 1.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.14 ± 1.18 / 47.18 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="score">49.23 ± 3.20</td> <!-- ScandEval score -->
   <td class="da-score">44.89 ± 2.99</td> <!-- Danish score -->
   <td class="no-score">49.07 ± 3.96</td> <!-- Norwegian score -->
   <td class="sv-score">53.73 ± 2.64</td> <!-- Swedish score -->
   <td class="da ner">63.38 ± 2.39 / 59.20 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">34.78 ± 1.49 / 55.59 ± 0.92</td> <!-- Angry Tweets -->
   <td class="da la">41.08 ± 7.28 / 69.77 ± 3.75</td> <!-- ScaLA-da -->
   <td class="da qa">40.32 ± 0.81 / 44.89 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">88.05 ± 0.85 / 84.88 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">83.08 ± 1.50 / 79.06 ± 1.70</td> <!-- NorNE-nn -->
   <td class="no sent">35.34 ± 1.88 / 48.31 ± 2.28</td> <!-- NoReC -->
   <td class="no la">31.45 ± 12.12 / 63.68 ± 6.21</td> <!-- ScaLA-nb -->
   <td class="no la">36.12 ± 8.59 / 66.98 ± 4.91</td> <!-- ScaLA-nn -->
   <td class="no qa">41.59 ± 2.45 / 54.67 ± 2.65</td> <!-- NorQuAD -->
   <td class="sv ner">76.55 ± 1.28 / 70.38 ± 1.01</td> <!-- SUC3 -->
   <td class="sv sent">61.60 ± 1.38 / 62.28 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">37.44 ± 6.65 / 66.67 ± 4.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.32 ± 1.25 / 43.87 ± 1.29</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="score">49.11 ± 2.71</td> <!-- ScandEval score -->
   <td class="da-score">44.37 ± 2.47</td> <!-- Danish score -->
   <td class="no-score">49.54 ± 3.00</td> <!-- Norwegian score -->
   <td class="sv-score">53.42 ± 2.67</td> <!-- Swedish score -->
   <td class="da ner">62.66 ± 1.84 / 58.60 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">33.91 ± 1.43 / 54.87 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">40.96 ± 4.05 / 69.68 ± 2.12</td> <!-- ScaLA-da -->
   <td class="da qa">39.93 ± 2.55 / 44.63 ± 2.71</td> <!-- ScandiQA-da -->
   <td class="no ner">89.07 ± 1.08 / 85.89 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">82.69 ± 0.90 / 79.22 ± 0.93</td> <!-- NorNE-nn -->
   <td class="no sent">34.97 ± 1.74 / 48.21 ± 2.02</td> <!-- NoReC -->
   <td class="no la">39.58 ± 5.70 / 67.91 ± 3.00</td> <!-- ScaLA-nb -->
   <td class="no la">31.27 ± 9.57 / 62.81 ± 7.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.89 ± 1.64 / 55.17 ± 2.07</td> <!-- NorQuAD -->
   <td class="sv ner">75.33 ± 0.99 / 69.89 ± 0.52</td> <!-- SUC3 -->
   <td class="sv sent">61.80 ± 1.76 / 58.93 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 5.98 / 66.91 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.95 ± 1.95 / 44.71 ± 1.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="score">49.09 ± 7.00</td> <!-- ScandEval score -->
   <td class="da-score">47.72 ± 6.19</td> <!-- Danish score -->
   <td class="no-score">43.30 ± 8.26</td> <!-- Norwegian score -->
   <td class="sv-score">56.24 ± 6.54</td> <!-- Swedish score -->
   <td class="da ner">71.42 ± 2.68 / 66.61 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">31.86 ± 8.76 / 47.51 ± 8.94</td> <!-- Angry Tweets -->
   <td class="da la">52.95 ± 11.68 / 73.96 ± 8.89</td> <!-- ScaLA-da -->
   <td class="da qa">34.66 ± 1.64 / 40.58 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="no ner">89.99 ± 1.32 / 87.51 ± 1.20</td> <!-- NorNE-nb -->
   <td class="no ner">78.60 ± 3.17 / 74.97 ± 3.56</td> <!-- NorNE-nn -->
   <td class="no sent">17.93 ± 14.48 / 34.24 ± 10.14</td> <!-- NoReC -->
   <td class="no la">43.46 ± 17.47 / 66.52 ± 12.26</td> <!-- ScaLA-nb -->
   <td class="no la">10.97 ± 10.84 / 43.47 ± 9.81</td> <!-- ScaLA-nn -->
   <td class="no qa">43.74 ± 2.17 / 59.80 ± 1.86</td> <!-- NorQuAD -->
   <td class="sv ner">68.39 ± 7.26 / 63.66 ± 6.41</td> <!-- SUC3 -->
   <td class="sv sent">73.43 ± 0.91 / 61.29 ± 1.81</td> <!-- SweReC -->
   <td class="sv la">45.09 ± 15.90 / 68.48 ± 11.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.04 ± 2.09 / 43.73 ± 1.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="score">48.84 ± 2.86</td> <!-- ScandEval score -->
   <td class="da-score">40.98 ± 4.16</td> <!-- Danish score -->
   <td class="no-score">51.22 ± 1.72</td> <!-- Norwegian score -->
   <td class="sv-score">54.32 ± 2.70</td> <!-- Swedish score -->
   <td class="da ner">62.53 ± 2.60 / 58.99 ± 2.88</td> <!-- DANSK -->
   <td class="da sent">32.88 ± 1.24 / 53.56 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">29.01 ± 11.25 / 61.89 ± 6.94</td> <!-- ScaLA-da -->
   <td class="da qa">39.51 ± 1.53 / 44.11 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="no ner">87.99 ± 1.24 / 84.84 ± 1.42</td> <!-- NorNE-nb -->
   <td class="no ner">83.10 ± 1.12 / 79.18 ± 1.45</td> <!-- NorNE-nn -->
   <td class="no sent">36.21 ± 1.82 / 49.48 ± 2.69</td> <!-- NoReC -->
   <td class="no la">46.43 ± 1.81 / 71.65 ± 1.39</td> <!-- ScaLA-nb -->
   <td class="no la">39.82 ± 2.81 / 68.68 ± 1.81</td> <!-- ScaLA-nn -->
   <td class="no qa">40.01 ± 1.58 / 53.12 ± 1.81</td> <!-- NorQuAD -->
   <td class="sv ner">75.62 ± 1.56 / 70.17 ± 1.46</td> <!-- SUC3 -->
   <td class="sv sent">62.50 ± 1.10 / 60.57 ± 2.75</td> <!-- SweReC -->
   <td class="sv la">38.18 ± 7.03 / 66.99 ± 4.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.96 ± 1.11 / 45.91 ± 1.20</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10</td> <!-- Rank -->
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="score">48.48 ± 5.08</td> <!-- ScandEval score -->
   <td class="da-score">42.97 ± 6.34</td> <!-- Danish score -->
   <td class="no-score">47.09 ± 4.93</td> <!-- Norwegian score -->
   <td class="sv-score">55.39 ± 3.96</td> <!-- Swedish score -->
   <td class="da ner">74.42 ± 1.81 / 69.54 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">37.94 ± 10.08 / 55.77 ± 9.21</td> <!-- Angry Tweets -->
   <td class="da la">15.26 ± 10.94 / 48.92 ± 8.26</td> <!-- ScaLA-da -->
   <td class="da qa">44.25 ± 2.55 / 50.10 ± 2.75</td> <!-- ScandiQA-da -->
   <td class="no ner">91.90 ± 0.62 / 89.48 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.59 ± 1.49 / 82.92 ± 1.66</td> <!-- NorNE-nn -->
   <td class="no sent">30.56 ± 13.68 / 45.96 ± 11.45</td> <!-- NoReC -->
   <td class="no la">9.79 ± 5.13 / 46.75 ± 6.05</td> <!-- ScaLA-nb -->
   <td class="no la">6.36 ± 2.82 / 48.52 ± 4.11</td> <!-- ScaLA-nn -->
   <td class="no qa">60.47 ± 1.01 / 74.70 ± 0.92</td> <!-- NorQuAD -->
   <td class="sv ner">79.53 ± 2.77 / 74.53 ± 2.70</td> <!-- SUC3 -->
   <td class="sv sent">75.42 ± 1.08 / 72.68 ± 3.19</td> <!-- SweReC -->
   <td class="sv la">18.44 ± 10.88 / 53.57 ± 7.20</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.19 ± 1.10 / 53.67 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="score">48.38 ± 2.69</td> <!-- ScandEval score -->
   <td class="da-score">42.70 ± 3.83</td> <!-- Danish score -->
   <td class="no-score">48.20 ± 2.95</td> <!-- Norwegian score -->
   <td class="sv-score">54.23 ± 1.30</td> <!-- Swedish score -->
   <td class="da ner">62.57 ± 1.98 / 59.39 ± 2.04</td> <!-- DANSK -->
   <td class="da sent">33.67 ± 1.54 / 54.48 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">35.79 ± 9.58 / 65.87 ± 5.46</td> <!-- ScaLA-da -->
   <td class="da qa">38.77 ± 2.23 / 43.26 ± 2.39</td> <!-- ScandiQA-da -->
   <td class="no ner">88.55 ± 0.85 / 85.29 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">83.09 ± 1.06 / 79.27 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">35.16 ± 1.75 / 48.41 ± 2.71</td> <!-- NoReC -->
   <td class="no la">31.82 ± 8.92 / 62.98 ± 6.52</td> <!-- ScaLA-nb -->
   <td class="no la">32.94 ± 5.88 / 64.36 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no qa">39.46 ± 1.70 / 52.33 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">74.88 ± 1.45 / 69.57 ± 1.83</td> <!-- SUC3 -->
   <td class="sv sent">61.89 ± 0.90 / 60.17 ± 3.06</td> <!-- SweReC -->
   <td class="sv la">40.22 ± 2.03 / 68.89 ± 2.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.95 ± 0.82 / 44.78 ± 0.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="score">48.07 ± 3.35</td> <!-- ScandEval score -->
   <td class="da-score">46.45 ± 2.91</td> <!-- Danish score -->
   <td class="no-score">44.18 ± 3.72</td> <!-- Norwegian score -->
   <td class="sv-score">53.56 ± 3.44</td> <!-- Swedish score -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">56.70 ± 1.80 / 64.12 ± 1.15</td> <!-- ScandiQA-da -->
   <td class="no ner">61.18 ± 2.76 / 56.36 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">65.16 ± 3.97 / 55.74 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">55.61 ± 4.02 / 68.27 ± 3.49</td> <!-- NoReC -->
   <td class="no la">20.84 ± 5.41 / 49.36 ± 4.98</td> <!-- ScaLA-nb -->
   <td class="no la">9.12 ± 3.51 / 43.06 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no qa">42.98 ± 3.04 / 69.12 ± 2.82</td> <!-- NorQuAD -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.43 ± 1.62 / 65.06 ± 1.24</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="score">46.94 ± 3.28</td> <!-- ScandEval score -->
   <td class="da-score">40.89 ± 4.42</td> <!-- Danish score -->
   <td class="no-score">47.23 ± 2.70</td> <!-- Norwegian score -->
   <td class="sv-score">52.71 ± 2.72</td> <!-- Swedish score -->
   <td class="da ner">62.76 ± 1.92 / 58.88 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">32.06 ± 1.44 / 52.57 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 11.93 / 63.72 ± 6.84</td> <!-- ScaLA-da -->
   <td class="da qa">37.79 ± 2.37 / 42.36 ± 2.56</td> <!-- ScandiQA-da -->
   <td class="no ner">87.52 ± 0.63 / 83.86 ± 0.68</td> <!-- NorNE-nb -->
   <td class="no ner">82.66 ± 1.64 / 78.65 ± 2.01</td> <!-- NorNE-nn -->
   <td class="no sent">32.73 ± 1.37 / 46.52 ± 1.86</td> <!-- NoReC -->
   <td class="no la">36.41 ± 8.89 / 65.20 ± 6.41</td> <!-- ScaLA-nb -->
   <td class="no la">30.37 ± 5.50 / 62.12 ± 5.66</td> <!-- ScaLA-nn -->
   <td class="no qa">37.71 ± 1.11 / 49.90 ± 1.47</td> <!-- NorQuAD -->
   <td class="sv ner">74.13 ± 1.17 / 68.93 ± 1.36</td> <!-- SUC3 -->
   <td class="sv sent">62.18 ± 1.26 / 59.44 ± 2.35</td> <!-- SweReC -->
   <td class="sv la">36.93 ± 6.47 / 65.97 ± 6.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.59 ± 1.99 / 41.94 ± 2.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="score">46.89 ± 3.14</td> <!-- ScandEval score -->
   <td class="da-score">45.38 ± 3.12</td> <!-- Danish score -->
   <td class="no-score">41.38 ± 3.33</td> <!-- Norwegian score -->
   <td class="sv-score">53.92 ± 2.97</td> <!-- Swedish score -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da qa">57.39 ± 1.73 / 63.66 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="no ner">54.04 ± 2.86 / 48.50 ± 2.85</td> <!-- NorNE-nb -->
   <td class="no ner">62.21 ± 3.31 / 50.38 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">54.74 ± 3.71 / 67.81 ± 2.80</td> <!-- NoReC -->
   <td class="no la">14.51 ± 1.97 / 40.94 ± 1.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.38 ± 4.69 / 37.62 ± 2.92</td> <!-- ScaLA-nn -->
   <td class="no qa">42.71 ± 3.21 / 69.11 ± 2.46</td> <!-- NorQuAD -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.92 ± 1.60 / 65.40 ± 1.37</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12</td> <!-- Rank -->
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="score">46.85 ± 2.58</td> <!-- ScandEval score -->
   <td class="da-score">39.98 ± 3.06</td> <!-- Danish score -->
   <td class="no-score">50.53 ± 1.89</td> <!-- Norwegian score -->
   <td class="sv-score">50.02 ± 2.78</td> <!-- Swedish score -->
   <td class="da ner">70.36 ± 2.14 / 65.91 ± 2.15</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.46 / 65.49 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">11.87 ± 5.47 / 48.82 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da qa">29.87 ± 3.18 / 35.11 ± 2.73</td> <!-- ScandiQA-da -->
   <td class="no ner">90.07 ± 1.08 / 87.56 ± 1.39</td> <!-- NorNE-nb -->
   <td class="no ner">85.65 ± 0.96 / 82.40 ± 1.16</td> <!-- NorNE-nn -->
   <td class="no sent">54.46 ± 1.16 / 68.25 ± 0.76</td> <!-- NoReC -->
   <td class="no la">12.16 ± 5.91 / 50.55 ± 4.73</td> <!-- ScaLA-nb -->
   <td class="no la">8.99 ± 2.25 / 48.57 ± 3.67</td> <!-- ScaLA-nn -->
   <td class="no qa">49.24 ± 1.30 / 64.35 ± 1.24</td> <!-- NorQuAD -->
   <td class="sv ner">78.60 ± 1.91 / 73.04 ± 2.25</td> <!-- SUC3 -->
   <td class="sv sent">73.67 ± 1.48 / 68.61 ± 3.14</td> <!-- SweReC -->
   <td class="sv la">15.41 ± 4.59 / 53.29 ± 3.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.41 ± 3.14 / 37.13 ± 3.07</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="score">46.66 ± 3.03</td> <!-- ScandEval score -->
   <td class="da-score">43.27 ± 3.17</td> <!-- Danish score -->
   <td class="no-score">42.72 ± 3.11</td> <!-- Norwegian score -->
   <td class="sv-score">53.98 ± 2.82</td> <!-- Swedish score -->
   <td class="da ner">45.61 ± 3.06 / 35.04 ± 2.94</td> <!-- DANSK -->
   <td class="da sent">53.73 ± 3.06 / 67.51 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">17.08 ± 5.36 / 52.62 ± 5.62</td> <!-- ScaLA-da -->
   <td class="da qa">56.67 ± 1.19 / 61.18 ± 1.07</td> <!-- ScandiQA-da -->
   <td class="no ner">48.24 ± 3.18 / 42.53 ± 3.52</td> <!-- NorNE-nb -->
   <td class="no ner">61.50 ± 1.54 / 50.90 ± 4.58</td> <!-- NorNE-nn -->
   <td class="no sent">49.40 ± 3.40 / 60.71 ± 3.33</td> <!-- NoReC -->
   <td class="no la">24.12 ± 3.24 / 59.38 ± 2.25</td> <!-- ScaLA-nb -->
   <td class="no la">13.20 ± 3.16 / 54.42 ± 3.04</td> <!-- ScaLA-nn -->
   <td class="no qa">47.93 ± 3.46 / 69.52 ± 3.06</td> <!-- NorQuAD -->
   <td class="sv ner">46.61 ± 3.11 / 34.10 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 2.01 / 78.30 ± 2.42</td> <!-- SweReC -->
   <td class="sv la">34.16 ± 4.39 / 60.06 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.77 ± 1.76 / 63.50 ± 1.47</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="score">46.46 ± 3.30</td> <!-- ScandEval score -->
   <td class="da-score">45.84 ± 3.41</td> <!-- Danish score -->
   <td class="no-score">39.43 ± 3.67</td> <!-- Norwegian score -->
   <td class="sv-score">54.10 ± 2.82</td> <!-- Swedish score -->
   <td class="da ner">45.94 ± 3.62 / 35.68 ± 3.35</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 4.52 / 62.28 ± 4.29</td> <!-- Angry Tweets -->
   <td class="da la">28.04 ± 3.83 / 58.31 ± 5.00</td> <!-- ScaLA-da -->
   <td class="da qa">57.65 ± 1.66 / 62.03 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="no ner">49.67 ± 3.12 / 43.26 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">61.11 ± 1.93 / 50.15 ± 4.14</td> <!-- NorNE-nn -->
   <td class="no sent">56.07 ± 5.22 / 68.93 ± 4.07</td> <!-- NoReC -->
   <td class="no la">3.81 ± 3.09 / 34.47 ± 1.22</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.98 ± 4.12 / 68.18 ± 3.39</td> <!-- NorQuAD -->
   <td class="sv ner">46.57 ± 3.34 / 33.94 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.53 ± 2.55 / 77.96 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">33.43 ± 3.89 / 61.87 ± 4.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.87 ± 1.52 / 64.53 ± 1.41</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="score">46.44 ± 3.31</td> <!-- ScandEval score -->
   <td class="da-score">45.76 ± 3.30</td> <!-- Danish score -->
   <td class="no-score">39.27 ± 3.63</td> <!-- Norwegian score -->
   <td class="sv-score">54.28 ± 2.99</td> <!-- Swedish score -->
   <td class="da ner">46.06 ± 3.28 / 35.43 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 4.23 / 61.68 ± 4.43</td> <!-- Angry Tweets -->
   <td class="da la">27.68 ± 4.25 / 57.59 ± 5.15</td> <!-- ScaLA-da -->
   <td class="da qa">57.78 ± 1.43 / 62.26 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="no ner">49.69 ± 2.90 / 43.57 ± 2.90</td> <!-- NorNE-nb -->
   <td class="no ner">61.78 ± 2.03 / 49.91 ± 4.24</td> <!-- NorNE-nn -->
   <td class="no sent">55.87 ± 5.21 / 68.97 ± 3.95</td> <!-- NoReC -->
   <td class="no la">2.99 ± 3.04 / 34.16 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.62 ± 4.06 / 68.17 ± 3.48</td> <!-- NorQuAD -->
   <td class="sv ner">47.28 ± 3.05 / 34.01 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.62 ± 2.52 / 78.04 ± 2.98</td> <!-- SweReC -->
   <td class="sv la">33.23 ± 4.72 / 61.29 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.00 ± 1.69 / 64.62 ± 1.44</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="score">46.41 ± 1.99</td> <!-- ScandEval score -->
   <td class="da-score">44.16 ± 2.18</td> <!-- Danish score -->
   <td class="no-score">42.90 ± 2.12</td> <!-- Norwegian score -->
   <td class="sv-score">52.16 ± 1.65</td> <!-- Swedish score -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">59.82 ± 0.84 / 65.44 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">61.41 ± 1.71 / 52.32 ± 2.63</td> <!-- NorNE-nb -->
   <td class="no ner">59.49 ± 1.26 / 49.45 ± 3.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.19 ± 1.64 / 63.36 ± 1.52</td> <!-- NoReC -->
   <td class="no la">15.17 ± 2.64 / 50.25 ± 4.51</td> <!-- ScaLA-nb -->
   <td class="no la">10.78 ± 1.99 / 50.08 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">48.98 ± 3.05 / 73.08 ± 2.30</td> <!-- NorQuAD -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.60 ± 1.00 / 64.53 ± 0.78</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="score">46.40 ± 1.43</td> <!-- ScandEval score -->
   <td class="da-score">35.39 ± 1.79</td> <!-- Danish score -->
   <td class="no-score">38.03 ± 1.72</td> <!-- Norwegian score -->
   <td class="sv-score">65.78 ± 0.79</td> <!-- Swedish score -->
   <td class="da ner">53.93 ± 1.88 / 52.04 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">36.31 ± 1.60 / 57.37 ± 1.15</td> <!-- Angry Tweets -->
   <td class="da la">23.46 ± 1.17 / 58.91 ± 1.36</td> <!-- ScaLA-da -->
   <td class="da qa">27.85 ± 2.53 / 34.34 ± 2.51</td> <!-- ScandiQA-da -->
   <td class="no ner">77.98 ± 1.58 / 75.03 ± 1.70</td> <!-- NorNE-nb -->
   <td class="no ner">75.00 ± 1.28 / 71.00 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">33.88 ± 1.40 / 49.21 ± 1.98</td> <!-- NoReC -->
   <td class="no la">24.23 ± 1.83 / 58.89 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">18.18 ± 2.65 / 57.28 ± 1.84</td> <!-- ScaLA-nn -->
   <td class="no qa">20.56 ± 1.82 / 30.08 ± 2.54</td> <!-- NorQuAD -->
   <td class="sv ner">79.29 ± 0.94 / 73.18 ± 0.95</td> <!-- SUC3 -->
   <td class="sv sent">75.85 ± 0.54 / 70.58 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">70.43 ± 1.03 / 83.85 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.56 ± 0.64 / 44.01 ± 0.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="score">45.83 ± 3.11</td> <!-- ScandEval score -->
   <td class="da-score">43.44 ± 3.38</td> <!-- Danish score -->
   <td class="no-score">41.00 ± 3.42</td> <!-- Norwegian score -->
   <td class="sv-score">53.05 ± 2.54</td> <!-- Swedish score -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da qa">58.27 ± 1.08 / 63.53 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">42.02 ± 2.82 / 66.99 ± 2.53</td> <!-- NorQuAD -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.18 ± 1.37 / 64.78 ± 1.14</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">45.69 ± 3.12</td> <!-- ScandEval score -->
   <td class="da-score">43.95 ± 3.15</td> <!-- Danish score -->
   <td class="no-score">41.99 ± 3.07</td> <!-- Norwegian score -->
   <td class="sv-score">51.13 ± 3.15</td> <!-- Swedish score -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da qa">51.75 ± 2.23 / 61.31 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no qa">34.48 ± 2.13 / 65.45 ± 2.05</td> <!-- NorQuAD -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.96 ± 2.34 / 60.01 ± 1.19</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="score">45.68 ± 3.06</td> <!-- ScandEval score -->
   <td class="da-score">45.56 ± 2.72</td> <!-- Danish score -->
   <td class="no-score">40.41 ± 3.51</td> <!-- Norwegian score -->
   <td class="sv-score">51.08 ± 2.95</td> <!-- Swedish score -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">58.23 ± 1.78 / 63.89 ± 1.51</td> <!-- ScandiQA-da -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no qa">41.56 ± 3.29 / 67.34 ± 2.82</td> <!-- NorQuAD -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.10 ± 1.61 / 65.00 ± 1.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="score">45.57 ± 3.04</td> <!-- ScandEval score -->
   <td class="da-score">42.97 ± 2.91</td> <!-- Danish score -->
   <td class="no-score">43.73 ± 3.25</td> <!-- Norwegian score -->
   <td class="sv-score">50.02 ± 2.95</td> <!-- Swedish score -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 2.00 / 64.34 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no qa">42.42 ± 2.92 / 69.55 ± 3.18</td> <!-- NorQuAD -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.69 ± 1.54 / 65.02 ± 1.14</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="score">45.44 ± 3.31</td> <!-- ScandEval score -->
   <td class="da-score">44.68 ± 3.17</td> <!-- Danish score -->
   <td class="no-score">39.79 ± 3.84</td> <!-- Norwegian score -->
   <td class="sv-score">51.85 ± 2.92</td> <!-- Swedish score -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da qa">56.81 ± 1.68 / 62.39 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="no ner">55.93 ± 2.70 / 50.51 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">63.85 ± 2.45 / 53.11 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">50.41 ± 5.49 / 64.49 ± 4.37</td> <!-- NoReC -->
   <td class="no la">15.74 ± 4.15 / 41.16 ± 2.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.23 ± 4.69 / 34.70 ± 1.39</td> <!-- ScaLA-nn -->
   <td class="no qa">39.87 ± 2.87 / 65.67 ± 2.58</td> <!-- NorQuAD -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.81 ± 1.16 / 64.81 ± 1.01</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">14=</td> <!-- Rank -->
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="score">45.09 ± 2.68</td> <!-- ScandEval score -->
   <td class="da-score">40.81 ± 3.88</td> <!-- Danish score -->
   <td class="no-score">41.42 ± 2.29</td> <!-- Norwegian score -->
   <td class="sv-score">53.05 ± 1.86</td> <!-- Swedish score -->
   <td class="da ner">61.98 ± 2.00 / 58.30 ± 2.12</td> <!-- DANSK -->
   <td class="da sent">47.20 ± 1.34 / 64.51 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">40.52 ± 7.38 / 67.99 ± 3.84</td> <!-- ScaLA-da -->
   <td class="da qa">13.53 ± 4.79 / 15.93 ± 5.58</td> <!-- ScandiQA-da -->
   <td class="no ner">84.11 ± 1.13 / 81.19 ± 1.37</td> <!-- NorNE-nb -->
   <td class="no ner">77.82 ± 1.28 / 73.93 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">39.63 ± 1.06 / 49.23 ± 2.13</td> <!-- NoReC -->
   <td class="no la">45.75 ± 3.27 / 71.33 ± 1.67</td> <!-- ScaLA-nb -->
   <td class="no la">33.74 ± 2.91 / 63.89 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 3.79 / 7.65 ± 5.41</td> <!-- NorQuAD -->
   <td class="sv ner">71.34 ± 0.91 / 65.04 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">70.91 ± 1.23 / 67.12 ± 3.79</td> <!-- SweReC -->
   <td class="sv la">53.52 ± 1.22 / 76.15 ± 0.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.41 ± 4.10 / 18.47 ± 4.44</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">14=</td> <!-- Rank -->
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="score">44.99 ± 2.24</td> <!-- ScandEval score -->
   <td class="da-score">41.00 ± 3.47</td> <!-- Danish score -->
   <td class="no-score">39.45 ± 1.89</td> <!-- Norwegian score -->
   <td class="sv-score">54.52 ± 1.36</td> <!-- Swedish score -->
   <td class="da ner">60.82 ± 2.03 / 57.64 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 0.78 / 55.56 ± 0.68</td> <!-- Angry Tweets -->
   <td class="da la">41.89 ± 9.80 / 70.04 ± 5.10</td> <!-- ScaLA-da -->
   <td class="da qa">26.83 ± 1.26 / 31.55 ± 1.26</td> <!-- ScandiQA-da -->
   <td class="no ner">85.42 ± 0.61 / 82.31 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">78.92 ± 1.42 / 74.86 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">36.27 ± 1.57 / 50.95 ± 1.70</td> <!-- NoReC -->
   <td class="no la">48.07 ± 5.64 / 72.00 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">29.81 ± 3.52 / 64.03 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no qa">0.44 ± 0.41 / 1.08 ± 0.99</td> <!-- NorQuAD -->
   <td class="sv ner">72.90 ± 1.37 / 66.93 ± 1.30</td> <!-- SUC3 -->
   <td class="sv sent">61.11 ± 1.28 / 58.97 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">55.05 ± 1.64 / 76.76 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.04 ± 1.16 / 33.60 ± 1.06</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">15=</td> <!-- Rank -->
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="score">44.85 ± 3.16</td> <!-- ScandEval score -->
   <td class="da-score">42.96 ± 2.99</td> <!-- Danish score -->
   <td class="no-score">38.65 ± 2.71</td> <!-- Norwegian score -->
   <td class="sv-score">52.95 ± 3.78</td> <!-- Swedish score -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da qa">57.88 ± 2.44 / 64.46 ± 1.86</td> <!-- ScandiQA-da -->
   <td class="no ner">53.68 ± 2.01 / 49.22 ± 2.67</td> <!-- NorNE-nb -->
   <td class="no ner">61.92 ± 4.06 / 49.03 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.19 / 57.76 ± 2.55</td> <!-- NoReC -->
   <td class="no la">0.91 ± 1.78 / 33.51 ± 0.85</td> <!-- ScaLA-nb -->
   <td class="no la">1.24 ± 1.66 / 33.71 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no qa">47.95 ± 2.91 / 71.02 ± 2.28</td> <!-- NorQuAD -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.03 ± 1.95 / 64.06 ± 1.75</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">15=</td> <!-- Rank -->
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="score">44.78 ± 3.29</td> <!-- ScandEval score -->
   <td class="da-score">42.27 ± 3.18</td> <!-- Danish score -->
   <td class="no-score">40.84 ± 3.52</td> <!-- Norwegian score -->
   <td class="sv-score">51.23 ± 3.18</td> <!-- Swedish score -->
   <td class="da ner">45.39 ± 2.46 / 34.45 ± 2.56</td> <!-- DANSK -->
   <td class="da sent">51.95 ± 2.65 / 65.69 ± 2.11</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 6.27 / 45.66 ± 5.58</td> <!-- ScaLA-da -->
   <td class="da qa">58.51 ± 1.35 / 62.73 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="no ner">47.61 ± 2.50 / 42.16 ± 2.82</td> <!-- NorNE-nb -->
   <td class="no ner">60.57 ± 2.02 / 48.89 ± 4.48</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 4.10 / 52.31 ± 4.53</td> <!-- NoReC -->
   <td class="no la">23.99 ± 5.54 / 60.60 ± 2.74</td> <!-- ScaLA-nb -->
   <td class="no la">11.60 ± 3.18 / 53.40 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">47.02 ± 3.37 / 69.07 ± 2.64</td> <!-- NorQuAD -->
   <td class="sv ner">48.36 ± 3.07 / 34.48 ± 5.22</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 2.19 / 78.11 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">20.94 ± 5.55 / 44.72 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.07 ± 1.90 / 63.87 ± 1.46</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="score">44.70 ± 3.06</td> <!-- ScandEval score -->
   <td class="da-score">39.03 ± 2.50</td> <!-- Danish score -->
   <td class="no-score">47.10 ± 4.79</td> <!-- Norwegian score -->
   <td class="sv-score">47.97 ± 1.90</td> <!-- Swedish score -->
   <td class="da ner">69.78 ± 1.59 / 65.83 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">46.78 ± 1.57 / 64.46 ± 1.17</td> <!-- Angry Tweets -->
   <td class="da la">11.27 ± 2.21 / 51.47 ± 2.07</td> <!-- ScaLA-da -->
   <td class="da qa">28.28 ± 4.63 / 33.33 ± 4.10</td> <!-- ScandiQA-da -->
   <td class="no ner">90.14 ± 0.97 / 87.71 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">84.12 ± 1.85 / 80.21 ± 2.19</td> <!-- NorNE-nn -->
   <td class="no sent">44.42 ± 13.10 / 57.73 ± 11.86</td> <!-- NoReC -->
   <td class="no la">11.20 ± 2.99 / 48.77 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">7.12 ± 2.39 / 49.23 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">47.69 ± 1.95 / 62.39 ± 1.74</td> <!-- NorQuAD -->
   <td class="sv ner">79.43 ± 1.07 / 74.17 ± 1.10</td> <!-- SUC3 -->
   <td class="sv sent">71.48 ± 2.63 / 65.72 ± 4.78</td> <!-- SweReC -->
   <td class="sv la">7.26 ± 2.18 / 45.42 ± 4.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.72 ± 1.71 / 38.23 ± 1.57</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="score">44.59 ± 3.02</td> <!-- ScandEval score -->
   <td class="da-score">38.62 ± 3.18</td> <!-- Danish score -->
   <td class="no-score">45.91 ± 3.54</td> <!-- Norwegian score -->
   <td class="sv-score">49.25 ± 2.34</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="score">44.59 ± 3.02</td> <!-- ScandEval score -->
   <td class="da-score">38.62 ± 3.18</td> <!-- Danish score -->
   <td class="no-score">45.91 ± 3.54</td> <!-- Norwegian score -->
   <td class="sv-score">49.25 ± 2.34</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="score">44.21 ± 2.16</td> <!-- ScandEval score -->
   <td class="da-score">31.39 ± 2.10</td> <!-- Danish score -->
   <td class="no-score">36.21 ± 2.90</td> <!-- Norwegian score -->
   <td class="sv-score">65.04 ± 1.47</td> <!-- Swedish score -->
   <td class="da ner">59.37 ± 1.94 / 57.15 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 0.77 / 58.57 ± 0.67</td> <!-- Angry Tweets -->
   <td class="da la">4.61 ± 2.95 / 49.70 ± 2.34</td> <!-- ScaLA-da -->
   <td class="da qa">23.13 ± 2.72 / 28.47 ± 2.30</td> <!-- ScandiQA-da -->
   <td class="no ner">83.23 ± 1.19 / 80.34 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">79.16 ± 1.50 / 75.55 ± 1.69</td> <!-- NorNE-nn -->
   <td class="no sent">33.94 ± 3.74 / 47.96 ± 4.12</td> <!-- NoReC -->
   <td class="no la">9.56 ± 5.01 / 52.24 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">4.16 ± 2.97 / 50.07 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">22.84 ± 2.52 / 33.72 ± 3.11</td> <!-- NorQuAD -->
   <td class="sv ner">79.99 ± 1.32 / 74.07 ± 1.54</td> <!-- SUC3 -->
   <td class="sv sent">76.04 ± 0.97 / 72.61 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">73.52 ± 2.31 / 85.57 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.60 ± 1.30 / 35.83 ± 1.02</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">17</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="score">44.20 ± 3.12</td> <!-- ScandEval score -->
   <td class="da-score">41.34 ± 2.96</td> <!-- Danish score -->
   <td class="no-score">40.33 ± 3.23</td> <!-- Norwegian score -->
   <td class="sv-score">50.94 ± 3.16</td> <!-- Swedish score -->
   <td class="da ner">46.03 ± 3.93 / 34.23 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">49.59 ± 3.26 / 63.45 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">12.72 ± 3.51 / 46.56 ± 5.33</td> <!-- ScaLA-da -->
   <td class="da qa">57.03 ± 1.13 / 61.58 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="no ner">47.26 ± 3.76 / 40.22 ± 3.43</td> <!-- NorNE-nb -->
   <td class="no ner">59.35 ± 2.82 / 45.26 ± 3.91</td> <!-- NorNE-nn -->
   <td class="no sent">54.93 ± 3.49 / 68.45 ± 2.61</td> <!-- NoReC -->
   <td class="no la">9.00 ± 2.87 / 37.53 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">5.26 ± 3.15 / 39.01 ± 3.54</td> <!-- ScaLA-nn -->
   <td class="no qa">45.95 ± 3.12 / 68.00 ± 3.07</td> <!-- NorQuAD -->
   <td class="sv ner">45.12 ± 2.72 / 30.73 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">78.74 ± 2.13 / 80.11 ± 2.64</td> <!-- SweReC -->
   <td class="sv la">19.74 ± 6.09 / 46.97 ± 5.83</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.15 ± 1.71 / 65.22 ± 1.28</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">18=</td> <!-- Rank -->
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="score">43.83 ± 5.12</td> <!-- ScandEval score -->
   <td class="da-score">39.17 ± 4.92</td> <!-- Danish score -->
   <td class="no-score">42.81 ± 5.63</td> <!-- Norwegian score -->
   <td class="sv-score">49.51 ± 4.80</td> <!-- Swedish score -->
   <td class="da ner">68.49 ± 2.09 / 64.72 ± 2.02</td> <!-- DANSK -->
   <td class="da sent">45.60 ± 1.76 / 63.53 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">28.26 ± 11.88 / 55.28 ± 7.93</td> <!-- ScaLA-da -->
   <td class="da qa">14.34 ± 3.95 / 18.60 ± 5.02</td> <!-- ScandiQA-da -->
   <td class="no ner">89.46 ± 1.18 / 86.62 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">79.71 ± 1.02 / 75.64 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">52.91 ± 2.29 / 64.64 ± 3.28</td> <!-- NoReC -->
   <td class="no la">27.55 ± 12.16 / 53.28 ± 8.27</td> <!-- ScaLA-nb -->
   <td class="no la">15.20 ± 9.06 / 51.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">12.36 ± 8.54 / 17.38 ± 11.78</td> <!-- NorQuAD -->
   <td class="sv ner">76.31 ± 1.29 / 70.91 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">73.32 ± 1.13 / 70.21 ± 3.74</td> <!-- SweReC -->
   <td class="sv la">32.29 ± 10.98 / 62.21 ± 5.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.12 ± 5.80 / 19.52 ± 6.73</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">18=</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="score">43.76 ± 2.12</td> <!-- ScandEval score -->
   <td class="da-score">41.52 ± 1.57</td> <!-- Danish score -->
   <td class="no-score">39.83 ± 2.35</td> <!-- Norwegian score -->
   <td class="sv-score">49.95 ± 2.43</td> <!-- Swedish score -->
   <td class="da ner">61.17 ± 2.09 / 58.41 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">46.39 ± 1.25 / 63.97 ± 1.08</td> <!-- Angry Tweets -->
   <td class="da la">38.61 ± 1.86 / 67.08 ± 1.08</td> <!-- ScaLA-da -->
   <td class="da qa">19.90 ± 1.09 / 25.77 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="no ner">81.26 ± 1.25 / 77.69 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.05 ± 1.72 / 69.84 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">49.93 ± 1.46 / 62.37 ± 2.34</td> <!-- NoReC -->
   <td class="no la">38.26 ± 7.56 / 66.01 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">25.17 ± 5.32 / 61.27 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">70.22 ± 1.49 / 63.97 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">71.33 ± 1.20 / 65.44 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">39.60 ± 5.87 / 66.60 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.65 ± 1.15 / 24.75 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">19=</td> <!-- Rank -->
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,002 ± 433 / 989 ± 323</td> <!-- Model inference speed -->
   <td class="score">43.65 ± 2.68</td> <!-- ScandEval score -->
   <td class="da-score">42.93 ± 2.85</td> <!-- Danish score -->
   <td class="no-score">38.63 ± 2.56</td> <!-- Norwegian score -->
   <td class="sv-score">49.39 ± 2.62</td> <!-- Swedish score -->
   <td class="da ner">43.61 ± 2.53 / 32.18 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 2.93 / 50.27 ± 3.75</td> <!-- Angry Tweets -->
   <td class="da la">24.82 ± 4.11 / 49.81 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">60.99 ± 1.82 / 66.38 ± 1.35</td> <!-- ScandiQA-da -->
   <td class="no ner">48.64 ± 1.93 / 37.45 ± 2.79</td> <!-- NorNE-nb -->
   <td class="no ner">58.21 ± 3.05 / 41.03 ± 3.32</td> <!-- NorNE-nn -->
   <td class="no sent">51.25 ± 3.31 / 65.69 ± 2.54</td> <!-- NoReC -->
   <td class="no la">1.60 ± 2.12 / 33.60 ± 0.96</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.34 ± 0.86</td> <!-- ScaLA-nn -->
   <td class="no qa">49.04 ± 3.40 / 71.29 ± 2.63</td> <!-- NorQuAD -->
   <td class="sv ner">47.73 ± 2.68 / 34.21 ± 3.41</td> <!-- SUC3 -->
   <td class="sv sent">75.86 ± 1.94 / 71.26 ± 2.30</td> <!-- SweReC -->
   <td class="sv la">15.31 ± 4.08 / 52.60 ± 3.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.64 ± 1.80 / 63.67 ± 1.24</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">19=</td> <!-- Rank -->
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="score">43.53 ± 2.13</td> <!-- ScandEval score -->
   <td class="da-score">35.03 ± 2.68</td> <!-- Danish score -->
   <td class="no-score">33.88 ± 2.36</td> <!-- Norwegian score -->
   <td class="sv-score">61.67 ± 1.35</td> <!-- Swedish score -->
   <td class="da ner">55.98 ± 2.24 / 52.41 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">36.66 ± 1.27 / 57.48 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">22.69 ± 5.37 / 59.46 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">24.81 ± 1.85 / 29.08 ± 1.74</td> <!-- ScandiQA-da -->
   <td class="no ner">79.25 ± 1.22 / 76.73 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">75.39 ± 1.03 / 71.63 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 3.06 / 51.25 ± 3.01</td> <!-- NoReC -->
   <td class="no la">22.02 ± 5.34 / 57.45 ± 3.59</td> <!-- ScaLA-nb -->
   <td class="no la">19.72 ± 3.67 / 56.70 ± 2.89</td> <!-- ScaLA-nn -->
   <td class="no qa">0.78 ± 0.74 / 1.49 ± 1.32</td> <!-- NorQuAD -->
   <td class="sv ner">75.40 ± 1.45 / 70.45 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">76.22 ± 0.78 / 75.25 ± 1.16</td> <!-- SweReC -->
   <td class="sv la">65.73 ± 1.73 / 81.50 ± 1.14</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.34 ± 1.44 / 34.01 ± 1.50</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">19=</td> <!-- Rank -->
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="score">43.37 ± 1.45</td> <!-- ScandEval score -->
   <td class="da-score">37.10 ± 0.78</td> <!-- Danish score -->
   <td class="no-score">45.06 ± 2.31</td> <!-- Norwegian score -->
   <td class="sv-score">47.96 ± 1.26</td> <!-- Swedish score -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">57.24 ± 0.74 / 63.79 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no qa">49.06 ± 4.30 / 74.35 ± 3.96</td> <!-- NorQuAD -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.13 ± 1.18 / 65.74 ± 0.69</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">20=</td> <!-- Rank -->
   <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="score">43.08 ± 1.64</td> <!-- ScandEval score -->
   <td class="da-score">38.59 ± 1.79</td> <!-- Danish score -->
   <td class="no-score">41.92 ± 1.72</td> <!-- Norwegian score -->
   <td class="sv-score">48.73 ± 1.39</td> <!-- Swedish score -->
   <td class="da ner">58.12 ± 1.30 / 54.97 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">32.53 ± 1.39 / 54.09 ± 1.00</td> <!-- Angry Tweets -->
   <td class="da la">35.53 ± 2.54 / 66.86 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">28.19 ± 1.93 / 32.96 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="no ner">83.62 ± 0.75 / 80.61 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">80.69 ± 0.69 / 76.61 ± 0.81</td> <!-- NorNE-nn -->
   <td class="no sent">33.16 ± 2.13 / 46.93 ± 2.66</td> <!-- NoReC -->
   <td class="no la">36.10 ± 2.45 / 66.11 ± 1.85</td> <!-- ScaLA-nb -->
   <td class="no la">30.10 ± 2.50 / 64.29 ± 1.69</td> <!-- ScaLA-nn -->
   <td class="no qa">19.26 ± 1.57 / 30.04 ± 2.13</td> <!-- NorQuAD -->
   <td class="sv ner">70.08 ± 1.38 / 64.46 ± 1.31</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.22 / 56.16 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">33.71 ± 1.12 / 65.32 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.48 ± 1.85 / 36.44 ± 1.87</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">20=</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="score">42.80 ± 2.35</td> <!-- ScandEval score -->
   <td class="da-score">39.99 ± 2.85</td> <!-- Danish score -->
   <td class="no-score">39.95 ± 1.74</td> <!-- Norwegian score -->
   <td class="sv-score">48.47 ± 2.47</td> <!-- Swedish score -->
   <td class="da ner">61.18 ± 1.22 / 57.94 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">49.13 ± 0.82 / 65.84 ± 0.66</td> <!-- Angry Tweets -->
   <td class="da la">29.66 ± 7.69 / 63.05 ± 4.35</td> <!-- ScaLA-da -->
   <td class="da qa">19.99 ± 1.65 / 26.42 ± 1.77</td> <!-- ScandiQA-da -->
   <td class="no ner">81.94 ± 0.73 / 78.39 ± 0.86</td> <!-- NorNE-nb -->
   <td class="no ner">75.56 ± 1.01 / 71.27 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">55.53 ± 1.05 / 68.89 ± 1.16</td> <!-- NoReC -->
   <td class="no la">36.01 ± 2.02 / 64.39 ± 1.49</td> <!-- ScaLA-nb -->
   <td class="no la">14.99 ± 8.03 / 54.08 ± 5.71</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">65.14 ± 1.57 / 59.82 ± 1.39</td> <!-- SUC3 -->
   <td class="sv sent">73.47 ± 0.84 / 70.20 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 6.55 / 66.09 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.65 ± 0.91 / 25.00 ± 0.87</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">21=</td> <!-- Rank -->
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="score">42.77 ± 1.84</td> <!-- ScandEval score -->
   <td class="da-score">41.28 ± 2.17</td> <!-- Danish score -->
   <td class="no-score">37.91 ± 1.80</td> <!-- Norwegian score -->
   <td class="sv-score">49.13 ± 1.55</td> <!-- Swedish score -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">58.35 ± 0.73 / 64.83 ± 0.45</td> <!-- ScandiQA-da -->
   <td class="no ner">51.99 ± 1.85 / 37.40 ± 2.95</td> <!-- NorNE-nb -->
   <td class="no ner">52.74 ± 1.13 / 36.83 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">50.39 ± 1.38 / 66.42 ± 1.20</td> <!-- NoReC -->
   <td class="no la">0.99 ± 1.03 / 33.56 ± 0.25</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 1.30 / 34.04 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">47.77 ± 3.16 / 72.52 ± 2.51</td> <!-- NorQuAD -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.33 ± 0.94 / 63.73 ± 1.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">21=</td> <!-- Rank -->
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="score">42.66 ± 2.15</td> <!-- ScandEval score -->
   <td class="da-score">38.79 ± 2.60</td> <!-- Danish score -->
   <td class="no-score">38.69 ± 2.29</td> <!-- Norwegian score -->
   <td class="sv-score">50.50 ± 1.56</td> <!-- Swedish score -->
   <td class="da ner">58.52 ± 1.78 / 55.04 ± 1.60</td> <!-- DANSK -->
   <td class="da sent">42.26 ± 1.13 / 61.41 ± 0.76</td> <!-- Angry Tweets -->
   <td class="da la">34.80 ± 5.89 / 64.51 ± 4.90</td> <!-- ScaLA-da -->
   <td class="da qa">19.60 ± 1.60 / 25.68 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">80.08 ± 1.46 / 75.93 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">74.59 ± 1.98 / 70.26 ± 2.24</td> <!-- NorNE-nn -->
   <td class="no sent">52.16 ± 0.99 / 66.79 ± 0.98</td> <!-- NoReC -->
   <td class="no la">36.30 ± 6.44 / 65.52 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">14.21 ± 6.44 / 52.78 ± 5.69</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">68.94 ± 1.53 / 62.54 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 0.89 / 68.13 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">40.21 ± 2.53 / 67.11 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.09 ± 1.31 / 25.99 ± 1.19</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">21=</td> <!-- Rank -->
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,505 ± 465 / 774 ± 242</td> <!-- Model inference speed -->
   <td class="score">42.66 ± 2.20</td> <!-- ScandEval score -->
   <td class="da-score">39.45 ± 2.21</td> <!-- Danish score -->
   <td class="no-score">35.76 ± 2.17</td> <!-- Norwegian score -->
   <td class="sv-score">52.77 ± 2.22</td> <!-- Swedish score -->
   <td class="da ner">41.66 ± 3.23 / 28.72 ± 2.20</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 2.03 / 62.67 ± 2.20</td> <!-- Angry Tweets -->
   <td class="da la">17.36 ± 2.43 / 53.55 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">51.28 ± 1.14 / 56.19 ± 0.93</td> <!-- ScandiQA-da -->
   <td class="no ner">48.28 ± 2.45 / 37.94 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">50.51 ± 2.81 / 38.77 ± 3.26</td> <!-- NorNE-nn -->
   <td class="no sent">49.76 ± 2.62 / 64.69 ± 2.26</td> <!-- NoReC -->
   <td class="no la">14.54 ± 2.23 / 47.43 ± 4.29</td> <!-- ScaLA-nb -->
   <td class="no la">9.16 ± 1.52 / 48.30 ± 3.84</td> <!-- ScaLA-nn -->
   <td class="no qa">32.04 ± 1.57 / 53.75 ± 1.86</td> <!-- NorQuAD -->
   <td class="sv ner">44.16 ± 2.57 / 29.58 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">80.29 ± 1.06 / 80.37 ± 0.72</td> <!-- SweReC -->
   <td class="sv la">34.80 ± 2.22 / 65.44 ± 2.16</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.82 ± 3.03 / 57.01 ± 2.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">22</td> <!-- Rank -->
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="score">42.60 ± 8.52</td> <!-- ScandEval score -->
   <td class="da-score">36.91 ± 10.14</td> <!-- Danish score -->
   <td class="no-score">41.07 ± 7.10</td> <!-- Norwegian score -->
   <td class="sv-score">49.83 ± 8.32</td> <!-- Swedish score -->
   <td class="da ner">43.90 ± 15.70 / 41.25 ± 14.74</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 5.85 / 62.62 ± 4.55</td> <!-- Angry Tweets -->
   <td class="da la">30.37 ± 17.09 / 63.92 ± 8.38</td> <!-- ScaLA-da -->
   <td class="da qa">28.89 ± 1.91 / 33.71 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">71.73 ± 15.69 / 68.50 ± 15.04</td> <!-- NorNE-nb -->
   <td class="no ner">79.80 ± 0.72 / 75.76 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">46.74 ± 5.96 / 60.25 ± 6.04</td> <!-- NoReC -->
   <td class="no la">8.02 ± 12.19 / 50.30 ± 7.19</td> <!-- ScaLA-nb -->
   <td class="no la">17.04 ± 13.78 / 56.87 ± 7.06</td> <!-- ScaLA-nn -->
   <td class="no qa">29.26 ± 1.27 / 42.50 ± 1.17</td> <!-- NorQuAD -->
   <td class="sv ner">58.84 ± 13.92 / 53.63 ± 12.63</td> <!-- SUC3 -->
   <td class="sv sent">72.28 ± 0.79 / 71.62 ± 1.38</td> <!-- SweReC -->
   <td class="sv la">37.61 ± 17.89 / 66.93 ± 9.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.59 ± 0.68 / 35.43 ± 0.61</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="score">42.44 ± 1.99</td> <!-- ScandEval score -->
   <td class="da-score">37.99 ± 2.03</td> <!-- Danish score -->
   <td class="no-score">40.96 ± 2.85</td> <!-- Norwegian score -->
   <td class="sv-score">48.37 ± 1.08</td> <!-- Swedish score -->
   <td class="da ner">58.44 ± 2.08 / 55.32 ± 1.81</td> <!-- DANSK -->
   <td class="da sent">31.81 ± 1.65 / 53.25 ± 1.65</td> <!-- Angry Tweets -->
   <td class="da la">34.13 ± 2.81 / 65.98 ± 2.30</td> <!-- ScaLA-da -->
   <td class="da qa">27.60 ± 1.58 / 32.18 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">83.59 ± 1.36 / 80.55 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">80.29 ± 1.02 / 76.08 ± 1.06</td> <!-- NorNE-nn -->
   <td class="no sent">33.19 ± 1.75 / 46.63 ± 2.55</td> <!-- NoReC -->
   <td class="no la">32.60 ± 6.93 / 65.19 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">24.97 ± 6.47 / 61.39 ± 3.34</td> <!-- ScaLA-nn -->
   <td class="no qa">19.93 ± 1.76 / 30.69 ± 2.36</td> <!-- NorQuAD -->
   <td class="sv ner">70.56 ± 1.36 / 64.49 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">60.69 ± 0.46 / 56.69 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">30.83 ± 1.47 / 63.39 ± 1.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.41 ± 1.05 / 36.45 ± 1.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="score">42.40 ± 1.75</td> <!-- ScandEval score -->
   <td class="da-score">38.22 ± 1.95</td> <!-- Danish score -->
   <td class="no-score">41.29 ± 2.15</td> <!-- Norwegian score -->
   <td class="sv-score">47.68 ± 1.15</td> <!-- Swedish score -->
   <td class="da ner">58.78 ± 1.75 / 55.50 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">31.30 ± 1.80 / 52.43 ± 1.61</td> <!-- Angry Tweets -->
   <td class="da la">34.92 ± 2.74 / 66.69 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">27.86 ± 1.51 / 32.53 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="no ner">83.49 ± 0.83 / 80.32 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">80.23 ± 1.09 / 76.10 ± 1.23</td> <!-- NorNE-nn -->
   <td class="no sent">32.66 ± 1.96 / 46.26 ± 3.19</td> <!-- NoReC -->
   <td class="no la">33.65 ± 6.63 / 65.22 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">29.07 ± 2.20 / 63.35 ± 1.54</td> <!-- ScaLA-nn -->
   <td class="no qa">19.29 ± 1.27 / 29.94 ± 1.81</td> <!-- NorQuAD -->
   <td class="sv ner">69.94 ± 1.11 / 63.93 ± 1.47</td> <!-- SUC3 -->
   <td class="sv sent">59.83 ± 1.11 / 55.15 ± 0.99</td> <!-- SweReC -->
   <td class="sv la">29.82 ± 1.23 / 63.32 ± 1.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.13 ± 1.15 / 36.20 ± 1.22</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="score">42.23 ± 1.59</td> <!-- ScandEval score -->
   <td class="da-score">37.83 ± 1.66</td> <!-- Danish score -->
   <td class="no-score">41.71 ± 1.64</td> <!-- Norwegian score -->
   <td class="sv-score">47.15 ± 1.47</td> <!-- Swedish score -->
   <td class="da ner">57.53 ± 1.89 / 54.43 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">32.95 ± 0.82 / 54.57 ± 0.80</td> <!-- Angry Tweets -->
   <td class="da la">33.63 ± 2.63 / 65.69 ± 1.82</td> <!-- ScaLA-da -->
   <td class="da qa">27.21 ± 1.31 / 32.05 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">83.93 ± 0.95 / 81.01 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">79.39 ± 1.03 / 75.07 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">32.32 ± 2.30 / 47.12 ± 2.85</td> <!-- NoReC -->
   <td class="no la">36.15 ± 1.99 / 66.57 ± 1.11</td> <!-- ScaLA-nb -->
   <td class="no la">30.17 ± 1.72 / 63.98 ± 1.36</td> <!-- ScaLA-nn -->
   <td class="no qa">19.71 ± 1.41 / 30.26 ± 1.56</td> <!-- NorQuAD -->
   <td class="sv ner">69.28 ± 1.15 / 63.61 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">59.53 ± 1.69 / 57.93 ± 2.20</td> <!-- SweReC -->
   <td class="sv la">29.36 ± 1.50 / 63.60 ± 0.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.42 ± 1.54 / 35.34 ± 1.63</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="score">41.91 ± 1.92</td> <!-- ScandEval score -->
   <td class="da-score">38.95 ± 1.64</td> <!-- Danish score -->
   <td class="no-score">39.30 ± 2.82</td> <!-- Norwegian score -->
   <td class="sv-score">47.47 ± 1.31</td> <!-- Swedish score -->
   <td class="da ner">59.50 ± 1.45 / 56.28 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">31.89 ± 1.59 / 53.99 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">36.00 ± 2.27 / 67.38 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.41 ± 1.26 / 33.19 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">83.27 ± 1.20 / 80.29 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">79.59 ± 0.97 / 75.31 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">29.37 ± 2.58 / 44.05 ± 3.33</td> <!-- NoReC -->
   <td class="no la">31.50 ± 6.37 / 64.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">24.06 ± 7.24 / 61.01 ± 3.82</td> <!-- ScaLA-nn -->
   <td class="no qa">18.62 ± 0.81 / 29.69 ± 1.81</td> <!-- NorQuAD -->
   <td class="sv ner">69.62 ± 0.88 / 63.51 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">59.42 ± 1.21 / 55.74 ± 1.26</td> <!-- SweReC -->
   <td class="sv la">29.01 ± 2.06 / 62.65 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.82 ± 1.07 / 36.82 ± 1.14</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="score">41.63 ± 1.61</td> <!-- ScandEval score -->
   <td class="da-score">38.19 ± 1.49</td> <!-- Danish score -->
   <td class="no-score">39.67 ± 1.94</td> <!-- Norwegian score -->
   <td class="sv-score">47.03 ± 1.39</td> <!-- Swedish score -->
   <td class="da ner">58.36 ± 1.69 / 55.30 ± 1.49</td> <!-- DANSK -->
   <td class="da sent">32.13 ± 1.52 / 53.89 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">34.75 ± 1.55 / 65.89 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">27.50 ± 1.21 / 32.16 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="no ner">82.84 ± 0.61 / 79.91 ± 0.64</td> <!-- NorNE-nb -->
   <td class="no ner">78.83 ± 1.18 / 74.64 ± 1.40</td> <!-- NorNE-nn -->
   <td class="no sent">30.70 ± 2.63 / 43.77 ± 2.62</td> <!-- NoReC -->
   <td class="no la">34.24 ± 2.30 / 65.60 ± 1.50</td> <!-- ScaLA-nb -->
   <td class="no la">27.20 ± 2.61 / 62.87 ± 1.41</td> <!-- ScaLA-nn -->
   <td class="no qa">16.44 ± 1.76 / 26.22 ± 2.65</td> <!-- NorQuAD -->
   <td class="sv ner">69.25 ± 1.37 / 63.90 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">58.47 ± 1.30 / 56.03 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">29.80 ± 1.57 / 63.53 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.61 ± 1.31 / 35.37 ± 1.52</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">23=</td> <!-- Rank -->
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="score">41.63 ± 3.55</td> <!-- ScandEval score -->
   <td class="da-score">43.36 ± 3.05</td> <!-- Danish score -->
   <td class="no-score">39.98 ± 3.98</td> <!-- Norwegian score -->
   <td class="sv-score">41.56 ± 3.60</td> <!-- Swedish score -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da qa">58.16 ± 1.29 / 63.63 ± 0.95</td> <!-- ScandiQA-da -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">41.18 ± 3.00 / 66.43 ± 2.76</td> <!-- NorQuAD -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.03 ± 1.52 / 64.13 ± 1.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">24=</td> <!-- Rank -->
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="score">40.91 ± 1.89</td> <!-- ScandEval score -->
   <td class="da-score">47.30 ± 1.83</td> <!-- Danish score -->
   <td class="no-score">36.92 ± 1.85</td> <!-- Norwegian score -->
   <td class="sv-score">38.50 ± 1.99</td> <!-- Swedish score -->
   <td class="da ner">64.28 ± 1.74 / 59.29 ± 1.54</td> <!-- DANSK -->
   <td class="da sent">36.85 ± 3.28 / 56.27 ± 3.98</td> <!-- Angry Tweets -->
   <td class="da la">63.55 ± 1.19 / 81.41 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">24.52 ± 1.11 / 29.88 ± 1.13</td> <!-- ScandiQA-da -->
   <td class="no ner">79.50 ± 0.70 / 76.09 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">73.03 ± 1.28 / 68.84 ± 1.39</td> <!-- NorNE-nn -->
   <td class="no sent">32.40 ± 1.48 / 44.59 ± 1.66</td> <!-- NoReC -->
   <td class="no la">41.65 ± 1.95 / 70.35 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">25.53 ± 2.31 / 62.04 ± 1.19</td> <!-- ScaLA-nn -->
   <td class="no qa">5.41 ± 2.79 / 8.15 ± 4.18</td> <!-- NorQuAD -->
   <td class="sv ner">58.01 ± 1.23 / 53.87 ± 1.25</td> <!-- SUC3 -->
   <td class="sv sent">57.67 ± 1.61 / 53.64 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">13.40 ± 4.31 / 55.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.92 ± 0.80 / 30.11 ± 0.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">24=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="score">40.78 ± 2.12</td> <!-- ScandEval score -->
   <td class="da-score">38.61 ± 2.17</td> <!-- Danish score -->
   <td class="no-score">36.26 ± 2.42</td> <!-- Norwegian score -->
   <td class="sv-score">47.46 ± 1.78</td> <!-- Swedish score -->
   <td class="da ner">43.17 ± 2.78 / 31.37 ± 2.95</td> <!-- DANSK -->
   <td class="da sent">43.40 ± 2.20 / 57.24 ± 3.52</td> <!-- Angry Tweets -->
   <td class="da la">11.08 ± 2.98 / 43.40 ± 4.66</td> <!-- ScaLA-da -->
   <td class="da qa">56.81 ± 0.70 / 63.10 ± 0.35</td> <!-- ScandiQA-da -->
   <td class="no ner">58.61 ± 1.58 / 47.74 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">60.40 ± 1.25 / 47.53 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">41.36 ± 3.50 / 58.47 ± 3.79</td> <!-- NoReC -->
   <td class="no la">6.52 ± 2.11 / 38.10 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 2.52 / 42.37 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">38.93 ± 2.43 / 65.76 ± 3.07</td> <!-- NorQuAD -->
   <td class="sv ner">50.85 ± 2.44 / 39.65 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">74.17 ± 2.12 / 76.62 ± 1.83</td> <!-- SweReC -->
   <td class="sv la">7.51 ± 1.94 / 37.81 ± 1.76</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.32 ± 0.63 / 63.28 ± 0.71</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">24=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="score">40.76 ± 1.93</td> <!-- ScandEval score -->
   <td class="da-score">40.88 ± 1.74</td> <!-- Danish score -->
   <td class="no-score">35.59 ± 2.12</td> <!-- Norwegian score -->
   <td class="sv-score">45.82 ± 1.92</td> <!-- Swedish score -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da qa">51.49 ± 1.17 / 60.76 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no qa">35.68 ± 2.46 / 64.20 ± 2.43</td> <!-- NorQuAD -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.50 ± 0.34 / 61.43 ± 0.56</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">25</td> <!-- Rank -->
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,161 ± 1,201 / 1,151 ± 376</td> <!-- Model inference speed -->
   <td class="score">40.72 ± 2.31</td> <!-- ScandEval score -->
   <td class="da-score">39.63 ± 2.30</td> <!-- Danish score -->
   <td class="no-score">33.37 ± 3.12</td> <!-- Norwegian score -->
   <td class="sv-score">49.16 ± 1.51</td> <!-- Swedish score -->
   <td class="da ner">46.30 ± 2.54 / 30.32 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">45.44 ± 1.76 / 59.21 ± 2.03</td> <!-- Angry Tweets -->
   <td class="da la">8.46 ± 4.07 / 37.89 ± 2.91</td> <!-- ScaLA-da -->
   <td class="da qa">58.33 ± 0.82 / 63.88 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">54.34 ± 2.57 / 43.19 ± 2.92</td> <!-- NorNE-nb -->
   <td class="no ner">55.98 ± 2.46 / 43.36 ± 2.98</td> <!-- NorNE-nn -->
   <td class="no sent">45.04 ± 3.29 / 62.68 ± 2.97</td> <!-- NoReC -->
   <td class="no la">2.22 ± 1.46 / 34.78 ± 0.95</td> <!-- ScaLA-nb -->
   <td class="no la">2.52 ± 2.47 / 35.88 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">30.90 ± 4.69 / 59.06 ± 4.25</td> <!-- NorQuAD -->
   <td class="sv ner">54.45 ± 2.98 / 39.71 ± 4.87</td> <!-- SUC3 -->
   <td class="sv sent">80.20 ± 0.57 / 80.03 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">3.78 ± 1.59 / 34.07 ± 0.58</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.21 ± 0.90 / 64.03 ± 0.67</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">26=</td> <!-- Rank -->
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="score">40.23 ± 1.72</td> <!-- ScandEval score -->
   <td class="da-score">31.25 ± 1.82</td> <!-- Danish score -->
   <td class="no-score">31.65 ± 1.81</td> <!-- Norwegian score -->
   <td class="sv-score">57.79 ± 1.54</td> <!-- Swedish score -->
   <td class="da ner">57.84 ± 1.47 / 54.75 ± 1.23</td> <!-- DANSK -->
   <td class="da sent">31.18 ± 0.94 / 53.05 ± 1.16</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 3.71 / 53.61 ± 2.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.73 ± 1.16 / 27.50 ± 1.00</td> <!-- ScandiQA-da -->
   <td class="no ner">81.82 ± 0.85 / 78.30 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">75.89 ± 1.11 / 72.08 ± 1.15</td> <!-- NorNE-nn -->
   <td class="no sent">33.42 ± 1.96 / 48.63 ± 3.34</td> <!-- NoReC -->
   <td class="no la">14.99 ± 4.11 / 52.87 ± 4.48</td> <!-- ScaLA-nb -->
   <td class="no la">13.63 ± 4.52 / 53.34 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">80.12 ± 1.41 / 73.78 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">71.28 ± 1.09 / 69.73 ± 2.94</td> <!-- SweReC -->
   <td class="sv la">51.58 ± 2.89 / 73.82 ± 2.21</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.16 ± 0.76 / 33.47 ± 0.62</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">26=</td> <!-- Rank -->
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="score">39.54 ± 4.86</td> <!-- ScandEval score -->
   <td class="da-score">36.67 ± 3.73</td> <!-- Danish score -->
   <td class="no-score">34.32 ± 5.44</td> <!-- Norwegian score -->
   <td class="sv-score">47.61 ± 5.40</td> <!-- Swedish score -->
   <td class="da ner">66.39 ± 1.42 / 62.24 ± 1.29</td> <!-- DANSK -->
   <td class="da sent">39.36 ± 3.13 / 58.64 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">7.06 ± 6.11 / 49.71 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">33.88 ± 4.27 / 38.42 ± 4.16</td> <!-- ScandiQA-da -->
   <td class="no ner">86.26 ± 0.71 / 83.48 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">80.10 ± 2.44 / 76.17 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">34.17 ± 2.42 / 43.74 ± 2.19</td> <!-- NoReC -->
   <td class="no la">12.11 ± 10.47 / 50.33 ± 7.16</td> <!-- ScaLA-nb -->
   <td class="no la">4.28 ± 4.18 / 45.75 ± 4.32</td> <!-- ScaLA-nn -->
   <td class="no qa">11.74 ± 10.45 / 16.38 ± 14.33</td> <!-- NorQuAD -->
   <td class="sv ner">74.26 ± 1.65 / 68.20 ± 1.70</td> <!-- SUC3 -->
   <td class="sv sent">63.35 ± 5.43 / 60.33 ± 5.50</td> <!-- SweReC -->
   <td class="sv la">16.07 ± 10.73 / 52.48 ± 7.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.77 ± 3.78 / 41.72 ± 3.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">27=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">39.39 ± 2.38</td> <!-- ScandEval score -->
   <td class="da-score">36.98 ± 2.64</td> <!-- Danish score -->
   <td class="no-score">35.70 ± 2.24</td> <!-- Norwegian score -->
   <td class="sv-score">45.50 ± 2.25</td> <!-- Swedish score -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.42 ± 2.35 / 58.76 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.31 ± 3.13 / 63.71 ± 2.98</td> <!-- NorQuAD -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.05 ± 1.44 / 59.27 ± 1.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">27=</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="score">39.39 ± 1.70</td> <!-- ScandEval score -->
   <td class="da-score">36.46 ± 1.54</td> <!-- Danish score -->
   <td class="no-score">35.88 ± 1.39</td> <!-- Norwegian score -->
   <td class="sv-score">45.84 ± 2.16</td> <!-- Swedish score -->
   <td class="da ner">56.75 ± 1.91 / 53.43 ± 1.87</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 1.32 / 63.11 ± 0.83</td> <!-- Angry Tweets -->
   <td class="da la">26.74 ± 1.94 / 62.19 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da qa">17.89 ± 1.00 / 25.53 ± 1.05</td> <!-- ScandiQA-da -->
   <td class="no ner">78.31 ± 1.22 / 74.65 ± 1.36</td> <!-- NorNE-nb -->
   <td class="no ner">72.13 ± 0.90 / 67.28 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">47.53 ± 0.94 / 62.73 ± 1.07</td> <!-- NoReC -->
   <td class="no la">26.92 ± 3.12 / 61.93 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.63 ± 4.00 / 56.24 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">66.50 ± 1.49 / 59.99 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">72.19 ± 0.71 / 67.88 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">28.75 ± 5.58 / 63.30 ± 2.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">15.91 ± 0.87 / 23.08 ± 0.95</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">27=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">39.19 ± 2.70</td> <!-- ScandEval score -->
   <td class="da-score">36.47 ± 2.48</td> <!-- Danish score -->
   <td class="no-score">34.50 ± 3.09</td> <!-- Norwegian score -->
   <td class="sv-score">46.60 ± 2.53</td> <!-- Swedish score -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">48.51 ± 2.11 / 53.66 ± 2.06</td> <!-- ScandiQA-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">29.44 ± 2.86 / 50.68 ± 3.91</td> <!-- NorQuAD -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.43 ± 4.69 / 54.33 ± 4.56</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">27=</td> <!-- Rank -->
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="score">38.91 ± 2.08</td> <!-- ScandEval score -->
   <td class="da-score">39.76 ± 1.98</td> <!-- Danish score -->
   <td class="no-score">33.30 ± 2.00</td> <!-- Norwegian score -->
   <td class="sv-score">43.68 ± 2.26</td> <!-- Swedish score -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">46.93 ± 1.12 / 55.22 ± 1.34</td> <!-- ScandiQA-da -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">25.79 ± 1.43 / 50.84 ± 1.80</td> <!-- NorQuAD -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.44 ± 1.45 / 57.11 ± 1.41</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">27=</td> <!-- Rank -->
   <td>danish-foundation-models/encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="score">38.23 ± 2.79</td> <!-- ScandEval score -->
   <td class="da-score">45.02 ± 4.07</td> <!-- Danish score -->
   <td class="no-score">35.66 ± 2.44</td> <!-- Norwegian score -->
   <td class="sv-score">34.00 ± 1.85</td> <!-- Swedish score -->
   <td class="da ner">63.42 ± 1.89 / 58.69 ± 2.54</td> <!-- DANSK -->
   <td class="da sent">39.91 ± 1.78 / 58.47 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">51.01 ± 10.50 / 74.54 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da qa">25.76 ± 2.11 / 31.49 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">68.66 ± 1.05 / 65.08 ± 1.07</td> <!-- NorNE-nb -->
   <td class="no ner">61.77 ± 2.03 / 57.87 ± 2.08</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 1.53 / 51.54 ± 2.45</td> <!-- NoReC -->
   <td class="no la">31.23 ± 6.86 / 63.55 ± 5.48</td> <!-- ScaLA-nb -->
   <td class="no la">5.40 ± 4.63 / 44.64 ± 6.37</td> <!-- ScaLA-nn -->
   <td class="no qa">22.56 ± 0.95 / 34.52 ± 1.15</td> <!-- NorQuAD -->
   <td class="sv ner">49.62 ± 2.01 / 46.05 ± 2.11</td> <!-- SUC3 -->
   <td class="sv sent">58.70 ± 2.54 / 58.15 ± 3.35</td> <!-- SweReC -->
   <td class="sv la">2.23 ± 2.12 / 46.43 ± 4.85</td> <!-- ScaLA-sv -->
   <td class="sv qa">25.45 ± 0.75 / 30.80 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">28</td> <!-- Rank -->
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="score">38.07 ± 2.48</td> <!-- ScandEval score -->
   <td class="da-score">32.06 ± 2.17</td> <!-- Danish score -->
   <td class="no-score">35.05 ± 3.61</td> <!-- Norwegian score -->
   <td class="sv-score">47.12 ± 1.67</td> <!-- Swedish score -->
   <td class="da ner">56.36 ± 1.95 / 53.98 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">31.16 ± 2.06 / 52.25 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">21.08 ± 2.54 / 56.96 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">19.63 ± 2.13 / 23.61 ± 2.07</td> <!-- ScandiQA-da -->
   <td class="no ner">82.98 ± 1.32 / 79.80 ± 1.69</td> <!-- NorNE-nb -->
   <td class="no ner">76.65 ± 1.24 / 72.29 ± 1.44</td> <!-- NorNE-nn -->
   <td class="no sent">30.38 ± 2.29 / 42.84 ± 2.38</td> <!-- NoReC -->
   <td class="no la">21.99 ± 6.74 / 54.54 ± 7.12</td> <!-- ScaLA-nb -->
   <td class="no la">19.06 ± 4.26 / 56.45 ± 5.24</td> <!-- ScaLA-nn -->
   <td class="no qa">9.47 ± 5.36 / 15.24 ± 8.64</td> <!-- NorQuAD -->
   <td class="sv ner">73.41 ± 1.54 / 66.98 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">62.10 ± 1.18 / 60.27 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">34.86 ± 1.29 / 66.98 ± 0.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.10 ± 2.67 / 21.09 ± 3.18</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">29=</td> <!-- Rank -->
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="score">38.05 ± 2.54</td> <!-- ScandEval score -->
   <td class="da-score">44.97 ± 3.18</td> <!-- Danish score -->
   <td class="no-score">36.99 ± 2.35</td> <!-- Norwegian score -->
   <td class="sv-score">32.20 ± 2.10</td> <!-- Swedish score -->
   <td class="da ner">64.64 ± 1.72 / 59.54 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.38 / 62.33 ± 1.20</td> <!-- Angry Tweets -->
   <td class="da la">47.47 ± 8.03 / 70.55 ± 4.26</td> <!-- ScaLA-da -->
   <td class="da qa">23.14 ± 1.59 / 29.91 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">71.69 ± 0.92 / 68.09 ± 0.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.00 ± 1.99 / 56.64 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">38.94 ± 2.59 / 53.58 ± 3.33</td> <!-- NoReC -->
   <td class="no la">30.32 ± 4.68 / 62.42 ± 3.11</td> <!-- ScaLA-nb -->
   <td class="no la">7.99 ± 3.34 / 53.24 ± 1.64</td> <!-- ScaLA-nn -->
   <td class="no qa">24.02 ± 1.35 / 37.28 ± 1.24</td> <!-- NorQuAD -->
   <td class="sv ner">48.32 ± 1.62 / 45.04 ± 1.50</td> <!-- SUC3 -->
   <td class="sv sent">53.98 ± 2.05 / 52.94 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">3.33 ± 2.12 / 51.06 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">23.15 ± 2.61 / 29.17 ± 2.19</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">29=</td> <!-- Rank -->
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="score">37.93 ± 1.46</td> <!-- ScandEval score -->
   <td class="da-score">43.66 ± 1.38</td> <!-- Danish score -->
   <td class="no-score">33.65 ± 1.56</td> <!-- Norwegian score -->
   <td class="sv-score">36.49 ± 1.44</td> <!-- Swedish score -->
   <td class="da ner">60.63 ± 1.32 / 56.90 ± 1.49</td> <!-- DANSK -->
   <td class="da sent">24.38 ± 1.74 / 40.85 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">68.58 ± 1.38 / 84.12 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">21.03 ± 1.09 / 27.53 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="no ner">73.15 ± 1.21 / 70.05 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">66.34 ± 1.25 / 62.07 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">29.97 ± 0.99 / 42.12 ± 0.47</td> <!-- NoReC -->
   <td class="no la">40.79 ± 2.06 / 69.48 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">25.08 ± 1.86 / 61.74 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">1.93 ± 2.05 / 3.62 ± 3.99</td> <!-- NorQuAD -->
   <td class="sv ner">52.79 ± 1.21 / 48.47 ± 0.71</td> <!-- SUC3 -->
   <td class="sv sent">57.93 ± 1.56 / 53.71 ± 0.61</td> <!-- SweReC -->
   <td class="sv la">14.72 ± 2.01 / 55.92 ± 1.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.54 ± 0.97 / 26.37 ± 0.75</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">29=</td> <!-- Rank -->
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="score">37.74 ± 3.87</td> <!-- ScandEval score -->
   <td class="da-score">29.82 ± 3.42</td> <!-- Danish score -->
   <td class="no-score">28.56 ± 3.10</td> <!-- Norwegian score -->
   <td class="sv-score">54.84 ± 5.09</td> <!-- Swedish score -->
   <td class="da ner">49.22 ± 1.85 / 47.83 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">33.51 ± 1.46 / 54.93 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">12.08 ± 8.71 / 54.24 ± 4.71</td> <!-- ScaLA-da -->
   <td class="da qa">24.49 ± 1.67 / 28.88 ± 1.71</td> <!-- ScandiQA-da -->
   <td class="no ner">72.74 ± 2.03 / 69.79 ± 2.34</td> <!-- NorNE-nb -->
   <td class="no ner">69.74 ± 1.81 / 65.59 ± 2.06</td> <!-- NorNE-nn -->
   <td class="no sent">29.68 ± 1.91 / 43.64 ± 2.18</td> <!-- NoReC -->
   <td class="no la">15.83 ± 10.06 / 55.51 ± 5.25</td> <!-- ScaLA-nb -->
   <td class="no la">8.70 ± 4.78 / 52.69 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">1.04 ± 1.17 / 1.93 ± 2.12</td> <!-- NorQuAD -->
   <td class="sv ner">68.55 ± 3.16 / 62.00 ± 2.58</td> <!-- SUC3 -->
   <td class="sv sent">69.96 ± 1.75 / 68.67 ± 3.21</td> <!-- SweReC -->
   <td class="sv la">52.88 ± 14.23 / 75.25 ± 7.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">27.99 ± 1.23 / 32.49 ± 1.27</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">29=</td> <!-- Rank -->
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="score">37.33 ± 1.78</td> <!-- ScandEval score -->
   <td class="da-score">45.69 ± 2.20</td> <!-- Danish score -->
   <td class="no-score">32.11 ± 1.63</td> <!-- Norwegian score -->
   <td class="sv-score">34.20 ± 1.50</td> <!-- Swedish score -->
   <td class="da ner">66.71 ± 1.80 / 61.55 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">43.79 ± 1.76 / 62.26 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">45.96 ± 2.91 / 69.62 ± 1.72</td> <!-- ScaLA-da -->
   <td class="da qa">26.29 ± 2.34 / 32.91 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="no ner">72.62 ± 0.81 / 69.33 ± 0.93</td> <!-- NorNE-nb -->
   <td class="no ner">58.73 ± 1.81 / 55.12 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">40.65 ± 1.63 / 55.20 ± 2.63</td> <!-- NoReC -->
   <td class="no la">29.47 ± 2.30 / 62.25 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">12.95 ± 3.01 / 55.31 ± 1.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.91 ± 0.93 / 2.56 ± 2.15</td> <!-- NorQuAD -->
   <td class="sv ner">50.29 ± 1.22 / 47.15 ± 1.18</td> <!-- SUC3 -->
   <td class="sv sent">57.42 ± 1.88 / 56.53 ± 1.66</td> <!-- SweReC -->
   <td class="sv la">4.94 ± 1.62 / 51.57 ± 1.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.16 ± 1.28 / 30.28 ± 1.18</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">29=</td> <!-- Rank -->
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="score">37.26 ± 1.78</td> <!-- ScandEval score -->
   <td class="da-score">41.84 ± 1.87</td> <!-- Danish score -->
   <td class="no-score">34.03 ± 1.83</td> <!-- Norwegian score -->
   <td class="sv-score">35.92 ± 1.63</td> <!-- Swedish score -->
   <td class="da ner">60.59 ± 1.84 / 57.31 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">29.52 ± 2.89 / 47.81 ± 4.54</td> <!-- Angry Tweets -->
   <td class="da la">57.10 ± 2.02 / 78.14 ± 1.10</td> <!-- ScaLA-da -->
   <td class="da qa">20.16 ± 0.73 / 25.69 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="no ner">76.07 ± 1.18 / 72.78 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">70.94 ± 1.19 / 66.73 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">32.49 ± 1.55 / 43.12 ± 0.71</td> <!-- NoReC -->
   <td class="no la">35.43 ± 2.39 / 66.84 ± 1.17</td> <!-- ScaLA-nb -->
   <td class="no la">21.11 ± 1.97 / 60.09 ± 0.93</td> <!-- ScaLA-nn -->
   <td class="no qa">1.84 ± 2.41 / 2.78 ± 3.65</td> <!-- NorQuAD -->
   <td class="sv ner">55.06 ± 0.96 / 51.37 ± 1.03</td> <!-- SUC3 -->
   <td class="sv sent">53.70 ± 1.46 / 51.98 ± 0.58</td> <!-- SweReC -->
   <td class="sv la">12.38 ± 3.23 / 55.18 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">22.53 ± 0.86 / 27.59 ± 0.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="score">36.87 ± 2.24</td> <!-- ScandEval score -->
   <td class="da-score">31.49 ± 1.75</td> <!-- Danish score -->
   <td class="no-score">40.70 ± 2.82</td> <!-- Norwegian score -->
   <td class="sv-score">38.44 ± 2.14</td> <!-- Swedish score -->
   <td class="da ner">59.94 ± 2.06 / 58.86 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">39.16 ± 1.75 / 58.91 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.16 ± 1.61 / 48.93 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">24.69 ± 1.58 / 28.57 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="no ner">87.63 ± 0.64 / 84.17 ± 0.81</td> <!-- NorNE-nb -->
   <td class="no ner">80.19 ± 2.00 / 75.70 ± 2.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.92 ± 1.44 / 63.75 ± 1.45</td> <!-- NoReC -->
   <td class="no la">7.93 ± 4.24 / 50.87 ± 2.29</td> <!-- ScaLA-nb -->
   <td class="no la">5.06 ± 0.83 / 51.44 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">22.46 ± 5.97 / 34.67 ± 8.87</td> <!-- NorQuAD -->
   <td class="sv ner">67.53 ± 1.66 / 62.96 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">59.27 ± 2.14 / 55.26 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.83 ± 2.01 / 49.25 ± 1.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.11 ± 2.76 / 27.79 ± 2.63</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="score">36.83 ± 3.31</td> <!-- ScandEval score -->
   <td class="da-score">37.96 ± 4.58</td> <!-- Danish score -->
   <td class="no-score">32.72 ± 3.80</td> <!-- Norwegian score -->
   <td class="sv-score">39.81 ± 1.54</td> <!-- Swedish score -->
   <td class="da ner">63.84 ± 1.73 / 59.85 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">43.90 ± 1.50 / 62.31 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">17.16 ± 13.94 / 56.47 ± 7.34</td> <!-- ScaLA-da -->
   <td class="da qa">26.94 ± 1.16 / 31.50 ± 1.03</td> <!-- ScandiQA-da -->
   <td class="no ner">76.14 ± 2.58 / 72.24 ± 2.54</td> <!-- NorNE-nb -->
   <td class="no ner">72.88 ± 1.50 / 68.61 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 9.23 / 49.08 ± 8.36</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.61 / 49.14 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">-0.08 ± 1.79 / 45.89 ± 3.49</td> <!-- ScaLA-nn -->
   <td class="no qa">23.91 ± 2.24 / 36.47 ± 2.77</td> <!-- NorQuAD -->
   <td class="sv ner">65.95 ± 1.70 / 60.53 ± 1.38</td> <!-- SUC3 -->
   <td class="sv sent">64.02 ± 2.78 / 62.27 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">0.80 ± 0.78 / 47.24 ± 3.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.46 ± 0.90 / 33.13 ± 0.88</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">36.47 ± 2.17</td> <!-- ScandEval score -->
   <td class="da-score">36.27 ± 1.80</td> <!-- Danish score -->
   <td class="no-score">31.47 ± 2.58</td> <!-- Norwegian score -->
   <td class="sv-score">41.68 ± 2.14</td> <!-- Swedish score -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.00 ± 0.79 / 61.31 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.76 ± 2.07 / 61.97 ± 2.31</td> <!-- NorQuAD -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.07 ± 0.84 / 60.93 ± 0.80</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="score">36.39 ± 3.52</td> <!-- ScandEval score -->
   <td class="da-score">34.15 ± 3.21</td> <!-- Danish score -->
   <td class="no-score">31.64 ± 3.95</td> <!-- Norwegian score -->
   <td class="sv-score">43.37 ± 3.40</td> <!-- Swedish score -->
   <td class="da ner">30.16 ± 4.47 / 25.03 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">48.49 ± 2.41 / 63.06 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">5.52 ± 4.66 / 38.81 ± 4.27</td> <!-- ScaLA-da -->
   <td class="da qa">52.44 ± 1.32 / 57.22 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="no ner">35.98 ± 3.79 / 27.51 ± 2.13</td> <!-- NorNE-nb -->
   <td class="no ner">47.39 ± 2.31 / 36.42 ± 2.87</td> <!-- NorNE-nn -->
   <td class="no sent">38.98 ± 5.51 / 58.23 ± 4.01</td> <!-- NoReC -->
   <td class="no la">11.54 ± 5.04 / 49.91 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">5.20 ± 3.47 / 46.19 ± 5.23</td> <!-- ScaLA-nn -->
   <td class="no qa">37.54 ± 3.00 / 56.56 ± 2.96</td> <!-- NorQuAD -->
   <td class="sv ner">32.37 ± 3.05 / 24.60 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">75.33 ± 2.41 / 77.99 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">12.73 ± 6.32 / 45.51 ± 7.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.05 ± 1.83 / 58.32 ± 1.46</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">35.39 ± 2.66</td> <!-- ScandEval score -->
   <td class="da-score">30.45 ± 2.59</td> <!-- Danish score -->
   <td class="no-score">31.58 ± 3.00</td> <!-- Norwegian score -->
   <td class="sv-score">44.14 ± 2.40</td> <!-- Swedish score -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.24 ± 3.46 / 41.07 ± 4.41</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da qa">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.51 ± 1.27 / 42.18 ± 1.39</td> <!-- NoReC -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no qa">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">78.88 ± 1.58 / 79.56 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,035 ± 84 / 4,068 ± 1,290</td> <!-- Model inference speed -->
   <td class="score">35.23 ± 1.24</td> <!-- ScandEval score -->
   <td class="da-score">40.94 ± 1.50</td> <!-- Danish score -->
   <td class="no-score">31.55 ± 1.15</td> <!-- Norwegian score -->
   <td class="sv-score">33.19 ± 1.07</td> <!-- Swedish score -->
   <td class="da ner">63.31 ± 1.75 / 58.18 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">32.72 ± 2.91 / 49.84 ± 4.90</td> <!-- Angry Tweets -->
   <td class="da la">67.74 ± 1.33 / 83.32 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">71.85 ± 1.11 / 68.20 ± 1.23</td> <!-- NorNE-nb -->
   <td class="no ner">67.14 ± 1.18 / 62.61 ± 1.22</td> <!-- NorNE-nn -->
   <td class="no sent">29.00 ± 1.28 / 41.72 ± 0.52</td> <!-- NoReC -->
   <td class="no la">33.57 ± 2.58 / 65.22 ± 1.59</td> <!-- ScaLA-nb -->
   <td class="no la">21.79 ± 1.60 / 60.32 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">0.03 ± 0.07 / 0.05 ± 0.10</td> <!-- NorQuAD -->
   <td class="sv ner">57.82 ± 1.40 / 54.55 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">55.68 ± 1.09 / 52.81 ± 0.44</td> <!-- SweReC -->
   <td class="sv la">19.26 ± 1.80 / 58.62 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">30=</td> <!-- Rank -->
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="score">34.97 ± 2.53</td> <!-- ScandEval score -->
   <td class="da-score">32.69 ± 2.02</td> <!-- Danish score -->
   <td class="no-score">28.16 ± 3.06</td> <!-- Norwegian score -->
   <td class="sv-score">44.08 ± 2.52</td> <!-- Swedish score -->
   <td class="da ner">37.80 ± 2.75 / 24.74 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">40.51 ± 1.75 / 55.84 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">3.35 ± 1.84 / 44.60 ± 4.67</td> <!-- ScaLA-da -->
   <td class="da qa">49.08 ± 1.74 / 55.58 ± 1.57</td> <!-- ScandiQA-da -->
   <td class="no ner">42.29 ± 4.36 / 31.45 ± 1.88</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 3.44 / 35.99 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">27.05 ± 3.33 / 45.30 ± 3.46</td> <!-- NoReC -->
   <td class="no la">1.63 ± 2.58 / 38.29 ± 4.05</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 40.92 ± 4.00</td> <!-- ScaLA-nn -->
   <td class="no qa">39.18 ± 2.84 / 61.85 ± 3.07</td> <!-- NorQuAD -->
   <td class="sv ner">48.78 ± 5.08 / 26.81 ± 3.42</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 1.23 / 74.78 ± 1.97</td> <!-- SweReC -->
   <td class="sv la">2.53 ± 2.80 / 47.37 ± 2.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.93 ± 0.97 / 55.09 ± 0.85</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,019 ± 480 / 1,048 ± 317</td> <!-- Model inference speed -->
   <td class="score">34.76 ± 3.15</td> <!-- ScandEval score -->
   <td class="da-score">35.42 ± 3.70</td> <!-- Danish score -->
   <td class="no-score">25.42 ± 3.32</td> <!-- Norwegian score -->
   <td class="sv-score">43.43 ± 2.43</td> <!-- Swedish score -->
   <td class="da ner">38.31 ± 2.59 / 27.23 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">37.13 ± 2.26 / 44.00 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">26.46 ± 5.28 / 53.12 ± 6.51</td> <!-- ScaLA-da -->
   <td class="da qa">39.77 ± 4.66 / 44.54 ± 5.00</td> <!-- ScandiQA-da -->
   <td class="no ner">46.32 ± 3.74 / 34.02 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">48.20 ± 1.59 / 35.05 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">20.46 ± 5.98 / 36.24 ± 6.77</td> <!-- NoReC -->
   <td class="no la">4.50 ± 4.17 / 35.29 ± 2.89</td> <!-- ScaLA-nb -->
   <td class="no la">1.10 ± 1.47 / 34.51 ± 1.24</td> <!-- ScaLA-nn -->
   <td class="no qa">31.16 ± 1.83 / 52.35 ± 2.34</td> <!-- NorQuAD -->
   <td class="sv ner">39.55 ± 2.39 / 27.89 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">78.79 ± 0.91 / 75.25 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">15.77 ± 1.64 / 54.44 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.62 ± 4.78 / 45.18 ± 4.72</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="score">34.75 ± 2.72</td> <!-- ScandEval score -->
   <td class="da-score">26.28 ± 2.17</td> <!-- Danish score -->
   <td class="no-score">30.36 ± 2.48</td> <!-- Norwegian score -->
   <td class="sv-score">47.62 ± 3.52</td> <!-- Swedish score -->
   <td class="da ner">47.61 ± 1.71 / 45.91 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">24.17 ± 1.92 / 43.75 ± 2.75</td> <!-- Angry Tweets -->
   <td class="da la">8.14 ± 3.76 / 51.78 ± 1.81</td> <!-- ScaLA-da -->
   <td class="da qa">25.19 ± 1.29 / 30.51 ± 1.06</td> <!-- ScandiQA-da -->
   <td class="no ner">68.63 ± 1.64 / 64.83 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">67.70 ± 2.68 / 63.70 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">25.68 ± 2.17 / 41.65 ± 2.77</td> <!-- NoReC -->
   <td class="no la">6.73 ± 5.40 / 48.20 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">3.35 ± 2.61 / 47.52 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">22.57 ± 1.57 / 34.64 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">68.83 ± 1.00 / 63.29 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">64.25 ± 1.66 / 63.62 ± 2.92</td> <!-- SweReC -->
   <td class="sv la">28.62 ± 9.43 / 59.33 ± 5.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.78 ± 2.01 / 34.26 ± 2.03</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="score">33.92 ± 2.25</td> <!-- ScandEval score -->
   <td class="da-score">28.84 ± 2.70</td> <!-- Danish score -->
   <td class="no-score">31.74 ± 1.54</td> <!-- Norwegian score -->
   <td class="sv-score">41.19 ± 2.51</td> <!-- Swedish score -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">15.42 ± 1.70 / 21.36 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.33 ± 1.03 / 64.03 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="score">33.80 ± 2.27</td> <!-- ScandEval score -->
   <td class="da-score">28.47 ± 2.71</td> <!-- Danish score -->
   <td class="no-score">31.74 ± 1.54</td> <!-- Norwegian score -->
   <td class="sv-score">41.20 ± 2.55</td> <!-- Swedish score -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">13.97 ± 1.75 / 19.76 ± 2.26</td> <!-- ScandiQA-da -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.36 ± 1.18 / 63.94 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="score">33.57 ± 2.07</td> <!-- ScandEval score -->
   <td class="da-score">24.44 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">31.27 ± 2.48</td> <!-- Norwegian score -->
   <td class="sv-score">45.01 ± 1.77</td> <!-- Swedish score -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">55.00 ± 0.85 / 60.83 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.33 ± 3.57 / 62.91 ± 3.37</td> <!-- NorQuAD -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.05 ± 0.85 / 60.85 ± 0.72</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="score">33.23 ± 2.22</td> <!-- ScandEval score -->
   <td class="da-score">26.54 ± 1.62</td> <!-- Danish score -->
   <td class="no-score">29.05 ± 1.94</td> <!-- Norwegian score -->
   <td class="sv-score">44.10 ± 3.11</td> <!-- Swedish score -->
   <td class="da ner">49.88 ± 2.14 / 46.74 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">27.93 ± 0.66 / 50.86 ± 0.42</td> <!-- Angry Tweets -->
   <td class="da la">5.42 ± 2.85 / 48.29 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">22.93 ± 0.81 / 28.62 ± 0.62</td> <!-- ScandiQA-da -->
   <td class="no ner">69.65 ± 1.48 / 66.15 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">66.78 ± 1.28 / 62.75 ± 1.40</td> <!-- NorNE-nn -->
   <td class="no sent">26.33 ± 1.84 / 40.67 ± 0.71</td> <!-- NoReC -->
   <td class="no la">6.62 ± 3.40 / 48.37 ± 4.02</td> <!-- ScaLA-nb -->
   <td class="no la">5.16 ± 3.07 / 45.99 ± 4.76</td> <!-- ScaLA-nn -->
   <td class="no qa">15.75 ± 1.30 / 27.15 ± 1.91</td> <!-- NorQuAD -->
   <td class="sv ner">66.11 ± 1.24 / 61.03 ± 1.08</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.84 / 55.24 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">26.28 ± 8.44 / 59.64 ± 5.68</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.36 ± 0.92 / 30.54 ± 0.96</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">33.23 ± 2.39</td> <!-- ScandEval score -->
   <td class="da-score">30.35 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">25.85 ± 2.05</td> <!-- Norwegian score -->
   <td class="sv-score">43.48 ± 3.18</td> <!-- Swedish score -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">45.42 ± 1.92 / 51.05 ± 2.05</td> <!-- ScandiQA-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">18.67 ± 2.60 / 36.99 ± 2.72</td> <!-- NorQuAD -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.42 ± 4.19 / 49.62 ± 4.21</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">31=</td> <!-- Rank -->
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="score">32.85 ± 1.77</td> <!-- ScandEval score -->
   <td class="da-score">41.16 ± 1.84</td> <!-- Danish score -->
   <td class="no-score">28.87 ± 1.43</td> <!-- Norwegian score -->
   <td class="sv-score">28.52 ± 2.03</td> <!-- Swedish score -->
   <td class="da ner">62.52 ± 1.33 / 57.14 ± 1.29</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 3.16 / 51.40 ± 5.12</td> <!-- Angry Tweets -->
   <td class="da la">65.15 ± 0.81 / 82.32 ± 0.45</td> <!-- ScaLA-da -->
   <td class="da qa">2.51 ± 2.06 / 2.75 ± 2.29</td> <!-- ScandiQA-da -->
   <td class="no ner">59.76 ± 3.01 / 55.95 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">51.44 ± 2.28 / 48.14 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">33.41 ± 1.40 / 45.12 ± 1.87</td> <!-- NoReC -->
   <td class="no la">32.87 ± 1.49 / 65.82 ± 0.78</td> <!-- ScaLA-nb -->
   <td class="no la">20.09 ± 1.88 / 59.27 ± 1.08</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">39.17 ± 4.06 / 36.74 ± 3.78</td> <!-- SUC3 -->
   <td class="sv sent">57.71 ± 1.40 / 53.54 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">17.10 ± 2.57 / 57.41 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.11 ± 0.11 / 0.13 ± 0.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">32</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">31.97 ± 2.05</td> <!-- ScandEval score -->
   <td class="da-score">27.79 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">25.65 ± 2.71</td> <!-- Norwegian score -->
   <td class="sv-score">42.46 ± 1.50</td> <!-- Swedish score -->
   <td class="da ner">33.41 ± 3.32 / 25.37 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">26.08 ± 2.58 / 36.10 ± 3.61</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 0.43 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">51.90 ± 1.44 / 56.87 ± 1.30</td> <!-- ScandiQA-da -->
   <td class="no ner">41.44 ± 4.22 / 32.73 ± 3.13</td> <!-- NorNE-nb -->
   <td class="no ner">45.09 ± 3.73 / 35.29 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">34.51 ± 3.16 / 54.99 ± 2.47</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.56 ± 1.10 / 33.93 ± 0.37</td> <!-- ScaLA-nn -->
   <td class="no qa">24.53 ± 3.16 / 41.00 ± 4.65</td> <!-- NorQuAD -->
   <td class="sv ner">41.08 ± 3.32 / 29.46 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 0.82 / 75.25 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">-0.21 ± 0.42 / 33.36 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.58 ± 1.46 / 57.71 ± 1.17</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">33</td> <!-- Rank -->
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="score">31.59 ± 2.27</td> <!-- ScandEval score -->
   <td class="da-score">38.38 ± 3.17</td> <!-- Danish score -->
   <td class="no-score">27.03 ± 1.87</td> <!-- Norwegian score -->
   <td class="sv-score">29.35 ± 1.76</td> <!-- Swedish score -->
   <td class="da ner">60.78 ± 1.12 / 55.74 ± 1.15</td> <!-- DANSK -->
   <td class="da sent">39.65 ± 1.31 / 59.23 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">37.67 ± 7.20 / 65.47 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">15.41 ± 3.05 / 22.46 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="no ner">65.95 ± 0.72 / 62.62 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">55.29 ± 1.26 / 51.50 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">33.31 ± 2.87 / 48.75 ± 3.38</td> <!-- NoReC -->
   <td class="no la">20.34 ± 4.81 / 58.57 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">8.07 ± 2.44 / 53.43 ± 1.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.14 ± 0.16</td> <!-- NorQuAD -->
   <td class="sv ner">42.99 ± 1.57 / 39.98 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">55.49 ± 1.28 / 55.99 ± 2.15</td> <!-- SweReC -->
   <td class="sv la">4.69 ± 2.28 / 51.01 ± 1.58</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.22 ± 1.90 / 20.83 ± 1.46</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">34=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="score">28.15 ± 3.23</td> <!-- ScandEval score -->
   <td class="da-score">22.16 ± 2.93</td> <!-- Danish score -->
   <td class="no-score">24.59 ± 3.76</td> <!-- Norwegian score -->
   <td class="sv-score">37.69 ± 2.99</td> <!-- Swedish score -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da qa">39.18 ± 3.52 / 44.53 ± 3.79</td> <!-- ScandiQA-da -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no qa">24.67 ± 2.82 / 43.02 ± 4.03</td> <!-- NorQuAD -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.78 ± 4.94 / 41.08 ± 5.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">34=</td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="score">25.98 ± 1.54</td> <!-- ScandEval score -->
   <td class="da-score">23.28 ± 1.64</td> <!-- Danish score -->
   <td class="no-score">22.36 ± 1.14</td> <!-- Norwegian score -->
   <td class="sv-score">32.30 ± 1.85</td> <!-- Swedish score -->
   <td class="da ner">46.78 ± 1.50 / 44.41 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">27.78 ± 2.22 / 49.38 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">3.04 ± 1.85 / 46.85 ± 3.03</td> <!-- ScaLA-da -->
   <td class="da qa">15.52 ± 0.98 / 23.22 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">60.76 ± 1.53 / 58.35 ± 1.41</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.19 / 55.90 ± 1.12</td> <!-- NorNE-nn -->
   <td class="no sent">25.98 ± 1.33 / 40.58 ± 0.60</td> <!-- NoReC -->
   <td class="no la">2.65 ± 2.08 / 48.09 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">3.47 ± 1.47 / 48.98 ± 1.75</td> <!-- ScaLA-nn -->
   <td class="no qa">0.20 ± 0.09 / 0.82 ± 0.39</td> <!-- NorQuAD -->
   <td class="sv ner">49.86 ± 1.85 / 44.53 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">60.06 ± 1.30 / 55.65 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">3.18 ± 1.63 / 48.38 ± 1.42</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.08 ± 2.60 / 23.46 ± 3.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">35=</td> <!-- Rank -->
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="score">25.80 ± 3.06</td> <!-- ScandEval score -->
   <td class="da-score">17.95 ± 3.16</td> <!-- Danish score -->
   <td class="no-score">22.30 ± 2.06</td> <!-- Norwegian score -->
   <td class="sv-score">37.13 ± 3.95</td> <!-- Swedish score -->
   <td class="da ner">29.90 ± 7.25 / 28.27 ± 6.86</td> <!-- DANSK -->
   <td class="da sent">19.79 ± 1.67 / 42.09 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">6.15 ± 1.66 / 52.04 ± 1.49</td> <!-- ScaLA-da -->
   <td class="da qa">15.96 ± 2.06 / 21.55 ± 2.17</td> <!-- ScandiQA-da -->
   <td class="no ner">66.97 ± 1.30 / 62.99 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">63.90 ± 2.54 / 59.95 ± 2.51</td> <!-- NorNE-nn -->
   <td class="no sent">18.85 ± 4.01 / 36.76 ± 2.79</td> <!-- NoReC -->
   <td class="no la">5.83 ± 2.36 / 51.59 ± 1.57</td> <!-- ScaLA-nb -->
   <td class="no la">4.02 ± 2.29 / 51.66 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">47.19 ± 9.01 / 44.34 ± 8.27</td> <!-- SUC3 -->
   <td class="sv sent">56.57 ± 1.41 / 53.47 ± 0.84</td> <!-- SweReC -->
   <td class="sv la">20.92 ± 4.12 / 59.05 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">23.86 ± 1.25 / 30.47 ± 1.51</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">35=</td> <!-- Rank -->
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="score">25.15 ± 1.82</td> <!-- ScandEval score -->
   <td class="da-score">20.94 ± 1.36</td> <!-- Danish score -->
   <td class="no-score">23.10 ± 1.74</td> <!-- Norwegian score -->
   <td class="sv-score">31.43 ± 2.35</td> <!-- Swedish score -->
   <td class="da ner">41.70 ± 1.80 / 38.74 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">26.03 ± 0.90 / 48.46 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.19 ± 1.92 / 49.80 ± 1.39</td> <!-- ScaLA-da -->
   <td class="da qa">13.82 ± 0.82 / 20.76 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">61.55 ± 1.55 / 58.24 ± 1.47</td> <!-- NorNE-nb -->
   <td class="no ner">59.90 ± 1.56 / 56.03 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">24.59 ± 1.57 / 40.34 ± 0.99</td> <!-- NoReC -->
   <td class="no la">3.45 ± 2.10 / 50.80 ± 1.16</td> <!-- ScaLA-nb -->
   <td class="no la">2.72 ± 1.56 / 48.79 ± 1.92</td> <!-- ScaLA-nn -->
   <td class="no qa">3.99 ± 2.02 / 7.49 ± 3.66</td> <!-- NorQuAD -->
   <td class="sv ner">50.07 ± 4.14 / 47.04 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">56.10 ± 1.85 / 52.92 ± 0.76</td> <!-- SweReC -->
   <td class="sv la">5.05 ± 2.27 / 51.08 ± 1.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.49 ± 1.13 / 22.34 ± 1.16</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="score">24.54 ± 2.38</td> <!-- ScandEval score -->
   <td class="da-score">18.31 ± 1.88</td> <!-- Danish score -->
   <td class="no-score">24.10 ± 2.96</td> <!-- Norwegian score -->
   <td class="sv-score">31.21 ± 2.29</td> <!-- Swedish score -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da qa">44.04 ± 2.07 / 51.91 ± 2.08</td> <!-- ScandiQA-da -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">31.39 ± 2.33 / 52.78 ± 3.03</td> <!-- NorQuAD -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.72 ± 2.66 / 50.17 ± 3.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="score">24.06 ± 2.89</td> <!-- ScandEval score -->
   <td class="da-score">23.00 ± 2.12</td> <!-- Danish score -->
   <td class="no-score">18.49 ± 3.00</td> <!-- Norwegian score -->
   <td class="sv-score">30.70 ± 3.56</td> <!-- Swedish score -->
   <td class="da ner">14.88 ± 3.92 / 14.02 ± 2.63</td> <!-- DANSK -->
   <td class="da sent">34.66 ± 1.82 / 46.40 ± 1.53</td> <!-- Angry Tweets -->
   <td class="da la">0.29 ± 1.86 / 41.01 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da qa">42.16 ± 0.88 / 47.49 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="no ner">14.58 ± 6.07 / 15.44 ± 5.52</td> <!-- NorNE-nb -->
   <td class="no ner">21.06 ± 7.77 / 21.99 ± 7.14</td> <!-- NorNE-nn -->
   <td class="no sent">32.02 ± 1.59 / 36.85 ± 2.01</td> <!-- NoReC -->
   <td class="no la">1.49 ± 1.40 / 35.35 ± 1.51</td> <!-- ScaLA-nb -->
   <td class="no la">0.98 ± 1.85 / 35.28 ± 2.43</td> <!-- ScaLA-nn -->
   <td class="no qa">22.87 ± 1.85 / 38.93 ± 2.59</td> <!-- NorQuAD -->
   <td class="sv ner">13.79 ± 8.46 / 14.43 ± 7.23</td> <!-- SUC3 -->
   <td class="sv sent">71.59 ± 2.78 / 59.82 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">-0.89 ± 1.22 / 43.82 ± 3.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.33 ± 1.79 / 44.00 ± 1.70</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="score">24.04 ± 3.09</td> <!-- ScandEval score -->
   <td class="da-score">21.40 ± 2.76</td> <!-- Danish score -->
   <td class="no-score">19.69 ± 4.15</td> <!-- Norwegian score -->
   <td class="sv-score">31.04 ± 2.35</td> <!-- Swedish score -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da qa">45.31 ± 0.88 / 51.56 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">34.90 ± 2.66 / 54.29 ± 2.94</td> <!-- NorQuAD -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.53 ± 0.83 / 51.66 ± 0.78</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="score">23.36 ± 1.43</td> <!-- ScandEval score -->
   <td class="da-score">18.76 ± 1.27</td> <!-- Danish score -->
   <td class="no-score">18.10 ± 1.46</td> <!-- Norwegian score -->
   <td class="sv-score">33.23 ± 1.55</td> <!-- Swedish score -->
   <td class="da ner">32.63 ± 1.06 / 32.76 ± 1.02</td> <!-- DANSK -->
   <td class="da sent">24.11 ± 1.74 / 44.78 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">2.91 ± 1.07 / 46.98 ± 3.78</td> <!-- ScaLA-da -->
   <td class="da qa">15.37 ± 1.22 / 22.17 ± 1.24</td> <!-- ScandiQA-da -->
   <td class="no ner">49.30 ± 0.97 / 46.11 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">46.11 ± 2.15 / 43.01 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">23.21 ± 2.32 / 44.26 ± 2.95</td> <!-- NoReC -->
   <td class="no la">2.26 ± 1.47 / 45.07 ± 4.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.66 ± 1.81 / 44.50 ± 3.45</td> <!-- ScaLA-nn -->
   <td class="no qa">0.68 ± 0.32 / 1.50 ± 0.80</td> <!-- NorQuAD -->
   <td class="sv ner">51.13 ± 2.13 / 46.67 ± 1.98</td> <!-- SUC3 -->
   <td class="sv sent">61.67 ± 1.40 / 59.12 ± 2.44</td> <!-- SweReC -->
   <td class="sv la">2.87 ± 1.53 / 48.92 ± 2.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.24 ± 1.13 / 25.10 ± 1.06</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="score">22.77 ± 2.98</td> <!-- ScandEval score -->
   <td class="da-score">20.21 ± 2.51</td> <!-- Danish score -->
   <td class="no-score">20.04 ± 2.50</td> <!-- Norwegian score -->
   <td class="sv-score">28.05 ± 3.93</td> <!-- Swedish score -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da qa">38.57 ± 0.65 / 47.40 ± 0.63</td> <!-- ScandiQA-da -->
   <td class="no ner">23.82 ± 4.25 / 22.08 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">26.04 ± 6.38 / 24.47 ± 3.69</td> <!-- NorNE-nn -->
   <td class="no sent">32.60 ± 1.84 / 47.47 ± 3.33</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.43 / 44.47 ± 2.44</td> <!-- ScaLA-nb -->
   <td class="no la">2.26 ± 2.27 / 45.41 ± 3.25</td> <!-- ScaLA-nn -->
   <td class="no qa">21.34 ± 0.98 / 42.76 ± 1.06</td> <!-- NorQuAD -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.22 ± 1.08 / 46.81 ± 0.82</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">36=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="score">21.42 ± 3.23</td> <!-- ScandEval score -->
   <td class="da-score">20.13 ± 2.48</td> <!-- Danish score -->
   <td class="no-score">20.78 ± 2.57</td> <!-- Norwegian score -->
   <td class="sv-score">23.34 ± 4.63</td> <!-- Swedish score -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da qa">34.81 ± 1.50 / 39.69 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">27.37 ± 4.07 / 27.94 ± 4.04</td> <!-- NorNE-nb -->
   <td class="no ner">31.22 ± 3.87 / 31.39 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">34.21 ± 1.63 / 47.17 ± 2.76</td> <!-- NoReC -->
   <td class="no la">0.92 ± 1.55 / 40.71 ± 2.58</td> <!-- ScaLA-nb -->
   <td class="no la">1.25 ± 2.30 / 43.49 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">18.54 ± 2.77 / 32.10 ± 4.22</td> <!-- NorQuAD -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.71 ± 1.47 / 38.82 ± 1.55</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="score">19.22 ± 2.18</td> <!-- ScandEval score -->
   <td class="da-score">15.82 ± 1.79</td> <!-- Danish score -->
   <td class="no-score">17.36 ± 2.39</td> <!-- Norwegian score -->
   <td class="sv-score">24.47 ± 2.37</td> <!-- Swedish score -->
   <td class="da ner">36.51 ± 2.44 / 36.31 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">22.07 ± 2.24 / 44.70 ± 3.72</td> <!-- Angry Tweets -->
   <td class="da la">1.63 ± 1.49 / 45.36 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da qa">3.09 ± 1.00 / 9.48 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">55.55 ± 3.71 / 52.52 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">53.53 ± 3.03 / 50.23 ± 3.00</td> <!-- NorNE-nn -->
   <td class="no sent">12.69 ± 4.51 / 32.23 ± 3.53</td> <!-- NoReC -->
   <td class="no la">2.79 ± 1.16 / 47.71 ± 2.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.66 ± 2.18 / 46.60 ± 2.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.60 ± 0.72</td> <!-- NorQuAD -->
   <td class="sv ner">42.78 ± 3.26 / 40.46 ± 3.04</td> <!-- SUC3 -->
   <td class="sv sent">44.95 ± 2.30 / 48.17 ± 1.06</td> <!-- SweReC -->
   <td class="sv la">1.43 ± 1.34 / 48.66 ± 2.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.71 ± 2.58 / 16.77 ± 2.50</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="score">18.87 ± 1.65</td> <!-- ScandEval score -->
   <td class="da-score">19.57 ± 2.17</td> <!-- Danish score -->
   <td class="no-score">17.28 ± 1.29</td> <!-- Norwegian score -->
   <td class="sv-score">19.75 ± 1.50</td> <!-- Swedish score -->
   <td class="da ner">33.05 ± 1.28 / 31.68 ± 1.05</td> <!-- DANSK -->
   <td class="da sent">30.67 ± 1.28 / 51.76 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">13.01 ± 5.22 / 55.11 ± 3.40</td> <!-- ScaLA-da -->
   <td class="da qa">1.56 ± 0.88 / 5.30 ± 2.21</td> <!-- ScandiQA-da -->
   <td class="no ner">42.18 ± 1.03 / 39.53 ± 1.04</td> <!-- NorNE-nb -->
   <td class="no ner">37.39 ± 1.81 / 34.88 ± 1.76</td> <!-- NorNE-nn -->
   <td class="no sent">24.39 ± 1.60 / 40.44 ± 1.78</td> <!-- NoReC -->
   <td class="no la">7.29 ± 2.49 / 49.37 ± 3.58</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 46.00 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">22.47 ± 1.55 / 20.74 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">53.88 ± 1.97 / 52.30 ± 1.04</td> <!-- SweReC -->
   <td class="sv la">1.55 ± 1.62 / 44.06 ± 3.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">1.12 ± 0.85 / 3.07 ± 1.91</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="score">18.72 ± 3.51</td> <!-- ScandEval score -->
   <td class="da-score">18.96 ± 2.48</td> <!-- Danish score -->
   <td class="no-score">15.36 ± 2.42</td> <!-- Norwegian score -->
   <td class="sv-score">21.84 ± 5.64</td> <!-- Swedish score -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da qa">18.78 ± 3.89 / 24.10 ± 4.26</td> <!-- ScandiQA-da -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 0.33 / 17.89 ± 1.64</td> <!-- NorQuAD -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">15.08 ± 3.85 / 19.72 ± 4.11</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">16.90 ± 2.84</td> <!-- ScandEval score -->
   <td class="da-score">11.58 ± 2.52</td> <!-- Danish score -->
   <td class="no-score">14.62 ± 1.70</td> <!-- Norwegian score -->
   <td class="sv-score">24.49 ± 4.30</td> <!-- Swedish score -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.21 ± 3.93 / 29.03 ± 4.17</td> <!-- ScandiQA-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.79 ± 1.65 / 50.19 ± 1.83</td> <!-- NorQuAD -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.37 ± 1.37 / 50.18 ± 1.18</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="score">14.93 ± 4.50</td> <!-- ScandEval score -->
   <td class="da-score">13.52 ± 3.03</td> <!-- Danish score -->
   <td class="no-score">11.81 ± 3.66</td> <!-- Norwegian score -->
   <td class="sv-score">19.47 ± 6.82</td> <!-- Swedish score -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">14.16 ± 1.82 / 19.24 ± 1.85</td> <!-- ScandiQA-da -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no qa">2.15 ± 0.46 / 10.01 ± 1.47</td> <!-- NorQuAD -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">21.56 ± 3.80 / 26.32 ± 4.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="score">14.62 ± 1.28</td> <!-- ScandEval score -->
   <td class="da-score">11.54 ± 1.17</td> <!-- Danish score -->
   <td class="no-score">12.03 ± 1.31</td> <!-- Norwegian score -->
   <td class="sv-score">20.27 ± 1.35</td> <!-- Swedish score -->
   <td class="da ner">22.21 ± 0.75 / 21.70 ± 0.70</td> <!-- DANSK -->
   <td class="da sent">20.33 ± 1.89 / 40.95 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">0.90 ± 1.40 / 48.85 ± 2.60</td> <!-- ScaLA-da -->
   <td class="da qa">2.73 ± 0.64 / 7.23 ± 1.45</td> <!-- ScandiQA-da -->
   <td class="no ner">31.87 ± 2.26 / 30.31 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">32.47 ± 1.48 / 30.59 ± 1.43</td> <!-- NorNE-nn -->
   <td class="no sent">15.07 ± 1.97 / 35.80 ± 1.15</td> <!-- NoReC -->
   <td class="no la">1.26 ± 1.26 / 48.42 ± 1.75</td> <!-- ScaLA-nb -->
   <td class="no la">0.49 ± 1.58 / 45.93 ± 3.88</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">24.61 ± 1.58 / 23.05 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">52.31 ± 1.22 / 51.51 ± 0.49</td> <!-- SweReC -->
   <td class="sv la">1.32 ± 1.87 / 46.80 ± 4.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.86 ± 0.73 / 8.44 ± 2.01</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,319 ± 94 / 656 ± 172</td> <!-- Model inference speed -->
   <td class="score">11.81 ± 2.05</td> <!-- ScandEval score -->
   <td class="da-score">9.08 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">9.87 ± 1.74</td> <!-- Norwegian score -->
   <td class="sv-score">16.47 ± 2.45</td> <!-- Swedish score -->
   <td class="da ner">16.04 ± 2.47 / 15.60 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">17.37 ± 3.82 / 36.83 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">1.34 ± 0.97 / 35.45 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da qa">1.58 ± 0.51 / 6.64 ± 1.56</td> <!-- ScandiQA-da -->
   <td class="no ner">25.49 ± 3.39 / 23.54 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">25.94 ± 1.70 / 24.10 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">12.60 ± 2.97 / 32.27 ± 3.43</td> <!-- NoReC -->
   <td class="no la">0.50 ± 1.27 / 36.93 ± 4.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.83 ± 1.64 / 37.67 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">11.91 ± 3.04 / 11.31 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.11 ± 5.32 / 50.09 ± 3.33</td> <!-- SweReC -->
   <td class="sv la">0.86 ± 0.82 / 39.16 ± 3.63</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.00 ± 0.63 / 7.20 ± 1.68</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">37=</td> <!-- Rank -->
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,219 ± 712 / 3,276 ± 803</td> <!-- Model inference speed -->
   <td class="score">10.74 ± 1.62</td> <!-- ScandEval score -->
   <td class="da-score">7.94 ± 1.80</td> <!-- Danish score -->
   <td class="no-score">7.78 ± 1.95</td> <!-- Norwegian score -->
   <td class="sv-score">16.49 ± 1.11</td> <!-- Swedish score -->
   <td class="da ner">12.87 ± 1.63 / 13.23 ± 1.55</td> <!-- DANSK -->
   <td class="da sent">18.61 ± 4.17 / 35.23 ± 3.90</td> <!-- Angry Tweets -->
   <td class="da la">0.30 ± 1.39 / 37.84 ± 3.88</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">18.38 ± 2.01 / 17.08 ± 1.97</td> <!-- NorNE-nb -->
   <td class="no ner">12.76 ± 1.29 / 11.65 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">15.29 ± 5.37 / 34.15 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.17 ± 0.84 / 36.29 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.37 ± 0.69 / 35.08 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">10.54 ± 1.12 / 9.71 ± 1.00</td> <!-- SUC3 -->
   <td class="sv sent">55.54 ± 2.75 / 52.75 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">-0.15 ± 0.52 / 35.33 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.02 ± 0.03 / 0.04 ± 0.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">38=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="score">9.23 ± 4.32</td> <!-- ScandEval score -->
   <td class="da-score">8.86 ± 3.49</td> <!-- Danish score -->
   <td class="no-score">7.45 ± 3.24</td> <!-- Norwegian score -->
   <td class="sv-score">11.40 ± 6.24</td> <!-- Swedish score -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da qa">6.82 ± 6.80 / 21.29 ± 6.25</td> <!-- ScandiQA-da -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">20.84 ± 6.06 / 35.78 ± 5.94</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.09 / 34.65 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">0.48 ± 0.66 / 32.86 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">2.45 ± 0.61 / 22.80 ± 2.27</td> <!-- NorQuAD -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.79 ± 11.20 / 31.10 ± 8.39</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">38=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="score">6.30 ± 3.30</td> <!-- ScandEval score -->
   <td class="da-score">4.10 ± 3.81</td> <!-- Danish score -->
   <td class="no-score">5.21 ± 1.76</td> <!-- Norwegian score -->
   <td class="sv-score">9.58 ± 4.33</td> <!-- Swedish score -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">5.16 ± 6.60 / 17.34 ± 5.84</td> <!-- ScandiQA-da -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">20.64 ± 5.63 / 36.75 ± 3.29</td> <!-- NoReC -->
   <td class="no la">-0.99 ± 0.88 / 33.37 ± 0.27</td> <!-- ScaLA-nb -->
   <td class="no la">-0.15 ± 0.72 / 32.83 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.55 ± 0.32 / 22.10 ± 2.28</td> <!-- NorQuAD -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">4.82 ± 3.58 / 18.08 ± 2.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">38=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="score">4.89 ± 3.07</td> <!-- ScandEval score -->
   <td class="da-score">5.02 ± 2.28</td> <!-- Danish score -->
   <td class="no-score">4.48 ± 2.74</td> <!-- Norwegian score -->
   <td class="sv-score">5.16 ± 4.18</td> <!-- Swedish score -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da qa">7.70 ± 0.67 / 10.40 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no qa">0.90 ± 0.23 / 4.99 ± 1.08</td> <!-- NorQuAD -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">7.64 ± 2.58 / 9.62 ± 3.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">39=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">4.05 ± 1.22</td> <!-- ScandEval score -->
   <td class="da-score">3.25 ± 1.04</td> <!-- Danish score -->
   <td class="no-score">0.24 ± 0.20</td> <!-- Norwegian score -->
   <td class="sv-score">8.66 ± 2.42</td> <!-- Swedish score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 12.40 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 33.55 ± 0.25</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 8.95 ± 2.92</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">39=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="score">2.89 ± 1.38</td> <!-- ScandEval score -->
   <td class="da-score">1.20 ± 0.67</td> <!-- Danish score -->
   <td class="no-score">0.32 ± 0.30</td> <!-- Norwegian score -->
   <td class="sv-score">7.16 ± 3.17</td> <!-- Swedish score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.81 ± 2.69 / 19.31 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 30.05 ± 4.99</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.27 ± 1.21 / 9.77 ± 0.51</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 32.25 ± 0.29</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.62 ± 12.67 / 35.36 ± 8.35</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 19.59 ± 6.84</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">39=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,982 ± 434 / 1,008 ± 322</td> <!-- Model inference speed -->
   <td class="score">2.75 ± 1.27</td> <!-- ScandEval score -->
   <td class="da-score">1.15 ± 0.84</td> <!-- Danish score -->
   <td class="no-score">0.06 ± 0.12</td> <!-- Norwegian score -->
   <td class="sv-score">7.03 ± 2.85</td> <!-- Swedish score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.60 ± 3.35 / 20.43 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.72 ± 0.91</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 29.30 ± 5.68</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.25 ± 0.49 / 8.63 ± 0.83</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.30 ± 0.69</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.28 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 33.54 ± 1.34</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.13 ± 11.41 / 34.63 ± 7.11</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.96</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 20.71 ± 7.37</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">39=</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">1.33 ± 1.26</td> <!-- ScandEval score -->
   <td class="da-score">1.13 ± 1.71</td> <!-- Danish score -->
   <td class="no-score">1.17 ± 0.96</td> <!-- Norwegian score -->
   <td class="sv-score">1.68 ± 1.10</td> <!-- Swedish score -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da qa">2.00 ± 1.70 / 2.69 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.73 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">6.24 ± 3.13 / 7.86 ± 3.68</td> <!-- ScandiQA-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">39=</td> <!-- Rank -->
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="score">0.35 ± 1.01</td> <!-- ScandEval score -->
   <td class="da-score">0.14 ± 1.11</td> <!-- Danish score -->
   <td class="no-score">-0.20 ± 0.83</td> <!-- Norwegian score -->
   <td class="sv-score">1.12 ± 1.09</td> <!-- Swedish score -->
   <td class="da ner">0.64 ± 0.89 / 0.52 ± 0.69</td> <!-- DANSK -->
   <td class="da sent">-0.52 ± 1.72 / 28.55 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">-0.02 ± 1.55 / 36.82 ± 2.52</td> <!-- ScaLA-da -->
   <td class="da qa">0.48 ± 0.27 / 2.89 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="no ner">0.29 ± 0.29 / 0.29 ± 0.27</td> <!-- NorNE-nb -->
   <td class="no ner">0.25 ± 0.17 / 0.27 ± 0.21</td> <!-- NorNE-nn -->
   <td class="no sent">-1.43 ± 1.45 / 20.90 ± 4.96</td> <!-- NoReC -->
   <td class="no la">-0.42 ± 1.10 / 35.77 ± 3.09</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.21 / 39.28 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.15 ± 0.55</td> <!-- NorQuAD -->
   <td class="sv ner">0.26 ± 0.16 / 0.26 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">4.75 ± 2.54 / 27.85 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">-0.60 ± 1.56 / 40.53 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.06 ± 0.09 / 1.07 ± 0.35</td> <!-- ScandiQA-sv -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlu.csv" target="_blank">Download as CSV</a>
</div>