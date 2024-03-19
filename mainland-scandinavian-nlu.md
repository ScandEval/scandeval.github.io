---
layout: leaderboard
title: Mainland Scandinavian NLU
---

<center>Last updated: 19/03/2024 10:24:40 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="mainland-scandinavian-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish rank, computed as 1 + the average number of standard deviations from the best model">Danish Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian rank, computed as 1 + the average number of standard deviations from the best model">Norwegian Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish rank, computed as 1 + the average number of standard deviations from the best model">Swedish Rank</span></th>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version">Version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">1.12</td> <!-- ScandEval rank -->
   <td class="da-rank">1.20</td> <!-- Danish rank -->
   <td class="no-rank">1.00</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.17</td> <!-- Swedish rank -->
   <td class="da ner">74.16 ± 1.73 / 70.93 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">51.20 ± 1.67 / 66.62 ± 1.58</td> <!-- Angry Tweets -->
   <td class="da la">73.87 ± 2.13 / 86.61 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da qa">49.34 ± 1.14 / 55.06 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="no ner">92.01 ± 0.98 / 92.36 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">87.17 ± 1.24 / 88.75 ± 0.89</td> <!-- NorNE-nn -->
   <td class="no sent">60.11 ± 2.96 / 70.55 ± 3.99</td> <!-- NoReC -->
   <td class="no la">72.85 ± 5.60 / 85.73 ± 3.14</td> <!-- ScaLA-nb -->
   <td class="no la">65.56 ± 1.91 / 82.23 ± 0.97</td> <!-- ScaLA-nn -->
   <td class="no qa">60.38 ± 0.95 / 75.42 ± 1.16</td> <!-- NorQuAD -->
   <td class="sv ner">82.65 ± 1.04 / 80.43 ± 0.93</td> <!-- SUC3 -->
   <td class="sv sent">77.25 ± 1.20 / 73.96 ± 2.59</td> <!-- SweReC -->
   <td class="sv la">77.90 ± 1.45 / 88.63 ± 0.76</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.64 ± 1.11 / 55.64 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.12</td> <!-- ScandEval rank -->
   <td class="da-rank">1.20</td> <!-- Danish rank -->
   <td class="no-rank">1.00</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.17</td> <!-- Swedish rank -->
   <td class="da ner">75.22 ± 1.64 / 71.57 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">49.94 ± 3.25 / 65.66 ± 2.73</td> <!-- Angry Tweets -->
   <td class="da la">72.59 ± 1.38 / 85.58 ± 0.97</td> <!-- ScaLA-da -->
   <td class="da qa">48.97 ± 1.22 / 54.79 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">92.49 ± 0.81 / 92.58 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">87.22 ± 1.19 / 88.71 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">58.77 ± 3.69 / 69.56 ± 4.55</td> <!-- NoReC -->
   <td class="no la">76.30 ± 2.09 / 87.19 ± 1.40</td> <!-- ScaLA-nb -->
   <td class="no la">64.11 ± 5.18 / 80.68 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">60.69 ± 1.15 / 75.73 ± 1.06</td> <!-- NorQuAD -->
   <td class="sv ner">82.97 ± 0.98 / 81.14 ± 1.14</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 1.25 / 73.57 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">73.81 ± 4.60 / 86.33 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.50 ± 1.32 / 55.34 ± 1.33</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da-rank">2.17</td> <!-- Danish rank -->
   <td class="no-rank">2.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
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
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="da-rank">2.07</td> <!-- Danish rank -->
   <td class="no-rank">2.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da-rank">2.21</td> <!-- Danish rank -->
   <td class="no-rank">2.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.16</td> <!-- Swedish rank -->
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
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="da-rank">2.07</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da-rank">2.22</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
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
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da-rank">2.26</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.19</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.34</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da-rank">2.03</td> <!-- Danish rank -->
   <td class="no-rank">2.93</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
   <td class="da ner">51.08 ± 1.60 / 35.83 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">54.69 ± 0.99 / 69.50 ± 0.93</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 1.48 / 62.15 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da qa">56.56 ± 0.76 / 64.32 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="no ner">62.43 ± 0.94 / 51.64 ± 2.45</td> <!-- NorNE-nb -->
   <td class="no ner">60.68 ± 0.74 / 48.91 ± 2.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.41 ± 1.46 / 69.49 ± 1.05</td> <!-- NoReC -->
   <td class="no la">-1.16 ± 1.31 / 33.56 ± 0.43</td> <!-- ScaLA-nb -->
   <td class="no la">0.30 ± 0.71 / 34.08 ± 0.32</td> <!-- ScaLA-nn -->
   <td class="no qa">49.15 ± 2.79 / 76.77 ± 1.59</td> <!-- NorQuAD -->
   <td class="sv ner">54.37 ± 3.04 / 42.16 ± 4.00</td> <!-- SUC3 -->
   <td class="sv sent">75.98 ± 1.15 / 74.44 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">17.98 ± 1.97 / 56.01 ± 2.08</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.07 ± 0.74 / 64.24 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>12.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da-rank">2.23</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
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
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.31</td> <!-- Danish rank -->
   <td class="no-rank">2.98</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
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
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">2.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.39</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.29</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.53</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.53</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da-rank">2.43</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.35</td> <!-- Swedish rank -->
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
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,505 ± 465 / 774 ± 242</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da-rank">2.52</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da-rank">2.52</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.30</td> <!-- Swedish rank -->
   <td class="da ner">40.14 ± 2.41 / 28.08 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">39.38 ± 1.56 / 49.16 ± 2.84</td> <!-- Angry Tweets -->
   <td class="da la">21.85 ± 3.24 / 53.75 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da qa">58.07 ± 1.13 / 63.63 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="no ner">50.10 ± 2.16 / 41.80 ± 2.77</td> <!-- NorNE-nb -->
   <td class="no ner">54.81 ± 1.88 / 45.95 ± 3.21</td> <!-- NorNE-nn -->
   <td class="no sent">48.64 ± 2.14 / 66.06 ± 1.47</td> <!-- NoReC -->
   <td class="no la">10.31 ± 3.46 / 43.68 ± 5.10</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.48 / 36.52 ± 2.31</td> <!-- ScaLA-nn -->
   <td class="no qa">42.20 ± 3.02 / 65.18 ± 2.86</td> <!-- NorQuAD -->
   <td class="sv ner">48.43 ± 2.75 / 35.31 ± 2.80</td> <!-- SUC3 -->
   <td class="sv sent">79.43 ± 0.85 / 78.21 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">17.37 ± 2.57 / 52.91 ± 4.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.05 ± 1.22 / 62.72 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.71</td> <!-- Swedish rank -->
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
   <td>9.3.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da-rank">2.79</td> <!-- Danish rank -->
   <td class="no-rank">2.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.52</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.52</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.58</td> <!-- Danish rank -->
   <td class="no-rank">3.10</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.56</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">3.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.72</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.62</td> <!-- Swedish rank -->
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
   <td>9.1.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.55</td> <!-- Danish rank -->
   <td class="no-rank">3.30</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.60</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="da-rank">2.77</td> <!-- Danish rank -->
   <td class="no-rank">3.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.68</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="da-rank">3.02</td> <!-- Danish rank -->
   <td class="no-rank">3.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.64</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="da-rank">2.79</td> <!-- Danish rank -->
   <td class="no-rank">3.32</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.81</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="da-rank">2.93</td> <!-- Danish rank -->
   <td class="no-rank">3.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
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
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">3.47</td> <!-- Danish rank -->
   <td class="no-rank">3.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.67</td> <!-- Swedish rank -->
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
   <td>10.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.73</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="da-rank">3.39</td> <!-- Danish rank -->
   <td class="no-rank">3.59</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.99</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.30</td> <!-- Danish rank -->
   <td class="no-rank">3.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.08</td> <!-- Swedish rank -->
   <td class="da ner">0.23 ± 0.17 / 0.52 ± 0.39</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="no ner">0.17 ± 0.11 / 0.24 ± 0.18</td> <!-- NorNE-nb -->
   <td class="no ner">0.14 ± 0.11 / 0.12 ± 0.10</td> <!-- NorNE-nn -->
   <td class="no sent">44.95 ± 3.19 / 61.88 ± 2.88</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td class="sv ner">0.11 ± 0.14 / 0.13 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="da-rank">3.24</td> <!-- Danish rank -->
   <td class="no-rank">3.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.26</td> <!-- Swedish rank -->
   <td class="da ner">0.25 ± 0.26 / 0.31 ± 0.26</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da qa">53.69 ± 0.94 / 59.72 ± 0.87</td> <!-- ScandiQA-da -->
   <td class="no ner">0.01 ± 0.02 / 0.03 ± 0.03</td> <!-- NorNE-nb -->
   <td class="no ner">0.09 ± 0.09 / 0.08 ± 0.08</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.59 / 45.73 ± 2.82</td> <!-- NoReC -->
   <td class="no la">3.57 ± 1.55 / 37.05 ± 2.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.61 ± 2.11 / 37.85 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="da-rank">3.44</td> <!-- Danish rank -->
   <td class="no-rank">3.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.18</td> <!-- Swedish rank -->
   <td class="da ner">18.23 ± 5.87 / 14.77 ± 3.36</td> <!-- DANSK -->
   <td class="da sent">22.71 ± 5.21 / 35.11 ± 6.59</td> <!-- Angry Tweets -->
   <td class="da la">5.03 ± 2.51 / 49.00 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da qa">49.11 ± 1.16 / 55.56 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="no ner">22.35 ± 7.84 / 23.89 ± 4.74</td> <!-- NorNE-nb -->
   <td class="no ner">21.98 ± 7.52 / 27.22 ± 4.97</td> <!-- NorNE-nn -->
   <td class="no sent">18.23 ± 9.28 / 38.93 ± 6.44</td> <!-- NoReC -->
   <td class="no la">1.68 ± 1.35 / 39.93 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">2.49 ± 1.88 / 40.26 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no qa">41.80 ± 3.14 / 64.25 ± 3.13</td> <!-- NorQuAD -->
   <td class="sv ner">18.83 ± 6.41 / 17.59 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">53.68 ± 10.39 / 58.92 ± 10.87</td> <!-- SweReC -->
   <td class="sv la">3.49 ± 2.20 / 46.13 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.81 ± 0.70 / 55.99 ± 0.69</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="da-rank">3.72</td> <!-- Danish rank -->
   <td class="no-rank">3.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.21</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="da-rank">3.39</td> <!-- Danish rank -->
   <td class="no-rank">4.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.17</td> <!-- Swedish rank -->
   <td class="da ner">2.44 ± 0.61 / 1.99 ± 0.48</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">0.02 ± 0.03 / 0.01 ± 0.03</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.89 ± 1.65 / 42.58 ± 3.16</td> <!-- NoReC -->
   <td class="no la">1.18 ± 1.00 / 33.34 ± 0.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td class="sv ner">0.11 ± 0.10 / 0.10 ± 0.09</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="da-rank">3.62</td> <!-- Danish rank -->
   <td class="no-rank">3.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.25</td> <!-- Swedish rank -->
   <td class="da ner">3.23 ± 0.74 / 2.88 ± 0.65</td> <!-- DANSK -->
   <td class="da sent">27.14 ± 1.93 / 42.34 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">2.65 ± 1.66 / 40.63 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">46.43 ± 0.60 / 54.21 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="no ner">2.61 ± 0.80 / 2.80 ± 0.78</td> <!-- NorNE-nb -->
   <td class="no ner">1.47 ± 0.38 / 1.58 ± 0.33</td> <!-- NorNE-nn -->
   <td class="no sent">35.58 ± 2.13 / 44.49 ± 2.52</td> <!-- NoReC -->
   <td class="no la">0.82 ± 1.46 / 34.78 ± 1.54</td> <!-- ScaLA-nb -->
   <td class="no la">1.43 ± 1.70 / 34.19 ± 1.10</td> <!-- ScaLA-nn -->
   <td class="no qa">36.07 ± 1.78 / 58.70 ± 1.65</td> <!-- NorQuAD -->
   <td class="sv ner">1.35 ± 0.51 / 1.30 ± 0.43</td> <!-- SUC3 -->
   <td class="sv sent">73.34 ± 1.34 / 68.41 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.90 ± 1.74 / 44.43 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.45 ± 0.58 / 54.69 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="da-rank">3.56</td> <!-- Danish rank -->
   <td class="no-rank">3.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.31</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="da-rank">3.50</td> <!-- Danish rank -->
   <td class="no-rank">4.00</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.35</td> <!-- Swedish rank -->
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
   <td>10.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="da-rank">3.59</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.40</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="da-rank">3.33</td> <!-- Danish rank -->
   <td class="no-rank">3.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.90</td> <!-- Swedish rank -->
   <td class="da ner">0.15 ± 0.19 / 0.23 ± 0.22</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da qa">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">0.07 ± 0.08 / 0.08 ± 0.07</td> <!-- NorNE-nb -->
   <td class="no ner">0.04 ± 0.03 / 0.03 ± 0.03</td> <!-- NorNE-nn -->
   <td class="no sent">36.97 ± 1.94 / 55.08 ± 2.30</td> <!-- NoReC -->
   <td class="no la">5.27 ± 3.31 / 40.91 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">1.40 ± 1.87 / 33.64 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no qa">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="da-rank">3.62</td> <!-- Danish rank -->
   <td class="no-rank">3.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.65</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="da-rank">3.69</td> <!-- Danish rank -->
   <td class="no-rank">4.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.70</td> <!-- Swedish rank -->
   <td class="da ner">2.58 ± 0.59 / 2.33 ± 0.49</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 3.80 / 49.66 ± 3.96</td> <!-- Angry Tweets -->
   <td class="da la">2.08 ± 1.48 / 45.41 ± 3.83</td> <!-- ScaLA-da -->
   <td class="da qa">36.58 ± 1.41 / 42.02 ± 1.46</td> <!-- ScandiQA-da -->
   <td class="no ner">0.40 ± 0.38 / 0.51 ± 0.37</td> <!-- NorNE-nb -->
   <td class="no ner">0.59 ± 0.37 / 0.62 ± 0.44</td> <!-- NorNE-nn -->
   <td class="no sent">30.88 ± 2.75 / 46.07 ± 3.07</td> <!-- NoReC -->
   <td class="no la">-0.30 ± 1.46 / 34.93 ± 1.25</td> <!-- ScaLA-nb -->
   <td class="no la">0.45 ± 0.57 / 33.74 ± 1.25</td> <!-- ScaLA-nn -->
   <td class="no qa">23.97 ± 1.58 / 42.67 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">0.46 ± 0.71 / 0.41 ± 0.62</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 3.60 / 54.09 ± 1.46</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.21 / 34.76 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.33 ± 1.36 / 40.39 ± 1.53</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="da-rank">3.61</td> <!-- Danish rank -->
   <td class="no-rank">4.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.80</td> <!-- Swedish rank -->
   <td class="da ner">2.41 ± 0.60 / 2.54 ± 0.42</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da qa">42.19 ± 1.15 / 49.79 ± 1.17</td> <!-- ScandiQA-da -->
   <td class="no ner">0.78 ± 0.71 / 0.73 ± 0.68</td> <!-- NorNE-nb -->
   <td class="no ner">0.56 ± 0.59 / 0.52 ± 0.56</td> <!-- NorNE-nn -->
   <td class="no sent">22.01 ± 3.00 / 40.48 ± 2.81</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.35 / 44.34 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">1.45 ± 1.35 / 39.55 ± 3.53</td> <!-- ScaLA-nn -->
   <td class="no qa">32.37 ± 1.70 / 56.60 ± 0.99</td> <!-- NorQuAD -->
   <td class="sv ner">0.49 ± 0.91 / 0.45 ± 0.83</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.43 ± 1.04 / 47.27 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="da-rank">4.01</td> <!-- Danish rank -->
   <td class="no-rank">4.20</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.36</td> <!-- Swedish rank -->
   <td class="da ner">0.44 ± 0.27 / 0.86 ± 0.59</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">7.28 ± 1.41 / 27.33 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="no ner">0.14 ± 0.11 / 0.15 ± 0.12</td> <!-- NorNE-nb -->
   <td class="no ner">0.09 ± 0.09 / 0.09 ± 0.07</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 3.40 / 62.00 ± 2.71</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">12.16 ± 3.31 / 46.85 ± 3.89</td> <!-- NorQuAD -->
   <td class="sv ner">0.04 ± 0.07 / 0.07 ± 0.10</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.42 ± 3.74 / 49.00 ± 2.78</td> <!-- ScandiQA-sv -->
   <td>12.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.87</td> <!-- ScandEval rank -->
   <td class="da-rank">3.68</td> <!-- Danish rank -->
   <td class="no-rank">4.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.58</td> <!-- Swedish rank -->
   <td class="da ner">0.30 ± 0.51 / 0.28 ± 0.47</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">0.01 ± 0.02 / 0.01 ± 0.01</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">22.82 ± 3.11 / 43.88 ± 3.10</td> <!-- NoReC -->
   <td class="no la">2.70 ± 2.16 / 47.68 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">2.21 ± 1.46 / 42.80 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td class="sv ner">0.12 ± 0.23 / 0.10 ± 0.20</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="da-rank">3.75</td> <!-- Danish rank -->
   <td class="no-rank">4.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.64</td> <!-- Swedish rank -->
   <td class="da ner">0.37 ± 0.33 / 0.46 ± 0.40</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da qa">41.68 ± 1.45 / 49.38 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">0.36 ± 0.31 / 0.32 ± 0.28</td> <!-- NorNE-nb -->
   <td class="no ner">0.30 ± 0.21 / 0.26 ± 0.18</td> <!-- NorNE-nn -->
   <td class="no sent">19.85 ± 1.97 / 35.75 ± 1.74</td> <!-- NoReC -->
   <td class="no la">1.96 ± 1.33 / 44.22 ± 2.93</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.39 / 39.57 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no qa">16.36 ± 2.18 / 31.09 ± 3.42</td> <!-- NorQuAD -->
   <td class="sv ner">0.40 ± 0.38 / 0.40 ± 0.35</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.49 ± 1.13 / 50.43 ± 1.47</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="da-rank">3.74</td> <!-- Danish rank -->
   <td class="no-rank">4.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.79</td> <!-- Swedish rank -->
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
   <td>9.1.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="da-rank">4.14</td> <!-- Danish rank -->
   <td class="no-rank">4.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.58</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="da-rank">4.06</td> <!-- Danish rank -->
   <td class="no-rank">4.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.94</td> <!-- Swedish rank -->
   <td class="da ner">1.20 ± 0.63 / 1.86 ± 0.71</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da qa">34.52 ± 0.94 / 40.30 ± 1.00</td> <!-- ScandiQA-da -->
   <td class="no ner">1.06 ± 0.42 / 1.12 ± 0.37</td> <!-- NorNE-nb -->
   <td class="no ner">0.81 ± 0.34 / 0.88 ± 0.34</td> <!-- NorNE-nn -->
   <td class="no sent">11.49 ± 1.38 / 27.12 ± 1.98</td> <!-- NoReC -->
   <td class="no la">0.29 ± 1.58 / 40.21 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">-0.12 ± 1.48 / 39.92 ± 3.90</td> <!-- ScaLA-nn -->
   <td class="no qa">7.73 ± 1.17 / 17.00 ± 2.71</td> <!-- NorQuAD -->
   <td class="sv ner">0.24 ± 0.22 / 0.24 ± 0.19</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.46 ± 2.47 / 35.02 ± 2.70</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="da-rank">4.25</td> <!-- Danish rank -->
   <td class="no-rank">4.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.15</td> <!-- Swedish rank -->
   <td class="da ner">13.98 ± 1.54 / 13.46 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">6.37 ± 3.38 / 25.43 ± 4.09</td> <!-- Angry Tweets -->
   <td class="da la">0.41 ± 0.80 / 33.31 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">20.48 ± 2.90 / 24.30 ± 3.23</td> <!-- ScandiQA-da -->
   <td class="no ner">27.66 ± 2.00 / 28.61 ± 2.15</td> <!-- NorNE-nb -->
   <td class="no ner">30.88 ± 2.13 / 31.97 ± 2.10</td> <!-- NorNE-nn -->
   <td class="no sent">5.13 ± 3.33 / 20.41 ± 3.12</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">7.54 ± 1.19 / 15.63 ± 2.65</td> <!-- NorQuAD -->
   <td class="sv ner">23.05 ± 2.31 / 24.35 ± 1.99</td> <!-- SUC3 -->
   <td class="sv sent">12.47 ± 7.10 / 23.03 ± 8.78</td> <!-- SweReC -->
   <td class="sv la">0.08 ± 0.16 / 33.34 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.46 ± 2.67 / 24.29 ± 2.63</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="da-rank">4.24</td> <!-- Danish rank -->
   <td class="no-rank">4.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.16</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="da-rank">4.10</td> <!-- Danish rank -->
   <td class="no-rank">4.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.09</td> <!-- Swedish rank -->
   <td class="da ner">1.56 ± 0.59 / 1.80 ± 0.53</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="no ner">1.05 ± 0.61 / 1.02 ± 0.58</td> <!-- NorNE-nb -->
   <td class="no ner">1.37 ± 0.67 / 1.41 ± 0.70</td> <!-- NorNE-nn -->
   <td class="no sent">6.31 ± 3.46 / 20.67 ± 2.69</td> <!-- NoReC -->
   <td class="no la">-1.59 ± 1.08 / 36.27 ± 3.71</td> <!-- ScaLA-nb -->
   <td class="no la">0.61 ± 1.41 / 38.84 ± 5.10</td> <!-- ScaLA-nn -->
   <td class="no qa">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td class="sv ner">0.56 ± 0.34 / 0.75 ± 0.40</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="da-rank">4.11</td> <!-- Danish rank -->
   <td class="no-rank">4.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.05</td> <!-- Swedish rank -->
   <td class="da ner">2.02 ± 1.31 / 1.91 ± 1.18</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da qa">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td class="no ner">2.22 ± 1.76 / 2.35 ± 1.75</td> <!-- NorNE-nb -->
   <td class="no ner">0.99 ± 0.56 / 1.01 ± 0.52</td> <!-- NorNE-nn -->
   <td class="no sent">9.95 ± 3.92 / 29.01 ± 2.80</td> <!-- NoReC -->
   <td class="no la">-0.95 ± 1.87 / 39.37 ± 3.33</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 1.73 / 42.36 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">1.51 ± 0.79 / 1.42 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.52</td> <!-- ScandEval rank -->
   <td class="da-rank">4.50</td> <!-- Danish rank -->
   <td class="no-rank">4.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.35</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.62</td> <!-- ScandEval rank -->
   <td class="da-rank">4.47</td> <!-- Danish rank -->
   <td class="no-rank">4.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.55</td> <!-- Swedish rank -->
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
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.70</td> <!-- ScandEval rank -->
   <td class="da-rank">4.62</td> <!-- Danish rank -->
   <td class="no-rank">5.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.46</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="da-rank">4.72</td> <!-- Danish rank -->
   <td class="no-rank">5.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.46</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.80</td> <!-- ScandEval rank -->
   <td class="da-rank">4.74</td> <!-- Danish rank -->
   <td class="no-rank">4.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.75</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="da-rank">4.79</td> <!-- Danish rank -->
   <td class="no-rank">5.04</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.69</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Mainland Scandinavian NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-eFFRi&quot; src=&quot;https://datawrapper.dwcdn.net/eFFRi/10/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
