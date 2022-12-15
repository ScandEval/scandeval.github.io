---
layout: leaderboard
title: Language Model Benchmark
---

<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="language-model-benchmark" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of trainable parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
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
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>vesteinn/ScandiBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>ltgoslo/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
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
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
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
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
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
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>fresh-xlmr-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
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
 </tbody>
</table>
</div>