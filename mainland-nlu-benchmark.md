---
layout: leaderboard
title: Mainland Scandinavian NLU Benchmark
---

<center>Last updated: 15/09/2023 17:05:00</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="nlu-benchmark" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of trainable parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>
   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score - Macro-average across tasks">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score - Macro-average across tasks">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score - Macro-average across tasks">SV</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total named entity recognition score - Macro-average across languages">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification tagging score - Macro-average across languages">SENT</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total linguistic acceptability score - Macro-average across languages">LA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total question answering score - Macro-average across languages">QA</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">DaNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">AngryTweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact match / F1-score">ScandiQA-da</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews correlation coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact match / F1-score">ScandiQA-no</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact match / F1-score">ScandiQA-sv</span></th>
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
   <td class="da ner">83.08 ± 0.86 / 85.34 ± 1.10</td> <!-- DaNE -->
   <td class="da sent">46.32 ± 1.22 / 64.13 ± 0.85</td> <!-- AngryTweets -->
   <td class="da la">66.41 ± 1.89 / 82.44 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da qa">45.41 ± 1.77 / 49.42 ± 1.72</td> <!-- ScandiQA-da -->
   <td class="no ner">89.36 ± 0.86 / 93.01 ± 0.68</td> <!-- NorNE-nb -->
   <td class="no ner">84.38 ± 0.81 / 88.43 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">60.84 ± 1.48 / 72.16 ± 1.38</td> <!-- NoReC -->
   <td class="no la">73.89 ± 1.31 / 86.19 ± 0.93</td> <!-- ScaLA-nb -->
   <td class="no la">72.10 ± 2.07 / 85.37 ± 1.33</td> <!-- ScaLA-nn -->
   <td class="no qa">42.74 ± 1.83 / 47.31 ± 1.87</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.35 ± 0.88 / 80.38 ± 0.99</td> <!-- SUC3 -->
   <td class="sv sent">71.21 ± 1.11 / 67.49 ± 2.90</td> <!-- SweReC -->
   <td class="sv la">64.03 ± 1.94 / 81.39 ± 1.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.61 ± 2.04 / 46.73 ± 1.80</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.70 ± 0.75 / 83.17 ± 0.71</td> <!-- DaNE -->
   <td class="da sent">49.66 ± 0.99 / 66.21 ± 0.72</td> <!-- AngryTweets -->
   <td class="da la">60.13 ± 13.57 / 78.92 ± 6.96</td> <!-- ScaLA-da -->
   <td class="da qa">41.92 ± 2.65 / 45.68 ± 2.57</td> <!-- ScandiQA-da -->
   <td class="no ner">86.13 ± 1.08 / 88.99 ± 0.96</td> <!-- NorNE-nb -->
   <td class="no ner">78.66 ± 1.85 / 82.99 ± 1.53</td> <!-- NorNE-nn -->
   <td class="no sent">57.37 ± 1.31 / 70.45 ± 1.13</td> <!-- NoReC -->
   <td class="no la">69.92 ± 2.01 / 83.51 ± 1.33</td> <!-- ScaLA-nb -->
   <td class="no la">70.05 ± 1.76 / 84.13 ± 1.17</td> <!-- ScaLA-nn -->
   <td class="no qa">40.55 ± 2.53 / 45.32 ± 2.29</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.31 ± 3.11 / 73.44 ± 2.81</td> <!-- SUC3 -->
   <td class="sv sent">73.63 ± 1.53 / 68.42 ± 4.24</td> <!-- SweReC -->
   <td class="sv la">58.91 ± 17.49 / 77.13 ± 10.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.58 ± 0.99 / 46.09 ± 0.99</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,326 ± 95 / 616 ± 167</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">83.21 ± 0.69 / 84.95 ± 0.76</td> <!-- DaNE -->
   <td class="da sent">47.00 ± 2.24 / 64.25 ± 1.84</td> <!-- AngryTweets -->
   <td class="da la">62.44 ± 2.23 / 80.48 ± 1.45</td> <!-- ScaLA-da -->
   <td class="da qa">42.40 ± 2.03 / 46.87 ± 2.14</td> <!-- ScandiQA-da -->
   <td class="no ner">87.15 ± 0.66 / 89.55 ± 0.56</td> <!-- NorNE-nb -->
   <td class="no ner">78.22 ± 3.18 / 81.94 ± 2.84</td> <!-- NorNE-nn -->
   <td class="no sent">53.23 ± 2.59 / 65.99 ± 3.76</td> <!-- NoReC -->
   <td class="no la">66.60 ± 2.68 / 82.12 ± 1.77</td> <!-- ScaLA-nb -->
   <td class="no la">36.19 ± 15.09 / 65.08 ± 10.44</td> <!-- ScaLA-nn -->
   <td class="no qa">41.41 ± 2.97 / 46.52 ± 2.96</td> <!-- ScandiQA-no -->
   <td class="sv ner">71.92 ± 1.86 / 78.21 ± 1.82</td> <!-- SUC3 -->
   <td class="sv sent">73.38 ± 2.23 / 68.86 ± 4.82</td> <!-- SweReC -->
   <td class="sv la">62.55 ± 9.85 / 79.88 ± 6.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.61 ± 2.73 / 47.66 ± 2.84</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>vesteinn/ScandiBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,610 ± 2,848 / 3,720 ± 1,195</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">82.95 ± 1.10 / 84.55 ± 1.27</td> <!-- DaNE -->
   <td class="da sent">47.61 ± 1.40 / 65.02 ± 1.06</td> <!-- AngryTweets -->
   <td class="da la">61.51 ± 7.24 / 79.84 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da qa">33.63 ± 3.31 / 37.61 ± 3.24</td> <!-- ScandiQA-da -->
   <td class="no ner">88.74 ± 0.88 / 91.35 ± 0.72</td> <!-- NorNE-nb -->
   <td class="no ner">81.18 ± 1.55 / 84.78 ± 1.36</td> <!-- NorNE-nn -->
   <td class="no sent">48.38 ± 3.15 / 57.53 ± 5.42</td> <!-- NoReC -->
   <td class="no la">62.43 ± 13.74 / 78.73 ± 9.87</td> <!-- ScaLA-nb -->
   <td class="no la">66.78 ± 3.05 / 82.50 ± 1.82</td> <!-- ScaLA-nn -->
   <td class="no qa">38.57 ± 1.69 / 43.17 ± 1.68</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.25 ± 0.88 / 80.45 ± 0.53</td> <!-- SUC3 -->
   <td class="sv sent">71.21 ± 1.00 / 64.47 ± 3.23</td> <!-- SweReC -->
   <td class="sv la">67.39 ± 2.68 / 82.65 ± 1.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.91 ± 2.41 / 45.52 ± 2.35</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,523 ± 2,863 / 3,690 ± 1,195</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">79.82 ± 0.49 / 81.40 ± 0.63</td> <!-- DaNE -->
   <td class="da sent">39.43 ± 0.70 / 59.43 ± 0.58</td> <!-- AngryTweets -->
   <td class="da la">50.76 ± 8.45 / 74.57 ± 4.53</td> <!-- ScaLA-da -->
   <td class="da qa">42.41 ± 1.47 / 47.05 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">87.36 ± 0.53 / 90.29 ± 0.44</td> <!-- NorNE-nb -->
   <td class="no ner">82.87 ± 0.96 / 86.56 ± 0.80</td> <!-- NorNE-nn -->
   <td class="no sent">59.11 ± 1.55 / 71.03 ± 1.57</td> <!-- NoReC -->
   <td class="no la">70.08 ± 1.57 / 83.73 ± 0.90</td> <!-- ScaLA-nb -->
   <td class="no la">66.37 ± 1.22 / 82.38 ± 0.79</td> <!-- ScaLA-nn -->
   <td class="no qa">44.29 ± 1.27 / 49.15 ± 1.36</td> <!-- ScandiQA-no -->
   <td class="sv ner">60.58 ± 0.99 / 65.97 ± 0.77</td> <!-- SUC3 -->
   <td class="sv sent">66.75 ± 0.88 / 65.54 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">35.67 ± 2.41 / 66.12 ± 1.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.62 ± 1.02 / 43.24 ± 1.00</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">79.64 ± 0.79 / 81.61 ± 0.61</td> <!-- DaNE -->
   <td class="da sent">45.30 ± 2.03 / 63.22 ± 1.47</td> <!-- AngryTweets -->
   <td class="da la">51.74 ± 2.53 / 74.31 ± 1.94</td> <!-- ScaLA-da -->
   <td class="da qa">34.45 ± 3.71 / 39.04 ± 3.65</td> <!-- ScandiQA-da -->
   <td class="no ner">85.32 ± 0.94 / 87.70 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">77.41 ± 1.57 / 81.41 ± 1.46</td> <!-- NorNE-nn -->
   <td class="no sent">48.34 ± 2.10 / 60.68 ± 3.61</td> <!-- NoReC -->
   <td class="no la">55.30 ± 2.89 / 75.77 ± 1.87</td> <!-- ScaLA-nb -->
   <td class="no la">37.46 ± 2.69 / 67.68 ± 1.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.55 ± 3.63 / 45.20 ± 3.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.03 ± 1.55 / 72.49 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">70.69 ± 1.08 / 67.03 ± 3.40</td> <!-- SweReC -->
   <td class="sv la">56.60 ± 3.25 / 76.70 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.22 ± 1.78 / 45.25 ± 1.68</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">79.98 ± 0.90 / 82.15 ± 0.75</td> <!-- DaNE -->
   <td class="da sent">34.78 ± 1.49 / 55.59 ± 0.92</td> <!-- AngryTweets -->
   <td class="da la">41.08 ± 7.28 / 69.77 ± 3.75</td> <!-- ScaLA-da -->
   <td class="da qa">48.92 ± 1.58 / 53.02 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">84.88 ± 1.05 / 88.05 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">79.06 ± 1.70 / 83.08 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">35.34 ± 1.88 / 48.31 ± 2.28</td> <!-- NoReC -->
   <td class="no la">31.45 ± 12.12 / 63.68 ± 6.21</td> <!-- ScaLA-nb -->
   <td class="no la">36.12 ± 8.59 / 66.98 ± 4.91</td> <!-- ScaLA-nn -->
   <td class="no qa">47.27 ± 0.71 / 52.22 ± 0.67</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.38 ± 1.01 / 76.55 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">61.60 ± 1.38 / 62.28 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">37.44 ± 6.65 / 66.67 ± 4.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.37 ± 1.13 / 50.75 ± 1.44</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.24 ± 1.75 / 82.18 ± 1.50</td> <!-- DaNE -->
   <td class="da sent">32.38 ± 1.72 / 53.30 ± 1.79</td> <!-- AngryTweets -->
   <td class="da la">27.93 ± 11.48 / 61.91 ± 6.69</td> <!-- ScaLA-da -->
   <td class="da qa">47.87 ± 1.91 / 52.09 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="no ner">85.49 ± 0.92 / 88.72 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">79.36 ± 1.38 / 83.08 ± 1.22</td> <!-- NorNE-nn -->
   <td class="no sent">35.87 ± 1.85 / 48.94 ± 3.37</td> <!-- NoReC -->
   <td class="no la">44.22 ± 3.29 / 70.31 ± 2.86</td> <!-- ScaLA-nb -->
   <td class="no la">39.55 ± 7.01 / 68.65 ± 3.36</td> <!-- ScaLA-nn -->
   <td class="no qa">47.67 ± 1.66 / 52.37 ± 1.69</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.33 ± 1.16 / 76.29 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">61.78 ± 1.21 / 60.94 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">47.74 ± 7.69 / 72.98 ± 4.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.94 ± 1.72 / 51.74 ± 1.72</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.01 ± 1.17 / 82.25 ± 1.15</td> <!-- DaNE -->
   <td class="da sent">32.88 ± 1.24 / 53.56 ± 1.47</td> <!-- AngryTweets -->
   <td class="da la">29.01 ± 11.25 / 61.89 ± 6.94</td> <!-- ScaLA-da -->
   <td class="da qa">48.37 ± 2.12 / 52.22 ± 2.11</td> <!-- ScandiQA-da -->
   <td class="no ner">84.84 ± 1.42 / 87.99 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">79.18 ± 1.45 / 83.10 ± 1.12</td> <!-- NorNE-nn -->
   <td class="no sent">36.21 ± 1.82 / 49.48 ± 2.69</td> <!-- NoReC -->
   <td class="no la">46.43 ± 1.81 / 71.65 ± 1.39</td> <!-- ScaLA-nb -->
   <td class="no la">39.82 ± 2.81 / 68.68 ± 1.81</td> <!-- ScaLA-nn -->
   <td class="no qa">46.09 ± 1.69 / 50.70 ± 1.72</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.17 ± 1.46 / 75.62 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">62.50 ± 1.10 / 60.57 ± 2.75</td> <!-- SweReC -->
   <td class="sv la">38.18 ± 7.03 / 66.99 ± 4.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.80 ± 1.96 / 51.53 ± 2.12</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.50 ± 0.78 / 82.80 ± 0.89</td> <!-- DaNE -->
   <td class="da sent">33.67 ± 1.54 / 54.48 ± 1.19</td> <!-- AngryTweets -->
   <td class="da la">35.79 ± 9.58 / 65.87 ± 5.46</td> <!-- ScaLA-da -->
   <td class="da qa">48.59 ± 1.17 / 52.44 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">85.29 ± 1.04 / 88.55 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">79.27 ± 1.21 / 83.09 ± 1.06</td> <!-- NorNE-nn -->
   <td class="no sent">35.16 ± 1.75 / 48.41 ± 2.71</td> <!-- NoReC -->
   <td class="no la">31.82 ± 8.92 / 62.98 ± 6.52</td> <!-- ScaLA-nb -->
   <td class="no la">32.94 ± 5.88 / 64.36 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no qa">46.26 ± 1.33 / 50.79 ± 1.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.57 ± 1.83 / 74.88 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">61.89 ± 0.90 / 60.17 ± 3.06</td> <!-- SweReC -->
   <td class="sv la">40.22 ± 2.03 / 68.89 ± 2.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.03 ± 1.09 / 51.72 ± 1.06</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">75.15 ± 1.19 / 77.97 ± 0.99</td> <!-- DaNE -->
   <td class="da sent">34.43 ± 4.13 / 51.90 ± 6.17</td> <!-- AngryTweets -->
   <td class="da la">67.27 ± 1.04 / 83.37 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">9.93 ± 4.98 / 10.82 ± 5.47</td> <!-- ScandiQA-da -->
   <td class="no ner">81.68 ± 0.65 / 84.95 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">74.62 ± 1.92 / 79.57 ± 1.49</td> <!-- NorNE-nn -->
   <td class="no sent">40.15 ± 1.15 / 46.26 ± 0.47</td> <!-- NoReC -->
   <td class="no la">72.87 ± 1.11 / 85.86 ± 0.63</td> <!-- ScaLA-nb -->
   <td class="no la">63.77 ± 1.27 / 81.62 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">8.06 ± 4.19 / 8.88 ± 4.62</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.46 ± 1.28 / 71.07 ± 1.59</td> <!-- SUC3 -->
   <td class="sv sent">66.42 ± 0.72 / 57.57 ± 1.23</td> <!-- SweReC -->
   <td class="sv la">69.19 ± 0.66 / 84.26 ± 0.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">13.64 ± 4.75 / 15.11 ± 5.29</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">78.99 ± 0.83 / 81.64 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">33.28 ± 1.65 / 54.37 ± 1.44</td> <!-- AngryTweets -->
   <td class="da la">33.15 ± 7.14 / 64.69 ± 4.47</td> <!-- ScaLA-da -->
   <td class="da qa">37.84 ± 2.23 / 41.60 ± 2.22</td> <!-- ScandiQA-da -->
   <td class="no ner">83.05 ± 1.29 / 85.91 ± 0.98</td> <!-- NorNE-nb -->
   <td class="no ner">76.00 ± 2.01 / 79.67 ± 1.62</td> <!-- NorNE-nn -->
   <td class="no sent">38.70 ± 2.53 / 50.88 ± 3.38</td> <!-- NoReC -->
   <td class="no la">39.13 ± 2.97 / 67.97 ± 1.68</td> <!-- ScaLA-nb -->
   <td class="no la">24.13 ± 6.88 / 60.76 ± 3.29</td> <!-- ScaLA-nn -->
   <td class="no qa">39.41 ± 1.54 / 43.68 ± 1.69</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.66 ± 1.60 / 81.95 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">75.58 ± 1.17 / 73.35 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">78.86 ± 0.83 / 89.07 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.05 ± 1.99 / 51.22 ± 2.02</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">74.61 ± 1.54 / 76.16 ± 1.71</td> <!-- DaNE -->
   <td class="da sent">42.17 ± 1.64 / 61.25 ± 1.45</td> <!-- AngryTweets -->
   <td class="da la">29.43 ± 13.02 / 62.08 ± 7.77</td> <!-- ScaLA-da -->
   <td class="da qa">39.59 ± 1.12 / 43.21 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">81.35 ± 1.22 / 84.11 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">73.67 ± 2.26 / 77.22 ± 1.99</td> <!-- NorNE-nn -->
   <td class="no sent">37.02 ± 1.09 / 47.88 ± 2.50</td> <!-- NoReC -->
   <td class="no la">35.42 ± 12.32 / 66.30 ± 6.78</td> <!-- ScaLA-nb -->
   <td class="no la">6.87 ± 6.85 / 50.70 ± 3.62</td> <!-- ScaLA-nn -->
   <td class="no qa">38.00 ± 2.82 / 42.08 ± 2.79</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.19 ± 1.42 / 70.17 ± 0.99</td> <!-- SUC3 -->
   <td class="sv sent">66.62 ± 1.71 / 61.90 ± 2.61</td> <!-- SweReC -->
   <td class="sv la">46.72 ± 3.65 / 72.15 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.62 ± 1.44 / 44.78 ± 1.50</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,343 ± 1,236 / 1,444 ± 456</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.83 ± 0.67 / 84.58 ± 0.73</td> <!-- DaNE -->
   <td class="da sent">49.07 ± 1.23 / 65.38 ± 1.16</td> <!-- AngryTweets -->
   <td class="da la">72.02 ± 2.15 / 85.74 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">54.66 ± 1.12 / 59.50 ± 0.96</td> <!-- ScandiQA-da -->
   <td class="no ner">87.09 ± 1.01 / 91.32 ± 0.90</td> <!-- NorNE-nb -->
   <td class="no ner">83.06 ± 1.22 / 87.29 ± 0.74</td> <!-- NorNE-nn -->
   <td class="no sent">63.40 ± 1.38 / 74.60 ± 1.12</td> <!-- NoReC -->
   <td class="no la">78.43 ± 1.47 / 88.75 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">79.59 ± 1.72 / 89.56 ± 0.88</td> <!-- ScaLA-nn -->
   <td class="no qa">53.42 ± 1.53 / 58.22 ± 1.40</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.77 ± 1.11 / 78.39 ± 0.90</td> <!-- SUC3 -->
   <td class="sv sent">75.86 ± 1.35 / 72.14 ± 4.29</td> <!-- SweReC -->
   <td class="sv la">74.75 ± 0.75 / 87.18 ± 0.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.78 ± 1.16 / 59.32 ± 1.10</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">84.28 ± 1.22 / 85.84 ± 1.24</td> <!-- DaNE -->
   <td class="da sent">48.33 ± 4.44 / 63.94 ± 5.16</td> <!-- AngryTweets -->
   <td class="da la">57.30 ± 14.90 / 76.82 ± 8.67</td> <!-- ScaLA-da -->
   <td class="da qa">51.80 ± 1.96 / 56.71 ± 1.65</td> <!-- ScandiQA-da -->
   <td class="no ner">89.34 ± 1.62 / 91.66 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">82.86 ± 1.29 / 86.19 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">50.25 ± 15.36 / 63.55 ± 13.05</td> <!-- NoReC -->
   <td class="no la">55.51 ± 18.28 / 74.00 ± 13.38</td> <!-- ScaLA-nb -->
   <td class="no la">43.89 ± 14.81 / 68.88 ± 10.32</td> <!-- ScaLA-nn -->
   <td class="no qa">54.20 ± 1.16 / 59.00 ± 1.25</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.03 ± 3.79 / 80.33 ± 2.50</td> <!-- SUC3 -->
   <td class="sv sent">76.63 ± 0.98 / 74.25 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">49.72 ± 19.88 / 69.94 ± 13.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.69 ± 1.27 / 57.28 ± 1.06</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.31 ± 1.00 / 85.31 ± 1.04</td> <!-- DaNE -->
   <td class="da sent">43.38 ± 3.20 / 60.05 ± 4.33</td> <!-- AngryTweets -->
   <td class="da la">67.05 ± 1.41 / 83.18 ± 0.80</td> <!-- ScaLA-da -->
   <td class="da qa">50.91 ± 1.30 / 55.81 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">89.55 ± 0.57 / 91.90 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">83.46 ± 1.68 / 86.81 ± 1.35</td> <!-- NorNE-nn -->
   <td class="no sent">53.69 ± 4.28 / 63.69 ± 6.95</td> <!-- NoReC -->
   <td class="no la">70.55 ± 1.64 / 84.79 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">61.21 ± 1.20 / 79.87 ± 0.76</td> <!-- ScaLA-nn -->
   <td class="no qa">50.15 ± 1.28 / 55.64 ± 1.28</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.86 ± 2.04 / 78.84 ± 2.19</td> <!-- SUC3 -->
   <td class="sv sent">75.24 ± 0.99 / 72.06 ± 2.67</td> <!-- SweReC -->
   <td class="sv la">72.30 ± 1.04 / 85.77 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.91 ± 1.27 / 56.23 ± 0.91</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.86 ± 1.19 / 84.09 ± 1.13</td> <!-- DaNE -->
   <td class="da sent">46.50 ± 1.57 / 64.31 ± 1.21</td> <!-- AngryTweets -->
   <td class="da la">52.92 ± 4.42 / 75.11 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">46.54 ± 2.39 / 51.17 ± 2.34</td> <!-- ScandiQA-da -->
   <td class="no ner">87.84 ± 1.00 / 90.58 ± 0.91</td> <!-- NorNE-nb -->
   <td class="no ner">81.57 ± 1.30 / 85.21 ± 1.05</td> <!-- NorNE-nn -->
   <td class="no sent">54.26 ± 1.75 / 67.25 ± 1.47</td> <!-- NoReC -->
   <td class="no la">59.44 ± 1.47 / 78.80 ± 1.00</td> <!-- ScaLA-nb -->
   <td class="no la">49.30 ± 1.39 / 74.02 ± 1.04</td> <!-- ScaLA-nn -->
   <td class="no qa">49.44 ± 1.42 / 54.42 ± 1.26</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.08 ± 1.81 / 77.78 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">73.58 ± 1.37 / 70.43 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">60.36 ± 2.98 / 79.72 ± 1.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.05 ± 1.60 / 55.03 ± 1.55</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.41 ± 1.35 / 79.75 ± 1.27</td> <!-- DaNE -->
   <td class="da sent">41.02 ± 1.64 / 60.13 ± 1.52</td> <!-- AngryTweets -->
   <td class="da la">27.10 ± 3.59 / 61.03 ± 2.41</td> <!-- ScaLA-da -->
   <td class="da qa">46.86 ± 1.37 / 52.41 ± 1.25</td> <!-- ScandiQA-da -->
   <td class="no ner">83.09 ± 0.94 / 85.99 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">75.61 ± 1.34 / 79.47 ± 1.14</td> <!-- NorNE-nn -->
   <td class="no sent">39.53 ± 0.99 / 50.90 ± 2.17</td> <!-- NoReC -->
   <td class="no la">27.39 ± 2.48 / 61.03 ± 2.27</td> <!-- ScaLA-nb -->
   <td class="no la">23.56 ± 2.23 / 60.05 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">47.84 ± 0.89 / 53.45 ± 0.90</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.08 ± 1.45 / 81.05 ± 1.34</td> <!-- SUC3 -->
   <td class="sv sent">78.00 ± 0.89 / 75.01 ± 2.18</td> <!-- SweReC -->
   <td class="sv la">76.79 ± 1.70 / 87.59 ± 1.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.58 ± 0.67 / 59.30 ± 0.50</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.31 ± 0.59 / 78.15 ± 0.58</td> <!-- DaNE -->
   <td class="da sent">38.46 ± 1.17 / 58.16 ± 0.95</td> <!-- AngryTweets -->
   <td class="da la">32.29 ± 5.92 / 63.74 ± 3.44</td> <!-- ScaLA-da -->
   <td class="da qa">46.33 ± 1.99 / 51.15 ± 1.83</td> <!-- ScandiQA-da -->
   <td class="no ner">80.48 ± 0.89 / 83.32 ± 0.99</td> <!-- NorNE-nb -->
   <td class="no ner">74.84 ± 1.18 / 77.97 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">38.44 ± 1.67 / 52.60 ± 1.95</td> <!-- NoReC -->
   <td class="no la">37.54 ± 1.13 / 64.46 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">23.10 ± 3.66 / 58.14 ± 3.65</td> <!-- ScaLA-nn -->
   <td class="no qa">46.70 ± 0.97 / 51.94 ± 0.96</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.84 ± 1.51 / 78.61 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 0.80 / 75.77 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">72.87 ± 2.36 / 85.57 ± 1.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.59 ± 1.41 / 58.04 ± 1.37</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.43 ± 0.89 / 80.18 ± 0.78</td> <!-- DaNE -->
   <td class="da sent">39.20 ± 1.69 / 59.33 ± 1.23</td> <!-- AngryTweets -->
   <td class="da la">26.68 ± 3.38 / 59.41 ± 2.16</td> <!-- ScaLA-da -->
   <td class="da qa">46.76 ± 1.10 / 51.76 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">80.97 ± 0.92 / 84.03 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">74.25 ± 1.62 / 77.98 ± 1.36</td> <!-- NorNE-nn -->
   <td class="no sent">39.15 ± 3.29 / 53.00 ± 3.85</td> <!-- NoReC -->
   <td class="no la">21.39 ± 2.73 / 58.08 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 3.43 / 57.00 ± 1.86</td> <!-- ScaLA-nn -->
   <td class="no qa">48.15 ± 1.21 / 53.34 ± 1.08</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.83 ± 1.44 / 80.39 ± 1.34</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 0.79 / 77.12 ± 0.86</td> <!-- SweReC -->
   <td class="sv la">76.28 ± 1.86 / 87.37 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.71 ± 1.26 / 57.70 ± 1.16</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.37 ± 1.04 / 78.85 ± 1.23</td> <!-- DaNE -->
   <td class="da sent">34.45 ± 0.78 / 55.56 ± 0.68</td> <!-- AngryTweets -->
   <td class="da la">41.89 ± 9.80 / 70.04 ± 5.10</td> <!-- ScaLA-da -->
   <td class="da qa">36.42 ± 1.34 / 40.35 ± 1.47</td> <!-- ScandiQA-da -->
   <td class="no ner">82.31 ± 0.65 / 85.42 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">74.86 ± 1.50 / 78.92 ± 1.42</td> <!-- NorNE-nn -->
   <td class="no sent">36.27 ± 1.57 / 50.95 ± 1.70</td> <!-- NoReC -->
   <td class="no la">48.07 ± 5.64 / 72.00 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">29.81 ± 3.52 / 64.03 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no qa">35.09 ± 1.56 / 39.27 ± 1.48</td> <!-- ScandiQA-no -->
   <td class="sv ner">66.93 ± 1.30 / 72.90 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">61.11 ± 1.28 / 58.97 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">55.05 ± 1.64 / 76.76 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.93 ± 1.72 / 41.27 ± 1.62</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.76 ± 1.00 / 77.48 ± 0.81</td> <!-- DaNE -->
   <td class="da sent">36.66 ± 1.27 / 57.48 ± 0.82</td> <!-- AngryTweets -->
   <td class="da la">22.69 ± 5.37 / 59.46 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">31.60 ± 2.58 / 35.19 ± 2.73</td> <!-- ScandiQA-da -->
   <td class="no ner">76.73 ± 1.16 / 79.25 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">71.63 ± 1.31 / 75.39 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 3.06 / 51.25 ± 3.01</td> <!-- NoReC -->
   <td class="no la">22.02 ± 5.34 / 57.45 ± 3.59</td> <!-- ScaLA-nb -->
   <td class="no la">19.72 ± 3.67 / 56.70 ± 2.89</td> <!-- ScaLA-nn -->
   <td class="no qa">32.67 ± 2.13 / 36.95 ± 2.20</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.45 ± 1.62 / 75.40 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">76.22 ± 0.78 / 75.25 ± 1.16</td> <!-- SweReC -->
   <td class="sv la">65.73 ± 1.73 / 81.50 ± 1.14</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.74 ± 1.62 / 42.17 ± 1.55</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.36 ± 1.08 / 79.04 ± 1.02</td> <!-- DaNE -->
   <td class="da sent">38.46 ± 0.77 / 58.57 ± 0.67</td> <!-- AngryTweets -->
   <td class="da la">4.61 ± 2.95 / 49.70 ± 2.34</td> <!-- ScaLA-da -->
   <td class="da qa">29.93 ± 2.70 / 34.77 ± 2.50</td> <!-- ScandiQA-da -->
   <td class="no ner">80.34 ± 1.44 / 83.23 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">75.55 ± 1.69 / 79.16 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">33.94 ± 3.74 / 47.96 ± 4.12</td> <!-- NoReC -->
   <td class="no la">9.56 ± 5.01 / 52.24 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">4.16 ± 2.97 / 50.07 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">31.20 ± 1.80 / 36.20 ± 1.87</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.07 ± 1.54 / 79.99 ± 1.32</td> <!-- SUC3 -->
   <td class="sv sent">76.04 ± 0.97 / 72.61 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">73.52 ± 2.31 / 85.57 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.90 ± 2.39 / 42.11 ± 2.26</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">73.74 ± 1.45 / 76.81 ± 1.39</td> <!-- DaNE -->
   <td class="da sent">36.31 ± 1.60 / 57.37 ± 1.15</td> <!-- AngryTweets -->
   <td class="da la">23.46 ± 1.17 / 58.91 ± 1.36</td> <!-- ScaLA-da -->
   <td class="da qa">36.27 ± 1.60 / 41.55 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="no ner">75.03 ± 1.70 / 77.98 ± 1.58</td> <!-- NorNE-nb -->
   <td class="no ner">71.00 ± 1.64 / 75.00 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">33.88 ± 1.40 / 49.21 ± 1.98</td> <!-- NoReC -->
   <td class="no la">24.23 ± 1.83 / 58.89 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">18.18 ± 2.65 / 57.28 ± 1.84</td> <!-- ScaLA-nn -->
   <td class="no qa">34.42 ± 3.11 / 39.99 ± 3.20</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.18 ± 0.95 / 79.29 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">75.85 ± 0.54 / 70.58 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">70.43 ± 1.03 / 83.85 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.05 ± 1.29 / 49.81 ± 1.35</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">70.37 ± 1.45 / 73.57 ± 1.60</td> <!-- DaNE -->
   <td class="da sent">32.72 ± 2.91 / 49.84 ± 4.90</td> <!-- AngryTweets -->
   <td class="da la">67.74 ± 1.33 / 83.32 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">0.60 ± 1.17 / 0.62 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="no ner">68.20 ± 1.23 / 71.85 ± 1.11</td> <!-- NorNE-nb -->
   <td class="no ner">62.61 ± 1.22 / 67.14 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">29.00 ± 1.28 / 41.72 ± 0.52</td> <!-- NoReC -->
   <td class="no la">33.57 ± 2.58 / 65.22 ± 1.59</td> <!-- ScaLA-nb -->
   <td class="no la">21.79 ± 1.60 / 60.32 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.01 ± 0.01</td> <!-- ScandiQA-no -->
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
   <td class="da ner">74.33 ± 1.00 / 78.34 ± 0.76</td> <!-- DaNE -->
   <td class="da sent">43.79 ± 1.76 / 62.26 ± 1.35</td> <!-- AngryTweets -->
   <td class="da la">45.96 ± 2.91 / 69.62 ± 1.72</td> <!-- ScaLA-da -->
   <td class="da qa">38.94 ± 1.32 / 43.91 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">69.33 ± 0.93 / 72.62 ± 0.81</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 1.67 / 58.73 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">40.65 ± 1.63 / 55.20 ± 2.63</td> <!-- NoReC -->
   <td class="no la">29.47 ± 2.30 / 62.25 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">12.95 ± 3.01 / 55.31 ± 1.87</td> <!-- ScaLA-nn -->
   <td class="no qa">34.34 ± 2.90 / 40.32 ± 2.71</td> <!-- ScandiQA-no -->
   <td class="sv ner">47.15 ± 1.18 / 50.29 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">57.42 ± 1.88 / 56.53 ± 1.66</td> <!-- SweReC -->
   <td class="sv la">4.94 ± 1.62 / 51.57 ± 1.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.19 ± 5.11 / 36.10 ± 4.75</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">68.83 ± 0.77 / 72.12 ± 1.08</td> <!-- DaNE -->
   <td class="da sent">34.45 ± 3.16 / 51.40 ± 5.12</td> <!-- AngryTweets -->
   <td class="da la">65.15 ± 0.81 / 82.32 ± 0.45</td> <!-- ScaLA-da -->
   <td class="da qa">7.34 ± 3.14 / 7.89 ± 3.43</td> <!-- ScandiQA-da -->
   <td class="no ner">55.95 ± 2.74 / 59.76 ± 3.01</td> <!-- NorNE-nb -->
   <td class="no ner">48.14 ± 1.95 / 51.44 ± 2.28</td> <!-- NorNE-nn -->
   <td class="no sent">33.41 ± 1.40 / 45.12 ± 1.87</td> <!-- NoReC -->
   <td class="no la">32.87 ± 1.49 / 65.82 ± 0.78</td> <!-- ScaLA-nb -->
   <td class="no la">20.09 ± 1.88 / 59.27 ± 1.08</td> <!-- ScaLA-nn -->
   <td class="no qa">1.27 ± 1.50 / 1.39 ± 1.67</td> <!-- ScandiQA-no -->
   <td class="sv ner">36.74 ± 3.78 / 39.17 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">57.71 ± 1.40 / 53.54 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">17.10 ± 2.57 / 57.41 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">3.01 ± 3.03 / 3.34 ± 3.37</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.00 ± 1.45 / 76.34 ± 1.49</td> <!-- DaNE -->
   <td class="da sent">42.26 ± 1.13 / 61.41 ± 0.76</td> <!-- AngryTweets -->
   <td class="da la">34.80 ± 5.89 / 64.51 ± 4.90</td> <!-- ScaLA-da -->
   <td class="da qa">26.89 ± 2.96 / 31.91 ± 2.59</td> <!-- ScandiQA-da -->
   <td class="no ner">75.93 ± 1.64 / 80.08 ± 1.46</td> <!-- NorNE-nb -->
   <td class="no ner">70.26 ± 2.24 / 74.59 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">52.16 ± 0.99 / 66.79 ± 0.98</td> <!-- NoReC -->
   <td class="no la">36.30 ± 6.44 / 65.52 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">14.21 ± 6.44 / 52.78 ± 5.69</td> <!-- ScaLA-nn -->
   <td class="no qa">28.09 ± 1.79 / 33.33 ± 1.60</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.54 ± 1.20 / 68.94 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 0.89 / 68.13 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">40.21 ± 2.53 / 67.11 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.20 ± 2.47 / 36.79 ± 2.27</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.79 ± 0.45 / 82.93 ± 0.34</td> <!-- DaNE -->
   <td class="da sent">32.06 ± 1.44 / 52.57 ± 1.80</td> <!-- AngryTweets -->
   <td class="da la">30.95 ± 11.93 / 63.72 ± 6.84</td> <!-- ScaLA-da -->
   <td class="da qa">45.61 ± 1.73 / 49.75 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">83.86 ± 0.68 / 87.52 ± 0.63</td> <!-- NorNE-nb -->
   <td class="no ner">78.65 ± 2.01 / 82.66 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">32.73 ± 1.37 / 46.52 ± 1.86</td> <!-- NoReC -->
   <td class="no la">36.41 ± 8.89 / 65.20 ± 6.41</td> <!-- ScaLA-nb -->
   <td class="no la">30.37 ± 5.50 / 62.12 ± 5.66</td> <!-- ScaLA-nn -->
   <td class="no qa">46.74 ± 1.83 / 51.28 ± 1.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.93 ± 1.36 / 74.13 ± 1.17</td> <!-- SUC3 -->
   <td class="sv sent">62.18 ± 1.26 / 59.44 ± 2.35</td> <!-- SweReC -->
   <td class="sv la">36.93 ± 6.47 / 65.97 ± 6.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.04 ± 0.99 / 52.40 ± 0.84</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.33 ± 0.81 / 79.47 ± 0.78</td> <!-- DaNE -->
   <td class="da sent">32.53 ± 1.39 / 54.09 ± 1.00</td> <!-- AngryTweets -->
   <td class="da la">35.53 ± 2.54 / 66.86 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">39.46 ± 1.89 / 43.06 ± 1.73</td> <!-- ScandiQA-da -->
   <td class="no ner">80.61 ± 1.00 / 83.62 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">76.61 ± 0.81 / 80.69 ± 0.69</td> <!-- NorNE-nn -->
   <td class="no sent">33.16 ± 2.13 / 46.93 ± 2.66</td> <!-- NoReC -->
   <td class="no la">36.10 ± 2.45 / 66.11 ± 1.85</td> <!-- ScaLA-nb -->
   <td class="no la">30.10 ± 2.50 / 64.29 ± 1.69</td> <!-- ScaLA-nn -->
   <td class="no qa">36.52 ± 1.35 / 40.98 ± 1.32</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.46 ± 1.31 / 70.08 ± 1.38</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.22 / 56.16 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">33.71 ± 1.12 / 65.32 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.33 ± 1.05 / 44.02 ± 1.09</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.56 ± 0.68 / 79.67 ± 0.63</td> <!-- DaNE -->
   <td class="da sent">31.81 ± 1.65 / 53.25 ± 1.65</td> <!-- AngryTweets -->
   <td class="da la">34.13 ± 2.81 / 65.98 ± 2.30</td> <!-- ScaLA-da -->
   <td class="da qa">38.86 ± 2.58 / 42.73 ± 2.61</td> <!-- ScandiQA-da -->
   <td class="no ner">80.55 ± 1.53 / 83.59 ± 1.36</td> <!-- NorNE-nb -->
   <td class="no ner">76.08 ± 1.06 / 80.29 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">33.19 ± 1.75 / 46.63 ± 2.55</td> <!-- NoReC -->
   <td class="no la">32.60 ± 6.93 / 65.19 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">24.97 ± 6.47 / 61.39 ± 3.34</td> <!-- ScaLA-nn -->
   <td class="no qa">37.25 ± 1.30 / 41.72 ± 1.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.49 ± 1.43 / 70.56 ± 1.36</td> <!-- SUC3 -->
   <td class="sv sent">60.69 ± 0.46 / 56.69 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">30.83 ± 1.47 / 63.39 ± 1.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.40 ± 1.34 / 46.03 ± 1.24</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.83 ± 0.53 / 79.01 ± 0.63</td> <!-- DaNE -->
   <td class="da sent">32.13 ± 1.52 / 53.89 ± 1.25</td> <!-- AngryTweets -->
   <td class="da la">34.75 ± 1.55 / 65.89 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">38.67 ± 1.67 / 42.64 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">79.91 ± 0.64 / 82.84 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">74.64 ± 1.40 / 78.83 ± 1.18</td> <!-- NorNE-nn -->
   <td class="no sent">30.70 ± 2.63 / 43.77 ± 2.62</td> <!-- NoReC -->
   <td class="no la">34.24 ± 2.30 / 65.60 ± 1.50</td> <!-- ScaLA-nb -->
   <td class="no la">27.20 ± 2.61 / 62.87 ± 1.41</td> <!-- ScaLA-nn -->
   <td class="no qa">36.30 ± 2.19 / 40.68 ± 2.13</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.90 ± 1.27 / 69.25 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">58.47 ± 1.30 / 56.03 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">29.80 ± 1.57 / 63.53 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.16 ± 1.24 / 44.79 ± 1.14</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.19 ± 0.92 / 79.59 ± 0.77</td> <!-- DaNE -->
   <td class="da sent">31.89 ± 1.59 / 53.99 ± 1.22</td> <!-- AngryTweets -->
   <td class="da la">36.00 ± 2.27 / 67.38 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">40.34 ± 2.04 / 44.20 ± 1.99</td> <!-- ScandiQA-da -->
   <td class="no ner">80.29 ± 1.38 / 83.27 ± 1.20</td> <!-- NorNE-nb -->
   <td class="no ner">75.31 ± 1.19 / 79.59 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">29.37 ± 2.58 / 44.05 ± 3.33</td> <!-- NoReC -->
   <td class="no la">31.50 ± 6.37 / 64.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">24.06 ± 7.24 / 61.01 ± 3.82</td> <!-- ScaLA-nn -->
   <td class="no qa">36.72 ± 1.72 / 41.16 ± 1.68</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.51 ± 1.33 / 69.62 ± 0.88</td> <!-- SUC3 -->
   <td class="sv sent">59.42 ± 1.21 / 55.74 ± 1.26</td> <!-- SweReC -->
   <td class="sv la">29.01 ± 2.06 / 62.65 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.43 ± 1.61 / 45.90 ± 1.54</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.82 ± 1.29 / 84.58 ± 1.22</td> <!-- DaNE -->
   <td class="da sent">47.83 ± 1.46 / 65.49 ± 0.96</td> <!-- AngryTweets -->
   <td class="da la">11.87 ± 5.47 / 48.82 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da qa">34.33 ± 4.75 / 38.50 ± 4.85</td> <!-- ScandiQA-da -->
   <td class="no ner">87.56 ± 1.39 / 90.07 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">82.40 ± 1.16 / 85.65 ± 0.96</td> <!-- NorNE-nn -->
   <td class="no sent">54.46 ± 1.16 / 68.25 ± 0.76</td> <!-- NoReC -->
   <td class="no la">12.16 ± 5.91 / 50.55 ± 4.73</td> <!-- ScaLA-nb -->
   <td class="no la">8.99 ± 2.25 / 48.57 ± 3.67</td> <!-- ScaLA-nn -->
   <td class="no qa">40.59 ± 5.70 / 45.66 ± 5.60</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.04 ± 2.25 / 78.60 ± 1.91</td> <!-- SUC3 -->
   <td class="sv sent">73.67 ± 1.48 / 68.61 ± 3.14</td> <!-- SweReC -->
   <td class="sv la">15.41 ± 4.59 / 53.29 ± 3.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.99 ± 4.18 / 47.01 ± 4.41</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.85 ± 0.98 / 79.05 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">31.30 ± 1.80 / 52.43 ± 1.61</td> <!-- AngryTweets -->
   <td class="da la">34.92 ± 2.74 / 66.69 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">39.14 ± 2.13 / 42.87 ± 2.14</td> <!-- ScandiQA-da -->
   <td class="no ner">80.32 ± 0.76 / 83.49 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">76.10 ± 1.23 / 80.23 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">32.66 ± 1.96 / 46.26 ± 3.19</td> <!-- NoReC -->
   <td class="no la">33.65 ± 6.63 / 65.22 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">29.07 ± 2.20 / 63.35 ± 1.54</td> <!-- ScaLA-nn -->
   <td class="no qa">35.74 ± 1.59 / 40.15 ± 1.44</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.93 ± 1.47 / 69.94 ± 1.11</td> <!-- SUC3 -->
   <td class="sv sent">59.83 ± 1.11 / 55.15 ± 0.99</td> <!-- SweReC -->
   <td class="sv la">29.82 ± 1.23 / 63.32 ± 1.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.55 ± 1.55 / 45.40 ± 1.53</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">71.71 ± 0.90 / 73.64 ± 0.72</td> <!-- DaNE -->
   <td class="da sent">44.48 ± 1.32 / 63.11 ± 0.83</td> <!-- AngryTweets -->
   <td class="da la">26.74 ± 1.94 / 62.19 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da qa">31.93 ± 2.40 / 37.51 ± 2.23</td> <!-- ScandiQA-da -->
   <td class="no ner">74.65 ± 1.36 / 78.31 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">67.28 ± 1.09 / 72.13 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">47.53 ± 0.94 / 62.73 ± 1.07</td> <!-- NoReC -->
   <td class="no la">26.92 ± 3.12 / 61.93 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.63 ± 4.00 / 56.24 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">23.95 ± 1.47 / 31.74 ± 1.35</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.99 ± 1.40 / 66.50 ± 1.49</td> <!-- SUC3 -->
   <td class="sv sent">72.19 ± 0.71 / 67.88 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">28.75 ± 5.58 / 63.30 ± 2.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">26.81 ± 1.67 / 33.84 ± 1.40</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">68.98 ± 1.26 / 72.12 ± 1.12</td> <!-- DaNE -->
   <td class="da sent">33.51 ± 1.46 / 54.93 ± 1.21</td> <!-- AngryTweets -->
   <td class="da la">12.08 ± 8.71 / 54.24 ± 4.71</td> <!-- ScaLA-da -->
   <td class="da qa">30.52 ± 1.76 / 33.70 ± 1.82</td> <!-- ScandiQA-da -->
   <td class="no ner">69.79 ± 2.34 / 72.74 ± 2.03</td> <!-- NorNE-nb -->
   <td class="no ner">65.59 ± 2.06 / 69.74 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">29.68 ± 1.91 / 43.64 ± 2.18</td> <!-- NoReC -->
   <td class="no la">15.83 ± 10.06 / 55.51 ± 5.25</td> <!-- ScaLA-nb -->
   <td class="no la">8.70 ± 4.78 / 52.69 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">30.23 ± 2.31 / 34.90 ± 2.34</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.00 ± 2.58 / 68.55 ± 3.16</td> <!-- SUC3 -->
   <td class="sv sent">69.96 ± 1.75 / 68.67 ± 3.21</td> <!-- SweReC -->
   <td class="sv la">52.88 ± 14.23 / 75.25 ± 7.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.06 ± 1.37 / 38.38 ± 1.32</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.83 ± 0.79 / 76.28 ± 0.94</td> <!-- DaNE -->
   <td class="da sent">31.16 ± 2.06 / 52.25 ± 2.48</td> <!-- AngryTweets -->
   <td class="da la">21.08 ± 2.54 / 56.96 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">28.27 ± 2.14 / 30.58 ± 2.39</td> <!-- ScandiQA-da -->
   <td class="no ner">79.80 ± 1.69 / 82.98 ± 1.32</td> <!-- NorNE-nb -->
   <td class="no ner">72.29 ± 1.44 / 76.65 ± 1.24</td> <!-- NorNE-nn -->
   <td class="no sent">30.38 ± 2.29 / 42.84 ± 2.38</td> <!-- NoReC -->
   <td class="no la">21.99 ± 6.74 / 54.54 ± 7.12</td> <!-- ScaLA-nb -->
   <td class="no la">19.06 ± 4.26 / 56.45 ± 5.24</td> <!-- ScaLA-nn -->
   <td class="no qa">28.65 ± 1.33 / 32.67 ± 1.63</td> <!-- ScandiQA-no -->
   <td class="sv ner">66.98 ± 1.68 / 73.41 ± 1.54</td> <!-- SUC3 -->
   <td class="sv sent">62.10 ± 1.18 / 60.27 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">34.86 ± 1.29 / 66.98 ± 0.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.21 ± 2.41 / 26.65 ± 2.88</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">56.31 ± 1.01 / 58.50 ± 1.11</td> <!-- DaNE -->
   <td class="da sent">27.78 ± 2.22 / 49.38 ± 2.89</td> <!-- AngryTweets -->
   <td class="da la">3.04 ± 1.85 / 46.85 ± 3.03</td> <!-- ScaLA-da -->
   <td class="da qa">32.12 ± 0.72 / 37.07 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">58.35 ± 1.41 / 60.76 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">55.90 ± 1.12 / 59.62 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">25.98 ± 1.33 / 40.58 ± 0.60</td> <!-- NoReC -->
   <td class="no la">2.65 ± 2.08 / 48.09 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">3.47 ± 1.47 / 48.98 ± 1.75</td> <!-- ScaLA-nn -->
   <td class="no qa">22.82 ± 5.56 / 30.15 ± 5.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.53 ± 1.58 / 49.86 ± 1.85</td> <!-- SUC3 -->
   <td class="sv sent">60.06 ± 1.30 / 55.65 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">3.18 ± 1.63 / 48.38 ± 1.42</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.50 ± 1.35 / 38.20 ± 1.10</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.69 ± 1.67 / 77.86 ± 1.70</td> <!-- DaNE -->
   <td class="da sent">44.48 ± 5.85 / 62.62 ± 4.55</td> <!-- AngryTweets -->
   <td class="da la">30.37 ± 17.09 / 63.92 ± 8.38</td> <!-- ScaLA-da -->
   <td class="da qa">34.66 ± 2.33 / 38.72 ± 2.20</td> <!-- ScandiQA-da -->
   <td class="no ner">68.50 ± 15.04 / 71.73 ± 15.69</td> <!-- NorNE-nb -->
   <td class="no ner">75.76 ± 0.90 / 79.80 ± 0.72</td> <!-- NorNE-nn -->
   <td class="no sent">46.74 ± 5.96 / 60.25 ± 6.04</td> <!-- NoReC -->
   <td class="no la">8.02 ± 12.19 / 50.30 ± 7.19</td> <!-- ScaLA-nb -->
   <td class="no la">17.04 ± 13.78 / 56.87 ± 7.06</td> <!-- ScaLA-nn -->
   <td class="no qa">35.50 ± 1.44 / 39.96 ± 1.27</td> <!-- ScandiQA-no -->
   <td class="sv ner">53.63 ± 12.63 / 58.84 ± 13.92</td> <!-- SUC3 -->
   <td class="sv sent">72.28 ± 0.79 / 71.62 ± 1.38</td> <!-- SweReC -->
   <td class="sv la">37.61 ± 17.89 / 66.93 ± 9.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.09 ± 1.36 / 41.86 ± 1.30</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.54 ± 1.37 / 77.75 ± 1.51</td> <!-- DaNE -->
   <td class="da sent">43.90 ± 1.50 / 62.31 ± 0.96</td> <!-- AngryTweets -->
   <td class="da la">17.16 ± 13.94 / 56.47 ± 7.34</td> <!-- ScaLA-da -->
   <td class="da qa">31.16 ± 2.13 / 35.06 ± 2.13</td> <!-- ScandiQA-da -->
   <td class="no ner">72.24 ± 2.54 / 76.14 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">68.61 ± 1.62 / 72.88 ± 1.50</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 9.23 / 49.08 ± 8.36</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.61 / 49.14 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">-0.08 ± 1.79 / 45.89 ± 3.49</td> <!-- ScaLA-nn -->
   <td class="no qa">33.03 ± 1.23 / 37.33 ± 1.30</td> <!-- ScandiQA-no -->
   <td class="sv ner">60.53 ± 1.38 / 65.95 ± 1.70</td> <!-- SUC3 -->
   <td class="sv sent">64.02 ± 2.78 / 62.27 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">0.80 ± 0.78 / 47.24 ± 3.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.73 ± 1.38 / 40.00 ± 1.33</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">62.48 ± 2.21 / 65.47 ± 2.05</td> <!-- DaNE -->
   <td class="da sent">19.79 ± 1.67 / 42.09 ± 1.98</td> <!-- AngryTweets -->
   <td class="da la">6.15 ± 1.66 / 52.04 ± 1.49</td> <!-- ScaLA-da -->
   <td class="da qa">24.08 ± 2.61 / 29.50 ± 2.91</td> <!-- ScandiQA-da -->
   <td class="no ner">62.99 ± 1.05 / 66.97 ± 1.30</td> <!-- NorNE-nb -->
   <td class="no ner">59.95 ± 2.51 / 63.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">18.85 ± 4.01 / 36.76 ± 2.79</td> <!-- NoReC -->
   <td class="no la">5.83 ± 2.36 / 51.59 ± 1.57</td> <!-- ScaLA-nb -->
   <td class="no la">4.02 ± 2.29 / 51.66 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no qa">25.06 ± 3.47 / 31.42 ± 3.94</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.34 ± 8.27 / 47.19 ± 9.01</td> <!-- SUC3 -->
   <td class="sv sent">56.57 ± 1.41 / 53.47 ± 0.84</td> <!-- SweReC -->
   <td class="sv la">20.92 ± 4.12 / 59.05 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.64 ± 2.91 / 35.18 ± 2.97</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">19.31 ± 2.87 / 15.94 ± 3.01</td> <!-- DaNE -->
   <td class="da sent">17.37 ± 3.82 / 36.83 ± 4.86</td> <!-- AngryTweets -->
   <td class="da la">1.34 ± 0.97 / 35.45 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da qa">4.68 ± 1.62 / 9.73 ± 3.03</td> <!-- ScandiQA-da -->
   <td class="no ner">23.54 ± 3.23 / 25.49 ± 3.39</td> <!-- NorNE-nb -->
   <td class="no ner">24.10 ± 1.64 / 25.94 ± 1.70</td> <!-- NorNE-nn -->
   <td class="no sent">12.60 ± 2.97 / 32.27 ± 3.43</td> <!-- NoReC -->
   <td class="no la">0.50 ± 1.27 / 36.93 ± 4.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.83 ± 1.64 / 37.67 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">4.42 ± 1.48 / 10.50 ± 2.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">11.31 ± 2.90 / 11.91 ± 3.04</td> <!-- SUC3 -->
   <td class="sv sent">51.11 ± 5.32 / 50.09 ± 3.33</td> <!-- SweReC -->
   <td class="sv la">0.86 ± 0.82 / 39.16 ± 3.63</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.30 ± 2.28 / 14.74 ± 2.84</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">15.26 ± 0.99 / 10.05 ± 1.26</td> <!-- DaNE -->
   <td class="da sent">18.61 ± 4.17 / 35.23 ± 3.90</td> <!-- AngryTweets -->
   <td class="da la">0.30 ± 1.39 / 37.84 ± 3.88</td> <!-- ScaLA-da -->
   <td class="da qa">0.01 ± 0.02 / 0.07 ± 0.09</td> <!-- ScandiQA-da -->
   <td class="no ner">17.08 ± 1.97 / 18.38 ± 2.01</td> <!-- NorNE-nb -->
   <td class="no ner">11.65 ± 1.21 / 12.76 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">15.29 ± 5.37 / 34.15 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.17 ± 0.84 / 36.29 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.37 ± 0.69 / 35.08 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no qa">0.09 ± 0.11 / 0.30 ± 0.30</td> <!-- ScandiQA-no -->
   <td class="sv ner">9.71 ± 1.00 / 10.54 ± 1.12</td> <!-- SUC3 -->
   <td class="sv sent">55.54 ± 2.75 / 52.75 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">-0.15 ± 0.52 / 35.33 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.22 ± 0.22 / 1.06 ± 0.78</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.39 ± 1.26 / 85.36 ± 1.23</td> <!-- DaNE -->
   <td class="da sent">51.33 ± 1.24 / 67.04 ± 1.22</td> <!-- AngryTweets -->
   <td class="da la">44.45 ± 19.17 / 70.51 ± 10.21</td> <!-- ScaLA-da -->
   <td class="da qa">39.92 ± 1.87 / 43.84 ± 1.80</td> <!-- ScandiQA-da -->
   <td class="no ner">89.26 ± 0.97 / 91.66 ± 0.74</td> <!-- NorNE-nb -->
   <td class="no ner">84.51 ± 1.03 / 87.74 ± 0.77</td> <!-- NorNE-nn -->
   <td class="no sent">57.43 ± 1.55 / 70.43 ± 1.41</td> <!-- NoReC -->
   <td class="no la">63.31 ± 11.58 / 80.18 ± 5.59</td> <!-- ScaLA-nb -->
   <td class="no la">62.79 ± 11.35 / 79.65 ± 6.48</td> <!-- ScaLA-nn -->
   <td class="no qa">40.25 ± 1.75 / 44.93 ± 1.66</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.45 ± 0.86 / 79.75 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">74.73 ± 1.15 / 70.83 ± 3.72</td> <!-- SweReC -->
   <td class="sv la">53.55 ± 16.68 / 75.79 ± 8.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.80 ± 0.83 / 46.25 ± 0.83</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">81.55 ± 0.91 / 84.37 ± 0.86</td> <!-- DaNE -->
   <td class="da sent">47.83 ± 1.22 / 64.90 ± 0.81</td> <!-- AngryTweets -->
   <td class="da la">54.99 ± 11.90 / 75.82 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">38.76 ± 2.08 / 43.19 ± 1.97</td> <!-- ScandiQA-da -->
   <td class="no ner">87.83 ± 1.34 / 90.60 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">83.48 ± 0.98 / 86.76 ± 0.82</td> <!-- NorNE-nn -->
   <td class="no sent">52.19 ± 2.87 / 65.60 ± 2.58</td> <!-- NoReC -->
   <td class="no la">54.98 ± 14.19 / 75.67 ± 6.70</td> <!-- ScaLA-nb -->
   <td class="no la">58.33 ± 10.94 / 77.88 ± 5.29</td> <!-- ScaLA-nn -->
   <td class="no qa">37.17 ± 1.92 / 42.00 ± 1.85</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.10 ± 0.94 / 77.97 ± 0.82</td> <!-- SUC3 -->
   <td class="sv sent">73.27 ± 0.75 / 71.87 ± 1.30</td> <!-- SweReC -->
   <td class="sv la">47.19 ± 16.37 / 72.10 ± 8.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.39 ± 1.09 / 43.97 ± 1.12</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">73.58 ± 0.87 / 76.88 ± 0.69</td> <!-- DaNE -->
   <td class="da sent">29.52 ± 2.89 / 47.81 ± 4.54</td> <!-- AngryTweets -->
   <td class="da la">57.10 ± 2.02 / 78.14 ± 1.10</td> <!-- ScaLA-da -->
   <td class="da qa">30.51 ± 1.57 / 34.62 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="no ner">72.78 ± 1.16 / 76.07 ± 1.18</td> <!-- NorNE-nb -->
   <td class="no ner">66.73 ± 1.21 / 70.94 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">32.49 ± 1.55 / 43.12 ± 0.71</td> <!-- NoReC -->
   <td class="no la">35.43 ± 2.39 / 66.84 ± 1.17</td> <!-- ScaLA-nb -->
   <td class="no la">21.11 ± 1.97 / 60.09 ± 0.93</td> <!-- ScaLA-nn -->
   <td class="no qa">26.67 ± 1.46 / 31.96 ± 1.19</td> <!-- ScandiQA-no -->
   <td class="sv ner">51.37 ± 1.03 / 55.06 ± 0.96</td> <!-- SUC3 -->
   <td class="sv sent">53.70 ± 1.46 / 51.98 ± 0.58</td> <!-- SweReC -->
   <td class="sv la">12.38 ± 3.23 / 55.18 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.49 ± 1.91 / 33.66 ± 1.69</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.83 ± 1.31 / 77.16 ± 1.46</td> <!-- DaNE -->
   <td class="da sent">31.18 ± 0.94 / 53.05 ± 1.16</td> <!-- AngryTweets -->
   <td class="da la">13.25 ± 3.71 / 53.61 ± 2.94</td> <!-- ScaLA-da -->
   <td class="da qa">32.11 ± 1.07 / 35.72 ± 1.03</td> <!-- ScandiQA-da -->
   <td class="no ner">78.30 ± 1.00 / 81.82 ± 0.85</td> <!-- NorNE-nb -->
   <td class="no ner">72.08 ± 1.15 / 75.89 ± 1.11</td> <!-- NorNE-nn -->
   <td class="no sent">33.42 ± 1.96 / 48.63 ± 3.34</td> <!-- NoReC -->
   <td class="no la">14.99 ± 4.11 / 52.87 ± 4.48</td> <!-- ScaLA-nb -->
   <td class="no la">13.63 ± 4.52 / 53.34 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">32.62 ± 1.18 / 36.49 ± 1.13</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.78 ± 1.37 / 80.12 ± 1.41</td> <!-- SUC3 -->
   <td class="sv sent">71.28 ± 1.09 / 69.73 ± 2.94</td> <!-- SweReC -->
   <td class="sv la">51.58 ± 2.89 / 73.82 ± 2.21</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.72 ± 1.71 / 43.73 ± 1.81</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">66.62 ± 2.08 / 68.05 ± 1.75</td> <!-- DaNE -->
   <td class="da sent">24.17 ± 1.92 / 43.75 ± 2.75</td> <!-- AngryTweets -->
   <td class="da la">8.14 ± 3.76 / 51.78 ± 1.81</td> <!-- ScaLA-da -->
   <td class="da qa">32.18 ± 2.45 / 36.69 ± 2.13</td> <!-- ScandiQA-da -->
   <td class="no ner">64.83 ± 1.55 / 68.63 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">63.70 ± 2.54 / 67.70 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">25.68 ± 2.17 / 41.65 ± 2.77</td> <!-- NoReC -->
   <td class="no la">6.73 ± 5.40 / 48.20 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">3.35 ± 2.61 / 47.52 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">35.51 ± 3.56 / 40.82 ± 3.52</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.29 ± 1.48 / 68.83 ± 1.00</td> <!-- SUC3 -->
   <td class="sv sent">64.25 ± 1.66 / 63.62 ± 2.92</td> <!-- SweReC -->
   <td class="sv la">28.62 ± 9.43 / 59.33 ± 5.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.53 ± 1.59 / 42.59 ± 1.64</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.62 ± 1.34 / 84.33 ± 1.31</td> <!-- DaNE -->
   <td class="da sent">47.73 ± 1.45 / 64.85 ± 1.13</td> <!-- AngryTweets -->
   <td class="da la">68.28 ± 1.77 / 83.52 ± 1.02</td> <!-- ScaLA-da -->
   <td class="da qa">39.00 ± 3.30 / 43.62 ± 3.41</td> <!-- ScandiQA-da -->
   <td class="no ner">88.45 ± 0.70 / 91.09 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">81.88 ± 2.16 / 85.72 ± 1.92</td> <!-- NorNE-nn -->
   <td class="no sent">50.90 ± 3.01 / 60.96 ± 5.41</td> <!-- NoReC -->
   <td class="no la">69.34 ± 3.13 / 83.11 ± 2.17</td> <!-- ScaLA-nb -->
   <td class="no la">66.24 ± 2.41 / 82.36 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">40.16 ± 2.68 / 45.07 ± 2.82</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.06 ± 2.01 / 79.08 ± 2.32</td> <!-- SUC3 -->
   <td class="sv sent">72.53 ± 0.98 / 67.74 ± 3.02</td> <!-- SweReC -->
   <td class="sv la">73.01 ± 1.43 / 85.98 ± 0.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.94 ± 1.65 / 48.90 ± 1.62</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.74 ± 0.65 / 85.59 ± 0.49</td> <!-- DaNE -->
   <td class="da sent">46.78 ± 1.57 / 64.46 ± 1.17</td> <!-- AngryTweets -->
   <td class="da la">11.27 ± 2.21 / 51.47 ± 2.07</td> <!-- ScaLA-da -->
   <td class="da qa">34.24 ± 2.36 / 38.46 ± 2.36</td> <!-- ScandiQA-da -->
   <td class="no ner">87.71 ± 1.24 / 90.14 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">80.21 ± 2.19 / 84.12 ± 1.85</td> <!-- NorNE-nn -->
   <td class="no sent">44.42 ± 13.10 / 57.73 ± 11.86</td> <!-- NoReC -->
   <td class="no la">11.20 ± 2.99 / 48.77 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">7.12 ± 2.39 / 49.23 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">36.21 ± 4.09 / 41.02 ± 3.97</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.17 ± 1.10 / 79.43 ± 1.07</td> <!-- SUC3 -->
   <td class="sv sent">71.48 ± 2.63 / 65.72 ± 4.78</td> <!-- SweReC -->
   <td class="sv la">7.26 ± 2.18 / 45.42 ± 4.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.63 ± 3.75 / 42.67 ± 3.52</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">75.13 ± 1.16 / 76.66 ± 0.79</td> <!-- DaNE -->
   <td class="da sent">46.39 ± 1.25 / 63.97 ± 1.08</td> <!-- AngryTweets -->
   <td class="da la">38.61 ± 1.86 / 67.08 ± 1.08</td> <!-- ScaLA-da -->
   <td class="da qa">33.31 ± 1.89 / 38.56 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="no ner">77.69 ± 1.29 / 81.26 ± 1.25</td> <!-- NorNE-nb -->
   <td class="no ner">69.84 ± 1.91 / 74.05 ± 1.72</td> <!-- NorNE-nn -->
   <td class="no sent">49.93 ± 1.46 / 62.37 ± 2.34</td> <!-- NoReC -->
   <td class="no la">38.26 ± 7.56 / 66.01 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">25.17 ± 5.32 / 61.27 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no qa">23.23 ± 1.48 / 29.46 ± 1.31</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.97 ± 1.48 / 70.22 ± 1.49</td> <!-- SUC3 -->
   <td class="sv sent">71.33 ± 1.20 / 65.44 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">39.60 ± 5.87 / 66.60 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.21 ± 1.82 / 33.58 ± 1.55</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">71.23 ± 1.20 / 72.66 ± 1.16</td> <!-- DaNE -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- AngryTweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">25.13 ± 2.53 / 30.95 ± 2.37</td> <!-- ScandiQA-da -->
   <td class="no ner">74.83 ± 0.79 / 77.81 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">68.32 ± 1.13 / 72.22 ± 0.95</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">28.46 ± 1.31 / 34.90 ± 1.43</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.72 ± 1.22 / 65.50 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">68.36 ± 1.18 / 63.94 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">26.38 ± 2.09 / 33.19 ± 1.97</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">79.21 ± 0.98 / 81.90 ± 0.92</td> <!-- DaNE -->
   <td class="da sent">33.31 ± 1.49 / 54.09 ± 1.49</td> <!-- AngryTweets -->
   <td class="da la">33.35 ± 7.32 / 64.61 ± 4.56</td> <!-- ScaLA-da -->
   <td class="da qa">35.59 ± 2.39 / 39.57 ± 2.39</td> <!-- ScandiQA-da -->
   <td class="no ner">82.13 ± 1.28 / 85.33 ± 1.01</td> <!-- NorNE-nb -->
   <td class="no ner">75.74 ± 1.96 / 79.44 ± 1.66</td> <!-- NorNE-nn -->
   <td class="no sent">38.17 ± 2.21 / 50.44 ± 3.11</td> <!-- NoReC -->
   <td class="no la">39.49 ± 3.36 / 68.13 ± 2.13</td> <!-- ScaLA-nb -->
   <td class="no la">22.17 ± 7.22 / 60.16 ± 3.80</td> <!-- ScaLA-nn -->
   <td class="no qa">39.51 ± 1.62 / 43.75 ± 1.73</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.95 ± 1.72 / 81.23 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">75.73 ± 0.72 / 73.61 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">78.60 ± 0.98 / 88.95 ± 0.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.06 ± 1.72 / 51.14 ± 1.65</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.57 ± 1.34 / 79.19 ± 1.49</td> <!-- DaNE -->
   <td class="da sent">36.85 ± 3.28 / 56.27 ± 3.98</td> <!-- AngryTweets -->
   <td class="da la">63.55 ± 1.19 / 81.41 ± 0.64</td> <!-- ScaLA-da -->
   <td class="da qa">34.36 ± 1.89 / 38.66 ± 1.76</td> <!-- ScandiQA-da -->
   <td class="no ner">76.09 ± 0.70 / 79.50 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.39 / 73.03 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">32.40 ± 1.48 / 44.59 ± 1.66</td> <!-- NoReC -->
   <td class="no la">41.65 ± 1.95 / 70.35 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">25.53 ± 2.31 / 62.04 ± 1.19</td> <!-- ScaLA-nn -->
   <td class="no qa">31.28 ± 1.82 / 36.01 ± 1.68</td> <!-- ScandiQA-no -->
   <td class="sv ner">53.87 ± 1.25 / 58.01 ± 1.23</td> <!-- SUC3 -->
   <td class="sv sent">57.67 ± 1.61 / 53.64 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">13.40 ± 4.31 / 55.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.63 ± 1.57 / 37.37 ± 1.40</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sarnikowski/electra-small-generator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">4</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">22,313 ± 3,528 / 5,726 ± 1,931</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">42.78 ± 1.74 / 42.53 ± 1.99</td> <!-- DaNE -->
   <td class="da sent">22.19 ± 2.04 / 41.57 ± 2.98</td> <!-- AngryTweets -->
   <td class="da la">2.43 ± 1.83 / 49.01 ± 3.57</td> <!-- ScaLA-da -->
   <td class="da qa">4.25 ± 0.63 / 10.17 ± 1.04</td> <!-- ScandiQA-da -->
   <td class="no ner">38.64 ± 1.57 / 40.85 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">32.27 ± 2.23 / 34.11 ± 2.36</td> <!-- NorNE-nn -->
   <td class="no sent">20.93 ± 2.47 / 39.13 ± 1.34</td> <!-- NoReC -->
   <td class="no la">4.84 ± 1.74 / 51.70 ± 1.02</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.59 / 49.43 ± 1.58</td> <!-- ScaLA-nn -->
   <td class="no qa">3.99 ± 0.40 / 10.80 ± 0.78</td> <!-- ScandiQA-no -->
   <td class="sv ner">27.06 ± 1.32 / 28.81 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">56.38 ± 1.07 / 53.11 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">3.84 ± 2.29 / 49.12 ± 3.68</td> <!-- ScaLA-sv -->
   <td class="sv qa">4.59 ± 0.50 / 11.77 ± 0.63</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">71.23 ± 1.20 / 72.66 ± 1.16</td> <!-- DaNE -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- AngryTweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da qa">25.13 ± 2.53 / 30.95 ± 2.37</td> <!-- ScandiQA-da -->
   <td class="no ner">74.83 ± 0.79 / 77.81 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">68.32 ± 1.13 / 72.22 ± 0.95</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no qa">28.46 ± 1.31 / 34.90 ± 1.43</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.72 ± 1.22 / 65.50 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">68.33 ± 1.03 / 64.03 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">26.38 ± 2.09 / 33.19 ± 1.97</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">45.13 ± 1.23 / 44.10 ± 1.32</td> <!-- DaNE -->
   <td class="da sent">24.11 ± 1.74 / 44.78 ± 2.78</td> <!-- AngryTweets -->
   <td class="da la">2.91 ± 1.07 / 46.98 ± 3.78</td> <!-- ScaLA-da -->
   <td class="da qa">25.43 ± 2.25 / 31.72 ± 2.31</td> <!-- ScandiQA-da -->
   <td class="no ner">46.11 ± 1.04 / 49.30 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">43.01 ± 2.05 / 46.11 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">23.21 ± 2.32 / 44.26 ± 2.95</td> <!-- NoReC -->
   <td class="no la">2.26 ± 1.47 / 45.07 ± 4.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.66 ± 1.81 / 44.50 ± 3.45</td> <!-- ScaLA-nn -->
   <td class="no qa">22.67 ± 1.62 / 29.77 ± 1.60</td> <!-- ScandiQA-no -->
   <td class="sv ner">46.67 ± 1.98 / 51.13 ± 2.13</td> <!-- SUC3 -->
   <td class="sv sent">61.67 ± 1.40 / 59.12 ± 2.44</td> <!-- SweReC -->
   <td class="sv la">2.87 ± 1.53 / 48.92 ± 2.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">27.14 ± 1.99 / 34.45 ± 1.97</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">42.02 ± 10.18 / 43.71 ± 10.38</td> <!-- DaNE -->
   <td class="da sent">22.07 ± 2.24 / 44.70 ± 3.72</td> <!-- AngryTweets -->
   <td class="da la">1.63 ± 1.49 / 45.36 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da qa">8.68 ± 3.32 / 16.14 ± 3.07</td> <!-- ScandiQA-da -->
   <td class="no ner">52.52 ± 3.51 / 55.55 ± 3.71</td> <!-- NorNE-nb -->
   <td class="no ner">50.23 ± 3.00 / 53.53 ± 3.03</td> <!-- NorNE-nn -->
   <td class="no sent">12.69 ± 4.51 / 32.23 ± 3.53</td> <!-- NoReC -->
   <td class="no la">2.79 ± 1.16 / 47.71 ± 2.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.66 ± 2.18 / 46.60 ± 2.87</td> <!-- ScaLA-nn -->
   <td class="no qa">14.55 ± 4.44 / 22.28 ± 3.84</td> <!-- ScandiQA-no -->
   <td class="sv ner">40.46 ± 3.04 / 42.78 ± 3.26</td> <!-- SUC3 -->
   <td class="sv sent">44.95 ± 2.30 / 48.17 ± 1.06</td> <!-- SweReC -->
   <td class="sv la">1.43 ± 1.34 / 48.66 ± 2.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.14 ± 3.56 / 21.74 ± 3.20</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">63.95 ± 1.09 / 65.37 ± 1.21</td> <!-- DaNE -->
   <td class="da sent">27.93 ± 0.66 / 50.86 ± 0.42</td> <!-- AngryTweets -->
   <td class="da la">5.42 ± 2.85 / 48.29 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">28.62 ± 2.21 / 33.54 ± 2.07</td> <!-- ScandiQA-da -->
   <td class="no ner">66.15 ± 1.66 / 69.65 ± 1.48</td> <!-- NorNE-nb -->
   <td class="no ner">62.75 ± 1.40 / 66.78 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">26.33 ± 1.84 / 40.67 ± 0.71</td> <!-- NoReC -->
   <td class="no la">6.62 ± 3.40 / 48.37 ± 4.02</td> <!-- ScaLA-nb -->
   <td class="no la">5.16 ± 3.07 / 45.99 ± 4.76</td> <!-- ScaLA-nn -->
   <td class="no qa">29.61 ± 1.07 / 34.97 ± 1.23</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.03 ± 1.08 / 66.11 ± 1.24</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.84 / 55.24 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">26.28 ± 8.44 / 59.64 ± 5.68</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.62 ± 1.13 / 37.22 ± 1.04</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">41.43 ± 3.77 / 41.23 ± 4.61</td> <!-- DaNE -->
   <td class="da sent">20.71 ± 1.68 / 40.07 ± 2.65</td> <!-- AngryTweets -->
   <td class="da la">1.19 ± 1.08 / 48.46 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">7.50 ± 3.84 / 11.50 ± 5.60</td> <!-- ScandiQA-da -->
   <td class="no ner">43.54 ± 3.44 / 46.11 ± 3.68</td> <!-- NorNE-nb -->
   <td class="no ner">33.22 ± 4.64 / 35.18 ± 4.90</td> <!-- NorNE-nn -->
   <td class="no sent">19.19 ± 2.87 / 37.36 ± 1.97</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.42 / 50.99 ± 0.83</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 1.04 / 49.39 ± 0.80</td> <!-- ScaLA-nn -->
   <td class="no qa">3.69 ± 2.27 / 6.80 ± 4.09</td> <!-- ScandiQA-no -->
   <td class="sv ner">25.42 ± 2.14 / 26.87 ± 2.26</td> <!-- SUC3 -->
   <td class="sv sent">57.41 ± 1.89 / 53.50 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">-1.06 ± 1.33 / 48.72 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv qa">7.29 ± 2.82 / 12.63 ± 4.51</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.48 ± 1.31 / 82.81 ± 1.46</td> <!-- DaNE -->
   <td class="da sent">33.91 ± 1.43 / 54.87 ± 1.38</td> <!-- AngryTweets -->
   <td class="da la">40.96 ± 4.05 / 69.68 ± 2.12</td> <!-- ScaLA-da -->
   <td class="da qa">48.52 ± 1.57 / 52.29 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">85.89 ± 1.04 / 89.07 ± 1.08</td> <!-- NorNE-nb -->
   <td class="no ner">79.22 ± 0.93 / 82.69 ± 0.90</td> <!-- NorNE-nn -->
   <td class="no sent">34.97 ± 1.74 / 48.21 ± 2.02</td> <!-- NoReC -->
   <td class="no la">39.58 ± 5.70 / 67.91 ± 3.00</td> <!-- ScaLA-nb -->
   <td class="no la">31.27 ± 9.57 / 62.81 ± 7.17</td> <!-- ScaLA-nn -->
   <td class="no qa">45.81 ± 0.69 / 50.74 ± 0.83</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.89 ± 0.52 / 75.33 ± 0.99</td> <!-- SUC3 -->
   <td class="sv sent">61.80 ± 1.76 / 58.93 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 5.98 / 66.91 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.09 ± 1.17 / 51.88 ± 1.11</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">44.89 ± 1.33 / 46.99 ± 1.64</td> <!-- DaNE -->
   <td class="da sent">30.67 ± 1.28 / 51.76 ± 1.28</td> <!-- AngryTweets -->
   <td class="da la">13.01 ± 5.22 / 55.11 ± 3.40</td> <!-- ScaLA-da -->
   <td class="da qa">0.05 ± 0.03 / 0.52 ± 0.12</td> <!-- ScandiQA-da -->
   <td class="no ner">39.53 ± 1.04 / 42.18 ± 1.03</td> <!-- NorNE-nb -->
   <td class="no ner">34.88 ± 1.76 / 37.39 ± 1.81</td> <!-- NorNE-nn -->
   <td class="no sent">24.39 ± 1.60 / 40.44 ± 1.78</td> <!-- NoReC -->
   <td class="no la">7.29 ± 2.49 / 49.37 ± 3.58</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 46.00 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">0.05 ± 0.05 / 0.73 ± 0.20</td> <!-- ScandiQA-no -->
   <td class="sv ner">20.74 ± 1.42 / 22.47 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">53.88 ± 1.97 / 52.30 ± 1.04</td> <!-- SweReC -->
   <td class="sv la">1.55 ± 1.62 / 44.06 ± 3.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.06 ± 0.07 / 0.64 ± 0.31</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">81.10 ± 1.46 / 83.56 ± 1.47</td> <!-- DaNE -->
   <td class="da sent">49.77 ± 0.92 / 66.38 ± 0.56</td> <!-- AngryTweets -->
   <td class="da la">64.31 ± 2.24 / 80.70 ± 1.53</td> <!-- ScaLA-da -->
   <td class="da qa">39.79 ± 1.89 / 43.93 ± 1.81</td> <!-- ScandiQA-da -->
   <td class="no ner">88.71 ± 0.94 / 91.16 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">80.56 ± 1.59 / 84.75 ± 1.23</td> <!-- NorNE-nn -->
   <td class="no sent">55.25 ± 2.36 / 66.95 ± 2.79</td> <!-- NoReC -->
   <td class="no la">68.03 ± 2.37 / 82.12 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">66.90 ± 2.07 / 82.33 ± 1.34</td> <!-- ScaLA-nn -->
   <td class="no qa">38.43 ± 1.81 / 43.20 ± 1.78</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.89 ± 2.16 / 74.48 ± 2.35</td> <!-- SUC3 -->
   <td class="sv sent">74.58 ± 1.29 / 70.97 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">69.07 ± 2.22 / 83.17 ± 1.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.96 ± 1.70 / 45.69 ± 1.59</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.40 ± 1.74 / 80.25 ± 1.91</td> <!-- DaNE -->
   <td class="da sent">50.48 ± 0.68 / 66.71 ± 0.40</td> <!-- AngryTweets -->
   <td class="da la">64.34 ± 2.43 / 80.92 ± 1.67</td> <!-- ScaLA-da -->
   <td class="da qa">39.50 ± 1.96 / 43.47 ± 1.92</td> <!-- ScandiQA-da -->
   <td class="no ner">85.81 ± 1.57 / 89.07 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">78.80 ± 2.22 / 83.27 ± 1.68</td> <!-- NorNE-nn -->
   <td class="no sent">53.23 ± 1.67 / 65.23 ± 2.65</td> <!-- NoReC -->
   <td class="no la">70.06 ± 2.33 / 83.61 ± 1.61</td> <!-- ScaLA-nb -->
   <td class="no la">66.81 ± 1.83 / 82.19 ± 1.20</td> <!-- ScaLA-nn -->
   <td class="no qa">36.74 ± 1.41 / 41.42 ± 1.29</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.94 ± 2.04 / 72.25 ± 2.16</td> <!-- SUC3 -->
   <td class="sv sent">75.04 ± 1.08 / 72.35 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">70.16 ± 1.47 / 84.29 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.90 ± 1.83 / 44.57 ± 1.70</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.98 ± 0.92 / 76.63 ± 0.85</td> <!-- DaNE -->
   <td class="da sent">49.13 ± 0.82 / 65.84 ± 0.66</td> <!-- AngryTweets -->
   <td class="da la">29.66 ± 7.69 / 63.05 ± 4.35</td> <!-- ScaLA-da -->
   <td class="da qa">0.14 ± 0.20 / 1.02 ± 1.34</td> <!-- ScandiQA-da -->
   <td class="no ner">78.39 ± 0.86 / 81.94 ± 0.73</td> <!-- NorNE-nb -->
   <td class="no ner">71.27 ± 1.18 / 75.56 ± 1.01</td> <!-- NorNE-nn -->
   <td class="no sent">55.53 ± 1.05 / 68.89 ± 1.16</td> <!-- NoReC -->
   <td class="no la">36.01 ± 2.02 / 64.39 ± 1.49</td> <!-- ScaLA-nb -->
   <td class="no la">14.99 ± 8.03 / 54.08 ± 5.71</td> <!-- ScaLA-nn -->
   <td class="no qa">0.04 ± 0.05 / 1.55 ± 1.67</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.82 ± 1.39 / 65.14 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">73.47 ± 0.84 / 70.20 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 6.55 / 66.09 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.25 ± 0.26 / 2.02 ± 2.04</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">79.96 ± 1.19 / 82.19 ± 1.02</td> <!-- DaNE -->
   <td class="da sent">45.60 ± 1.76 / 63.53 ± 1.48</td> <!-- AngryTweets -->
   <td class="da la">28.26 ± 11.88 / 55.28 ± 7.93</td> <!-- ScaLA-da -->
   <td class="da qa">0.01 ± 0.01 / 0.60 ± 0.99</td> <!-- ScandiQA-da -->
   <td class="no ner">86.62 ± 1.53 / 89.46 ± 1.18</td> <!-- NorNE-nb -->
   <td class="no ner">75.64 ± 1.17 / 79.71 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">52.91 ± 2.29 / 64.64 ± 3.28</td> <!-- NoReC -->
   <td class="no la">27.55 ± 12.16 / 53.28 ± 8.27</td> <!-- ScaLA-nb -->
   <td class="no la">15.20 ± 9.06 / 51.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">0.04 ± 0.05 / 0.63 ± 0.83</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.91 ± 1.27 / 76.31 ± 1.29</td> <!-- SUC3 -->
   <td class="sv sent">73.32 ± 1.13 / 70.21 ± 3.74</td> <!-- SweReC -->
   <td class="sv la">32.29 ± 10.98 / 62.21 ± 5.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.03 ± 0.05 / 0.80 ± 1.07</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">69.55 ± 1.35 / 72.54 ± 1.28</td> <!-- DaNE -->
   <td class="da sent">24.38 ± 1.74 / 40.85 ± 3.07</td> <!-- AngryTweets -->
   <td class="da la">68.58 ± 1.38 / 84.12 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">27.69 ± 1.49 / 33.04 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="no ner">70.05 ± 1.16 / 73.15 ± 1.21</td> <!-- NorNE-nb -->
   <td class="no ner">62.07 ± 1.31 / 66.34 ± 1.25</td> <!-- NorNE-nn -->
   <td class="no sent">29.97 ± 0.99 / 42.12 ± 0.47</td> <!-- NoReC -->
   <td class="no la">40.79 ± 2.06 / 69.48 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">25.08 ± 1.86 / 61.74 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">25.65 ± 1.44 / 31.84 ± 1.29</td> <!-- ScandiQA-no -->
   <td class="sv ner">48.47 ± 0.71 / 52.79 ± 1.21</td> <!-- SUC3 -->
   <td class="sv sent">57.93 ± 1.56 / 53.71 ± 0.61</td> <!-- SweReC -->
   <td class="sv la">14.72 ± 2.01 / 55.92 ± 1.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">26.89 ± 1.09 / 32.71 ± 0.97</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">81.91 ± 0.87 / 84.06 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">48.03 ± 0.74 / 65.34 ± 0.40</td> <!-- AngryTweets -->
   <td class="da la">55.31 ± 2.29 / 76.29 ± 1.57</td> <!-- ScaLA-da -->
   <td class="da qa">49.16 ± 2.73 / 53.75 ± 2.68</td> <!-- ScandiQA-da -->
   <td class="no ner">87.12 ± 1.08 / 90.08 ± 0.76</td> <!-- NorNE-nb -->
   <td class="no ner">81.89 ± 0.98 / 86.04 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">56.35 ± 1.25 / 69.31 ± 1.02</td> <!-- NoReC -->
   <td class="no la">59.38 ± 2.52 / 78.02 ± 1.71</td> <!-- ScaLA-nb -->
   <td class="no la">46.54 ± 3.21 / 71.78 ± 2.00</td> <!-- ScaLA-nn -->
   <td class="no qa">51.46 ± 1.85 / 56.73 ± 1.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.21 ± 1.26 / 80.05 ± 1.13</td> <!-- SUC3 -->
   <td class="sv sent">75.09 ± 1.30 / 72.93 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">61.83 ± 1.28 / 79.96 ± 0.82</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.77 ± 1.30 / 57.11 ± 1.22</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">85.45 ± 1.08 / 87.11 ± 1.23</td> <!-- DaNE -->
   <td class="da sent">37.94 ± 10.08 / 55.77 ± 9.21</td> <!-- AngryTweets -->
   <td class="da la">15.26 ± 10.94 / 48.92 ± 8.26</td> <!-- ScaLA-da -->
   <td class="da qa">52.30 ± 0.80 / 57.35 ± 0.93</td> <!-- ScandiQA-da -->
   <td class="no ner">89.48 ± 0.83 / 91.90 ± 0.62</td> <!-- NorNE-nb -->
   <td class="no ner">82.92 ± 1.66 / 86.59 ± 1.49</td> <!-- NorNE-nn -->
   <td class="no sent">30.56 ± 13.68 / 45.96 ± 11.45</td> <!-- NoReC -->
   <td class="no la">9.79 ± 5.13 / 46.75 ± 6.05</td> <!-- ScaLA-nb -->
   <td class="no la">6.36 ± 2.82 / 48.52 ± 4.11</td> <!-- ScaLA-nn -->
   <td class="no qa">52.77 ± 1.38 / 58.11 ± 1.38</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.53 ± 2.70 / 79.53 ± 2.77</td> <!-- SUC3 -->
   <td class="sv sent">75.42 ± 1.08 / 72.68 ± 3.19</td> <!-- SweReC -->
   <td class="sv la">18.44 ± 10.88 / 53.57 ± 7.20</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.60 ± 1.04 / 60.00 ± 0.86</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.58 ± 1.37 / 79.67 ± 1.34</td> <!-- DaNE -->
   <td class="da sent">39.36 ± 3.13 / 58.64 ± 2.64</td> <!-- AngryTweets -->
   <td class="da la">7.06 ± 6.11 / 49.71 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">43.31 ± 2.11 / 47.39 ± 2.00</td> <!-- ScandiQA-da -->
   <td class="no ner">83.48 ± 1.19 / 86.26 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">76.17 ± 2.67 / 80.10 ± 2.44</td> <!-- NorNE-nn -->
   <td class="no sent">34.17 ± 2.42 / 43.74 ± 2.19</td> <!-- NoReC -->
   <td class="no la">12.11 ± 10.47 / 50.33 ± 7.16</td> <!-- ScaLA-nb -->
   <td class="no la">4.28 ± 4.18 / 45.75 ± 4.32</td> <!-- ScaLA-nn -->
   <td class="no qa">43.51 ± 2.72 / 48.19 ± 2.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.20 ± 1.70 / 74.26 ± 1.65</td> <!-- SUC3 -->
   <td class="sv sent">63.35 ± 5.43 / 60.33 ± 5.50</td> <!-- SweReC -->
   <td class="sv la">16.07 ± 10.73 / 52.48 ± 7.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.74 ± 4.46 / 48.67 ± 4.30</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">81.68 ± 1.38 / 84.31 ± 1.05</td> <!-- DaNE -->
   <td class="da sent">50.19 ± 1.82 / 66.32 ± 1.50</td> <!-- AngryTweets -->
   <td class="da la">69.72 ± 2.25 / 84.30 ± 1.64</td> <!-- ScaLA-da -->
   <td class="da qa">52.03 ± 1.07 / 56.54 ± 1.37</td> <!-- ScandiQA-da -->
   <td class="no ner">84.95 ± 2.83 / 88.70 ± 2.05</td> <!-- NorNE-nb -->
   <td class="no ner">82.16 ± 1.96 / 86.11 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">54.19 ± 3.15 / 65.18 ± 4.55</td> <!-- NoReC -->
   <td class="no la">69.83 ± 2.01 / 84.72 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">54.84 ± 12.59 / 75.13 ± 9.44</td> <!-- ScaLA-nn -->
   <td class="no qa">51.14 ± 1.72 / 55.91 ± 1.86</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.58 ± 1.51 / 78.23 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">75.99 ± 1.15 / 71.01 ± 4.17</td> <!-- SweReC -->
   <td class="sv la">72.17 ± 0.94 / 85.94 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.80 ± 2.25 / 55.83 ± 2.37</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">77.68 ± 0.74 / 79.94 ± 0.83</td> <!-- DaNE -->
   <td class="da sent">33.50 ± 2.57 / 54.63 ± 2.14</td> <!-- AngryTweets -->
   <td class="da la">46.75 ± 3.43 / 72.71 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">49.17 ± 0.76 / 53.32 ± 0.84</td> <!-- ScandiQA-da -->
   <td class="no ner">79.06 ± 1.52 / 82.90 ± 1.44</td> <!-- NorNE-nb -->
   <td class="no ner">72.83 ± 1.96 / 77.33 ± 2.00</td> <!-- NorNE-nn -->
   <td class="no sent">37.28 ± 2.13 / 48.69 ± 3.26</td> <!-- NoReC -->
   <td class="no la">49.41 ± 1.57 / 73.96 ± 0.87</td> <!-- ScaLA-nb -->
   <td class="no la">43.58 ± 2.23 / 71.20 ± 1.61</td> <!-- ScaLA-nn -->
   <td class="no qa">46.16 ± 1.80 / 50.73 ± 1.89</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.50 ± 1.71 / 70.85 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">63.30 ± 0.93 / 59.96 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">48.97 ± 1.14 / 73.78 ± 0.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.22 ± 1.91 / 50.81 ± 2.00</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">76.16 ± 0.89 / 78.57 ± 0.83</td> <!-- DaNE -->
   <td class="da sent">32.95 ± 0.82 / 54.57 ± 0.80</td> <!-- AngryTweets -->
   <td class="da la">33.63 ± 2.63 / 65.69 ± 1.82</td> <!-- ScaLA-da -->
   <td class="da qa">37.92 ± 1.65 / 41.72 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">81.01 ± 0.94 / 83.93 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">75.07 ± 1.03 / 79.39 ± 1.03</td> <!-- NorNE-nn -->
   <td class="no sent">32.32 ± 2.30 / 47.12 ± 2.85</td> <!-- NoReC -->
   <td class="no la">36.15 ± 1.99 / 66.57 ± 1.11</td> <!-- ScaLA-nb -->
   <td class="no la">30.17 ± 1.72 / 63.98 ± 1.36</td> <!-- ScaLA-nn -->
   <td class="no qa">36.88 ± 1.18 / 41.12 ± 1.14</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.61 ± 1.27 / 69.28 ± 1.15</td> <!-- SUC3 -->
   <td class="sv sent">59.53 ± 1.69 / 57.93 ± 2.20</td> <!-- SweReC -->
   <td class="sv la">29.36 ± 1.50 / 63.60 ± 0.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.60 ± 1.02 / 46.04 ± 0.91</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">55.05 ± 1.66 / 56.69 ± 1.54</td> <!-- DaNE -->
   <td class="da sent">26.03 ± 0.90 / 48.46 ± 1.21</td> <!-- AngryTweets -->
   <td class="da la">2.19 ± 1.92 / 49.80 ± 1.39</td> <!-- ScaLA-da -->
   <td class="da qa">22.16 ± 1.47 / 28.35 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="no ner">58.24 ± 1.47 / 61.55 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">56.03 ± 1.41 / 59.90 ± 1.56</td> <!-- NorNE-nn -->
   <td class="no sent">24.59 ± 1.57 / 40.34 ± 0.99</td> <!-- NoReC -->
   <td class="no la">3.45 ± 2.10 / 50.80 ± 1.16</td> <!-- ScaLA-nb -->
   <td class="no la">2.72 ± 1.56 / 48.79 ± 1.92</td> <!-- ScaLA-nn -->
   <td class="no qa">23.14 ± 1.75 / 30.36 ± 1.63</td> <!-- ScandiQA-no -->
   <td class="sv ner">47.04 ± 3.83 / 50.07 ± 4.14</td> <!-- SUC3 -->
   <td class="sv sent">56.10 ± 1.85 / 52.92 ± 0.76</td> <!-- SweReC -->
   <td class="sv la">5.05 ± 2.27 / 51.08 ± 1.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">21.66 ± 1.09 / 29.00 ± 1.21</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">30.47 ± 1.44 / 29.37 ± 1.40</td> <!-- DaNE -->
   <td class="da sent">20.33 ± 1.89 / 40.95 ± 2.78</td> <!-- AngryTweets -->
   <td class="da la">0.90 ± 1.40 / 48.85 ± 2.60</td> <!-- ScaLA-da -->
   <td class="da qa">4.78 ± 0.58 / 11.12 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="no ner">30.31 ± 2.14 / 31.87 ± 2.26</td> <!-- NorNE-nb -->
   <td class="no ner">30.59 ± 1.43 / 32.47 ± 1.48</td> <!-- NorNE-nn -->
   <td class="no sent">15.07 ± 1.97 / 35.80 ± 1.15</td> <!-- NoReC -->
   <td class="no la">1.26 ± 1.26 / 48.42 ± 1.75</td> <!-- ScaLA-nb -->
   <td class="no la">0.49 ± 1.58 / 45.93 ± 3.88</td> <!-- ScaLA-nn -->
   <td class="no qa">3.83 ± 0.66 / 10.51 ± 1.00</td> <!-- ScandiQA-no -->
   <td class="sv ner">23.05 ± 1.43 / 24.61 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">52.31 ± 1.22 / 51.51 ± 0.49</td> <!-- SweReC -->
   <td class="sv la">1.32 ± 1.87 / 46.80 ± 4.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">3.85 ± 0.78 / 10.00 ± 1.75</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.55 ± 0.90 / 77.53 ± 0.90</td> <!-- DaNE -->
   <td class="da sent">39.40 ± 1.14 / 59.02 ± 0.60</td> <!-- AngryTweets -->
   <td class="da la">23.50 ± 1.86 / 59.54 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">39.43 ± 2.37 / 44.55 ± 2.51</td> <!-- ScandiQA-da -->
   <td class="no ner">79.13 ± 1.26 / 82.20 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">72.90 ± 1.43 / 76.64 ± 1.10</td> <!-- NorNE-nn -->
   <td class="no sent">40.20 ± 1.56 / 54.68 ± 2.46</td> <!-- NoReC -->
   <td class="no la">24.45 ± 2.21 / 58.75 ± 1.80</td> <!-- ScaLA-nb -->
   <td class="no la">19.18 ± 3.55 / 57.93 ± 2.05</td> <!-- ScaLA-nn -->
   <td class="no qa">39.12 ± 2.67 / 44.42 ± 2.98</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.93 ± 1.08 / 78.91 ± 1.24</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 0.81 / 72.74 ± 2.11</td> <!-- SweReC -->
   <td class="sv la">70.08 ± 2.11 / 83.40 ± 1.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.34 ± 1.23 / 53.17 ± 1.03</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,280 ± 2,296 / 4,838 ± 1,583</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.40 ± 1.84 / 79.01 ± 1.66</td> <!-- DaNE -->
   <td class="da sent">40.06 ± 1.09 / 59.62 ± 0.80</td> <!-- AngryTweets -->
   <td class="da la">33.73 ± 6.11 / 65.40 ± 4.04</td> <!-- ScaLA-da -->
   <td class="da qa">33.39 ± 2.24 / 37.59 ± 2.12</td> <!-- ScandiQA-da -->
   <td class="no ner">87.89 ± 0.79 / 90.55 ± 0.63</td> <!-- NorNE-nb -->
   <td class="no ner">82.22 ± 1.58 / 85.72 ± 1.45</td> <!-- NorNE-nn -->
   <td class="no sent">52.65 ± 1.78 / 64.34 ± 2.59</td> <!-- NoReC -->
   <td class="no la">66.85 ± 2.72 / 82.12 ± 1.73</td> <!-- ScaLA-nb -->
   <td class="no la">54.86 ± 10.30 / 76.67 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no qa">37.68 ± 1.35 / 42.92 ± 1.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.27 ± 1.66 / 69.22 ± 0.88</td> <!-- SUC3 -->
   <td class="sv sent">62.59 ± 1.35 / 60.17 ± 2.69</td> <!-- SweReC -->
   <td class="sv la">22.87 ± 3.41 / 59.79 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.73 ± 2.86 / 38.50 ± 2.77</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>mideind/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,697 ± 2,113 / 5,432 ± 1,749</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">67.86 ± 1.25 / 71.51 ± 1.10</td> <!-- DaNE -->
   <td class="da sent">22.70 ± 2.43 / 44.12 ± 3.94</td> <!-- AngryTweets -->
   <td class="da la">-0.27 ± 2.37 / 39.44 ± 4.09</td> <!-- ScaLA-da -->
   <td class="da qa">30.52 ± 3.63 / 33.17 ± 3.98</td> <!-- ScandiQA-da -->
   <td class="no ner">71.71 ± 1.20 / 75.50 ± 1.15</td> <!-- NorNE-nb -->
   <td class="no ner">67.09 ± 1.04 / 71.88 ± 0.73</td> <!-- NorNE-nn -->
   <td class="no sent">14.13 ± 5.52 / 33.71 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.68 ± 2.45 / 42.20 ± 4.02</td> <!-- ScaLA-nb -->
   <td class="no la">0.92 ± 1.54 / 37.68 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no qa">30.40 ± 3.02 / 33.96 ± 3.14</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.43 ± 1.13 / 63.51 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">55.09 ± 2.80 / 52.44 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">1.53 ± 1.85 / 42.55 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.13 ± 2.77 / 34.89 ± 2.76</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>patrickvonplaten/norwegian-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,698 ± 2,699 / 3,891 ± 1,278</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">74.45 ± 0.71 / 77.37 ± 0.74</td> <!-- DaNE -->
   <td class="da sent">40.66 ± 0.60 / 60.41 ± 0.40</td> <!-- AngryTweets -->
   <td class="da la">36.60 ± 8.17 / 65.89 ± 4.40</td> <!-- ScaLA-da -->
   <td class="da qa">33.51 ± 1.85 / 37.38 ± 1.97</td> <!-- ScandiQA-da -->
   <td class="no ner">85.72 ± 0.68 / 88.58 ± 0.62</td> <!-- NorNE-nb -->
   <td class="no ner">79.58 ± 1.00 / 83.60 ± 0.98</td> <!-- NorNE-nn -->
   <td class="no sent">58.16 ± 1.17 / 70.61 ± 1.02</td> <!-- NoReC -->
   <td class="no la">64.86 ± 2.58 / 80.24 ± 1.80</td> <!-- ScaLA-nb -->
   <td class="no la">52.72 ± 2.04 / 74.23 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no qa">35.53 ± 1.45 / 39.65 ± 1.46</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.56 ± 1.57 / 69.21 ± 1.36</td> <!-- SUC3 -->
   <td class="sv sent">63.27 ± 2.13 / 62.27 ± 3.49</td> <!-- SweReC -->
   <td class="sv la">26.27 ± 5.93 / 61.44 ± 3.01</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.51 ± 1.53 / 38.94 ± 1.40</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>TurkuNLP/bert-base-finnish-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,701 ± 2,104 / 5,450 ± 1,778</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">63.53 ± 1.11 / 67.45 ± 0.99</td> <!-- DaNE -->
   <td class="da sent">27.71 ± 1.03 / 50.39 ± 0.86</td> <!-- AngryTweets -->
   <td class="da la">3.07 ± 2.03 / 47.90 ± 2.80</td> <!-- ScaLA-da -->
   <td class="da qa">35.91 ± 1.72 / 39.87 ± 1.92</td> <!-- ScandiQA-da -->
   <td class="no ner">69.29 ± 1.52 / 72.21 ± 1.47</td> <!-- NorNE-nb -->
   <td class="no ner">59.21 ± 1.85 / 63.35 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">19.30 ± 2.52 / 37.75 ± 2.45</td> <!-- NoReC -->
   <td class="no la">1.11 ± 2.51 / 44.42 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">2.67 ± 1.70 / 44.34 ± 4.55</td> <!-- ScaLA-nn -->
   <td class="no qa">37.41 ± 2.26 / 41.71 ± 2.28</td> <!-- ScandiQA-no -->
   <td class="sv ner">58.37 ± 1.26 / 63.05 ± 1.21</td> <!-- SUC3 -->
   <td class="sv sent">57.64 ± 2.01 / 55.06 ± 2.50</td> <!-- SweReC -->
   <td class="sv la">2.89 ± 1.97 / 45.55 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.84 ± 0.79 / 41.03 ± 0.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,043 ± 2,590 / 4,268 ± 1,377</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">70.08 ± 0.97 / 72.61 ± 1.16</td> <!-- DaNE -->
   <td class="da sent">27.60 ± 1.70 / 50.58 ± 1.22</td> <!-- AngryTweets -->
   <td class="da la">2.49 ± 2.08 / 50.07 ± 0.99</td> <!-- ScaLA-da -->
   <td class="da qa">34.29 ± 2.52 / 38.13 ± 2.47</td> <!-- ScandiQA-da -->
   <td class="no ner">69.37 ± 1.08 / 71.81 ± 1.01</td> <!-- NorNE-nb -->
   <td class="no ner">65.09 ± 1.93 / 68.15 ± 1.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.74 ± 2.05 / 37.47 ± 1.58</td> <!-- NoReC -->
   <td class="no la">1.67 ± 1.69 / 45.73 ± 3.55</td> <!-- ScaLA-nb -->
   <td class="no la">0.84 ± 1.75 / 44.24 ± 3.91</td> <!-- ScaLA-nn -->
   <td class="no qa">36.07 ± 1.27 / 40.14 ± 1.27</td> <!-- ScandiQA-no -->
   <td class="sv ner">59.86 ± 1.23 / 64.27 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">53.82 ± 3.41 / 53.50 ± 2.77</td> <!-- SweReC -->
   <td class="sv la">0.69 ± 1.21 / 47.36 ± 2.87</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.25 ± 1.16 / 41.29 ± 1.06</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.80 ± 1.73 / 72.68 ± 1.70</td> <!-- DaNE -->
   <td class="da sent">29.27 ± 3.00 / 51.00 ± 3.94</td> <!-- AngryTweets -->
   <td class="da la">1.18 ± 1.48 / 40.35 ± 4.04</td> <!-- ScaLA-da -->
   <td class="da qa">36.17 ± 2.23 / 39.52 ± 2.16</td> <!-- ScandiQA-da -->
   <td class="no ner">73.25 ± 2.35 / 75.97 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">63.94 ± 2.11 / 67.89 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">17.25 ± 4.57 / 34.91 ± 3.73</td> <!-- NoReC -->
   <td class="no la">2.95 ± 1.93 / 44.03 ± 4.72</td> <!-- ScaLA-nb -->
   <td class="no la">1.30 ± 1.85 / 41.87 ± 4.06</td> <!-- ScaLA-nn -->
   <td class="no qa">35.72 ± 2.06 / 39.67 ± 2.05</td> <!-- ScandiQA-no -->
   <td class="sv ner">60.30 ± 1.25 / 65.03 ± 1.31</td> <!-- SUC3 -->
   <td class="sv sent">53.74 ± 3.02 / 52.22 ± 1.67</td> <!-- SweReC -->
   <td class="sv la">2.67 ± 1.29 / 38.57 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.26 ± 2.11 / 44.37 ± 2.12</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">117</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">62.44 ± 0.69 / 66.04 ± 1.00</td> <!-- DaNE -->
   <td class="da sent">29.75 ± 1.68 / 52.53 ± 1.20</td> <!-- AngryTweets -->
   <td class="da la">2.21 ± 1.34 / 48.56 ± 2.17</td> <!-- ScaLA-da -->
   <td class="da qa">32.73 ± 2.76 / 36.27 ± 2.82</td> <!-- ScandiQA-da -->
   <td class="no ner">65.28 ± 1.79 / 67.30 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">59.94 ± 2.59 / 63.58 ± 2.49</td> <!-- NorNE-nn -->
   <td class="no sent">19.12 ± 4.18 / 37.47 ± 3.42</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.67 / 45.13 ± 3.10</td> <!-- ScaLA-nb -->
   <td class="no la">1.48 ± 1.68 / 46.67 ± 2.59</td> <!-- ScaLA-nn -->
   <td class="no qa">30.40 ± 1.99 / 34.61 ± 2.01</td> <!-- ScandiQA-no -->
   <td class="sv ner">53.74 ± 1.03 / 57.82 ± 1.19</td> <!-- SUC3 -->
   <td class="sv sent">53.95 ± 2.73 / 52.13 ± 1.40</td> <!-- SweReC -->
   <td class="sv la">1.16 ± 1.80 / 48.26 ± 1.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.41 ± 1.91 / 35.63 ± 1.84</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>DeepPavlov/rubert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,785 ± 2,658 / 3,983 ± 1,289</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.36 ± 1.07 / 71.10 ± 1.46</td> <!-- DaNE -->
   <td class="da sent">26.41 ± 1.45 / 49.24 ± 1.23</td> <!-- AngryTweets -->
   <td class="da la">3.84 ± 2.52 / 43.36 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da qa">36.03 ± 2.48 / 39.69 ± 2.52</td> <!-- ScandiQA-da -->
   <td class="no ner">72.02 ± 1.41 / 74.82 ± 1.33</td> <!-- NorNE-nb -->
   <td class="no ner">68.79 ± 2.23 / 72.52 ± 1.87</td> <!-- NorNE-nn -->
   <td class="no sent">21.34 ± 2.21 / 38.12 ± 2.10</td> <!-- NoReC -->
   <td class="no la">5.21 ± 3.54 / 45.00 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">3.00 ± 2.36 / 43.58 ± 2.74</td> <!-- ScaLA-nn -->
   <td class="no qa">38.36 ± 1.72 / 42.55 ± 1.75</td> <!-- ScandiQA-no -->
   <td class="sv ner">58.18 ± 1.69 / 63.07 ± 1.74</td> <!-- SUC3 -->
   <td class="sv sent">54.68 ± 2.31 / 52.79 ± 1.54</td> <!-- SweReC -->
   <td class="sv la">6.15 ± 2.42 / 49.78 ± 2.07</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.53 ± 2.91 / 41.90 ± 2.91</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>asafaya/bert-base-arabic</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,347 ± 2,191 / 5,125 ± 1,672</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">37.71 ± 1.50 / 34.61 ± 1.57</td> <!-- DaNE -->
   <td class="da sent">25.13 ± 2.41 / 46.58 ± 3.06</td> <!-- AngryTweets -->
   <td class="da la">1.09 ± 0.72 / 44.63 ± 3.67</td> <!-- ScaLA-da -->
   <td class="da qa">27.63 ± 2.65 / 33.00 ± 2.39</td> <!-- ScandiQA-da -->
   <td class="no ner">31.35 ± 1.94 / 31.77 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">33.56 ± 2.03 / 34.70 ± 2.07</td> <!-- NorNE-nn -->
   <td class="no sent">17.55 ± 1.80 / 36.12 ± 1.25</td> <!-- NoReC -->
   <td class="no la">2.29 ± 2.47 / 46.04 ± 4.40</td> <!-- ScaLA-nb -->
   <td class="no la">0.71 ± 1.94 / 45.99 ± 3.28</td> <!-- ScaLA-nn -->
   <td class="no qa">28.41 ± 2.95 / 33.32 ± 2.81</td> <!-- ScandiQA-no -->
   <td class="sv ner">10.71 ± 3.93 / 11.74 ± 4.22</td> <!-- SUC3 -->
   <td class="sv sent">58.56 ± 1.57 / 55.18 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">2.67 ± 1.55 / 43.90 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.67 ± 3.72 / 34.83 ± 3.54</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ViktorAlm/electra-base-norwegian-uncased-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">30</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,725 ± 2,688 / 3,986 ± 1,295</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">53.55 ± 1.38 / 49.43 ± 1.44</td> <!-- DaNE -->
   <td class="da sent">36.99 ± 2.39 / 56.20 ± 3.67</td> <!-- AngryTweets -->
   <td class="da la">43.10 ± 2.55 / 69.95 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da qa">24.43 ± 2.03 / 28.85 ± 2.29</td> <!-- ScandiQA-da -->
   <td class="no ner">51.80 ± 3.02 / 52.80 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">50.62 ± 2.44 / 53.51 ± 2.16</td> <!-- NorNE-nn -->
   <td class="no sent">56.63 ± 1.15 / 69.80 ± 1.39</td> <!-- NoReC -->
   <td class="no la">67.52 ± 1.79 / 82.70 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">57.16 ± 1.35 / 77.82 ± 0.80</td> <!-- ScaLA-nn -->
   <td class="no qa">26.91 ± 2.28 / 31.83 ± 2.56</td> <!-- ScandiQA-no -->
   <td class="sv ner">39.52 ± 1.94 / 41.97 ± 2.07</td> <!-- SUC3 -->
   <td class="sv sent">64.80 ± 1.64 / 60.10 ± 2.85</td> <!-- SweReC -->
   <td class="sv la">35.28 ± 2.25 / 67.15 ± 1.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">22.18 ± 1.35 / 26.76 ± 1.47</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>af-ai-center/bert-base-swedish-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,694 ± 2,680 / 3,972 ± 1,283</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.72 ± 1.30 / 60.11 ± 1.42</td> <!-- DaNE -->
   <td class="da sent">25.99 ± 1.39 / 48.69 ± 1.33</td> <!-- AngryTweets -->
   <td class="da la">2.45 ± 1.81 / 49.39 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">32.39 ± 1.05 / 37.60 ± 1.00</td> <!-- ScandiQA-da -->
   <td class="no ner">59.57 ± 1.06 / 63.17 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">54.26 ± 0.78 / 58.05 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">24.48 ± 1.48 / 40.79 ± 1.44</td> <!-- NoReC -->
   <td class="no la">5.59 ± 2.02 / 51.01 ± 1.70</td> <!-- ScaLA-nb -->
   <td class="no la">5.09 ± 3.84 / 50.72 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no qa">31.05 ± 1.49 / 36.49 ± 1.50</td> <!-- ScandiQA-no -->
   <td class="sv ner">56.82 ± 1.20 / 61.30 ± 1.19</td> <!-- SUC3 -->
   <td class="sv sent">62.00 ± 1.18 / 58.68 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">27.76 ± 2.17 / 63.61 ± 1.18</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.87 ± 1.45 / 41.08 ± 1.27</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>birgermoell/roberta-swedish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,465 ± 2,846 / 3,624 ± 1,192</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">74.17 ± 0.48 / 76.71 ± 0.57</td> <!-- DaNE -->
   <td class="da sent">35.54 ± 0.87 / 56.97 ± 0.53</td> <!-- AngryTweets -->
   <td class="da la">20.59 ± 9.60 / 58.61 ± 4.99</td> <!-- ScaLA-da -->
   <td class="da qa">32.76 ± 1.81 / 36.38 ± 1.84</td> <!-- ScandiQA-da -->
   <td class="no ner">74.94 ± 1.46 / 77.32 ± 1.26</td> <!-- NorNE-nb -->
   <td class="no ner">70.20 ± 1.20 / 73.85 ± 0.93</td> <!-- NorNE-nn -->
   <td class="no sent">36.55 ± 1.80 / 51.42 ± 2.73</td> <!-- NoReC -->
   <td class="no la">31.14 ± 6.24 / 64.37 ± 3.09</td> <!-- ScaLA-nb -->
   <td class="no la">19.73 ± 5.69 / 58.64 ± 3.32</td> <!-- ScaLA-nn -->
   <td class="no qa">31.12 ± 2.48 / 35.76 ± 2.31</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.81 ± 1.09 / 74.71 ± 1.24</td> <!-- SUC3 -->
   <td class="sv sent">72.02 ± 1.44 / 70.27 ± 2.97</td> <!-- SweReC -->
   <td class="sv la">62.18 ± 1.52 / 79.87 ± 1.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.06 ± 1.58 / 41.48 ± 1.57</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/bert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,805 ± 2,563 / 4,214 ± 1,360</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">72.66 ± 0.84 / 75.38 ± 1.07</td> <!-- DaNE -->
   <td class="da sent">26.78 ± 1.90 / 48.51 ± 2.47</td> <!-- AngryTweets -->
   <td class="da la">18.84 ± 5.73 / 58.47 ± 2.90</td> <!-- ScaLA-da -->
   <td class="da qa">32.47 ± 1.41 / 36.72 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">76.61 ± 1.24 / 79.97 ± 1.07</td> <!-- NorNE-nb -->
   <td class="no ner">68.12 ± 1.10 / 72.17 ± 0.85</td> <!-- NorNE-nn -->
   <td class="no sent">29.81 ± 2.15 / 43.25 ± 1.57</td> <!-- NoReC -->
   <td class="no la">23.05 ± 3.40 / 58.49 ± 2.66</td> <!-- ScaLA-nb -->
   <td class="no la">17.52 ± 3.51 / 57.06 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no qa">34.59 ± 1.69 / 39.45 ± 1.65</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.19 ± 1.57 / 80.03 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">73.13 ± 0.96 / 71.48 ± 2.57</td> <!-- SweReC -->
   <td class="sv la">72.31 ± 1.20 / 85.67 ± 0.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">41.02 ± 1.08 / 45.89 ± 1.20</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/roberta-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">126</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,231 ± 2,310 / 4,879 ± 1,564</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">71.05 ± 0.95 / 73.74 ± 0.78</td> <!-- DaNE -->
   <td class="da sent">29.75 ± 1.78 / 51.42 ± 2.00</td> <!-- AngryTweets -->
   <td class="da la">11.90 ± 4.80 / 52.36 ± 4.24</td> <!-- ScaLA-da -->
   <td class="da qa">25.57 ± 3.29 / 29.98 ± 3.22</td> <!-- ScandiQA-da -->
   <td class="no ner">75.79 ± 1.35 / 79.24 ± 1.34</td> <!-- NorNE-nb -->
   <td class="no ner">69.83 ± 1.22 / 73.74 ± 1.08</td> <!-- NorNE-nn -->
   <td class="no sent">24.86 ± 1.57 / 39.65 ± 1.46</td> <!-- NoReC -->
   <td class="no la">17.30 ± 3.31 / 57.52 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">9.79 ± 4.47 / 52.07 ± 3.65</td> <!-- ScaLA-nn -->
   <td class="no qa">26.88 ± 2.90 / 32.07 ± 2.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.88 ± 1.12 / 75.78 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">66.73 ± 0.95 / 63.29 ± 2.21</td> <!-- SweReC -->
   <td class="sv la">59.64 ± 1.57 / 78.93 ± 0.73</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.13 ± 2.25 / 35.50 ± 2.07</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KBLab/electra-small-swedish-cased-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">16</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,921 ± 3,328 / 4,833 ± 1,594</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">63.91 ± 1.90 / 66.13 ± 2.21</td> <!-- DaNE -->
   <td class="da sent">21.48 ± 1.76 / 39.08 ± 2.35</td> <!-- AngryTweets -->
   <td class="da la">26.99 ± 2.37 / 62.28 ± 0.96</td> <!-- ScaLA-da -->
   <td class="da qa">25.44 ± 2.12 / 31.39 ± 1.96</td> <!-- ScandiQA-da -->
   <td class="no ner">62.41 ± 3.57 / 66.04 ± 3.77</td> <!-- NorNE-nb -->
   <td class="no ner">60.89 ± 1.33 / 65.43 ± 1.33</td> <!-- NorNE-nn -->
   <td class="no sent">24.46 ± 1.06 / 40.08 ± 0.71</td> <!-- NoReC -->
   <td class="no la">23.54 ± 1.78 / 60.01 ± 1.30</td> <!-- ScaLA-nb -->
   <td class="no la">15.53 ± 3.71 / 55.47 ± 3.76</td> <!-- ScaLA-nn -->
   <td class="no qa">19.77 ± 2.55 / 27.11 ± 2.32</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.57 ± 2.40 / 66.70 ± 2.34</td> <!-- SUC3 -->
   <td class="sv sent">62.59 ± 1.26 / 56.06 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">67.85 ± 0.55 / 83.34 ± 0.33</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.68 ± 3.14 / 36.34 ± 2.71</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.27 ± 1.09 / 85.41 ± 0.91</td> <!-- DaNE -->
   <td class="da sent">52.08 ± 1.06 / 67.98 ± 0.77</td> <!-- AngryTweets -->
   <td class="da la">67.99 ± 2.28 / 83.02 ± 1.44</td> <!-- ScaLA-da -->
   <td class="da qa">41.08 ± 1.35 / 45.20 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="no ner">89.66 ± 0.60 / 92.24 ± 0.44</td> <!-- NorNE-nb -->
   <td class="no ner">84.23 ± 0.85 / 87.58 ± 0.68</td> <!-- NorNE-nn -->
   <td class="no sent">59.98 ± 1.33 / 71.70 ± 1.69</td> <!-- NoReC -->
   <td class="no la">70.18 ± 1.41 / 83.83 ± 0.91</td> <!-- ScaLA-nb -->
   <td class="no la">70.81 ± 1.50 / 84.45 ± 0.95</td> <!-- ScaLA-nn -->
   <td class="no qa">40.58 ± 1.82 / 45.32 ± 1.67</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.04 ± 1.75 / 80.02 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 1.60 / 73.41 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">71.92 ± 1.07 / 85.01 ± 0.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.80 ± 1.29 / 47.62 ± 1.27</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>pere/nb-roberta-base-scandinavian-long</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,086 ± 3,279 / 2,694 ± 892</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.90 ± 0.74 / 79.53 ± 0.89</td> <!-- DaNE -->
   <td class="da sent">40.71 ± 1.48 / 59.29 ± 1.86</td> <!-- AngryTweets -->
   <td class="da la">52.05 ± 9.20 / 74.77 ± 4.76</td> <!-- ScaLA-da -->
   <td class="da qa">37.07 ± 2.94 / 40.36 ± 2.90</td> <!-- ScandiQA-da -->
   <td class="no ner">82.51 ± 1.34 / 86.03 ± 1.30</td> <!-- NorNE-nb -->
   <td class="no ner">78.79 ± 1.82 / 82.69 ± 1.79</td> <!-- NorNE-nn -->
   <td class="no sent">48.17 ± 1.52 / 62.07 ± 2.22</td> <!-- NoReC -->
   <td class="no la">64.02 ± 2.42 / 80.90 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">53.43 ± 10.63 / 75.89 ± 5.55</td> <!-- ScaLA-nn -->
   <td class="no qa">35.29 ± 1.16 / 39.35 ± 1.27</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.97 ± 1.70 / 70.83 ± 1.59</td> <!-- SUC3 -->
   <td class="sv sent">67.99 ± 1.13 / 65.00 ± 3.31</td> <!-- SweReC -->
   <td class="sv la">60.13 ± 0.96 / 79.47 ± 0.78</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.25 ± 1.40 / 41.49 ± 1.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>NbAiLab/nb-roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,051 ± 3,289 / 2,704 ± 897</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.90 ± 0.74 / 79.53 ± 0.89</td> <!-- DaNE -->
   <td class="da sent">40.71 ± 1.48 / 59.29 ± 1.86</td> <!-- AngryTweets -->
   <td class="da la">52.05 ± 9.20 / 74.77 ± 4.76</td> <!-- ScaLA-da -->
   <td class="da qa">37.07 ± 2.94 / 40.36 ± 2.90</td> <!-- ScandiQA-da -->
   <td class="no ner">82.51 ± 1.34 / 86.03 ± 1.30</td> <!-- NorNE-nb -->
   <td class="no ner">78.79 ± 1.82 / 82.69 ± 1.79</td> <!-- NorNE-nn -->
   <td class="no sent">48.17 ± 1.52 / 62.07 ± 2.22</td> <!-- NoReC -->
   <td class="no la">64.02 ± 2.42 / 80.90 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">53.43 ± 10.63 / 75.89 ± 5.55</td> <!-- ScaLA-nn -->
   <td class="no qa">35.29 ± 1.16 / 39.35 ± 1.27</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.97 ± 1.70 / 70.83 ± 1.59</td> <!-- SUC3 -->
   <td class="sv sent">67.99 ± 1.13 / 65.00 ± 3.31</td> <!-- SweReC -->
   <td class="sv la">60.13 ± 0.96 / 79.47 ± 0.78</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.25 ± 1.40 / 41.49 ± 1.31</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.48 ± 0.94 / 84.71 ± 0.89</td> <!-- DaNE -->
   <td class="da sent">51.70 ± 1.98 / 67.54 ± 1.47</td> <!-- AngryTweets -->
   <td class="da la">62.03 ± 11.56 / 80.01 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">41.67 ± 1.47 / 45.58 ± 1.35</td> <!-- ScandiQA-da -->
   <td class="no ner">89.67 ± 0.54 / 92.09 ± 0.51</td> <!-- NorNE-nb -->
   <td class="no ner">83.35 ± 2.01 / 86.85 ± 1.94</td> <!-- NorNE-nn -->
   <td class="no sent">59.84 ± 1.40 / 72.11 ± 1.25</td> <!-- NoReC -->
   <td class="no la">73.33 ± 2.17 / 85.89 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">71.06 ± 1.62 / 84.78 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">40.93 ± 1.69 / 45.44 ± 1.69</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.80 ± 1.53 / 79.90 ± 1.41</td> <!-- SUC3 -->
   <td class="sv sent">76.20 ± 1.16 / 74.01 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">73.62 ± 1.17 / 86.19 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.66 ± 1.09 / 45.33 ± 0.88</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.39 ± 1.08 / 82.06 ± 0.82</td> <!-- DaNE -->
   <td class="da sent">31.86 ± 8.76 / 47.51 ± 8.94</td> <!-- AngryTweets -->
   <td class="da la">52.95 ± 11.68 / 73.96 ± 8.89</td> <!-- ScaLA-da -->
   <td class="da qa">43.23 ± 2.84 / 47.86 ± 2.90</td> <!-- ScandiQA-da -->
   <td class="no ner">87.51 ± 1.20 / 89.99 ± 1.32</td> <!-- NorNE-nb -->
   <td class="no ner">74.97 ± 3.56 / 78.60 ± 3.17</td> <!-- NorNE-nn -->
   <td class="no sent">17.93 ± 14.48 / 34.24 ± 10.14</td> <!-- NoReC -->
   <td class="no la">43.46 ± 17.47 / 66.52 ± 12.26</td> <!-- ScaLA-nb -->
   <td class="no la">10.97 ± 10.84 / 43.47 ± 9.81</td> <!-- ScaLA-nn -->
   <td class="no qa">42.98 ± 3.29 / 48.67 ± 3.06</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.66 ± 6.41 / 68.39 ± 7.26</td> <!-- SUC3 -->
   <td class="sv sent">73.43 ± 0.91 / 61.29 ± 1.81</td> <!-- SweReC -->
   <td class="sv la">45.09 ± 15.90 / 68.48 ± 11.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.18 ± 2.75 / 50.15 ± 2.65</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">75.58 ± 1.26 / 78.43 ± 1.14</td> <!-- DaNE -->
   <td class="da sent">47.20 ± 1.34 / 64.51 ± 1.21</td> <!-- AngryTweets -->
   <td class="da la">40.52 ± 7.38 / 67.99 ± 3.84</td> <!-- ScaLA-da -->
   <td class="da qa">13.97 ± 5.69 / 15.40 ± 5.97</td> <!-- ScandiQA-da -->
   <td class="no ner">81.19 ± 1.37 / 84.11 ± 1.13</td> <!-- NorNE-nb -->
   <td class="no ner">73.93 ± 1.46 / 77.82 ± 1.28</td> <!-- NorNE-nn -->
   <td class="no sent">39.63 ± 1.06 / 49.23 ± 2.13</td> <!-- NoReC -->
   <td class="no la">45.75 ± 3.27 / 71.33 ± 1.67</td> <!-- ScaLA-nb -->
   <td class="no la">33.74 ± 2.91 / 63.89 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">14.79 ± 4.63 / 16.74 ± 5.09</td> <!-- ScandiQA-no -->
   <td class="sv ner">65.04 ± 1.33 / 71.34 ± 0.91</td> <!-- SUC3 -->
   <td class="sv sent">70.91 ± 1.23 / 67.12 ± 3.79</td> <!-- SweReC -->
   <td class="sv la">53.52 ± 1.22 / 76.15 ± 0.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">21.94 ± 5.48 / 24.63 ± 5.75</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">81.82 ± 0.83 / 84.01 ± 0.75</td> <!-- DaNE -->
   <td class="da sent">52.86 ± 1.08 / 68.19 ± 1.02</td> <!-- AngryTweets -->
   <td class="da la">75.20 ± 1.73 / 86.99 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">45.61 ± 1.39 / 50.34 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="no ner">84.15 ± 0.59 / 86.82 ± 0.53</td> <!-- NorNE-nb -->
   <td class="no ner">76.65 ± 1.46 / 79.91 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">47.84 ± 2.44 / 60.67 ± 3.47</td> <!-- NoReC -->
   <td class="no la">51.99 ± 11.45 / 72.87 ± 8.55</td> <!-- ScaLA-nb -->
   <td class="no la">30.57 ± 8.63 / 62.90 ± 7.32</td> <!-- ScaLA-nn -->
   <td class="no qa">45.44 ± 1.40 / 50.58 ± 1.26</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.15 ± 0.85 / 72.33 ± 0.82</td> <!-- SUC3 -->
   <td class="sv sent">67.77 ± 1.19 / 62.98 ± 2.57</td> <!-- SweReC -->
   <td class="sv la">33.79 ± 7.61 / 64.01 ± 6.84</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.61 ± 1.14 / 44.43 ± 1.12</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">70.30 ± 0.78 / 74.21 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">39.65 ± 1.31 / 59.23 ± 0.94</td> <!-- AngryTweets -->
   <td class="da la">37.67 ± 7.20 / 65.47 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da qa">24.84 ± 4.84 / 30.58 ± 4.46</td> <!-- ScandiQA-da -->
   <td class="no ner">62.62 ± 0.66 / 65.95 ± 0.72</td> <!-- NorNE-nb -->
   <td class="no ner">51.50 ± 1.21 / 55.29 ± 1.26</td> <!-- NorNE-nn -->
   <td class="no sent">33.31 ± 2.87 / 48.75 ± 3.38</td> <!-- NoReC -->
   <td class="no la">20.34 ± 4.81 / 58.57 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">8.07 ± 2.44 / 53.43 ± 1.32</td> <!-- ScaLA-nn -->
   <td class="no qa">26.98 ± 3.94 / 33.32 ± 3.73</td> <!-- ScandiQA-no -->
   <td class="sv ner">39.98 ± 1.42 / 42.99 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">55.49 ± 1.28 / 55.99 ± 2.15</td> <!-- SweReC -->
   <td class="sv la">4.69 ± 2.28 / 51.01 ± 1.58</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.96 ± 4.02 / 27.42 ± 3.83</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>chcaa/dfm-encoder-small-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,002 ± 129 / 3,832 ± 1,242</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">74.80 ± 1.18 / 78.92 ± 1.04</td> <!-- DaNE -->
   <td class="da sent">29.39 ± 2.55 / 45.17 ± 3.06</td> <!-- AngryTweets -->
   <td class="da la">59.38 ± 1.70 / 78.64 ± 1.11</td> <!-- ScaLA-da -->
   <td class="da qa">1.14 ± 1.66 / 1.93 ± 2.63</td> <!-- ScandiQA-da -->
   <td class="no ner">72.09 ± 1.61 / 75.77 ± 1.02</td> <!-- NorNE-nb -->
   <td class="no ner">63.25 ± 2.26 / 67.32 ± 2.49</td> <!-- NorNE-nn -->
   <td class="no sent">10.30 ± 8.55 / 28.38 ± 5.82</td> <!-- NoReC -->
   <td class="no la">39.06 ± 1.92 / 67.45 ± 1.02</td> <!-- ScaLA-nb -->
   <td class="no la">21.66 ± 5.92 / 56.29 ± 6.92</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-no -->
   <td class="sv ner">38.61 ± 8.85 / 40.83 ± 9.37</td> <!-- SUC3 -->
   <td class="sv sent">59.58 ± 1.27 / 54.36 ± 0.49</td> <!-- SweReC -->
   <td class="sv la">23.36 ± 5.27 / 57.75 ± 4.71</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.02 ± 0.03 / 0.08 ± 0.15</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">72.50 ± 1.28 / 75.49 ± 1.05</td> <!-- DaNE -->
   <td class="da sent">39.91 ± 1.78 / 58.47 ± 2.16</td> <!-- AngryTweets -->
   <td class="da la">51.01 ± 10.50 / 74.54 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da qa">36.89 ± 2.71 / 40.91 ± 2.53</td> <!-- ScandiQA-da -->
   <td class="no ner">65.08 ± 1.07 / 68.66 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">57.87 ± 2.08 / 61.77 ± 2.03</td> <!-- NorNE-nn -->
   <td class="no sent">36.56 ± 1.53 / 51.54 ± 2.45</td> <!-- NoReC -->
   <td class="no la">31.23 ± 6.86 / 63.55 ± 5.48</td> <!-- ScaLA-nb -->
   <td class="no la">5.40 ± 4.63 / 44.64 ± 6.37</td> <!-- ScaLA-nn -->
   <td class="no qa">35.93 ± 1.89 / 40.56 ± 1.70</td> <!-- ScandiQA-no -->
   <td class="sv ner">46.05 ± 2.11 / 49.62 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">58.70 ± 2.54 / 58.15 ± 3.35</td> <!-- SweReC -->
   <td class="sv la">2.23 ± 2.12 / 46.43 ± 4.85</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.96 ± 1.17 / 40.86 ± 1.03</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.69 ± 0.85 / 85.08 ± 0.77</td> <!-- DaNE -->
   <td class="da sent">51.42 ± 2.30 / 67.07 ± 1.97</td> <!-- AngryTweets -->
   <td class="da la">76.11 ± 1.17 / 87.41 ± 0.67</td> <!-- ScaLA-da -->
   <td class="da qa">54.45 ± 1.65 / 59.52 ± 1.45</td> <!-- ScandiQA-da -->
   <td class="no ner">84.60 ± 1.44 / 88.66 ± 1.23</td> <!-- NorNE-nb -->
   <td class="no ner">80.07 ± 2.11 / 84.59 ± 1.98</td> <!-- NorNE-nn -->
   <td class="no sent">55.59 ± 10.43 / 67.82 ± 9.45</td> <!-- NoReC -->
   <td class="no la">71.43 ± 1.67 / 84.61 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">53.30 ± 13.11 / 74.52 ± 7.96</td> <!-- ScaLA-nn -->
   <td class="no qa">52.46 ± 4.57 / 57.66 ± 4.45</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.89 ± 2.46 / 74.18 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">75.11 ± 1.19 / 74.74 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">64.11 ± 3.27 / 81.63 ± 1.66</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.98 ± 1.42 / 59.70 ± 1.27</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">82.36 ± 0.74 / 84.38 ± 0.63</td> <!-- DaNE -->
   <td class="da sent">49.18 ± 1.55 / 65.94 ± 1.28</td> <!-- AngryTweets -->
   <td class="da la">65.45 ± 1.97 / 81.55 ± 1.33</td> <!-- ScaLA-da -->
   <td class="da qa">39.33 ± 2.44 / 43.67 ± 2.73</td> <!-- ScandiQA-da -->
   <td class="no ner">88.03 ± 0.77 / 90.65 ± 0.66</td> <!-- NorNE-nb -->
   <td class="no ner">81.01 ± 1.95 / 84.88 ± 1.55</td> <!-- NorNE-nn -->
   <td class="no sent">52.44 ± 2.90 / 62.48 ± 4.62</td> <!-- NoReC -->
   <td class="no la">68.77 ± 2.01 / 83.10 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">65.40 ± 2.43 / 81.72 ± 1.68</td> <!-- ScaLA-nn -->
   <td class="no qa">39.93 ± 2.95 / 44.71 ± 2.99</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.45 ± 1.57 / 78.58 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">73.41 ± 0.98 / 68.72 ± 3.80</td> <!-- SweReC -->
   <td class="sv la">71.14 ± 1.62 / 84.55 ± 0.97</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.76 ± 3.98 / 48.30 ± 3.92</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>sileod/mdeberta-v3-base-tasksource-nli</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,346 ± 1,621 / 2,296 ± 753</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">84.82 ± 0.73 / 86.85 ± 0.83</td> <!-- DaNE -->
   <td class="da sent">50.98 ± 1.25 / 67.18 ± 0.86</td> <!-- AngryTweets -->
   <td class="da la">57.33 ± 11.34 / 77.46 ± 5.70</td> <!-- ScaLA-da -->
   <td class="da qa">49.56 ± 0.60 / 55.17 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">89.11 ± 1.05 / 91.70 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">83.50 ± 0.95 / 86.79 ± 0.87</td> <!-- NorNE-nn -->
   <td class="no sent">52.87 ± 2.07 / 65.06 ± 2.55</td> <!-- NoReC -->
   <td class="no la">67.09 ± 1.55 / 82.49 ± 0.90</td> <!-- ScaLA-nb -->
   <td class="no la">58.36 ± 1.37 / 78.55 ± 0.87</td> <!-- ScaLA-nn -->
   <td class="no qa">50.64 ± 0.92 / 56.68 ± 0.86</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.72 ± 1.82 / 78.68 ± 1.76</td> <!-- SUC3 -->
   <td class="sv sent">75.70 ± 0.93 / 73.09 ± 2.62</td> <!-- SweReC -->
   <td class="sv la">68.65 ± 1.96 / 83.70 ± 1.16</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.63 ± 1.49 / 56.54 ± 1.44</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">73.56 ± 1.19 / 77.11 ± 1.24</td> <!-- DaNE -->
   <td class="da sent">44.62 ± 1.38 / 62.33 ± 1.20</td> <!-- AngryTweets -->
   <td class="da la">47.47 ± 8.03 / 70.55 ± 4.26</td> <!-- ScaLA-da -->
   <td class="da qa">32.06 ± 2.43 / 36.66 ± 2.26</td> <!-- ScandiQA-da -->
   <td class="no ner">68.09 ± 0.91 / 71.69 ± 0.92</td> <!-- NorNE-nb -->
   <td class="no ner">56.64 ± 1.98 / 60.00 ± 1.99</td> <!-- NorNE-nn -->
   <td class="no sent">38.94 ± 2.59 / 53.58 ± 3.33</td> <!-- NoReC -->
   <td class="no la">30.32 ± 4.68 / 62.42 ± 3.11</td> <!-- ScaLA-nb -->
   <td class="no la">7.99 ± 3.34 / 53.24 ± 1.64</td> <!-- ScaLA-nn -->
   <td class="no qa">30.74 ± 2.61 / 36.49 ± 2.36</td> <!-- ScandiQA-no -->
   <td class="sv ner">45.04 ± 1.50 / 48.32 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">53.98 ± 2.05 / 52.94 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">3.33 ± 2.12 / 51.06 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.34 ± 1.32 / 37.02 ± 1.18</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">74.47 ± 1.23 / 76.67 ± 1.35</td> <!-- DaNE -->
   <td class="da sent">39.16 ± 1.75 / 58.91 ± 1.21</td> <!-- AngryTweets -->
   <td class="da la">2.16 ± 1.61 / 48.93 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">26.02 ± 1.69 / 29.29 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">84.17 ± 0.81 / 87.63 ± 0.64</td> <!-- NorNE-nb -->
   <td class="no ner">75.70 ± 2.31 / 80.19 ± 2.00</td> <!-- NorNE-nn -->
   <td class="no sent">49.92 ± 1.44 / 63.75 ± 1.45</td> <!-- NoReC -->
   <td class="no la">7.93 ± 4.24 / 50.87 ± 2.29</td> <!-- ScaLA-nb -->
   <td class="no la">5.06 ± 0.83 / 51.44 ± 1.05</td> <!-- ScaLA-nn -->
   <td class="no qa">24.07 ± 2.78 / 28.57 ± 2.45</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.96 ± 1.62 / 67.53 ± 1.66</td> <!-- SUC3 -->
   <td class="sv sent">59.27 ± 2.14 / 55.26 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.83 ± 2.01 / 49.25 ± 1.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">24.78 ± 1.23 / 28.67 ± 1.13</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">80.87 ± 1.21 / 82.67 ± 1.40</td> <!-- DaNE -->
   <td class="da sent">39.34 ± 2.85 / 58.37 ± 3.66</td> <!-- AngryTweets -->
   <td class="da la">50.90 ± 1.26 / 74.15 ± 0.81</td> <!-- ScaLA-da -->
   <td class="da qa">40.37 ± 2.04 / 44.31 ± 2.05</td> <!-- ScandiQA-da -->
   <td class="no ner">86.99 ± 0.87 / 90.02 ± 0.72</td> <!-- NorNE-nb -->
   <td class="no ner">83.03 ± 1.53 / 86.52 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 3.24 / 61.35 ± 5.46</td> <!-- NoReC -->
   <td class="no la">67.29 ± 2.13 / 82.23 ± 1.36</td> <!-- ScaLA-nb -->
   <td class="no la">56.67 ± 2.29 / 76.74 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no qa">44.74 ± 1.87 / 49.28 ± 1.93</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.68 ± 1.40 / 74.22 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">63.80 ± 1.56 / 57.65 ± 2.24</td> <!-- SweReC -->
   <td class="sv la">37.77 ± 5.16 / 65.87 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.97 ± 1.35 / 41.89 ± 1.35</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">84.22 ± 0.50 / 85.84 ± 0.54</td> <!-- DaNE -->
   <td class="da sent">43.94 ± 1.37 / 61.91 ± 0.97</td> <!-- AngryTweets -->
   <td class="da la">51.62 ± 15.51 / 73.99 ± 9.26</td> <!-- ScaLA-da -->
   <td class="da qa">47.92 ± 1.43 / 52.42 ± 1.47</td> <!-- ScandiQA-da -->
   <td class="no ner">89.79 ± 0.73 / 92.36 ± 0.55</td> <!-- NorNE-nb -->
   <td class="no ner">85.45 ± 1.21 / 88.49 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">59.73 ± 2.46 / 70.77 ± 3.26</td> <!-- NoReC -->
   <td class="no la">74.40 ± 2.03 / 86.34 ± 1.28</td> <!-- ScaLA-nb -->
   <td class="no la">68.85 ± 3.21 / 83.17 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">50.44 ± 2.26 / 54.91 ± 2.21</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.63 ± 0.98 / 78.21 ± 0.92</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 1.70 / 70.72 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">56.02 ± 2.92 / 77.31 ± 1.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.60 ± 1.30 / 51.06 ± 1.23</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">84.42 ± 1.36 / 86.37 ± 1.33</td> <!-- DaNE -->
   <td class="da sent">48.29 ± 2.60 / 64.67 ± 2.10</td> <!-- AngryTweets -->
   <td class="da la">71.55 ± 1.81 / 85.17 ± 1.13</td> <!-- ScaLA-da -->
   <td class="da qa">53.35 ± 2.03 / 57.87 ± 1.81</td> <!-- ScandiQA-da -->
   <td class="no ner">90.13 ± 1.02 / 93.12 ± 0.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.03 ± 0.65 / 89.39 ± 0.52</td> <!-- NorNE-nn -->
   <td class="no sent">64.62 ± 1.36 / 75.40 ± 0.97</td> <!-- NoReC -->
   <td class="no la">77.97 ± 3.04 / 88.19 ± 1.89</td> <!-- ScaLA-nb -->
   <td class="no la">76.30 ± 1.56 / 87.68 ± 0.86</td> <!-- ScaLA-nn -->
   <td class="no qa">55.22 ± 0.75 / 60.09 ± 0.94</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.76 ± 1.48 / 79.01 ± 1.13</td> <!-- SUC3 -->
   <td class="sv sent">75.32 ± 1.55 / 69.39 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">69.11 ± 1.50 / 84.32 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.78 ± 1.23 / 61.14 ± 1.33</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-oversampled-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,280 ± 2,775 / 4,077 ± 1,316</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.70 ± 0.77 / 83.72 ± 0.76</td> <!-- DaNE -->
   <td class="da sent">42.97 ± 1.86 / 61.51 ± 1.50</td> <!-- AngryTweets -->
   <td class="da la">57.15 ± 1.84 / 77.44 ± 1.26</td> <!-- ScaLA-da -->
   <td class="da qa">46.01 ± 0.93 / 50.26 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">88.16 ± 0.64 / 91.21 ± 0.62</td> <!-- NorNE-nb -->
   <td class="no ner">83.63 ± 1.07 / 87.06 ± 0.79</td> <!-- NorNE-nn -->
   <td class="no sent">57.37 ± 1.73 / 68.85 ± 1.96</td> <!-- NoReC -->
   <td class="no la">71.95 ± 1.39 / 85.06 ± 0.92</td> <!-- ScaLA-nb -->
   <td class="no la">67.31 ± 1.65 / 82.81 ± 1.09</td> <!-- ScaLA-nn -->
   <td class="no qa">48.46 ± 1.07 / 53.17 ± 1.10</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.37 ± 1.30 / 75.84 ± 1.32</td> <!-- SUC3 -->
   <td class="sv sent">70.42 ± 1.14 / 69.42 ± 2.29</td> <!-- SweReC -->
   <td class="sv la">46.84 ± 7.74 / 72.52 ± 3.94</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.47 ± 1.35 / 51.03 ± 1.36</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>ltg/norbert3-ncc-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,292 ± 2,830 / 4,092 ± 1,329</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.34 ± 0.65 / 83.31 ± 0.64</td> <!-- DaNE -->
   <td class="da sent">42.73 ± 1.14 / 61.44 ± 0.88</td> <!-- AngryTweets -->
   <td class="da la">53.31 ± 2.13 / 75.84 ± 1.15</td> <!-- ScaLA-da -->
   <td class="da qa">47.09 ± 0.86 / 51.59 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="no ner">88.83 ± 0.83 / 91.96 ± 0.78</td> <!-- NorNE-nb -->
   <td class="no ner">83.48 ± 1.21 / 86.89 ± 1.04</td> <!-- NorNE-nn -->
   <td class="no sent">55.28 ± 3.22 / 63.87 ± 5.64</td> <!-- NoReC -->
   <td class="no la">73.67 ± 0.92 / 86.51 ± 0.61</td> <!-- ScaLA-nb -->
   <td class="no la">67.67 ± 2.15 / 83.37 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no qa">47.63 ± 0.73 / 52.79 ± 0.75</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.06 ± 0.93 / 76.00 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">65.91 ± 1.26 / 60.30 ± 2.44</td> <!-- SweReC -->
   <td class="sv la">43.26 ± 3.91 / 70.54 ± 2.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.46 ± 1.25 / 49.86 ± 1.25</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">51</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,806 ± 3,522 / 2,161 ± 717</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">8.89 ± 5.50 / 27.03 ± 4.15</td> <!-- AngryTweets -->
   <td class="da la">1.06 ± 1.24 / 36.59 ± 2.04</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 2.60 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.52 ± 1.16 / 10.67 ± 0.61</td> <!-- NoReC -->
   <td class="no la">-2.32 ± 1.12 / 42.00 ± 3.60</td> <!-- ScaLA-nb -->
   <td class="no la">-1.20 ± 1.41 / 47.06 ± 1.29</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 2.83 ± 0.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.04 ± 0.07 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">7.85 ± 5.44 / 21.19 ± 3.34</td> <!-- SweReC -->
   <td class="sv la">-1.46 ± 1.28 / 44.00 ± 3.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.01 ± 0.02 / 2.77 ± 0.28</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">51</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">12,652 ± 3,468 / 2,133 ± 710</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">2.43 ± 1.16 / 2.98 ± 1.38</td> <!-- DaNE -->
   <td class="da sent">4.00 ± 3.32 / 28.01 ± 4.19</td> <!-- AngryTweets -->
   <td class="da la">-0.66 ± 1.22 / 36.05 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">0.04 ± 0.03 / 3.39 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="no ner">0.56 ± 0.51 / 0.60 ± 0.56</td> <!-- NorNE-nb -->
   <td class="no ner">0.10 ± 0.12 / 0.11 ± 0.13</td> <!-- NorNE-nn -->
   <td class="no sent">3.16 ± 2.37 / 18.63 ± 3.47</td> <!-- NoReC -->
   <td class="no la">-0.56 ± 1.06 / 33.61 ± 0.53</td> <!-- ScaLA-nb -->
   <td class="no la">0.30 ± 0.59 / 32.81 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.86 ± 1.36</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.04 ± 0.05 / 0.06 ± 0.07</td> <!-- SUC3 -->
   <td class="sv sent">26.67 ± 8.99 / 36.58 ± 6.98</td> <!-- SweReC -->
   <td class="sv la">0.41 ± 1.44 / 34.85 ± 1.95</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.02 ± 0.02 / 4.22 ± 0.81</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">64.84 ± 2.83 / 76.94 ± 2.14</td> <!-- DaNE -->
   <td class="da sent">51.80 ± 1.29 / 68.17 ± 0.86</td> <!-- AngryTweets -->
   <td class="da la">54.22 ± 1.49 / 74.13 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">56.55 ± 1.12 / 65.84 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">64.00 ± 2.37 / 74.92 ± 1.24</td> <!-- NorNE-nb -->
   <td class="no ner">68.02 ± 1.41 / 75.34 ± 1.15</td> <!-- NorNE-nn -->
   <td class="no sent">57.64 ± 1.33 / 71.34 ± 1.15</td> <!-- NoReC -->
   <td class="no la">49.93 ± 1.78 / 69.26 ± 1.76</td> <!-- ScaLA-nb -->
   <td class="no la">34.22 ± 2.98 / 57.61 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">57.12 ± 0.47 / 65.39 ± 0.39</td> <!-- ScandiQA-no -->
   <td class="sv ner">58.93 ± 3.29 / 71.43 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 1.54 / 76.51 ± 1.63</td> <!-- SweReC -->
   <td class="sv la">55.99 ± 2.64 / 75.08 ± 2.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.46 ± 0.90 / 64.95 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">68</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,601 ± 1,570 / 959 ± 318</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">28.95 ± 4.02 / 43.25 ± 2.71</td> <!-- AngryTweets -->
   <td class="da la">1.60 ± 1.21 / 35.43 ± 1.01</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 5.57 ± 1.24</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">29.39 ± 3.69 / 47.39 ± 2.43</td> <!-- NoReC -->
   <td class="no la">-0.52 ± 1.12 / 35.38 ± 1.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.28 ± 1.69 / 37.88 ± 1.41</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 4.61 ± 0.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">47.33 ± 10.50 / 45.15 ± 6.55</td> <!-- SweReC -->
   <td class="sv la">0.37 ± 1.21 / 36.07 ± 0.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.05 ± 0.06 / 5.33 ± 0.79</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">68</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,604 ± 1,556 / 954 ± 317</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.67 ± 0.55 / 0.85 ± 0.69</td> <!-- DaNE -->
   <td class="da sent">32.79 ± 4.28 / 44.69 ± 4.21</td> <!-- AngryTweets -->
   <td class="da la">0.50 ± 1.63 / 40.93 ± 4.58</td> <!-- ScaLA-da -->
   <td class="da qa">0.38 ± 0.20 / 10.71 ± 1.55</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.05 ± 0.08 / 0.04 ± 0.06</td> <!-- NorNE-nn -->
   <td class="no sent">28.15 ± 3.21 / 45.12 ± 3.88</td> <!-- NoReC -->
   <td class="no la">0.54 ± 0.84 / 33.46 ± 0.44</td> <!-- ScaLA-nb -->
   <td class="no la">-0.35 ± 0.49 / 32.82 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">0.19 ± 0.23 / 10.64 ± 1.02</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.39 ± 0.52 / 0.43 ± 0.58</td> <!-- SUC3 -->
   <td class="sv sent">72.01 ± 1.29 / 59.31 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.44 / 33.66 ± 0.66</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.63 ± 0.48 / 10.69 ± 0.78</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,360 ± 745 / 740 ± 237</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">33.36 ± 2.61 / 54.36 ± 2.24</td> <!-- AngryTweets -->
   <td class="da la">1.30 ± 1.73 / 48.33 ± 1.82</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 11.00 ± 0.79</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">26.26 ± 3.43 / 49.77 ± 2.31</td> <!-- NoReC -->
   <td class="no la">2.15 ± 0.93 / 43.97 ± 3.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.78 ± 1.54 / 38.67 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 11.40 ± 1.23</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">68.17 ± 1.99 / 70.95 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">-0.44 ± 1.45 / 47.68 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 10.36 ± 1.71</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,364 ± 750 / 742 ± 237</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">33.85 ± 2.25 / 51.67 ± 3.25</td> <!-- AngryTweets -->
   <td class="da la">2.94 ± 2.08 / 40.06 ± 4.44</td> <!-- ScaLA-da -->
   <td class="da qa">3.39 ± 1.23 / 19.07 ± 1.08</td> <!-- ScandiQA-da -->
   <td class="no ner">0.56 ± 0.69 / 0.59 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">0.03 ± 0.04 / 0.04 ± 0.05</td> <!-- NorNE-nn -->
   <td class="no sent">37.97 ± 1.76 / 48.60 ± 3.88</td> <!-- NoReC -->
   <td class="no la">2.47 ± 1.78 / 39.36 ± 4.71</td> <!-- ScaLA-nb -->
   <td class="no la">2.75 ± 1.43 / 39.54 ± 4.97</td> <!-- ScaLA-nn -->
   <td class="no qa">2.71 ± 1.03 / 18.30 ± 0.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">71.63 ± 1.33 / 70.68 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">2.58 ± 1.55 / 43.49 ± 3.40</td> <!-- ScaLA-sv -->
   <td class="sv qa">1.77 ± 0.94 / 18.87 ± 0.62</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">271</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,019 ± 179 / 299 ± 91</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.14 ± 0.27 / 0.11 ± 0.23</td> <!-- DaNE -->
   <td class="da sent">25.42 ± 3.00 / 35.63 ± 3.13</td> <!-- AngryTweets -->
   <td class="da la">7.99 ± 1.48 / 45.90 ± 3.29</td> <!-- ScaLA-da -->
   <td class="da qa">0.04 ± 0.04 / 13.06 ± 3.39</td> <!-- ScandiQA-da -->
   <td class="no ner">0.08 ± 0.09 / 0.09 ± 0.10</td> <!-- NorNE-nb -->
   <td class="no ner">1.01 ± 1.25 / 0.94 ± 1.17</td> <!-- NorNE-nn -->
   <td class="no sent">36.65 ± 4.87 / 56.98 ± 3.53</td> <!-- NoReC -->
   <td class="no la">3.64 ± 2.24 / 40.57 ± 4.78</td> <!-- ScaLA-nb -->
   <td class="no la">4.04 ± 2.38 / 41.29 ± 4.66</td> <!-- ScaLA-nn -->
   <td class="no qa">0.05 ± 0.07 / 13.00 ± 1.66</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.06 ± 0.11 / 0.07 ± 0.13</td> <!-- SUC3 -->
   <td class="sv sent">76.98 ± 1.90 / 77.77 ± 1.61</td> <!-- SweReC -->
   <td class="sv la">5.23 ± 2.64 / 40.89 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.03 ± 0.03 / 13.61 ± 2.27</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">271</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,017 ± 178 / 299 ± 90</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">3.50 ± 1.52 / 18.27 ± 0.39</td> <!-- AngryTweets -->
   <td class="da la">7.69 ± 1.45 / 48.43 ± 3.14</td> <!-- ScaLA-da -->
   <td class="da qa">0.21 ± 0.17 / 14.42 ± 2.64</td> <!-- ScandiQA-da -->
   <td class="no ner">0.27 ± 0.26 / 0.30 ± 0.28</td> <!-- NorNE-nb -->
   <td class="no ner">0.29 ± 0.48 / 0.34 ± 0.56</td> <!-- NorNE-nn -->
   <td class="no sent">31.03 ± 4.76 / 47.90 ± 5.40</td> <!-- NoReC -->
   <td class="no la">4.22 ± 2.43 / 38.13 ± 3.76</td> <!-- ScaLA-nb -->
   <td class="no la">5.65 ± 1.87 / 42.43 ± 3.71</td> <!-- ScaLA-nn -->
   <td class="no qa">0.34 ± 0.36 / 16.05 ± 1.03</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.13 ± 0.25 / 0.14 ± 0.28</td> <!-- SUC3 -->
   <td class="sv sent">45.41 ± 3.48 / 51.55 ± 4.00</td> <!-- SweReC -->
   <td class="sv la">7.84 ± 1.67 / 49.54 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.16 ± 0.11 / 17.72 ± 1.71</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">262</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">908 ± 171 / 248 ± 76</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">17.08 ± 2.11 / 22.55 ± 2.89</td> <!-- DaNE -->
   <td class="da sent">39.50 ± 1.36 / 57.75 ± 1.40</td> <!-- AngryTweets -->
   <td class="da la">-0.86 ± 1.15 / 33.44 ± 0.21</td> <!-- ScaLA-da -->
   <td class="da qa">0.19 ± 0.11 / 12.76 ± 2.64</td> <!-- ScandiQA-da -->
   <td class="no ner">10.21 ± 4.32 / 10.64 ± 4.71</td> <!-- NorNE-nb -->
   <td class="no ner">8.23 ± 3.99 / 8.47 ± 4.40</td> <!-- NorNE-nn -->
   <td class="no sent">32.48 ± 1.21 / 41.56 ± 1.94</td> <!-- NoReC -->
   <td class="no la">-0.12 ± 0.98 / 33.55 ± 0.31</td> <!-- ScaLA-nb -->
   <td class="no la">-1.37 ± 1.36 / 34.19 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">0.50 ± 0.49 / 12.38 ± 1.55</td> <!-- ScandiQA-no -->
   <td class="sv ner">14.10 ± 2.39 / 16.81 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 0.85 / 76.27 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">0.76 ± 1.41 / 37.92 ± 3.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.47 ± 0.31 / 14.76 ± 1.55</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>gpt-4-0613 (val) (few-shot)</td> <!-- Model ID -->
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
   <td class="da ner">66.13 ± 4.16 / 82.80 ± 1.74</td> <!-- DaNE -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- AngryTweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">49.82 ± 1.79 / 60.78 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">63.39 ± 4.07 / 81.16 ± 2.46</td> <!-- NorNE-nb -->
   <td class="no ner">60.44 ± 5.46 / 75.75 ± 4.49</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">54.79 ± 1.85 / 65.03 ± 1.52</td> <!-- ScandiQA-no -->
   <td class="sv ner">54.97 ± 4.44 / 76.86 ± 1.89</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.50 ± 1.74 / 67.22 ± 1.24</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (val) (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">66.79 ± 3.20 / 78.54 ± 2.27</td> <!-- DaNE -->
   <td class="da sent">50.54 ± 3.00 / 66.79 ± 1.87</td> <!-- AngryTweets -->
   <td class="da la">57.57 ± 3.30 / 77.07 ± 1.91</td> <!-- ScaLA-da -->
   <td class="da qa">51.09 ± 1.97 / 59.01 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">68.71 ± 2.97 / 77.70 ± 2.64</td> <!-- NorNE-nb -->
   <td class="no ner">67.96 ± 2.67 / 73.92 ± 2.53</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">57.31 ± 1.83 / 64.43 ± 1.58</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.64 ± 3.63 / 73.04 ± 2.74</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.59 ± 2.08 / 65.53 ± 1.76</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">85.01 ± 0.51 / 85.45 ± 0.79</td> <!-- DaNE -->
   <td class="da sent">55.07 ± 1.53 / 69.43 ± 1.47</td> <!-- AngryTweets -->
   <td class="da la">57.67 ± 2.56 / 78.48 ± 1.32</td> <!-- ScaLA-da -->
   <td class="da qa">50.24 ± 1.96 / 55.93 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">90.64 ± 0.80 / 89.86 ± 0.93</td> <!-- NorNE-nb -->
   <td class="no ner">86.52 ± 0.94 / 84.32 ± 1.08</td> <!-- NorNE-nn -->
   <td class="no sent">61.52 ± 1.87 / 72.72 ± 1.95</td> <!-- NoReC -->
   <td class="no la">62.34 ± 2.48 / 79.94 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">34.88 ± 11.23 / 66.51 ± 5.72</td> <!-- ScaLA-nn -->
   <td class="no qa">53.63 ± 1.65 / 59.77 ± 1.34</td> <!-- ScandiQA-no -->
   <td class="sv ner">78.57 ± 1.27 / 80.36 ± 1.12</td> <!-- SUC3 -->
   <td class="sv sent">79.65 ± 1.05 / 78.90 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">63.15 ± 1.65 / 81.06 ± 0.95</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.35 ± 1.49 / 59.32 ± 1.41</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.79 ± 0.57 / 81.04 ± 0.60</td> <!-- DaNE -->
   <td class="da sent">41.53 ± 1.91 / 59.82 ± 1.67</td> <!-- AngryTweets -->
   <td class="da la">41.62 ± 10.78 / 68.99 ± 5.73</td> <!-- ScaLA-da -->
   <td class="da qa">45.00 ± 1.07 / 49.43 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="no ner">87.45 ± 0.54 / 87.50 ± 0.53</td> <!-- NorNE-nb -->
   <td class="no ner">82.71 ± 1.13 / 80.57 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">47.11 ± 2.05 / 60.70 ± 3.19</td> <!-- NoReC -->
   <td class="no la">52.62 ± 3.99 / 75.01 ± 2.43</td> <!-- ScaLA-nb -->
   <td class="no la">25.06 ± 6.94 / 60.75 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">46.55 ± 1.76 / 51.41 ± 1.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">78.69 ± 1.68 / 80.65 ± 2.12</td> <!-- SUC3 -->
   <td class="sv sent">77.43 ± 1.07 / 75.95 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">76.56 ± 1.06 / 87.86 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.25 ± 1.41 / 55.38 ± 1.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>BAAI/bge-large-en</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,117 ± 1,352 / 1,299 ± 417</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">58.72 ± 1.19 / 55.07 ± 1.24</td> <!-- DaNE -->
   <td class="da sent">28.73 ± 2.73 / 48.91 ± 3.71</td> <!-- AngryTweets -->
   <td class="da la">3.81 ± 1.98 / 46.36 ± 3.00</td> <!-- ScaLA-da -->
   <td class="da qa">35.33 ± 1.66 / 38.87 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="no ner">60.70 ± 1.14 / 60.83 ± 1.42</td> <!-- NorNE-nb -->
   <td class="no ner">56.19 ± 1.53 / 56.28 ± 1.80</td> <!-- NorNE-nn -->
   <td class="no sent">22.17 ± 2.38 / 40.55 ± 2.37</td> <!-- NoReC -->
   <td class="no la">2.10 ± 2.57 / 43.68 ± 3.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.57 ± 1.18 / 46.46 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">34.24 ± 1.12 / 38.52 ± 1.15</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.29 ± 2.53 / 45.73 ± 2.74</td> <!-- SUC3 -->
   <td class="sv sent">60.08 ± 0.84 / 57.18 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">3.03 ± 1.67 / 45.20 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.68 ± 2.14 / 40.92 ± 2.00</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>numind/generic-sentiment-multi-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,703 ± 2,909 / 3,251 ± 1,057</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.99 ± 1.00 / 81.00 ± 1.49</td> <!-- DaNE -->
   <td class="da sent">50.62 ± 1.69 / 66.18 ± 1.52</td> <!-- AngryTweets -->
   <td class="da la">24.10 ± 5.15 / 54.72 ± 4.73</td> <!-- ScaLA-da -->
   <td class="da qa">40.46 ± 4.43 / 46.26 ± 4.36</td> <!-- ScandiQA-da -->
   <td class="no ner">88.87 ± 1.16 / 87.92 ± 1.42</td> <!-- NorNE-nb -->
   <td class="no ner">83.93 ± 0.73 / 81.51 ± 0.92</td> <!-- NorNE-nn -->
   <td class="no sent">54.92 ± 1.07 / 67.91 ± 1.41</td> <!-- NoReC -->
   <td class="no la">26.26 ± 8.44 / 54.22 ± 5.52</td> <!-- ScaLA-nb -->
   <td class="no la">11.85 ± 6.47 / 51.82 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no qa">41.51 ± 3.48 / 47.54 ± 3.65</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.74 ± 1.41 / 77.94 ± 1.35</td> <!-- SUC3 -->
   <td class="sv sent">74.96 ± 0.84 / 67.87 ± 2.52</td> <!-- SweReC -->
   <td class="sv la">42.06 ± 5.36 / 66.63 ± 2.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.01 ± 1.94 / 49.31 ± 2.01</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">84.75 ± 0.68 / 85.19 ± 0.81</td> <!-- DaNE -->
   <td class="da sent">47.55 ± 1.25 / 64.66 ± 0.96</td> <!-- AngryTweets -->
   <td class="da la">68.72 ± 1.40 / 83.85 ± 0.85</td> <!-- ScaLA-da -->
   <td class="da qa">47.46 ± 0.85 / 52.01 ± 0.85</td> <!-- ScandiQA-da -->
   <td class="no ner">91.04 ± 0.58 / 91.17 ± 0.52</td> <!-- NorNE-nb -->
   <td class="no ner">88.83 ± 0.84 / 87.30 ± 1.07</td> <!-- NorNE-nn -->
   <td class="no sent">59.10 ± 1.47 / 70.50 ± 2.06</td> <!-- NoReC -->
   <td class="no la">74.32 ± 1.76 / 86.47 ± 1.18</td> <!-- ScaLA-nb -->
   <td class="no la">72.94 ± 1.63 / 86.07 ± 0.99</td> <!-- ScaLA-nn -->
   <td class="no qa">47.77 ± 0.86 / 53.09 ± 0.99</td> <!-- ScandiQA-no -->
   <td class="sv ner">79.18 ± 1.23 / 81.35 ± 1.26</td> <!-- SUC3 -->
   <td class="sv sent">71.16 ± 1.21 / 69.78 ± 3.24</td> <!-- SweReC -->
   <td class="sv la">63.89 ± 1.18 / 81.45 ± 0.75</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.04 ± 1.42 / 50.20 ± 1.43</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.61 ± 0.63 / 84.30 ± 0.68</td> <!-- DaNE -->
   <td class="da sent">55.12 ± 1.58 / 69.99 ± 1.09</td> <!-- AngryTweets -->
   <td class="da la">76.34 ± 2.35 / 87.56 ± 1.48</td> <!-- ScaLA-da -->
   <td class="da qa">45.83 ± 7.90 / 51.05 ± 7.83</td> <!-- ScandiQA-da -->
   <td class="no ner">85.37 ± 0.78 / 86.78 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">82.22 ± 1.30 / 83.28 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">58.73 ± 2.31 / 70.10 ± 2.66</td> <!-- NoReC -->
   <td class="no la">70.73 ± 3.19 / 84.71 ± 1.82</td> <!-- ScaLA-nb -->
   <td class="no la">59.58 ± 7.22 / 78.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">54.15 ± 2.17 / 59.53 ± 2.15</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.05 ± 1.65 / 71.86 ± 1.73</td> <!-- SUC3 -->
   <td class="sv sent">74.67 ± 1.43 / 71.15 ± 3.57</td> <!-- SweReC -->
   <td class="sv la">62.77 ± 3.14 / 80.75 ± 1.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.21 ± 3.52 / 57.13 ± 3.34</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>numind/generic-sentiment-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,921 ± 3,214 / 2,714 ± 886</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">57.96 ± 1.22 / 54.81 ± 1.52</td> <!-- DaNE -->
   <td class="da sent">35.25 ± 0.80 / 55.85 ± 0.89</td> <!-- AngryTweets -->
   <td class="da la">2.64 ± 1.25 / 48.56 ± 2.09</td> <!-- ScaLA-da -->
   <td class="da qa">30.30 ± 1.66 / 34.82 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="no ner">56.14 ± 1.62 / 55.89 ± 1.84</td> <!-- NorNE-nb -->
   <td class="no ner">52.91 ± 1.43 / 52.79 ± 1.36</td> <!-- NorNE-nn -->
   <td class="no sent">26.15 ± 1.97 / 43.01 ± 2.36</td> <!-- NoReC -->
   <td class="no la">0.87 ± 1.38 / 45.54 ± 3.74</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 1.98 / 47.98 ± 2.59</td> <!-- ScaLA-nn -->
   <td class="no qa">30.08 ± 1.52 / 34.62 ± 1.47</td> <!-- ScandiQA-no -->
   <td class="sv ner">39.30 ± 3.21 / 40.62 ± 3.22</td> <!-- SUC3 -->
   <td class="sv sent">61.43 ± 1.77 / 56.67 ± 1.99</td> <!-- SweReC -->
   <td class="sv la">2.38 ± 1.82 / 48.42 ± 1.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.60 ± 2.18 / 36.77 ± 2.02</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">82.30 ± 0.85 / 82.09 ± 0.94</td> <!-- DaNE -->
   <td class="da sent">49.88 ± 1.21 / 66.06 ± 1.12</td> <!-- AngryTweets -->
   <td class="da la">44.20 ± 2.01 / 70.33 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da qa">45.20 ± 2.63 / 51.03 ± 2.47</td> <!-- ScandiQA-da -->
   <td class="no ner">89.24 ± 0.95 / 88.26 ± 1.11</td> <!-- NorNE-nb -->
   <td class="no ner">83.89 ± 1.34 / 81.37 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">54.61 ± 1.51 / 67.19 ± 1.65</td> <!-- NoReC -->
   <td class="no la">50.35 ± 1.78 / 73.06 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">22.15 ± 9.02 / 58.20 ± 5.38</td> <!-- ScaLA-nn -->
   <td class="no qa">46.16 ± 1.57 / 52.30 ± 1.60</td> <!-- ScandiQA-no -->
   <td class="sv ner">77.59 ± 0.76 / 79.02 ± 0.74</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.89 / 69.85 ± 3.16</td> <!-- SweReC -->
   <td class="sv la">50.19 ± 1.23 / 74.23 ± 0.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.88 ± 1.29 / 53.21 ± 1.29</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>BAAI/bge-base-en</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,076 ± 3,208 / 2,747 ± 895</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">48.95 ± 0.94 / 44.43 ± 1.01</td> <!-- DaNE -->
   <td class="da sent">29.98 ± 2.75 / 50.27 ± 4.20</td> <!-- AngryTweets -->
   <td class="da la">2.94 ± 1.46 / 47.32 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da qa">32.84 ± 2.29 / 37.51 ± 2.36</td> <!-- ScandiQA-da -->
   <td class="no ner">50.86 ± 2.05 / 50.46 ± 2.18</td> <!-- NorNE-nb -->
   <td class="no ner">47.15 ± 2.60 / 46.75 ± 2.53</td> <!-- NorNE-nn -->
   <td class="no sent">20.34 ± 2.81 / 37.92 ± 3.29</td> <!-- NoReC -->
   <td class="no la">2.29 ± 1.44 / 48.73 ± 1.70</td> <!-- ScaLA-nb -->
   <td class="no la">0.83 ± 1.51 / 46.34 ± 3.28</td> <!-- ScaLA-nn -->
   <td class="no qa">33.70 ± 1.50 / 39.09 ± 1.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">32.58 ± 2.48 / 33.99 ± 2.38</td> <!-- SUC3 -->
   <td class="sv sent">61.34 ± 0.79 / 57.88 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">2.97 ± 1.98 / 48.51 ± 2.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.84 ± 1.62 / 37.40 ± 1.69</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>thenlper/gte-large</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,271 ± 1,362 / 1,345 ± 429</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">59.67 ± 1.68 / 56.78 ± 1.79</td> <!-- DaNE -->
   <td class="da sent">28.22 ± 2.92 / 48.64 ± 4.09</td> <!-- AngryTweets -->
   <td class="da la">1.41 ± 2.05 / 46.26 ± 3.31</td> <!-- ScaLA-da -->
   <td class="da qa">30.96 ± 3.17 / 34.12 ± 3.37</td> <!-- ScandiQA-da -->
   <td class="no ner">60.85 ± 1.45 / 60.48 ± 1.46</td> <!-- NorNE-nb -->
   <td class="no ner">58.13 ± 1.09 / 57.90 ± 1.16</td> <!-- NorNE-nn -->
   <td class="no sent">18.82 ± 4.62 / 35.98 ± 3.95</td> <!-- NoReC -->
   <td class="no la">0.98 ± 1.23 / 47.66 ± 2.35</td> <!-- ScaLA-nb -->
   <td class="no la">0.32 ± 0.80 / 46.12 ± 3.38</td> <!-- ScaLA-nn -->
   <td class="no qa">34.39 ± 2.03 / 38.22 ± 1.88</td> <!-- ScandiQA-no -->
   <td class="sv ner">44.03 ± 1.91 / 45.74 ± 2.08</td> <!-- SUC3 -->
   <td class="sv sent">56.50 ± 2.85 / 53.06 ± 1.20</td> <!-- SweReC -->
   <td class="sv la">3.57 ± 1.65 / 46.15 ± 3.18</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.67 ± 3.00 / 39.88 ± 2.82</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>thenlper/gte-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,255 ± 3,022 / 2,597 ± 843</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">48.26 ± 1.78 / 43.74 ± 2.53</td> <!-- DaNE -->
   <td class="da sent">27.50 ± 2.17 / 47.23 ± 3.71</td> <!-- AngryTweets -->
   <td class="da la">2.66 ± 1.84 / 47.50 ± 2.84</td> <!-- ScaLA-da -->
   <td class="da qa">31.52 ± 2.20 / 36.41 ± 2.36</td> <!-- ScandiQA-da -->
   <td class="no ner">51.56 ± 1.77 / 51.20 ± 1.84</td> <!-- NorNE-nb -->
   <td class="no ner">47.41 ± 1.30 / 47.15 ± 1.35</td> <!-- NorNE-nn -->
   <td class="no sent">20.21 ± 1.94 / 37.93 ± 1.05</td> <!-- NoReC -->
   <td class="no la">1.00 ± 1.33 / 49.48 ± 1.17</td> <!-- ScaLA-nb -->
   <td class="no la">1.36 ± 1.96 / 47.74 ± 2.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.97 ± 1.40 / 39.42 ± 1.35</td> <!-- ScandiQA-no -->
   <td class="sv ner">27.43 ± 7.85 / 28.68 ± 8.10</td> <!-- SUC3 -->
   <td class="sv sent">60.29 ± 1.45 / 56.28 ± 2.38</td> <!-- SweReC -->
   <td class="sv la">2.67 ± 1.22 / 50.23 ± 0.76</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.63 ± 1.77 / 37.99 ± 1.75</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>BAAI/bge-small-en</td> <!-- Model ID -->
   <td class="num_model_parameters">33</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,320 ± 3,732 / 2,708 ± 883</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">45.50 ± 1.58 / 40.60 ± 1.99</td> <!-- DaNE -->
   <td class="da sent">30.57 ± 1.75 / 52.42 ± 1.65</td> <!-- AngryTweets -->
   <td class="da la">2.04 ± 1.32 / 48.36 ± 2.78</td> <!-- ScaLA-da -->
   <td class="da qa">34.04 ± 1.75 / 39.19 ± 1.74</td> <!-- ScandiQA-da -->
   <td class="no ner">44.65 ± 2.72 / 44.49 ± 2.76</td> <!-- NorNE-nb -->
   <td class="no ner">41.94 ± 0.99 / 41.71 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">18.03 ± 2.87 / 36.56 ± 2.43</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.58 / 47.09 ± 2.15</td> <!-- ScaLA-nb -->
   <td class="no la">3.39 ± 1.48 / 47.82 ± 2.77</td> <!-- ScaLA-nn -->
   <td class="no qa">32.20 ± 2.82 / 37.78 ± 2.77</td> <!-- ScandiQA-no -->
   <td class="sv ner">33.88 ± 1.50 / 35.49 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">55.44 ± 1.73 / 52.60 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">3.23 ± 2.31 / 46.12 ± 2.73</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.50 ± 2.08 / 42.12 ± 2.09</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>intfloat/e5-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,100 ± 2,962 / 2,594 ± 838</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">56.37 ± 1.18 / 53.39 ± 1.55</td> <!-- DaNE -->
   <td class="da sent">32.51 ± 1.61 / 53.48 ± 1.34</td> <!-- AngryTweets -->
   <td class="da la">2.76 ± 1.99 / 46.13 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da qa">32.91 ± 1.64 / 37.51 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="no ner">57.53 ± 1.47 / 57.27 ± 1.75</td> <!-- NorNE-nb -->
   <td class="no ner">52.66 ± 1.06 / 52.63 ± 1.05</td> <!-- NorNE-nn -->
   <td class="no sent">21.08 ± 1.44 / 39.20 ± 1.29</td> <!-- NoReC -->
   <td class="no la">2.34 ± 1.55 / 48.26 ± 2.28</td> <!-- ScaLA-nb -->
   <td class="no la">2.41 ± 2.13 / 48.88 ± 1.85</td> <!-- ScaLA-nn -->
   <td class="no qa">34.89 ± 2.02 / 39.62 ± 1.91</td> <!-- ScandiQA-no -->
   <td class="sv ner">41.67 ± 2.15 / 43.43 ± 2.19</td> <!-- SUC3 -->
   <td class="sv sent">60.05 ± 1.84 / 58.14 ± 2.20</td> <!-- SweReC -->
   <td class="sv la">3.10 ± 1.11 / 47.62 ± 2.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.51 ± 1.96 / 39.42 ± 1.94</td> <!-- ScandiQA-sv -->
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
   <td class="da ner">83.14 ± 0.50 / 83.61 ± 0.62</td> <!-- DaNE -->
   <td class="da sent">53.85 ± 1.39 / 68.94 ± 1.19</td> <!-- AngryTweets -->
   <td class="da la">75.71 ± 1.95 / 87.29 ± 1.14</td> <!-- ScaLA-da -->
   <td class="da qa">51.70 ± 1.75 / 56.71 ± 1.66</td> <!-- ScandiQA-da -->
   <td class="no ner">85.20 ± 0.97 / 86.39 ± 1.06</td> <!-- NorNE-nb -->
   <td class="no ner">82.50 ± 1.19 / 83.22 ± 1.44</td> <!-- NorNE-nn -->
   <td class="no sent">59.61 ± 1.28 / 71.40 ± 1.68</td> <!-- NoReC -->
   <td class="no la">67.88 ± 7.37 / 82.75 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">62.44 ± 4.39 / 80.43 ± 2.39</td> <!-- ScaLA-nn -->
   <td class="no qa">51.98 ± 2.70 / 57.40 ± 2.51</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.08 ± 1.45 / 71.65 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">74.92 ± 0.98 / 72.01 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">63.43 ± 2.30 / 81.00 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.44 ± 4.06 / 57.13 ± 4.00</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-2</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,965 ± 2,550 / 3,798 ± 1,216</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">82.93 ± 0.65 / 83.71 ± 0.74</td> <!-- DaNE -->
   <td class="da sent">50.25 ± 1.47 / 66.43 ± 1.28</td> <!-- AngryTweets -->
   <td class="da la">75.14 ± 1.15 / 87.22 ± 0.60</td> <!-- ScaLA-da -->
   <td class="da qa">44.92 ± 1.38 / 49.93 ± 1.23</td> <!-- ScandiQA-da -->
   <td class="no ner">87.68 ± 0.83 / 87.07 ± 1.01</td> <!-- NorNE-nb -->
   <td class="no ner">79.86 ± 1.27 / 77.63 ± 1.69</td> <!-- NorNE-nn -->
   <td class="no sent">48.01 ± 0.97 / 61.92 ± 1.34</td> <!-- NoReC -->
   <td class="no la">57.39 ± 1.02 / 78.18 ± 0.68</td> <!-- ScaLA-nb -->
   <td class="no la">15.72 ± 9.07 / 56.05 ± 4.76</td> <!-- ScaLA-nn -->
   <td class="no qa">41.15 ± 2.83 / 46.64 ± 3.08</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.47 ± 1.56 / 72.99 ± 1.54</td> <!-- SUC3 -->
   <td class="sv sent">66.15 ± 0.83 / 66.44 ± 1.92</td> <!-- SweReC -->
   <td class="sv la">18.80 ± 10.50 / 57.59 ± 5.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.34 ± 1.18 / 44.72 ± 1.28</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,998 ± 2,549 / 3,833 ± 1,223</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">84.04 ± 0.72 / 84.40 ± 0.80</td> <!-- DaNE -->
   <td class="da sent">51.88 ± 1.86 / 67.72 ± 1.50</td> <!-- AngryTweets -->
   <td class="da la">72.22 ± 2.83 / 85.57 ± 1.45</td> <!-- ScaLA-da -->
   <td class="da qa">44.32 ± 2.01 / 49.51 ± 2.01</td> <!-- ScandiQA-da -->
   <td class="no ner">86.64 ± 1.03 / 85.77 ± 1.14</td> <!-- NorNE-nb -->
   <td class="no ner">81.68 ± 1.41 / 79.55 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">50.00 ± 1.41 / 64.19 ± 1.32</td> <!-- NoReC -->
   <td class="no la">56.68 ± 2.18 / 77.32 ± 1.61</td> <!-- ScaLA-nb -->
   <td class="no la">20.64 ± 9.03 / 59.21 ± 4.53</td> <!-- ScaLA-nn -->
   <td class="no qa">44.13 ± 1.49 / 49.68 ± 1.31</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.79 ± 1.09 / 73.08 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">65.98 ± 1.14 / 61.49 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">23.08 ± 10.49 / 58.31 ± 6.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.97 ± 1.70 / 44.11 ± 1.61</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,702 ± 1,519 / 2,128 ± 705</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">83.88 ± 0.73 / 84.11 ± 0.80</td> <!-- DaNE -->
   <td class="da sent">37.70 ± 2.33 / 57.76 ± 1.94</td> <!-- AngryTweets -->
   <td class="da la">51.68 ± 5.63 / 74.01 ± 3.51</td> <!-- ScaLA-da -->
   <td class="da qa">47.53 ± 1.50 / 53.93 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="no ner">90.46 ± 0.96 / 90.42 ± 0.98</td> <!-- NorNE-nb -->
   <td class="no ner">85.94 ± 1.30 / 84.35 ± 1.85</td> <!-- NorNE-nn -->
   <td class="no sent">40.30 ± 1.63 / 57.15 ± 1.82</td> <!-- NoReC -->
   <td class="no la">49.52 ± 4.76 / 71.89 ± 2.96</td> <!-- ScaLA-nb -->
   <td class="no la">32.29 ± 9.64 / 64.60 ± 5.06</td> <!-- ScaLA-nn -->
   <td class="no qa">50.94 ± 1.08 / 57.37 ± 0.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.23 ± 0.91 / 77.52 ± 1.56</td> <!-- SUC3 -->
   <td class="sv sent">71.57 ± 1.09 / 70.18 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">48.13 ± 9.69 / 73.12 ± 4.96</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.78 ± 1.45 / 55.59 ± 1.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>joelito/legal-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">184</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,294 ± 2,513 / 3,065 ± 989</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.88 ± 0.79 / 69.79 ± 1.31</td> <!-- DaNE -->
   <td class="da sent">36.43 ± 1.10 / 56.80 ± 1.26</td> <!-- AngryTweets -->
   <td class="da la">44.91 ± 2.68 / 70.74 ± 2.71</td> <!-- ScaLA-da -->
   <td class="da qa">14.14 ± 2.82 / 35.23 ± 4.92</td> <!-- ScandiQA-da -->
   <td class="no ner">63.61 ± 1.76 / 65.02 ± 2.09</td> <!-- NorNE-nb -->
   <td class="no ner">57.92 ± 0.84 / 59.42 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">29.63 ± 2.39 / 44.36 ± 2.93</td> <!-- NoReC -->
   <td class="no la">21.65 ± 10.25 / 60.22 ± 5.20</td> <!-- ScaLA-nb -->
   <td class="no la">6.63 ± 4.89 / 48.30 ± 4.94</td> <!-- ScaLA-nn -->
   <td class="no qa">13.32 ± 1.53 / 34.85 ± 2.74</td> <!-- ScandiQA-no -->
   <td class="sv ner">54.68 ± 1.27 / 56.92 ± 1.26</td> <!-- SUC3 -->
   <td class="sv sent">66.64 ± 1.04 / 62.60 ± 3.05</td> <!-- SweReC -->
   <td class="sv la">49.11 ± 1.62 / 73.82 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">13.79 ± 2.10 / 35.46 ± 3.01</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>joelito/legal-xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">435</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,190 ± 1,150 / 1,534 ± 490</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.43 ± 0.99 / 76.26 ± 1.02</td> <!-- DaNE -->
   <td class="da sent">35.67 ± 6.45 / 54.23 ± 7.36</td> <!-- AngryTweets -->
   <td class="da la">10.25 ± 11.58 / 50.79 ± 7.22</td> <!-- ScaLA-da -->
   <td class="da qa">15.78 ± 2.52 / 40.01 ± 4.22</td> <!-- ScandiQA-da -->
   <td class="no ner">62.57 ± 13.70 / 63.94 ± 14.01</td> <!-- NorNE-nb -->
   <td class="no ner">59.08 ± 6.22 / 60.44 ± 5.90</td> <!-- NorNE-nn -->
   <td class="no sent">10.28 ± 9.99 / 30.78 ± 8.26</td> <!-- NoReC -->
   <td class="no la">5.78 ± 3.89 / 44.86 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">0.73 ± 1.05 / 44.50 ± 4.08</td> <!-- ScaLA-nn -->
   <td class="no qa">13.32 ± 3.51 / 35.54 ± 6.68</td> <!-- ScandiQA-no -->
   <td class="sv ner">48.11 ± 15.90 / 50.19 ± 16.59</td> <!-- SUC3 -->
   <td class="sv sent">57.27 ± 9.47 / 54.20 ± 5.68</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 6.42 / 46.25 ± 5.14</td> <!-- ScaLA-sv -->
   <td class="sv qa">13.88 ± 1.80 / 36.16 ± 4.81</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td class="rank"></td> <!-- Rank -->
   <td>dandanw/bloom-3b-sv (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1843</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">259</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">515</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,715 ± 367 / 399 ± 128</td> <!-- Model inference speed -->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DaNE -->
   <td class="da sent">3.62 ± 3.14 / 26.55 ± 3.60</td> <!-- AngryTweets -->
   <td class="da la">3.27 ± 0.71 / 40.67 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 1.91 ± 0.28</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.61 ± 2.91 / 23.67 ± 2.67</td> <!-- NoReC -->
   <td class="no la">0.37 ± 0.93 / 34.03 ± 0.54</td> <!-- ScaLA-nb -->
   <td class="no la">1.01 ± 1.45 / 33.76 ± 1.06</td> <!-- ScaLA-nn -->
   <td class="no qa">0.03 ± 0.02 / 1.80 ± 0.33</td> <!-- ScandiQA-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">41.76 ± 9.57 / 44.25 ± 7.77</td> <!-- SweReC -->
   <td class="sv la">2.64 ± 1.75 / 46.87 ± 2.08</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.02 ± 0.03 / 3.42 ± 0.35</td> <!-- ScandiQA-sv -->
  </tr>
 </tbody>
</table>
</div>