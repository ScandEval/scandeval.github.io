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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of trainable parameters in the model">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Sequence length</span></th>
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">ABSAbank-Imm</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact match / F1-score">ScandiQA-sv</span></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135195651</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">74.32 ± 0.46 / 77.17 ± 0.48</td> <!-- DaNE -->
   <td class="da sent">39.16 ± 1.09 / 59.54 ± 0.72</td> <!-- AngryTweets -->
   <td class="da la">4.42 ± 1.28 / 47.16 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">28.36 ± 0.33 / 34.00 ± 0.32</td> <!-- ScandiQA-da -->
   <td class="no ner">81.39 ± 0.29 / 84.02 ± 0.32</td> <!-- NorNE-nb -->
   <td class="no ner">78.01 ± 0.37 / 81.32 ± 0.31</td> <!-- NorNE-nn -->
   <td class="no sent">41.31 ± 0.73 / 58.97 ± 0.59</td> <!-- NoReC -->
   <td class="no la">15.14 ± 1.52 / 57.51 ± 0.76</td> <!-- ScaLA-nb -->
   <td class="no la">4.85 ± 1.39 / 52.37 ± 0.69</td> <!-- ScaLA-nn -->
   <td class="no qa">31.39 ± 0.37 / 36.28 ± 0.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.59 ± 0.66 / 81.24 ± 0.68</td> <!-- SUC3 -->
   <td class="sv sent">32.37 ± 1.80 / 55.26 ± 1.40</td> <!-- ABSAbank-Imm -->
   <td class="sv la">73.22 ± 0.69 / 85.18 ± 0.38</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.85 ± 0.65 / 49.14 ± 0.66</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278045955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">46.25 ± 3.45 / 48.51 ± 3.20</td> <!-- DaNE -->
   <td class="da sent">23.24 ± 1.01 / 48.20 ± 0.68</td> <!-- AngryTweets -->
   <td class="da la">1.61 ± 1.67 / 47.00 ± 2.78</td> <!-- ScaLA-da -->
   <td class="da qa">1.06 ± 0.12 / 7.28 ± 0.14</td> <!-- ScandiQA-da -->
   <td class="no ner">48.03 ± 10.73 / 50.66 ± 11.31</td> <!-- NorNE-nb -->
   <td class="no ner">47.14 ± 3.57 / 50.18 ± 3.71</td> <!-- NorNE-nn -->
   <td class="no sent">14.29 ± 1.75 / 34.44 ± 1.66</td> <!-- NoReC -->
   <td class="no la">1.70 ± 1.34 / 45.90 ± 1.50</td> <!-- ScaLA-nb -->
   <td class="no la">-0.56 ± 1.39 / 46.11 ± 1.85</td> <!-- ScaLA-nn -->
   <td class="no qa">19.16 ± 0.35 / 25.58 ± 0.27</td> <!-- ScandiQA-no -->
   <td class="sv ner">41.45 ± 2.11 / 43.81 ± 2.27</td> <!-- SUC3 -->
   <td class="sv sent">-7.73 ± 0.88 / 21.74 ± 0.17</td> <!-- ABSAbank-Imm -->
   <td class="sv la">1.12 ± 1.73 / 47.34 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.56 ± 0.35 / 22.41 ± 0.35</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>sarnikowski/electra-small-generator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">4389827</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">28995</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">42.55 ± 1.66 / 42.30 ± 1.89</td> <!-- DaNE -->
   <td class="da sent">22.87 ± 2.73 / 42.11 ± 3.33</td> <!-- AngryTweets -->
   <td class="da la">2.03 ± 1.81 / 45.56 ± 3.32</td> <!-- ScaLA-da -->
   <td class="da qa">4.98 ± 0.24 / 10.95 ± 0.20</td> <!-- ScandiQA-da -->
   <td class="no ner">38.83 ± 1.53 / 41.08 ± 1.58</td> <!-- NorNE-nb -->
   <td class="no ner">31.96 ± 2.18 / 33.78 ± 2.30</td> <!-- NorNE-nn -->
   <td class="no sent">19.70 ± 2.19 / 38.53 ± 1.37</td> <!-- NoReC -->
   <td class="no la">5.10 ± 1.92 / 50.22 ± 3.35</td> <!-- ScaLA-nb -->
   <td class="no la">0.39 ± 1.36 / 43.71 ± 3.81</td> <!-- ScaLA-nn -->
   <td class="no qa">4.03 ± 0.20 / 10.15 ± 0.25</td> <!-- ScandiQA-no -->
   <td class="sv ner">26.98 ± 1.24 / 28.81 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">8.21 ± 1.43 / 31.69 ± 1.58</td> <!-- ABSAbank-Imm -->
   <td class="sv la">3.78 ± 2.19 / 45.84 ± 5.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">5.54 ± 0.23 / 13.25 ± 0.17</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/distilbert-base-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61485315</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23399</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.79 ± 0.97 / 78.84 ± 0.94</td> <!-- DaNE -->
   <td class="da sent">30.59 ± 1.27 / 52.88 ± 1.19</td> <!-- AngryTweets -->
   <td class="da la">32.97 ± 2.29 / 65.26 ± 2.05</td> <!-- ScaLA-da -->
   <td class="da qa">36.62 ± 0.30 / 40.34 ± 0.36</td> <!-- ScandiQA-da -->
   <td class="no ner">81.50 ± 1.10 / 84.30 ± 1.05</td> <!-- NorNE-nb -->
   <td class="no ner">75.25 ± 1.20 / 79.43 ± 0.99</td> <!-- NorNE-nn -->
   <td class="no sent">31.69 ± 1.94 / 44.58 ± 2.55</td> <!-- NoReC -->
   <td class="no la">36.35 ± 2.23 / 66.84 ± 1.81</td> <!-- ScaLA-nb -->
   <td class="no la">25.46 ± 5.64 / 61.46 ± 3.14</td> <!-- ScaLA-nn -->
   <td class="no qa">35.38 ± 0.38 / 39.25 ± 0.42</td> <!-- ScandiQA-no -->
   <td class="sv ner">63.95 ± 1.30 / 69.70 ± 0.95</td> <!-- SUC3 -->
   <td class="sv sent">15.43 ± 2.84 / 37.98 ± 3.70</td> <!-- ABSAbank-Imm -->
   <td class="sv la">29.20 ± 1.00 / 63.07 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">36.29 ± 0.49 / 41.28 ± 0.45</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>ltgoslo/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">124523523</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50104</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">79.75 ± 0.45 / 81.34 ± 0.55</td> <!-- DaNE -->
   <td class="da sent">39.83 ± 1.53 / 59.76 ± 1.33</td> <!-- AngryTweets -->
   <td class="da la">53.92 ± 2.85 / 75.85 ± 1.99</td> <!-- ScaLA-da -->
   <td class="da qa">37.44 ± 0.44 / 41.24 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="no ner">87.21 ± 0.57 / 90.16 ± 0.43</td> <!-- NorNE-nb -->
   <td class="no ner">82.97 ± 0.87 / 86.52 ± 0.69</td> <!-- NorNE-nn -->
   <td class="no sent">58.84 ± 1.17 / 70.79 ± 1.27</td> <!-- NoReC -->
   <td class="no la">69.27 ± 2.09 / 83.11 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">66.96 ± 1.49 / 82.84 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no qa">41.47 ± 0.58 / 45.66 ± 0.49</td> <!-- ScandiQA-no -->
   <td class="sv ner">60.77 ± 0.66 / 65.87 ± 0.65</td> <!-- SUC3 -->
   <td class="sv sent">21.15 ± 3.24 / 46.79 ± 3.88</td> <!-- ABSAbank-Imm -->
   <td class="sv la">34.51 ± 2.47 / 65.50 ± 1.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.06 ± 0.61 / 39.72 ± 0.63</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135293955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">73.02 ± 0.44 / 75.99 ± 0.52</td> <!-- DaNE -->
   <td class="da sent">36.49 ± 1.05 / 57.33 ± 0.68</td> <!-- AngryTweets -->
   <td class="da la">22.80 ± 0.91 / 57.17 ± 0.60</td> <!-- ScaLA-da -->
   <td class="da qa">37.89 ± 0.54 / 43.03 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">76.13 ± 0.59 / 78.68 ± 0.56</td> <!-- NorNE-nb -->
   <td class="no ner">73.29 ± 0.57 / 76.92 ± 0.38</td> <!-- NorNE-nn -->
   <td class="no sent">29.25 ± 0.93 / 41.92 ± 0.40</td> <!-- NoReC -->
   <td class="no la">20.03 ± 1.55 / 53.88 ± 0.94</td> <!-- ScaLA-nb -->
   <td class="no la">19.26 ± 1.19 / 57.45 ± 0.59</td> <!-- ScaLA-nn -->
   <td class="no qa">33.99 ± 0.42 / 39.01 ± 0.57</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.19 ± 0.64 / 80.38 ± 0.53</td> <!-- SUC3 -->
   <td class="sv sent">31.41 ± 1.34 / 55.19 ± 0.84</td> <!-- ABSAbank-Imm -->
   <td class="sv la">71.92 ± 0.78 / 84.82 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.57 ± 0.33 / 36.12 ± 0.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61294083</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23150</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">75.08 ± 0.63 / 76.98 ± 0.60</td> <!-- DaNE -->
   <td class="da sent">32.39 ± 0.87 / 54.48 ± 0.61</td> <!-- AngryTweets -->
   <td class="da la">33.82 ± 1.43 / 64.71 ± 0.82</td> <!-- ScaLA-da -->
   <td class="da qa">40.87 ± 0.39 / 45.05 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">80.75 ± 0.80 / 83.98 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">75.64 ± 0.83 / 79.76 ± 0.63</td> <!-- NorNE-nn -->
   <td class="no sent">31.55 ± 1.03 / 43.00 ± 0.45</td> <!-- NoReC -->
   <td class="no la">35.55 ± 1.20 / 66.45 ± 0.58</td> <!-- ScaLA-nb -->
   <td class="no la">27.18 ± 0.69 / 62.57 ± 0.36</td> <!-- ScaLA-nn -->
   <td class="no qa">35.02 ± 0.29 / 38.98 ± 0.38</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.56 ± 0.65 / 70.82 ± 0.61</td> <!-- SUC3 -->
   <td class="sv sent">8.71 ± 0.99 / 29.64 ± 0.61</td> <!-- ABSAbank-Imm -->
   <td class="sv la">26.47 ± 1.08 / 61.85 ± 0.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.51 ± 0.52 / 45.03 ± 0.38</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80109315</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200001</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">28.95 ± 0.74 / 28.07 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">21.45 ± 1.06 / 40.39 ± 0.61</td> <!-- AngryTweets -->
   <td class="da la">1.09 ± 1.33 / 50.34 ± 0.70</td> <!-- ScaLA-da -->
   <td class="da qa">3.94 ± 0.24 / 9.32 ± 0.26</td> <!-- ScandiQA-da -->
   <td class="no ner">34.10 ± 0.93 / 36.06 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">29.47 ± 0.99 / 31.17 ± 0.97</td> <!-- NorNE-nn -->
   <td class="no sent">14.50 ± 1.20 / 35.53 ± 0.50</td> <!-- NoReC -->
   <td class="no la">1.65 ± 1.59 / 49.55 ± 0.83</td> <!-- ScaLA-nb -->
   <td class="no la">-0.08 ± 1.44 / 48.63 ± 0.77</td> <!-- ScaLA-nn -->
   <td class="no qa">4.77 ± 0.39 / 11.88 ± 0.37</td> <!-- ScandiQA-no -->
   <td class="sv ner">24.08 ± 0.84 / 25.51 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">5.69 ± 0.89 / 31.77 ± 0.42</td> <!-- ABSAbank-Imm -->
   <td class="sv la">1.80 ± 1.67 / 50.87 ± 0.85</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.02 ± 0.20 / 5.42 ± 0.32</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151312131</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">84985</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">82.00 ± 0.58 / 84.14 ± 0.56</td> <!-- DaNE -->
   <td class="da sent">33.97 ± 0.55 / 54.25 ± 0.47</td> <!-- AngryTweets -->
   <td class="da la">46.96 ± 1.19 / 73.40 ± 0.61</td> <!-- ScaLA-da -->
   <td class="da qa">48.38 ± 0.35 / 52.32 ± 0.31</td> <!-- ScandiQA-da -->
   <td class="no ner">82.25 ± 0.69 / 85.51 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">78.63 ± 0.51 / 82.81 ± 0.36</td> <!-- NorNE-nn -->
   <td class="no sent">35.16 ± 0.74 / 50.18 ± 0.64</td> <!-- NoReC -->
   <td class="no la">41.79 ± 0.93 / 67.70 ± 0.55</td> <!-- ScaLA-nb -->
   <td class="no la">37.95 ± 1.01 / 67.15 ± 0.56</td> <!-- ScaLA-nn -->
   <td class="no qa">46.94 ± 0.38 / 51.98 ± 0.38</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.73 ± 0.84 / 74.70 ± 0.90</td> <!-- SUC3 -->
   <td class="sv sent">23.21 ± 1.22 / 46.75 ± 0.67</td> <!-- ABSAbank-Imm -->
   <td class="sv la">43.51 ± 0.84 / 71.51 ± 0.40</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.90 ± 0.55 / 54.19 ± 0.54</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118076931</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">41710</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.98 ± 0.54 / 82.79 ± 0.52</td> <!-- DaNE -->
   <td class="da sent">33.50 ± 0.91 / 53.20 ± 0.62</td> <!-- AngryTweets -->
   <td class="da la">45.45 ± 1.43 / 72.71 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">50.45 ± 0.50 / 54.22 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="no ner">84.03 ± 0.51 / 87.17 ± 0.49</td> <!-- NorNE-nb -->
   <td class="no ner">78.83 ± 0.81 / 83.12 ± 0.64</td> <!-- NorNE-nn -->
   <td class="no sent">37.13 ± 1.09 / 51.84 ± 0.55</td> <!-- NoReC -->
   <td class="no la">48.50 ± 1.12 / 72.63 ± 0.47</td> <!-- ScaLA-nb -->
   <td class="no la">43.16 ± 1.14 / 70.43 ± 0.62</td> <!-- ScaLA-nn -->
   <td class="no qa">48.43 ± 0.56 / 53.36 ± 0.61</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.63 ± 0.75 / 74.97 ± 0.92</td> <!-- SUC3 -->
   <td class="sv sent">25.28 ± 1.20 / 49.92 ± 0.81</td> <!-- ABSAbank-Imm -->
   <td class="sv la">41.37 ± 0.90 / 69.62 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.78 ± 0.33 / 50.84 ± 0.28</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14245891</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">63.07 ± 1.23 / 66.25 ± 1.19</td> <!-- DaNE -->
   <td class="da sent">20.12 ± 1.17 / 38.29 ± 0.67</td> <!-- AngryTweets -->
   <td class="da la">5.31 ± 0.97 / 51.88 ± 0.51</td> <!-- ScaLA-da -->
   <td class="da qa">11.05 ± 0.43 / 15.67 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">59.46 ± 0.75 / 63.60 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">62.32 ± 1.15 / 66.44 ± 1.04</td> <!-- NorNE-nn -->
   <td class="no sent">22.36 ± 1.20 / 39.20 ± 0.48</td> <!-- NoReC -->
   <td class="no la">4.73 ± 1.22 / 51.44 ± 0.59</td> <!-- ScaLA-nb -->
   <td class="no la">-2.18 ± 0.97 / 45.36 ± 0.67</td> <!-- ScaLA-nn -->
   <td class="no qa">19.13 ± 0.40 / 23.80 ± 0.47</td> <!-- ScandiQA-no -->
   <td class="sv ner">57.04 ± 1.21 / 61.44 ± 1.23</td> <!-- SUC3 -->
   <td class="sv sent">18.18 ± 1.03 / 46.21 ± 0.65</td> <!-- ABSAbank-Imm -->
   <td class="sv la">20.13 ± 1.39 / 57.92 ± 0.72</td> <!-- ScaLA-sv -->
   <td class="sv qa">32.76 ± 0.36 / 38.88 ± 0.42</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135328515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">119547</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">75.18 ± 0.59 / 76.39 ± 0.61</td> <!-- DaNE -->
   <td class="da sent">31.85 ± 0.53 / 54.39 ± 0.38</td> <!-- AngryTweets -->
   <td class="da la">20.76 ± 1.25 / 57.47 ± 0.79</td> <!-- ScaLA-da -->
   <td class="da qa">31.38 ± 0.25 / 34.02 ± 0.29</td> <!-- ScandiQA-da -->
   <td class="no ner">77.91 ± 0.87 / 81.24 ± 0.78</td> <!-- NorNE-nb -->
   <td class="no ner">73.79 ± 0.74 / 78.19 ± 0.66</td> <!-- NorNE-nn -->
   <td class="no sent">35.40 ± 0.73 / 46.62 ± 0.45</td> <!-- NoReC -->
   <td class="no la">25.39 ± 0.78 / 59.57 ± 0.49</td> <!-- ScaLA-nb -->
   <td class="no la">27.05 ± 1.76 / 63.46 ± 0.87</td> <!-- ScaLA-nn -->
   <td class="no qa">23.87 ± 0.59 / 28.53 ± 0.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.08 ± 0.76 / 74.90 ± 0.63</td> <!-- SUC3 -->
   <td class="sv sent">20.02 ± 0.87 / 43.75 ± 0.57</td> <!-- ABSAbank-Imm -->
   <td class="sv la">36.74 ± 0.64 / 68.35 ± 0.32</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.28 ± 0.44 / 33.05 ± 0.46</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111181059</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32731</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.95 ± 0.64 / 82.84 ± 0.63</td> <!-- DaNE -->
   <td class="da sent">34.70 ± 0.70 / 55.12 ± 0.55</td> <!-- AngryTweets -->
   <td class="da la">48.82 ± 1.46 / 74.38 ± 0.74</td> <!-- ScaLA-da -->
   <td class="da qa">49.24 ± 0.45 / 52.73 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">85.99 ± 0.39 / 88.92 ± 0.45</td> <!-- NorNE-nb -->
   <td class="no ner">81.10 ± 0.49 / 84.83 ± 0.35</td> <!-- NorNE-nn -->
   <td class="no sent">33.18 ± 0.87 / 46.89 ± 0.58</td> <!-- NoReC -->
   <td class="no la">18.00 ± 1.95 / 58.57 ± 1.04</td> <!-- ScaLA-nb -->
   <td class="no la">27.80 ± 1.39 / 63.86 ± 0.70</td> <!-- ScaLA-nn -->
   <td class="no qa">44.12 ± 0.49 / 48.86 ± 0.51</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.85 ± 0.88 / 77.22 ± 1.03</td> <!-- SUC3 -->
   <td class="sv sent">23.17 ± 1.26 / 49.43 ± 0.79</td> <!-- ABSAbank-Imm -->
   <td class="sv la">41.24 ± 0.47 / 68.30 ± 0.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.83 ± 0.51 / 50.45 ± 0.41</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">108783363</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">84985</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">77.17 ± 0.75 / 79.29 ± 0.64</td> <!-- DaNE -->
   <td class="da sent">31.07 ± 1.13 / 53.40 ± 0.80</td> <!-- AngryTweets -->
   <td class="da la">34.73 ± 1.37 / 63.84 ± 0.89</td> <!-- ScaLA-da -->
   <td class="da qa">39.81 ± 0.41 / 43.86 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="no ner">80.99 ± 0.84 / 84.11 ± 0.73</td> <!-- NorNE-nb -->
   <td class="no ner">74.80 ± 0.94 / 79.35 ± 0.74</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.09 / 43.26 ± 0.46</td> <!-- NoReC -->
   <td class="no la">30.02 ± 1.42 / 64.97 ± 0.72</td> <!-- ScaLA-nb -->
   <td class="no la">31.35 ± 1.48 / 65.64 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">36.77 ± 0.43 / 40.80 ± 0.51</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.40 ± 0.35 / 68.32 ± 0.48</td> <!-- SUC3 -->
   <td class="sv sent">7.21 ± 0.78 / 26.37 ± 0.30</td> <!-- ABSAbank-Imm -->
   <td class="sv la">27.83 ± 0.75 / 61.30 ± 0.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.02 ± 0.49 / 47.51 ± 0.47</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>fresh-xlmr-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278045955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">22.22 ± 0.78 / 18.84 ± 0.88</td> <!-- DaNE -->
   <td class="da sent">15.10 ± 1.20 / 29.87 ± 0.66</td> <!-- AngryTweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">5.82 ± 0.22 / 11.35 ± 0.23</td> <!-- ScandiQA-da -->
   <td class="no ner">30.24 ± 1.02 / 33.06 ± 1.15</td> <!-- NorNE-nb -->
   <td class="no ner">24.29 ± 1.04 / 25.74 ± 1.08</td> <!-- NorNE-nn -->
   <td class="no sent">18.74 ± 1.11 / 36.63 ± 0.46</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">2.44 ± 1.43 / 49.84 ± 0.67</td> <!-- ScaLA-nn -->
   <td class="no qa">0.86 ± 0.13 / 4.22 ± 0.17</td> <!-- ScandiQA-no -->
   <td class="sv ner">6.19 ± 0.77 / 6.92 ± 0.87</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 21.73 ± 0.22</td> <!-- ABSAbank-Imm -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.11 ± 0.29 / 15.63 ± 0.29</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135326979</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">119547</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">75.99 ± 0.49 / 78.03 ± 0.38</td> <!-- DaNE -->
   <td class="da sent">32.42 ± 1.15 / 53.57 ± 0.80</td> <!-- AngryTweets -->
   <td class="da la">30.25 ± 1.32 / 61.71 ± 0.73</td> <!-- ScaLA-da -->
   <td class="da qa">38.39 ± 0.39 / 41.86 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="no ner">81.44 ± 0.73 / 84.23 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">78.07 ± 0.78 / 81.87 ± 0.52</td> <!-- NorNE-nn -->
   <td class="no sent">36.26 ± 1.14 / 52.34 ± 0.79</td> <!-- NoReC -->
   <td class="no la">35.01 ± 1.45 / 66.64 ± 0.74</td> <!-- ScaLA-nb -->
   <td class="no la">32.71 ± 1.65 / 66.34 ± 0.82</td> <!-- ScaLA-nn -->
   <td class="no qa">36.43 ± 0.41 / 41.57 ± 0.44</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.94 ± 0.51 / 67.97 ± 0.65</td> <!-- SUC3 -->
   <td class="sv sent">20.43 ± 1.55 / 45.68 ± 1.00</td> <!-- ABSAbank-Imm -->
   <td class="sv la">33.06 ± 1.12 / 65.34 ± 0.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.92 ± 0.70 / 42.22 ± 0.67</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">110619651</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">73.14 ± 0.57 / 77.98 ± 0.49</td> <!-- DaNE -->
   <td class="da sent">45.76 ± 0.90 / 63.86 ± 0.58</td> <!-- AngryTweets -->
   <td class="da la">43.24 ± 1.24 / 68.70 ± 0.71</td> <!-- ScaLA-da -->
   <td class="da qa">41.96 ± 0.37 / 46.58 ± 0.39</td> <!-- ScandiQA-da -->
   <td class="no ner">69.15 ± 0.46 / 72.61 ± 0.46</td> <!-- NorNE-nb -->
   <td class="no ner">52.27 ± 0.89 / 55.86 ± 0.82</td> <!-- NorNE-nn -->
   <td class="no sent">39.49 ± 1.00 / 54.42 ± 0.92</td> <!-- NoReC -->
   <td class="no la">32.36 ± 1.32 / 64.69 ± 0.63</td> <!-- ScaLA-nb -->
   <td class="no la">15.68 ± 1.28 / 57.83 ± 0.64</td> <!-- ScaLA-nn -->
   <td class="no qa">35.19 ± 0.32 / 41.91 ± 0.45</td> <!-- ScandiQA-no -->
   <td class="sv ner">47.54 ± 1.03 / 51.37 ± 1.13</td> <!-- SUC3 -->
   <td class="sv sent">10.47 ± 1.17 / 37.07 ± 0.72</td> <!-- ABSAbank-Imm -->
   <td class="sv la">3.44 ± 1.38 / 50.26 ± 0.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.49 ± 0.52 / 37.19 ± 0.49</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278045955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.27 ± 0.49 / 83.16 ± 0.60</td> <!-- DaNE -->
   <td class="da sent">49.97 ± 0.78 / 67.06 ± 0.53</td> <!-- AngryTweets -->
   <td class="da la">14.35 ± 1.59 / 55.67 ± 0.82</td> <!-- ScaLA-da -->
   <td class="da qa">34.42 ± 0.54 / 38.24 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">90.68 ± 0.51 / 92.63 ± 0.34</td> <!-- NorNE-nb -->
   <td class="no ner">78.88 ± 0.87 / 82.66 ± 0.73</td> <!-- NorNE-nn -->
   <td class="no sent">54.73 ± 0.59 / 68.19 ± 0.53</td> <!-- NoReC -->
   <td class="no la">13.39 ± 1.03 / 50.71 ± 0.35</td> <!-- ScaLA-nb -->
   <td class="no la">10.02 ± 1.39 / 54.77 ± 0.68</td> <!-- ScaLA-nn -->
   <td class="no qa">31.91 ± 0.40 / 37.36 ± 0.51</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.01 ± 1.03 / 77.04 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">30.98 ± 0.85 / 55.00 ± 0.50</td> <!-- ABSAbank-Imm -->
   <td class="sv la">10.16 ± 1.18 / 50.42 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.37 ± 0.53 / 34.09 ± 0.47</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">68652291</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32731</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.70 ± 0.62 / 79.10 ± 0.59</td> <!-- DaNE -->
   <td class="da sent">32.73 ± 1.20 / 54.86 ± 0.85</td> <!-- AngryTweets -->
   <td class="da la">36.86 ± 1.19 / 66.30 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">34.70 ± 0.38 / 37.97 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">79.35 ± 1.02 / 82.93 ± 0.77</td> <!-- NorNE-nb -->
   <td class="no ner">72.87 ± 1.01 / 77.58 ± 0.81</td> <!-- NorNE-nn -->
   <td class="no sent">28.57 ± 0.96 / 41.84 ± 0.40</td> <!-- NoReC -->
   <td class="no la">34.06 ± 1.03 / 66.03 ± 0.52</td> <!-- ScaLA-nb -->
   <td class="no la">31.33 ± 1.63 / 65.58 ± 0.81</td> <!-- ScaLA-nn -->
   <td class="no qa">34.66 ± 0.58 / 38.71 ± 0.59</td> <!-- ScandiQA-no -->
   <td class="sv ner">62.62 ± 0.67 / 69.75 ± 0.65</td> <!-- SUC3 -->
   <td class="sv sent">21.30 ± 1.68 / 47.41 ± 1.14</td> <!-- ABSAbank-Imm -->
   <td class="sv la">28.18 ± 1.00 / 63.08 ± 0.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.02 ± 0.57 / 47.21 ± 0.51</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">103822851</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23150</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">78.48 ± 0.73 / 80.67 ± 0.59</td> <!-- DaNE -->
   <td class="da sent">31.42 ± 1.03 / 50.84 ± 0.59</td> <!-- AngryTweets -->
   <td class="da la">20.72 ± 0.81 / 58.88 ± 0.39</td> <!-- ScaLA-da -->
   <td class="da qa">43.22 ± 0.47 / 47.24 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="no ner">84.32 ± 0.78 / 87.16 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">79.98 ± 0.68 / 83.38 ± 0.56</td> <!-- NorNE-nn -->
   <td class="no sent">31.19 ± 0.58 / 43.27 ± 0.31</td> <!-- NoReC -->
   <td class="no la">46.22 ± 0.71 / 72.05 ± 0.35</td> <!-- ScaLA-nb -->
   <td class="no la">32.93 ± 1.09 / 64.90 ± 0.56</td> <!-- ScaLA-nn -->
   <td class="no qa">48.05 ± 0.51 / 52.81 ± 0.54</td> <!-- ScandiQA-no -->
   <td class="sv ner">71.40 ± 0.88 / 77.72 ± 0.96</td> <!-- SUC3 -->
   <td class="sv sent">12.12 ± 1.56 / 33.44 ± 0.57</td> <!-- ABSAbank-Imm -->
   <td class="sv la">2.08 ± 1.30 / 50.91 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.35 ± 0.63 / 53.57 ± 0.58</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354039810</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">82.87 ± 0.48 / 85.14 ± 0.48</td> <!-- DaNE -->
   <td class="da sent">51.20 ± 0.59 / 67.43 ± 0.36</td> <!-- AngryTweets -->
   <td class="da la">72.33 ± 0.87 / 85.98 ± 0.44</td> <!-- ScaLA-da -->
   <td class="da qa">53.98 ± 0.46 / 59.22 ± 0.39</td> <!-- ScandiQA-da -->
   <td class="no ner">86.61 ± 0.53 / 90.76 ± 0.41</td> <!-- NorNE-nb -->
   <td class="no ner">84.98 ± 0.49 / 88.51 ± 0.42</td> <!-- NorNE-nn -->
   <td class="no sent">65.35 ± 0.99 / 76.89 ± 0.65</td> <!-- NoReC -->
   <td class="no la">79.48 ± 0.95 / 89.51 ± 0.46</td> <!-- ScaLA-nb -->
   <td class="no la">80.02 ± 0.69 / 89.83 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">53.81 ± 0.42 / 57.77 ± 0.40</td> <!-- ScandiQA-no -->
   <td class="sv ner">69.54 ± 0.65 / 76.27 ± 0.65</td> <!-- SUC3 -->
   <td class="sv sent">24.39 ± 1.65 / 49.59 ± 1.05</td> <!-- ABSAbank-Imm -->
   <td class="sv la">71.79 ± 0.81 / 85.13 ± 0.42</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.44 ± 0.54 / 60.63 ± 0.56</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">177855747</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">119547</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">84.17 ± 0.56 / 86.20 ± 0.54</td> <!-- DaNE -->
   <td class="da sent">47.31 ± 0.88 / 65.00 ± 0.60</td> <!-- AngryTweets -->
   <td class="da la">63.59 ± 1.07 / 80.62 ± 0.55</td> <!-- ScaLA-da -->
   <td class="da qa">46.57 ± 0.29 / 50.26 ± 0.29</td> <!-- ScandiQA-da -->
   <td class="no ner">89.96 ± 0.46 / 93.23 ± 0.35</td> <!-- NorNE-nb -->
   <td class="no ner">85.50 ± 0.51 / 89.20 ± 0.33</td> <!-- NorNE-nn -->
   <td class="no sent">60.45 ± 0.40 / 72.66 ± 0.28</td> <!-- NoReC -->
   <td class="no la">71.01 ± 0.70 / 83.91 ± 0.44</td> <!-- ScaLA-nb -->
   <td class="no la">74.58 ± 0.69 / 87.18 ± 0.36</td> <!-- ScaLA-nn -->
   <td class="no qa">41.73 ± 0.39 / 45.49 ± 0.41</td> <!-- ScandiQA-no -->
   <td class="sv ner">75.14 ± 0.92 / 79.75 ± 0.84</td> <!-- SUC3 -->
   <td class="sv sent">28.96 ± 1.08 / 53.94 ± 0.61</td> <!-- ABSAbank-Imm -->
   <td class="sv la">60.12 ± 0.88 / 78.76 ± 0.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.38 ± 0.32 / 46.92 ± 0.41</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278045955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.21 ± 0.54 / 82.31 ± 0.59</td> <!-- DaNE -->
   <td class="da sent">48.95 ± 0.91 / 66.18 ± 0.60</td> <!-- AngryTweets -->
   <td class="da la">62.38 ± 0.78 / 79.81 ± 0.47</td> <!-- ScaLA-da -->
   <td class="da qa">41.10 ± 0.49 / 46.04 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="no ner">88.29 ± 0.75 / 90.35 ± 0.62</td> <!-- NorNE-nb -->
   <td class="no ner">73.54 ± 0.88 / 78.17 ± 0.76</td> <!-- NorNE-nn -->
   <td class="no sent">55.17 ± 0.94 / 68.88 ± 0.71</td> <!-- NoReC -->
   <td class="no la">66.53 ± 0.62 / 81.59 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">50.11 ± 1.21 / 73.78 ± 0.72</td> <!-- ScaLA-nn -->
   <td class="no qa">41.59 ± 0.60 / 47.01 ± 0.61</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.67 ± 0.83 / 78.57 ± 0.71</td> <!-- SUC3 -->
   <td class="sv sent">28.65 ± 1.21 / 52.73 ± 0.77</td> <!-- ABSAbank-Imm -->
   <td class="sv la">67.41 ± 0.62 / 83.13 ± 0.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.05 ± 0.47 / 54.03 ± 0.52</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559893507</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">86.49 ± 0.33 / 88.24 ± 0.49</td> <!-- DaNE -->
   <td class="da sent">50.59 ± 0.77 / 66.07 ± 0.49</td> <!-- AngryTweets -->
   <td class="da la">72.30 ± 1.50 / 85.53 ± 0.79</td> <!-- ScaLA-da -->
   <td class="da qa">54.09 ± 0.43 / 59.08 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="no ner">88.87 ± 0.45 / 91.28 ± 0.42</td> <!-- NorNE-nb -->
   <td class="no ner">85.19 ± 0.68 / 88.36 ± 0.43</td> <!-- NorNE-nn -->
   <td class="no sent">62.78 ± 0.85 / 74.06 ± 0.74</td> <!-- NoReC -->
   <td class="no la">70.00 ± 0.98 / 84.38 ± 0.56</td> <!-- ScaLA-nb -->
   <td class="no la">61.60 ± 1.13 / 80.64 ± 0.58</td> <!-- ScaLA-nn -->
   <td class="no qa">49.76 ± 0.43 / 54.69 ± 0.44</td> <!-- ScandiQA-no -->
   <td class="sv ner">74.63 ± 0.80 / 81.69 ± 0.65</td> <!-- SUC3 -->
   <td class="sv sent">29.77 ± 1.41 / 53.98 ± 0.84</td> <!-- ABSAbank-Imm -->
   <td class="sv la">71.66 ± 0.64 / 85.75 ± 0.32</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.69 ± 0.67 / 59.64 ± 0.72</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13738755</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.57 ± 0.71 / 73.47 ± 0.68</td> <!-- DaNE -->
   <td class="da sent">37.04 ± 0.79 / 56.56 ± 0.57</td> <!-- AngryTweets -->
   <td class="da la">67.47 ± 1.29 / 82.99 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">64.48 ± 0.74 / 68.15 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">62.30 ± 0.87 / 66.23 ± 0.78</td> <!-- NorNE-nn -->
   <td class="no sent">28.59 ± 0.76 / 41.69 ± 0.30</td> <!-- NoReC -->
   <td class="no la">32.23 ± 1.35 / 64.05 ± 0.76</td> <!-- ScaLA-nb -->
   <td class="no la">19.64 ± 1.60 / 57.65 ± 0.77</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-no -->
   <td class="sv ner">55.96 ± 0.86 / 59.17 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">11.10 ± 0.89 / 33.92 ± 0.42</td> <!-- ABSAbank-Imm -->
   <td class="sv la">15.20 ± 1.09 / 57.16 ± 0.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">13738755</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32000</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">69.03 ± 0.62 / 72.66 ± 0.49</td> <!-- DaNE -->
   <td class="da sent">37.38 ± 1.07 / 57.06 ± 0.76</td> <!-- AngryTweets -->
   <td class="da la">65.76 ± 0.60 / 82.27 ± 0.30</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">48.51 ± 0.92 / 51.32 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">45.98 ± 0.58 / 49.03 ± 0.48</td> <!-- NorNE-nn -->
   <td class="no sent">31.84 ± 1.12 / 42.92 ± 0.47</td> <!-- NoReC -->
   <td class="no la">38.30 ± 1.37 / 69.01 ± 0.68</td> <!-- ScaLA-nb -->
   <td class="no la">18.69 ± 1.22 / 58.70 ± 0.62</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.04 ± 0.02</td> <!-- ScandiQA-no -->
   <td class="sv ner">39.59 ± 0.90 / 42.14 ± 0.97</td> <!-- SUC3 -->
   <td class="sv sent">11.56 ± 1.11 / 33.66 ± 0.53</td> <!-- ABSAbank-Imm -->
   <td class="sv la">19.97 ± 1.43 / 59.69 ± 0.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">2.35 ± 0.09 / 2.55 ± 0.09</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>flax-community/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">124647939</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50265</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">77.20 ± 0.51 / 79.89 ± 0.47</td> <!-- DaNE -->
   <td class="da sent">45.58 ± 0.85 / 63.65 ± 0.56</td> <!-- AngryTweets -->
   <td class="da la">3.02 ± 1.66 / 51.50 ± 0.83</td> <!-- ScaLA-da -->
   <td class="da qa">36.43 ± 0.41 / 40.06 ± 0.37</td> <!-- ScandiQA-da -->
   <td class="no ner">70.90 ± 0.50 / 74.33 ± 0.54</td> <!-- NorNE-nb -->
   <td class="no ner">63.67 ± 0.65 / 67.75 ± 0.55</td> <!-- NorNE-nn -->
   <td class="no sent">46.35 ± 0.96 / 62.83 ± 0.62</td> <!-- NoReC -->
   <td class="no la">0.17 ± 1.20 / 48.77 ± 0.58</td> <!-- ScaLA-nb -->
   <td class="no la">-0.77 ± 1.41 / 49.59 ± 0.70</td> <!-- ScaLA-nn -->
   <td class="no qa">33.98 ± 0.37 / 38.76 ± 0.45</td> <!-- ScandiQA-no -->
   <td class="sv ner">61.83 ± 0.70 / 65.68 ± 0.55</td> <!-- SUC3 -->
   <td class="sv sent">22.20 ± 0.80 / 49.06 ± 0.49</td> <!-- ABSAbank-Imm -->
   <td class="sv la">0.36 ± 1.05 / 41.18 ± 0.63</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.34 ± 0.55 / 39.79 ± 0.58</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">124693251</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50325</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">78.99 ± 0.92 / 82.18 ± 0.77</td> <!-- DaNE -->
   <td class="da sent">37.38 ± 0.97 / 57.60 ± 0.70</td> <!-- AngryTweets -->
   <td class="da la">12.43 ± 1.67 / 52.88 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da qa">33.34 ± 0.35 / 37.31 ± 0.32</td> <!-- ScandiQA-da -->
   <td class="no ner">83.44 ± 0.69 / 85.86 ± 0.67</td> <!-- NorNE-nb -->
   <td class="no ner">76.66 ± 0.79 / 80.15 ± 0.65</td> <!-- NorNE-nn -->
   <td class="no sent">38.33 ± 0.79 / 49.13 ± 0.63</td> <!-- NoReC -->
   <td class="no la">38.87 ± 1.39 / 65.56 ± 0.64</td> <!-- ScaLA-nb -->
   <td class="no la">-1.01 ± 1.68 / 49.05 ± 0.79</td> <!-- ScaLA-nn -->
   <td class="no qa">37.85 ± 0.63 / 41.88 ± 0.61</td> <!-- ScandiQA-no -->
   <td class="sv ner">76.49 ± 0.86 / 82.43 ± 0.75</td> <!-- SUC3 -->
   <td class="sv sent">31.48 ± 1.40 / 54.58 ± 0.90</td> <!-- ABSAbank-Imm -->
   <td class="sv la">80.14 ± 0.70 / 89.70 ± 0.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.10 ± 0.47 / 48.15 ± 0.44</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>vesteinn/ScandiBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124448259</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50005</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">83.53 ± 0.61 / 85.34 ± 0.84</td> <!-- DaNE -->
   <td class="da sent">46.81 ± 1.10 / 63.88 ± 0.71</td> <!-- AngryTweets -->
   <td class="da la">60.85 ± 0.86 / 79.33 ± 0.50</td> <!-- ScaLA-da -->
   <td class="da qa">41.48 ± 0.41 / 45.93 ± 0.44</td> <!-- ScandiQA-da -->
   <td class="no ner">89.71 ± 0.62 / 92.36 ± 0.57</td> <!-- NorNE-nb -->
   <td class="no ner">80.44 ± 0.92 / 84.44 ± 0.82</td> <!-- NorNE-nn -->
   <td class="no sent">46.12 ± 0.84 / 48.84 ± 0.35</td> <!-- NoReC -->
   <td class="no la">71.94 ± 0.99 / 85.51 ± 0.50</td> <!-- ScaLA-nb -->
   <td class="no la">58.38 ± 0.99 / 77.02 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">37.56 ± 0.43 / 42.19 ± 0.45</td> <!-- ScandiQA-no -->
   <td class="sv ner">72.28 ± 0.90 / 79.65 ± 0.80</td> <!-- SUC3 -->
   <td class="sv sent">33.02 ± 0.94 / 55.41 ± 0.56</td> <!-- ABSAbank-Imm -->
   <td class="sv la">70.41 ± 0.64 / 83.96 ± 0.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.07 ± 0.46 / 49.27 ± 0.42</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470929155</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501153</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">83.22 ± 0.51 / 84.45 ± 0.47</td> <!-- DaNE -->
   <td class="da sent">48.78 ± 0.64 / 66.17 ± 0.39</td> <!-- AngryTweets -->
   <td class="da la">54.32 ± 1.25 / 76.54 ± 0.69</td> <!-- ScaLA-da -->
   <td class="da qa">48.46 ± 0.43 / 52.84 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">86.59 ± 0.70 / 89.33 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">80.98 ± 0.62 / 84.73 ± 0.48</td> <!-- NorNE-nn -->
   <td class="no sent">54.13 ± 0.68 / 65.75 ± 0.61</td> <!-- NoReC -->
   <td class="no la">57.09 ± 1.15 / 78.11 ± 0.55</td> <!-- ScaLA-nb -->
   <td class="no la">50.63 ± 1.20 / 74.38 ± 0.65</td> <!-- ScaLA-nn -->
   <td class="no qa">53.29 ± 0.57 / 57.72 ± 0.50</td> <!-- ScandiQA-no -->
   <td class="sv ner">70.10 ± 0.90 / 77.76 ± 0.73</td> <!-- SUC3 -->
   <td class="sv sent">27.22 ± 1.15 / 51.01 ± 0.67</td> <!-- ABSAbank-Imm -->
   <td class="sv la">58.68 ± 1.13 / 77.23 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.17 ± 0.49 / 56.31 ± 0.57</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278045955</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250002</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.57 ± 0.68 / 82.26 ± 0.51</td> <!-- DaNE -->
   <td class="da sent">44.54 ± 0.86 / 62.87 ± 0.62</td> <!-- AngryTweets -->
   <td class="da la">51.22 ± 1.03 / 74.63 ± 0.49</td> <!-- ScaLA-da -->
   <td class="da qa">30.09 ± 0.23 / 34.08 ± 0.29</td> <!-- ScandiQA-da -->
   <td class="no ner">85.21 ± 0.68 / 87.40 ± 0.45</td> <!-- NorNE-nb -->
   <td class="no ner">79.32 ± 0.82 / 83.46 ± 0.60</td> <!-- NorNE-nn -->
   <td class="no sent">49.13 ± 0.90 / 64.13 ± 0.72</td> <!-- NoReC -->
   <td class="no la">54.29 ± 0.78 / 74.18 ± 0.34</td> <!-- ScaLA-nb -->
   <td class="no la">39.28 ± 1.35 / 69.06 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">32.83 ± 0.38 / 37.22 ± 0.40</td> <!-- ScandiQA-no -->
   <td class="sv ner">66.79 ± 0.88 / 74.25 ± 0.72</td> <!-- SUC3 -->
   <td class="sv sent">17.29 ± 0.69 / 42.44 ± 0.56</td> <!-- ABSAbank-Imm -->
   <td class="sv la">58.28 ± 1.00 / 77.76 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.84 ± 0.31 / 42.93 ± 0.31</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">21944195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96105</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">76.40 ± 0.74 / 79.03 ± 0.80</td> <!-- DaNE -->
   <td class="da sent">39.06 ± 0.95 / 58.93 ± 0.74</td> <!-- AngryTweets -->
   <td class="da la">64.73 ± 0.69 / 81.68 ± 0.42</td> <!-- ScaLA-da -->
   <td class="da qa">14.61 ± 0.37 / 15.58 ± 0.36</td> <!-- ScandiQA-da -->
   <td class="no ner">82.13 ± 0.70 / 85.40 ± 0.55</td> <!-- NorNE-nb -->
   <td class="no ner">77.41 ± 0.85 / 82.30 ± 0.64</td> <!-- NorNE-nn -->
   <td class="no sent">39.39 ± 0.90 / 46.03 ± 0.39</td> <!-- NoReC -->
   <td class="no la">71.16 ± 0.73 / 84.60 ± 0.42</td> <!-- ScaLA-nb -->
   <td class="no la">62.62 ± 0.97 / 80.87 ± 0.51</td> <!-- ScaLA-nn -->
   <td class="no qa">10.43 ± 0.27 / 11.18 ± 0.29</td> <!-- ScandiQA-no -->
   <td class="sv ner">64.32 ± 0.60 / 73.85 ± 0.46</td> <!-- SUC3 -->
   <td class="sv sent">18.34 ± 1.06 / 36.67 ± 0.53</td> <!-- ABSAbank-Imm -->
   <td class="sv la">69.19 ± 0.98 / 84.36 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv qa">25.51 ± 0.38 / 29.05 ± 0.38</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177855747</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">119547</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">81.34 ± 0.64 / 82.59 ± 0.60</td> <!-- DaNE -->
   <td class="da sent">35.81 ± 0.79 / 57.38 ± 0.53</td> <!-- AngryTweets -->
   <td class="da la">42.38 ± 1.10 / 70.36 ± 0.59</td> <!-- ScaLA-da -->
   <td class="da qa">44.87 ± 0.35 / 49.11 ± 0.33</td> <!-- ScandiQA-da -->
   <td class="no ner">88.30 ± 0.62 / 91.29 ± 0.50</td> <!-- NorNE-nb -->
   <td class="no ner">81.29 ± 0.68 / 84.30 ± 0.53</td> <!-- NorNE-nn -->
   <td class="no sent">36.11 ± 0.83 / 52.20 ± 0.55</td> <!-- NoReC -->
   <td class="no la">49.23 ± 1.20 / 73.79 ± 0.55</td> <!-- ScaLA-nb -->
   <td class="no la">37.93 ± 1.10 / 64.76 ± 0.67</td> <!-- ScaLA-nn -->
   <td class="no qa">43.45 ± 0.38 / 48.32 ± 0.46</td> <!-- ScandiQA-no -->
   <td class="sv ner">67.29 ± 0.73 / 72.57 ± 0.63</td> <!-- SUC3 -->
   <td class="sv sent">12.31 ± 0.96 / 39.88 ± 0.48</td> <!-- ABSAbank-Imm -->
   <td class="sv la">50.70 ± 0.79 / 73.40 ± 0.40</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.31 ± 0.68 / 52.19 ± 0.64</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>Geotrend/bert-base-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104014083</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23399</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">80.90 ± 0.62 / 83.44 ± 0.57</td> <!-- DaNE -->
   <td class="da sent">34.94 ± 0.77 / 56.17 ± 0.48</td> <!-- AngryTweets -->
   <td class="da la">34.45 ± 0.78 / 66.72 ± 0.39</td> <!-- ScaLA-da -->
   <td class="da qa">45.43 ± 0.36 / 50.21 ± 0.31</td> <!-- ScandiQA-da -->
   <td class="no ner">85.29 ± 0.60 / 88.53 ± 0.45</td> <!-- NorNE-nb -->
   <td class="no ner">81.55 ± 0.61 / 84.59 ± 0.50</td> <!-- NorNE-nn -->
   <td class="no sent">32.52 ± 0.69 / 44.86 ± 0.38</td> <!-- NoReC -->
   <td class="no la">50.06 ± 0.95 / 74.02 ± 0.43</td> <!-- ScaLA-nb -->
   <td class="no la">40.91 ± 0.93 / 70.22 ± 0.51</td> <!-- ScaLA-nn -->
   <td class="no qa">48.21 ± 0.48 / 52.42 ± 0.50</td> <!-- ScandiQA-no -->
   <td class="sv ner">68.99 ± 0.78 / 76.50 ± 0.82</td> <!-- SUC3 -->
   <td class="sv sent">12.10 ± 1.19 / 32.66 ± 0.65</td> <!-- ABSAbank-Imm -->
   <td class="sv la">44.22 ± 1.29 / 71.45 ± 0.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.91 ± 0.42 / 52.62 ± 0.42</td> <!-- ScandiQA-sv -->
  </tr>
  <tr>
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">369557507</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">78.42 ± 0.36 / 80.44 ± 0.40</td> <!-- DaNE -->
   <td class="da sent">36.99 ± 0.84 / 57.62 ± 0.52</td> <!-- AngryTweets -->
   <td class="da la">26.32 ± 1.24 / 59.45 ± 0.70</td> <!-- ScaLA-da -->
   <td class="da qa">44.48 ± 0.40 / 49.63 ± 0.35</td> <!-- ScandiQA-da -->
   <td class="no ner">82.74 ± 0.82 / 85.33 ± 0.75</td> <!-- NorNE-nb -->
   <td class="no ner">76.16 ± 0.72 / 79.27 ± 0.71</td> <!-- NorNE-nn -->
   <td class="no sent">37.40 ± 0.88 / 50.41 ± 0.59</td> <!-- NoReC -->
   <td class="no la">26.17 ± 1.38 / 63.04 ± 0.69</td> <!-- ScaLA-nb -->
   <td class="no la">23.16 ± 1.44 / 61.04 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no qa">45.16 ± 0.50 / 50.68 ± 0.52</td> <!-- ScandiQA-no -->
   <td class="sv ner">73.65 ± 1.14 / 80.03 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">31.78 ± 0.96 / 55.85 ± 0.63</td> <!-- ABSAbank-Imm -->
   <td class="sv la">76.16 ± 0.64 / 87.37 ± 0.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.80 ± 0.76 / 57.84 ± 0.65</td> <!-- ScandiQA-sv -->
  </tr>
 </tbody>
</table>
</div>