---
layout: leaderboard
title: Mainland Scandinavian NLU Benchmark
---

<center>Last updated: 06/01/2024 11:22:06</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="mainland-scandinavian-nlu-benchmark" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score">SV</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total named entity recognition score">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification score">SENT</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total linguistic acceptability score">LA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total question answering score">QA</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">DANSK</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Angry Tweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">ScandiQA-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact Match / F1-score">ScandiQA-sv</span></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.92 ± 1.70 / 70.36 ± 1.61</td> <!-- DANSK -->
   <td class="da sent">46.32 ± 1.22 / 64.13 ± 0.85</td> <!-- Angry Tweets -->
   <td class="da la">66.41 ± 1.89 / 82.44 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da qa">36.42 ± 1.11 / 41.53 ± 1.29</td> <!-- ScandiQA-da -->
   <td class="no ner">89.36 ± 0.86 / 93.01 ± 0.68</td> <!-- NorNE-nb -->
   <td class="no ner">84.38 ± 0.81 / 88.43 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">60.84 ± 1.48 / 72.16 ± 1.38</td> <!-- NoReC -->
   <td class="no la">73.89 ± 1.31 / 86.19 ± 0.93</td> <!-- ScaLA-nb -->
   <td class="no la">72.10 ± 2.07 / 85.37 ± 1.33</td> <!-- ScaLA-nn -->
   <td class="no qa">33.01 ± 3.06 / 45.28 ± 3.64</td> <!-- NorQuAD -->
   <td class="no qa">35.27 ± 3.01 / 39.54 ± 3.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.35 ± 0.88 / 80.38 ± 0.99</td> <!-- SUC3 -->
   <td class="sv sent">71.21 ± 1.11 / 67.49 ± 2.90</td> <!-- SweReC -->
   <td class="sv la">64.03 ± 1.94 / 81.39 ± 1.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.33 ± 2.25 / 39.61 ± 2.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">64.77 ± 1.86 / 68.77 ± 2.07</td> <!-- DANSK -->
   <td class="da sent">49.66 ± 0.99 / 66.21 ± 0.72</td> <!-- Angry Tweets -->
   <td class="da la">60.13 ± 13.57 / 78.92 ± 6.96</td> <!-- ScaLA-da -->
   <td class="da qa">32.60 ± 0.75 / 37.37 ± 0.72</td> <!-- ScandiQA-da -->
   <td class="no ner">86.13 ± 1.08 / 88.99 ± 0.96</td> <!-- NorNE-nb -->
   <td class="no ner">78.66 ± 1.85 / 82.99 ± 1.53</td> <!-- NorNE-nn -->
   <td class="no sent">57.37 ± 1.31 / 70.45 ± 1.13</td> <!-- NoReC -->
   <td class="no la">69.92 ± 2.01 / 83.51 ± 1.33</td> <!-- ScaLA-nb -->
   <td class="no la">70.05 ± 1.76 / 84.13 ± 1.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.98 ± 3.70 / 55.88 ± 3.70</td> <!-- NorQuAD -->
   <td class="no qa">30.43 ± 1.60 / 35.00 ± 1.43</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.31 ± 3.11 / 73.44 ± 2.81</td> <!-- SUC3 -->
   <td class="sv sent">73.63 ± 1.53 / 68.42 ± 4.24</td> <!-- SweReC -->
   <td class="sv la">58.91 ± 17.49 / 77.13 ± 10.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.39 ± 1.02 / 37.33 ± 0.86</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">64.54 ± 1.00 / 70.10 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">45.30 ± 2.03 / 63.22 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">51.74 ± 2.53 / 74.31 ± 1.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.01 ± 2.50 / 27.76 ± 2.44</td> <!-- ScandiQA-da -->
   <td class="no ner">85.32 ± 0.94 / 87.70 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">77.41 ± 1.57 / 81.41 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">48.34 ± 2.10 / 60.68 ± 3.61</td> <!-- NoReC -->
   <td class="no la">55.30 ± 2.89 / 75.77 ± 1.87</td> <!-- ScaLA-nb -->
   <td class="no la">37.46 ± 2.69 / 67.68 ± 1.66</td> <!-- ScaLA-nn -->
   <td class="no qa">24.49 ± 6.03 / 35.93 ± 8.56</td> <!-- NorQuAD -->
   <td class="no qa">29.72 ± 3.40 / 34.87 ± 3.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.03 ± 1.55 / 72.49 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">70.69 ± 1.08 / 67.03 ± 3.40</td> <!-- SweReC -->
   <td class="sv la">56.60 ± 3.25 / 76.70 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.89 ± 1.88 / 37.63 ± 1.86</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.20 ± 1.98 / 63.38 ± 2.39</td> <!-- DANSK -->
   <td class="da sent">34.78 ± 1.49 / 55.59 ± 0.92</td> <!-- Angry Tweets -->
   <td class="da la">41.08 ± 7.28 / 69.77 ± 3.75</td> <!-- ScaLA-da -->
   <td class="da qa">40.32 ± 0.81 / 44.89 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">84.88 ± 1.05 / 88.05 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">79.06 ± 1.70 / 83.08 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">35.34 ± 1.88 / 48.31 ± 2.28</td> <!-- NoReC -->
   <td class="no la">31.45 ± 12.12 / 63.68 ± 6.21</td> <!-- ScaLA-nb -->
   <td class="no la">36.12 ± 8.59 / 66.98 ± 4.91</td> <!-- ScaLA-nn -->
   <td class="no qa">41.59 ± 2.45 / 54.67 ± 2.65</td> <!-- NorQuAD -->
   <td class="no qa">39.40 ± 1.47 / 43.81 ± 1.55</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.38 ± 1.01 / 76.55 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">61.60 ± 1.38 / 62.28 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">37.44 ± 6.65 / 66.67 ± 4.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.32 ± 1.25 / 43.87 ± 1.29</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.45 ± 2.58 / 63.17 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">32.38 ± 1.72 / 53.30 ± 1.79</td> <!-- Angry Tweets -->
   <td class="da la">27.93 ± 11.48 / 61.91 ± 6.69</td> <!-- ScaLA-da -->
   <td class="da qa">39.57 ± 1.18 / 44.06 ± 1.25</td> <!-- ScandiQA-da -->
   <td class="no ner">85.49 ± 0.92 / 88.72 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">79.36 ± 1.38 / 83.08 ± 1.22</td> <!-- NorNE-nn -->
   <td class="no sent">35.87 ± 1.85 / 48.94 ± 3.37</td> <!-- NoReC -->
   <td class="no la">44.22 ± 3.29 / 70.31 ± 2.86</td> <!-- ScaLA-nb -->
   <td class="no la">39.55 ± 7.01 / 68.65 ± 3.36</td> <!-- ScaLA-nn -->
   <td class="no qa">40.55 ± 2.19 / 53.62 ± 2.68</td> <!-- NorQuAD -->
   <td class="no qa">38.24 ± 2.08 / 42.62 ± 2.20</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.33 ± 1.16 / 76.29 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">61.78 ± 1.21 / 60.94 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">47.74 ± 7.69 / 72.98 ± 4.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.17 ± 1.01 / 46.07 ± 1.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.99 ± 2.88 / 62.53 ± 2.60</td> <!-- DANSK -->
   <td class="da sent">32.88 ± 1.24 / 53.56 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">29.01 ± 11.25 / 61.89 ± 6.94</td> <!-- ScaLA-da -->
   <td class="da qa">39.51 ± 1.53 / 44.11 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="no ner">84.84 ± 1.42 / 87.99 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">79.18 ± 1.45 / 83.10 ± 1.12</td> <!-- NorNE-nn -->
   <td class="no sent">36.21 ± 1.82 / 49.48 ± 2.69</td> <!-- NoReC -->
   <td class="no la">46.43 ± 1.81 / 71.65 ± 1.39</td> <!-- ScaLA-nb -->
   <td class="no la">39.82 ± 2.81 / 68.68 ± 1.81</td> <!-- ScaLA-nn -->
   <td class="no qa">40.01 ± 1.58 / 53.12 ± 1.81</td> <!-- NorQuAD -->
   <td class="no qa">38.04 ± 1.25 / 42.59 ± 1.47</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.17 ± 1.46 / 75.62 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">62.50 ± 1.10 / 60.57 ± 2.75</td> <!-- SweReC -->
   <td class="sv la">38.18 ± 7.03 / 66.99 ± 4.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.96 ± 1.11 / 45.91 ± 1.20</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.39 ± 2.04 / 62.57 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">33.67 ± 1.54 / 54.48 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">35.79 ± 9.58 / 65.87 ± 5.46</td> <!-- ScaLA-da -->
   <td class="da qa">38.77 ± 2.23 / 43.26 ± 2.39</td> <!-- ScandiQA-da -->
   <td class="no ner">85.29 ± 1.04 / 88.55 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">79.27 ± 1.21 / 83.09 ± 1.06</td> <!-- NorNE-nn -->
   <td class="no sent">35.16 ± 1.75 / 48.41 ± 2.71</td> <!-- NoReC -->
   <td class="no la">31.82 ± 8.92 / 62.98 ± 6.52</td> <!-- ScaLA-nb -->
   <td class="no la">32.94 ± 5.88 / 64.36 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no qa">39.46 ± 1.70 / 52.33 ± 1.94</td> <!-- NorQuAD -->
   <td class="no qa">36.54 ± 2.03 / 40.65 ± 2.15</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.57 ± 1.83 / 74.88 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">61.89 ± 0.90 / 60.17 ± 3.06</td> <!-- SweReC -->
   <td class="sv la">40.22 ± 2.03 / 68.89 ± 2.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.95 ± 0.82 / 44.78 ± 0.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">60.53 ± 1.65 / 65.40 ± 2.02</td> <!-- DANSK -->
   <td class="da sent">34.43 ± 4.13 / 51.90 ± 6.17</td> <!-- Angry Tweets -->
   <td class="da la">67.27 ± 1.04 / 83.37 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">6.60 ± 2.98 / 7.09 ± 3.29</td> <!-- ScandiQA-da -->
   <td class="no ner">81.68 ± 0.65 / 84.95 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">74.62 ± 1.92 / 79.57 ± 1.49</td> <!-- NorNE-nn -->
   <td class="no sent">40.15 ± 1.15 / 46.26 ± 0.47</td> <!-- NoReC -->
   <td class="no la">72.87 ± 1.11 / 85.86 ± 0.63</td> <!-- ScaLA-nb -->
   <td class="no la">63.77 ± 1.27 / 81.62 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">14.16 ± 4.55 / 19.70 ± 6.40</td> <!-- NorQuAD -->
   <td class="no qa">5.81 ± 3.66 / 6.29 ± 4.04</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.46 ± 1.28 / 71.07 ± 1.59</td> <!-- SUC3 -->
   <td class="sv sent">66.42 ± 0.72 / 57.57 ± 1.23</td> <!-- SweReC -->
   <td class="sv la">69.19 ± 0.66 / 84.26 ± 0.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">11.85 ± 4.94 / 13.02 ± 5.55</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.09 ± 1.52 / 61.74 ± 1.46</td> <!-- DANSK -->
   <td class="da sent">33.28 ± 1.65 / 54.37 ± 1.44</td> <!-- Angry Tweets -->
   <td class="da la">33.15 ± 7.14 / 64.69 ± 4.47</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td class="no ner">83.05 ± 1.29 / 85.91 ± 0.98</td> <!-- NorNE-nb -->
   <td class="no ner">76.00 ± 2.01 / 79.67 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">38.70 ± 2.53 / 50.88 ± 3.38</td> <!-- NoReC -->
   <td class="no la">39.13 ± 2.97 / 67.97 ± 1.68</td> <!-- ScaLA-nb -->
   <td class="no la">24.13 ± 6.88 / 60.76 ± 3.29</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td class="no qa">31.24 ± 1.57 / 35.41 ± 1.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.66 ± 1.60 / 81.95 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">75.58 ± 1.17 / 73.35 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">78.86 ± 0.83 / 89.07 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.15 ± 2.53 / 72.74 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.33 ± 4.44 / 63.94 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">57.30 ± 14.90 / 76.82 ± 8.67</td> <!-- ScaLA-da -->
   <td class="da qa">43.57 ± 3.28 / 49.29 ± 3.35</td> <!-- ScandiQA-da -->
   <td class="no ner">89.34 ± 1.62 / 91.66 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">82.86 ± 1.29 / 86.19 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">50.25 ± 15.36 / 63.55 ± 13.05</td> <!-- NoReC -->
   <td class="no la">55.51 ± 18.28 / 74.00 ± 13.38</td> <!-- ScaLA-nb -->
   <td class="no la">43.89 ± 14.81 / 68.88 ± 10.32</td> <!-- ScaLA-nn -->
   <td class="no qa">57.57 ± 2.43 / 72.69 ± 2.22</td> <!-- NorQuAD -->
   <td class="no qa">44.63 ± 1.05 / 49.69 ± 0.89</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.03 ± 3.79 / 80.33 ± 2.50</td> <!-- SUC3 -->
   <td class="sv sent">76.63 ± 0.98 / 74.25 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">49.72 ± 19.88 / 69.94 ± 13.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.64 ± 1.42 / 52.21 ± 1.45</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.41 ± 2.19 / 72.90 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">43.38 ± 3.20 / 60.05 ± 4.33</td> <!-- Angry Tweets -->
   <td class="da la">67.05 ± 1.41 / 83.18 ± 0.80</td> <!-- ScaLA-da -->
   <td class="da qa">42.15 ± 2.12 / 47.97 ± 1.99</td> <!-- ScandiQA-da -->
   <td class="no ner">89.55 ± 0.57 / 91.90 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">83.46 ± 1.68 / 86.81 ± 1.35</td> <!-- NorNE-nn -->
   <td class="no sent">53.69 ± 4.28 / 63.69 ± 6.95</td> <!-- NoReC -->
   <td class="no la">70.55 ± 1.64 / 84.79 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">61.21 ± 1.20 / 79.87 ± 0.76</td> <!-- ScaLA-nn -->
   <td class="no qa">48.82 ± 1.20 / 63.72 ± 1.06</td> <!-- NorQuAD -->
   <td class="no qa">42.86 ± 1.22 / 48.99 ± 1.19</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.86 ± 2.04 / 78.84 ± 2.19</td> <!-- SUC3 -->
   <td class="sv sent">75.24 ± 0.99 / 72.06 ± 2.67</td> <!-- SweReC -->
   <td class="sv la">72.30 ± 1.04 / 85.77 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.74 ± 1.04 / 50.62 ± 0.85</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.41 ± 1.64 / 71.24 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">46.50 ± 1.57 / 64.31 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">52.92 ± 4.42 / 75.11 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">40.08 ± 1.22 / 45.40 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">87.84 ± 1.00 / 90.58 ± 0.91</td> <!-- NorNE-nb -->
   <td class="no ner">81.57 ± 1.30 / 85.21 ± 1.05</td> <!-- NorNE-nn -->
   <td class="no sent">54.26 ± 1.75 / 67.25 ± 1.47</td> <!-- NoReC -->
   <td class="no la">59.44 ± 1.47 / 78.80 ± 1.00</td> <!-- ScaLA-nb -->
   <td class="no la">49.30 ± 1.39 / 74.02 ± 1.04</td> <!-- ScaLA-nn -->
   <td class="no qa">46.42 ± 1.44 / 61.82 ± 1.47</td> <!-- NorQuAD -->
   <td class="no qa">40.50 ± 0.74 / 45.74 ± 0.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.08 ± 1.81 / 77.78 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">73.58 ± 1.37 / 70.43 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">60.36 ± 2.98 / 79.72 ± 1.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.71 ± 1.08 / 47.07 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.82 ± 3.50 / 58.50 ± 4.21</td> <!-- DANSK -->
   <td class="da sent">41.02 ± 1.64 / 60.13 ± 1.52</td> <!-- Angry Tweets -->
   <td class="da la">27.10 ± 3.59 / 61.03 ± 2.41</td> <!-- ScaLA-da -->
   <td class="da qa">39.99 ± 1.25 / 45.72 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="no ner">83.09 ± 0.94 / 85.99 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">75.61 ± 1.34 / 79.47 ± 1.14</td> <!-- NorNE-nn -->
   <td class="no sent">39.53 ± 0.99 / 50.90 ± 2.17</td> <!-- NoReC -->
   <td class="no la">27.39 ± 2.48 / 61.03 ± 2.27</td> <!-- ScaLA-nb -->
   <td class="no la">23.56 ± 2.23 / 60.05 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">39.01 ± 1.18 / 51.83 ± 1.58</td> <!-- NorQuAD -->
   <td class="no qa">39.71 ± 0.96 / 45.25 ± 0.94</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.08 ± 1.45 / 81.05 ± 1.34</td> <!-- SUC3 -->
   <td class="sv sent">78.00 ± 0.89 / 75.01 ± 2.18</td> <!-- SweReC -->
   <td class="sv la">76.79 ± 1.70 / 87.59 ± 1.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.71 ± 1.09 / 51.70 ± 0.89</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">56.95 ± 1.66 / 60.66 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 1.17 / 58.16 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.29 ± 5.92 / 63.74 ± 3.44</td> <!-- ScaLA-da -->
   <td class="da qa">37.68 ± 1.06 / 43.21 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">80.48 ± 0.89 / 83.32 ± 0.99</td> <!-- NorNE-nb -->
   <td class="no ner">74.84 ± 1.18 / 77.97 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">38.44 ± 1.67 / 52.60 ± 1.95</td> <!-- NoReC -->
   <td class="no la">37.54 ± 1.13 / 64.46 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">23.10 ± 3.66 / 58.14 ± 3.65</td> <!-- ScaLA-nn -->
   <td class="no qa">39.97 ± 0.84 / 51.67 ± 1.11</td> <!-- NorQuAD -->
   <td class="no qa">38.13 ± 1.55 / 43.19 ± 1.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.84 ± 1.51 / 78.61 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 0.80 / 75.77 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">72.87 ± 2.36 / 85.57 ± 1.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.11 ± 0.99 / 49.29 ± 1.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.15 ± 2.47 / 60.18 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">39.20 ± 1.69 / 59.33 ± 1.23</td> <!-- Angry Tweets -->
   <td class="da la">26.68 ± 3.38 / 59.41 ± 2.16</td> <!-- ScaLA-da -->
   <td class="da qa">39.34 ± 0.84 / 44.87 ± 0.79</td> <!-- ScandiQA-da -->
   <td class="no ner">80.97 ± 0.92 / 84.03 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">74.25 ± 1.62 / 77.98 ± 1.36</td> <!-- NorNE-nn -->
   <td class="no sent">39.15 ± 3.29 / 53.00 ± 3.85</td> <!-- NoReC -->
   <td class="no la">21.39 ± 2.73 / 58.08 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 3.43 / 57.00 ± 1.86</td> <!-- ScaLA-nn -->
   <td class="no qa">35.32 ± 1.71 / 47.41 ± 2.25</td> <!-- NorQuAD -->
   <td class="no qa">38.92 ± 0.96 / 44.25 ± 1.03</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.83 ± 1.44 / 80.39 ± 1.34</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 0.79 / 77.12 ± 0.86</td> <!-- SweReC -->
   <td class="sv la">76.28 ± 1.86 / 87.37 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.56 ± 0.52 / 50.85 ± 0.56</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.64 ± 2.08 / 60.82 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 0.78 / 55.56 ± 0.68</td> <!-- Angry Tweets -->
   <td class="da la">41.89 ± 9.80 / 70.04 ± 5.10</td> <!-- ScaLA-da -->
   <td class="da qa">26.83 ± 1.26 / 31.55 ± 1.26</td> <!-- ScandiQA-da -->
   <td class="no ner">82.31 ± 0.65 / 85.42 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">74.86 ± 1.50 / 78.92 ± 1.42</td> <!-- NorNE-nn -->
   <td class="no sent">36.27 ± 1.57 / 50.95 ± 1.70</td> <!-- NoReC -->
   <td class="no la">48.07 ± 5.64 / 72.00 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">29.81 ± 3.52 / 64.03 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no qa">0.44 ± 0.41 / 1.08 ± 0.99</td> <!-- NorQuAD -->
   <td class="no qa">27.54 ± 1.10 / 31.80 ± 1.13</td> <!-- ScandiQA-no -->
   <td class="sv ner">66.93 ± 1.30 / 72.90 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">61.11 ± 1.28 / 58.97 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">55.05 ± 1.64 / 76.76 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.04 ± 1.16 / 33.60 ± 1.06</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">52.41 ± 1.98 / 55.98 ± 2.24</td> <!-- DANSK -->
   <td class="da sent">36.66 ± 1.27 / 57.48 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">22.69 ± 5.37 / 59.46 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">24.81 ± 1.85 / 29.08 ± 1.74</td> <!-- ScandiQA-da -->
   <td class="no ner">76.73 ± 1.16 / 79.25 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">71.63 ± 1.31 / 75.39 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 3.06 / 51.25 ± 3.01</td> <!-- NoReC -->
   <td class="no la">22.02 ± 5.34 / 57.45 ± 3.59</td> <!-- ScaLA-nb -->
   <td class="no la">19.72 ± 3.67 / 56.70 ± 2.89</td> <!-- ScaLA-nn -->
   <td class="no qa">0.78 ± 0.74 / 1.49 ± 1.32</td> <!-- NorQuAD -->
   <td class="no qa">26.74 ± 0.91 / 30.79 ± 0.93</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.45 ± 1.62 / 75.40 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">76.22 ± 0.78 / 75.25 ± 1.16</td> <!-- SweReC -->
   <td class="sv la">65.73 ± 1.73 / 81.50 ± 1.14</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.34 ± 1.44 / 34.01 ± 1.50</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.15 ± 1.78 / 59.37 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">38.46 ± 0.77 / 58.57 ± 0.67</td> <!-- Angry Tweets -->
   <td class="da la">4.61 ± 2.95 / 49.70 ± 2.34</td> <!-- ScaLA-da -->
   <td class="da qa">23.13 ± 2.72 / 28.47 ± 2.30</td> <!-- ScandiQA-da -->
   <td class="no ner">80.34 ± 1.44 / 83.23 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">75.55 ± 1.69 / 79.16 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">33.94 ± 3.74 / 47.96 ± 4.12</td> <!-- NoReC -->
   <td class="no la">9.56 ± 5.01 / 52.24 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">4.16 ± 2.97 / 50.07 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">22.84 ± 2.52 / 33.72 ± 3.11</td> <!-- NorQuAD -->
   <td class="no qa">24.84 ± 1.79 / 29.84 ± 1.59</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.07 ± 1.54 / 79.99 ± 1.32</td> <!-- SUC3 -->
   <td class="sv sent">76.04 ± 0.97 / 72.61 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">73.52 ± 2.31 / 85.57 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.60 ± 1.30 / 35.83 ± 1.02</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">52.04 ± 1.64 / 53.93 ± 1.88</td> <!-- DANSK -->
   <td class="da sent">36.31 ± 1.60 / 57.37 ± 1.15</td> <!-- Angry Tweets -->
   <td class="da la">23.46 ± 1.17 / 58.91 ± 1.36</td> <!-- ScaLA-da -->
   <td class="da qa">27.85 ± 2.53 / 34.34 ± 2.51</td> <!-- ScandiQA-da -->
   <td class="no ner">75.03 ± 1.70 / 77.98 ± 1.58</td> <!-- NorNE-nb -->
   <td class="no ner">71.00 ± 1.64 / 75.00 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">33.88 ± 1.40 / 49.21 ± 1.98</td> <!-- NoReC -->
   <td class="no la">24.23 ± 1.83 / 58.89 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">18.18 ± 2.65 / 57.28 ± 1.84</td> <!-- ScaLA-nn -->
   <td class="no qa">20.56 ± 1.82 / 30.08 ± 2.54</td> <!-- NorQuAD -->
   <td class="no qa">28.66 ± 1.73 / 33.95 ± 1.68</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.18 ± 0.95 / 79.29 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">75.85 ± 0.54 / 70.58 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">70.43 ± 1.03 / 83.85 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.56 ± 0.64 / 44.01 ± 0.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,035 ± 84 / 4,068 ± 1,290</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.18 ± 1.78 / 63.31 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">32.72 ± 2.91 / 49.84 ± 4.90</td> <!-- Angry Tweets -->
   <td class="da la">67.74 ± 1.33 / 83.32 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">68.20 ± 1.23 / 71.85 ± 1.11</td> <!-- NorNE-nb -->
   <td class="no ner">62.61 ± 1.22 / 67.14 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">29.00 ± 1.28 / 41.72 ± 0.52</td> <!-- NoReC -->
   <td class="no la">33.57 ± 2.58 / 65.22 ± 1.59</td> <!-- ScaLA-nb -->
   <td class="no la">21.79 ± 1.60 / 60.32 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">0.03 ± 0.07 / 0.05 ± 0.10</td> <!-- NorQuAD -->
   <td class="no qa">0.58 ± 1.15 / 0.71 ± 1.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">54.55 ± 1.33 / 57.82 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">55.68 ± 1.09 / 52.81 ± 0.44</td> <!-- SweReC -->
   <td class="sv la">19.26 ± 1.80 / 58.62 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">61.55 ± 1.75 / 66.71 ± 1.80</td> <!-- DANSK -->
   <td class="da sent">43.79 ± 1.76 / 62.26 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">45.96 ± 2.91 / 69.62 ± 1.72</td> <!-- ScaLA-da -->
   <td class="da qa">26.29 ± 2.34 / 32.91 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="no ner">69.33 ± 0.93 / 72.62 ± 0.81</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 1.67 / 58.73 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">40.65 ± 1.63 / 55.20 ± 2.63</td> <!-- NoReC -->
   <td class="no la">29.47 ± 2.30 / 62.25 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">12.95 ± 3.01 / 55.31 ± 1.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.91 ± 0.93 / 2.56 ± 2.15</td> <!-- NorQuAD -->
   <td class="no qa">24.99 ± 3.12 / 31.27 ± 2.83</td> <!-- ScandiQA-no -->
   <td class="sv ner">47.15 ± 1.18 / 50.29 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">57.42 ± 1.88 / 56.53 ± 1.66</td> <!-- SweReC -->
   <td class="sv la">4.94 ± 1.62 / 51.57 ± 1.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.16 ± 1.28 / 30.28 ± 1.18</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.14 ± 1.29 / 62.52 ± 1.33</td> <!-- DANSK -->
   <td class="da sent">34.45 ± 3.16 / 51.40 ± 5.12</td> <!-- Angry Tweets -->
   <td class="da la">65.15 ± 0.81 / 82.32 ± 0.45</td> <!-- ScaLA-da -->
   <td class="da qa">2.51 ± 2.06 / 2.75 ± 2.29</td> <!-- ScandiQA-da -->
   <td class="no ner">55.95 ± 2.74 / 59.76 ± 3.01</td> <!-- NorNE-nb -->
   <td class="no ner">48.14 ± 1.95 / 51.44 ± 2.28</td> <!-- NorNE-nn -->
   <td class="no sent">33.41 ± 1.40 / 45.12 ± 1.87</td> <!-- NoReC -->
   <td class="no la">32.87 ± 1.49 / 65.82 ± 0.78</td> <!-- ScaLA-nb -->
   <td class="no la">20.09 ± 1.88 / 59.27 ± 1.08</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">1.29 ± 1.58 / 1.38 ± 1.70</td> <!-- ScandiQA-no -->
   <td class="sv ner">36.74 ± 3.78 / 39.17 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">57.71 ± 1.40 / 53.54 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">17.10 ± 2.57 / 57.41 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.11 ± 0.11 / 0.13 ± 0.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.04 ± 1.60 / 58.52 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">42.26 ± 1.13 / 61.41 ± 0.76</td> <!-- Angry Tweets -->
   <td class="da la">34.80 ± 5.89 / 64.51 ± 4.90</td> <!-- ScaLA-da -->
   <td class="da qa">19.60 ± 1.60 / 25.68 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">75.93 ± 1.64 / 80.08 ± 1.46</td> <!-- NorNE-nb -->
   <td class="no ner">70.26 ± 2.24 / 74.59 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">52.16 ± 0.99 / 66.79 ± 0.98</td> <!-- NoReC -->
   <td class="no la">36.30 ± 6.44 / 65.52 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">14.21 ± 6.44 / 52.78 ± 5.69</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">21.51 ± 1.72 / 26.97 ± 1.64</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.54 ± 1.20 / 68.94 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 0.89 / 68.13 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">40.21 ± 2.53 / 67.11 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.09 ± 1.31 / 25.99 ± 1.19</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.88 ± 1.74 / 62.76 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">32.06 ± 1.44 / 52.57 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 11.93 / 63.72 ± 6.84</td> <!-- ScaLA-da -->
   <td class="da qa">37.79 ± 2.37 / 42.36 ± 2.56</td> <!-- ScandiQA-da -->
   <td class="no ner">83.86 ± 0.68 / 87.52 ± 0.63</td> <!-- NorNE-nb -->
   <td class="no ner">78.65 ± 2.01 / 82.66 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">32.73 ± 1.37 / 46.52 ± 1.86</td> <!-- NoReC -->
   <td class="no la">36.41 ± 8.89 / 65.20 ± 6.41</td> <!-- ScaLA-nb -->
   <td class="no la">30.37 ± 5.50 / 62.12 ± 5.66</td> <!-- ScaLA-nn -->
   <td class="no qa">37.71 ± 1.11 / 49.90 ± 1.47</td> <!-- NorQuAD -->
   <td class="no qa">35.77 ± 2.11 / 39.84 ± 2.30</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.93 ± 1.36 / 74.13 ± 1.17</td> <!-- SUC3 -->
   <td class="sv sent">62.18 ± 1.26 / 59.44 ± 2.35</td> <!-- SweReC -->
   <td class="sv la">36.93 ± 6.47 / 65.97 ± 6.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.59 ± 1.99 / 41.94 ± 2.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">54.97 ± 1.45 / 58.12 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">32.53 ± 1.39 / 54.09 ± 1.00</td> <!-- Angry Tweets -->
   <td class="da la">35.53 ± 2.54 / 66.86 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">28.19 ± 1.93 / 32.96 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="no ner">80.61 ± 1.00 / 83.62 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">76.61 ± 0.81 / 80.69 ± 0.69</td> <!-- NorNE-nn -->
   <td class="no sent">33.16 ± 2.13 / 46.93 ± 2.66</td> <!-- NoReC -->
   <td class="no la">36.10 ± 2.45 / 66.11 ± 1.85</td> <!-- ScaLA-nb -->
   <td class="no la">30.10 ± 2.50 / 64.29 ± 1.69</td> <!-- ScaLA-nn -->
   <td class="no qa">19.26 ± 1.57 / 30.04 ± 2.13</td> <!-- NorQuAD -->
   <td class="no qa">27.10 ± 1.49 / 31.24 ± 1.46</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.46 ± 1.31 / 70.08 ± 1.38</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.22 / 56.16 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">33.71 ± 1.12 / 65.32 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.48 ± 1.85 / 36.44 ± 1.87</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.32 ± 1.81 / 58.44 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">31.81 ± 1.65 / 53.25 ± 1.65</td> <!-- Angry Tweets -->
   <td class="da la">34.13 ± 2.81 / 65.98 ± 2.30</td> <!-- ScaLA-da -->
   <td class="da qa">27.60 ± 1.58 / 32.18 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">80.55 ± 1.53 / 83.59 ± 1.36</td> <!-- NorNE-nb -->
   <td class="no ner">76.08 ± 1.06 / 80.29 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">33.19 ± 1.75 / 46.63 ± 2.55</td> <!-- NoReC -->
   <td class="no la">32.60 ± 6.93 / 65.19 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">24.97 ± 6.47 / 61.39 ± 3.34</td> <!-- ScaLA-nn -->
   <td class="no qa">19.93 ± 1.76 / 30.69 ± 2.36</td> <!-- NorQuAD -->
   <td class="no qa">29.09 ± 0.94 / 33.04 ± 0.85</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.49 ± 1.43 / 70.56 ± 1.36</td> <!-- SUC3 -->
   <td class="sv sent">60.69 ± 0.46 / 56.69 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">30.83 ± 1.47 / 63.39 ± 1.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.41 ± 1.05 / 36.45 ± 1.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.30 ± 1.49 / 58.36 ± 1.69</td> <!-- DANSK -->
   <td class="da sent">32.13 ± 1.52 / 53.89 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">34.75 ± 1.55 / 65.89 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">27.50 ± 1.21 / 32.16 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="no ner">79.91 ± 0.64 / 82.84 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">74.64 ± 1.40 / 78.83 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">30.70 ± 2.63 / 43.77 ± 2.62</td> <!-- NoReC -->
   <td class="no la">34.24 ± 2.30 / 65.60 ± 1.50</td> <!-- ScaLA-nb -->
   <td class="no la">27.20 ± 2.61 / 62.87 ± 1.41</td> <!-- ScaLA-nn -->
   <td class="no qa">16.44 ± 1.76 / 26.22 ± 2.65</td> <!-- NorQuAD -->
   <td class="no qa">28.42 ± 0.77 / 32.35 ± 0.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.90 ± 1.27 / 69.25 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">58.47 ± 1.30 / 56.03 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">29.80 ± 1.57 / 63.53 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.61 ± 1.31 / 35.37 ± 1.52</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">56.28 ± 1.67 / 59.50 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">31.89 ± 1.59 / 53.99 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">36.00 ± 2.27 / 67.38 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.41 ± 1.26 / 33.19 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">80.29 ± 1.38 / 83.27 ± 1.20</td> <!-- NorNE-nb -->
   <td class="no ner">75.31 ± 1.19 / 79.59 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">29.37 ± 2.58 / 44.05 ± 3.33</td> <!-- NoReC -->
   <td class="no la">31.50 ± 6.37 / 64.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">24.06 ± 7.24 / 61.01 ± 3.82</td> <!-- ScaLA-nn -->
   <td class="no qa">18.62 ± 0.81 / 29.69 ± 1.81</td> <!-- NorQuAD -->
   <td class="no qa">27.00 ± 1.09 / 31.38 ± 0.80</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.51 ± 1.33 / 69.62 ± 0.88</td> <!-- SUC3 -->
   <td class="sv sent">59.42 ± 1.21 / 55.74 ± 1.26</td> <!-- SweReC -->
   <td class="sv la">29.01 ± 2.06 / 62.65 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.82 ± 1.07 / 36.82 ± 1.14</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.91 ± 2.15 / 70.36 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.46 / 65.49 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">11.87 ± 5.47 / 48.82 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da qa">29.87 ± 3.18 / 35.11 ± 2.73</td> <!-- ScandiQA-da -->
   <td class="no ner">87.56 ± 1.39 / 90.07 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">82.40 ± 1.16 / 85.65 ± 0.96</td> <!-- NorNE-nn -->
   <td class="no sent">54.46 ± 1.16 / 68.25 ± 0.76</td> <!-- NoReC -->
   <td class="no la">12.16 ± 5.91 / 50.55 ± 4.73</td> <!-- ScaLA-nb -->
   <td class="no la">8.99 ± 2.25 / 48.57 ± 3.67</td> <!-- ScaLA-nn -->
   <td class="no qa">49.24 ± 1.30 / 64.35 ± 1.24</td> <!-- NorQuAD -->
   <td class="no qa">29.01 ± 2.06 / 33.58 ± 1.99</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.04 ± 2.25 / 78.60 ± 1.91</td> <!-- SUC3 -->
   <td class="sv sent">73.67 ± 1.48 / 68.61 ± 3.14</td> <!-- SweReC -->
   <td class="sv la">15.41 ± 4.59 / 53.29 ± 3.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.41 ± 3.14 / 37.13 ± 3.07</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.50 ± 1.82 / 58.78 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">31.30 ± 1.80 / 52.43 ± 1.61</td> <!-- Angry Tweets -->
   <td class="da la">34.92 ± 2.74 / 66.69 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">27.86 ± 1.51 / 32.53 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="no ner">80.32 ± 0.76 / 83.49 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">76.10 ± 1.23 / 80.23 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">32.66 ± 1.96 / 46.26 ± 3.19</td> <!-- NoReC -->
   <td class="no la">33.65 ± 6.63 / 65.22 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">29.07 ± 2.20 / 63.35 ± 1.54</td> <!-- ScaLA-nn -->
   <td class="no qa">19.29 ± 1.27 / 29.94 ± 1.81</td> <!-- NorQuAD -->
   <td class="no qa">27.59 ± 0.51 / 31.65 ± 0.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.93 ± 1.47 / 69.94 ± 1.11</td> <!-- SUC3 -->
   <td class="sv sent">59.83 ± 1.11 / 55.15 ± 0.99</td> <!-- SweReC -->
   <td class="sv la">29.82 ± 1.23 / 63.32 ± 1.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.13 ± 1.15 / 36.20 ± 1.22</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">53.43 ± 1.87 / 56.75 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 1.32 / 63.11 ± 0.83</td> <!-- Angry Tweets -->
   <td class="da la">26.74 ± 1.94 / 62.19 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da qa">17.89 ± 1.00 / 25.53 ± 1.05</td> <!-- ScandiQA-da -->
   <td class="no ner">74.65 ± 1.36 / 78.31 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">67.28 ± 1.09 / 72.13 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">47.53 ± 0.94 / 62.73 ± 1.07</td> <!-- NoReC -->
   <td class="no la">26.92 ± 3.12 / 61.93 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.63 ± 4.00 / 56.24 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">17.10 ± 0.57 / 24.19 ± 0.79</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.99 ± 1.40 / 66.50 ± 1.49</td> <!-- SUC3 -->
   <td class="sv sent">72.19 ± 0.71 / 67.88 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">28.75 ± 5.58 / 63.30 ± 2.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">15.91 ± 0.87 / 23.08 ± 0.95</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">47.83 ± 1.59 / 49.22 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">33.51 ± 1.46 / 54.93 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">12.08 ± 8.71 / 54.24 ± 4.71</td> <!-- ScaLA-da -->
   <td class="da qa">24.49 ± 1.67 / 28.88 ± 1.71</td> <!-- ScandiQA-da -->
   <td class="no ner">69.79 ± 2.34 / 72.74 ± 2.03</td> <!-- NorNE-nb -->
   <td class="no ner">65.59 ± 2.06 / 69.74 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">29.68 ± 1.91 / 43.64 ± 2.18</td> <!-- NoReC -->
   <td class="no la">15.83 ± 10.06 / 55.51 ± 5.25</td> <!-- ScaLA-nb -->
   <td class="no la">8.70 ± 4.78 / 52.69 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">1.04 ± 1.17 / 1.93 ± 2.12</td> <!-- NorQuAD -->
   <td class="no qa">26.01 ± 0.83 / 30.43 ± 0.86</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.00 ± 2.58 / 68.55 ± 3.16</td> <!-- SUC3 -->
   <td class="sv sent">69.96 ± 1.75 / 68.67 ± 3.21</td> <!-- SweReC -->
   <td class="sv la">52.88 ± 14.23 / 75.25 ± 7.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">27.99 ± 1.23 / 32.49 ± 1.27</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">53.98 ± 1.92 / 56.36 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">31.16 ± 2.06 / 52.25 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">21.08 ± 2.54 / 56.96 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">19.63 ± 2.13 / 23.61 ± 2.07</td> <!-- ScandiQA-da -->
   <td class="no ner">79.80 ± 1.69 / 82.98 ± 1.32</td> <!-- NorNE-nb -->
   <td class="no ner">72.29 ± 1.44 / 76.65 ± 1.24</td> <!-- NorNE-nn -->
   <td class="no sent">30.38 ± 2.29 / 42.84 ± 2.38</td> <!-- NoReC -->
   <td class="no la">21.99 ± 6.74 / 54.54 ± 7.12</td> <!-- ScaLA-nb -->
   <td class="no la">19.06 ± 4.26 / 56.45 ± 5.24</td> <!-- ScaLA-nn -->
   <td class="no qa">9.47 ± 5.36 / 15.24 ± 8.64</td> <!-- NorQuAD -->
   <td class="no qa">19.54 ± 2.06 / 22.69 ± 2.28</td> <!-- ScandiQA-no -->
   <td class="sv ner">66.98 ± 1.68 / 73.41 ± 1.54</td> <!-- SUC3 -->
   <td class="sv sent">62.10 ± 1.18 / 60.27 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">34.86 ± 1.29 / 66.98 ± 0.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.10 ± 2.67 / 21.09 ± 3.18</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">44.41 ± 1.78 / 46.78 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">27.78 ± 2.22 / 49.38 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">3.04 ± 1.85 / 46.85 ± 3.03</td> <!-- ScaLA-da -->
   <td class="da qa">15.52 ± 0.98 / 23.22 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">58.35 ± 1.41 / 60.76 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">55.90 ± 1.12 / 59.62 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">25.98 ± 1.33 / 40.58 ± 0.60</td> <!-- NoReC -->
   <td class="no la">2.65 ± 2.08 / 48.09 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">3.47 ± 1.47 / 48.98 ± 1.75</td> <!-- ScaLA-nn -->
   <td class="no qa">0.20 ± 0.09 / 0.82 ± 0.39</td> <!-- NorQuAD -->
   <td class="no qa">14.36 ± 2.52 / 21.71 ± 3.03</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.53 ± 1.58 / 49.86 ± 1.85</td> <!-- SUC3 -->
   <td class="sv sent">60.06 ± 1.30 / 55.65 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">3.18 ± 1.63 / 48.38 ± 1.42</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.08 ± 2.60 / 23.46 ± 3.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">41.25 ± 14.74 / 43.90 ± 15.70</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 5.85 / 62.62 ± 4.55</td> <!-- Angry Tweets -->
   <td class="da la">30.37 ± 17.09 / 63.92 ± 8.38</td> <!-- ScaLA-da -->
   <td class="da qa">28.89 ± 1.91 / 33.71 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">68.50 ± 15.04 / 71.73 ± 15.69</td> <!-- NorNE-nb -->
   <td class="no ner">75.76 ± 0.90 / 79.80 ± 0.72</td> <!-- NorNE-nn -->
   <td class="no sent">46.74 ± 5.96 / 60.25 ± 6.04</td> <!-- NoReC -->
   <td class="no la">8.02 ± 12.19 / 50.30 ± 7.19</td> <!-- ScaLA-nb -->
   <td class="no la">17.04 ± 13.78 / 56.87 ± 7.06</td> <!-- ScaLA-nn -->
   <td class="no qa">29.26 ± 1.27 / 42.50 ± 1.17</td> <!-- NorQuAD -->
   <td class="no qa">27.92 ± 1.29 / 32.28 ± 1.15</td> <!-- ScandiQA-no -->
   <td class="sv ner">53.63 ± 12.63 / 58.84 ± 13.92</td> <!-- SUC3 -->
   <td class="sv sent">72.28 ± 0.79 / 71.62 ± 1.38</td> <!-- SweReC -->
   <td class="sv la">37.61 ± 17.89 / 66.93 ± 9.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.59 ± 0.68 / 35.43 ± 0.61</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.85 ± 1.44 / 63.84 ± 1.73</td> <!-- DANSK -->
   <td class="da sent">43.90 ± 1.50 / 62.31 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">17.16 ± 13.94 / 56.47 ± 7.34</td> <!-- ScaLA-da -->
   <td class="da qa">26.94 ± 1.16 / 31.50 ± 1.03</td> <!-- ScandiQA-da -->
   <td class="no ner">72.24 ± 2.54 / 76.14 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">68.61 ± 1.62 / 72.88 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 9.23 / 49.08 ± 8.36</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.61 / 49.14 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">-0.08 ± 1.79 / 45.89 ± 3.49</td> <!-- ScaLA-nn -->
   <td class="no qa">23.91 ± 2.24 / 36.47 ± 2.77</td> <!-- NorQuAD -->
   <td class="no qa">27.08 ± 1.48 / 31.31 ± 1.37</td> <!-- ScandiQA-no -->
   <td class="sv ner">60.53 ± 1.38 / 65.95 ± 1.70</td> <!-- SUC3 -->
   <td class="sv sent">64.02 ± 2.78 / 62.27 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">0.80 ± 0.78 / 47.24 ± 3.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.46 ± 0.90 / 33.13 ± 0.88</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">28.27 ± 6.86 / 29.90 ± 7.25</td> <!-- DANSK -->
   <td class="da sent">19.79 ± 1.67 / 42.09 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">6.15 ± 1.66 / 52.04 ± 1.49</td> <!-- ScaLA-da -->
   <td class="da qa">15.96 ± 2.06 / 21.55 ± 2.17</td> <!-- ScandiQA-da -->
   <td class="no ner">62.99 ± 1.05 / 66.97 ± 1.30</td> <!-- NorNE-nb -->
   <td class="no ner">59.95 ± 2.51 / 63.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">18.85 ± 4.01 / 36.76 ± 2.79</td> <!-- NoReC -->
   <td class="no la">5.83 ± 2.36 / 51.59 ± 1.57</td> <!-- ScaLA-nb -->
   <td class="no la">4.02 ± 2.29 / 51.66 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">23.07 ± 2.29 / 28.36 ± 2.26</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.34 ± 8.27 / 47.19 ± 9.01</td> <!-- SUC3 -->
   <td class="sv sent">56.57 ± 1.41 / 53.47 ± 0.84</td> <!-- SweReC -->
   <td class="sv la">20.92 ± 4.12 / 59.05 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">23.86 ± 1.25 / 30.47 ± 1.51</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,319 ± 94 / 656 ± 172</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">15.60 ± 2.62 / 16.04 ± 2.47</td> <!-- DANSK -->
   <td class="da sent">17.37 ± 3.82 / 36.83 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">1.34 ± 0.97 / 35.45 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da qa">1.58 ± 0.51 / 6.64 ± 1.56</td> <!-- ScandiQA-da -->
   <td class="no ner">23.54 ± 3.23 / 25.49 ± 3.39</td> <!-- NorNE-nb -->
   <td class="no ner">24.10 ± 1.64 / 25.94 ± 1.70</td> <!-- NorNE-nn -->
   <td class="no sent">12.60 ± 2.97 / 32.27 ± 3.43</td> <!-- NoReC -->
   <td class="no la">0.50 ± 1.27 / 36.93 ± 4.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.83 ± 1.64 / 37.67 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">1.55 ± 0.69 / 5.88 ± 2.00</td> <!-- ScandiQA-no -->
   <td class="sv ner">11.31 ± 2.90 / 11.91 ± 3.04</td> <!-- SUC3 -->
   <td class="sv sent">51.11 ± 5.32 / 50.09 ± 3.33</td> <!-- SweReC -->
   <td class="sv la">0.86 ± 0.82 / 39.16 ± 3.63</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.00 ± 0.63 / 7.20 ± 1.68</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,219 ± 712 / 3,276 ± 803</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">13.23 ± 1.55 / 12.87 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">18.61 ± 4.17 / 35.23 ± 3.90</td> <!-- Angry Tweets -->
   <td class="da la">0.30 ± 1.39 / 37.84 ± 3.88</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">17.08 ± 1.97 / 18.38 ± 2.01</td> <!-- NorNE-nb -->
   <td class="no ner">11.65 ± 1.21 / 12.76 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">15.29 ± 5.37 / 34.15 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.17 ± 0.84 / 36.29 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.37 ± 0.69 / 35.08 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-no -->
   <td class="sv ner">9.71 ± 1.00 / 10.54 ± 1.12</td> <!-- SUC3 -->
   <td class="sv sent">55.54 ± 2.75 / 52.75 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">-0.15 ± 0.52 / 35.33 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.02 ± 0.03 / 0.04 ± 0.05</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.25 ± 1.47 / 71.90 ± 1.08</td> <!-- DANSK -->
   <td class="da sent">51.33 ± 1.24 / 67.04 ± 1.22</td> <!-- Angry Tweets -->
   <td class="da la">44.45 ± 19.17 / 70.51 ± 10.21</td> <!-- ScaLA-da -->
   <td class="da qa">32.51 ± 0.79 / 37.00 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="no ner">89.26 ± 0.97 / 91.66 ± 0.74</td> <!-- NorNE-nb -->
   <td class="no ner">84.51 ± 1.03 / 87.74 ± 0.77</td> <!-- NorNE-nn -->
   <td class="no sent">57.43 ± 1.55 / 70.43 ± 1.41</td> <!-- NoReC -->
   <td class="no la">63.31 ± 11.58 / 80.18 ± 5.59</td> <!-- ScaLA-nb -->
   <td class="no la">62.79 ± 11.35 / 79.65 ± 6.48</td> <!-- ScaLA-nn -->
   <td class="no qa">41.05 ± 2.59 / 54.44 ± 3.33</td> <!-- NorQuAD -->
   <td class="no qa">30.63 ± 1.77 / 34.98 ± 1.76</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.45 ± 0.86 / 79.75 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">74.73 ± 1.15 / 70.83 ± 3.72</td> <!-- SweReC -->
   <td class="sv la">53.55 ± 16.68 / 75.79 ± 8.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.20 ± 0.86 / 36.88 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.85 ± 1.93 / 71.81 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.22 / 64.90 ± 0.81</td> <!-- Angry Tweets -->
   <td class="da la">54.99 ± 11.90 / 75.82 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.92 ± 0.98 / 34.74 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">87.83 ± 1.34 / 90.60 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">83.48 ± 0.98 / 86.76 ± 0.82</td> <!-- NorNE-nn -->
   <td class="no sent">52.19 ± 2.87 / 65.60 ± 2.58</td> <!-- NoReC -->
   <td class="no la">54.98 ± 14.19 / 75.67 ± 6.70</td> <!-- ScaLA-nb -->
   <td class="no la">58.33 ± 10.94 / 77.88 ± 5.29</td> <!-- ScaLA-nn -->
   <td class="no qa">29.17 ± 1.36 / 41.75 ± 1.59</td> <!-- NorQuAD -->
   <td class="no qa">27.83 ± 1.27 / 32.42 ± 1.29</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.10 ± 0.94 / 77.97 ± 0.82</td> <!-- SUC3 -->
   <td class="sv sent">73.27 ± 0.75 / 71.87 ± 1.30</td> <!-- SweReC -->
   <td class="sv la">47.19 ± 16.37 / 72.10 ± 8.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.07 ± 0.93 / 36.17 ± 0.73</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.31 ± 1.47 / 60.59 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">29.52 ± 2.89 / 47.81 ± 4.54</td> <!-- Angry Tweets -->
   <td class="da la">57.10 ± 2.02 / 78.14 ± 1.10</td> <!-- ScaLA-da -->
   <td class="da qa">20.16 ± 0.73 / 25.69 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="no ner">72.78 ± 1.16 / 76.07 ± 1.18</td> <!-- NorNE-nb -->
   <td class="no ner">66.73 ± 1.21 / 70.94 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">32.49 ± 1.55 / 43.12 ± 0.71</td> <!-- NoReC -->
   <td class="no la">35.43 ± 2.39 / 66.84 ± 1.17</td> <!-- ScaLA-nb -->
   <td class="no la">21.11 ± 1.97 / 60.09 ± 0.93</td> <!-- ScaLA-nn -->
   <td class="no qa">1.84 ± 2.41 / 2.78 ± 3.65</td> <!-- NorQuAD -->
   <td class="no qa">21.73 ± 0.91 / 26.66 ± 0.95</td> <!-- ScandiQA-no -->
   <td class="sv ner">51.37 ± 1.03 / 55.06 ± 0.96</td> <!-- SUC3 -->
   <td class="sv sent">53.70 ± 1.46 / 51.98 ± 0.58</td> <!-- SweReC -->
   <td class="sv la">12.38 ± 3.23 / 55.18 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">22.53 ± 0.86 / 27.59 ± 0.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">54.75 ± 1.23 / 57.84 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">31.18 ± 0.94 / 53.05 ± 1.16</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 3.71 / 53.61 ± 2.94</td> <!-- ScaLA-da -->
   <td class="da qa">22.73 ± 1.16 / 27.50 ± 1.00</td> <!-- ScandiQA-da -->
   <td class="no ner">78.30 ± 1.00 / 81.82 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">72.08 ± 1.15 / 75.89 ± 1.11</td> <!-- NorNE-nn -->
   <td class="no sent">33.42 ± 1.96 / 48.63 ± 3.34</td> <!-- NoReC -->
   <td class="no la">14.99 ± 4.11 / 52.87 ± 4.48</td> <!-- ScaLA-nb -->
   <td class="no la">13.63 ± 4.52 / 53.34 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">25.23 ± 1.62 / 29.07 ± 1.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.78 ± 1.37 / 80.12 ± 1.41</td> <!-- SUC3 -->
   <td class="sv sent">71.28 ± 1.09 / 69.73 ± 2.94</td> <!-- SweReC -->
   <td class="sv la">51.58 ± 2.89 / 73.82 ± 2.21</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.16 ± 0.76 / 33.47 ± 0.62</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">45.91 ± 1.91 / 47.61 ± 1.71</td> <!-- DANSK -->
   <td class="da sent">24.17 ± 1.92 / 43.75 ± 2.75</td> <!-- Angry Tweets -->
   <td class="da la">8.14 ± 3.76 / 51.78 ± 1.81</td> <!-- ScaLA-da -->
   <td class="da qa">25.19 ± 1.29 / 30.51 ± 1.06</td> <!-- ScandiQA-da -->
   <td class="no ner">64.83 ± 1.55 / 68.63 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">63.70 ± 2.54 / 67.70 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">25.68 ± 2.17 / 41.65 ± 2.77</td> <!-- NoReC -->
   <td class="no la">6.73 ± 5.40 / 48.20 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">3.35 ± 2.61 / 47.52 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">22.57 ± 1.57 / 34.64 ± 1.94</td> <!-- NorQuAD -->
   <td class="no qa">26.84 ± 1.19 / 31.38 ± 1.36</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.29 ± 1.48 / 68.83 ± 1.00</td> <!-- SUC3 -->
   <td class="sv sent">64.25 ± 1.66 / 63.62 ± 2.92</td> <!-- SweReC -->
   <td class="sv la">28.62 ± 9.43 / 59.33 ± 5.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.78 ± 2.01 / 34.26 ± 2.03</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.20 ± 1.94 / 69.79 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.45 / 64.85 ± 1.13</td> <!-- Angry Tweets -->
   <td class="da la">68.28 ± 1.77 / 83.52 ± 1.02</td> <!-- ScaLA-da -->
   <td class="da qa">31.90 ± 2.50 / 37.07 ± 2.36</td> <!-- ScandiQA-da -->
   <td class="no ner">88.45 ± 0.70 / 91.09 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">81.88 ± 2.16 / 85.72 ± 1.92</td> <!-- NorNE-nn -->
   <td class="no sent">50.90 ± 3.01 / 60.96 ± 5.41</td> <!-- NoReC -->
   <td class="no la">69.34 ± 3.13 / 83.11 ± 2.17</td> <!-- ScaLA-nb -->
   <td class="no la">66.24 ± 2.41 / 82.36 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">48.45 ± 0.63 / 62.96 ± 0.80</td> <!-- NorQuAD -->
   <td class="no qa">32.38 ± 2.54 / 36.60 ± 2.64</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.06 ± 2.01 / 79.08 ± 2.32</td> <!-- SUC3 -->
   <td class="sv sent">72.53 ± 0.98 / 67.74 ± 3.02</td> <!-- SweReC -->
   <td class="sv la">73.01 ± 1.43 / 85.98 ± 0.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.92 ± 2.25 / 41.99 ± 2.38</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.83 ± 2.08 / 69.78 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">46.78 ± 1.57 / 64.46 ± 1.17</td> <!-- Angry Tweets -->
   <td class="da la">11.27 ± 2.21 / 51.47 ± 2.07</td> <!-- ScaLA-da -->
   <td class="da qa">28.28 ± 4.63 / 33.33 ± 4.10</td> <!-- ScandiQA-da -->
   <td class="no ner">87.71 ± 1.24 / 90.14 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">80.21 ± 2.19 / 84.12 ± 1.85</td> <!-- NorNE-nn -->
   <td class="no sent">44.42 ± 13.10 / 57.73 ± 11.86</td> <!-- NoReC -->
   <td class="no la">11.20 ± 2.99 / 48.77 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">7.12 ± 2.39 / 49.23 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">47.69 ± 1.95 / 62.39 ± 1.74</td> <!-- NorQuAD -->
   <td class="no qa">31.45 ± 1.86 / 35.85 ± 1.72</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.17 ± 1.10 / 79.43 ± 1.07</td> <!-- SUC3 -->
   <td class="sv sent">71.48 ± 2.63 / 65.72 ± 4.78</td> <!-- SweReC -->
   <td class="sv la">7.26 ± 2.18 / 45.42 ± 4.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.72 ± 1.71 / 38.23 ± 1.57</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.41 ± 2.11 / 61.17 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">46.39 ± 1.25 / 63.97 ± 1.08</td> <!-- Angry Tweets -->
   <td class="da la">38.61 ± 1.86 / 67.08 ± 1.08</td> <!-- ScaLA-da -->
   <td class="da qa">19.90 ± 1.09 / 25.77 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="no ner">77.69 ± 1.29 / 81.26 ± 1.25</td> <!-- NorNE-nb -->
   <td class="no ner">69.84 ± 1.91 / 74.05 ± 1.72</td> <!-- NorNE-nn -->
   <td class="no sent">49.93 ± 1.46 / 62.37 ± 2.34</td> <!-- NoReC -->
   <td class="no la">38.26 ± 7.56 / 66.01 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">25.17 ± 5.32 / 61.27 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">20.52 ± 0.96 / 25.78 ± 0.93</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.97 ± 1.48 / 70.22 ± 1.49</td> <!-- SUC3 -->
   <td class="sv sent">71.33 ± 1.20 / 65.44 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">39.60 ± 5.87 / 66.60 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.65 ± 1.15 / 24.75 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">52.85 ± 2.28 / 54.48 ± 2.16</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">13.97 ± 1.75 / 19.76 ± 2.26</td> <!-- ScandiQA-da -->
   <td class="no ner">74.83 ± 0.79 / 77.81 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">68.32 ± 1.13 / 72.22 ± 0.95</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">18.99 ± 0.92 / 25.41 ± 0.94</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.72 ± 1.22 / 65.50 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">68.36 ± 1.18 / 63.94 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.09 ± 1.52 / 61.74 ± 1.46</td> <!-- DANSK -->
   <td class="da sent">33.31 ± 1.49 / 54.09 ± 1.49</td> <!-- Angry Tweets -->
   <td class="da la">33.35 ± 7.32 / 64.61 ± 4.56</td> <!-- ScaLA-da -->
   <td class="da qa">28.67 ± 0.79 / 33.03 ± 0.87</td> <!-- ScandiQA-da -->
   <td class="no ner">82.13 ± 1.28 / 85.33 ± 1.01</td> <!-- NorNE-nb -->
   <td class="no ner">75.74 ± 1.96 / 79.44 ± 1.66</td> <!-- NorNE-nn -->
   <td class="no sent">38.17 ± 2.21 / 50.44 ± 3.11</td> <!-- NoReC -->
   <td class="no la">39.49 ± 3.36 / 68.13 ± 2.13</td> <!-- ScaLA-nb -->
   <td class="no la">22.17 ± 7.22 / 60.16 ± 3.80</td> <!-- ScaLA-nn -->
   <td class="no qa">19.04 ± 4.63 / 27.73 ± 6.70</td> <!-- NorQuAD -->
   <td class="no qa">31.24 ± 1.57 / 35.41 ± 1.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.95 ± 1.72 / 81.23 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">75.73 ± 0.72 / 73.61 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">78.60 ± 0.98 / 88.95 ± 0.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.29 ± 1.54 / 64.28 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">36.85 ± 3.28 / 56.27 ± 3.98</td> <!-- Angry Tweets -->
   <td class="da la">63.55 ± 1.19 / 81.41 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">24.52 ± 1.11 / 29.88 ± 1.13</td> <!-- ScandiQA-da -->
   <td class="no ner">76.09 ± 0.70 / 79.50 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.39 / 73.03 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">32.40 ± 1.48 / 44.59 ± 1.66</td> <!-- NoReC -->
   <td class="no la">41.65 ± 1.95 / 70.35 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">25.53 ± 2.31 / 62.04 ± 1.19</td> <!-- ScaLA-nn -->
   <td class="no qa">5.41 ± 2.79 / 8.15 ± 4.18</td> <!-- NorQuAD -->
   <td class="no qa">25.09 ± 0.59 / 30.02 ± 0.79</td> <!-- ScandiQA-no -->
   <td class="sv ner">53.87 ± 1.25 / 58.01 ± 1.23</td> <!-- SUC3 -->
   <td class="sv sent">57.67 ± 1.61 / 53.64 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">13.40 ± 4.31 / 55.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.92 ± 0.80 / 30.11 ± 0.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">52.85 ± 2.28 / 54.48 ± 2.16</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">15.42 ± 1.70 / 21.36 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">74.83 ± 0.79 / 77.81 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">68.32 ± 1.13 / 72.22 ± 0.95</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">19.65 ± 0.69 / 25.92 ± 0.69</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.72 ± 1.22 / 65.50 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">68.33 ± 1.03 / 64.03 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">32.76 ± 1.02 / 32.63 ± 1.06</td> <!-- DANSK -->
   <td class="da sent">24.11 ± 1.74 / 44.78 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">2.91 ± 1.07 / 46.98 ± 3.78</td> <!-- ScaLA-da -->
   <td class="da qa">15.37 ± 1.22 / 22.17 ± 1.24</td> <!-- ScandiQA-da -->
   <td class="no ner">46.11 ± 1.04 / 49.30 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">43.01 ± 2.05 / 46.11 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">23.21 ± 2.32 / 44.26 ± 2.95</td> <!-- NoReC -->
   <td class="no la">2.26 ± 1.47 / 45.07 ± 4.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.66 ± 1.81 / 44.50 ± 3.45</td> <!-- ScaLA-nn -->
   <td class="no qa">0.68 ± 0.32 / 1.50 ± 0.80</td> <!-- NorQuAD -->
   <td class="no qa">14.08 ± 1.18 / 21.85 ± 1.31</td> <!-- ScandiQA-no -->
   <td class="sv ner">46.67 ± 1.98 / 51.13 ± 2.13</td> <!-- SUC3 -->
   <td class="sv sent">61.67 ± 1.40 / 59.12 ± 2.44</td> <!-- SweReC -->
   <td class="sv la">2.87 ± 1.53 / 48.92 ± 2.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.24 ± 1.13 / 25.10 ± 1.06</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">36.31 ± 2.71 / 36.51 ± 2.44</td> <!-- DANSK -->
   <td class="da sent">22.07 ± 2.24 / 44.70 ± 3.72</td> <!-- Angry Tweets -->
   <td class="da la">1.63 ± 1.49 / 45.36 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da qa">3.09 ± 1.00 / 9.48 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">52.52 ± 3.51 / 55.55 ± 3.71</td> <!-- NorNE-nb -->
   <td class="no ner">50.23 ± 3.00 / 53.53 ± 3.03</td> <!-- NorNE-nn -->
   <td class="no sent">12.69 ± 4.51 / 32.23 ± 3.53</td> <!-- NoReC -->
   <td class="no la">2.79 ± 1.16 / 47.71 ± 2.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.66 ± 2.18 / 46.60 ± 2.87</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.60 ± 0.72</td> <!-- NorQuAD -->
   <td class="no qa">10.25 ± 2.57 / 17.71 ± 2.28</td> <!-- ScandiQA-no -->
   <td class="sv ner">40.46 ± 3.04 / 42.78 ± 3.26</td> <!-- SUC3 -->
   <td class="sv sent">44.95 ± 2.30 / 48.17 ± 1.06</td> <!-- SweReC -->
   <td class="sv la">1.43 ± 1.34 / 48.66 ± 2.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.71 ± 2.58 / 16.77 ± 2.50</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">46.74 ± 1.94 / 49.88 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">27.93 ± 0.66 / 50.86 ± 0.42</td> <!-- Angry Tweets -->
   <td class="da la">5.42 ± 2.85 / 48.29 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">22.93 ± 0.81 / 28.62 ± 0.62</td> <!-- ScandiQA-da -->
   <td class="no ner">66.15 ± 1.66 / 69.65 ± 1.48</td> <!-- NorNE-nb -->
   <td class="no ner">62.75 ± 1.40 / 66.78 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">26.33 ± 1.84 / 40.67 ± 0.71</td> <!-- NoReC -->
   <td class="no la">6.62 ± 3.40 / 48.37 ± 4.02</td> <!-- ScaLA-nb -->
   <td class="no la">5.16 ± 3.07 / 45.99 ± 4.76</td> <!-- ScaLA-nn -->
   <td class="no qa">15.75 ± 1.30 / 27.15 ± 1.91</td> <!-- NorQuAD -->
   <td class="no qa">23.02 ± 1.21 / 28.39 ± 1.10</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.03 ± 1.08 / 66.11 ± 1.24</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.84 / 55.24 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">26.28 ± 8.44 / 59.64 ± 5.68</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.36 ± 0.92 / 30.54 ± 0.96</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.60 ± 1.78 / 62.66 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">33.91 ± 1.43 / 54.87 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">40.96 ± 4.05 / 69.68 ± 2.12</td> <!-- ScaLA-da -->
   <td class="da qa">39.93 ± 2.55 / 44.63 ± 2.71</td> <!-- ScandiQA-da -->
   <td class="no ner">85.89 ± 1.04 / 89.07 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">79.22 ± 0.93 / 82.69 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">34.97 ± 1.74 / 48.21 ± 2.02</td> <!-- NoReC -->
   <td class="no la">39.58 ± 5.70 / 67.91 ± 3.00</td> <!-- ScaLA-nb -->
   <td class="no la">31.27 ± 9.57 / 62.81 ± 7.17</td> <!-- ScaLA-nn -->
   <td class="no qa">41.89 ± 1.64 / 55.17 ± 2.07</td> <!-- NorQuAD -->
   <td class="no qa">39.57 ± 1.25 / 44.13 ± 1.37</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.89 ± 0.52 / 75.33 ± 0.99</td> <!-- SUC3 -->
   <td class="sv sent">61.80 ± 1.76 / 58.93 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 5.98 / 66.91 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.95 ± 1.95 / 44.71 ± 1.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">31.68 ± 1.05 / 33.05 ± 1.28</td> <!-- DANSK -->
   <td class="da sent">30.67 ± 1.28 / 51.76 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">13.01 ± 5.22 / 55.11 ± 3.40</td> <!-- ScaLA-da -->
   <td class="da qa">1.56 ± 0.88 / 5.30 ± 2.21</td> <!-- ScandiQA-da -->
   <td class="no ner">39.53 ± 1.04 / 42.18 ± 1.03</td> <!-- NorNE-nb -->
   <td class="no ner">34.88 ± 1.76 / 37.39 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">24.39 ± 1.60 / 40.44 ± 1.78</td> <!-- NoReC -->
   <td class="no la">7.29 ± 2.49 / 49.37 ± 3.58</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 46.00 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">0.32 ± 0.21 / 1.97 ± 0.91</td> <!-- ScandiQA-no -->
   <td class="sv ner">20.74 ± 1.42 / 22.47 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">53.88 ± 1.97 / 52.30 ± 1.04</td> <!-- SweReC -->
   <td class="sv la">1.55 ± 1.62 / 44.06 ± 3.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">1.12 ± 0.85 / 3.07 ± 1.91</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.53 ± 1.53 / 71.34 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">49.77 ± 0.92 / 66.38 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">64.31 ± 2.24 / 80.70 ± 1.53</td> <!-- ScaLA-da -->
   <td class="da qa">31.86 ± 1.88 / 37.00 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">88.71 ± 0.94 / 91.16 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">80.56 ± 1.59 / 84.75 ± 1.23</td> <!-- NorNE-nn -->
   <td class="no sent">55.25 ± 2.36 / 66.95 ± 2.79</td> <!-- NoReC -->
   <td class="no la">68.03 ± 2.37 / 82.12 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">66.90 ± 2.07 / 82.33 ± 1.34</td> <!-- ScaLA-nn -->
   <td class="no qa">41.65 ± 1.17 / 55.71 ± 1.73</td> <!-- NorQuAD -->
   <td class="no qa">30.36 ± 1.29 / 34.88 ± 1.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.89 ± 2.16 / 74.48 ± 2.35</td> <!-- SUC3 -->
   <td class="sv sent">74.58 ± 1.29 / 70.97 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">69.07 ± 2.22 / 83.17 ± 1.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.66 ± 1.18 / 37.05 ± 1.10</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">64.34 ± 2.02 / 68.46 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">50.48 ± 0.68 / 66.71 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">64.34 ± 2.43 / 80.92 ± 1.67</td> <!-- ScaLA-da -->
   <td class="da qa">30.30 ± 1.40 / 35.30 ± 1.16</td> <!-- ScandiQA-da -->
   <td class="no ner">85.81 ± 1.57 / 89.07 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">78.80 ± 2.22 / 83.27 ± 1.68</td> <!-- NorNE-nn -->
   <td class="no sent">53.23 ± 1.67 / 65.23 ± 2.65</td> <!-- NoReC -->
   <td class="no la">70.06 ± 2.33 / 83.61 ± 1.61</td> <!-- ScaLA-nb -->
   <td class="no la">66.81 ± 1.83 / 82.19 ± 1.20</td> <!-- ScaLA-nn -->
   <td class="no qa">34.17 ± 2.16 / 47.61 ± 2.55</td> <!-- NorQuAD -->
   <td class="no qa">30.11 ± 1.51 / 34.60 ± 1.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.94 ± 2.04 / 72.25 ± 2.16</td> <!-- SUC3 -->
   <td class="sv sent">75.04 ± 1.08 / 72.35 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">70.16 ± 1.47 / 84.29 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.89 ± 0.99 / 36.93 ± 0.90</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.94 ± 1.56 / 61.18 ± 1.22</td> <!-- DANSK -->
   <td class="da sent">49.13 ± 0.82 / 65.84 ± 0.66</td> <!-- Angry Tweets -->
   <td class="da la">29.66 ± 7.69 / 63.05 ± 4.35</td> <!-- ScaLA-da -->
   <td class="da qa">19.99 ± 1.65 / 26.42 ± 1.77</td> <!-- ScandiQA-da -->
   <td class="no ner">78.39 ± 0.86 / 81.94 ± 0.73</td> <!-- NorNE-nb -->
   <td class="no ner">71.27 ± 1.18 / 75.56 ± 1.01</td> <!-- NorNE-nn -->
   <td class="no sent">55.53 ± 1.05 / 68.89 ± 1.16</td> <!-- NoReC -->
   <td class="no la">36.01 ± 2.02 / 64.39 ± 1.49</td> <!-- ScaLA-nb -->
   <td class="no la">14.99 ± 8.03 / 54.08 ± 5.71</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">19.58 ± 1.78 / 25.70 ± 1.87</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.82 ± 1.39 / 65.14 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">73.47 ± 0.84 / 70.20 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 6.55 / 66.09 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">18.65 ± 0.91 / 25.00 ± 0.87</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">64.72 ± 2.02 / 68.49 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">45.60 ± 1.76 / 63.53 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">28.26 ± 11.88 / 55.28 ± 7.93</td> <!-- ScaLA-da -->
   <td class="da qa">14.34 ± 3.95 / 18.60 ± 5.02</td> <!-- ScandiQA-da -->
   <td class="no ner">86.62 ± 1.53 / 89.46 ± 1.18</td> <!-- NorNE-nb -->
   <td class="no ner">75.64 ± 1.17 / 79.71 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">52.91 ± 2.29 / 64.64 ± 3.28</td> <!-- NoReC -->
   <td class="no la">27.55 ± 12.16 / 53.28 ± 8.27</td> <!-- ScaLA-nb -->
   <td class="no la">15.20 ± 9.06 / 51.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">12.36 ± 8.54 / 17.38 ± 11.78</td> <!-- NorQuAD -->
   <td class="no qa">7.98 ± 5.51 / 9.88 ± 6.71</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.91 ± 1.27 / 76.31 ± 1.29</td> <!-- SUC3 -->
   <td class="sv sent">73.32 ± 1.13 / 70.21 ± 3.74</td> <!-- SweReC -->
   <td class="sv la">32.29 ± 10.98 / 62.21 ± 5.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.12 ± 5.80 / 19.52 ± 6.73</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">56.90 ± 1.49 / 60.63 ± 1.32</td> <!-- DANSK -->
   <td class="da sent">24.38 ± 1.74 / 40.85 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">68.58 ± 1.38 / 84.12 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">21.03 ± 1.09 / 27.53 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="no ner">70.05 ± 1.16 / 73.15 ± 1.21</td> <!-- NorNE-nb -->
   <td class="no ner">62.07 ± 1.31 / 66.34 ± 1.25</td> <!-- NorNE-nn -->
   <td class="no sent">29.97 ± 0.99 / 42.12 ± 0.47</td> <!-- NoReC -->
   <td class="no la">40.79 ± 2.06 / 69.48 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">25.08 ± 1.86 / 61.74 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">1.93 ± 2.05 / 3.62 ± 3.99</td> <!-- NorQuAD -->
   <td class="no qa">19.68 ± 0.53 / 25.51 ± 0.61</td> <!-- ScandiQA-no -->
   <td class="sv ner">48.47 ± 0.71 / 52.79 ± 1.21</td> <!-- SUC3 -->
   <td class="sv sent">57.93 ± 1.56 / 53.71 ± 0.61</td> <!-- SweReC -->
   <td class="sv la">14.72 ± 2.01 / 55.92 ± 1.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.54 ± 0.97 / 26.37 ± 0.75</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.80 ± 1.78 / 69.17 ± 2.07</td> <!-- DANSK -->
   <td class="da sent">48.03 ± 0.74 / 65.34 ± 0.40</td> <!-- Angry Tweets -->
   <td class="da la">55.31 ± 2.29 / 76.29 ± 1.57</td> <!-- ScaLA-da -->
   <td class="da qa">42.34 ± 3.05 / 47.57 ± 3.10</td> <!-- ScandiQA-da -->
   <td class="no ner">87.12 ± 1.08 / 90.08 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">81.89 ± 0.98 / 86.04 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">56.35 ± 1.25 / 69.31 ± 1.02</td> <!-- NoReC -->
   <td class="no la">59.38 ± 2.52 / 78.02 ± 1.71</td> <!-- ScaLA-nb -->
   <td class="no la">46.54 ± 3.21 / 71.78 ± 2.00</td> <!-- ScaLA-nn -->
   <td class="no qa">55.05 ± 1.24 / 70.46 ± 1.22</td> <!-- NorQuAD -->
   <td class="no qa">42.03 ± 1.04 / 47.38 ± 0.99</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.21 ± 1.26 / 80.05 ± 1.13</td> <!-- SUC3 -->
   <td class="sv sent">75.09 ± 1.30 / 72.93 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">61.83 ± 1.28 / 79.96 ± 0.82</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.69 ± 1.11 / 51.07 ± 1.04</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.54 ± 1.52 / 74.42 ± 1.81</td> <!-- DANSK -->
   <td class="da sent">37.94 ± 10.08 / 55.77 ± 9.21</td> <!-- Angry Tweets -->
   <td class="da la">15.26 ± 10.94 / 48.92 ± 8.26</td> <!-- ScaLA-da -->
   <td class="da qa">44.25 ± 2.55 / 50.10 ± 2.75</td> <!-- ScandiQA-da -->
   <td class="no ner">89.48 ± 0.83 / 91.90 ± 0.62</td> <!-- NorNE-nb -->
   <td class="no ner">82.92 ± 1.66 / 86.59 ± 1.49</td> <!-- NorNE-nn -->
   <td class="no sent">30.56 ± 13.68 / 45.96 ± 11.45</td> <!-- NoReC -->
   <td class="no la">9.79 ± 5.13 / 46.75 ± 6.05</td> <!-- ScaLA-nb -->
   <td class="no la">6.36 ± 2.82 / 48.52 ± 4.11</td> <!-- ScaLA-nn -->
   <td class="no qa">60.47 ± 1.01 / 74.70 ± 0.92</td> <!-- NorQuAD -->
   <td class="no qa">46.35 ± 0.85 / 51.65 ± 0.79</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.53 ± 2.70 / 79.53 ± 2.77</td> <!-- SUC3 -->
   <td class="sv sent">75.42 ± 1.08 / 72.68 ± 3.19</td> <!-- SweReC -->
   <td class="sv la">18.44 ± 10.88 / 53.57 ± 7.20</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.19 ± 1.10 / 53.67 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">62.24 ± 1.29 / 66.39 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">39.36 ± 3.13 / 58.64 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">7.06 ± 6.11 / 49.71 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">33.88 ± 4.27 / 38.42 ± 4.16</td> <!-- ScandiQA-da -->
   <td class="no ner">83.48 ± 1.19 / 86.26 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">76.17 ± 2.67 / 80.10 ± 2.44</td> <!-- NorNE-nn -->
   <td class="no sent">34.17 ± 2.42 / 43.74 ± 2.19</td> <!-- NoReC -->
   <td class="no la">12.11 ± 10.47 / 50.33 ± 7.16</td> <!-- ScaLA-nb -->
   <td class="no la">4.28 ± 4.18 / 45.75 ± 4.32</td> <!-- ScaLA-nn -->
   <td class="no qa">11.74 ± 10.45 / 16.38 ± 14.33</td> <!-- NorQuAD -->
   <td class="no qa">36.15 ± 2.57 / 40.88 ± 2.63</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.20 ± 1.70 / 74.26 ± 1.65</td> <!-- SUC3 -->
   <td class="sv sent">63.35 ± 5.43 / 60.33 ± 5.50</td> <!-- SweReC -->
   <td class="sv la">16.07 ± 10.73 / 52.48 ± 7.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.77 ± 3.78 / 41.72 ± 3.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.64 ± 2.68 / 70.19 ± 3.34</td> <!-- DANSK -->
   <td class="da sent">50.19 ± 1.82 / 66.32 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">69.72 ± 2.25 / 84.30 ± 1.64</td> <!-- ScaLA-da -->
   <td class="da qa">39.85 ± 8.97 / 44.44 ± 9.99</td> <!-- ScandiQA-da -->
   <td class="no ner">84.95 ± 2.83 / 88.70 ± 2.05</td> <!-- NorNE-nb -->
   <td class="no ner">82.16 ± 1.96 / 86.11 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">54.19 ± 3.15 / 65.18 ± 4.55</td> <!-- NoReC -->
   <td class="no la">69.83 ± 2.01 / 84.72 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">54.84 ± 12.59 / 75.13 ± 9.44</td> <!-- ScaLA-nn -->
   <td class="no qa">58.18 ± 1.84 / 71.29 ± 1.51</td> <!-- NorQuAD -->
   <td class="no qa">43.32 ± 2.00 / 48.35 ± 1.95</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.58 ± 1.51 / 78.23 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">75.99 ± 1.15 / 71.01 ± 4.17</td> <!-- SweReC -->
   <td class="sv la">72.17 ± 0.94 / 85.94 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.00 ± 2.13 / 51.05 ± 2.40</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">60.82 ± 1.86 / 64.92 ± 2.17</td> <!-- DANSK -->
   <td class="da sent">33.50 ± 2.57 / 54.63 ± 2.14</td> <!-- Angry Tweets -->
   <td class="da la">46.75 ± 3.43 / 72.71 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">37.09 ± 2.08 / 41.77 ± 2.25</td> <!-- ScandiQA-da -->
   <td class="no ner">79.06 ± 1.52 / 82.90 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">72.83 ± 1.96 / 77.33 ± 2.00</td> <!-- NorNE-nn -->
   <td class="no sent">37.28 ± 2.13 / 48.69 ± 3.26</td> <!-- NoReC -->
   <td class="no la">49.41 ± 1.57 / 73.96 ± 0.87</td> <!-- ScaLA-nb -->
   <td class="no la">43.58 ± 2.23 / 71.20 ± 1.61</td> <!-- ScaLA-nn -->
   <td class="no qa">40.35 ± 2.26 / 54.01 ± 2.42</td> <!-- NorQuAD -->
   <td class="no qa">36.91 ± 1.69 / 41.55 ± 1.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.50 ± 1.71 / 70.85 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">63.30 ± 0.93 / 59.96 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">48.97 ± 1.14 / 73.78 ± 0.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.00 ± 1.52 / 42.69 ± 1.62</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">54.43 ± 1.91 / 57.53 ± 1.89</td> <!-- DANSK -->
   <td class="da sent">32.95 ± 0.82 / 54.57 ± 0.80</td> <!-- Angry Tweets -->
   <td class="da la">33.63 ± 2.63 / 65.69 ± 1.82</td> <!-- ScaLA-da -->
   <td class="da qa">27.21 ± 1.31 / 32.05 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">81.01 ± 0.94 / 83.93 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">75.07 ± 1.03 / 79.39 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">32.32 ± 2.30 / 47.12 ± 2.85</td> <!-- NoReC -->
   <td class="no la">36.15 ± 1.99 / 66.57 ± 1.11</td> <!-- ScaLA-nb -->
   <td class="no la">30.17 ± 1.72 / 63.98 ± 1.36</td> <!-- ScaLA-nn -->
   <td class="no qa">19.71 ± 1.41 / 30.26 ± 1.56</td> <!-- NorQuAD -->
   <td class="no qa">28.51 ± 1.04 / 32.56 ± 0.99</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.61 ± 1.27 / 69.28 ± 1.15</td> <!-- SUC3 -->
   <td class="sv sent">59.53 ± 1.69 / 57.93 ± 2.20</td> <!-- SweReC -->
   <td class="sv la">29.36 ± 1.50 / 63.60 ± 0.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.42 ± 1.54 / 35.34 ± 1.63</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">38.74 ± 1.82 / 41.70 ± 1.80</td> <!-- DANSK -->
   <td class="da sent">26.03 ± 0.90 / 48.46 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.19 ± 1.92 / 49.80 ± 1.39</td> <!-- ScaLA-da -->
   <td class="da qa">13.82 ± 0.82 / 20.76 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">58.24 ± 1.47 / 61.55 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">56.03 ± 1.41 / 59.90 ± 1.56</td> <!-- NorNE-nn -->
   <td class="no sent">24.59 ± 1.57 / 40.34 ± 0.99</td> <!-- NoReC -->
   <td class="no la">3.45 ± 2.10 / 50.80 ± 1.16</td> <!-- ScaLA-nb -->
   <td class="no la">2.72 ± 1.56 / 48.79 ± 1.92</td> <!-- ScaLA-nn -->
   <td class="no qa">3.99 ± 2.02 / 7.49 ± 3.66</td> <!-- NorQuAD -->
   <td class="no qa">16.06 ± 1.03 / 23.06 ± 1.10</td> <!-- ScandiQA-no -->
   <td class="sv ner">47.04 ± 3.83 / 50.07 ± 4.14</td> <!-- SUC3 -->
   <td class="sv sent">56.10 ± 1.85 / 52.92 ± 0.76</td> <!-- SweReC -->
   <td class="sv la">5.05 ± 2.27 / 51.08 ± 1.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.49 ± 1.13 / 22.34 ± 1.16</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">21.70 ± 0.70 / 22.21 ± 0.75</td> <!-- DANSK -->
   <td class="da sent">20.33 ± 1.89 / 40.95 ± 2.78</td> <!-- Angry Tweets -->
   <td class="da la">0.90 ± 1.40 / 48.85 ± 2.60</td> <!-- ScaLA-da -->
   <td class="da qa">2.73 ± 0.64 / 7.23 ± 1.45</td> <!-- ScandiQA-da -->
   <td class="no ner">30.31 ± 2.14 / 31.87 ± 2.26</td> <!-- NorNE-nb -->
   <td class="no ner">30.59 ± 1.43 / 32.47 ± 1.48</td> <!-- NorNE-nn -->
   <td class="no sent">15.07 ± 1.97 / 35.80 ± 1.15</td> <!-- NoReC -->
   <td class="no la">1.26 ± 1.26 / 48.42 ± 1.75</td> <!-- ScaLA-nb -->
   <td class="no la">0.49 ± 1.58 / 45.93 ± 3.88</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="no qa">3.14 ± 0.53 / 9.05 ± 1.07</td> <!-- ScandiQA-no -->
   <td class="sv ner">23.05 ± 1.43 / 24.61 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">52.31 ± 1.22 / 51.51 ± 0.49</td> <!-- SweReC -->
   <td class="sv la">1.32 ± 1.87 / 46.80 ± 4.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.86 ± 0.73 / 8.44 ± 2.01</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">54.71 ± 1.72 / 57.97 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">39.40 ± 1.14 / 59.02 ± 0.60</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 1.86 / 59.54 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">31.87 ± 2.77 / 36.99 ± 2.78</td> <!-- ScandiQA-da -->
   <td class="no ner">79.13 ± 1.26 / 82.20 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">72.90 ± 1.43 / 76.64 ± 1.10</td> <!-- NorNE-nn -->
   <td class="no sent">40.20 ± 1.56 / 54.68 ± 2.46</td> <!-- NoReC -->
   <td class="no la">24.45 ± 2.21 / 58.75 ± 1.80</td> <!-- ScaLA-nb -->
   <td class="no la">19.18 ± 3.55 / 57.93 ± 2.05</td> <!-- ScaLA-nn -->
   <td class="no qa">30.69 ± 1.64 / 42.59 ± 1.94</td> <!-- NorQuAD -->
   <td class="no qa">31.43 ± 2.21 / 36.18 ± 2.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.93 ± 1.08 / 78.91 ± 1.24</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 0.81 / 72.74 ± 2.11</td> <!-- SweReC -->
   <td class="sv la">70.08 ± 2.11 / 83.40 ± 1.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.14 ± 1.18 / 47.18 ± 0.98</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">68.37 ± 1.73 / 73.28 ± 1.37</td> <!-- DANSK -->
   <td class="da sent">52.08 ± 1.06 / 67.98 ± 0.77</td> <!-- Angry Tweets -->
   <td class="da la">67.99 ± 2.28 / 83.02 ± 1.44</td> <!-- ScaLA-da -->
   <td class="da qa">32.39 ± 0.87 / 37.27 ± 0.79</td> <!-- ScandiQA-da -->
   <td class="no ner">89.66 ± 0.60 / 92.24 ± 0.44</td> <!-- NorNE-nb -->
   <td class="no ner">84.23 ± 0.85 / 87.58 ± 0.68</td> <!-- NorNE-nn -->
   <td class="no sent">59.98 ± 1.33 / 71.70 ± 1.69</td> <!-- NoReC -->
   <td class="no la">70.18 ± 1.41 / 83.83 ± 0.91</td> <!-- ScaLA-nb -->
   <td class="no la">70.81 ± 1.50 / 84.45 ± 0.95</td> <!-- ScaLA-nn -->
   <td class="no qa">44.27 ± 1.46 / 58.30 ± 1.82</td> <!-- NorQuAD -->
   <td class="no qa">31.84 ± 2.38 / 36.34 ± 2.11</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.04 ± 1.75 / 80.02 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 1.60 / 73.41 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">71.92 ± 1.07 / 85.01 ± 0.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.80 ± 0.78 / 38.58 ± 0.70</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">68.01 ± 1.69 / 72.16 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">51.70 ± 1.98 / 67.54 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">62.03 ± 11.56 / 80.01 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">29.95 ± 2.38 / 35.36 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">89.67 ± 0.54 / 92.09 ± 0.51</td> <!-- NorNE-nb -->
   <td class="no ner">83.35 ± 2.01 / 86.85 ± 1.94</td> <!-- NorNE-nn -->
   <td class="no sent">59.84 ± 1.40 / 72.11 ± 1.25</td> <!-- NoReC -->
   <td class="no la">73.33 ± 2.17 / 85.89 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">71.06 ± 1.62 / 84.78 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">43.67 ± 1.71 / 57.42 ± 1.56</td> <!-- NorQuAD -->
   <td class="no qa">29.83 ± 2.83 / 34.73 ± 2.38</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.80 ± 1.53 / 79.90 ± 1.41</td> <!-- SUC3 -->
   <td class="sv sent">76.20 ± 1.16 / 74.01 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">73.62 ± 1.17 / 86.19 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.38 ± 1.23 / 37.12 ± 1.20</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.61 ± 1.99 / 71.42 ± 2.68</td> <!-- DANSK -->
   <td class="da sent">31.86 ± 8.76 / 47.51 ± 8.94</td> <!-- Angry Tweets -->
   <td class="da la">52.95 ± 11.68 / 73.96 ± 8.89</td> <!-- ScaLA-da -->
   <td class="da qa">34.66 ± 1.64 / 40.58 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="no ner">87.51 ± 1.20 / 89.99 ± 1.32</td> <!-- NorNE-nb -->
   <td class="no ner">74.97 ± 3.56 / 78.60 ± 3.17</td> <!-- NorNE-nn -->
   <td class="no sent">17.93 ± 14.48 / 34.24 ± 10.14</td> <!-- NoReC -->
   <td class="no la">43.46 ± 17.47 / 66.52 ± 12.26</td> <!-- ScaLA-nb -->
   <td class="no la">10.97 ± 10.84 / 43.47 ± 9.81</td> <!-- ScaLA-nn -->
   <td class="no qa">43.74 ± 2.17 / 59.80 ± 1.86</td> <!-- NorQuAD -->
   <td class="no qa">33.94 ± 3.50 / 39.96 ± 2.98</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.66 ± 6.41 / 68.39 ± 7.26</td> <!-- SUC3 -->
   <td class="sv sent">73.43 ± 0.91 / 61.29 ± 1.81</td> <!-- SweReC -->
   <td class="sv la">45.09 ± 15.90 / 68.48 ± 11.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.04 ± 2.09 / 43.73 ± 1.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.30 ± 2.12 / 61.98 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">47.20 ± 1.34 / 64.51 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">40.52 ± 7.38 / 67.99 ± 3.84</td> <!-- ScaLA-da -->
   <td class="da qa">13.53 ± 4.79 / 15.93 ± 5.58</td> <!-- ScandiQA-da -->
   <td class="no ner">81.19 ± 1.37 / 84.11 ± 1.13</td> <!-- NorNE-nb -->
   <td class="no ner">73.93 ± 1.46 / 77.82 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">39.63 ± 1.06 / 49.23 ± 2.13</td> <!-- NoReC -->
   <td class="no la">45.75 ± 3.27 / 71.33 ± 1.67</td> <!-- ScaLA-nb -->
   <td class="no la">33.74 ± 2.91 / 63.89 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 3.79 / 7.65 ± 5.41</td> <!-- NorQuAD -->
   <td class="no qa">14.05 ± 2.62 / 16.16 ± 2.75</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.04 ± 1.33 / 71.34 ± 0.91</td> <!-- SUC3 -->
   <td class="sv sent">70.91 ± 1.23 / 67.12 ± 3.79</td> <!-- SweReC -->
   <td class="sv la">53.52 ± 1.22 / 76.15 ± 0.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.41 ± 4.10 / 18.47 ± 4.44</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.31 ± 1.93 / 72.55 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">52.86 ± 1.08 / 68.19 ± 1.02</td> <!-- Angry Tweets -->
   <td class="da la">75.20 ± 1.73 / 86.99 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">37.65 ± 0.96 / 43.48 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">84.15 ± 0.59 / 86.82 ± 0.53</td> <!-- NorNE-nb -->
   <td class="no ner">76.65 ± 1.46 / 79.91 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">47.84 ± 2.44 / 60.67 ± 3.47</td> <!-- NoReC -->
   <td class="no la">51.99 ± 11.45 / 72.87 ± 8.55</td> <!-- ScaLA-nb -->
   <td class="no la">30.57 ± 8.63 / 62.90 ± 7.32</td> <!-- ScaLA-nn -->
   <td class="no qa">36.75 ± 2.18 / 50.77 ± 2.11</td> <!-- NorQuAD -->
   <td class="no qa">34.47 ± 1.47 / 39.18 ± 1.57</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.15 ± 0.85 / 72.33 ± 0.82</td> <!-- SUC3 -->
   <td class="sv sent">67.77 ± 1.19 / 62.98 ± 2.57</td> <!-- SweReC -->
   <td class="sv la">33.79 ± 7.61 / 64.01 ± 6.84</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.71 ± 0.77 / 37.46 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">55.74 ± 1.15 / 60.78 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">39.65 ± 1.31 / 59.23 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">37.67 ± 7.20 / 65.47 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">15.41 ± 3.05 / 22.46 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="no ner">62.62 ± 0.66 / 65.95 ± 0.72</td> <!-- NorNE-nb -->
   <td class="no ner">51.50 ± 1.21 / 55.29 ± 1.26</td> <!-- NorNE-nn -->
   <td class="no sent">33.31 ± 2.87 / 48.75 ± 3.38</td> <!-- NoReC -->
   <td class="no la">20.34 ± 4.81 / 58.57 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">8.07 ± 2.44 / 53.43 ± 1.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.14 ± 0.16</td> <!-- NorQuAD -->
   <td class="no qa">19.65 ± 2.05 / 26.01 ± 2.02</td> <!-- ScandiQA-no -->
   <td class="sv ner">39.98 ± 1.42 / 42.99 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">55.49 ± 1.28 / 55.99 ± 2.15</td> <!-- SweReC -->
   <td class="sv la">4.69 ± 2.28 / 51.01 ± 1.58</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.22 ± 1.90 / 20.83 ± 1.46</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>chcaa/dfm-encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.69 ± 2.54 / 63.42 ± 1.89</td> <!-- DANSK -->
   <td class="da sent">39.91 ± 1.78 / 58.47 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">51.01 ± 10.50 / 74.54 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da qa">25.76 ± 2.11 / 31.49 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">65.08 ± 1.07 / 68.66 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">57.87 ± 2.08 / 61.77 ± 2.03</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 1.53 / 51.54 ± 2.45</td> <!-- NoReC -->
   <td class="no la">31.23 ± 6.86 / 63.55 ± 5.48</td> <!-- ScaLA-nb -->
   <td class="no la">5.40 ± 4.63 / 44.64 ± 6.37</td> <!-- ScaLA-nn -->
   <td class="no qa">22.56 ± 0.95 / 34.52 ± 1.15</td> <!-- NorQuAD -->
   <td class="no qa">24.22 ± 2.60 / 29.92 ± 2.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">46.05 ± 2.11 / 49.62 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">58.70 ± 2.54 / 58.15 ± 3.35</td> <!-- SweReC -->
   <td class="sv la">2.23 ± 2.12 / 46.43 ± 4.85</td> <!-- ScaLA-sv -->
   <td class="sv qa">25.45 ± 0.75 / 30.80 ± 0.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>chcaa/dfm-encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.95 ± 2.01 / 74.60 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">51.42 ± 2.30 / 67.07 ± 1.97</td> <!-- Angry Tweets -->
   <td class="da la">76.11 ± 1.17 / 87.41 ± 0.67</td> <!-- ScaLA-da -->
   <td class="da qa">47.42 ± 1.86 / 53.06 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">84.60 ± 1.44 / 88.66 ± 1.23</td> <!-- NorNE-nb -->
   <td class="no ner">80.07 ± 2.11 / 84.59 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">55.59 ± 10.43 / 67.82 ± 9.45</td> <!-- NoReC -->
   <td class="no la">71.43 ± 1.67 / 84.61 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">53.30 ± 13.11 / 74.52 ± 7.96</td> <!-- ScaLA-nn -->
   <td class="no qa">57.38 ± 1.41 / 72.48 ± 1.49</td> <!-- NorQuAD -->
   <td class="no qa">45.40 ± 0.78 / 51.18 ± 0.73</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.89 ± 2.46 / 74.18 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">75.11 ± 1.19 / 74.74 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">64.11 ± 3.27 / 81.63 ± 1.66</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.79 ± 1.61 / 52.40 ± 1.77</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.80 ± 1.79 / 69.65 ± 2.04</td> <!-- DANSK -->
   <td class="da sent">49.18 ± 1.55 / 65.94 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">65.45 ± 1.97 / 81.55 ± 1.33</td> <!-- ScaLA-da -->
   <td class="da qa">32.40 ± 2.41 / 37.33 ± 2.34</td> <!-- ScandiQA-da -->
   <td class="no ner">88.03 ± 0.77 / 90.65 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">81.01 ± 1.95 / 84.88 ± 1.55</td> <!-- NorNE-nn -->
   <td class="no sent">52.44 ± 2.90 / 62.48 ± 4.62</td> <!-- NoReC -->
   <td class="no la">68.77 ± 2.01 / 83.10 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">65.40 ± 2.43 / 81.72 ± 1.68</td> <!-- ScaLA-nn -->
   <td class="no qa">43.13 ± 2.05 / 56.76 ± 2.21</td> <!-- NorQuAD -->
   <td class="no qa">29.97 ± 2.32 / 34.41 ± 2.34</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.45 ± 1.57 / 78.58 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">73.41 ± 0.98 / 68.72 ± 3.80</td> <!-- SweReC -->
   <td class="sv la">71.14 ± 1.62 / 84.55 ± 0.97</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.62 ± 1.35 / 36.20 ± 1.16</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.54 ± 1.83 / 64.64 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.38 / 62.33 ± 1.20</td> <!-- Angry Tweets -->
   <td class="da la">47.47 ± 8.03 / 70.55 ± 4.26</td> <!-- ScaLA-da -->
   <td class="da qa">23.14 ± 1.59 / 29.91 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">68.09 ± 0.91 / 71.69 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">56.64 ± 1.98 / 60.00 ± 1.99</td> <!-- NorNE-nn -->
   <td class="no sent">38.94 ± 2.59 / 53.58 ± 3.33</td> <!-- NoReC -->
   <td class="no la">30.32 ± 4.68 / 62.42 ± 3.11</td> <!-- ScaLA-nb -->
   <td class="no la">7.99 ± 3.34 / 53.24 ± 1.64</td> <!-- ScaLA-nn -->
   <td class="no qa">24.02 ± 1.35 / 37.28 ± 1.24</td> <!-- NorQuAD -->
   <td class="no qa">23.76 ± 2.30 / 29.92 ± 2.08</td> <!-- ScandiQA-no -->
   <td class="sv ner">45.04 ± 1.50 / 48.32 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">53.98 ± 2.05 / 52.94 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">3.33 ± 2.12 / 51.06 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">23.15 ± 2.61 / 29.17 ± 2.19</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.86 ± 1.85 / 59.94 ± 2.06</td> <!-- DANSK -->
   <td class="da sent">39.16 ± 1.75 / 58.91 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">2.16 ± 1.61 / 48.93 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">24.69 ± 1.58 / 28.57 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="no ner">84.17 ± 0.81 / 87.63 ± 0.64</td> <!-- NorNE-nb -->
   <td class="no ner">75.70 ± 2.31 / 80.19 ± 2.00</td> <!-- NorNE-nn -->
   <td class="no sent">49.92 ± 1.44 / 63.75 ± 1.45</td> <!-- NoReC -->
   <td class="no la">7.93 ± 4.24 / 50.87 ± 2.29</td> <!-- ScaLA-nb -->
   <td class="no la">5.06 ± 0.83 / 51.44 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">22.46 ± 5.97 / 34.67 ± 8.87</td> <!-- NorQuAD -->
   <td class="no qa">25.38 ± 1.20 / 28.94 ± 1.08</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.96 ± 1.62 / 67.53 ± 1.66</td> <!-- SUC3 -->
   <td class="sv sent">59.27 ± 2.14 / 55.26 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.83 ± 2.01 / 49.25 ± 1.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.11 ± 2.76 / 27.79 ± 2.63</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">64.13 ± 1.94 / 67.89 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">39.34 ± 2.85 / 58.37 ± 3.66</td> <!-- Angry Tweets -->
   <td class="da la">50.90 ± 1.26 / 74.15 ± 0.81</td> <!-- ScaLA-da -->
   <td class="da qa">34.82 ± 1.33 / 39.58 ± 1.59</td> <!-- ScandiQA-da -->
   <td class="no ner">86.99 ± 0.87 / 90.02 ± 0.72</td> <!-- NorNE-nb -->
   <td class="no ner">83.03 ± 1.53 / 86.52 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 3.24 / 61.35 ± 5.46</td> <!-- NoReC -->
   <td class="no la">67.29 ± 2.13 / 82.23 ± 1.36</td> <!-- ScaLA-nb -->
   <td class="no la">56.67 ± 2.29 / 76.74 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no qa">48.63 ± 1.31 / 63.28 ± 1.09</td> <!-- NorQuAD -->
   <td class="no qa">35.72 ± 2.37 / 40.17 ± 2.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.68 ± 1.40 / 74.22 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">63.80 ± 1.56 / 57.65 ± 2.24</td> <!-- SweReC -->
   <td class="sv la">37.77 ± 5.16 / 65.87 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.45 ± 0.94 / 35.81 ± 0.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.83 ± 1.48 / 73.26 ± 1.37</td> <!-- DANSK -->
   <td class="da sent">43.94 ± 1.37 / 61.91 ± 0.97</td> <!-- Angry Tweets -->
   <td class="da la">51.62 ± 15.51 / 73.99 ± 9.26</td> <!-- ScaLA-da -->
   <td class="da qa">40.70 ± 0.86 / 45.68 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="no ner">89.79 ± 0.73 / 92.36 ± 0.55</td> <!-- NorNE-nb -->
   <td class="no ner">85.45 ± 1.21 / 88.49 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">59.73 ± 2.46 / 70.77 ± 3.26</td> <!-- NoReC -->
   <td class="no la">74.40 ± 2.03 / 86.34 ± 1.28</td> <!-- ScaLA-nb -->
   <td class="no la">68.85 ± 3.21 / 83.17 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">57.67 ± 1.86 / 72.51 ± 1.52</td> <!-- NorQuAD -->
   <td class="no qa">42.46 ± 1.33 / 47.28 ± 1.28</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.63 ± 0.98 / 78.21 ± 0.92</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 1.70 / 70.72 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">56.02 ± 2.92 / 77.31 ± 1.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.52 ± 1.02 / 47.31 ± 0.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">68.91 ± 1.04 / 73.62 ± 1.06</td> <!-- DANSK -->
   <td class="da sent">48.29 ± 2.60 / 64.67 ± 2.10</td> <!-- Angry Tweets -->
   <td class="da la">71.55 ± 1.81 / 85.17 ± 1.13</td> <!-- ScaLA-da -->
   <td class="da qa">48.59 ± 1.35 / 53.54 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">90.13 ± 1.02 / 93.12 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.03 ± 0.65 / 89.39 ± 0.52</td> <!-- NorNE-nn -->
   <td class="no sent">64.62 ± 1.36 / 75.40 ± 0.97</td> <!-- NoReC -->
   <td class="no la">77.97 ± 3.04 / 88.19 ± 1.89</td> <!-- ScaLA-nb -->
   <td class="no la">76.30 ± 1.56 / 87.68 ± 0.86</td> <!-- ScaLA-nn -->
   <td class="no qa">66.03 ± 1.19 / 79.64 ± 1.09</td> <!-- NorQuAD -->
   <td class="no qa">49.70 ± 0.90 / 54.71 ± 0.95</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.76 ± 1.48 / 79.01 ± 1.13</td> <!-- SUC3 -->
   <td class="sv sent">75.32 ± 1.55 / 69.39 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">69.11 ± 1.50 / 84.32 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.88 ± 0.87 / 54.15 ± 0.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">43.10 ± 1.97 / 59.40 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">51.80 ± 1.29 / 68.17 ± 0.86</td> <!-- Angry Tweets -->
   <td class="da la">54.22 ± 1.49 / 74.13 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">56.55 ± 1.12 / 65.84 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">64.00 ± 2.37 / 74.92 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">68.02 ± 1.41 / 75.34 ± 1.15</td> <!-- NorNE-nn -->
   <td class="no sent">57.64 ± 1.33 / 71.34 ± 1.15</td> <!-- NoReC -->
   <td class="no la">49.93 ± 1.78 / 69.26 ± 1.76</td> <!-- ScaLA-nb -->
   <td class="no la">34.22 ± 2.98 / 57.61 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 1.06 / 71.71 ± 0.83</td> <!-- NorQuAD -->
   <td class="no qa">57.12 ± 0.47 / 65.39 ± 0.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">58.93 ± 3.29 / 71.43 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 1.54 / 76.51 ± 1.63</td> <!-- SweReC -->
   <td class="sv la">55.99 ± 2.64 / 75.08 ± 2.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.46 ± 0.90 / 64.95 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,244 ± 510 / 3,515 ± 848</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">45.76 ± 3.31 / 64.94 ± 1.96</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">49.82 ± 1.79 / 60.78 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">63.39 ± 4.07 / 81.16 ± 2.46</td> <!-- NorNE-nb -->
   <td class="no ner">60.44 ± 5.46 / 75.75 ± 4.49</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">49.93 ± 3.13 / 77.72 ± 1.70</td> <!-- NorQuAD -->
   <td class="no qa">54.79 ± 1.85 / 65.03 ± 1.52</td> <!-- ScandiQA-no -->
   <td class="sv ner">54.97 ± 4.44 / 76.86 ± 1.89</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.50 ± 1.74 / 67.22 ± 1.24</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">65.03 ± 1.31 / 69.50 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">55.07 ± 1.53 / 69.43 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">57.67 ± 2.56 / 78.48 ± 1.32</td> <!-- ScaLA-da -->
   <td class="da qa">46.71 ± 1.25 / 52.84 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">90.64 ± 0.80 / 89.86 ± 0.93</td> <!-- NorNE-nb -->
   <td class="no ner">86.52 ± 0.94 / 84.32 ± 1.08</td> <!-- NorNE-nn -->
   <td class="no sent">61.52 ± 1.87 / 72.72 ± 1.95</td> <!-- NoReC -->
   <td class="no la">62.34 ± 2.48 / 79.94 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">34.88 ± 11.23 / 66.51 ± 5.72</td> <!-- ScaLA-nn -->
   <td class="no qa">53.01 ± 1.05 / 70.46 ± 0.86</td> <!-- NorQuAD -->
   <td class="no qa">46.09 ± 2.65 / 52.41 ± 2.14</td> <!-- ScandiQA-no -->
   <td class="sv ner">78.57 ± 1.27 / 80.36 ± 1.12</td> <!-- SUC3 -->
   <td class="sv sent">79.65 ± 1.05 / 78.90 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">63.15 ± 1.65 / 81.06 ± 0.95</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.99 ± 1.18 / 53.49 ± 0.89</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.27 ± 1.78 / 71.21 ± 1.46</td> <!-- DANSK -->
   <td class="da sent">47.55 ± 1.25 / 64.66 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">68.72 ± 1.40 / 83.85 ± 0.85</td> <!-- ScaLA-da -->
   <td class="da qa">38.33 ± 1.25 / 43.90 ± 1.45</td> <!-- ScandiQA-da -->
   <td class="no ner">91.04 ± 0.58 / 91.17 ± 0.52</td> <!-- NorNE-nb -->
   <td class="no ner">88.83 ± 0.84 / 87.30 ± 1.07</td> <!-- NorNE-nn -->
   <td class="no sent">59.10 ± 1.47 / 70.50 ± 2.06</td> <!-- NoReC -->
   <td class="no la">74.32 ± 1.76 / 86.47 ± 1.18</td> <!-- ScaLA-nb -->
   <td class="no la">72.94 ± 1.63 / 86.07 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">34.06 ± 2.05 / 45.46 ± 2.65</td> <!-- NorQuAD -->
   <td class="no qa">39.53 ± 1.00 / 44.57 ± 0.93</td> <!-- ScandiQA-no -->
   <td class="sv ner">79.18 ± 1.23 / 81.35 ± 1.26</td> <!-- SUC3 -->
   <td class="sv sent">71.16 ± 1.21 / 69.78 ± 3.24</td> <!-- SweReC -->
   <td class="sv la">63.89 ± 1.18 / 81.45 ± 0.75</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.18 ± 2.04 / 42.09 ± 2.23</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">70.13 ± 1.50 / 75.30 ± 1.02</td> <!-- DANSK -->
   <td class="da sent">55.12 ± 1.58 / 69.99 ± 1.09</td> <!-- Angry Tweets -->
   <td class="da la">76.34 ± 2.35 / 87.56 ± 1.48</td> <!-- ScaLA-da -->
   <td class="da qa">45.15 ± 3.33 / 50.82 ± 3.13</td> <!-- ScandiQA-da -->
   <td class="no ner">85.37 ± 0.78 / 86.78 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">82.22 ± 1.30 / 83.28 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">58.73 ± 2.31 / 70.10 ± 2.66</td> <!-- NoReC -->
   <td class="no la">70.73 ± 3.19 / 84.71 ± 1.82</td> <!-- ScaLA-nb -->
   <td class="no la">59.58 ± 7.22 / 78.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">56.04 ± 1.56 / 71.02 ± 1.42</td> <!-- NorQuAD -->
   <td class="no qa">46.88 ± 1.86 / 52.73 ± 1.82</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.05 ± 1.65 / 71.86 ± 1.73</td> <!-- SUC3 -->
   <td class="sv sent">74.67 ± 1.43 / 71.15 ± 3.57</td> <!-- SweReC -->
   <td class="sv la">62.77 ± 3.14 / 80.75 ± 1.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.77 ± 3.06 / 50.58 ± 2.94</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">70.34 ± 1.50 / 74.99 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">53.85 ± 1.39 / 68.94 ± 1.19</td> <!-- Angry Tweets -->
   <td class="da la">75.71 ± 1.95 / 87.29 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">44.85 ± 4.12 / 50.40 ± 4.01</td> <!-- ScandiQA-da -->
   <td class="no ner">85.20 ± 0.97 / 86.39 ± 1.06</td> <!-- NorNE-nb -->
   <td class="no ner">82.50 ± 1.19 / 83.22 ± 1.44</td> <!-- NorNE-nn -->
   <td class="no sent">59.61 ± 1.28 / 71.40 ± 1.68</td> <!-- NoReC -->
   <td class="no la">67.88 ± 7.37 / 82.75 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">62.44 ± 4.39 / 80.43 ± 2.39</td> <!-- ScaLA-nn -->
   <td class="no qa">55.69 ± 1.60 / 70.77 ± 1.64</td> <!-- NorQuAD -->
   <td class="no qa">46.49 ± 1.45 / 52.19 ± 1.43</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.08 ± 1.45 / 71.65 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">74.92 ± 0.98 / 72.01 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">63.43 ± 2.30 / 81.00 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.20 ± 1.03 / 51.94 ± 0.92</td> <!-- ScandiQA-sv -->
  </tr>
 </tbody>
</table>
</div>