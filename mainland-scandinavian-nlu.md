---
layout: leaderboard
title: Mainland Scandinavian NLU 🇩🇰🇳🇴🇸🇪
---

<center>Last updated: 25/07/2024 22:32:33 CET</center>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Danish tasks">Danish Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Norwegian tasks">Norwegian Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Swedish tasks">Swedish Rank</span></th>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on DANSK">DANSK version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Angry Tweets">Angry Tweets version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-da">ScaLA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-da">ScandiQA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nb">NorNE-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nn">NorNE-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NoReC">NoReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nb">ScaLA-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nn">ScaLA-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorQuAD">NorQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SUC3">SUC3 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweReC">SweReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-sv">ScaLA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-sv">ScandiQA-sv version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.33</td> <!-- ScandEval rank -->
   <td class="da-rank">1.24</td> <!-- Danish rank -->
   <td class="no-rank">1.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.28</td> <!-- Swedish rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">56.43 ± 2.98 / 68.46 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">47.50 ± 2.86 / 75.24 ± 1.32</td> <!-- NorQuAD -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">1.35</td> <!-- ScandEval rank -->
   <td class="da-rank">1.37</td> <!-- Danish rank -->
   <td class="no-rank">1.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.33</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="rank">1.37</td> <!-- ScandEval rank -->
   <td class="da-rank">1.51</td> <!-- Danish rank -->
   <td class="no-rank">1.10</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.50</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.38</td> <!-- ScandEval rank -->
   <td class="da-rank">1.43</td> <!-- Danish rank -->
   <td class="no-rank">1.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.35</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.41</td> <!-- ScandEval rank -->
   <td class="da-rank">1.26</td> <!-- Danish rank -->
   <td class="no-rank">1.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.36</td> <!-- Swedish rank -->
   <td class="da ner">66.80 ± 3.01 / 45.69 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">61.62 ± 2.17 / 73.99 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">66.84 ± 3.27 / 82.79 ± 1.86</td> <!-- ScaLA-da -->
   <td class="da qa">56.85 ± 2.62 / 68.83 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="no ner">77.48 ± 2.32 / 55.87 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">78.70 ± 2.78 / 57.58 ± 4.23</td> <!-- NorNE-nn -->
   <td class="no sent">62.55 ± 2.82 / 72.41 ± 2.42</td> <!-- NoReC -->
   <td class="no la">74.45 ± 4.27 / 86.22 ± 2.49</td> <!-- ScaLA-nb -->
   <td class="no la">56.31 ± 5.81 / 74.04 ± 4.03</td> <!-- ScaLA-nn -->
   <td class="no qa">44.67 ± 3.23 / 73.39 ± 1.83</td> <!-- NorQuAD -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.2</td> <!-- NoReC version -->
   <td>12.10.2</td> <!-- ScaLA-nb version -->
   <td>12.10.2</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.43</td> <!-- ScandEval rank -->
   <td class="da-rank">1.40</td> <!-- Danish rank -->
   <td class="no-rank">1.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.32</td> <!-- Swedish rank -->
   <td class="da ner">63.62 ± 3.74 / 53.29 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">60.19 ± 3.31 / 73.13 ± 2.17</td> <!-- Angry Tweets -->
   <td class="da la">50.07 ± 5.86 / 72.94 ± 4.16</td> <!-- ScaLA-da -->
   <td class="da qa">60.97 ± 2.76 / 66.71 ± 2.27</td> <!-- ScandiQA-da -->
   <td class="no ner">75.31 ± 3.84 / 64.90 ± 4.05</td> <!-- NorNE-nb -->
   <td class="no ner">75.94 ± 4.62 / 62.81 ± 5.25</td> <!-- NorNE-nn -->
   <td class="no sent">66.74 ± 4.50 / 74.89 ± 3.69</td> <!-- NoReC -->
   <td class="no la">59.82 ± 3.52 / 79.17 ± 2.10</td> <!-- ScaLA-nb -->
   <td class="no la">47.56 ± 3.52 / 71.91 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">60.87 ± 4.82 / 82.30 ± 2.52</td> <!-- NorQuAD -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.48</td> <!-- ScandEval rank -->
   <td class="da-rank">1.44</td> <!-- Danish rank -->
   <td class="no-rank">1.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.35</td> <!-- Swedish rank -->
   <td class="da ner">71.15 ± 2.89 / 52.24 ± 3.76</td> <!-- DANSK -->
   <td class="da sent">49.42 ± 3.29 / 61.74 ± 2.59</td> <!-- Angry Tweets -->
   <td class="da la">64.59 ± 2.97 / 79.93 ± 1.88</td> <!-- ScaLA-da -->
   <td class="da qa">57.35 ± 2.51 / 67.87 ± 1.75</td> <!-- ScandiQA-da -->
   <td class="no ner">79.07 ± 3.01 / 64.17 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">81.56 ± 2.45 / 64.06 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">66.66 ± 1.91 / 77.70 ± 1.29</td> <!-- NoReC -->
   <td class="no la">64.53 ± 6.09 / 79.17 ± 4.89</td> <!-- ScaLA-nb -->
   <td class="no la">54.70 ± 4.36 / 74.94 ± 3.26</td> <!-- ScaLA-nn -->
   <td class="no qa">43.51 ± 3.40 / 74.52 ± 1.79</td> <!-- NorQuAD -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.2</td> <!-- NoReC version -->
   <td>12.10.2</td> <!-- ScaLA-nb version -->
   <td>12.10.2</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
   <td class="da-rank">1.38</td> <!-- Danish rank -->
   <td class="no-rank">1.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.64</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="da-rank">1.37</td> <!-- Danish rank -->
   <td class="no-rank">1.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.67</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="da-rank">1.37</td> <!-- Danish rank -->
   <td class="no-rank">1.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.72</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="da-rank">1.59</td> <!-- Danish rank -->
   <td class="no-rank">1.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.51</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.61</td> <!-- ScandEval rank -->
   <td class="da-rank">1.61</td> <!-- Danish rank -->
   <td class="no-rank">1.70</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.51</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="da-rank">1.70</td> <!-- Danish rank -->
   <td class="no-rank">1.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.65</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="da-rank">1.71</td> <!-- Danish rank -->
   <td class="no-rank">1.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.53</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="da-rank">1.78</td> <!-- Danish rank -->
   <td class="no-rank">1.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.67</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="da-rank">1.87</td> <!-- Danish rank -->
   <td class="no-rank">1.31</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.79</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,231 ± 8,171 / 4,863 ± 1,598</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="da-rank">1.81</td> <!-- Danish rank -->
   <td class="no-rank">1.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.60</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="da-rank">1.73</td> <!-- Danish rank -->
   <td class="no-rank">1.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.69</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="da-rank">1.71</td> <!-- Danish rank -->
   <td class="no-rank">1.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.74</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="da-rank">1.60</td> <!-- Danish rank -->
   <td class="no-rank">2.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.58</td> <!-- Swedish rank -->
   <td class="da ner">61.31 ± 2.34 / 49.86 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">52.52 ± 2.05 / 68.10 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">57.63 ± 2.80 / 77.01 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da qa">57.03 ± 1.95 / 65.51 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">45.35 ± 2.97 / 73.47 ± 1.69</td> <!-- NorQuAD -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">1.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.66</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="da-rank">1.79</td> <!-- Danish rank -->
   <td class="no-rank">1.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.78</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">837 ± 294 / 126 ± 43</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="da-rank">1.67</td> <!-- Danish rank -->
   <td class="no-rank">2.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.57</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="da-rank">1.81</td> <!-- Danish rank -->
   <td class="no-rank">1.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.79</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">1.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.75</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,314 ± 1,202 / 776 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="da-rank">1.42</td> <!-- Danish rank -->
   <td class="no-rank">2.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.07</td> <!-- Swedish rank -->
   <td class="da ner">58.44 ± 1.72 / 46.94 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">54.96 ± 1.30 / 68.41 ± 1.45</td> <!-- Angry Tweets -->
   <td class="da la">70.55 ± 1.00 / 85.14 ± 0.52</td> <!-- ScaLA-da -->
   <td class="da qa">60.95 ± 0.31 / 65.86 ± 0.36</td> <!-- ScandiQA-da -->
   <td class="no ner">85.07 ± 0.60 / 84.47 ± 0.48</td> <!-- NorNE-nb -->
   <td class="no ner">81.43 ± 0.59 / 79.70 ± 0.68</td> <!-- NorNE-nn -->
   <td class="no sent">38.52 ± 2.49 / 53.36 ± 2.80</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">40.52 ± 2.89 / 66.67 ± 3.21</td> <!-- NorQuAD -->
   <td class="sv ner">88.78 ± 1.05 / 85.30 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">81.73 ± 0.71 / 80.87 ± 0.96</td> <!-- SweReC -->
   <td class="sv la">75.83 ± 0.49 / 87.67 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">61.35 ± 0.70 / 65.90 ± 0.55</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-sbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,757 ± 3,883 / 3,864 ± 1,237</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="da-rank">1.81</td> <!-- Danish rank -->
   <td class="no-rank">1.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.82</td> <!-- Swedish rank -->
   <td class="da ner">70.12 ± 1.61 / 65.80 ± 1.43</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.05 / 65.23 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">63.25 ± 2.38 / 80.82 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da qa">36.51 ± 2.05 / 41.01 ± 2.35</td> <!-- ScandiQA-da -->
   <td class="no ner">90.96 ± 0.66 / 90.87 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">87.34 ± 1.74 / 88.75 ± 1.38</td> <!-- NorNE-nn -->
   <td class="no sent">60.57 ± 1.22 / 72.70 ± 0.75</td> <!-- NoReC -->
   <td class="no la">72.11 ± 1.85 / 85.08 ± 1.24</td> <!-- ScaLA-nb -->
   <td class="no la">70.20 ± 2.24 / 84.26 ± 1.48</td> <!-- ScaLA-nn -->
   <td class="no qa">29.94 ± 3.33 / 40.55 ± 4.21</td> <!-- NorQuAD -->
   <td class="sv ner">80.26 ± 1.10 / 77.87 ± 1.03</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 0.75 / 69.24 ± 2.39</td> <!-- SweReC -->
   <td class="sv la">62.49 ± 2.06 / 80.42 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.80 ± 1.33 / 38.28 ± 1.45</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- ScaLA-nb version -->
   <td>12.10.5</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="da-rank">1.86</td> <!-- Danish rank -->
   <td class="no-rank">1.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.87</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">1.81</td> <!-- ScandEval rank -->
   <td class="da-rank">1.86</td> <!-- Danish rank -->
   <td class="no-rank">1.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.72</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">1.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.82</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="da-rank">1.99</td> <!-- Danish rank -->
   <td class="no-rank">1.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.86</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.88</td> <!-- ScandEval rank -->
   <td class="da-rank">1.72</td> <!-- Danish rank -->
   <td class="no-rank">2.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.70</td> <!-- Swedish rank -->
   <td class="da ner">58.06 ± 2.48 / 50.10 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">53.24 ± 4.04 / 67.81 ± 2.74</td> <!-- Angry Tweets -->
   <td class="da la">39.71 ± 4.96 / 65.90 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">62.51 ± 1.48 / 67.47 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="no ner">62.46 ± 4.62 / 60.77 ± 4.36</td> <!-- NorNE-nb -->
   <td class="no ner">64.68 ± 3.04 / 61.69 ± 2.31</td> <!-- NorNE-nn -->
   <td class="no sent">59.68 ± 3.30 / 70.62 ± 3.08</td> <!-- NoReC -->
   <td class="no la">27.34 ± 12.20 / 50.42 ± 9.24</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 4.66 / 36.08 ± 3.27</td> <!-- ScaLA-nn -->
   <td class="no qa">57.44 ± 4.59 / 78.69 ± 3.09</td> <!-- NorQuAD -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv qa">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="da-rank">1.77</td> <!-- Danish rank -->
   <td class="no-rank">2.22</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.72</td> <!-- Swedish rank -->
   <td class="da ner">56.96 ± 2.39 / 45.84 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">55.11 ± 4.11 / 69.60 ± 2.69</td> <!-- Angry Tweets -->
   <td class="da la">42.64 ± 3.22 / 71.04 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">54.58 ± 2.19 / 64.12 ± 1.41</td> <!-- ScandiQA-da -->
   <td class="no ner">66.75 ± 2.07 / 58.61 ± 3.33</td> <!-- NorNE-nb -->
   <td class="no ner">66.81 ± 2.57 / 57.71 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">60.58 ± 4.96 / 70.33 ± 4.12</td> <!-- NoReC -->
   <td class="no la">47.53 ± 4.07 / 72.24 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">17.14 ± 4.72 / 51.14 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">41.92 ± 3.36 / 72.51 ± 1.91</td> <!-- NorQuAD -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="da-rank">2.14</td> <!-- Danish rank -->
   <td class="no-rank">2.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.49</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="da-rank">1.79</td> <!-- Danish rank -->
   <td class="no-rank">2.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="da ner">63.10 ± 2.12 / 55.10 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">53.09 ± 3.85 / 68.18 ± 2.27</td> <!-- Angry Tweets -->
   <td class="da la">40.98 ± 4.46 / 69.10 ± 2.72</td> <!-- ScaLA-da -->
   <td class="da qa">51.13 ± 1.89 / 63.12 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">80.50 ± 2.85 / 76.71 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">76.47 ± 3.13 / 73.94 ± 2.95</td> <!-- NorNE-nn -->
   <td class="no sent">59.29 ± 5.92 / 69.99 ± 4.80</td> <!-- NoReC -->
   <td class="no la">47.28 ± 3.57 / 69.23 ± 3.04</td> <!-- ScaLA-nb -->
   <td class="no la">32.76 ± 3.80 / 60.66 ± 3.10</td> <!-- ScaLA-nn -->
   <td class="no qa">39.71 ± 2.59 / 71.60 ± 1.57</td> <!-- NorQuAD -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="da-rank">1.87</td> <!-- Danish rank -->
   <td class="no-rank">2.27</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.79</td> <!-- Swedish rank -->
   <td class="da ner">68.70 ± 2.40 / 64.05 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">49.88 ± 1.21 / 66.06 ± 1.12</td> <!-- Angry Tweets -->
   <td class="da la">44.20 ± 2.01 / 70.33 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da qa">39.90 ± 1.37 / 45.91 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">88.26 ± 1.11 / 89.24 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">81.37 ± 1.67 / 83.89 ± 1.34</td> <!-- NorNE-nn -->
   <td class="no sent">54.61 ± 1.51 / 67.19 ± 1.65</td> <!-- NoReC -->
   <td class="no la">50.35 ± 1.78 / 73.06 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">22.15 ± 9.02 / 58.20 ± 5.38</td> <!-- ScaLA-nn -->
   <td class="no qa">31.77 ± 1.55 / 45.47 ± 2.02</td> <!-- NorQuAD -->
   <td class="sv ner">79.02 ± 0.74 / 77.59 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.89 / 69.85 ± 3.16</td> <!-- SweReC -->
   <td class="sv la">50.19 ± 1.23 / 74.23 ± 0.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">40.65 ± 1.29 / 46.62 ± 1.30</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="da-rank">1.96</td> <!-- Danish rank -->
   <td class="no-rank">2.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.00</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="da-rank">1.54</td> <!-- Danish rank -->
   <td class="no-rank">2.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.27</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">1.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="da-rank">1.97</td> <!-- Danish rank -->
   <td class="no-rank">2.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.94</td> <!-- Swedish rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da qa">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">66.22 ± 2.15 / 48.98 ± 4.65</td> <!-- NorNE-nb -->
   <td class="no ner">64.14 ± 1.26 / 49.59 ± 4.31</td> <!-- NorNE-nn -->
   <td class="no sent">55.48 ± 1.77 / 69.68 ± 1.45</td> <!-- NoReC -->
   <td class="no la">26.13 ± 1.28 / 56.08 ± 2.05</td> <!-- ScaLA-nb -->
   <td class="no la">17.32 ± 0.77 / 54.57 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="da-rank">2.39</td> <!-- Danish rank -->
   <td class="no-rank">2.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.42</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/orpo-llama-3-swe (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,974 ± 1,208 / 1,032 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="da-rank">2.07</td> <!-- Danish rank -->
   <td class="no-rank">2.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.89</td> <!-- Swedish rank -->
   <td class="da ner">46.75 ± 2.79 / 29.40 ± 2.22</td> <!-- DANSK -->
   <td class="da sent">51.73 ± 1.40 / 66.43 ± 1.93</td> <!-- Angry Tweets -->
   <td class="da la">24.73 ± 4.78 / 53.98 ± 6.10</td> <!-- ScaLA-da -->
   <td class="da qa">59.97 ± 1.27 / 65.74 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">61.63 ± 1.64 / 48.09 ± 2.89</td> <!-- NorNE-nb -->
   <td class="no ner">61.30 ± 1.94 / 50.08 ± 2.60</td> <!-- NorNE-nn -->
   <td class="no sent">48.85 ± 2.22 / 64.93 ± 2.00</td> <!-- NoReC -->
   <td class="no la">24.15 ± 6.12 / 56.29 ± 6.81</td> <!-- ScaLA-nb -->
   <td class="no la">21.33 ± 3.03 / 58.05 ± 2.59</td> <!-- ScaLA-nn -->
   <td class="no qa">53.66 ± 4.34 / 75.19 ± 3.59</td> <!-- NorQuAD -->
   <td class="sv ner">60.93 ± 2.85 / 38.87 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.68 / 75.13 ± 1.85</td> <!-- SweReC -->
   <td class="sv la">26.02 ± 4.38 / 52.19 ± 5.44</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.84 ± 0.92 / 65.92 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.12</td> <!-- Danish rank -->
   <td class="no-rank">2.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.86</td> <!-- Swedish rank -->
   <td class="da ner">46.31 ± 3.22 / 29.09 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 1.47 / 66.35 ± 1.70</td> <!-- Angry Tweets -->
   <td class="da la">25.70 ± 4.59 / 55.65 ± 5.87</td> <!-- ScaLA-da -->
   <td class="da qa">59.79 ± 1.21 / 65.44 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">61.48 ± 1.83 / 47.65 ± 2.94</td> <!-- NorNE-nb -->
   <td class="no ner">61.58 ± 2.21 / 50.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">49.87 ± 1.88 / 66.15 ± 1.44</td> <!-- NoReC -->
   <td class="no la">21.20 ± 6.57 / 52.29 ± 7.43</td> <!-- ScaLA-nb -->
   <td class="no la">19.65 ± 4.32 / 56.66 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">53.35 ± 4.33 / 74.98 ± 3.70</td> <!-- NorQuAD -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/sol (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,701 ± 876 / 771 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.19</td> <!-- Danish rank -->
   <td class="no-rank">2.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.95</td> <!-- Swedish rank -->
   <td class="da ner">54.91 ± 1.53 / 36.29 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">44.38 ± 2.83 / 57.19 ± 3.61</td> <!-- Angry Tweets -->
   <td class="da la">21.11 ± 3.23 / 45.43 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da qa">58.96 ± 1.71 / 65.85 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">65.14 ± 1.62 / 52.85 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">65.88 ± 1.53 / 52.89 ± 2.29</td> <!-- NorNE-nn -->
   <td class="no sent">57.06 ± 1.54 / 71.09 ± 1.17</td> <!-- NoReC -->
   <td class="no la">26.41 ± 3.80 / 51.92 ± 5.30</td> <!-- ScaLA-nb -->
   <td class="no la">19.58 ± 1.29 / 53.93 ± 2.90</td> <!-- ScaLA-nn -->
   <td class="no qa">51.60 ± 1.97 / 77.87 ± 1.44</td> <!-- NorQuAD -->
   <td class="sv ner">57.51 ± 2.30 / 37.74 ± 3.15</td> <!-- SUC3 -->
   <td class="sv sent">77.31 ± 1.01 / 70.55 ± 2.26</td> <!-- SweReC -->
   <td class="sv la">25.06 ± 5.02 / 49.04 ± 4.68</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.16 ± 1.77 / 67.43 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.31</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.99</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">2.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.51</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da-rank">2.45</td> <!-- Danish rank -->
   <td class="no-rank">2.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.42</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/dolphin-2.9-llama3-8b-flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,018 ± 1,216 / 996 ± 324</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.93</td> <!-- Swedish rank -->
   <td class="da ner">51.37 ± 2.38 / 37.56 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">52.17 ± 3.44 / 67.14 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">27.98 ± 7.51 / 60.57 ± 5.72</td> <!-- ScaLA-da -->
   <td class="da qa">51.65 ± 0.84 / 59.94 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="no ner">64.51 ± 3.28 / 51.06 ± 4.78</td> <!-- NorNE-nb -->
   <td class="no ner">65.66 ± 3.82 / 53.90 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">52.90 ± 4.31 / 65.38 ± 3.73</td> <!-- NoReC -->
   <td class="no la">29.34 ± 4.34 / 59.36 ± 4.64</td> <!-- ScaLA-nb -->
   <td class="no la">17.42 ± 4.38 / 52.01 ± 3.50</td> <!-- ScaLA-nn -->
   <td class="no qa">38.49 ± 4.41 / 67.16 ± 3.41</td> <!-- NorQuAD -->
   <td class="sv ner">65.33 ± 2.38 / 46.88 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">74.99 ± 3.45 / 76.76 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">32.65 ± 5.08 / 61.25 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.71 ± 1.34 / 64.54 ± 1.00</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da qa">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">68.11 ± 1.83 / 57.57 ± 3.10</td> <!-- NorNE-nb -->
   <td class="no ner">68.19 ± 1.01 / 56.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">55.33 ± 1.95 / 69.71 ± 1.56</td> <!-- NoReC -->
   <td class="no la">10.15 ± 3.24 / 36.27 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">7.51 ± 2.97 / 35.89 ± 1.30</td> <!-- ScaLA-nn -->
   <td class="no qa">55.33 ± 3.29 / 80.42 ± 1.68</td> <!-- NorQuAD -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv qa">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da-rank">2.06</td> <!-- Danish rank -->
   <td class="no-rank">2.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.04</td> <!-- Swedish rank -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">56.51 ± 1.80 / 64.01 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="no ner">61.18 ± 2.76 / 56.36 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">65.16 ± 3.97 / 55.74 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">55.61 ± 4.02 / 68.27 ± 3.49</td> <!-- NoReC -->
   <td class="no la">20.84 ± 5.41 / 49.36 ± 4.98</td> <!-- ScaLA-nb -->
   <td class="no la">9.12 ± 3.51 / 43.06 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no qa">42.92 ± 3.08 / 69.13 ± 2.85</td> <!-- NorQuAD -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.43 ± 1.59 / 65.06 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="da-rank">2.09</td> <!-- Danish rank -->
   <td class="no-rank">2.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.99</td> <!-- Swedish rank -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da qa">57.26 ± 1.76 / 63.60 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">54.04 ± 2.86 / 48.50 ± 2.85</td> <!-- NorNE-nb -->
   <td class="no ner">62.21 ± 3.31 / 50.38 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">54.74 ± 3.71 / 67.81 ± 2.80</td> <!-- NoReC -->
   <td class="no la">14.51 ± 1.97 / 40.94 ± 1.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.38 ± 4.69 / 37.62 ± 2.92</td> <!-- ScaLA-nn -->
   <td class="no qa">42.83 ± 3.31 / 69.15 ± 2.50</td> <!-- NorQuAD -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.65 / 65.44 ± 1.38</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="da-rank">2.32</td> <!-- Danish rank -->
   <td class="no-rank">2.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.12</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.21</td> <!-- Swedish rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da qa">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">74.47 ± 1.47 / 65.57 ± 2.39</td> <!-- NorNE-nb -->
   <td class="no ner">72.93 ± 1.00 / 65.44 ± 2.55</td> <!-- NorNE-nn -->
   <td class="no sent">50.62 ± 3.52 / 65.69 ± 3.50</td> <!-- NoReC -->
   <td class="no la">27.77 ± 1.63 / 61.75 ± 1.77</td> <!-- ScaLA-nb -->
   <td class="no la">20.35 ± 1.92 / 57.74 ± 2.28</td> <!-- ScaLA-nn -->
   <td class="no qa">42.90 ± 3.57 / 69.90 ± 3.17</td> <!-- NorQuAD -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="da-rank">1.96</td> <!-- Danish rank -->
   <td class="no-rank">2.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>12.0.0</td> <!-- DANSK version -->
   <td>12.0.0</td> <!-- Angry Tweets version -->
   <td>12.0.0</td> <!-- ScaLA-da version -->
   <td>12.0.0</td> <!-- ScandiQA-da version -->
   <td>12.0.0</td> <!-- NorNE-nb version -->
   <td>12.0.0</td> <!-- NorNE-nn version -->
   <td>12.0.0</td> <!-- NoReC version -->
   <td>12.0.0</td> <!-- ScaLA-nb version -->
   <td>12.0.0</td> <!-- ScaLA-nn version -->
   <td>12.0.0</td> <!-- NorQuAD version -->
   <td>12.0.0</td> <!-- SUC3 version -->
   <td>12.0.0</td> <!-- SweReC version -->
   <td>12.0.0</td> <!-- ScaLA-sv version -->
   <td>12.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da-rank">2.21</td> <!-- Danish rank -->
   <td class="no-rank">2.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="da ner">63.59 ± 2.16 / 42.42 ± 3.34</td> <!-- DANSK -->
   <td class="da sent">29.47 ± 4.78 / 50.59 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">38.37 ± 9.13 / 60.56 ± 8.53</td> <!-- ScaLA-da -->
   <td class="da qa">54.63 ± 0.51 / 65.79 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="no ner">75.05 ± 1.56 / 57.52 ± 4.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.08 ± 1.43 / 62.50 ± 4.89</td> <!-- NorNE-nn -->
   <td class="no sent">37.79 ± 4.47 / 55.88 ± 3.23</td> <!-- NoReC -->
   <td class="no la">31.59 ± 11.25 / 54.68 ± 10.28</td> <!-- ScaLA-nb -->
   <td class="no la">39.25 ± 7.82 / 62.90 ± 7.12</td> <!-- ScaLA-nn -->
   <td class="no qa">39.43 ± 2.31 / 72.15 ± 1.71</td> <!-- NorQuAD -->
   <td class="sv ner">67.38 ± 1.52 / 52.86 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 4.81 / 67.01 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">29.41 ± 10.34 / 52.38 ± 8.76</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.67 ± 0.89 / 66.26 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- NorNE-nb version -->
   <td>12.11.0</td> <!-- NorNE-nn version -->
   <td>12.11.0</td> <!-- NoReC version -->
   <td>12.11.0</td> <!-- ScaLA-nb version -->
   <td>12.11.0</td> <!-- ScaLA-nn version -->
   <td>12.11.0</td> <!-- NorQuAD version -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da-rank">2.17</td> <!-- Danish rank -->
   <td class="no-rank">2.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Llama-3-8B-flashback-v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,807 ± 1,152 / 979 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.84</td> <!-- Swedish rank -->
   <td class="da ner">46.59 ± 4.16 / 31.16 ± 3.95</td> <!-- DANSK -->
   <td class="da sent">50.25 ± 1.25 / 66.18 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">14.46 ± 2.48 / 50.96 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">56.86 ± 1.23 / 62.50 ± 0.92</td> <!-- ScandiQA-da -->
   <td class="no ner">59.09 ± 1.89 / 52.82 ± 2.60</td> <!-- NorNE-nb -->
   <td class="no ner">60.02 ± 1.44 / 52.04 ± 2.63</td> <!-- NorNE-nn -->
   <td class="no sent">47.58 ± 1.91 / 64.35 ± 1.95</td> <!-- NoReC -->
   <td class="no la">10.52 ± 4.67 / 46.13 ± 6.95</td> <!-- ScaLA-nb -->
   <td class="no la">6.67 ± 4.53 / 40.61 ± 5.40</td> <!-- ScaLA-nn -->
   <td class="no qa">49.89 ± 4.89 / 71.90 ± 4.09</td> <!-- NorQuAD -->
   <td class="sv ner">59.03 ± 2.04 / 41.99 ± 4.35</td> <!-- SUC3 -->
   <td class="sv sent">81.13 ± 0.94 / 80.80 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">33.06 ± 3.65 / 61.21 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.21 ± 0.67 / 64.01 ± 0.68</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.26</td> <!-- Danish rank -->
   <td class="no-rank">2.44</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.49</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.11</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.00</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.34</td> <!-- Danish rank -->
   <td class="no-rank">2.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.98</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da-rank">2.11</td> <!-- Danish rank -->
   <td class="no-rank">2.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.00</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="da-rank">2.12</td> <!-- Danish rank -->
   <td class="no-rank">2.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
   <td class="da ner">52.22 ± 2.07 / 38.82 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">50.66 ± 1.88 / 62.04 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">23.57 ± 3.82 / 56.09 ± 4.62</td> <!-- ScaLA-da -->
   <td class="da qa">53.82 ± 2.13 / 61.94 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="no ner">60.21 ± 1.86 / 47.06 ± 3.08</td> <!-- NorNE-nb -->
   <td class="no ner">62.99 ± 2.66 / 48.82 ± 5.49</td> <!-- NorNE-nn -->
   <td class="no sent">55.12 ± 5.10 / 66.55 ± 5.07</td> <!-- NoReC -->
   <td class="no la">27.12 ± 4.90 / 54.26 ± 6.80</td> <!-- ScaLA-nb -->
   <td class="no la">6.82 ± 5.06 / 46.18 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">38.50 ± 3.93 / 69.99 ± 2.23</td> <!-- NorQuAD -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">2.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.51</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.62</td> <!-- Danish rank -->
   <td class="no-rank">2.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.59</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="da ner">65.10 ± 1.65 / 61.96 ± 1.26</td> <!-- DANSK -->
   <td class="da sent">45.07 ± 1.23 / 63.33 ± 0.78</td> <!-- Angry Tweets -->
   <td class="da la">26.83 ± 11.38 / 60.41 ± 6.66</td> <!-- ScaLA-da -->
   <td class="da qa">29.92 ± 1.25 / 35.05 ± 1.16</td> <!-- ScandiQA-da -->
   <td class="no ner">86.56 ± 1.18 / 87.30 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">80.57 ± 1.55 / 83.03 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">49.62 ± 2.72 / 62.56 ± 3.88</td> <!-- NoReC -->
   <td class="no la">38.45 ± 15.28 / 67.14 ± 7.71</td> <!-- ScaLA-nb -->
   <td class="no la">11.38 ± 7.59 / 51.68 ± 4.73</td> <!-- ScaLA-nn -->
   <td class="no qa">31.50 ± 2.41 / 47.61 ± 2.55</td> <!-- NorQuAD -->
   <td class="sv ner">75.49 ± 1.09 / 74.57 ± 0.60</td> <!-- SUC3 -->
   <td class="sv sent">71.12 ± 0.90 / 60.88 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">36.69 ± 15.58 / 65.77 ± 8.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.55 ± 2.07 / 38.90 ± 2.21</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.05</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da-rank">2.22</td> <!-- Danish rank -->
   <td class="no-rank">2.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.10</td> <!-- Swedish rank -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">59.90 ± 0.84 / 65.47 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="no ner">61.41 ± 1.71 / 52.32 ± 2.63</td> <!-- NorNE-nb -->
   <td class="no ner">59.49 ± 1.26 / 49.45 ± 3.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.19 ± 1.64 / 63.36 ± 1.52</td> <!-- NoReC -->
   <td class="no la">15.17 ± 2.64 / 50.25 ± 4.51</td> <!-- ScaLA-nb -->
   <td class="no la">10.78 ± 1.99 / 50.08 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">48.99 ± 2.91 / 73.08 ± 2.26</td> <!-- NorQuAD -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.67 ± 0.96 / 64.58 ± 0.78</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da-rank">2.09</td> <!-- Danish rank -->
   <td class="no-rank">2.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">58.17 ± 1.71 / 63.79 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no qa">41.43 ± 3.34 / 67.26 ± 2.73</td> <!-- NorQuAD -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.92 ± 1.64 / 64.87 ± 1.47</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da-rank">2.25</td> <!-- Danish rank -->
   <td class="no-rank">2.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 1.98 / 64.33 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no qa">42.42 ± 2.92 / 69.53 ± 3.17</td> <!-- NorQuAD -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.75 ± 1.46 / 65.08 ± 1.15</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.10</td> <!-- Swedish rank -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da qa">56.82 ± 1.75 / 62.40 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="no ner">55.93 ± 2.70 / 50.51 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">63.85 ± 2.45 / 53.11 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">50.41 ± 5.49 / 64.49 ± 4.37</td> <!-- NoReC -->
   <td class="no la">15.74 ± 4.15 / 41.16 ± 2.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.23 ± 4.69 / 34.70 ± 1.39</td> <!-- ScaLA-nn -->
   <td class="no qa">39.81 ± 2.81 / 65.65 ± 2.64</td> <!-- NorQuAD -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.75 ± 1.13 / 64.72 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,396 ± 6,394 / 4,534 ± 1,421</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="da-rank">2.23</td> <!-- Danish rank -->
   <td class="no-rank">2.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.98</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.45</td> <!-- Danish rank -->
   <td class="no-rank">2.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.27</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da qa">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no qa">34.48 ± 2.13 / 65.43 ± 2.07</td> <!-- NorQuAD -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.45</td> <!-- Danish rank -->
   <td class="no-rank">2.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.27</td> <!-- Danish rank -->
   <td class="no-rank">2.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.06</td> <!-- Swedish rank -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da qa">56.46 ± 1.48 / 61.69 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">39.21 ± 3.48 / 64.09 ± 3.49</td> <!-- NorQuAD -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.42 ± 1.64 / 63.83 ± 1.18</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da-rank">2.21</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,431 ± 1,267 / 1,139 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
   <td class="da ner">38.25 ± 3.75 / 28.14 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">39.37 ± 2.09 / 56.57 ± 1.90</td> <!-- Angry Tweets -->
   <td class="da la">29.76 ± 3.24 / 61.80 ± 2.22</td> <!-- ScaLA-da -->
   <td class="da qa">57.02 ± 1.28 / 63.16 ± 0.90</td> <!-- ScandiQA-da -->
   <td class="no ner">50.47 ± 2.96 / 43.31 ± 2.54</td> <!-- NorNE-nb -->
   <td class="no ner">51.97 ± 3.83 / 42.66 ± 5.03</td> <!-- NorNE-nn -->
   <td class="no sent">48.03 ± 1.71 / 65.89 ± 1.68</td> <!-- NoReC -->
   <td class="no la">22.65 ± 3.80 / 51.83 ± 5.03</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 4.78 / 49.03 ± 6.45</td> <!-- ScaLA-nn -->
   <td class="no qa">44.72 ± 4.47 / 68.08 ± 4.22</td> <!-- NorQuAD -->
   <td class="sv ner">48.19 ± 2.55 / 37.50 ± 3.62</td> <!-- SUC3 -->
   <td class="sv sent">79.95 ± 0.87 / 81.24 ± 0.64</td> <!-- SweReC -->
   <td class="sv la">32.85 ± 2.28 / 61.74 ± 3.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.39 ± 1.52 / 63.58 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="da-rank">2.24</td> <!-- Danish rank -->
   <td class="no-rank">2.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
   <td class="da ner">47.01 ± 2.76 / 36.47 ± 3.27</td> <!-- DANSK -->
   <td class="da sent">50.60 ± 3.33 / 65.49 ± 2.38</td> <!-- Angry Tweets -->
   <td class="da la">13.73 ± 3.33 / 52.15 ± 3.17</td> <!-- ScaLA-da -->
   <td class="da qa">56.35 ± 1.68 / 61.63 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="no ner">58.60 ± 4.42 / 52.72 ± 4.93</td> <!-- NorNE-nb -->
   <td class="no ner">63.15 ± 2.29 / 54.03 ± 4.33</td> <!-- NorNE-nn -->
   <td class="no sent">51.85 ± 3.51 / 64.28 ± 2.54</td> <!-- NoReC -->
   <td class="no la">0.66 ± 1.29 / 33.42 ± 0.80</td> <!-- ScaLA-nb -->
   <td class="no la">0.53 ± 1.05 / 33.42 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">43.22 ± 2.24 / 68.55 ± 2.42</td> <!-- NorQuAD -->
   <td class="sv ner">56.21 ± 2.49 / 44.78 ± 4.19</td> <!-- SUC3 -->
   <td class="sv sent">78.30 ± 1.71 / 79.80 ± 2.03</td> <!-- SweReC -->
   <td class="sv la">14.35 ± 5.65 / 48.69 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">61.08 ± 1.47 / 65.72 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da-rank">2.24</td> <!-- Danish rank -->
   <td class="no-rank">2.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da qa">57.87 ± 2.32 / 64.53 ± 1.73</td> <!-- ScandiQA-da -->
   <td class="no ner">53.68 ± 2.01 / 49.22 ± 2.67</td> <!-- NorNE-nb -->
   <td class="no ner">61.92 ± 4.06 / 49.03 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.19 / 57.76 ± 2.55</td> <!-- NoReC -->
   <td class="no la">0.91 ± 1.78 / 33.51 ± 0.85</td> <!-- ScaLA-nb -->
   <td class="no la">1.24 ± 1.66 / 33.71 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no qa">47.76 ± 2.93 / 70.99 ± 2.39</td> <!-- NorQuAD -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.96 ± 2.00 / 64.06 ± 1.76</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama3-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,695 ± 1,277 / 532 ± 183</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="da ner">51.40 ± 3.08 / 37.70 ± 3.28</td> <!-- DANSK -->
   <td class="da sent">42.13 ± 0.57 / 45.91 ± 0.39</td> <!-- Angry Tweets -->
   <td class="da la">3.91 ± 2.02 / 34.38 ± 0.47</td> <!-- ScaLA-da -->
   <td class="da qa">57.81 ± 1.03 / 66.28 ± 0.48</td> <!-- ScandiQA-da -->
   <td class="no ner">66.94 ± 2.67 / 60.25 ± 3.14</td> <!-- NorNE-nb -->
   <td class="no ner">67.69 ± 1.87 / 61.57 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">48.40 ± 3.28 / 61.42 ± 3.56</td> <!-- NoReC -->
   <td class="no la">24.26 ± 2.68 / 57.31 ± 2.64</td> <!-- ScaLA-nb -->
   <td class="no la">18.43 ± 1.34 / 52.28 ± 2.63</td> <!-- ScaLA-nn -->
   <td class="no qa">46.80 ± 2.74 / 74.57 ± 2.20</td> <!-- NorQuAD -->
   <td class="sv ner">63.19 ± 2.83 / 51.22 ± 3.61</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.64 / 61.59 ± 0.77</td> <!-- SweReC -->
   <td class="sv la">5.34 ± 1.42 / 34.32 ± 0.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.70 ± 0.87 / 66.00 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="da ner">46.70 ± 3.49 / 36.30 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 3.90 / 55.98 ± 4.69</td> <!-- Angry Tweets -->
   <td class="da la">8.04 ± 5.32 / 36.02 ± 2.59</td> <!-- ScaLA-da -->
   <td class="da qa">60.05 ± 1.30 / 64.15 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">51.82 ± 4.16 / 44.64 ± 4.66</td> <!-- NorNE-nb -->
   <td class="no ner">62.55 ± 3.84 / 49.66 ± 5.87</td> <!-- NorNE-nn -->
   <td class="no sent">56.37 ± 4.27 / 69.55 ± 4.52</td> <!-- NoReC -->
   <td class="no la">6.04 ± 5.92 / 36.34 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">-0.02 ± 0.04 / 33.47 ± 0.88</td> <!-- ScaLA-nn -->
   <td class="no qa">48.85 ± 4.11 / 70.75 ± 3.73</td> <!-- NorQuAD -->
   <td class="sv ner">52.34 ± 3.07 / 39.14 ± 4.60</td> <!-- SUC3 -->
   <td class="sv sent">77.66 ± 2.09 / 78.59 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.00 ± 4.15 / 36.34 ± 2.20</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.16 ± 1.81 / 64.12 ± 1.59</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.1</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.1</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.1</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da-rank">2.37</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.04</td> <!-- Swedish rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da qa">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
   <td class="no ner">48.97 ± 2.42 / 39.15 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">51.52 ± 2.96 / 40.17 ± 3.62</td> <!-- NorNE-nn -->
   <td class="no sent">49.05 ± 2.73 / 63.94 ± 2.42</td> <!-- NoReC -->
   <td class="no la">14.37 ± 2.18 / 47.80 ± 4.36</td> <!-- ScaLA-nb -->
   <td class="no la">9.96 ± 1.34 / 48.97 ± 3.77</td> <!-- ScaLA-nn -->
   <td class="no qa">44.07 ± 3.40 / 68.49 ± 2.97</td> <!-- NorQuAD -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,141 ± 994 / 905 ± 299</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da-rank">2.33</td> <!-- Danish rank -->
   <td class="no-rank">2.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
   <td class="da ner">36.72 ± 3.33 / 27.73 ± 2.57</td> <!-- DANSK -->
   <td class="da sent">46.48 ± 1.17 / 55.20 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">26.10 ± 3.17 / 59.19 ± 3.94</td> <!-- ScaLA-da -->
   <td class="da qa">58.00 ± 0.91 / 64.11 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="no ner">44.53 ± 2.58 / 36.59 ± 1.71</td> <!-- NorNE-nb -->
   <td class="no ner">47.02 ± 2.08 / 39.99 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">41.84 ± 2.46 / 56.79 ± 2.95</td> <!-- NoReC -->
   <td class="no la">19.97 ± 3.99 / 47.40 ± 4.84</td> <!-- ScaLA-nb -->
   <td class="no la">15.61 ± 4.20 / 43.40 ± 4.90</td> <!-- ScaLA-nn -->
   <td class="no qa">50.91 ± 4.42 / 73.43 ± 3.55</td> <!-- NorQuAD -->
   <td class="sv ner">36.45 ± 2.44 / 27.24 ± 2.29</td> <!-- SUC3 -->
   <td class="sv sent">81.12 ± 1.02 / 77.04 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">26.80 ± 2.07 / 59.15 ± 2.72</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.16 ± 0.82 / 64.72 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- ScaLA-nb version -->
   <td>12.10.5</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da-rank">2.52</td> <!-- Danish rank -->
   <td class="no-rank">2.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.34</td> <!-- Swedish rank -->
   <td class="da ner">52.61 ± 1.77 / 33.64 ± 2.67</td> <!-- DANSK -->
   <td class="da sent">49.81 ± 1.43 / 66.32 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">19.64 ± 1.63 / 54.22 ± 2.32</td> <!-- ScaLA-da -->
   <td class="da qa">48.03 ± 1.24 / 57.94 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">64.37 ± 2.17 / 52.81 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">62.77 ± 0.83 / 51.80 ± 2.77</td> <!-- NorNE-nn -->
   <td class="no sent">50.60 ± 4.90 / 66.76 ± 3.04</td> <!-- NoReC -->
   <td class="no la">18.09 ± 2.04 / 52.56 ± 2.60</td> <!-- ScaLA-nb -->
   <td class="no la">12.25 ± 2.18 / 50.79 ± 2.42</td> <!-- ScaLA-nn -->
   <td class="no qa">38.34 ± 2.39 / 69.54 ± 1.96</td> <!-- NorQuAD -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da-rank">2.59</td> <!-- Danish rank -->
   <td class="no-rank">2.49</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">57.26 ± 0.79 / 63.80 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no qa">49.03 ± 4.22 / 74.38 ± 3.92</td> <!-- NorQuAD -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.16 ± 1.23 / 65.78 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.12</td> <!-- Swedish rank -->
   <td class="da ner">39.12 ± 4.28 / 28.74 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">36.47 ± 4.90 / 50.72 ± 6.21</td> <!-- Angry Tweets -->
   <td class="da la">26.76 ± 4.78 / 57.02 ± 5.13</td> <!-- ScaLA-da -->
   <td class="da qa">58.75 ± 1.19 / 64.41 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="no ner">50.43 ± 2.27 / 42.19 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">54.20 ± 1.81 / 43.92 ± 2.94</td> <!-- NorNE-nn -->
   <td class="no sent">39.21 ± 5.64 / 56.54 ± 6.43</td> <!-- NoReC -->
   <td class="no la">20.51 ± 4.43 / 52.48 ± 5.96</td> <!-- ScaLA-nb -->
   <td class="no la">11.66 ± 4.10 / 48.13 ± 6.13</td> <!-- ScaLA-nn -->
   <td class="no qa">51.57 ± 3.87 / 73.95 ± 3.51</td> <!-- NorQuAD -->
   <td class="sv ner">47.10 ± 2.60 / 35.06 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">73.05 ± 5.27 / 74.56 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">30.29 ± 2.63 / 61.40 ± 3.22</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.39 ± 1.38 / 63.51 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.05</td> <!-- Swedish rank -->
   <td class="da ner">19.59 ± 2.54 / 15.47 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">46.55 ± 1.89 / 59.52 ± 3.56</td> <!-- Angry Tweets -->
   <td class="da la">32.64 ± 2.91 / 63.84 ± 1.69</td> <!-- ScaLA-da -->
   <td class="da qa">59.40 ± 1.02 / 64.81 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">26.43 ± 3.36 / 26.32 ± 2.35</td> <!-- NorNE-nb -->
   <td class="no ner">32.66 ± 3.42 / 29.43 ± 1.74</td> <!-- NorNE-nn -->
   <td class="no sent">41.82 ± 3.69 / 53.06 ± 5.15</td> <!-- NoReC -->
   <td class="no la">25.82 ± 4.43 / 59.85 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">20.16 ± 3.43 / 53.83 ± 5.61</td> <!-- ScaLA-nn -->
   <td class="no qa">52.68 ± 3.58 / 75.16 ± 2.44</td> <!-- NorQuAD -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.9.1</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.9.1</td> <!-- ScaLA-nb version -->
   <td>12.9.1</td> <!-- ScaLA-nn version -->
   <td>12.9.1</td> <!-- NorQuAD version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.79</td> <!-- Danish rank -->
   <td class="no-rank">2.98</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.64</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,735 ± 7,558 / 6,846 ± 2,312</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.53</td> <!-- Danish rank -->
   <td class="no-rank">2.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.37</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">46.86 ± 3.27 / 70.86 ± 2.79</td> <!-- NorQuAD -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da qa">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">50.63 ± 2.12 / 44.59 ± 1.80</td> <!-- NorNE-nb -->
   <td class="no ner">52.69 ± 2.30 / 46.51 ± 3.63</td> <!-- NorNE-nn -->
   <td class="no sent">44.05 ± 2.51 / 61.80 ± 2.28</td> <!-- NoReC -->
   <td class="no la">11.60 ± 4.10 / 43.01 ± 5.07</td> <!-- ScaLA-nb -->
   <td class="no la">9.26 ± 1.14 / 46.28 ± 3.60</td> <!-- ScaLA-nn -->
   <td class="no qa">45.23 ± 3.73 / 68.68 ± 3.29</td> <!-- NorQuAD -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.1</td> <!-- Angry Tweets version -->
   <td>12.5.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.1</td> <!-- NoReC version -->
   <td>12.5.1</td> <!-- ScaLA-nb version -->
   <td>12.5.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.1</td> <!-- SweReC version -->
   <td>12.5.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.22</td> <!-- Swedish rank -->
   <td class="da ner">44.90 ± 3.15 / 31.91 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">42.61 ± 1.79 / 53.47 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 3.44 / 38.18 ± 4.21</td> <!-- ScaLA-da -->
   <td class="da qa">59.62 ± 1.12 / 64.70 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">52.52 ± 1.85 / 43.46 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.60 ± 3.22 / 45.25 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">48.23 ± 3.31 / 65.51 ± 3.01</td> <!-- NoReC -->
   <td class="no la">8.53 ± 3.72 / 38.61 ± 3.22</td> <!-- ScaLA-nb -->
   <td class="no la">6.65 ± 1.40 / 39.32 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no qa">46.89 ± 3.29 / 70.96 ± 2.84</td> <!-- NorQuAD -->
   <td class="sv ner">53.00 ± 2.53 / 39.09 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">79.70 ± 0.65 / 79.45 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">4.32 ± 2.19 / 34.43 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.03 ± 1.03 / 64.74 ± 0.84</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="da ner">43.60 ± 2.94 / 32.17 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.92 ± 1.50 / 61.91 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">15.43 ± 3.79 / 46.20 ± 5.54</td> <!-- ScaLA-da -->
   <td class="da qa">59.13 ± 0.86 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">50.56 ± 2.04 / 44.38 ± 1.85</td> <!-- NorNE-nb -->
   <td class="no ner">52.65 ± 2.27 / 46.48 ± 3.65</td> <!-- NorNE-nn -->
   <td class="no sent">44.61 ± 2.28 / 62.22 ± 2.10</td> <!-- NoReC -->
   <td class="no la">12.10 ± 4.22 / 43.27 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">9.30 ± 0.99 / 46.11 ± 3.47</td> <!-- ScaLA-nn -->
   <td class="no qa">45.15 ± 3.72 / 68.61 ± 3.30</td> <!-- NorQuAD -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.48</td> <!-- Danish rank -->
   <td class="no-rank">2.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.16</td> <!-- Swedish rank -->
   <td class="da ner">60.01 ± 2.63 / 56.13 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">42.17 ± 1.64 / 61.25 ± 1.45</td> <!-- Angry Tweets -->
   <td class="da la">29.43 ± 13.02 / 62.08 ± 7.77</td> <!-- ScaLA-da -->
   <td class="da qa">29.79 ± 3.33 / 34.82 ± 2.83</td> <!-- ScandiQA-da -->
   <td class="no ner">84.11 ± 1.00 / 81.35 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">77.22 ± 1.99 / 73.67 ± 2.26</td> <!-- NorNE-nn -->
   <td class="no sent">37.02 ± 1.09 / 47.88 ± 2.50</td> <!-- NoReC -->
   <td class="no la">35.42 ± 12.32 / 66.30 ± 6.78</td> <!-- ScaLA-nb -->
   <td class="no la">6.87 ± 6.85 / 50.70 ± 3.62</td> <!-- ScaLA-nn -->
   <td class="no qa">25.98 ± 2.87 / 36.16 ± 3.35</td> <!-- NorQuAD -->
   <td class="sv ner">70.17 ± 0.99 / 64.19 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">66.62 ± 1.71 / 61.90 ± 2.61</td> <!-- SweReC -->
   <td class="sv la">46.72 ± 3.65 / 72.15 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">31.38 ± 1.36 / 35.79 ± 1.33</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
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
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 0.73 / 64.76 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">51.99 ± 1.85 / 37.40 ± 2.95</td> <!-- NorNE-nb -->
   <td class="no ner">52.74 ± 1.13 / 36.83 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">50.39 ± 1.38 / 66.42 ± 1.20</td> <!-- NoReC -->
   <td class="no la">0.99 ± 1.03 / 33.56 ± 0.25</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 1.30 / 34.04 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">47.95 ± 3.19 / 72.60 ± 2.57</td> <!-- NorQuAD -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.31 ± 0.92 / 63.73 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.23</td> <!-- Swedish rank -->
   <td class="da ner">44.00 ± 2.63 / 29.00 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.41 ± 1.79 / 62.27 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">16.17 ± 2.17 / 56.93 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">57.06 ± 0.83 / 63.94 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="no ner">57.21 ± 1.51 / 40.40 ± 2.79</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.34 / 41.07 ± 2.58</td> <!-- NorNE-nn -->
   <td class="no sent">38.93 ± 3.56 / 57.45 ± 3.77</td> <!-- NoReC -->
   <td class="no la">8.65 ± 3.33 / 47.18 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">5.92 ± 1.58 / 47.50 ± 3.58</td> <!-- ScaLA-nn -->
   <td class="no qa">42.32 ± 2.80 / 69.24 ± 2.68</td> <!-- NorQuAD -->
   <td class="sv ner">49.90 ± 2.28 / 35.48 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 2.05 / 79.13 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">14.67 ± 2.27 / 53.90 ± 2.24</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.12 ± 0.70 / 63.72 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.11.0</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">2.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da qa">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">61.90 ± 2.57 / 57.16 ± 2.81</td> <!-- NorNE-nb -->
   <td class="no ner">66.92 ± 2.52 / 57.81 ± 3.54</td> <!-- NorNE-nn -->
   <td class="no sent">48.80 ± 4.56 / 63.38 ± 3.06</td> <!-- NoReC -->
   <td class="no la">19.53 ± 5.49 / 51.96 ± 4.90</td> <!-- ScaLA-nb -->
   <td class="no la">9.83 ± 4.57 / 47.95 ± 2.22</td> <!-- ScaLA-nn -->
   <td class="no qa">30.27 ± 2.28 / 62.04 ± 2.19</td> <!-- NorQuAD -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.36</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da-rank">2.94</td> <!-- Danish rank -->
   <td class="no-rank">3.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.69</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da-rank">2.45</td> <!-- Danish rank -->
   <td class="no-rank">2.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.38</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="da-rank">2.27</td> <!-- Danish rank -->
   <td class="no-rank">2.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.71</td> <!-- Swedish rank -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da qa">57.96 ± 0.80 / 63.50 ± 0.73</td> <!-- ScandiQA-da -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">40.64 ± 2.58 / 66.46 ± 2.62</td> <!-- NorQuAD -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.26 ± 1.66 / 64.40 ± 1.35</td> <!-- ScandiQA-sv -->
   <td>9.3.0</td> <!-- DANSK version -->
   <td>9.3.0</td> <!-- Angry Tweets version -->
   <td>9.3.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.0</td> <!-- NorNE-nb version -->
   <td>9.3.0</td> <!-- NorNE-nn version -->
   <td>9.3.0</td> <!-- NoReC version -->
   <td>9.3.0</td> <!-- ScaLA-nb version -->
   <td>9.3.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.0</td> <!-- SUC3 version -->
   <td>9.3.0</td> <!-- SweReC version -->
   <td>9.3.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-13B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 645 / 709 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.57</td> <!-- Danish rank -->
   <td class="no-rank">2.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.35</td> <!-- Swedish rank -->
   <td class="da ner">44.17 ± 3.14 / 31.63 ± 3.03</td> <!-- DANSK -->
   <td class="da sent">44.28 ± 1.94 / 55.59 ± 3.06</td> <!-- Angry Tweets -->
   <td class="da la">3.11 ± 1.88 / 34.35 ± 0.74</td> <!-- ScaLA-da -->
   <td class="da qa">55.59 ± 0.65 / 63.25 ± 0.37</td> <!-- ScandiQA-da -->
   <td class="no ner">56.72 ± 1.90 / 43.75 ± 2.72</td> <!-- NorNE-nb -->
   <td class="no ner">57.62 ± 1.35 / 43.81 ± 2.43</td> <!-- NorNE-nn -->
   <td class="no sent">48.86 ± 2.54 / 64.32 ± 2.46</td> <!-- NoReC -->
   <td class="no la">9.87 ± 1.78 / 44.29 ± 3.62</td> <!-- ScaLA-nb -->
   <td class="no la">6.90 ± 1.65 / 48.96 ± 3.09</td> <!-- ScaLA-nn -->
   <td class="no qa">41.27 ± 3.42 / 69.36 ± 3.54</td> <!-- NorQuAD -->
   <td class="sv ner">49.26 ± 2.31 / 36.92 ± 4.05</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 0.80 / 77.87 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">0.22 ± 0.43 / 33.38 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.78 ± 1.02 / 63.61 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.48</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.30</td> <!-- Swedish rank -->
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
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.80</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.85</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.98</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.46</td> <!-- Swedish rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da qa">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no qa">35.74 ± 2.44 / 64.27 ± 2.42</td> <!-- NorQuAD -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">3.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.04</td> <!-- Swedish rank -->
   <td class="da ner">41.28 ± 3.92 / 31.98 ± 3.26</td> <!-- DANSK -->
   <td class="da sent">23.01 ± 3.87 / 36.55 ± 6.42</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 2.75 / 58.11 ± 3.45</td> <!-- ScaLA-da -->
   <td class="da qa">60.29 ± 0.81 / 65.52 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">51.12 ± 3.13 / 47.26 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">55.35 ± 1.60 / 49.99 ± 2.21</td> <!-- NorNE-nn -->
   <td class="no sent">23.75 ± 3.25 / 42.92 ± 4.45</td> <!-- NoReC -->
   <td class="no la">14.00 ± 4.25 / 42.71 ± 5.83</td> <!-- ScaLA-nb -->
   <td class="no la">7.61 ± 2.57 / 45.86 ± 3.96</td> <!-- ScaLA-nn -->
   <td class="no qa">49.24 ± 4.28 / 72.68 ± 3.66</td> <!-- NorQuAD -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="da-rank">2.37</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">52.78 ± 1.15 / 60.80 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">32.75 ± 1.68 / 59.21 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.22 ± 0.88 / 61.85 ± 0.63</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="da-rank">2.61</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.32</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da-rank">2.58</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="da ner">41.63 ± 2.33 / 28.51 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.52 / 60.64 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">54.25 ± 0.85 / 61.70 ± 0.71</td> <!-- ScandiQA-da -->
   <td class="no ner">56.18 ± 3.05 / 49.39 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">56.96 ± 1.64 / 48.30 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">50.94 ± 1.41 / 66.55 ± 1.06</td> <!-- NoReC -->
   <td class="no la">8.19 ± 1.95 / 45.17 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">5.55 ± 1.71 / 48.92 ± 2.94</td> <!-- ScaLA-nn -->
   <td class="no qa">41.35 ± 2.33 / 69.72 ± 2.52</td> <!-- NorQuAD -->
   <td class="sv ner">53.95 ± 1.89 / 42.16 ± 4.59</td> <!-- SUC3 -->
   <td class="sv sent">60.91 ± 2.35 / 59.47 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">0.32 ± 0.62 / 33.39 ± 0.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.28 ± 0.62 / 63.41 ± 0.55</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">3.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
   <td class="da ner">40.60 ± 2.25 / 28.71 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">36.89 ± 2.27 / 43.77 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">26.41 ± 5.40 / 53.03 ± 6.56</td> <!-- ScaLA-da -->
   <td class="da qa">57.81 ± 1.11 / 63.44 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="no ner">48.89 ± 3.42 / 35.46 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">51.95 ± 1.59 / 36.45 ± 2.57</td> <!-- NorNE-nn -->
   <td class="no sent">20.54 ± 6.01 / 36.30 ± 6.77</td> <!-- NoReC -->
   <td class="no la">4.39 ± 3.94 / 35.23 ± 2.81</td> <!-- ScaLA-nb -->
   <td class="no la">1.20 ± 1.64 / 34.54 ± 1.31</td> <!-- ScaLA-nn -->
   <td class="no qa">47.16 ± 4.15 / 70.08 ± 3.96</td> <!-- NorQuAD -->
   <td class="sv ner">42.23 ± 2.44 / 30.30 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">78.80 ± 0.93 / 75.28 ± 1.78</td> <!-- SweReC -->
   <td class="sv la">15.47 ± 1.79 / 54.26 ± 3.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.75 ± 1.15 / 62.43 ± 0.95</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.45</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.38</td> <!-- Swedish rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="no ner">45.50 ± 2.71 / 40.02 ± 3.16</td> <!-- NorNE-nb -->
   <td class="no ner">45.96 ± 2.67 / 41.28 ± 2.25</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 3.40 / 62.00 ± 2.71</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">52.19 ± 2.88 / 74.97 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.2.0</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.2.0</td> <!-- NoReC version -->
   <td>12.3.1</td> <!-- ScaLA-nb version -->
   <td>12.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.2.0</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.67</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.32</td> <!-- Swedish rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="no ner">45.28 ± 3.06 / 41.73 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">46.00 ± 4.26 / 42.96 ± 3.38</td> <!-- NorNE-nn -->
   <td class="no sent">44.95 ± 3.19 / 61.88 ± 2.88</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">2.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="da-rank">2.59</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.45</td> <!-- Swedish rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.23 ± 3.15 / 63.67 ± 2.98</td> <!-- NorQuAD -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">2.96</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="da-rank">2.53</td> <!-- Danish rank -->
   <td class="no-rank">3.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="da ner">38.39 ± 3.57 / 24.87 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">49.44 ± 1.03 / 66.00 ± 0.88</td> <!-- Angry Tweets -->
   <td class="da la">7.50 ± 2.07 / 47.53 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">51.24 ± 1.09 / 57.72 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="no ner">38.82 ± 5.36 / 30.48 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">43.28 ± 3.13 / 33.87 ± 3.30</td> <!-- NorNE-nn -->
   <td class="no sent">38.05 ± 1.85 / 47.06 ± 3.97</td> <!-- NoReC -->
   <td class="no la">8.45 ± 2.47 / 46.75 ± 3.97</td> <!-- ScaLA-nb -->
   <td class="no la">7.50 ± 1.65 / 48.14 ± 4.65</td> <!-- ScaLA-nn -->
   <td class="no qa">40.47 ± 2.77 / 64.21 ± 2.94</td> <!-- NorQuAD -->
   <td class="sv ner">47.24 ± 3.36 / 24.94 ± 3.21</td> <!-- SUC3 -->
   <td class="sv sent">77.91 ± 1.42 / 76.08 ± 2.54</td> <!-- SweReC -->
   <td class="sv la">5.55 ± 2.55 / 48.57 ± 3.21</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.41 ± 0.74 / 57.55 ± 0.69</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-33B@1000B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,080 ± 700 / 331 ± 117</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.62</td> <!-- Danish rank -->
   <td class="no-rank">3.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.37</td> <!-- Swedish rank -->
   <td class="da ner">34.22 ± 2.47 / 22.52 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">45.05 ± 2.49 / 62.23 ± 1.84</td> <!-- Angry Tweets -->
   <td class="da la">9.40 ± 2.63 / 44.83 ± 4.69</td> <!-- ScaLA-da -->
   <td class="da qa">54.92 ± 1.00 / 60.33 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">40.40 ± 2.29 / 30.41 ± 2.07</td> <!-- NorNE-nb -->
   <td class="no ner">44.45 ± 3.61 / 34.06 ± 3.27</td> <!-- NorNE-nn -->
   <td class="no sent">40.79 ± 1.70 / 57.84 ± 2.77</td> <!-- NoReC -->
   <td class="no la">5.91 ± 2.51 / 47.81 ± 3.76</td> <!-- ScaLA-nb -->
   <td class="no la">2.98 ± 2.86 / 45.49 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no qa">37.75 ± 3.23 / 59.72 ± 3.03</td> <!-- NorQuAD -->
   <td class="sv ner">42.35 ± 1.51 / 28.31 ± 3.87</td> <!-- SUC3 -->
   <td class="sv sent">77.68 ± 1.11 / 78.86 ± 0.93</td> <!-- SweReC -->
   <td class="sv la">8.08 ± 1.69 / 50.52 ± 2.25</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.57 ± 1.25 / 60.34 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- NorNE-nb version -->
   <td>12.9.0</td> <!-- NorNE-nn version -->
   <td>12.9.0</td> <!-- NoReC version -->
   <td>12.9.0</td> <!-- ScaLA-nb version -->
   <td>12.9.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da-rank">2.63</td> <!-- Danish rank -->
   <td class="no-rank">3.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da-rank">2.72</td> <!-- Danish rank -->
   <td class="no-rank">3.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.31</td> <!-- Swedish rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">44.19 ± 4.13 / 66.18 ± 4.05</td> <!-- NorQuAD -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da-rank">2.23</td> <!-- Danish rank -->
   <td class="no-rank">3.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.89</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">3.05</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
   <td class="da ner">21.47 ± 3.87 / 16.98 ± 3.19</td> <!-- DANSK -->
   <td class="da sent">48.39 ± 0.66 / 64.51 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">12.46 ± 2.22 / 52.33 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">52.51 ± 1.57 / 58.49 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="no ner">21.09 ± 6.44 / 20.45 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">26.31 ± 4.64 / 26.42 ± 2.98</td> <!-- NorNE-nn -->
   <td class="no sent">49.00 ± 3.88 / 65.98 ± 2.95</td> <!-- NoReC -->
   <td class="no la">7.15 ± 2.14 / 40.83 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">7.98 ± 2.64 / 45.21 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">47.70 ± 5.32 / 68.04 ± 5.37</td> <!-- NorQuAD -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">3.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-40b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">39927</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">409 ± 53 / 182 ± 54</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da-rank">2.65</td> <!-- Danish rank -->
   <td class="no-rank">3.27</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.45</td> <!-- Swedish rank -->
   <td class="da ner">26.57 ± 5.22 / 17.35 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">47.81 ± 1.32 / 64.26 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">11.13 ± 2.06 / 51.34 ± 3.02</td> <!-- ScaLA-da -->
   <td class="da qa">53.78 ± 0.70 / 60.13 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="no ner">24.07 ± 5.59 / 19.09 ± 2.55</td> <!-- NorNE-nb -->
   <td class="no ner">26.67 ± 6.24 / 21.18 ± 2.80</td> <!-- NorNE-nn -->
   <td class="no sent">31.05 ± 7.03 / 45.69 ± 8.29</td> <!-- NoReC -->
   <td class="no la">10.80 ± 1.96 / 52.29 ± 2.55</td> <!-- ScaLA-nb -->
   <td class="no la">8.89 ± 2.52 / 47.62 ± 4.31</td> <!-- ScaLA-nn -->
   <td class="no qa">48.78 ± 3.64 / 71.66 ± 3.34</td> <!-- NorQuAD -->
   <td class="sv ner">32.00 ± 3.27 / 17.02 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">80.44 ± 0.54 / 77.81 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">10.73 ± 2.53 / 51.37 ± 4.05</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.80 ± 0.86 / 60.53 ± 0.78</td> <!-- ScandiQA-sv -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- NorNE-nb version -->
   <td>12.9.0</td> <!-- NorNE-nn version -->
   <td>12.9.0</td> <!-- NoReC version -->
   <td>12.9.0</td> <!-- ScaLA-nb version -->
   <td>12.9.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da-rank">3.01</td> <!-- Danish rank -->
   <td class="no-rank">3.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.99</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Phi-3-mini-4k-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,360 ± 179 / 566 ± 190</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">3.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.56</td> <!-- Swedish rank -->
   <td class="da ner">39.96 ± 3.11 / 25.49 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">44.93 ± 1.13 / 62.99 ± 0.87</td> <!-- Angry Tweets -->
   <td class="da la">4.01 ± 1.10 / 45.80 ± 2.61</td> <!-- ScaLA-da -->
   <td class="da qa">55.01 ± 0.80 / 60.67 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="no ner">56.41 ± 2.05 / 37.55 ± 3.57</td> <!-- NorNE-nb -->
   <td class="no ner">53.95 ± 1.23 / 38.44 ± 4.85</td> <!-- NorNE-nn -->
   <td class="no sent">42.27 ± 1.52 / 56.76 ± 2.10</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.21 ± 1.00 / 34.08 ± 0.56</td> <!-- ScaLA-nn -->
   <td class="no qa">29.35 ± 1.40 / 53.48 ± 2.01</td> <!-- NorQuAD -->
   <td class="sv ner">47.81 ± 2.60 / 27.94 ± 5.79</td> <!-- SUC3 -->
   <td class="sv sent">68.43 ± 2.12 / 68.82 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">3.63 ± 1.46 / 43.69 ± 4.56</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.03 ± 0.62 / 58.80 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="da-rank">2.61</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.77 ± 2.11 / 61.99 ± 2.34</td> <!-- NorQuAD -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">3.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.08</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.17</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="da ner">41.37 ± 2.50 / 24.64 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">42.60 ± 1.06 / 61.52 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">6.52 ± 1.34 / 45.01 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da qa">50.57 ± 1.03 / 57.75 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="no ner">56.33 ± 1.63 / 36.68 ± 3.27</td> <!-- NorNE-nb -->
   <td class="no ner">54.68 ± 1.29 / 37.85 ± 3.79</td> <!-- NorNE-nn -->
   <td class="no sent">37.18 ± 1.30 / 55.44 ± 1.46</td> <!-- NoReC -->
   <td class="no la">6.76 ± 2.81 / 41.69 ± 2.82</td> <!-- ScaLA-nb -->
   <td class="no la">6.79 ± 1.51 / 45.45 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">30.11 ± 2.09 / 52.56 ± 2.38</td> <!-- NorQuAD -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,004 ± 2,244 / 2,324 ± 761</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.83</td> <!-- Danish rank -->
   <td class="no-rank">3.05</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">58.49 ± 1.50 / 56.15 ± 1.57</td> <!-- DANSK -->
   <td class="da sent">37.47 ± 2.55 / 56.94 ± 3.79</td> <!-- Angry Tweets -->
   <td class="da la">6.71 ± 5.56 / 45.62 ± 6.46</td> <!-- ScaLA-da -->
   <td class="da qa">30.60 ± 1.23 / 35.52 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">82.46 ± 1.46 / 83.74 ± 1.16</td> <!-- NorNE-nb -->
   <td class="no ner">74.22 ± 0.57 / 77.50 ± 0.57</td> <!-- NorNE-nn -->
   <td class="no sent">37.19 ± 1.76 / 47.27 ± 2.85</td> <!-- NoReC -->
   <td class="no la">13.25 ± 6.73 / 48.39 ± 7.10</td> <!-- ScaLA-nb -->
   <td class="no la">7.96 ± 5.56 / 45.68 ± 6.73</td> <!-- ScaLA-nn -->
   <td class="no qa">18.75 ± 3.84 / 30.21 ± 5.73</td> <!-- NorQuAD -->
   <td class="sv ner">70.57 ± 1.07 / 70.41 ± 0.93</td> <!-- SUC3 -->
   <td class="sv sent">66.01 ± 1.43 / 57.28 ± 0.85</td> <!-- SweReC -->
   <td class="sv la">10.20 ± 5.38 / 50.80 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.71 ± 0.94 / 36.08 ± 0.92</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.63</td> <!-- Danish rank -->
   <td class="no-rank">3.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.62</td> <!-- Swedish rank -->
   <td class="da ner">39.83 ± 2.18 / 25.99 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">47.48 ± 2.00 / 63.93 ± 1.86</td> <!-- Angry Tweets -->
   <td class="da la">4.55 ± 2.34 / 42.91 ± 4.05</td> <!-- ScaLA-da -->
   <td class="da qa">49.23 ± 0.63 / 57.45 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="no ner">46.49 ± 2.30 / 31.87 ± 1.92</td> <!-- NorNE-nb -->
   <td class="no ner">51.46 ± 2.36 / 35.87 ± 2.14</td> <!-- NorNE-nn -->
   <td class="no sent">37.98 ± 1.72 / 43.91 ± 2.51</td> <!-- NoReC -->
   <td class="no la">7.86 ± 2.74 / 47.20 ± 2.71</td> <!-- ScaLA-nb -->
   <td class="no la">7.23 ± 1.97 / 46.62 ± 3.92</td> <!-- ScaLA-nn -->
   <td class="no qa">33.31 ± 1.03 / 59.27 ± 1.53</td> <!-- NorQuAD -->
   <td class="sv ner">51.45 ± 3.13 / 26.49 ± 3.00</td> <!-- SUC3 -->
   <td class="sv sent">63.64 ± 3.74 / 65.08 ± 2.46</td> <!-- SweReC -->
   <td class="sv la">5.80 ± 1.74 / 51.04 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.95 ± 1.00 / 57.09 ± 0.92</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="da-rank">2.70</td> <!-- Danish rank -->
   <td class="no-rank">3.54</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.25</td> <!-- Swedish rank -->
   <td class="da ner">37.02 ± 5.66 / 27.64 ± 3.92</td> <!-- DANSK -->
   <td class="da sent">40.65 ± 2.10 / 57.47 ± 2.56</td> <!-- Angry Tweets -->
   <td class="da la">7.48 ± 2.51 / 46.56 ± 4.52</td> <!-- ScaLA-da -->
   <td class="da qa">52.71 ± 0.70 / 59.07 ± 0.65</td> <!-- ScandiQA-da -->
   <td class="no ner">50.34 ± 3.17 / 45.09 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">52.06 ± 2.41 / 46.88 ± 2.39</td> <!-- NorNE-nn -->
   <td class="no sent">32.19 ± 2.52 / 43.19 ± 4.63</td> <!-- NoReC -->
   <td class="no la">-0.22 ± 0.43 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">20.57 ± 0.64 / 40.19 ± 1.13</td> <!-- NorQuAD -->
   <td class="sv ner">46.74 ± 4.30 / 33.57 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">77.06 ± 1.82 / 79.02 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">14.00 ± 1.59 / 53.89 ± 3.10</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.74 ± 0.52 / 63.45 ± 0.49</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="da-rank">2.57</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.76</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.64</td> <!-- Swedish rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da qa">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">44.83 ± 1.58 / 40.11 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 1.65 / 41.63 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.59 / 45.73 ± 2.82</td> <!-- NoReC -->
   <td class="no la">3.57 ± 1.55 / 37.05 ± 2.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.61 ± 2.11 / 37.85 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="da-rank">2.82</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.60</td> <!-- Swedish rank -->
   <td class="da ner">16.72 ± 2.23 / 15.96 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">45.89 ± 2.13 / 63.12 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">11.25 ± 2.33 / 51.88 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">53.17 ± 0.79 / 59.30 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="no ner">31.45 ± 1.64 / 31.64 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">33.85 ± 1.95 / 34.29 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">36.06 ± 3.96 / 52.59 ± 4.67</td> <!-- NoReC -->
   <td class="no la">8.34 ± 2.97 / 45.11 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">6.84 ± 3.88 / 45.28 ± 5.45</td> <!-- ScaLA-nn -->
   <td class="no qa">48.31 ± 4.22 / 69.39 ± 4.10</td> <!-- NorQuAD -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="da-rank">2.99</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.47</td> <!-- Swedish rank -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.23 ± 3.43 / 41.05 ± 4.38</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da qa">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.50 ± 1.29 / 42.21 ± 1.39</td> <!-- NoReC -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no qa">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">79.20 ± 1.03 / 79.87 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>12.10.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>12.10.0</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>12.10.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="da-rank">2.25</td> <!-- Danish rank -->
   <td class="no-rank">3.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.10</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="da-rank">2.96</td> <!-- Danish rank -->
   <td class="no-rank">3.24</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="da ner">33.80 ± 2.66 / 25.32 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">31.57 ± 2.65 / 46.48 ± 3.84</td> <!-- Angry Tweets -->
   <td class="da la">2.76 ± 1.76 / 44.96 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">54.20 ± 1.63 / 59.50 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">42.78 ± 1.09 / 37.34 ± 1.81</td> <!-- NorNE-nb -->
   <td class="no ner">42.85 ± 1.93 / 37.34 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">36.68 ± 2.11 / 46.78 ± 2.71</td> <!-- NoReC -->
   <td class="no la">2.39 ± 1.54 / 43.99 ± 3.66</td> <!-- ScaLA-nb -->
   <td class="no la">1.91 ± 1.37 / 44.20 ± 4.28</td> <!-- ScaLA-nn -->
   <td class="no qa">39.16 ± 2.56 / 62.28 ± 2.34</td> <!-- NorQuAD -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">2.97</td> <!-- Danish rank -->
   <td class="no-rank">3.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.51</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">2.94</td> <!-- Danish rank -->
   <td class="no-rank">2.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.88</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">2.81</td> <!-- Danish rank -->
   <td class="no-rank">3.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
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
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="da-rank">2.54</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.01</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-33b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">501 ± 50 / 238 ± 69</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da-rank">2.85</td> <!-- Danish rank -->
   <td class="no-rank">3.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">25.35 ± 3.59 / 17.77 ± 2.25</td> <!-- DANSK -->
   <td class="da sent">44.70 ± 1.80 / 60.56 ± 2.77</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.60 / 34.16 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da qa">52.29 ± 0.96 / 58.32 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">31.38 ± 5.44 / 24.32 ± 2.75</td> <!-- NorNE-nb -->
   <td class="no ner">37.84 ± 4.65 / 29.35 ± 4.10</td> <!-- NorNE-nn -->
   <td class="no sent">38.88 ± 4.12 / 54.92 ± 4.66</td> <!-- NoReC -->
   <td class="no la">3.41 ± 2.16 / 35.53 ± 2.75</td> <!-- ScaLA-nb -->
   <td class="no la">3.11 ± 1.55 / 39.80 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">30.39 ± 2.51 / 51.24 ± 2.87</td> <!-- NorQuAD -->
   <td class="sv ner">33.61 ± 6.02 / 22.18 ± 4.32</td> <!-- SUC3 -->
   <td class="sv sent">76.75 ± 1.17 / 74.66 ± 1.20</td> <!-- SweReC -->
   <td class="sv la">1.66 ± 1.36 / 33.60 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.68 ± 1.94 / 56.96 ± 1.73</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.10.0</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- ScaLA-nb version -->
   <td>12.10.0</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.10.0</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da-rank">2.73</td> <!-- Danish rank -->
   <td class="no-rank">3.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.55</td> <!-- Swedish rank -->
   <td class="da ner">28.60 ± 4.69 / 20.29 ± 3.37</td> <!-- DANSK -->
   <td class="da sent">48.71 ± 1.27 / 60.90 ± 2.95</td> <!-- Angry Tweets -->
   <td class="da la">2.30 ± 1.34 / 37.21 ± 2.50</td> <!-- ScaLA-da -->
   <td class="da qa">53.85 ± 1.73 / 58.96 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="no ner">26.76 ± 6.99 / 23.69 ± 3.73</td> <!-- NorNE-nb -->
   <td class="no ner">35.38 ± 5.87 / 27.52 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">29.22 ± 2.89 / 39.25 ± 1.86</td> <!-- NoReC -->
   <td class="no la">2.58 ± 2.68 / 36.11 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">2.79 ± 1.44 / 36.17 ± 1.51</td> <!-- ScaLA-nn -->
   <td class="no qa">34.41 ± 3.68 / 53.61 ± 4.28</td> <!-- NorQuAD -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da-rank">2.88</td> <!-- Danish rank -->
   <td class="no-rank">2.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.02</td> <!-- Swedish rank -->
   <td class="da ner">43.83 ± 1.93 / 34.03 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">29.21 ± 1.92 / 52.86 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">12.96 ± 1.67 / 55.83 ± 0.88</td> <!-- ScaLA-da -->
   <td class="da qa">49.76 ± 0.59 / 56.52 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="no ner">59.77 ± 2.77 / 56.12 ± 2.72</td> <!-- NorNE-nb -->
   <td class="no ner">60.98 ± 2.01 / 57.99 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">28.14 ± 1.90 / 49.76 ± 1.59</td> <!-- NoReC -->
   <td class="no la">14.01 ± 2.15 / 56.43 ± 1.08</td> <!-- ScaLA-nb -->
   <td class="no la">10.15 ± 1.06 / 54.56 ± 0.71</td> <!-- ScaLA-nn -->
   <td class="no qa">51.08 ± 2.83 / 74.34 ± 1.55</td> <!-- NorQuAD -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.0</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- ScaLA-nb version -->
   <td>12.10.0</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="da-rank">2.56</td> <!-- Danish rank -->
   <td class="no-rank">3.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.05</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="da-rank">3.42</td> <!-- Danish rank -->
   <td class="no-rank">3.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.41</td> <!-- Swedish rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.28 ± 3.58 / 62.78 ± 3.34</td> <!-- NorQuAD -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.95 ± 0.86 / 60.77 ± 0.75</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="da-rank">2.97</td> <!-- Danish rank -->
   <td class="no-rank">3.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.59</td> <!-- Swedish rank -->
   <td class="da ner">28.45 ± 1.61 / 22.90 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">39.09 ± 1.15 / 45.25 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.26 / 37.98 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">51.67 ± 2.31 / 57.34 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="no ner">41.64 ± 3.64 / 39.43 ± 3.55</td> <!-- NorNE-nb -->
   <td class="no ner">42.37 ± 3.13 / 40.79 ± 3.10</td> <!-- NorNE-nn -->
   <td class="no sent">33.71 ± 2.57 / 55.00 ± 1.41</td> <!-- NoReC -->
   <td class="no la">-0.19 ± 0.77 / 33.29 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.25 / 34.51 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">30.14 ± 2.44 / 50.96 ± 3.46</td> <!-- NorQuAD -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td>12.10.8</td> <!-- DANSK version -->
   <td>12.10.8</td> <!-- Angry Tweets version -->
   <td>12.10.8</td> <!-- ScaLA-da version -->
   <td>12.10.8</td> <!-- ScandiQA-da version -->
   <td>12.10.8</td> <!-- NorNE-nb version -->
   <td>12.10.8</td> <!-- NorNE-nn version -->
   <td>12.10.8</td> <!-- NoReC version -->
   <td>12.10.8</td> <!-- ScaLA-nb version -->
   <td>12.10.8</td> <!-- ScaLA-nn version -->
   <td>12.10.8</td> <!-- NorQuAD version -->
   <td>12.10.8</td> <!-- SUC3 version -->
   <td>12.10.8</td> <!-- SweReC version -->
   <td>12.10.8</td> <!-- ScaLA-sv version -->
   <td>12.10.8</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="da-rank">3.26</td> <!-- Danish rank -->
   <td class="no-rank">3.37</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.45</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.13</td> <!-- Danish rank -->
   <td class="no-rank">3.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.74</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.13</td> <!-- Danish rank -->
   <td class="no-rank">3.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.74</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="da-rank">3.31</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.61</td> <!-- Swedish rank -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da qa">51.22 ± 0.94 / 57.23 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no qa">44.62 ± 3.31 / 67.57 ± 3.03</td> <!-- NorQuAD -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.57 ± 0.94 / 56.51 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="da-rank">3.13</td> <!-- Danish rank -->
   <td class="no-rank">3.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.85</td> <!-- Swedish rank -->
   <td class="da ner">15.94 ± 1.59 / 14.05 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">32.78 ± 4.04 / 47.79 ± 5.25</td> <!-- Angry Tweets -->
   <td class="da la">7.86 ± 1.87 / 41.91 ± 2.25</td> <!-- ScaLA-da -->
   <td class="da qa">52.16 ± 0.84 / 60.27 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">23.95 ± 1.93 / 21.43 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">26.55 ± 1.50 / 25.06 ± 1.61</td> <!-- NorNE-nn -->
   <td class="no sent">40.89 ± 3.60 / 59.86 ± 3.59</td> <!-- NoReC -->
   <td class="no la">9.45 ± 1.58 / 44.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">8.32 ± 1.89 / 42.30 ± 2.78</td> <!-- ScaLA-nn -->
   <td class="no qa">43.19 ± 1.82 / 67.93 ± 1.55</td> <!-- NorQuAD -->
   <td class="sv ner">15.70 ± 1.54 / 14.65 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">68.23 ± 3.81 / 71.17 ± 3.07</td> <!-- SweReC -->
   <td class="sv la">12.39 ± 1.39 / 50.99 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.04 ± 0.97 / 60.86 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="da-rank">2.65</td> <!-- Danish rank -->
   <td class="no-rank">3.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.22</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="da-rank">3.12</td> <!-- Danish rank -->
   <td class="no-rank">3.27</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.84</td> <!-- Swedish rank -->
   <td class="da ner">4.51 ± 2.12 / 3.71 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">40.85 ± 1.26 / 59.79 ± 1.32</td> <!-- Angry Tweets -->
   <td class="da la">5.43 ± 1.74 / 46.21 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da qa">51.76 ± 0.73 / 58.44 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="no ner">52.18 ± 2.03 / 29.83 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">50.53 ± 1.49 / 31.94 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">33.30 ± 2.01 / 51.15 ± 2.93</td> <!-- NoReC -->
   <td class="no la">2.63 ± 2.56 / 40.21 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">4.00 ± 1.87 / 44.87 ± 3.17</td> <!-- ScaLA-nn -->
   <td class="no qa">37.08 ± 2.44 / 61.14 ± 2.01</td> <!-- NorQuAD -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.9.1</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.9.1</td> <!-- ScaLA-nb version -->
   <td>12.9.1</td> <!-- ScaLA-nn version -->
   <td>12.9.1</td> <!-- NorQuAD version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="da-rank">3.04</td> <!-- Danish rank -->
   <td class="no-rank">3.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="da ner">23.98 ± 3.74 / 17.18 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">38.74 ± 2.15 / 49.48 ± 3.14</td> <!-- Angry Tweets -->
   <td class="da la">1.04 ± 1.57 / 33.67 ± 0.22</td> <!-- ScaLA-da -->
   <td class="da qa">50.17 ± 0.92 / 56.29 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="no ner">22.37 ± 5.96 / 23.75 ± 3.97</td> <!-- NorNE-nb -->
   <td class="no ner">29.90 ± 4.44 / 26.84 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">35.86 ± 3.52 / 52.28 ± 3.76</td> <!-- NoReC -->
   <td class="no la">1.03 ± 2.07 / 36.12 ± 2.97</td> <!-- ScaLA-nb -->
   <td class="no la">2.92 ± 1.89 / 36.47 ± 2.72</td> <!-- ScaLA-nn -->
   <td class="no qa">34.39 ± 3.15 / 54.65 ± 3.56</td> <!-- NorQuAD -->
   <td class="sv ner">30.64 ± 4.19 / 23.90 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.02 ± 3.18 / 72.36 ± 3.96</td> <!-- SweReC -->
   <td class="sv la">1.08 ± 1.36 / 38.63 ± 3.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.72 ± 1.05 / 54.59 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-13b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,520 ± 736 / 823 ± 273</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="da-rank">2.97</td> <!-- Danish rank -->
   <td class="no-rank">3.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.71</td> <!-- Swedish rank -->
   <td class="da ner">28.72 ± 2.61 / 20.53 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">37.19 ± 3.92 / 53.63 ± 4.06</td> <!-- Angry Tweets -->
   <td class="da la">2.96 ± 1.73 / 46.67 ± 3.16</td> <!-- ScaLA-da -->
   <td class="da qa">49.53 ± 1.49 / 54.83 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="no ner">28.94 ± 5.63 / 27.01 ± 4.91</td> <!-- NorNE-nb -->
   <td class="no ner">33.83 ± 5.52 / 30.49 ± 4.07</td> <!-- NorNE-nn -->
   <td class="no sent">27.32 ± 3.13 / 38.30 ± 2.19</td> <!-- NoReC -->
   <td class="no la">1.46 ± 1.07 / 49.06 ± 1.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.59 ± 1.36 / 45.94 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no qa">25.62 ± 4.99 / 40.88 ± 7.54</td> <!-- NorQuAD -->
   <td class="sv ner">32.19 ± 4.64 / 24.93 ± 4.09</td> <!-- SUC3 -->
   <td class="sv sent">72.26 ± 6.90 / 72.58 ± 5.87</td> <!-- SweReC -->
   <td class="sv la">2.39 ± 1.29 / 48.49 ± 2.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.92 ± 2.28 / 53.44 ± 2.49</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="da-rank">3.27</td> <!-- Danish rank -->
   <td class="no-rank">3.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.66</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">2.63</td> <!-- Danish rank -->
   <td class="no-rank">3.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.40</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="da-rank">2.62</td> <!-- Danish rank -->
   <td class="no-rank">3.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.33</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.81</td> <!-- Swedish rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">15.53 ± 5.69 / 15.49 ± 5.08</td> <!-- NorNE-nb -->
   <td class="no ner">19.78 ± 4.54 / 18.86 ± 4.22</td> <!-- NorNE-nn -->
   <td class="no sent">32.89 ± 1.65 / 42.58 ± 3.16</td> <!-- NoReC -->
   <td class="no la">1.18 ± 1.00 / 33.34 ± 0.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da-rank">2.79</td> <!-- Danish rank -->
   <td class="no-rank">3.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.57</td> <!-- Swedish rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da qa">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">32.12 ± 5.17 / 32.01 ± 2.80</td> <!-- NorNE-nb -->
   <td class="no ner">36.86 ± 3.53 / 35.46 ± 3.07</td> <!-- NorNE-nn -->
   <td class="no sent">36.97 ± 1.94 / 55.08 ± 2.30</td> <!-- NoReC -->
   <td class="no la">5.27 ± 3.31 / 40.91 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">1.40 ± 1.87 / 33.64 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no qa">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="da-rank">3.11</td> <!-- Danish rank -->
   <td class="no-rank">3.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.71</td> <!-- Swedish rank -->
   <td class="da ner">24.93 ± 4.36 / 22.23 ± 3.32</td> <!-- DANSK -->
   <td class="da sent">31.65 ± 2.94 / 51.95 ± 2.92</td> <!-- Angry Tweets -->
   <td class="da la">0.06 ± 1.20 / 34.30 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da qa">51.47 ± 1.82 / 57.00 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">32.21 ± 1.63 / 31.19 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">36.62 ± 1.94 / 36.40 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">16.98 ± 3.42 / 27.01 ± 3.17</td> <!-- NoReC -->
   <td class="no la">1.57 ± 1.20 / 41.68 ± 4.20</td> <!-- ScaLA-nb -->
   <td class="no la">0.97 ± 1.79 / 40.10 ± 4.50</td> <!-- ScaLA-nn -->
   <td class="no qa">26.28 ± 1.51 / 44.62 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- ScaLA-nb version -->
   <td>12.10.5</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="da-rank">3.38</td> <!-- Danish rank -->
   <td class="no-rank">3.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.90</td> <!-- Swedish rank -->
   <td class="da ner">14.73 ± 1.84 / 14.44 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">27.14 ± 1.93 / 42.34 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">2.65 ± 1.66 / 40.63 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">46.38 ± 0.61 / 54.18 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="no ner">33.08 ± 2.22 / 34.51 ± 2.24</td> <!-- NorNE-nb -->
   <td class="no ner">38.28 ± 2.63 / 40.50 ± 2.72</td> <!-- NorNE-nn -->
   <td class="no sent">35.58 ± 2.13 / 44.49 ± 2.52</td> <!-- NoReC -->
   <td class="no la">0.82 ± 1.46 / 34.78 ± 1.54</td> <!-- ScaLA-nb -->
   <td class="no la">1.43 ± 1.70 / 34.19 ± 1.10</td> <!-- ScaLA-nn -->
   <td class="no qa">36.06 ± 1.76 / 58.71 ± 1.63</td> <!-- NorQuAD -->
   <td class="sv ner">19.04 ± 2.67 / 19.98 ± 2.64</td> <!-- SUC3 -->
   <td class="sv sent">73.34 ± 1.34 / 68.41 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.90 ± 1.74 / 44.43 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.45 ± 0.58 / 54.69 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">3.33</td> <!-- ScandEval rank -->
   <td class="da-rank">3.09</td> <!-- Danish rank -->
   <td class="no-rank">3.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.94</td> <!-- Swedish rank -->
   <td class="da ner">21.98 ± 3.33 / 18.42 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">37.77 ± 3.06 / 55.35 ± 4.51</td> <!-- Angry Tweets -->
   <td class="da la">1.26 ± 1.86 / 34.03 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">46.03 ± 1.44 / 52.54 ± 1.95</td> <!-- ScandiQA-da -->
   <td class="no ner">20.25 ± 6.26 / 20.45 ± 5.54</td> <!-- NorNE-nb -->
   <td class="no ner">28.99 ± 5.03 / 27.50 ± 4.36</td> <!-- NorNE-nn -->
   <td class="no sent">17.44 ± 3.49 / 35.51 ± 4.10</td> <!-- NoReC -->
   <td class="no la">3.20 ± 1.84 / 34.58 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">2.61 ± 1.80 / 34.49 ± 1.46</td> <!-- ScaLA-nn -->
   <td class="no qa">21.50 ± 2.60 / 40.73 ± 3.86</td> <!-- NorQuAD -->
   <td class="sv ner">27.07 ± 6.33 / 25.24 ± 4.89</td> <!-- SUC3 -->
   <td class="sv sent">61.96 ± 2.69 / 67.81 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">2.65 ± 1.46 / 40.25 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.16 ± 0.91 / 52.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.20</td> <!-- Danish rank -->
   <td class="no-rank">4.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="no ner">34.42 ± 3.22 / 27.79 ± 2.40</td> <!-- NorNE-nb -->
   <td class="no ner">35.17 ± 4.05 / 30.70 ± 3.37</td> <!-- NorNE-nn -->
   <td class="no sent">21.46 ± 5.63 / 38.36 ± 6.18</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.25 / 33.60 ± 0.50</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.58 / 34.69 ± 3.11</td> <!-- ScaLA-nn -->
   <td class="no qa">0.12 ± 0.04 / 9.85 ± 0.17</td> <!-- NorQuAD -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da-rank">3.71</td> <!-- Danish rank -->
   <td class="no-rank">3.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.04</td> <!-- Swedish rank -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da qa">50.51 ± 0.90 / 58.22 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">42.52 ± 2.05 / 68.98 ± 2.23</td> <!-- NorQuAD -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.18 ± 0.54 / 57.90 ± 0.53</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="da-rank">3.22</td> <!-- Danish rank -->
   <td class="no-rank">3.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.12</td> <!-- Swedish rank -->
   <td class="da ner">41.09 ± 1.83 / 40.40 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">27.33 ± 1.92 / 49.78 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">21.58 ± 3.92 / 59.41 ± 2.63</td> <!-- ScaLA-da -->
   <td class="da qa">20.68 ± 0.82 / 26.68 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">49.92 ± 0.61 / 49.17 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">44.37 ± 1.15 / 43.43 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">19.81 ± 2.15 / 40.90 ± 2.60</td> <!-- NoReC -->
   <td class="no la">8.64 ± 3.57 / 53.17 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">3.11 ± 1.16 / 50.44 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no qa">15.89 ± 1.29 / 26.33 ± 2.41</td> <!-- NorQuAD -->
   <td class="sv ner">38.36 ± 1.60 / 37.63 ± 1.73</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 1.72 / 56.25 ± 1.72</td> <!-- SweReC -->
   <td class="sv la">19.40 ± 5.65 / 58.63 ± 3.13</td> <!-- ScaLA-sv -->
   <td class="sv qa">19.23 ± 0.59 / 26.64 ± 0.90</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="da-rank">3.24</td> <!-- Danish rank -->
   <td class="no-rank">3.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.29</td> <!-- Swedish rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da qa">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
   <td class="no ner">39.78 ± 2.67 / 31.15 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">43.58 ± 2.49 / 36.60 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">22.01 ± 3.00 / 40.48 ± 2.81</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.35 / 44.34 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">1.45 ± 1.35 / 39.55 ± 3.53</td> <!-- ScaLA-nn -->
   <td class="no qa">32.42 ± 1.72 / 56.65 ± 0.92</td> <!-- NorQuAD -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da-rank">3.45</td> <!-- Danish rank -->
   <td class="no-rank">3.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.03</td> <!-- Swedish rank -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da qa">45.34 ± 0.88 / 51.59 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">34.91 ± 2.65 / 54.30 ± 2.96</td> <!-- NorQuAD -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.55 ± 0.85 / 51.69 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="da-rank">3.35</td> <!-- Danish rank -->
   <td class="no-rank">3.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.15</td> <!-- Swedish rank -->
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
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,027 ± 503 / 903 ± 296</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="da-rank">3.49</td> <!-- Danish rank -->
   <td class="no-rank">3.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.05</td> <!-- Swedish rank -->
   <td class="da ner">13.78 ± 2.85 / 11.90 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">42.16 ± 0.68 / 45.21 ± 0.45</td> <!-- Angry Tweets -->
   <td class="da la">3.52 ± 1.90 / 39.81 ± 3.18</td> <!-- ScaLA-da -->
   <td class="da qa">20.02 ± 2.31 / 31.67 ± 2.19</td> <!-- ScandiQA-da -->
   <td class="no ner">27.49 ± 2.13 / 24.26 ± 1.41</td> <!-- NorNE-nb -->
   <td class="no ner">32.33 ± 2.92 / 29.29 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.12 / 64.33 ± 2.80</td> <!-- NoReC -->
   <td class="no la">3.92 ± 1.56 / 45.78 ± 2.36</td> <!-- ScaLA-nb -->
   <td class="no la">4.27 ± 2.44 / 42.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">2.46 ± 0.73 / 29.01 ± 1.18</td> <!-- NorQuAD -->
   <td class="sv ner">20.97 ± 2.51 / 16.21 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 0.75 / 67.99 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.35 ± 1.63 / 38.48 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv qa">28.65 ± 2.11 / 38.84 ± 1.85</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="da-rank">3.35</td> <!-- Danish rank -->
   <td class="no-rank">3.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.10</td> <!-- Swedish rank -->
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
   <td>10.0.0</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>10.0.0</td> <!-- ScandiQA-da version -->
   <td>10.0.0</td> <!-- NorNE-nb version -->
   <td>10.0.0</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>10.0.0</td> <!-- NorQuAD version -->
   <td>10.0.0</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>10.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="da-rank">3.26</td> <!-- Danish rank -->
   <td class="no-rank">3.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.25</td> <!-- Swedish rank -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da qa">41.82 ± 2.07 / 48.91 ± 2.47</td> <!-- ScandiQA-da -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">19.10 ± 2.33 / 38.96 ± 2.78</td> <!-- NorQuAD -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.57 ± 2.45 / 41.66 ± 2.41</td> <!-- ScandiQA-sv -->
   <td>9.1.2</td> <!-- DANSK version -->
   <td>9.1.2</td> <!-- Angry Tweets version -->
   <td>9.1.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.1.2</td> <!-- NorNE-nb version -->
   <td>9.1.2</td> <!-- NorNE-nn version -->
   <td>9.1.2</td> <!-- NoReC version -->
   <td>9.1.2</td> <!-- ScaLA-nb version -->
   <td>9.1.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.1.2</td> <!-- SUC3 version -->
   <td>9.1.2</td> <!-- SweReC version -->
   <td>9.1.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="da-rank">3.44</td> <!-- Danish rank -->
   <td class="no-rank">3.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.18</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="da-rank">3.43</td> <!-- Danish rank -->
   <td class="no-rank">3.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.35</td> <!-- Swedish rank -->
   <td class="da ner">11.28 ± 0.96 / 11.02 ± 0.85</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 3.80 / 49.66 ± 3.96</td> <!-- Angry Tweets -->
   <td class="da la">2.08 ± 1.48 / 45.41 ± 3.83</td> <!-- ScaLA-da -->
   <td class="da qa">36.59 ± 1.41 / 42.03 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="no ner">24.38 ± 2.13 / 25.79 ± 2.29</td> <!-- NorNE-nb -->
   <td class="no ner">31.28 ± 1.60 / 33.48 ± 1.60</td> <!-- NorNE-nn -->
   <td class="no sent">30.88 ± 2.75 / 46.07 ± 3.07</td> <!-- NoReC -->
   <td class="no la">-0.30 ± 1.46 / 34.93 ± 1.25</td> <!-- ScaLA-nb -->
   <td class="no la">0.45 ± 0.57 / 33.74 ± 1.25</td> <!-- ScaLA-nn -->
   <td class="no qa">23.99 ± 1.59 / 42.69 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">14.84 ± 1.63 / 15.90 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 3.60 / 54.09 ± 1.46</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.21 / 34.76 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.37 ± 1.36 / 40.44 ± 1.53</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="da-rank">3.70</td> <!-- Danish rank -->
   <td class="no-rank">3.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.96</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="da-rank">3.51</td> <!-- Danish rank -->
   <td class="no-rank">3.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.28</td> <!-- Swedish rank -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da qa">38.60 ± 0.65 / 47.40 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="no ner">23.82 ± 4.25 / 22.08 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">26.04 ± 6.38 / 24.47 ± 3.69</td> <!-- NorNE-nn -->
   <td class="no sent">32.60 ± 1.84 / 47.47 ± 3.33</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.43 / 44.47 ± 2.44</td> <!-- ScaLA-nb -->
   <td class="no la">2.26 ± 2.27 / 45.41 ± 3.25</td> <!-- ScaLA-nn -->
   <td class="no qa">21.33 ± 0.98 / 42.76 ± 1.02</td> <!-- NorQuAD -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.23 ± 1.07 / 46.83 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="da-rank">3.58</td> <!-- Danish rank -->
   <td class="no-rank">3.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.24</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.74</td> <!-- Danish rank -->
   <td class="no-rank">3.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.22</td> <!-- Swedish rank -->
   <td class="da ner">26.96 ± 1.31 / 25.63 ± 1.35</td> <!-- DANSK -->
   <td class="da sent">30.13 ± 2.10 / 46.78 ± 4.49</td> <!-- Angry Tweets -->
   <td class="da la">2.01 ± 1.29 / 48.79 ± 1.65</td> <!-- ScaLA-da -->
   <td class="da qa">8.22 ± 1.11 / 16.40 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">62.71 ± 0.81 / 57.24 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.76 ± 1.03 / 17.62 ± 1.24</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.74</td> <!-- Danish rank -->
   <td class="no-rank">3.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.22</td> <!-- Swedish rank -->
   <td class="da ner">26.96 ± 1.31 / 25.63 ± 1.35</td> <!-- DANSK -->
   <td class="da sent">30.13 ± 2.10 / 46.78 ± 4.49</td> <!-- Angry Tweets -->
   <td class="da la">2.01 ± 1.29 / 48.79 ± 1.65</td> <!-- ScaLA-da -->
   <td class="da qa">8.25 ± 1.03 / 16.49 ± 1.77</td> <!-- ScandiQA-da -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">63.04 ± 0.70 / 56.50 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">8.93 ± 1.00 / 17.75 ± 1.16</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="da-rank">3.41</td> <!-- Danish rank -->
   <td class="no-rank">4.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.23</td> <!-- Swedish rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da qa">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">26.99 ± 3.92 / 24.61 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">25.74 ± 3.76 / 24.51 ± 2.96</td> <!-- NorNE-nn -->
   <td class="no sent">19.85 ± 1.97 / 35.75 ± 1.74</td> <!-- NoReC -->
   <td class="no la">1.96 ± 1.33 / 44.22 ± 2.93</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.39 / 39.57 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no qa">16.33 ± 2.17 / 31.16 ± 3.40</td> <!-- NorQuAD -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="da-rank">3.46</td> <!-- Danish rank -->
   <td class="no-rank">4.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.25</td> <!-- Swedish rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">12.10 ± 5.58 / 12.85 ± 4.80</td> <!-- NorNE-nb -->
   <td class="no ner">13.42 ± 6.02 / 13.82 ± 5.16</td> <!-- NorNE-nn -->
   <td class="no sent">22.82 ± 3.11 / 43.88 ± 3.10</td> <!-- NoReC -->
   <td class="no la">2.70 ± 2.16 / 47.68 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">2.21 ± 1.46 / 42.80 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="da-rank">3.63</td> <!-- Danish rank -->
   <td class="no-rank">4.27</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.91</td> <!-- Swedish rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da qa">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="no ner">9.06 ± 6.86 / 8.39 ± 6.41</td> <!-- NorNE-nb -->
   <td class="no ner">17.16 ± 6.21 / 16.00 ± 5.94</td> <!-- NorNE-nn -->
   <td class="no sent">25.52 ± 3.72 / 41.44 ± 4.44</td> <!-- NoReC -->
   <td class="no la">0.68 ± 1.54 / 45.09 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">0.17 ± 2.27 / 42.02 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.46 ± 0.07 / 6.96 ± 0.13</td> <!-- NorQuAD -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="da-rank">3.69</td> <!-- Danish rank -->
   <td class="no-rank">3.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.13</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="da-rank">3.54</td> <!-- Danish rank -->
   <td class="no-rank">3.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.58</td> <!-- Swedish rank -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da qa">34.79 ± 1.52 / 39.67 ± 1.69</td> <!-- ScandiQA-da -->
   <td class="no ner">27.37 ± 4.07 / 27.94 ± 4.04</td> <!-- NorNE-nb -->
   <td class="no ner">31.22 ± 3.87 / 31.39 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">34.21 ± 1.63 / 47.17 ± 2.76</td> <!-- NoReC -->
   <td class="no la">0.92 ± 1.55 / 40.71 ± 2.58</td> <!-- ScaLA-nb -->
   <td class="no la">1.25 ± 2.30 / 43.49 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">18.52 ± 2.78 / 32.10 ± 4.23</td> <!-- NorQuAD -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.70 ± 1.46 / 38.82 ± 1.54</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da-rank">3.62</td> <!-- Danish rank -->
   <td class="no-rank">3.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.80</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da-rank">3.62</td> <!-- Danish rank -->
   <td class="no-rank">4.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.63</td> <!-- Swedish rank -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">32.12 ± 1.62 / 38.99 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no qa">5.84 ± 1.36 / 16.14 ± 2.48</td> <!-- NorQuAD -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">30.81 ± 2.73 / 35.67 ± 2.95</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.82</td> <!-- ScandEval rank -->
   <td class="da-rank">3.83</td> <!-- Danish rank -->
   <td class="no-rank">4.04</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.60</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.89</td> <!-- ScandEval rank -->
   <td class="da-rank">4.06</td> <!-- Danish rank -->
   <td class="no-rank">4.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.48</td> <!-- Swedish rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.86 ± 1.65 / 50.11 ± 1.80</td> <!-- NorQuAD -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="da-rank">3.86</td> <!-- Danish rank -->
   <td class="no-rank">4.27</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.58</td> <!-- Swedish rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da qa">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">29.52 ± 1.48 / 29.79 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">31.27 ± 1.30 / 31.91 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">11.49 ± 1.38 / 27.12 ± 1.98</td> <!-- NoReC -->
   <td class="no la">0.29 ± 1.58 / 40.21 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">-0.12 ± 1.48 / 39.92 ± 3.90</td> <!-- ScaLA-nn -->
   <td class="no qa">7.80 ± 1.19 / 17.09 ± 2.72</td> <!-- NorQuAD -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="da-rank">3.94</td> <!-- Danish rank -->
   <td class="no-rank">4.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.67</td> <!-- Swedish rank -->
   <td class="da ner">33.62 ± 1.57 / 31.69 ± 1.40</td> <!-- DANSK -->
   <td class="da sent">20.71 ± 1.68 / 40.07 ± 2.65</td> <!-- Angry Tweets -->
   <td class="da la">1.19 ± 1.08 / 48.46 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da qa">4.19 ± 0.88 / 7.68 ± 1.59</td> <!-- ScandiQA-da -->
   <td class="no ner">46.11 ± 3.68 / 43.54 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">35.18 ± 4.90 / 33.22 ± 4.64</td> <!-- NorNE-nn -->
   <td class="no sent">19.19 ± 2.87 / 37.36 ± 1.97</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.42 / 50.99 ± 0.83</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 1.04 / 49.39 ± 0.80</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">26.87 ± 2.26 / 25.42 ± 2.14</td> <!-- SUC3 -->
   <td class="sv sent">57.41 ± 1.89 / 53.50 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">-1.06 ± 1.33 / 48.72 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv qa">5.54 ± 1.44 / 10.83 ± 2.62</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="da-rank">3.83</td> <!-- Danish rank -->
   <td class="no-rank">4.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.67</td> <!-- Swedish rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="no ner">34.46 ± 2.01 / 33.09 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">33.41 ± 2.21 / 33.91 ± 2.33</td> <!-- NorNE-nn -->
   <td class="no sent">6.31 ± 3.46 / 20.67 ± 2.69</td> <!-- NoReC -->
   <td class="no la">-1.59 ± 1.08 / 36.27 ± 3.71</td> <!-- ScaLA-nb -->
   <td class="no la">0.61 ± 1.41 / 38.84 ± 5.10</td> <!-- ScaLA-nn -->
   <td class="no qa">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="da-rank">3.92</td> <!-- Danish rank -->
   <td class="no-rank">4.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.66</td> <!-- Swedish rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da qa">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td class="no ner">30.79 ± 1.95 / 32.18 ± 1.98</td> <!-- NorNE-nb -->
   <td class="no ner">31.12 ± 2.36 / 33.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">9.95 ± 3.92 / 29.01 ± 2.80</td> <!-- NoReC -->
   <td class="no la">-0.95 ± 1.87 / 39.37 ± 3.33</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 1.73 / 42.36 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="da-rank">4.08</td> <!-- Danish rank -->
   <td class="no-rank">4.30</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.79</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="da-rank">4.18</td> <!-- Danish rank -->
   <td class="no-rank">4.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.95</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="da-rank">4.25</td> <!-- Danish rank -->
   <td class="no-rank">4.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.93</td> <!-- Swedish rank -->
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
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>0.0.0</td> <!-- ScandiQA-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>0.0.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="da-rank">4.23</td> <!-- Danish rank -->
   <td class="no-rank">4.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.08</td> <!-- Swedish rank -->
   <td class="da ner">13.98 ± 1.54 / 13.46 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">6.37 ± 3.38 / 25.43 ± 4.09</td> <!-- Angry Tweets -->
   <td class="da la">0.41 ± 0.80 / 33.31 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">20.46 ± 2.90 / 24.27 ± 3.23</td> <!-- ScandiQA-da -->
   <td class="no ner">27.66 ± 2.00 / 28.61 ± 2.15</td> <!-- NorNE-nb -->
   <td class="no ner">30.88 ± 2.13 / 31.97 ± 2.10</td> <!-- NorNE-nn -->
   <td class="no sent">5.13 ± 3.33 / 20.41 ± 3.12</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">7.55 ± 1.17 / 15.63 ± 2.64</td> <!-- NorQuAD -->
   <td class="sv ner">23.05 ± 2.31 / 24.35 ± 1.99</td> <!-- SUC3 -->
   <td class="sv sent">12.47 ± 7.10 / 23.03 ± 8.78</td> <!-- SweReC -->
   <td class="sv la">0.08 ± 0.16 / 33.34 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">20.43 ± 2.69 / 24.25 ± 2.67</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="da-rank">4.14</td> <!-- Danish rank -->
   <td class="no-rank">4.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.20</td> <!-- Swedish rank -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da qa">6.84 ± 6.83 / 21.33 ± 6.27</td> <!-- ScandiQA-da -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">20.84 ± 6.06 / 35.78 ± 5.94</td> <!-- NoReC -->
   <td class="no la">0.45 ± 1.09 / 34.65 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">0.48 ± 0.66 / 32.86 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">2.43 ± 0.61 / 22.78 ± 2.29</td> <!-- NorQuAD -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.82 ± 11.21 / 31.12 ± 8.39</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.34</td> <!-- ScandEval rank -->
   <td class="da-rank">4.23</td> <!-- Danish rank -->
   <td class="no-rank">4.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.27</td> <!-- Swedish rank -->
   <td class="da ner">12.82 ± 2.64 / 12.37 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">3.55 ± 3.64 / 22.75 ± 4.02</td> <!-- Angry Tweets -->
   <td class="da la">0.68 ± 1.41 / 35.13 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da qa">19.85 ± 1.75 / 24.31 ± 1.88</td> <!-- ScandiQA-da -->
   <td class="no ner">12.77 ± 3.48 / 14.13 ± 3.09</td> <!-- NorNE-nb -->
   <td class="no ner">10.51 ± 3.44 / 9.95 ± 3.51</td> <!-- NorNE-nn -->
   <td class="no sent">8.70 ± 4.43 / 25.39 ± 3.30</td> <!-- NoReC -->
   <td class="no la">0.00 ± 1.60 / 38.54 ± 3.41</td> <!-- ScaLA-nb -->
   <td class="no la">0.82 ± 1.39 / 37.77 ± 4.45</td> <!-- ScaLA-nn -->
   <td class="no qa">1.85 ± 0.82 / 10.19 ± 1.99</td> <!-- NorQuAD -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.42</td> <!-- ScandEval rank -->
   <td class="da-rank">4.45</td> <!-- Danish rank -->
   <td class="no-rank">4.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.29</td> <!-- Swedish rank -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">5.15 ± 6.60 / 17.35 ± 5.86</td> <!-- ScandiQA-da -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">20.64 ± 5.63 / 36.75 ± 3.29</td> <!-- NoReC -->
   <td class="no la">-0.99 ± 0.88 / 33.37 ± 0.27</td> <!-- ScaLA-nb -->
   <td class="no la">-0.15 ± 0.72 / 32.83 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.53 ± 0.31 / 22.14 ± 2.25</td> <!-- NorQuAD -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">4.79 ± 3.55 / 18.06 ± 2.80</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="da-rank">4.24</td> <!-- Danish rank -->
   <td class="no-rank">4.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.48</td> <!-- Swedish rank -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da qa">16.64 ± 3.32 / 19.46 ± 3.63</td> <!-- ScandiQA-da -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no qa">2.32 ± 0.68 / 6.65 ± 1.90</td> <!-- NorQuAD -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">16.40 ± 2.88 / 19.18 ± 3.18</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.61</td> <!-- ScandEval rank -->
   <td class="da-rank">4.58</td> <!-- Danish rank -->
   <td class="no-rank">4.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.37</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 12.39 ± 1.52</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 33.45 ± 0.27</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 8.92 ± 2.90</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.68</td> <!-- ScandEval rank -->
   <td class="da-rank">4.71</td> <!-- Danish rank -->
   <td class="no-rank">4.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.48</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.71</td> <!-- ScandEval rank -->
   <td class="da-rank">4.72</td> <!-- Danish rank -->
   <td class="no-rank">4.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.63</td> <!-- Swedish rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da qa">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.74 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="da-rank">4.76</td> <!-- Danish rank -->
   <td class="no-rank">4.78</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.76</td> <!-- Swedish rank -->
   <td class="da ner">1.13 ± 1.19 / 0.97 ± 1.03</td> <!-- DANSK -->
   <td class="da sent">2.06 ± 2.30 / 20.38 ± 2.71</td> <!-- Angry Tweets -->
   <td class="da la">-0.36 ± 0.97 / 41.52 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da qa">0.32 ± 0.12 / 4.20 ± 0.61</td> <!-- ScandiQA-da -->
   <td class="no ner">3.14 ± 2.12 / 2.91 ± 2.02</td> <!-- NorNE-nb -->
   <td class="no ner">3.00 ± 1.58 / 2.65 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">3.41 ± 2.11 / 14.87 ± 2.38</td> <!-- NoReC -->
   <td class="no la">0.22 ± 0.42 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.27 ± 0.79 / 38.20 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 2.27 ± 0.89</td> <!-- NorQuAD -->
   <td class="sv ner">1.47 ± 1.90 / 1.32 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">5.50 ± 4.49 / 28.77 ± 3.76</td> <!-- SweReC -->
   <td class="sv la">-2.19 ± 1.29 / 40.52 ± 3.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.10 ± 0.06 / 4.36 ± 0.44</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/qa-icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">44,889 ± 6,944 / 13,506 ± 4,256</td> <!-- Model inference speed -->
   <td class="rank">4.83</td> <!-- ScandEval rank -->
   <td class="da-rank">4.83</td> <!-- Danish rank -->
   <td class="no-rank">4.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.78</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.07 ± 0.70 / 27.86 ± 0.36</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.08 ± 0.02</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.00 ± 1.27 / 13.84 ± 2.10</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.53 ± 0.06</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-0.10 ± 1.04 / 22.69 ± 0.52</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.83</td> <!-- ScandEval rank -->
   <td class="da-rank">4.81</td> <!-- Danish rank -->
   <td class="no-rank">4.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.75</td> <!-- Swedish rank -->
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
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">4.89</td> <!-- ScandEval rank -->
   <td class="da-rank">4.83</td> <!-- Danish rank -->
   <td class="no-rank">4.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.95</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 0.04 ± 0.01</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.47 ± 0.03</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-3.60 ± 3.63 / 20.29 ± 1.99</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Mainland Scandinavian NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-oI5Lv&quot; src=&quot;https://datawrapper.dwcdn.net/oI5Lv/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
