---
layout: leaderboard
title: Germanic NLU 🇪🇺
---

<center>Last updated: 11/08/2024 09:34:54 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="germanic-nlu-test" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Icelandic tasks">Icelandic Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on German tasks">German Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Dutch tasks">Dutch Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on English tasks">English Rank</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">DANSK</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Angry Tweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish reading comprehension - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian reading comprehension - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish reading comprehension - Exact Match / F1-score">ScandiQA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic reading comprehension - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German reading comprehension - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch reading comprehension - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English reading comprehension - Exact Match / F1-score">SQuAD</span></th>
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermEval">GermEval version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SB10k">SB10k version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-de">ScaLA-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermanQuAD">GermanQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-nl">CoNLL-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Dutch Social">Dutch Social version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nl">ScaLA-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD-nl">SQuAD-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-en">CoNLL-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SST5">SST5 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-en">ScaLA-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD">SQuAD version</span></th>
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
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="da-rank">1.18</td> <!-- Danish rank -->
   <td class="no-rank">1.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.21</td> <!-- Swedish rank -->
   <td class="is-rank">1.81</td> <!-- Icelandic rank -->
   <td class="de-rank">1.36</td> <!-- German rank -->
   <td class="nl-rank">1.75</td> <!-- Dutch rank -->
   <td class="en-rank">1.31</td> <!-- English rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">56.43 ± 2.98 / 68.46 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no rc">47.50 ± 2.86 / 75.24 ± 1.32</td> <!-- NorQuAD -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="is ner">78.67 ± 2.16 / 59.54 ± 4.85</td> <!-- MIM-GOLD-NER -->
   <td class="is la">33.65 ± 3.19 / 60.56 ± 2.35</td> <!-- ScaLA-is -->
   <td class="is rc">32.25 ± 2.01 / 60.12 ± 1.31</td> <!-- NQiI -->
   <td class="de ner">69.48 ± 2.32 / 54.66 ± 2.17</td> <!-- GermEval -->
   <td class="de sent">64.91 ± 1.86 / 75.96 ± 1.59</td> <!-- SB10k -->
   <td class="de la">50.23 ± 4.16 / 74.54 ± 2.10</td> <!-- ScaLA-de -->
   <td class="de rc">33.17 ± 1.86 / 65.14 ± 1.53</td> <!-- GermanQuAD -->
   <td class="nl ner">73.35 ± 2.61 / 56.00 ± 2.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.92 ± 2.78 / 40.80 ± 2.43</td> <!-- Dutch Social -->
   <td class="nl la">76.70 ± 2.39 / 88.16 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.03 ± 1.96 / 76.47 ± 1.22</td> <!-- SQuAD-nl -->
   <td class="en ner">78.06 ± 2.73 / 70.76 ± 3.80</td> <!-- CoNLL-en -->
   <td class="en sent">69.06 ± 2.20 / 76.04 ± 1.60</td> <!-- SST5 -->
   <td class="en la">55.76 ± 3.84 / 76.34 ± 1.44</td> <!-- ScaLA-en -->
   <td class="en rc">67.35 ± 1.98 / 85.76 ± 0.77</td> <!-- SQuAD -->
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
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.2.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.2.0</td> <!-- ScaLA-en version -->
   <td>12.2.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.45</td> <!-- ScandEval rank -->
   <td class="da-rank">1.26</td> <!-- Danish rank -->
   <td class="no-rank">1.42</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.27</td> <!-- Swedish rank -->
   <td class="is-rank">1.30</td> <!-- Icelandic rank -->
   <td class="de-rank">1.52</td> <!-- German rank -->
   <td class="nl-rank">2.04</td> <!-- Dutch rank -->
   <td class="en-rank">1.35</td> <!-- English rank -->
   <td class="da ner">66.80 ± 3.01 / 45.69 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">61.62 ± 2.17 / 73.99 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">66.84 ± 3.27 / 82.79 ± 1.86</td> <!-- ScaLA-da -->
   <td class="da rc">56.85 ± 2.62 / 68.83 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="no ner">77.48 ± 2.32 / 55.87 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">78.70 ± 2.78 / 57.58 ± 4.23</td> <!-- NorNE-nn -->
   <td class="no sent">62.55 ± 2.82 / 72.41 ± 2.42</td> <!-- NoReC -->
   <td class="no la">74.45 ± 4.27 / 86.22 ± 2.49</td> <!-- ScaLA-nb -->
   <td class="no la">56.31 ± 5.81 / 74.04 ± 4.03</td> <!-- ScaLA-nn -->
   <td class="no rc">44.67 ± 3.23 / 73.39 ± 1.83</td> <!-- NorQuAD -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="de ner">68.94 ± 2.50 / 44.89 ± 2.85</td> <!-- GermEval -->
   <td class="de sent">60.47 ± 2.94 / 72.79 ± 1.90</td> <!-- SB10k -->
   <td class="de la">51.26 ± 4.94 / 74.76 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">30.04 ± 1.30 / 58.77 ± 1.50</td> <!-- GermanQuAD -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.22 ± 3.26 / 33.41 ± 3.24</td> <!-- Dutch Social -->
   <td class="nl la">72.30 ± 2.26 / 85.96 ± 1.13</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="en ner">81.79 ± 1.39 / 65.51 ± 4.16</td> <!-- CoNLL-en -->
   <td class="en sent">67.55 ± 2.34 / 74.04 ± 1.80</td> <!-- SST5 -->
   <td class="en la">51.21 ± 4.96 / 75.11 ± 2.42</td> <!-- ScaLA-en -->
   <td class="en rc">66.60 ± 1.45 / 84.48 ± 0.76</td> <!-- SQuAD -->
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
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.3.2</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="da-rank">1.57</td> <!-- Danish rank -->
   <td class="no-rank">1.37</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.41</td> <!-- Swedish rank -->
   <td class="is-rank">1.52</td> <!-- Icelandic rank -->
   <td class="de-rank">1.21</td> <!-- German rank -->
   <td class="nl-rank">2.39</td> <!-- Dutch rank -->
   <td class="en-rank">1.39</td> <!-- English rank -->
   <td class="da ner">70.19 ± 3.34 / 66.64 ± 2.68</td> <!-- DANSK -->
   <td class="da sent">50.19 ± 1.82 / 66.32 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">69.72 ± 2.25 / 84.30 ± 1.64</td> <!-- ScaLA-da -->
   <td class="da rc">39.85 ± 8.97 / 44.44 ± 9.99</td> <!-- ScandiQA-da -->
   <td class="no ner">88.70 ± 2.05 / 84.95 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">86.11 ± 1.67 / 82.16 ± 1.96</td> <!-- NorNE-nn -->
   <td class="no sent">54.19 ± 3.15 / 65.18 ± 4.55</td> <!-- NoReC -->
   <td class="no la">69.83 ± 2.01 / 84.72 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">54.84 ± 12.59 / 75.13 ± 9.44</td> <!-- ScaLA-nn -->
   <td class="no rc">58.18 ± 1.84 / 71.29 ± 1.51</td> <!-- NorQuAD -->
   <td class="sv ner">78.23 ± 1.53 / 72.58 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">75.99 ± 1.15 / 71.01 ± 4.17</td> <!-- SweReC -->
   <td class="sv la">72.17 ± 0.94 / 85.94 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.00 ± 2.13 / 51.05 ± 2.40</td> <!-- ScandiQA-sv -->
   <td class="is ner">78.05 ± 1.72 / 78.74 ± 1.41</td> <!-- MIM-GOLD-NER -->
   <td class="is la">48.29 ± 2.59 / 73.54 ± 1.99</td> <!-- ScaLA-is -->
   <td class="is rc">29.38 ± 1.81 / 52.42 ± 3.00</td> <!-- NQiI -->
   <td class="de ner">77.62 ± 0.80 / 76.16 ± 0.79</td> <!-- GermEval -->
   <td class="de sent">60.65 ± 2.10 / 73.52 ± 1.58</td> <!-- SB10k -->
   <td class="de la">62.60 ± 2.16 / 81.12 ± 1.14</td> <!-- ScaLA-de -->
   <td class="de rc">33.62 ± 1.34 / 60.41 ± 1.36</td> <!-- GermanQuAD -->
   <td class="nl ner">75.49 ± 1.75 / 81.37 ± 1.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.79 ± 3.93 / 27.49 ± 2.37</td> <!-- Dutch Social -->
   <td class="nl la">66.47 ± 2.04 / 83.16 ± 1.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.70 ± 1.62 / 68.38 ± 1.47</td> <!-- SQuAD-nl -->
   <td class="en ner">90.17 ± 0.50 / 89.85 ± 0.49</td> <!-- CoNLL-en -->
   <td class="en sent">51.74 ± 10.59 / 58.97 ± 6.34</td> <!-- SST5 -->
   <td class="en la">55.55 ± 1.66 / 77.55 ± 0.89</td> <!-- ScaLA-en -->
   <td class="en rc">69.02 ± 1.23 / 81.57 ± 1.05</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="da-rank">1.39</td> <!-- Danish rank -->
   <td class="no-rank">1.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.27</td> <!-- Swedish rank -->
   <td class="is-rank">1.30</td> <!-- Icelandic rank -->
   <td class="de-rank">1.68</td> <!-- German rank -->
   <td class="nl-rank">2.19</td> <!-- Dutch rank -->
   <td class="en-rank">1.48</td> <!-- English rank -->
   <td class="da ner">71.15 ± 2.89 / 52.24 ± 3.76</td> <!-- DANSK -->
   <td class="da sent">49.42 ± 3.29 / 61.74 ± 2.59</td> <!-- Angry Tweets -->
   <td class="da la">64.59 ± 2.97 / 79.93 ± 1.88</td> <!-- ScaLA-da -->
   <td class="da rc">57.35 ± 2.51 / 67.87 ± 1.75</td> <!-- ScandiQA-da -->
   <td class="no ner">79.07 ± 3.01 / 64.17 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">81.56 ± 2.45 / 64.06 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">66.66 ± 1.91 / 77.70 ± 1.29</td> <!-- NoReC -->
   <td class="no la">64.53 ± 6.09 / 79.17 ± 4.89</td> <!-- ScaLA-nb -->
   <td class="no la">54.70 ± 4.36 / 74.94 ± 3.26</td> <!-- ScaLA-nn -->
   <td class="no rc">43.51 ± 3.40 / 74.52 ± 1.79</td> <!-- NorQuAD -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="is ner">81.19 ± 2.45 / 54.02 ± 5.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is rc">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="de ner">69.99 ± 1.63 / 45.58 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">54.82 ± 2.19 / 68.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">43.66 ± 5.67 / 64.64 ± 4.65</td> <!-- ScaLA-de -->
   <td class="de rc">30.06 ± 1.04 / 60.77 ± 1.11</td> <!-- GermanQuAD -->
   <td class="nl ner">76.75 ± 3.44 / 61.13 ± 4.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 2.24 / 32.52 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">56.26 ± 4.51 / 73.83 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.55 ± 2.54 / 76.28 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="en ner">83.48 ± 1.52 / 75.51 ± 2.26</td> <!-- CoNLL-en -->
   <td class="en sent">62.74 ± 2.04 / 71.28 ± 1.46</td> <!-- SST5 -->
   <td class="en la">46.56 ± 3.35 / 71.13 ± 1.97</td> <!-- ScaLA-en -->
   <td class="en rc">65.41 ± 1.96 / 84.78 ± 0.68</td> <!-- SQuAD -->
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
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="da-rank">1.34</td> <!-- Danish rank -->
   <td class="no-rank">1.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.26</td> <!-- Swedish rank -->
   <td class="is-rank">2.21</td> <!-- Icelandic rank -->
   <td class="de-rank">1.46</td> <!-- German rank -->
   <td class="nl-rank">1.91</td> <!-- Dutch rank -->
   <td class="en-rank">1.42</td> <!-- English rank -->
   <td class="da ner">63.62 ± 3.74 / 53.29 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">60.19 ± 3.31 / 73.13 ± 2.17</td> <!-- Angry Tweets -->
   <td class="da la">50.07 ± 5.86 / 72.94 ± 4.16</td> <!-- ScaLA-da -->
   <td class="da rc">60.97 ± 2.76 / 66.71 ± 2.27</td> <!-- ScandiQA-da -->
   <td class="no ner">75.31 ± 3.84 / 64.90 ± 4.05</td> <!-- NorNE-nb -->
   <td class="no ner">75.94 ± 4.62 / 62.81 ± 5.25</td> <!-- NorNE-nn -->
   <td class="no sent">66.74 ± 4.50 / 74.89 ± 3.69</td> <!-- NoReC -->
   <td class="no la">59.82 ± 3.52 / 79.17 ± 2.10</td> <!-- ScaLA-nb -->
   <td class="no la">47.56 ± 3.52 / 71.91 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no rc">60.87 ± 4.82 / 82.30 ± 2.52</td> <!-- NorQuAD -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="is ner">75.33 ± 3.06 / 62.43 ± 3.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">14.89 ± 3.28 / 51.55 ± 4.71</td> <!-- ScaLA-is -->
   <td class="is rc">34.36 ± 2.87 / 64.02 ± 2.94</td> <!-- NQiI -->
   <td class="de ner">69.04 ± 2.51 / 61.10 ± 3.39</td> <!-- GermEval -->
   <td class="de sent">63.51 ± 2.57 / 75.01 ± 1.74</td> <!-- SB10k -->
   <td class="de la">37.41 ± 2.43 / 67.63 ± 1.05</td> <!-- ScaLA-de -->
   <td class="de rc">38.29 ± 3.54 / 69.69 ± 2.78</td> <!-- GermanQuAD -->
   <td class="nl ner">72.91 ± 3.24 / 68.06 ± 4.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">19.08 ± 3.37 / 42.04 ± 2.31</td> <!-- Dutch Social -->
   <td class="nl la">54.33 ± 3.49 / 75.54 ± 2.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.99 ± 2.07 / 77.63 ± 1.16</td> <!-- SQuAD-nl -->
   <td class="en ner">79.06 ± 2.34 / 74.41 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">65.53 ± 2.61 / 68.71 ± 2.08</td> <!-- SST5 -->
   <td class="en la">46.28 ± 4.01 / 72.38 ± 2.33</td> <!-- ScaLA-en -->
   <td class="en rc">75.20 ± 1.68 / 86.90 ± 1.14</td> <!-- SQuAD -->
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
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="da-rank">1.66</td> <!-- Danish rank -->
   <td class="no-rank">1.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.46</td> <!-- Swedish rank -->
   <td class="is-rank">1.21</td> <!-- Icelandic rank -->
   <td class="de-rank">1.66</td> <!-- German rank -->
   <td class="nl-rank">2.34</td> <!-- Dutch rank -->
   <td class="en-rank">1.37</td> <!-- English rank -->
   <td class="da ner">72.90 ± 2.53 / 67.41 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">43.38 ± 3.20 / 60.05 ± 4.33</td> <!-- Angry Tweets -->
   <td class="da la">67.05 ± 1.41 / 83.18 ± 0.80</td> <!-- ScaLA-da -->
   <td class="da rc">42.15 ± 2.12 / 47.97 ± 1.99</td> <!-- ScandiQA-da -->
   <td class="no ner">91.90 ± 0.54 / 89.55 ± 0.57</td> <!-- NorNE-nb -->
   <td class="no ner">86.81 ± 1.35 / 83.46 ± 1.68</td> <!-- NorNE-nn -->
   <td class="no sent">53.69 ± 4.28 / 63.69 ± 6.95</td> <!-- NoReC -->
   <td class="no la">70.55 ± 1.64 / 84.79 ± 0.86</td> <!-- ScaLA-nb -->
   <td class="no la">61.21 ± 1.20 / 79.87 ± 0.76</td> <!-- ScaLA-nn -->
   <td class="no rc">48.82 ± 1.20 / 63.72 ± 1.06</td> <!-- NorQuAD -->
   <td class="sv ner">78.84 ± 2.19 / 72.86 ± 2.04</td> <!-- SUC3 -->
   <td class="sv sent">75.24 ± 0.99 / 72.06 ± 2.67</td> <!-- SweReC -->
   <td class="sv la">72.30 ± 1.04 / 85.77 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.74 ± 1.04 / 50.62 ± 0.85</td> <!-- ScandiQA-sv -->
   <td class="is ner">81.12 ± 2.02 / 81.48 ± 1.69</td> <!-- MIM-GOLD-NER -->
   <td class="is la">54.11 ± 2.40 / 76.46 ± 1.28</td> <!-- ScaLA-is -->
   <td class="is rc">30.93 ± 0.96 / 56.17 ± 1.10</td> <!-- NQiI -->
   <td class="de ner">77.42 ± 1.30 / 76.39 ± 1.16</td> <!-- GermEval -->
   <td class="de sent">50.90 ± 6.20 / 66.89 ± 4.34</td> <!-- SB10k -->
   <td class="de la">59.38 ± 2.00 / 79.12 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">20.28 ± 1.15 / 42.79 ± 1.37</td> <!-- GermanQuAD -->
   <td class="nl ner">84.47 ± 1.84 / 87.98 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.16 ± 5.21 / 27.85 ± 3.29</td> <!-- Dutch Social -->
   <td class="nl la">71.23 ± 1.62 / 85.45 ± 0.83</td> <!-- ScaLA-nl -->
   <td class="nl rc">46.43 ± 0.72 / 57.80 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="en ner">91.83 ± 0.50 / 91.40 ± 0.43</td> <!-- CoNLL-en -->
   <td class="en sent">53.75 ± 1.47 / 56.40 ± 2.82</td> <!-- SST5 -->
   <td class="en la">62.11 ± 1.53 / 80.67 ± 0.77</td> <!-- ScaLA-en -->
   <td class="en rc">62.10 ± 1.03 / 73.26 ± 0.85</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="da-rank">1.54</td> <!-- Danish rank -->
   <td class="no-rank">1.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.44</td> <!-- Swedish rank -->
   <td class="is-rank">2.94</td> <!-- Icelandic rank -->
   <td class="de-rank">1.36</td> <!-- German rank -->
   <td class="nl-rank">1.43</td> <!-- Dutch rank -->
   <td class="en-rank">1.29</td> <!-- English rank -->
   <td class="da ner">69.50 ± 1.78 / 65.03 ± 1.31</td> <!-- DANSK -->
   <td class="da sent">55.07 ± 1.53 / 69.43 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">57.67 ± 2.56 / 78.48 ± 1.32</td> <!-- ScaLA-da -->
   <td class="da rc">46.71 ± 1.25 / 52.84 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">89.86 ± 0.93 / 90.64 ± 0.80</td> <!-- NorNE-nb -->
   <td class="no ner">84.32 ± 1.08 / 86.52 ± 0.94</td> <!-- NorNE-nn -->
   <td class="no sent">61.52 ± 1.87 / 72.72 ± 1.95</td> <!-- NoReC -->
   <td class="no la">62.34 ± 2.48 / 79.94 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">34.88 ± 11.23 / 66.51 ± 5.72</td> <!-- ScaLA-nn -->
   <td class="no rc">53.01 ± 1.05 / 70.46 ± 0.86</td> <!-- NorQuAD -->
   <td class="sv ner">80.36 ± 1.12 / 78.57 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">79.65 ± 1.05 / 78.90 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">63.15 ± 1.65 / 81.06 ± 0.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.99 ± 1.18 / 53.49 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">78.43 ± 1.53 / 79.30 ± 1.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">10.78 ± 7.04 / 53.28 ± 3.97</td> <!-- ScaLA-is -->
   <td class="is rc">13.79 ± 0.96 / 54.20 ± 1.31</td> <!-- NQiI -->
   <td class="de ner">79.73 ± 1.38 / 78.52 ± 1.44</td> <!-- GermEval -->
   <td class="de sent">64.78 ± 1.34 / 76.30 ± 0.98</td> <!-- SB10k -->
   <td class="de la">47.24 ± 13.67 / 71.51 ± 8.03</td> <!-- ScaLA-de -->
   <td class="de rc">28.11 ± 0.94 / 54.87 ± 1.08</td> <!-- GermanQuAD -->
   <td class="nl ner">82.31 ± 2.14 / 86.91 ± 1.34</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.64 ± 2.91 / 49.90 ± 3.42</td> <!-- Dutch Social -->
   <td class="nl la">58.51 ± 4.12 / 78.17 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.32 ± 1.91 / 57.53 ± 1.78</td> <!-- SQuAD-nl -->
   <td class="en ner">91.69 ± 0.67 / 91.29 ± 0.54</td> <!-- CoNLL-en -->
   <td class="en sent">64.37 ± 1.28 / 65.16 ± 2.10</td> <!-- SST5 -->
   <td class="en la">53.58 ± 10.20 / 74.70 ± 7.53</td> <!-- ScaLA-en -->
   <td class="en rc">60.47 ± 1.61 / 73.00 ± 1.37</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">1.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.62</td> <!-- Swedish rank -->
   <td class="is-rank">2.22</td> <!-- Icelandic rank -->
   <td class="de-rank">1.54</td> <!-- German rank -->
   <td class="nl-rank">1.52</td> <!-- Dutch rank -->
   <td class="en-rank">1.60</td> <!-- English rank -->
   <td class="da ner">71.24 ± 1.63 / 66.41 ± 1.64</td> <!-- DANSK -->
   <td class="da sent">46.50 ± 1.57 / 64.31 ± 1.21</td> <!-- Angry Tweets -->
   <td class="da la">52.92 ± 4.42 / 75.11 ± 3.22</td> <!-- ScaLA-da -->
   <td class="da rc">40.08 ± 1.22 / 45.40 ± 1.14</td> <!-- ScandiQA-da -->
   <td class="no ner">90.58 ± 0.91 / 87.84 ± 1.00</td> <!-- NorNE-nb -->
   <td class="no ner">85.21 ± 1.05 / 81.57 ± 1.30</td> <!-- NorNE-nn -->
   <td class="no sent">54.26 ± 1.75 / 67.25 ± 1.47</td> <!-- NoReC -->
   <td class="no la">59.44 ± 1.47 / 78.80 ± 1.00</td> <!-- ScaLA-nb -->
   <td class="no la">49.30 ± 1.39 / 74.02 ± 1.04</td> <!-- ScaLA-nn -->
   <td class="no rc">46.42 ± 1.44 / 61.82 ± 1.47</td> <!-- NorQuAD -->
   <td class="sv ner">77.78 ± 1.69 / 72.08 ± 1.81</td> <!-- SUC3 -->
   <td class="sv sent">73.58 ± 1.37 / 70.43 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">60.36 ± 2.98 / 79.72 ± 1.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">41.71 ± 1.08 / 47.07 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="is ner">80.45 ± 1.29 / 81.01 ± 1.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">36.92 ± 7.62 / 66.07 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is rc">11.75 ± 0.66 / 46.17 ± 1.42</td> <!-- NQiI -->
   <td class="de ner">79.44 ± 0.96 / 78.42 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">58.65 ± 1.67 / 72.12 ± 1.18</td> <!-- SB10k -->
   <td class="de la">52.19 ± 2.96 / 74.17 ± 1.82</td> <!-- ScaLA-de -->
   <td class="de rc">23.66 ± 0.97 / 45.11 ± 1.50</td> <!-- GermanQuAD -->
   <td class="nl ner">82.02 ± 1.04 / 84.71 ± 0.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">33.99 ± 4.05 / 50.69 ± 4.23</td> <!-- Dutch Social -->
   <td class="nl la">60.77 ± 1.53 / 79.80 ± 0.87</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.55 ± 1.08 / 51.73 ± 1.18</td> <!-- SQuAD-nl -->
   <td class="en ner">90.33 ± 0.62 / 90.31 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">52.93 ± 1.41 / 58.98 ± 1.52</td> <!-- SST5 -->
   <td class="en la">50.70 ± 2.70 / 74.17 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en rc">53.77 ± 0.57 / 65.07 ± 0.61</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="da-rank">1.66</td> <!-- Danish rank -->
   <td class="no-rank">1.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.60</td> <!-- Swedish rank -->
   <td class="is-rank">2.36</td> <!-- Icelandic rank -->
   <td class="de-rank">1.25</td> <!-- German rank -->
   <td class="nl-rank">2.21</td> <!-- Dutch rank -->
   <td class="en-rank">1.70</td> <!-- English rank -->
   <td class="da ner">72.74 ± 2.58 / 67.15 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">48.33 ± 4.44 / 63.94 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">57.30 ± 14.90 / 76.82 ± 8.67</td> <!-- ScaLA-da -->
   <td class="da rc">43.57 ± 3.28 / 49.29 ± 3.35</td> <!-- ScandiQA-da -->
   <td class="no ner">91.66 ± 1.24 / 89.34 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">86.19 ± 0.97 / 82.86 ± 1.29</td> <!-- NorNE-nn -->
   <td class="no sent">50.25 ± 15.36 / 63.55 ± 13.05</td> <!-- NoReC -->
   <td class="no la">55.51 ± 18.28 / 74.00 ± 13.38</td> <!-- ScaLA-nb -->
   <td class="no la">43.89 ± 14.81 / 68.88 ± 10.32</td> <!-- ScaLA-nn -->
   <td class="no rc">57.57 ± 2.43 / 72.69 ± 2.22</td> <!-- NorQuAD -->
   <td class="sv ner">80.33 ± 2.50 / 75.03 ± 3.79</td> <!-- SUC3 -->
   <td class="sv sent">76.63 ± 0.98 / 74.25 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">49.72 ± 19.88 / 69.94 ± 13.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.64 ± 1.42 / 52.21 ± 1.45</td> <!-- ScandiQA-sv -->
   <td class="is ner">82.83 ± 1.09 / 83.16 ± 1.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">22.78 ± 12.25 / 57.07 ± 8.18</td> <!-- ScaLA-is -->
   <td class="is rc">15.72 ± 1.39 / 55.29 ± 1.30</td> <!-- NQiI -->
   <td class="de ner">80.64 ± 0.81 / 80.03 ± 0.97</td> <!-- GermEval -->
   <td class="de sent">63.02 ± 1.62 / 75.25 ± 1.08</td> <!-- SB10k -->
   <td class="de la">54.83 ± 9.12 / 76.02 ± 5.19</td> <!-- ScaLA-de -->
   <td class="de rc">29.09 ± 1.00 / 55.68 ± 1.11</td> <!-- GermanQuAD -->
   <td class="nl ner">83.49 ± 1.51 / 86.12 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.82 ± 7.93 / 30.82 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">64.80 ± 8.79 / 80.93 ± 6.29</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.72 ± 1.20 / 61.66 ± 1.16</td> <!-- SQuAD-nl -->
   <td class="en ner">89.81 ± 0.60 / 89.25 ± 0.72</td> <!-- CoNLL-en -->
   <td class="en sent">41.97 ± 17.48 / 50.33 ± 9.16</td> <!-- SST5 -->
   <td class="en la">35.55 ± 18.61 / 63.79 ± 12.17</td> <!-- ScaLA-en -->
   <td class="en rc">68.88 ± 1.40 / 79.18 ± 1.17</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="da-rank">1.84</td> <!-- Danish rank -->
   <td class="no-rank">1.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.55</td> <!-- Swedish rank -->
   <td class="is-rank">2.94</td> <!-- Icelandic rank -->
   <td class="de-rank">1.32</td> <!-- German rank -->
   <td class="nl-rank">1.74</td> <!-- Dutch rank -->
   <td class="en-rank">1.27</td> <!-- English rank -->
   <td class="da ner">69.86 ± 1.64 / 65.30 ± 1.46</td> <!-- DANSK -->
   <td class="da sent">55.45 ± 1.57 / 69.74 ± 1.66</td> <!-- Angry Tweets -->
   <td class="da la">31.14 ± 18.61 / 63.23 ± 10.14</td> <!-- ScaLA-da -->
   <td class="da rc">45.51 ± 2.60 / 52.75 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">89.27 ± 1.00 / 90.42 ± 0.65</td> <!-- NorNE-nb -->
   <td class="no ner">83.78 ± 1.53 / 86.17 ± 1.36</td> <!-- NorNE-nn -->
   <td class="no sent">63.35 ± 0.63 / 74.20 ± 0.91</td> <!-- NoReC -->
   <td class="no la">55.71 ± 11.72 / 77.00 ± 5.84</td> <!-- ScaLA-nb -->
   <td class="no la">12.32 ± 12.70 / 53.74 ± 7.38</td> <!-- ScaLA-nn -->
   <td class="no rc">38.74 ± 7.61 / 58.52 ± 7.90</td> <!-- NorQuAD -->
   <td class="sv ner">79.50 ± 0.96 / 77.37 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">79.48 ± 0.87 / 77.47 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">53.01 ± 15.20 / 75.97 ± 7.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.68 ± 1.62 / 53.19 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="is ner">78.32 ± 1.32 / 79.70 ± 1.08</td> <!-- MIM-GOLD-NER -->
   <td class="is la">8.11 ± 3.77 / 50.71 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">13.93 ± 1.14 / 53.59 ± 1.62</td> <!-- NQiI -->
   <td class="de ner">79.77 ± 1.22 / 78.93 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">65.72 ± 1.70 / 76.73 ± 1.23</td> <!-- SB10k -->
   <td class="de la">49.82 ± 10.56 / 73.61 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">28.42 ± 1.71 / 55.35 ± 1.55</td> <!-- GermanQuAD -->
   <td class="nl ner">83.68 ± 1.57 / 87.38 ± 1.03</td> <!-- CoNLL-nl -->
   <td class="nl sent">27.19 ± 6.73 / 45.37 ± 6.25</td> <!-- Dutch Social -->
   <td class="nl la">51.80 ± 10.91 / 75.02 ± 5.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">46.07 ± 1.33 / 58.70 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="en ner">91.43 ± 0.52 / 91.15 ± 0.44</td> <!-- CoNLL-en -->
   <td class="en sent">66.42 ± 1.01 / 64.56 ± 1.33</td> <!-- SST5 -->
   <td class="en la">53.05 ± 12.06 / 75.49 ± 6.21</td> <!-- ScaLA-en -->
   <td class="en rc">61.34 ± 1.79 / 74.85 ± 1.26</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (zero-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,038 ± 338 / 125 ± 44</td> <!-- Model inference speed -->
   <td class="rank">1.81</td> <!-- ScandEval rank -->
   <td class="da-rank">1.72</td> <!-- Danish rank -->
   <td class="no-rank">1.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.46</td> <!-- Swedish rank -->
   <td class="is-rank">1.93</td> <!-- Icelandic rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.28</td> <!-- Dutch rank -->
   <td class="en-rank">1.43</td> <!-- English rank -->
   <td class="da ner">70.01 ± 1.46 / 44.46 ± 1.11</td> <!-- DANSK -->
   <td class="da sent">38.62 ± 0.60 / 57.57 ± 0.47</td> <!-- Angry Tweets -->
   <td class="da la">63.79 ± 0.65 / 80.48 ± 0.38</td> <!-- ScaLA-da -->
   <td class="da rc">51.16 ± 0.67 / 63.82 ± 0.45</td> <!-- ScandiQA-da -->
   <td class="no ner">78.32 ± 1.01 / 53.24 ± 1.12</td> <!-- NorNE-nb -->
   <td class="no ner">76.39 ± 0.99 / 51.27 ± 1.07</td> <!-- NorNE-nn -->
   <td class="no sent">43.76 ± 0.65 / 62.74 ± 0.49</td> <!-- NoReC -->
   <td class="no la">69.31 ± 0.93 / 83.44 ± 0.54</td> <!-- ScaLA-nb -->
   <td class="no la">53.80 ± 0.52 / 73.43 ± 0.38</td> <!-- ScaLA-nn -->
   <td class="no rc">42.90 ± 0.61 / 73.26 ± 0.40</td> <!-- NorQuAD -->
   <td class="sv ner">72.20 ± 0.93 / 42.33 ± 0.96</td> <!-- SUC3 -->
   <td class="sv sent">78.97 ± 0.73 / 79.52 ± 0.60</td> <!-- SweReC -->
   <td class="sv la">64.97 ± 0.71 / 81.63 ± 0.38</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.43 ± 0.47 / 64.54 ± 0.32</td> <!-- ScandiQA-sv -->
   <td class="is ner">69.43 ± 0.59 / 33.00 ± 0.65</td> <!-- MIM-GOLD-NER -->
   <td class="is la">41.94 ± 1.30 / 68.25 ± 0.58</td> <!-- ScaLA-is -->
   <td class="is rc">24.44 ± 0.70 / 47.20 ± 0.62</td> <!-- NQiI -->
   <td class="de ner">73.26 ± 0.73 / 38.24 ± 0.63</td> <!-- GermEval -->
   <td class="de sent">51.03 ± 1.01 / 67.12 ± 0.78</td> <!-- SB10k -->
   <td class="de la">28.67 ± 1.24 / 57.93 ± 0.71</td> <!-- ScaLA-de -->
   <td class="de rc">25.84 ± 0.64 / 54.34 ± 0.44</td> <!-- GermanQuAD -->
   <td class="nl ner">64.16 ± 1.72 / 33.82 ± 0.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.08 ± 1.64 / 35.80 ± 0.97</td> <!-- Dutch Social -->
   <td class="nl la">63.41 ± 0.93 / 81.39 ± 0.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.53 ± 0.49 / 71.50 ± 0.29</td> <!-- SQuAD-nl -->
   <td class="en ner">79.15 ± 0.47 / 70.67 ± 0.64</td> <!-- CoNLL-en -->
   <td class="en sent">65.20 ± 0.66 / 70.31 ± 0.45</td> <!-- SST5 -->
   <td class="en la">53.91 ± 1.08 / 75.95 ± 0.55</td> <!-- ScaLA-en -->
   <td class="en rc">61.28 ± 0.46 / 82.98 ± 0.27</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.88</td> <!-- ScandEval rank -->
   <td class="da-rank">1.57</td> <!-- Danish rank -->
   <td class="no-rank">1.78</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.48</td> <!-- Swedish rank -->
   <td class="is-rank">2.53</td> <!-- Icelandic rank -->
   <td class="de-rank">1.83</td> <!-- German rank -->
   <td class="nl-rank">2.37</td> <!-- Dutch rank -->
   <td class="en-rank">1.59</td> <!-- English rank -->
   <td class="da ner">61.31 ± 2.34 / 49.86 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">52.52 ± 2.05 / 68.10 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">57.63 ± 2.80 / 77.01 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da rc">57.03 ± 1.95 / 65.51 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no rc">45.35 ± 2.97 / 73.47 ± 1.69</td> <!-- NorQuAD -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is rc">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de rc">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en rc">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="da-rank">1.77</td> <!-- Danish rank -->
   <td class="no-rank">2.10</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.63</td> <!-- Swedish rank -->
   <td class="is-rank">2.63</td> <!-- Icelandic rank -->
   <td class="de-rank">1.73</td> <!-- German rank -->
   <td class="nl-rank">2.16</td> <!-- Dutch rank -->
   <td class="en-rank">1.68</td> <!-- English rank -->
   <td class="da ner">56.96 ± 2.39 / 45.84 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">55.11 ± 4.11 / 69.60 ± 2.69</td> <!-- Angry Tweets -->
   <td class="da la">42.64 ± 3.22 / 71.04 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da rc">54.58 ± 2.19 / 64.12 ± 1.41</td> <!-- ScandiQA-da -->
   <td class="no ner">66.75 ± 2.07 / 58.61 ± 3.33</td> <!-- NorNE-nb -->
   <td class="no ner">66.81 ± 2.57 / 57.71 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">60.58 ± 4.96 / 70.33 ± 4.12</td> <!-- NoReC -->
   <td class="no la">47.53 ± 4.07 / 72.24 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">17.14 ± 4.72 / 51.14 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no rc">41.92 ± 3.36 / 72.51 ± 1.91</td> <!-- NorQuAD -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="is ner">61.13 ± 3.80 / 50.79 ± 5.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.75 ± 5.66 / 46.83 ± 4.00</td> <!-- ScaLA-is -->
   <td class="is rc">27.27 ± 4.08 / 60.91 ± 1.98</td> <!-- NQiI -->
   <td class="de ner">65.19 ± 2.58 / 56.17 ± 3.57</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 2.15 / 71.98 ± 1.46</td> <!-- SB10k -->
   <td class="de la">41.86 ± 5.44 / 69.70 ± 2.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.51 ± 3.79 / 63.19 ± 2.48</td> <!-- GermanQuAD -->
   <td class="nl ner">67.00 ± 3.69 / 56.41 ± 4.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.33 ± 4.14 / 36.14 ± 2.91</td> <!-- Dutch Social -->
   <td class="nl la">55.48 ± 4.37 / 77.55 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.02 ± 1.67 / 76.87 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="en ner">71.83 ± 1.48 / 65.37 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.99 ± 3.04 / 69.81 ± 1.86</td> <!-- SST5 -->
   <td class="en la">39.97 ± 3.89 / 69.38 ± 1.87</td> <!-- ScaLA-en -->
   <td class="en rc">64.42 ± 3.17 / 80.97 ± 1.54</td> <!-- SQuAD -->
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
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="da-rank">1.64</td> <!-- Danish rank -->
   <td class="no-rank">2.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.59</td> <!-- Swedish rank -->
   <td class="is-rank">2.78</td> <!-- Icelandic rank -->
   <td class="de-rank">1.65</td> <!-- German rank -->
   <td class="nl-rank">2.44</td> <!-- Dutch rank -->
   <td class="en-rank">1.54</td> <!-- English rank -->
   <td class="da ner">58.06 ± 2.48 / 50.10 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">53.24 ± 4.04 / 67.81 ± 2.74</td> <!-- Angry Tweets -->
   <td class="da la">39.71 ± 4.96 / 65.90 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da rc">62.51 ± 1.48 / 67.47 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="no ner">62.46 ± 4.62 / 60.77 ± 4.36</td> <!-- NorNE-nb -->
   <td class="no ner">64.68 ± 3.04 / 61.69 ± 2.31</td> <!-- NorNE-nn -->
   <td class="no sent">59.68 ± 3.30 / 70.62 ± 3.08</td> <!-- NoReC -->
   <td class="no la">27.34 ± 12.20 / 50.42 ± 9.24</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 4.66 / 36.08 ± 3.27</td> <!-- ScaLA-nn -->
   <td class="no rc">57.44 ± 4.59 / 78.69 ± 3.09</td> <!-- NorQuAD -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv rc">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td class="is ner">63.25 ± 4.52 / 53.70 ± 3.09</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.12 ± 0.74</td> <!-- ScaLA-is -->
   <td class="is rc">32.65 ± 4.82 / 61.15 ± 3.96</td> <!-- NQiI -->
   <td class="de ner">63.71 ± 2.43 / 57.08 ± 2.70</td> <!-- GermEval -->
   <td class="de sent">58.17 ± 2.51 / 71.34 ± 1.62</td> <!-- SB10k -->
   <td class="de la">36.33 ± 5.00 / 64.51 ± 3.38</td> <!-- ScaLA-de -->
   <td class="de rc">36.06 ± 2.89 / 69.62 ± 2.81</td> <!-- GermanQuAD -->
   <td class="nl ner">66.50 ± 3.72 / 57.66 ± 3.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.82 ± 4.30 / 34.91 ± 2.53</td> <!-- Dutch Social -->
   <td class="nl la">49.55 ± 4.95 / 73.43 ± 3.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">65.26 ± 1.55 / 77.36 ± 1.41</td> <!-- SQuAD-nl -->
   <td class="en ner">72.38 ± 1.28 / 66.44 ± 1.74</td> <!-- CoNLL-en -->
   <td class="en sent">60.98 ± 2.19 / 68.64 ± 2.17</td> <!-- SST5 -->
   <td class="en la">43.12 ± 5.21 / 70.12 ± 2.87</td> <!-- ScaLA-en -->
   <td class="en rc">74.50 ± 3.41 / 86.22 ± 1.70</td> <!-- SQuAD -->
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
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="da-rank">1.76</td> <!-- Danish rank -->
   <td class="no-rank">1.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.96</td> <!-- Swedish rank -->
   <td class="is-rank">2.63</td> <!-- Icelandic rank -->
   <td class="de-rank">1.78</td> <!-- German rank -->
   <td class="nl-rank">2.13</td> <!-- Dutch rank -->
   <td class="en-rank">1.68</td> <!-- English rank -->
   <td class="da ner">63.10 ± 2.12 / 55.10 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">53.09 ± 3.85 / 68.18 ± 2.27</td> <!-- Angry Tweets -->
   <td class="da la">40.98 ± 4.46 / 69.10 ± 2.72</td> <!-- ScaLA-da -->
   <td class="da rc">51.13 ± 1.89 / 63.12 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">80.50 ± 2.85 / 76.71 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">76.47 ± 3.13 / 73.94 ± 2.95</td> <!-- NorNE-nn -->
   <td class="no sent">59.29 ± 5.92 / 69.99 ± 4.80</td> <!-- NoReC -->
   <td class="no la">47.28 ± 3.57 / 69.23 ± 3.04</td> <!-- ScaLA-nb -->
   <td class="no la">32.76 ± 3.80 / 60.66 ± 3.10</td> <!-- ScaLA-nn -->
   <td class="no rc">39.71 ± 2.59 / 71.60 ± 1.57</td> <!-- NorQuAD -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="is ner">72.91 ± 3.48 / 68.22 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.01 ± 4.64 / 50.69 ± 3.23</td> <!-- ScaLA-is -->
   <td class="is rc">31.86 ± 1.86 / 60.66 ± 1.58</td> <!-- NQiI -->
   <td class="de ner">75.20 ± 2.15 / 64.06 ± 3.60</td> <!-- GermEval -->
   <td class="de sent">54.38 ± 3.31 / 68.02 ± 2.21</td> <!-- SB10k -->
   <td class="de la">36.59 ± 4.24 / 67.36 ± 1.77</td> <!-- ScaLA-de -->
   <td class="de rc">26.90 ± 2.67 / 58.28 ± 2.22</td> <!-- GermanQuAD -->
   <td class="nl ner">74.64 ± 3.67 / 71.84 ± 4.01</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.90 ± 2.04 / 41.93 ± 1.60</td> <!-- Dutch Social -->
   <td class="nl la">49.54 ± 4.22 / 74.03 ± 2.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">44.77 ± 1.67 / 71.44 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="en ner">81.30 ± 1.35 / 76.64 ± 1.77</td> <!-- CoNLL-en -->
   <td class="en sent">66.18 ± 2.04 / 72.85 ± 1.27</td> <!-- SST5 -->
   <td class="en la">38.10 ± 2.32 / 68.58 ± 1.40</td> <!-- ScaLA-en -->
   <td class="en rc">53.31 ± 3.61 / 77.76 ± 1.59</td> <!-- SQuAD -->
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
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">2.01</td> <!-- ScandEval rank -->
   <td class="da-rank">1.91</td> <!-- Danish rank -->
   <td class="no-rank">2.10</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.69</td> <!-- Swedish rank -->
   <td class="is-rank">3.05</td> <!-- Icelandic rank -->
   <td class="de-rank">1.74</td> <!-- German rank -->
   <td class="nl-rank">2.07</td> <!-- Dutch rank -->
   <td class="en-rank">1.54</td> <!-- English rank -->
   <td class="da ner">68.70 ± 2.40 / 64.05 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">49.88 ± 1.21 / 66.06 ± 1.12</td> <!-- Angry Tweets -->
   <td class="da la">44.20 ± 2.01 / 70.33 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">39.90 ± 1.37 / 45.91 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="no ner">88.26 ± 1.11 / 89.24 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">81.37 ± 1.67 / 83.89 ± 1.34</td> <!-- NorNE-nn -->
   <td class="no sent">54.61 ± 1.51 / 67.19 ± 1.65</td> <!-- NoReC -->
   <td class="no la">50.35 ± 1.78 / 73.06 ± 1.46</td> <!-- ScaLA-nb -->
   <td class="no la">22.15 ± 9.02 / 58.20 ± 5.38</td> <!-- ScaLA-nn -->
   <td class="no rc">31.77 ± 1.55 / 45.47 ± 2.02</td> <!-- NorQuAD -->
   <td class="sv ner">79.02 ± 0.74 / 77.59 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.89 / 69.85 ± 3.16</td> <!-- SweReC -->
   <td class="sv la">50.19 ± 1.23 / 74.23 ± 0.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.65 ± 1.29 / 46.62 ± 1.30</td> <!-- ScandiQA-sv -->
   <td class="is ner">75.46 ± 1.42 / 77.52 ± 0.88</td> <!-- MIM-GOLD-NER -->
   <td class="is la">15.21 ± 8.62 / 54.40 ± 5.57</td> <!-- ScaLA-is -->
   <td class="is rc">10.82 ± 0.92 / 43.65 ± 2.51</td> <!-- NQiI -->
   <td class="de ner">74.79 ± 1.45 / 75.10 ± 1.37</td> <!-- GermEval -->
   <td class="de sent">63.29 ± 1.54 / 75.42 ± 1.03</td> <!-- SB10k -->
   <td class="de la">45.32 ± 8.38 / 71.30 ± 4.11</td> <!-- ScaLA-de -->
   <td class="de rc">16.42 ± 0.54 / 34.46 ± 1.03</td> <!-- GermanQuAD -->
   <td class="nl ner">79.12 ± 1.90 / 83.05 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">27.67 ± 2.85 / 44.90 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">39.28 ± 12.28 / 67.90 ± 5.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">35.71 ± 1.70 / 46.63 ± 1.40</td> <!-- SQuAD-nl -->
   <td class="en ner">89.65 ± 0.52 / 89.71 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">61.46 ± 0.89 / 60.48 ± 2.52</td> <!-- SST5 -->
   <td class="en la">51.32 ± 1.98 / 74.21 ± 1.18</td> <!-- ScaLA-en -->
   <td class="en rc">50.78 ± 1.14 / 63.05 ± 0.89</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="da-rank">2.08</td> <!-- Danish rank -->
   <td class="no-rank">2.32</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.90</td> <!-- Swedish rank -->
   <td class="is-rank">2.54</td> <!-- Icelandic rank -->
   <td class="de-rank">1.56</td> <!-- German rank -->
   <td class="nl-rank">2.40</td> <!-- Dutch rank -->
   <td class="en-rank">1.49</td> <!-- English rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da rc">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">68.11 ± 1.83 / 57.57 ± 3.10</td> <!-- NorNE-nb -->
   <td class="no ner">68.19 ± 1.01 / 56.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">55.33 ± 1.95 / 69.71 ± 1.56</td> <!-- NoReC -->
   <td class="no la">10.15 ± 3.24 / 36.27 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">7.51 ± 2.97 / 35.89 ± 1.30</td> <!-- ScaLA-nn -->
   <td class="no rc">55.33 ± 3.29 / 80.42 ± 1.68</td> <!-- NorQuAD -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="is ner">62.08 ± 2.27 / 51.09 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.58 ± 1.03 / 44.38 ± 3.90</td> <!-- ScaLA-is -->
   <td class="is rc">29.66 ± 3.02 / 56.60 ± 2.22</td> <!-- NQiI -->
   <td class="de ner">68.11 ± 1.32 / 56.25 ± 1.65</td> <!-- GermEval -->
   <td class="de sent">59.79 ± 1.60 / 71.47 ± 1.54</td> <!-- SB10k -->
   <td class="de la">35.45 ± 3.06 / 66.13 ± 1.28</td> <!-- ScaLA-de -->
   <td class="de rc">37.27 ± 1.23 / 68.54 ± 1.94</td> <!-- GermanQuAD -->
   <td class="nl ner">65.37 ± 1.61 / 46.10 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.93 ± 1.80 / 34.67 ± 2.84</td> <!-- Dutch Social -->
   <td class="nl la">41.67 ± 1.53 / 69.81 ± 1.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">67.75 ± 0.62 / 78.01 ± 0.45</td> <!-- SQuAD-nl -->
   <td class="en ner">69.50 ± 1.14 / 63.41 ± 0.77</td> <!-- CoNLL-en -->
   <td class="en sent">70.01 ± 0.93 / 59.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">41.35 ± 2.01 / 70.11 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">76.79 ± 0.43 / 89.35 ± 0.19</td> <!-- SQuAD -->
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
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="da-rank">1.33</td> <!-- Danish rank -->
   <td class="no-rank">1.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.25</td> <!-- Swedish rank -->
   <td class="is-rank">3.05</td> <!-- Icelandic rank -->
   <td class="de-rank">2.71</td> <!-- German rank -->
   <td class="nl-rank">3.38</td> <!-- Dutch rank -->
   <td class="en-rank">1.46</td> <!-- English rank -->
   <td class="da ner">75.22 ± 1.64 / 71.57 ± 1.50</td> <!-- DANSK -->
   <td class="da sent">49.94 ± 3.25 / 65.66 ± 2.73</td> <!-- Angry Tweets -->
   <td class="da la">72.59 ± 1.38 / 85.58 ± 0.97</td> <!-- ScaLA-da -->
   <td class="da rc">48.97 ± 1.22 / 54.79 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">92.49 ± 0.81 / 92.58 ± 0.61</td> <!-- NorNE-nb -->
   <td class="no ner">87.22 ± 1.19 / 88.71 ± 1.02</td> <!-- NorNE-nn -->
   <td class="no sent">58.77 ± 3.69 / 69.56 ± 4.55</td> <!-- NoReC -->
   <td class="no la">76.30 ± 2.09 / 87.19 ± 1.40</td> <!-- ScaLA-nb -->
   <td class="no la">64.11 ± 5.18 / 80.68 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no rc">60.69 ± 1.15 / 75.73 ± 1.06</td> <!-- NorQuAD -->
   <td class="sv ner">82.97 ± 0.98 / 81.14 ± 1.14</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 1.25 / 73.57 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">73.81 ± 4.60 / 86.33 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.50 ± 1.32 / 55.34 ± 1.33</td> <!-- ScandiQA-sv -->
   <td class="is ner">73.92 ± 1.40 / 75.86 ± 1.21</td> <!-- MIM-GOLD-NER -->
   <td class="is la">11.77 ± 5.19 / 43.60 ± 7.11</td> <!-- ScaLA-is -->
   <td class="is rc">11.84 ± 1.07 / 48.30 ± 1.02</td> <!-- NQiI -->
   <td class="de ner">67.24 ± 1.51 / 66.01 ± 1.32</td> <!-- GermEval -->
   <td class="de sent">45.84 ± 2.11 / 63.35 ± 1.48</td> <!-- SB10k -->
   <td class="de la">2.28 ± 1.62 / 35.18 ± 2.11</td> <!-- ScaLA-de -->
   <td class="de rc">18.17 ± 1.85 / 33.37 ± 2.80</td> <!-- GermanQuAD -->
   <td class="nl ner">73.03 ± 2.07 / 79.97 ± 1.63</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.65 ± 4.19 / 26.89 ± 2.64</td> <!-- Dutch Social -->
   <td class="nl la">2.00 ± 2.03 / 39.53 ± 4.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">42.85 ± 0.98 / 53.68 ± 0.89</td> <!-- SQuAD-nl -->
   <td class="en ner">89.48 ± 0.86 / 89.32 ± 0.69</td> <!-- CoNLL-en -->
   <td class="en sent">51.88 ± 6.25 / 56.03 ± 4.61</td> <!-- SST5 -->
   <td class="en la">50.69 ± 4.90 / 73.54 ± 2.97</td> <!-- ScaLA-en -->
   <td class="en rc">69.46 ± 1.02 / 80.82 ± 0.75</td> <!-- SQuAD -->
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
   <td>10.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.1</td> <!-- ScaLA-is version -->
   <td>10.0.1</td> <!-- NQiI version -->
   <td>10.0.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>10.0.1</td> <!-- ScaLA-de version -->
   <td>10.0.1</td> <!-- GermanQuAD version -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>10.0.1</td> <!-- SQuAD-nl version -->
   <td>10.0.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>10.0.1</td> <!-- ScaLA-en version -->
   <td>10.0.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="da-rank">1.33</td> <!-- Danish rank -->
   <td class="no-rank">1.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.25</td> <!-- Swedish rank -->
   <td class="is-rank">3.37</td> <!-- Icelandic rank -->
   <td class="de-rank">2.64</td> <!-- German rank -->
   <td class="nl-rank">3.39</td> <!-- Dutch rank -->
   <td class="en-rank">1.38</td> <!-- English rank -->
   <td class="da ner">74.16 ± 1.73 / 70.93 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">51.20 ± 1.67 / 66.62 ± 1.58</td> <!-- Angry Tweets -->
   <td class="da la">73.87 ± 2.13 / 86.61 ± 1.17</td> <!-- ScaLA-da -->
   <td class="da rc">49.34 ± 1.14 / 55.06 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="no ner">92.01 ± 0.98 / 92.36 ± 0.70</td> <!-- NorNE-nb -->
   <td class="no ner">87.17 ± 1.24 / 88.75 ± 0.89</td> <!-- NorNE-nn -->
   <td class="no sent">60.11 ± 2.96 / 70.55 ± 3.99</td> <!-- NoReC -->
   <td class="no la">72.85 ± 5.60 / 85.73 ± 3.14</td> <!-- ScaLA-nb -->
   <td class="no la">65.56 ± 1.91 / 82.23 ± 0.97</td> <!-- ScaLA-nn -->
   <td class="no rc">60.38 ± 0.95 / 75.42 ± 1.16</td> <!-- NorQuAD -->
   <td class="sv ner">82.65 ± 1.04 / 80.43 ± 0.93</td> <!-- SUC3 -->
   <td class="sv sent">77.25 ± 1.20 / 73.96 ± 2.59</td> <!-- SweReC -->
   <td class="sv la">77.90 ± 1.45 / 88.63 ± 0.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.64 ± 1.11 / 55.64 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="is ner">74.30 ± 2.15 / 76.10 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.06 ± 2.43 / 37.04 ± 4.14</td> <!-- ScaLA-is -->
   <td class="is rc">11.47 ± 0.96 / 48.11 ± 0.94</td> <!-- NQiI -->
   <td class="de ner">68.93 ± 1.48 / 67.48 ± 1.55</td> <!-- GermEval -->
   <td class="de sent">46.81 ± 1.79 / 64.02 ± 1.31</td> <!-- SB10k -->
   <td class="de la">3.39 ± 3.01 / 39.29 ± 4.82</td> <!-- ScaLA-de -->
   <td class="de rc">18.62 ± 1.74 / 34.87 ± 2.36</td> <!-- GermanQuAD -->
   <td class="nl ner">70.92 ± 1.61 / 78.52 ± 1.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.50 ± 3.15 / 27.25 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">2.06 ± 1.79 / 41.06 ± 5.11</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.40 ± 1.92 / 51.93 ± 2.09</td> <!-- SQuAD-nl -->
   <td class="en ner">89.53 ± 0.40 / 89.37 ± 0.30</td> <!-- CoNLL-en -->
   <td class="en sent">53.90 ± 1.96 / 54.63 ± 2.32</td> <!-- SST5 -->
   <td class="en la">55.31 ± 2.36 / 76.38 ± 1.93</td> <!-- ScaLA-en -->
   <td class="en rc">69.89 ± 0.99 / 80.82 ± 0.97</td> <!-- SQuAD -->
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
   <td>10.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.1</td> <!-- ScaLA-is version -->
   <td>10.0.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>10.0.1</td> <!-- SQuAD-nl version -->
   <td>10.0.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>10.0.1</td> <!-- ScaLA-en version -->
   <td>10.0.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,019 ± 420 / 147 ± 51</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">2.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.82</td> <!-- Swedish rank -->
   <td class="is-rank">2.78</td> <!-- Icelandic rank -->
   <td class="de-rank">2.11</td> <!-- German rank -->
   <td class="nl-rank">2.46</td> <!-- Dutch rank -->
   <td class="en-rank">1.71</td> <!-- English rank -->
   <td class="da ner">57.71 ± 1.13 / 31.64 ± 0.41</td> <!-- DANSK -->
   <td class="da sent">47.99 ± 0.74 / 62.91 ± 0.55</td> <!-- Angry Tweets -->
   <td class="da la">53.42 ± 0.87 / 73.99 ± 0.50</td> <!-- ScaLA-da -->
   <td class="da rc">50.06 ± 0.49 / 63.60 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="no ner">61.43 ± 0.97 / 38.97 ± 0.80</td> <!-- NorNE-nb -->
   <td class="no ner">60.13 ± 0.94 / 37.20 ± 0.62</td> <!-- NorNE-nn -->
   <td class="no sent">54.47 ± 0.71 / 70.13 ± 0.47</td> <!-- NoReC -->
   <td class="no la">45.47 ± 0.98 / 64.82 ± 0.74</td> <!-- ScaLA-nb -->
   <td class="no la">35.63 ± 1.13 / 60.68 ± 0.56</td> <!-- ScaLA-nn -->
   <td class="no rc">35.74 ± 0.61 / 68.93 ± 0.38</td> <!-- NorQuAD -->
   <td class="sv ner">50.60 ± 0.87 / 28.56 ± 0.80</td> <!-- SUC3 -->
   <td class="sv sent">77.80 ± 0.72 / 78.26 ± 0.53</td> <!-- SweReC -->
   <td class="sv la">54.85 ± 1.19 / 74.76 ± 0.71</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.31 ± 0.41 / 63.54 ± 0.36</td> <!-- ScandiQA-sv -->
   <td class="is ner">33.24 ± 0.58 / 15.02 ± 0.33</td> <!-- MIM-GOLD-NER -->
   <td class="is la">30.32 ± 1.39 / 58.98 ± 0.68</td> <!-- ScaLA-is -->
   <td class="is rc">22.71 ± 0.78 / 46.74 ± 0.59</td> <!-- NQiI -->
   <td class="de ner">61.02 ± 0.63 / 31.83 ± 0.75</td> <!-- GermEval -->
   <td class="de sent">50.67 ± 1.06 / 65.88 ± 0.99</td> <!-- SB10k -->
   <td class="de la">37.73 ± 0.85 / 68.10 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de rc">21.94 ± 0.57 / 51.62 ± 0.44</td> <!-- GermanQuAD -->
   <td class="nl ner">57.45 ± 0.91 / 30.74 ± 0.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.47 ± 1.54 / 32.77 ± 0.99</td> <!-- Dutch Social -->
   <td class="nl la">58.04 ± 1.44 / 78.05 ± 0.69</td> <!-- ScaLA-nl -->
   <td class="nl rc">43.95 ± 0.57 / 67.94 ± 0.36</td> <!-- SQuAD-nl -->
   <td class="en ner">74.51 ± 0.97 / 55.10 ± 0.90</td> <!-- CoNLL-en -->
   <td class="en sent">59.66 ± 0.63 / 68.45 ± 0.37</td> <!-- SST5 -->
   <td class="en la">45.60 ± 0.98 / 72.50 ± 0.50</td> <!-- ScaLA-en -->
   <td class="en rc">58.11 ± 0.50 / 81.14 ± 0.24</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da-rank">1.95</td> <!-- Danish rank -->
   <td class="no-rank">2.24</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.89</td> <!-- Swedish rank -->
   <td class="is-rank">3.23</td> <!-- Icelandic rank -->
   <td class="de-rank">1.82</td> <!-- German rank -->
   <td class="nl-rank">2.37</td> <!-- Dutch rank -->
   <td class="en-rank">1.45</td> <!-- English rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da rc">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">66.22 ± 2.15 / 48.98 ± 4.65</td> <!-- NorNE-nb -->
   <td class="no ner">64.14 ± 1.26 / 49.59 ± 4.31</td> <!-- NorNE-nn -->
   <td class="no sent">55.48 ± 1.77 / 69.68 ± 1.45</td> <!-- NoReC -->
   <td class="no la">26.13 ± 1.28 / 56.08 ± 2.05</td> <!-- ScaLA-nb -->
   <td class="no la">17.32 ± 0.77 / 54.57 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no rc">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">49.20 ± 2.64 / 40.79 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.45 ± 1.40 / 51.11 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">24.61 ± 3.36 / 54.99 ± 2.36</td> <!-- NQiI -->
   <td class="de ner">65.01 ± 0.68 / 43.34 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">51.80 ± 1.29 / 67.45 ± 0.87</td> <!-- SB10k -->
   <td class="de la">36.18 ± 1.31 / 67.86 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de rc">32.12 ± 2.08 / 67.30 ± 1.66</td> <!-- GermanQuAD -->
   <td class="nl ner">64.47 ± 2.31 / 40.89 ± 2.81</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.83 ± 1.91 / 41.53 ± 1.23</td> <!-- Dutch Social -->
   <td class="nl la">45.69 ± 1.76 / 72.13 ± 1.39</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.03 ± 1.37 / 73.17 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="en ner">71.81 ± 1.02 / 59.93 ± 2.52</td> <!-- CoNLL-en -->
   <td class="en sent">69.98 ± 1.00 / 69.79 ± 0.76</td> <!-- SST5 -->
   <td class="en la">45.34 ± 2.51 / 72.10 ± 1.10</td> <!-- ScaLA-en -->
   <td class="en rc">72.49 ± 1.57 / 87.51 ± 0.74</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.14</td> <!-- Danish rank -->
   <td class="no-rank">2.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.95</td> <!-- Swedish rank -->
   <td class="is-rank">2.31</td> <!-- Icelandic rank -->
   <td class="de-rank">1.84</td> <!-- German rank -->
   <td class="nl-rank">2.88</td> <!-- Dutch rank -->
   <td class="en-rank">1.55</td> <!-- English rank -->
   <td class="da ner">63.59 ± 2.16 / 42.42 ± 3.34</td> <!-- DANSK -->
   <td class="da sent">29.47 ± 4.78 / 50.59 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">38.37 ± 9.13 / 60.56 ± 8.53</td> <!-- ScaLA-da -->
   <td class="da rc">54.63 ± 0.51 / 65.79 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="no ner">75.05 ± 1.56 / 57.52 ± 4.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.08 ± 1.43 / 62.50 ± 4.89</td> <!-- NorNE-nn -->
   <td class="no sent">37.79 ± 4.47 / 55.88 ± 3.23</td> <!-- NoReC -->
   <td class="no la">31.59 ± 11.25 / 54.68 ± 10.28</td> <!-- ScaLA-nb -->
   <td class="no la">39.25 ± 7.82 / 62.90 ± 7.12</td> <!-- ScaLA-nn -->
   <td class="no rc">39.43 ± 2.31 / 72.15 ± 1.71</td> <!-- NorQuAD -->
   <td class="sv ner">67.38 ± 1.52 / 52.86 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 4.81 / 67.01 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">29.41 ± 10.34 / 52.38 ± 8.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.67 ± 0.89 / 66.26 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">67.56 ± 1.93 / 43.20 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">23.28 ± 7.61 / 52.43 ± 7.20</td> <!-- ScaLA-is -->
   <td class="is rc">24.91 ± 1.14 / 52.48 ± 0.90</td> <!-- NQiI -->
   <td class="de ner">67.90 ± 1.07 / 45.53 ± 3.11</td> <!-- GermEval -->
   <td class="de sent">51.88 ± 5.19 / 67.24 ± 3.71</td> <!-- SB10k -->
   <td class="de la">46.77 ± 2.33 / 69.48 ± 2.55</td> <!-- ScaLA-de -->
   <td class="de rc">24.70 ± 1.31 / 56.87 ± 0.77</td> <!-- GermanQuAD -->
   <td class="nl ner">68.20 ± 1.93 / 49.92 ± 2.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.65 ± 1.80 / 14.84 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">31.15 ± 7.70 / 52.16 ± 7.03</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.17 ± 1.82 / 72.08 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="en ner">78.84 ± 1.47 / 68.25 ± 3.41</td> <!-- CoNLL-en -->
   <td class="en sent">60.72 ± 1.81 / 67.08 ± 1.16</td> <!-- SST5 -->
   <td class="en la">50.99 ± 1.31 / 72.72 ± 1.34</td> <!-- ScaLA-en -->
   <td class="en rc">61.45 ± 1.95 / 83.59 ± 0.82</td> <!-- SQuAD -->
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
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.11.0</td> <!-- SST5 version -->
   <td>12.11.0</td> <!-- ScaLA-en version -->
   <td>12.11.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="da-rank">2.10</td> <!-- Danish rank -->
   <td class="no-rank">2.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.79</td> <!-- Swedish rank -->
   <td class="is-rank">2.94</td> <!-- Icelandic rank -->
   <td class="de-rank">1.79</td> <!-- German rank -->
   <td class="nl-rank">2.53</td> <!-- Dutch rank -->
   <td class="en-rank">1.73</td> <!-- English rank -->
   <td class="da ner">47.68 ± 2.50 / 32.67 ± 2.45</td> <!-- DANSK -->
   <td class="da sent">49.71 ± 1.43 / 64.00 ± 1.96</td> <!-- Angry Tweets -->
   <td class="da la">25.48 ± 2.83 / 58.45 ± 2.63</td> <!-- ScaLA-da -->
   <td class="da rc">60.31 ± 1.24 / 65.79 ± 0.84</td> <!-- ScandiQA-da -->
   <td class="no ner">64.62 ± 1.26 / 53.50 ± 3.27</td> <!-- NorNE-nb -->
   <td class="no ner">65.10 ± 1.86 / 56.43 ± 2.58</td> <!-- NorNE-nn -->
   <td class="no sent">52.87 ± 1.18 / 68.71 ± 1.01</td> <!-- NoReC -->
   <td class="no la">28.34 ± 3.26 / 58.57 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">22.40 ± 3.12 / 53.51 ± 5.42</td> <!-- ScaLA-nn -->
   <td class="no rc">53.20 ± 3.15 / 75.98 ± 2.62</td> <!-- NorQuAD -->
   <td class="sv ner">63.85 ± 2.49 / 44.62 ± 4.10</td> <!-- SUC3 -->
   <td class="sv sent">79.96 ± 0.93 / 75.75 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">31.70 ± 4.07 / 59.28 ± 5.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.33 ± 0.88 / 65.24 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="is ner">52.57 ± 2.04 / 36.81 ± 2.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.87 ± 2.28 / 40.95 ± 4.97</td> <!-- ScaLA-is -->
   <td class="is rc">30.12 ± 4.65 / 57.81 ± 4.78</td> <!-- NQiI -->
   <td class="de ner">60.46 ± 1.26 / 47.72 ± 1.69</td> <!-- GermEval -->
   <td class="de sent">58.57 ± 2.53 / 71.30 ± 1.70</td> <!-- SB10k -->
   <td class="de la">26.25 ± 5.90 / 61.41 ± 3.94</td> <!-- ScaLA-de -->
   <td class="de rc">34.85 ± 3.43 / 64.05 ± 3.68</td> <!-- GermanQuAD -->
   <td class="nl ner">64.79 ± 1.96 / 45.48 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.83 / 37.12 ± 2.19</td> <!-- Dutch Social -->
   <td class="nl la">32.97 ± 2.68 / 58.52 ± 2.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.89 ± 1.06 / 74.73 ± 1.02</td> <!-- SQuAD-nl -->
   <td class="en ner">69.86 ± 2.10 / 62.68 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">66.76 ± 0.72 / 68.58 ± 0.72</td> <!-- SST5 -->
   <td class="en la">30.96 ± 2.46 / 61.29 ± 3.61</td> <!-- ScaLA-en -->
   <td class="en rc">71.39 ± 2.20 / 84.24 ± 1.55</td> <!-- SQuAD -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- NorNE-nb version -->
   <td>12.11.0</td> <!-- NorNE-nn version -->
   <td>12.11.0</td> <!-- NoReC version -->
   <td>12.11.0</td> <!-- ScaLA-nb version -->
   <td>12.11.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.11.0</td> <!-- SST5 version -->
   <td>12.11.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da-rank">2.06</td> <!-- Danish rank -->
   <td class="no-rank">2.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.83</td> <!-- Swedish rank -->
   <td class="is-rank">2.82</td> <!-- Icelandic rank -->
   <td class="de-rank">1.95</td> <!-- German rank -->
   <td class="nl-rank">2.59</td> <!-- Dutch rank -->
   <td class="en-rank">1.80</td> <!-- English rank -->
   <td class="da ner">46.31 ± 3.22 / 29.09 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 1.47 / 66.35 ± 1.70</td> <!-- Angry Tweets -->
   <td class="da la">25.70 ± 4.59 / 55.65 ± 5.87</td> <!-- ScaLA-da -->
   <td class="da rc">59.79 ± 1.21 / 65.44 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="no ner">61.48 ± 1.83 / 47.65 ± 2.94</td> <!-- NorNE-nb -->
   <td class="no ner">61.58 ± 2.21 / 50.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">49.87 ± 1.88 / 66.15 ± 1.44</td> <!-- NoReC -->
   <td class="no la">21.20 ± 6.57 / 52.29 ± 7.43</td> <!-- ScaLA-nb -->
   <td class="no la">19.65 ± 4.32 / 56.66 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no rc">53.35 ± 4.33 / 74.98 ± 3.70</td> <!-- NorQuAD -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="is ner">48.70 ± 3.02 / 34.52 ± 2.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.49 ± 2.51 / 43.40 ± 4.41</td> <!-- ScaLA-is -->
   <td class="is rc">29.56 ± 5.47 / 55.53 ± 5.79</td> <!-- NQiI -->
   <td class="de ner">56.00 ± 1.94 / 43.49 ± 2.05</td> <!-- GermEval -->
   <td class="de sent">56.40 ± 3.89 / 70.17 ± 2.91</td> <!-- SB10k -->
   <td class="de la">22.01 ± 5.17 / 56.97 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de rc">35.39 ± 2.49 / 64.61 ± 2.42</td> <!-- GermanQuAD -->
   <td class="nl ner">62.26 ± 2.20 / 42.41 ± 2.02</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.45 ± 2.69 / 33.45 ± 1.99</td> <!-- Dutch Social -->
   <td class="nl la">30.30 ± 3.94 / 62.28 ± 2.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.99 ± 1.00 / 73.73 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="en ner">66.31 ± 2.09 / 58.68 ± 1.95</td> <!-- CoNLL-en -->
   <td class="en sent">64.30 ± 0.65 / 69.26 ± 0.50</td> <!-- SST5 -->
   <td class="en la">28.18 ± 3.96 / 58.97 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en rc">70.38 ± 3.51 / 82.95 ± 2.38</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.22</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
   <td class="is-rank">2.79</td> <!-- Icelandic rank -->
   <td class="de-rank">1.87</td> <!-- German rank -->
   <td class="nl-rank">2.59</td> <!-- Dutch rank -->
   <td class="en-rank">1.79</td> <!-- English rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da rc">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">74.47 ± 1.47 / 65.57 ± 2.39</td> <!-- NorNE-nb -->
   <td class="no ner">72.93 ± 1.00 / 65.44 ± 2.55</td> <!-- NorNE-nn -->
   <td class="no sent">50.62 ± 3.52 / 65.69 ± 3.50</td> <!-- NoReC -->
   <td class="no la">27.77 ± 1.63 / 61.75 ± 1.77</td> <!-- ScaLA-nb -->
   <td class="no la">20.35 ± 1.92 / 57.74 ± 2.28</td> <!-- ScaLA-nn -->
   <td class="no rc">42.90 ± 3.57 / 69.90 ± 3.17</td> <!-- NorQuAD -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="is ner">61.69 ± 2.17 / 41.25 ± 3.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.10 ± 1.61 / 48.74 ± 3.05</td> <!-- ScaLA-is -->
   <td class="is rc">31.52 ± 2.08 / 58.96 ± 1.57</td> <!-- NQiI -->
   <td class="de ner">68.18 ± 0.95 / 57.72 ± 1.15</td> <!-- GermEval -->
   <td class="de sent">58.33 ± 2.83 / 69.31 ± 3.16</td> <!-- SB10k -->
   <td class="de la">29.12 ± 3.17 / 63.60 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 1.99 / 56.42 ± 3.34</td> <!-- GermanQuAD -->
   <td class="nl ner">68.72 ± 1.81 / 54.89 ± 2.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.67 ± 2.51 / 41.36 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">32.91 ± 2.56 / 64.93 ± 1.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.36 ± 1.31 / 67.50 ± 0.69</td> <!-- SQuAD-nl -->
   <td class="en ner">75.02 ± 1.31 / 69.47 ± 1.18</td> <!-- CoNLL-en -->
   <td class="en sent">67.64 ± 1.12 / 71.04 ± 1.17</td> <!-- SST5 -->
   <td class="en la">32.29 ± 3.05 / 64.85 ± 2.07</td> <!-- ScaLA-en -->
   <td class="en rc">54.84 ± 2.22 / 79.10 ± 1.10</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da-rank">2.26</td> <!-- Danish rank -->
   <td class="no-rank">2.31</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.97</td> <!-- Swedish rank -->
   <td class="is-rank">2.72</td> <!-- Icelandic rank -->
   <td class="de-rank">1.87</td> <!-- German rank -->
   <td class="nl-rank">2.60</td> <!-- Dutch rank -->
   <td class="en-rank">1.82</td> <!-- English rank -->
   <td class="da ner">57.19 ± 1.73 / 44.34 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">51.30 ± 1.32 / 64.44 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">10.31 ± 3.91 / 42.59 ± 5.19</td> <!-- ScaLA-da -->
   <td class="da rc">48.80 ± 1.66 / 60.46 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="no ner">74.77 ± 0.84 / 71.87 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">72.80 ± 1.57 / 69.98 ± 1.84</td> <!-- NorNE-nn -->
   <td class="no sent">57.30 ± 0.98 / 71.58 ± 0.90</td> <!-- NoReC -->
   <td class="no la">5.23 ± 1.83 / 34.90 ± 0.81</td> <!-- ScaLA-nb -->
   <td class="no la">11.51 ± 3.24 / 45.73 ± 5.97</td> <!-- ScaLA-nn -->
   <td class="no rc">43.93 ± 3.73 / 70.96 ± 3.00</td> <!-- NorQuAD -->
   <td class="sv ner">71.52 ± 1.43 / 59.28 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">80.46 ± 0.83 / 78.67 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">12.29 ± 3.59 / 40.53 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.54 ± 1.52 / 62.08 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="is ner">55.09 ± 1.76 / 40.34 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">8.45 ± 1.33 / 51.00 ± 1.95</td> <!-- ScaLA-is -->
   <td class="is rc">29.65 ± 1.09 / 56.96 ± 1.35</td> <!-- NQiI -->
   <td class="de ner">67.61 ± 1.23 / 60.39 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">59.96 ± 2.00 / 70.71 ± 1.80</td> <!-- SB10k -->
   <td class="de la">28.25 ± 3.57 / 59.54 ± 3.88</td> <!-- ScaLA-de -->
   <td class="de rc">28.79 ± 2.02 / 55.82 ± 3.28</td> <!-- GermanQuAD -->
   <td class="nl ner">69.76 ± 1.36 / 57.66 ± 1.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.51 ± 1.59 / 39.71 ± 1.21</td> <!-- Dutch Social -->
   <td class="nl la">37.58 ± 3.42 / 66.98 ± 2.22</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.26 ± 2.09 / 65.63 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="en ner">76.95 ± 0.95 / 72.47 ± 0.82</td> <!-- CoNLL-en -->
   <td class="en sent">68.12 ± 0.92 / 72.48 ± 0.53</td> <!-- SST5 -->
   <td class="en la">34.34 ± 3.37 / 65.84 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en rc">47.88 ± 3.37 / 76.21 ± 1.69</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="da-rank">2.11</td> <!-- Danish rank -->
   <td class="no-rank">2.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.90</td> <!-- Swedish rank -->
   <td class="is-rank">2.79</td> <!-- Icelandic rank -->
   <td class="de-rank">2.20</td> <!-- German rank -->
   <td class="nl-rank">2.40</td> <!-- Dutch rank -->
   <td class="en-rank">2.21</td> <!-- English rank -->
   <td class="da ner">70.10 ± 1.16 / 64.54 ± 1.00</td> <!-- DANSK -->
   <td class="da sent">45.30 ± 2.03 / 63.22 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">51.74 ± 2.53 / 74.31 ± 1.94</td> <!-- ScaLA-da -->
   <td class="da rc">22.01 ± 2.50 / 27.76 ± 2.44</td> <!-- ScandiQA-da -->
   <td class="no ner">87.70 ± 0.66 / 85.32 ± 0.94</td> <!-- NorNE-nb -->
   <td class="no ner">81.41 ± 1.46 / 77.41 ± 1.57</td> <!-- NorNE-nn -->
   <td class="no sent">48.34 ± 2.10 / 60.68 ± 3.61</td> <!-- NoReC -->
   <td class="no la">55.30 ± 2.89 / 75.77 ± 1.87</td> <!-- ScaLA-nb -->
   <td class="no la">37.46 ± 2.69 / 67.68 ± 1.66</td> <!-- ScaLA-nn -->
   <td class="no rc">24.49 ± 6.03 / 35.93 ± 8.56</td> <!-- NorQuAD -->
   <td class="sv ner">72.49 ± 1.68 / 67.03 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">70.69 ± 1.08 / 67.03 ± 3.40</td> <!-- SweReC -->
   <td class="sv la">56.60 ± 3.25 / 76.70 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.89 ± 1.88 / 37.63 ± 1.86</td> <!-- ScandiQA-sv -->
   <td class="is ner">72.69 ± 0.79 / 73.57 ± 1.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">28.72 ± 5.29 / 60.29 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">8.46 ± 0.51 / 31.01 ± 0.72</td> <!-- NQiI -->
   <td class="de ner">74.89 ± 0.86 / 73.54 ± 0.84</td> <!-- GermEval -->
   <td class="de sent">63.01 ± 1.50 / 75.21 ± 1.03</td> <!-- SB10k -->
   <td class="de la">36.60 ± 2.17 / 64.93 ± 1.39</td> <!-- ScaLA-de -->
   <td class="de rc">0.65 ± 0.25 / 5.05 ± 1.30</td> <!-- GermanQuAD -->
   <td class="nl ner">77.15 ± 1.38 / 81.92 ± 1.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.78 ± 6.76 / 37.09 ± 4.14</td> <!-- Dutch Social -->
   <td class="nl la">56.72 ± 3.83 / 77.53 ± 2.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">14.61 ± 4.26 / 20.91 ± 5.21</td> <!-- SQuAD-nl -->
   <td class="en ner">87.09 ± 0.61 / 87.25 ± 0.49</td> <!-- CoNLL-en -->
   <td class="en sent">55.40 ± 0.56 / 52.86 ± 0.29</td> <!-- SST5 -->
   <td class="en la">39.78 ± 3.59 / 67.21 ± 2.02</td> <!-- ScaLA-en -->
   <td class="en rc">6.20 ± 4.26 / 13.47 ± 5.29</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.30</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
   <td class="is-rank">3.48</td> <!-- Icelandic rank -->
   <td class="de-rank">2.02</td> <!-- German rank -->
   <td class="nl-rank">1.92</td> <!-- Dutch rank -->
   <td class="en-rank">1.97</td> <!-- English rank -->
   <td class="da ner">65.10 ± 1.65 / 61.96 ± 1.26</td> <!-- DANSK -->
   <td class="da sent">45.07 ± 1.23 / 63.33 ± 0.78</td> <!-- Angry Tweets -->
   <td class="da la">26.83 ± 11.38 / 60.41 ± 6.66</td> <!-- ScaLA-da -->
   <td class="da rc">29.92 ± 1.25 / 35.05 ± 1.16</td> <!-- ScandiQA-da -->
   <td class="no ner">86.56 ± 1.18 / 87.30 ± 0.95</td> <!-- NorNE-nb -->
   <td class="no ner">80.57 ± 1.55 / 83.03 ± 1.19</td> <!-- NorNE-nn -->
   <td class="no sent">49.62 ± 2.72 / 62.56 ± 3.88</td> <!-- NoReC -->
   <td class="no la">38.45 ± 15.28 / 67.14 ± 7.71</td> <!-- ScaLA-nb -->
   <td class="no la">11.38 ± 7.59 / 51.68 ± 4.73</td> <!-- ScaLA-nn -->
   <td class="no rc">31.50 ± 2.41 / 47.61 ± 2.55</td> <!-- NorQuAD -->
   <td class="sv ner">75.49 ± 1.09 / 74.57 ± 0.60</td> <!-- SUC3 -->
   <td class="sv sent">71.12 ± 0.90 / 60.88 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">36.69 ± 15.58 / 65.77 ± 8.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.55 ± 2.07 / 38.90 ± 2.21</td> <!-- ScandiQA-sv -->
   <td class="is ner">75.27 ± 1.18 / 76.85 ± 0.94</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.47 ± 1.14 / 47.14 ± 3.33</td> <!-- ScaLA-is -->
   <td class="is rc">7.67 ± 0.80 / 32.31 ± 0.81</td> <!-- NQiI -->
   <td class="de ner">74.50 ± 1.06 / 74.21 ± 0.83</td> <!-- GermEval -->
   <td class="de sent">58.23 ± 1.13 / 72.00 ± 0.75</td> <!-- SB10k -->
   <td class="de la">34.74 ± 14.22 / 64.18 ± 7.54</td> <!-- ScaLA-de -->
   <td class="de rc">11.19 ± 3.07 / 26.81 ± 6.54</td> <!-- GermanQuAD -->
   <td class="nl ner">78.45 ± 1.88 / 83.50 ± 0.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">22.67 ± 7.22 / 44.07 ± 6.51</td> <!-- Dutch Social -->
   <td class="nl la">54.92 ± 9.62 / 76.14 ± 5.00</td> <!-- ScaLA-nl -->
   <td class="nl rc">31.82 ± 2.84 / 40.85 ± 3.02</td> <!-- SQuAD-nl -->
   <td class="en ner">85.88 ± 0.99 / 86.21 ± 0.87</td> <!-- CoNLL-en -->
   <td class="en sent">51.46 ± 1.15 / 51.20 ± 0.50</td> <!-- SST5 -->
   <td class="en la">35.83 ± 11.08 / 65.86 ± 4.95</td> <!-- ScaLA-en -->
   <td class="en rc">43.26 ± 1.61 / 55.52 ± 1.60</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.06</td> <!-- Danish rank -->
   <td class="no-rank">2.47</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.17</td> <!-- Swedish rank -->
   <td class="is-rank">3.42</td> <!-- Icelandic rank -->
   <td class="de-rank">1.95</td> <!-- German rank -->
   <td class="nl-rank">2.54</td> <!-- Dutch rank -->
   <td class="en-rank">1.79</td> <!-- English rank -->
   <td class="da ner">52.22 ± 2.07 / 38.82 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">50.66 ± 1.88 / 62.04 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">23.57 ± 3.82 / 56.09 ± 4.62</td> <!-- ScaLA-da -->
   <td class="da rc">53.82 ± 2.13 / 61.94 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="no ner">60.21 ± 1.86 / 47.06 ± 3.08</td> <!-- NorNE-nb -->
   <td class="no ner">62.99 ± 2.66 / 48.82 ± 5.49</td> <!-- NorNE-nn -->
   <td class="no sent">55.12 ± 5.10 / 66.55 ± 5.07</td> <!-- NoReC -->
   <td class="no la">27.12 ± 4.90 / 54.26 ± 6.80</td> <!-- ScaLA-nb -->
   <td class="no la">6.82 ± 5.06 / 46.18 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no rc">38.50 ± 3.93 / 69.99 ± 2.23</td> <!-- NorQuAD -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="is ner">46.32 ± 5.10 / 35.77 ± 3.59</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-3.31 ± 3.91 / 38.63 ± 2.52</td> <!-- ScaLA-is -->
   <td class="is rc">24.26 ± 4.64 / 55.26 ± 2.41</td> <!-- NQiI -->
   <td class="de ner">62.39 ± 2.72 / 50.86 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">53.16 ± 3.17 / 64.24 ± 3.42</td> <!-- SB10k -->
   <td class="de la">31.81 ± 5.15 / 62.15 ± 4.02</td> <!-- ScaLA-de -->
   <td class="de rc">28.99 ± 2.22 / 60.53 ± 2.92</td> <!-- GermanQuAD -->
   <td class="nl ner">64.00 ± 3.52 / 48.94 ± 3.83</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.30 ± 3.75 / 30.50 ± 2.48</td> <!-- Dutch Social -->
   <td class="nl la">30.88 ± 4.62 / 59.62 ± 4.50</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.14 ± 1.55 / 70.96 ± 1.01</td> <!-- SQuAD-nl -->
   <td class="en ner">72.80 ± 1.65 / 64.88 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.76 ± 2.53 / 71.14 ± 1.90</td> <!-- SST5 -->
   <td class="en la">28.37 ± 4.76 / 62.85 ± 3.04</td> <!-- ScaLA-en -->
   <td class="en rc">64.70 ± 2.69 / 81.80 ± 1.41</td> <!-- SQuAD -->
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
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da-rank">2.14</td> <!-- Danish rank -->
   <td class="no-rank">2.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.12</td> <!-- Swedish rank -->
   <td class="is-rank">3.29</td> <!-- Icelandic rank -->
   <td class="de-rank">1.99</td> <!-- German rank -->
   <td class="nl-rank">2.75</td> <!-- Dutch rank -->
   <td class="en-rank">1.92</td> <!-- English rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da rc">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no rc">34.48 ± 2.13 / 65.43 ± 2.07</td> <!-- NorQuAD -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is rc">22.48 ± 4.43 / 55.51 ± 2.89</td> <!-- NQiI -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de rc">25.22 ± 3.84 / 60.93 ± 2.99</td> <!-- GermanQuAD -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.94 ± 1.12 / 70.12 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en rc">52.69 ± 2.21 / 76.37 ± 1.27</td> <!-- SQuAD -->
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
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.29</td> <!-- Swedish rank -->
   <td class="is-rank">3.19</td> <!-- Icelandic rank -->
   <td class="de-rank">2.07</td> <!-- German rank -->
   <td class="nl-rank">2.66</td> <!-- Dutch rank -->
   <td class="en-rank">1.92</td> <!-- English rank -->
   <td class="da ner">52.61 ± 1.77 / 33.64 ± 2.67</td> <!-- DANSK -->
   <td class="da sent">49.81 ± 1.43 / 66.32 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">19.64 ± 1.63 / 54.22 ± 2.32</td> <!-- ScaLA-da -->
   <td class="da rc">48.03 ± 1.24 / 57.94 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">64.37 ± 2.17 / 52.81 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">62.77 ± 0.83 / 51.80 ± 2.77</td> <!-- NorNE-nn -->
   <td class="no sent">50.60 ± 4.90 / 66.76 ± 3.04</td> <!-- NoReC -->
   <td class="no la">18.09 ± 2.04 / 52.56 ± 2.60</td> <!-- ScaLA-nb -->
   <td class="no la">12.25 ± 2.18 / 50.79 ± 2.42</td> <!-- ScaLA-nn -->
   <td class="no rc">38.34 ± 2.39 / 69.54 ± 1.96</td> <!-- NorQuAD -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">56.71 ± 1.98 / 46.71 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="de ner">64.38 ± 1.60 / 50.26 ± 2.53</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.45 / 69.32 ± 1.02</td> <!-- SB10k -->
   <td class="de la">26.03 ± 2.23 / 61.88 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">25.68 ± 2.81 / 62.48 ± 2.93</td> <!-- GermanQuAD -->
   <td class="nl ner">64.25 ± 2.23 / 46.52 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.66 ± 1.99 / 39.45 ± 1.52</td> <!-- Dutch Social -->
   <td class="nl la">28.59 ± 1.48 / 61.24 ± 1.46</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.64 ± 0.86 / 68.04 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="en ner">70.62 ± 0.90 / 58.92 ± 2.15</td> <!-- CoNLL-en -->
   <td class="en sent">67.78 ± 1.03 / 72.29 ± 0.47</td> <!-- SST5 -->
   <td class="en la">30.99 ± 2.94 / 62.20 ± 2.56</td> <!-- ScaLA-en -->
   <td class="en rc">49.56 ± 2.85 / 76.72 ± 1.15</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.13</td> <!-- Swedish rank -->
   <td class="is-rank">3.18</td> <!-- Icelandic rank -->
   <td class="de-rank">2.11</td> <!-- German rank -->
   <td class="nl-rank">2.87</td> <!-- Dutch rank -->
   <td class="en-rank">1.75</td> <!-- English rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da rc">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no rc">46.86 ± 3.27 / 70.86 ± 2.79</td> <!-- NorQuAD -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.70 ± 5.36 / 49.31 ± 5.21</td> <!-- NQiI -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de rc">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en rc">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
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
   <td>9.1.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.1.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>9.1.2</td> <!-- GermEval version -->
   <td>9.1.2</td> <!-- SB10k version -->
   <td>9.1.2</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>9.1.2</td> <!-- CoNLL-nl version -->
   <td>9.1.2</td> <!-- Dutch Social version -->
   <td>9.1.2</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.1.2</td> <!-- CoNLL-en version -->
   <td>9.1.2</td> <!-- SST5 version -->
   <td>9.1.2</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="da-rank">2.41</td> <!-- Danish rank -->
   <td class="no-rank">2.70</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.00</td> <!-- Swedish rank -->
   <td class="is-rank">3.20</td> <!-- Icelandic rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.98</td> <!-- Dutch rank -->
   <td class="en-rank">1.93</td> <!-- English rank -->
   <td class="da ner">19.59 ± 2.54 / 15.47 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">46.55 ± 1.89 / 59.52 ± 3.56</td> <!-- Angry Tweets -->
   <td class="da la">32.64 ± 2.91 / 63.84 ± 1.69</td> <!-- ScaLA-da -->
   <td class="da rc">59.40 ± 1.02 / 64.81 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">26.43 ± 3.36 / 26.32 ± 2.35</td> <!-- NorNE-nb -->
   <td class="no ner">32.66 ± 3.42 / 29.43 ± 1.74</td> <!-- NorNE-nn -->
   <td class="no sent">41.82 ± 3.69 / 53.06 ± 5.15</td> <!-- NoReC -->
   <td class="no la">25.82 ± 4.43 / 59.85 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">20.16 ± 3.43 / 53.83 ± 5.61</td> <!-- ScaLA-nn -->
   <td class="no rc">52.68 ± 3.58 / 75.16 ± 2.44</td> <!-- NorQuAD -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td class="is ner">30.61 ± 4.61 / 25.80 ± 3.57</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.60 ± 1.68 / 38.26 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">32.22 ± 3.19 / 55.22 ± 2.59</td> <!-- NQiI -->
   <td class="de ner">39.88 ± 2.56 / 35.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">56.23 ± 3.17 / 68.87 ± 2.73</td> <!-- SB10k -->
   <td class="de la">32.71 ± 1.60 / 64.55 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">36.58 ± 2.81 / 64.92 ± 2.97</td> <!-- GermanQuAD -->
   <td class="nl ner">47.75 ± 2.33 / 35.64 ± 1.89</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.68 ± 0.61 / 26.25 ± 1.18</td> <!-- Dutch Social -->
   <td class="nl la">28.28 ± 2.48 / 62.81 ± 1.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.49 ± 1.15 / 73.19 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="en ner">47.20 ± 3.34 / 41.96 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.88 ± 2.24 / 66.49 ± 0.81</td> <!-- SST5 -->
   <td class="en la">35.75 ± 2.65 / 66.41 ± 2.26</td> <!-- ScaLA-en -->
   <td class="en rc">69.40 ± 4.29 / 82.46 ± 2.86</td> <!-- SQuAD -->
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
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.32</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
   <td class="is-rank">3.27</td> <!-- Icelandic rank -->
   <td class="de-rank">2.17</td> <!-- German rank -->
   <td class="nl-rank">2.93</td> <!-- Dutch rank -->
   <td class="en-rank">1.79</td> <!-- English rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da rc">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">50.63 ± 2.12 / 44.59 ± 1.80</td> <!-- NorNE-nb -->
   <td class="no ner">52.69 ± 2.30 / 46.51 ± 3.63</td> <!-- NorNE-nn -->
   <td class="no sent">44.05 ± 2.51 / 61.80 ± 2.28</td> <!-- NoReC -->
   <td class="no la">11.60 ± 4.10 / 43.01 ± 5.07</td> <!-- ScaLA-nb -->
   <td class="no la">9.26 ± 1.14 / 46.28 ± 3.60</td> <!-- ScaLA-nn -->
   <td class="no rc">45.23 ± 3.73 / 68.68 ± 3.29</td> <!-- NorQuAD -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td class="is ner">44.85 ± 3.44 / 36.23 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.69 ± 2.06 / 35.01 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">25.52 ± 5.27 / 49.12 ± 5.22</td> <!-- NQiI -->
   <td class="de ner">55.32 ± 1.55 / 48.33 ± 1.45</td> <!-- GermEval -->
   <td class="de sent">52.49 ± 2.16 / 67.50 ± 1.61</td> <!-- SB10k -->
   <td class="de la">24.34 ± 2.29 / 59.66 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">31.54 ± 3.00 / 59.96 ± 3.89</td> <!-- GermanQuAD -->
   <td class="nl ner">56.76 ± 1.52 / 42.03 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.11 ± 1.17 / 26.36 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">23.55 ± 2.76 / 59.14 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.89 ± 1.10 / 72.41 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="en ner">61.02 ± 2.70 / 55.57 ± 2.50</td> <!-- CoNLL-en -->
   <td class="en sent">67.10 ± 0.81 / 70.66 ± 0.76</td> <!-- SST5 -->
   <td class="en la">29.82 ± 5.18 / 62.86 ± 4.72</td> <!-- ScaLA-en -->
   <td class="en rc">73.50 ± 1.67 / 84.26 ± 1.30</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.32</td> <!-- Danish rank -->
   <td class="no-rank">2.70</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
   <td class="is-rank">3.27</td> <!-- Icelandic rank -->
   <td class="de-rank">2.12</td> <!-- German rank -->
   <td class="nl-rank">2.93</td> <!-- Dutch rank -->
   <td class="en-rank">1.79</td> <!-- English rank -->
   <td class="da ner">43.60 ± 2.94 / 32.17 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.92 ± 1.50 / 61.91 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">15.43 ± 3.79 / 46.20 ± 5.54</td> <!-- ScaLA-da -->
   <td class="da rc">59.13 ± 0.86 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">50.56 ± 2.04 / 44.38 ± 1.85</td> <!-- NorNE-nb -->
   <td class="no ner">52.65 ± 2.27 / 46.48 ± 3.65</td> <!-- NorNE-nn -->
   <td class="no sent">44.61 ± 2.28 / 62.22 ± 2.10</td> <!-- NoReC -->
   <td class="no la">12.10 ± 4.22 / 43.27 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">9.30 ± 0.99 / 46.11 ± 3.47</td> <!-- ScaLA-nn -->
   <td class="no rc">45.15 ± 3.72 / 68.61 ± 3.30</td> <!-- NorQuAD -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="is ner">44.68 ± 3.50 / 36.20 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.12 ± 1.68 / 35.09 ± 1.17</td> <!-- ScaLA-is -->
   <td class="is rc">25.52 ± 5.24 / 49.15 ± 5.21</td> <!-- NQiI -->
   <td class="de ner">55.41 ± 1.45 / 48.39 ± 1.46</td> <!-- GermEval -->
   <td class="de sent">52.58 ± 2.42 / 67.52 ± 1.82</td> <!-- SB10k -->
   <td class="de la">24.10 ± 2.12 / 59.47 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">31.52 ± 2.95 / 60.03 ± 3.81</td> <!-- GermanQuAD -->
   <td class="nl ner">56.52 ± 1.42 / 41.84 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.02 ± 1.21 / 26.40 ± 2.96</td> <!-- Dutch Social -->
   <td class="nl la">23.41 ± 2.91 / 59.14 ± 3.11</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.90 ± 1.07 / 72.49 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="en ner">61.02 ± 2.74 / 55.65 ± 2.55</td> <!-- CoNLL-en -->
   <td class="en sent">67.29 ± 0.80 / 70.81 ± 0.84</td> <!-- SST5 -->
   <td class="en la">30.10 ± 5.12 / 62.99 ± 4.71</td> <!-- ScaLA-en -->
   <td class="en rc">73.59 ± 1.75 / 84.31 ± 1.35</td> <!-- SQuAD -->
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
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
   <td class="is-rank">3.43</td> <!-- Icelandic rank -->
   <td class="de-rank">2.17</td> <!-- German rank -->
   <td class="nl-rank">2.80</td> <!-- Dutch rank -->
   <td class="en-rank">2.03</td> <!-- English rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da rc">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">61.90 ± 2.57 / 57.16 ± 2.81</td> <!-- NorNE-nb -->
   <td class="no ner">66.92 ± 2.52 / 57.81 ± 3.54</td> <!-- NorNE-nn -->
   <td class="no sent">48.80 ± 4.56 / 63.38 ± 3.06</td> <!-- NoReC -->
   <td class="no la">19.53 ± 5.49 / 51.96 ± 4.90</td> <!-- ScaLA-nb -->
   <td class="no la">9.83 ± 4.57 / 47.95 ± 2.22</td> <!-- ScaLA-nn -->
   <td class="no rc">30.27 ± 2.28 / 62.04 ± 2.19</td> <!-- NorQuAD -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="is ner">50.85 ± 4.15 / 42.91 ± 5.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.80 ± 3.84 / 49.12 ± 2.51</td> <!-- ScaLA-is -->
   <td class="is rc">20.23 ± 3.73 / 52.99 ± 2.11</td> <!-- NQiI -->
   <td class="de ner">63.36 ± 2.68 / 51.59 ± 3.44</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 3.18 / 72.32 ± 2.23</td> <!-- SB10k -->
   <td class="de la">22.98 ± 8.11 / 60.88 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de rc">20.96 ± 3.59 / 57.36 ± 2.94</td> <!-- GermanQuAD -->
   <td class="nl ner">64.71 ± 5.15 / 53.58 ± 3.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.14 ± 3.37 / 38.64 ± 2.36</td> <!-- Dutch Social -->
   <td class="nl la">25.22 ± 5.45 / 61.28 ± 2.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">46.34 ± 1.07 / 66.56 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="en ner">69.19 ± 2.03 / 55.64 ± 3.53</td> <!-- CoNLL-en -->
   <td class="en sent">63.77 ± 2.55 / 71.13 ± 1.83</td> <!-- SST5 -->
   <td class="en la">28.43 ± 3.97 / 62.28 ± 1.86</td> <!-- ScaLA-en -->
   <td class="en rc">44.39 ± 2.68 / 71.79 ± 1.25</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="is-rank">3.26</td> <!-- Icelandic rank -->
   <td class="de-rank">2.16</td> <!-- German rank -->
   <td class="nl-rank">2.84</td> <!-- Dutch rank -->
   <td class="en-rank">2.74</td> <!-- English rank -->
   <td class="da ner">70.36 ± 2.14 / 65.91 ± 2.15</td> <!-- DANSK -->
   <td class="da sent">47.83 ± 1.46 / 65.49 ± 0.96</td> <!-- Angry Tweets -->
   <td class="da la">11.87 ± 5.47 / 48.82 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da rc">29.87 ± 3.18 / 35.11 ± 2.73</td> <!-- ScandiQA-da -->
   <td class="no ner">90.07 ± 1.08 / 87.56 ± 1.39</td> <!-- NorNE-nb -->
   <td class="no ner">85.65 ± 0.96 / 82.40 ± 1.16</td> <!-- NorNE-nn -->
   <td class="no sent">54.46 ± 1.16 / 68.25 ± 0.76</td> <!-- NoReC -->
   <td class="no la">12.16 ± 5.91 / 50.55 ± 4.73</td> <!-- ScaLA-nb -->
   <td class="no la">8.99 ± 2.25 / 48.57 ± 3.67</td> <!-- ScaLA-nn -->
   <td class="no rc">49.24 ± 1.30 / 64.35 ± 1.24</td> <!-- NorQuAD -->
   <td class="sv ner">78.60 ± 1.91 / 73.04 ± 2.25</td> <!-- SUC3 -->
   <td class="sv sent">73.67 ± 1.48 / 68.61 ± 3.14</td> <!-- SweReC -->
   <td class="sv la">15.41 ± 4.59 / 53.29 ± 3.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.41 ± 3.14 / 37.13 ± 3.07</td> <!-- ScandiQA-sv -->
   <td class="is ner">78.01 ± 2.18 / 79.20 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.92 ± 1.91 / 46.95 ± 3.38</td> <!-- ScaLA-is -->
   <td class="is rc">10.47 ± 1.42 / 43.32 ± 3.55</td> <!-- NQiI -->
   <td class="de ner">79.38 ± 0.80 / 79.33 ± 0.74</td> <!-- GermEval -->
   <td class="de sent">58.58 ± 2.31 / 72.09 ± 1.64</td> <!-- SB10k -->
   <td class="de la">15.34 ± 5.24 / 52.99 ± 1.90</td> <!-- ScaLA-de -->
   <td class="de rc">16.58 ± 6.50 / 32.33 ± 11.35</td> <!-- GermanQuAD -->
   <td class="nl ner">78.85 ± 2.48 / 83.35 ± 2.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.80 ± 7.64 / 33.49 ± 6.73</td> <!-- Dutch Social -->
   <td class="nl la">14.56 ± 8.02 / 53.64 ± 5.14</td> <!-- ScaLA-nl -->
   <td class="nl rc">42.08 ± 7.94 / 51.94 ± 9.08</td> <!-- SQuAD-nl -->
   <td class="en ner">88.62 ± 0.53 / 88.44 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">11.09 ± 10.39 / 33.19 ± 4.75</td> <!-- SST5 -->
   <td class="en la">8.46 ± 2.34 / 51.98 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en rc">49.64 ± 1.94 / 62.02 ± 1.77</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da-rank">2.34</td> <!-- Danish rank -->
   <td class="no-rank">2.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.99</td> <!-- Swedish rank -->
   <td class="is-rank">3.60</td> <!-- Icelandic rank -->
   <td class="de-rank">2.30</td> <!-- German rank -->
   <td class="nl-rank">3.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.90</td> <!-- English rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
   <td class="no ner">48.97 ± 2.42 / 39.15 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">51.52 ± 2.96 / 40.17 ± 3.62</td> <!-- NorNE-nn -->
   <td class="no sent">49.05 ± 2.73 / 63.94 ± 2.42</td> <!-- NoReC -->
   <td class="no la">14.37 ± 2.18 / 47.80 ± 4.36</td> <!-- ScaLA-nb -->
   <td class="no la">9.96 ± 1.34 / 48.97 ± 3.77</td> <!-- ScaLA-nn -->
   <td class="no rc">44.07 ± 3.40 / 68.49 ± 2.97</td> <!-- NorQuAD -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="is ner">36.47 ± 4.24 / 30.33 ± 3.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is rc">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="de ner">50.66 ± 1.53 / 39.89 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">54.79 ± 3.53 / 68.79 ± 3.00</td> <!-- SB10k -->
   <td class="de la">20.17 ± 1.69 / 58.67 ± 1.13</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 4.70 / 54.38 ± 5.91</td> <!-- GermanQuAD -->
   <td class="nl ner">54.56 ± 2.96 / 37.86 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.43 ± 1.27 / 24.23 ± 0.94</td> <!-- Dutch Social -->
   <td class="nl la">10.99 ± 2.55 / 50.46 ± 4.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.91 ± 1.08 / 66.78 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="en ner">59.10 ± 1.87 / 51.31 ± 1.87</td> <!-- CoNLL-en -->
   <td class="en sent">68.41 ± 1.17 / 70.85 ± 0.74</td> <!-- SST5 -->
   <td class="en la">25.43 ± 4.22 / 60.79 ± 3.45</td> <!-- ScaLA-en -->
   <td class="en rc">71.89 ± 2.20 / 82.99 ± 1.78</td> <!-- SQuAD -->
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
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da-rank">2.43</td> <!-- Danish rank -->
   <td class="no-rank">2.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
   <td class="is-rank">3.23</td> <!-- Icelandic rank -->
   <td class="de-rank">2.20</td> <!-- German rank -->
   <td class="nl-rank">3.10</td> <!-- Dutch rank -->
   <td class="en-rank">2.21</td> <!-- English rank -->
   <td class="da ner">60.01 ± 2.63 / 56.13 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">42.17 ± 1.64 / 61.25 ± 1.45</td> <!-- Angry Tweets -->
   <td class="da la">29.43 ± 13.02 / 62.08 ± 7.77</td> <!-- ScaLA-da -->
   <td class="da rc">29.79 ± 3.33 / 34.82 ± 2.83</td> <!-- ScandiQA-da -->
   <td class="no ner">84.11 ± 1.00 / 81.35 ± 1.22</td> <!-- NorNE-nb -->
   <td class="no ner">77.22 ± 1.99 / 73.67 ± 2.26</td> <!-- NorNE-nn -->
   <td class="no sent">37.02 ± 1.09 / 47.88 ± 2.50</td> <!-- NoReC -->
   <td class="no la">35.42 ± 12.32 / 66.30 ± 6.78</td> <!-- ScaLA-nb -->
   <td class="no la">6.87 ± 6.85 / 50.70 ± 3.62</td> <!-- ScaLA-nn -->
   <td class="no rc">25.98 ± 2.87 / 36.16 ± 3.35</td> <!-- NorQuAD -->
   <td class="sv ner">70.17 ± 0.99 / 64.19 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">66.62 ± 1.71 / 61.90 ± 2.61</td> <!-- SweReC -->
   <td class="sv la">46.72 ± 3.65 / 72.15 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.38 ± 1.36 / 35.79 ± 1.33</td> <!-- ScandiQA-sv -->
   <td class="is ner">70.38 ± 1.44 / 72.00 ± 1.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">11.09 ± 6.94 / 51.60 ± 5.19</td> <!-- ScaLA-is -->
   <td class="is rc">7.67 ± 0.74 / 30.52 ± 0.52</td> <!-- NQiI -->
   <td class="de ner">70.35 ± 1.34 / 69.09 ± 1.36</td> <!-- GermEval -->
   <td class="de sent">55.03 ± 2.38 / 69.65 ± 1.75</td> <!-- SB10k -->
   <td class="de la">43.87 ± 8.85 / 69.71 ± 6.73</td> <!-- ScaLA-de -->
   <td class="de rc">2.81 ± 0.73 / 10.15 ± 2.34</td> <!-- GermanQuAD -->
   <td class="nl ner">74.03 ± 3.05 / 80.59 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.53 ± 5.28 / 32.06 ± 4.17</td> <!-- Dutch Social -->
   <td class="nl la">39.12 ± 12.90 / 68.36 ± 6.85</td> <!-- ScaLA-nl -->
   <td class="nl rc">7.71 ± 0.42 / 12.90 ± 0.39</td> <!-- SQuAD-nl -->
   <td class="en ner">87.77 ± 0.51 / 87.83 ± 0.47</td> <!-- CoNLL-en -->
   <td class="en sent">41.09 ± 4.38 / 48.17 ± 3.16</td> <!-- SST5 -->
   <td class="en la">32.26 ± 10.79 / 61.20 ± 5.53</td> <!-- ScaLA-en -->
   <td class="en rc">35.15 ± 1.89 / 44.98 ± 1.93</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.61</td> <!-- Danish rank -->
   <td class="no-rank">2.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.31</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="de-rank">2.35</td> <!-- German rank -->
   <td class="nl-rank">2.77</td> <!-- Dutch rank -->
   <td class="en-rank">1.85</td> <!-- English rank -->
   <td class="da ner">48.44 ± 1.69 / 36.99 ± 1.77</td> <!-- DANSK -->
   <td class="da sent">39.07 ± 1.03 / 56.85 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">9.72 ± 1.58 / 46.85 ± 3.66</td> <!-- ScaLA-da -->
   <td class="da rc">51.18 ± 0.92 / 56.54 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="no ner">68.40 ± 1.16 / 62.53 ± 1.69</td> <!-- NorNE-nb -->
   <td class="no ner">65.15 ± 0.79 / 60.39 ± 2.11</td> <!-- NorNE-nn -->
   <td class="no sent">42.00 ± 1.78 / 59.90 ± 1.22</td> <!-- NoReC -->
   <td class="no la">5.20 ± 2.23 / 36.33 ± 1.30</td> <!-- ScaLA-nb -->
   <td class="no la">3.32 ± 2.02 / 37.81 ± 3.26</td> <!-- ScaLA-nn -->
   <td class="no rc">37.51 ± 2.58 / 60.94 ± 3.06</td> <!-- NorQuAD -->
   <td class="sv ner">59.77 ± 3.55 / 45.71 ± 4.91</td> <!-- SUC3 -->
   <td class="sv sent">74.45 ± 1.19 / 72.26 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">3.97 ± 1.50 / 34.79 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 1.05 / 56.07 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">50.89 ± 2.90 / 35.75 ± 4.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.50 ± 0.94 / 33.77 ± 0.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.43 ± 3.38 / 41.32 ± 3.18</td> <!-- NQiI -->
   <td class="de ner">59.07 ± 0.78 / 51.00 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.44 / 65.93 ± 1.66</td> <!-- SB10k -->
   <td class="de la">14.71 ± 2.21 / 53.75 ± 3.07</td> <!-- ScaLA-de -->
   <td class="de rc">29.45 ± 2.13 / 56.14 ± 2.53</td> <!-- GermanQuAD -->
   <td class="nl ner">63.29 ± 2.51 / 52.18 ± 4.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.81 ± 1.66 / 36.99 ± 2.58</td> <!-- Dutch Social -->
   <td class="nl la">8.16 ± 1.97 / 44.29 ± 4.25</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.64 ± 0.68 / 66.29 ± 0.71</td> <!-- SQuAD-nl -->
   <td class="en ner">72.76 ± 0.57 / 67.49 ± 0.90</td> <!-- CoNLL-en -->
   <td class="en sent">62.35 ± 1.68 / 67.34 ± 0.77</td> <!-- SST5 -->
   <td class="en la">21.57 ± 2.22 / 59.22 ± 1.69</td> <!-- ScaLA-en -->
   <td class="en rc">69.80 ± 3.60 / 81.37 ± 2.26</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.37</td> <!-- Danish rank -->
   <td class="no-rank">2.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
   <td class="is-rank">3.62</td> <!-- Icelandic rank -->
   <td class="de-rank">2.22</td> <!-- German rank -->
   <td class="nl-rank">2.97</td> <!-- Dutch rank -->
   <td class="en-rank">1.97</td> <!-- English rank -->
   <td class="da ner">44.00 ± 2.63 / 29.00 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.41 ± 1.79 / 62.27 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">16.17 ± 2.17 / 56.93 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">57.06 ± 0.83 / 63.94 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="no ner">57.21 ± 1.51 / 40.40 ± 2.79</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.34 / 41.07 ± 2.58</td> <!-- NorNE-nn -->
   <td class="no sent">38.93 ± 3.56 / 57.45 ± 3.77</td> <!-- NoReC -->
   <td class="no la">8.65 ± 3.33 / 47.18 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">5.92 ± 1.58 / 47.50 ± 3.58</td> <!-- ScaLA-nn -->
   <td class="no rc">42.32 ± 2.80 / 69.24 ± 2.68</td> <!-- NorQuAD -->
   <td class="sv ner">49.90 ± 2.28 / 35.48 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 2.05 / 79.13 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">14.67 ± 2.27 / 53.90 ± 2.24</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.12 ± 0.70 / 63.72 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="is ner">37.53 ± 3.42 / 30.51 ± 3.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.14 ± 1.96 / 39.45 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">20.91 ± 2.93 / 43.86 ± 1.90</td> <!-- NQiI -->
   <td class="de ner">57.57 ± 1.46 / 44.84 ± 2.12</td> <!-- GermEval -->
   <td class="de sent">49.40 ± 2.11 / 63.02 ± 2.68</td> <!-- SB10k -->
   <td class="de la">23.32 ± 2.20 / 59.16 ± 2.36</td> <!-- ScaLA-de -->
   <td class="de rc">30.24 ± 1.18 / 61.10 ± 1.87</td> <!-- GermanQuAD -->
   <td class="nl ner">57.80 ± 1.53 / 39.43 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 1.27 / 29.84 ± 2.35</td> <!-- Dutch Social -->
   <td class="nl la">17.40 ± 1.54 / 57.26 ± 1.96</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.35 ± 0.85 / 69.69 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="en ner">68.75 ± 1.54 / 60.01 ± 1.57</td> <!-- CoNLL-en -->
   <td class="en sent">62.37 ± 1.68 / 67.79 ± 1.51</td> <!-- SST5 -->
   <td class="en la">25.07 ± 3.20 / 61.02 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en rc">61.56 ± 1.18 / 80.11 ± 0.70</td> <!-- SQuAD -->
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
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.11.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
   <td class="is-rank">3.61</td> <!-- Icelandic rank -->
   <td class="de-rank">2.56</td> <!-- German rank -->
   <td class="nl-rank">2.48</td> <!-- Dutch rank -->
   <td class="en-rank">2.19</td> <!-- English rank -->
   <td class="da ner">61.17 ± 2.09 / 58.41 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">46.39 ± 1.25 / 63.97 ± 1.08</td> <!-- Angry Tweets -->
   <td class="da la">38.61 ± 1.86 / 67.08 ± 1.08</td> <!-- ScaLA-da -->
   <td class="da rc">19.90 ± 1.09 / 25.77 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="no ner">81.26 ± 1.25 / 77.69 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.05 ± 1.72 / 69.84 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">49.93 ± 1.46 / 62.37 ± 2.34</td> <!-- NoReC -->
   <td class="no la">38.26 ± 7.56 / 66.01 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">25.17 ± 5.32 / 61.27 ± 3.01</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">70.22 ± 1.49 / 63.97 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">71.33 ± 1.20 / 65.44 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">39.60 ± 5.87 / 66.60 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv rc">18.65 ± 1.15 / 24.75 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="is ner">65.15 ± 1.02 / 67.50 ± 0.90</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.15 ± 1.57 / 49.60 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">9.56 ± 0.42 / 27.88 ± 0.44</td> <!-- NQiI -->
   <td class="de ner">69.45 ± 0.82 / 68.02 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">57.94 ± 2.12 / 71.92 ± 1.45</td> <!-- SB10k -->
   <td class="de la">21.81 ± 12.05 / 58.13 ± 4.73</td> <!-- ScaLA-de -->
   <td class="de rc">0.33 ± 0.15 / 3.03 ± 1.06</td> <!-- GermanQuAD -->
   <td class="nl ner">70.59 ± 1.60 / 78.25 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">21.37 ± 8.79 / 40.62 ± 7.64</td> <!-- Dutch Social -->
   <td class="nl la">45.86 ± 2.06 / 71.32 ± 1.40</td> <!-- ScaLA-nl -->
   <td class="nl rc">5.20 ± 0.30 / 10.40 ± 0.38</td> <!-- SQuAD-nl -->
   <td class="en ner">84.05 ± 0.61 / 84.48 ± 0.51</td> <!-- CoNLL-en -->
   <td class="en sent">54.92 ± 1.28 / 52.65 ± 0.58</td> <!-- SST5 -->
   <td class="en la">45.85 ± 1.41 / 71.78 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">4.13 ± 0.19 / 10.53 ± 0.24</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">2.93</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.98</td> <!-- Swedish rank -->
   <td class="is-rank">3.51</td> <!-- Icelandic rank -->
   <td class="de-rank">2.29</td> <!-- German rank -->
   <td class="nl-rank">3.05</td> <!-- Dutch rank -->
   <td class="en-rank">1.89</td> <!-- English rank -->
   <td class="da ner">41.28 ± 3.92 / 31.98 ± 3.26</td> <!-- DANSK -->
   <td class="da sent">23.01 ± 3.87 / 36.55 ± 6.42</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 2.75 / 58.11 ± 3.45</td> <!-- ScaLA-da -->
   <td class="da rc">60.29 ± 0.81 / 65.52 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="no ner">51.12 ± 3.13 / 47.26 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">55.35 ± 1.60 / 49.99 ± 2.21</td> <!-- NorNE-nn -->
   <td class="no sent">23.75 ± 3.25 / 42.92 ± 4.45</td> <!-- NoReC -->
   <td class="no la">14.00 ± 4.25 / 42.71 ± 5.83</td> <!-- ScaLA-nb -->
   <td class="no la">7.61 ± 2.57 / 45.86 ± 3.96</td> <!-- ScaLA-nn -->
   <td class="no rc">49.24 ± 4.28 / 72.68 ± 3.66</td> <!-- NorQuAD -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td class="is ner">36.56 ± 3.03 / 34.23 ± 3.45</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.73 ± 1.56 / 45.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is rc">21.97 ± 4.26 / 46.27 ± 3.94</td> <!-- NQiI -->
   <td class="de ner">52.08 ± 1.86 / 46.67 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">46.38 ± 2.70 / 60.32 ± 2.80</td> <!-- SB10k -->
   <td class="de la">22.39 ± 3.96 / 57.26 ± 4.22</td> <!-- ScaLA-de -->
   <td class="de rc">33.43 ± 2.38 / 62.65 ± 2.83</td> <!-- GermanQuAD -->
   <td class="nl ner">52.55 ± 1.64 / 43.32 ± 1.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.26 ± 2.09 / 28.32 ± 2.68</td> <!-- Dutch Social -->
   <td class="nl la">24.57 ± 3.54 / 54.94 ± 5.33</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.99 ± 0.95 / 72.74 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="en ner">63.75 ± 2.50 / 59.28 ± 2.20</td> <!-- CoNLL-en -->
   <td class="en sent">61.85 ± 1.70 / 69.02 ± 0.76</td> <!-- SST5 -->
   <td class="en la">26.41 ± 4.93 / 59.67 ± 4.84</td> <!-- ScaLA-en -->
   <td class="en rc">73.48 ± 2.06 / 85.27 ± 1.15</td> <!-- SQuAD -->
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
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da-rank">2.37</td> <!-- Danish rank -->
   <td class="no-rank">2.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.36</td> <!-- Swedish rank -->
   <td class="is-rank">3.48</td> <!-- Icelandic rank -->
   <td class="de-rank">2.33</td> <!-- German rank -->
   <td class="nl-rank">2.89</td> <!-- Dutch rank -->
   <td class="en-rank">2.03</td> <!-- English rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da rc">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no rc">35.74 ± 2.44 / 64.27 ± 2.42</td> <!-- NorQuAD -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is rc">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="de ner">55.10 ± 1.35 / 41.89 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">47.69 ± 2.35 / 64.93 ± 1.71</td> <!-- SB10k -->
   <td class="de la">24.14 ± 2.09 / 60.83 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">23.93 ± 2.11 / 57.64 ± 1.89</td> <!-- GermanQuAD -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en rc">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
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
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="da-rank">2.45</td> <!-- Danish rank -->
   <td class="no-rank">2.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.27</td> <!-- Swedish rank -->
   <td class="is-rank">3.70</td> <!-- Icelandic rank -->
   <td class="de-rank">2.34</td> <!-- German rank -->
   <td class="nl-rank">2.97</td> <!-- Dutch rank -->
   <td class="en-rank">1.89</td> <!-- English rank -->
   <td class="da ner">43.17 ± 2.78 / 31.37 ± 2.95</td> <!-- DANSK -->
   <td class="da sent">43.40 ± 2.20 / 57.24 ± 3.52</td> <!-- Angry Tweets -->
   <td class="da la">11.08 ± 2.98 / 43.40 ± 4.66</td> <!-- ScaLA-da -->
   <td class="da rc">56.81 ± 0.70 / 63.10 ± 0.35</td> <!-- ScandiQA-da -->
   <td class="no ner">58.61 ± 1.58 / 47.74 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">60.40 ± 1.25 / 47.53 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">41.36 ± 3.50 / 58.47 ± 3.79</td> <!-- NoReC -->
   <td class="no la">6.52 ± 2.11 / 38.10 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 2.52 / 42.37 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no rc">38.93 ± 2.43 / 65.76 ± 3.07</td> <!-- NorQuAD -->
   <td class="sv ner">50.85 ± 2.44 / 39.65 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">74.17 ± 2.12 / 76.62 ± 1.83</td> <!-- SweReC -->
   <td class="sv la">7.51 ± 1.94 / 37.81 ± 1.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.32 ± 0.63 / 63.28 ± 0.71</td> <!-- ScandiQA-sv -->
   <td class="is ner">28.35 ± 2.89 / 26.44 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.14 ± 1.74 / 44.57 ± 3.85</td> <!-- ScaLA-is -->
   <td class="is rc">19.80 ± 2.66 / 43.44 ± 1.74</td> <!-- NQiI -->
   <td class="de ner">57.02 ± 1.39 / 47.95 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.02 / 62.41 ± 3.30</td> <!-- SB10k -->
   <td class="de la">19.80 ± 3.22 / 52.76 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 2.01 / 57.65 ± 2.01</td> <!-- GermanQuAD -->
   <td class="nl ner">57.66 ± 1.29 / 43.77 ± 2.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.41 ± 1.47 / 25.59 ± 1.30</td> <!-- Dutch Social -->
   <td class="nl la">16.93 ± 2.60 / 55.72 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.29 ± 1.11 / 68.94 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en rc">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">2.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.35</td> <!-- Swedish rank -->
   <td class="is-rank">3.58</td> <!-- Icelandic rank -->
   <td class="de-rank">2.11</td> <!-- German rank -->
   <td class="nl-rank">3.02</td> <!-- Dutch rank -->
   <td class="en-rank">2.03</td> <!-- English rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da rc">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="no ner">45.50 ± 2.71 / 40.02 ± 3.16</td> <!-- NorNE-nb -->
   <td class="no ner">45.96 ± 2.67 / 41.28 ± 2.25</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 3.40 / 62.00 ± 2.71</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no rc">52.19 ± 2.88 / 74.97 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="is ner">40.71 ± 2.93 / 34.57 ± 4.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is rc">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="de ner">52.63 ± 1.89 / 42.99 ± 2.40</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de rc">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td class="nl ner">53.78 ± 1.86 / 41.29 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="en ner">56.90 ± 3.08 / 51.16 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en rc">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.2.0</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.2.0</td> <!-- Dutch Social version -->
   <td>12.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">2.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
   <td class="is-rank">3.62</td> <!-- Icelandic rank -->
   <td class="de-rank">2.50</td> <!-- German rank -->
   <td class="nl-rank">2.87</td> <!-- Dutch rank -->
   <td class="en-rank">2.18</td> <!-- English rank -->
   <td class="da ner">58.52 ± 1.78 / 55.04 ± 1.60</td> <!-- DANSK -->
   <td class="da sent">42.26 ± 1.13 / 61.41 ± 0.76</td> <!-- Angry Tweets -->
   <td class="da la">34.80 ± 5.89 / 64.51 ± 4.90</td> <!-- ScaLA-da -->
   <td class="da rc">19.60 ± 1.60 / 25.68 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="no ner">80.08 ± 1.46 / 75.93 ± 1.64</td> <!-- NorNE-nb -->
   <td class="no ner">74.59 ± 1.98 / 70.26 ± 2.24</td> <!-- NorNE-nn -->
   <td class="no sent">52.16 ± 0.99 / 66.79 ± 0.98</td> <!-- NoReC -->
   <td class="no la">36.30 ± 6.44 / 65.52 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">14.21 ± 6.44 / 52.78 ± 5.69</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">68.94 ± 1.53 / 62.54 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 0.89 / 68.13 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">40.21 ± 2.53 / 67.11 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.09 ± 1.31 / 25.99 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="is ner">66.23 ± 1.24 / 67.76 ± 1.08</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.04 ± 0.78 / 45.96 ± 2.83</td> <!-- ScaLA-is -->
   <td class="is rc">10.04 ± 0.99 / 28.66 ± 0.92</td> <!-- NQiI -->
   <td class="de ner">67.47 ± 1.09 / 66.34 ± 1.08</td> <!-- GermEval -->
   <td class="de sent">52.85 ± 1.53 / 68.48 ± 1.02</td> <!-- SB10k -->
   <td class="de la">29.59 ± 6.40 / 60.98 ± 2.57</td> <!-- ScaLA-de -->
   <td class="de rc">0.73 ± 0.17 / 4.35 ± 1.32</td> <!-- GermanQuAD -->
   <td class="nl ner">66.85 ± 1.32 / 72.84 ± 0.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">20.56 ± 1.44 / 39.67 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">35.56 ± 1.76 / 66.00 ± 1.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">5.04 ± 0.46 / 10.13 ± 0.40</td> <!-- SQuAD-nl -->
   <td class="en ner">82.39 ± 0.62 / 83.07 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">57.35 ± 1.00 / 54.82 ± 0.65</td> <!-- SST5 -->
   <td class="en la">47.29 ± 2.10 / 71.85 ± 1.30</td> <!-- ScaLA-en -->
   <td class="en rc">4.29 ± 0.33 / 10.53 ± 0.29</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
   <td class="is-rank">3.81</td> <!-- Icelandic rank -->
   <td class="de-rank">2.00</td> <!-- German rank -->
   <td class="nl-rank">3.01</td> <!-- Dutch rank -->
   <td class="en-rank">1.82</td> <!-- English rank -->
   <td class="da ner">41.37 ± 2.50 / 24.64 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">42.60 ± 1.06 / 61.52 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">6.52 ± 1.34 / 45.01 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">50.57 ± 1.03 / 57.75 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="no ner">56.33 ± 1.63 / 36.68 ± 3.27</td> <!-- NorNE-nb -->
   <td class="no ner">54.68 ± 1.29 / 37.85 ± 3.79</td> <!-- NorNE-nn -->
   <td class="no sent">37.18 ± 1.30 / 55.44 ± 1.46</td> <!-- NoReC -->
   <td class="no la">6.76 ± 2.81 / 41.69 ± 2.82</td> <!-- ScaLA-nb -->
   <td class="no la">6.79 ± 1.51 / 45.45 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no rc">30.11 ± 2.09 / 52.56 ± 2.38</td> <!-- NorQuAD -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="is ner">33.05 ± 4.29 / 29.75 ± 3.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 1.18 / 34.80 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">17.23 ± 2.51 / 39.88 ± 1.59</td> <!-- NQiI -->
   <td class="de ner">59.68 ± 0.41 / 48.00 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.75 ± 2.36 / 68.54 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.22 ± 2.94 / 64.51 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">29.27 ± 1.03 / 59.19 ± 2.46</td> <!-- GermanQuAD -->
   <td class="nl ner">50.31 ± 1.94 / 41.54 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.58 ± 1.62 / 36.56 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">14.72 ± 1.84 / 50.23 ± 3.10</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.19 ± 0.80 / 66.72 ± 0.92</td> <!-- SQuAD-nl -->
   <td class="en ner">66.13 ± 1.16 / 53.55 ± 2.73</td> <!-- CoNLL-en -->
   <td class="en sent">63.66 ± 1.31 / 70.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">34.07 ± 2.32 / 66.51 ± 1.23</td> <!-- ScaLA-en -->
   <td class="en rc">68.10 ± 1.44 / 83.46 ± 1.01</td> <!-- SQuAD -->
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
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">2.96</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
   <td class="is-rank">3.52</td> <!-- Icelandic rank -->
   <td class="de-rank">2.30</td> <!-- German rank -->
   <td class="nl-rank">3.15</td> <!-- Dutch rank -->
   <td class="en-rank">2.01</td> <!-- English rank -->
   <td class="da ner">66.39 ± 1.42 / 62.24 ± 1.29</td> <!-- DANSK -->
   <td class="da sent">39.36 ± 3.13 / 58.64 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">7.06 ± 6.11 / 49.71 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da rc">33.88 ± 4.27 / 38.42 ± 4.16</td> <!-- ScandiQA-da -->
   <td class="no ner">86.26 ± 0.71 / 83.48 ± 1.19</td> <!-- NorNE-nb -->
   <td class="no ner">80.10 ± 2.44 / 76.17 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">34.17 ± 2.42 / 43.74 ± 2.19</td> <!-- NoReC -->
   <td class="no la">12.11 ± 10.47 / 50.33 ± 7.16</td> <!-- ScaLA-nb -->
   <td class="no la">4.28 ± 4.18 / 45.75 ± 4.32</td> <!-- ScaLA-nn -->
   <td class="no rc">11.74 ± 10.45 / 16.38 ± 14.33</td> <!-- NorQuAD -->
   <td class="sv ner">74.26 ± 1.65 / 68.20 ± 1.70</td> <!-- SUC3 -->
   <td class="sv sent">63.35 ± 5.43 / 60.33 ± 5.50</td> <!-- SweReC -->
   <td class="sv la">16.07 ± 10.73 / 52.48 ± 7.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">36.77 ± 3.78 / 41.72 ± 3.83</td> <!-- ScandiQA-sv -->
   <td class="is ner">71.48 ± 1.97 / 73.71 ± 1.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.20 ± 2.00 / 43.42 ± 4.87</td> <!-- ScaLA-is -->
   <td class="is rc">8.19 ± 0.76 / 33.02 ± 1.85</td> <!-- NQiI -->
   <td class="de ner">74.36 ± 1.33 / 73.61 ± 1.47</td> <!-- GermEval -->
   <td class="de sent">53.52 ± 2.28 / 68.49 ± 1.49</td> <!-- SB10k -->
   <td class="de la">22.26 ± 11.63 / 58.51 ± 6.63</td> <!-- ScaLA-de -->
   <td class="de rc">11.68 ± 4.11 / 22.54 ± 7.80</td> <!-- GermanQuAD -->
   <td class="nl ner">77.35 ± 2.80 / 82.50 ± 1.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.55 ± 5.33 / 28.68 ± 3.64</td> <!-- Dutch Social -->
   <td class="nl la">18.25 ± 8.41 / 54.00 ± 5.57</td> <!-- ScaLA-nl -->
   <td class="nl rc">28.37 ± 4.84 / 36.84 ± 5.92</td> <!-- SQuAD-nl -->
   <td class="en ner">89.50 ± 0.47 / 89.39 ± 0.41</td> <!-- CoNLL-en -->
   <td class="en sent">45.98 ± 2.97 / 49.81 ± 2.03</td> <!-- SST5 -->
   <td class="en la">30.58 ± 13.07 / 61.93 ± 7.87</td> <!-- ScaLA-en -->
   <td class="en rc">48.44 ± 1.37 / 59.47 ± 1.12</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="da-rank">2.53</td> <!-- Danish rank -->
   <td class="no-rank">2.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.36</td> <!-- Swedish rank -->
   <td class="is-rank">3.69</td> <!-- Icelandic rank -->
   <td class="de-rank">2.44</td> <!-- German rank -->
   <td class="nl-rank">3.14</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da rc">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no rc">37.23 ± 3.15 / 63.67 ± 2.98</td> <!-- NorQuAD -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="de ner">47.19 ± 3.74 / 33.02 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">47.26 ± 3.14 / 63.48 ± 2.94</td> <!-- SB10k -->
   <td class="de la">22.32 ± 1.78 / 56.73 ± 4.00</td> <!-- ScaLA-de -->
   <td class="de rc">24.36 ± 3.78 / 54.61 ± 4.44</td> <!-- GermanQuAD -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en rc">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="da-rank">2.63</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.27</td> <!-- Swedish rank -->
   <td class="is-rank">3.70</td> <!-- Icelandic rank -->
   <td class="de-rank">2.28</td> <!-- German rank -->
   <td class="nl-rank">3.11</td> <!-- Dutch rank -->
   <td class="en-rank">2.09</td> <!-- English rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="no ner">45.28 ± 3.06 / 41.73 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">46.00 ± 4.26 / 42.96 ± 3.38</td> <!-- NorNE-nn -->
   <td class="no sent">44.95 ± 3.19 / 61.88 ± 2.88</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no rc">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="de ner">51.39 ± 1.35 / 44.47 ± 2.77</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td class="nl ner">51.31 ± 2.32 / 42.95 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="en ner">55.37 ± 2.94 / 51.08 ± 2.87</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en rc">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.65</td> <!-- Danish rank -->
   <td class="no-rank">2.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.36</td> <!-- Swedish rank -->
   <td class="is-rank">3.65</td> <!-- Icelandic rank -->
   <td class="de-rank">2.42</td> <!-- German rank -->
   <td class="nl-rank">2.98</td> <!-- Dutch rank -->
   <td class="en-rank">2.32</td> <!-- English rank -->
   <td class="da ner">58.44 ± 2.08 / 55.32 ± 1.81</td> <!-- DANSK -->
   <td class="da sent">31.81 ± 1.65 / 53.25 ± 1.65</td> <!-- Angry Tweets -->
   <td class="da la">34.13 ± 2.81 / 65.98 ± 2.30</td> <!-- ScaLA-da -->
   <td class="da rc">27.60 ± 1.58 / 32.18 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">83.59 ± 1.36 / 80.55 ± 1.53</td> <!-- NorNE-nb -->
   <td class="no ner">80.29 ± 1.02 / 76.08 ± 1.06</td> <!-- NorNE-nn -->
   <td class="no sent">33.19 ± 1.75 / 46.63 ± 2.55</td> <!-- NoReC -->
   <td class="no la">32.60 ± 6.93 / 65.19 ± 3.31</td> <!-- ScaLA-nb -->
   <td class="no la">24.97 ± 6.47 / 61.39 ± 3.34</td> <!-- ScaLA-nn -->
   <td class="no rc">19.93 ± 1.76 / 30.69 ± 2.36</td> <!-- NorQuAD -->
   <td class="sv ner">70.56 ± 1.36 / 64.49 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">60.69 ± 0.46 / 56.69 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">30.83 ± 1.47 / 63.39 ± 1.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.41 ± 1.05 / 36.45 ± 1.05</td> <!-- ScandiQA-sv -->
   <td class="is ner">65.76 ± 0.98 / 68.15 ± 0.89</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.08 ± 1.89 / 48.68 ± 2.96</td> <!-- ScaLA-is -->
   <td class="is rc">6.81 ± 0.33 / 30.96 ± 0.65</td> <!-- NQiI -->
   <td class="de ner">72.97 ± 0.68 / 71.83 ± 0.80</td> <!-- GermEval -->
   <td class="de sent">41.51 ± 1.91 / 60.79 ± 1.27</td> <!-- SB10k -->
   <td class="de la">45.39 ± 1.52 / 71.60 ± 0.73</td> <!-- ScaLA-de -->
   <td class="de rc">1.89 ± 0.52 / 6.88 ± 1.73</td> <!-- GermanQuAD -->
   <td class="nl ner">75.02 ± 1.48 / 81.57 ± 0.76</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.45 ± 2.99 / 29.70 ± 1.94</td> <!-- Dutch Social -->
   <td class="nl la">45.28 ± 0.55 / 71.89 ± 0.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.18 ± 1.26 / 27.86 ± 1.48</td> <!-- SQuAD-nl -->
   <td class="en ner">87.08 ± 0.62 / 87.08 ± 0.57</td> <!-- CoNLL-en -->
   <td class="en sent">36.77 ± 1.52 / 45.15 ± 0.60</td> <!-- SST5 -->
   <td class="en la">37.10 ± 1.79 / 67.20 ± 1.15</td> <!-- ScaLA-en -->
   <td class="en rc">26.99 ± 0.77 / 37.98 ± 0.63</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.30</td> <!-- Swedish rank -->
   <td class="is-rank">3.69</td> <!-- Icelandic rank -->
   <td class="de-rank">2.46</td> <!-- German rank -->
   <td class="nl-rank">3.19</td> <!-- Dutch rank -->
   <td class="en-rank">2.09</td> <!-- English rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no rc">44.19 ± 4.13 / 66.18 ± 4.05</td> <!-- NorQuAD -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="de ner">43.02 ± 1.93 / 32.69 ± 1.98</td> <!-- GermEval -->
   <td class="de sent">50.21 ± 2.43 / 65.81 ± 1.82</td> <!-- SB10k -->
   <td class="de la">15.79 ± 2.35 / 53.25 ± 4.45</td> <!-- ScaLA-de -->
   <td class="de rc">28.57 ± 5.09 / 55.54 ± 6.14</td> <!-- GermanQuAD -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.92 ± 0.61 / 70.24 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en rc">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
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
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>9.2.0</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.2.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.2.0</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.2.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="da-rank">3.17</td> <!-- Danish rank -->
   <td class="no-rank">3.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
   <td class="is-rank">3.58</td> <!-- Icelandic rank -->
   <td class="de-rank">2.49</td> <!-- German rank -->
   <td class="nl-rank">3.23</td> <!-- Dutch rank -->
   <td class="en-rank">1.72</td> <!-- English rank -->
   <td class="da ner">35.21 ± 2.52 / 23.65 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">12.73 ± 2.87 / 22.69 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">4.75 ± 2.45 / 35.71 ± 3.01</td> <!-- ScaLA-da -->
   <td class="da rc">55.95 ± 1.09 / 61.53 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">46.02 ± 2.12 / 35.05 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">48.72 ± 1.76 / 35.97 ± 2.78</td> <!-- NorNE-nn -->
   <td class="no sent">27.86 ± 0.76 / 31.62 ± 0.80</td> <!-- NoReC -->
   <td class="no la">2.41 ± 1.92 / 35.60 ± 2.65</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 2.05 / 34.90 ± 1.27</td> <!-- ScaLA-nn -->
   <td class="no rc">44.70 ± 3.79 / 67.06 ± 2.85</td> <!-- NorQuAD -->
   <td class="sv ner">45.55 ± 2.18 / 26.78 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">70.71 ± 1.99 / 71.19 ± 1.14</td> <!-- SweReC -->
   <td class="sv la">4.83 ± 3.48 / 36.64 ± 2.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.25 ± 1.21 / 61.21 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">38.15 ± 2.30 / 28.10 ± 4.65</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.98 ± 1.44 / 35.86 ± 1.12</td> <!-- ScaLA-is -->
   <td class="is rc">20.39 ± 3.04 / 44.20 ± 2.72</td> <!-- NQiI -->
   <td class="de ner">48.20 ± 1.57 / 39.04 ± 2.38</td> <!-- GermEval -->
   <td class="de sent">47.12 ± 4.20 / 59.69 ± 4.45</td> <!-- SB10k -->
   <td class="de la">12.39 ± 1.39 / 45.13 ± 3.93</td> <!-- ScaLA-de -->
   <td class="de rc">30.50 ± 3.67 / 57.48 ± 4.51</td> <!-- GermanQuAD -->
   <td class="nl ner">51.18 ± 1.62 / 35.45 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.23 ± 2.84 / 19.38 ± 4.37</td> <!-- Dutch Social -->
   <td class="nl la">1.99 ± 2.56 / 34.69 ± 1.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.66 ± 1.25 / 65.31 ± 1.06</td> <!-- SQuAD-nl -->
   <td class="en ner">55.51 ± 1.48 / 50.61 ± 1.37</td> <!-- CoNLL-en -->
   <td class="en sent">68.74 ± 0.81 / 58.25 ± 0.31</td> <!-- SST5 -->
   <td class="en la">40.81 ± 3.66 / 69.94 ± 1.98</td> <!-- ScaLA-en -->
   <td class="en rc">72.33 ± 2.68 / 84.50 ± 1.61</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="da-rank">2.56</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.53</td> <!-- Swedish rank -->
   <td class="is-rank">3.79</td> <!-- Icelandic rank -->
   <td class="de-rank">2.59</td> <!-- German rank -->
   <td class="nl-rank">3.15</td> <!-- Dutch rank -->
   <td class="en-rank">2.01</td> <!-- English rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da rc">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no rc">33.77 ± 2.11 / 61.99 ± 2.34</td> <!-- NorQuAD -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="de ner">50.09 ± 1.33 / 38.59 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">46.52 ± 2.85 / 63.64 ± 2.10</td> <!-- SB10k -->
   <td class="de la">15.23 ± 1.71 / 55.08 ± 1.88</td> <!-- ScaLA-de -->
   <td class="de rc">25.54 ± 3.58 / 56.07 ± 3.76</td> <!-- GermanQuAD -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en rc">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="da-rank">2.81</td> <!-- Danish rank -->
   <td class="no-rank">2.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.82</td> <!-- Swedish rank -->
   <td class="is-rank">3.54</td> <!-- Icelandic rank -->
   <td class="de-rank">2.92</td> <!-- German rank -->
   <td class="nl-rank">3.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.90</td> <!-- English rank -->
   <td class="da ner">43.83 ± 1.93 / 34.03 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">29.21 ± 1.92 / 52.86 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">12.96 ± 1.67 / 55.83 ± 0.88</td> <!-- ScaLA-da -->
   <td class="da rc">49.76 ± 0.59 / 56.52 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="no ner">59.77 ± 2.77 / 56.12 ± 2.72</td> <!-- NorNE-nb -->
   <td class="no ner">60.98 ± 2.01 / 57.99 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">28.14 ± 1.90 / 49.76 ± 1.59</td> <!-- NoReC -->
   <td class="no la">14.01 ± 2.15 / 56.43 ± 1.08</td> <!-- ScaLA-nb -->
   <td class="no la">10.15 ± 1.06 / 54.56 ± 0.71</td> <!-- ScaLA-nn -->
   <td class="no rc">51.08 ± 2.83 / 74.34 ± 1.55</td> <!-- NorQuAD -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td class="is ner">37.69 ± 3.97 / 34.52 ± 3.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.11 ± 1.49 / 48.48 ± 2.77</td> <!-- ScaLA-is -->
   <td class="is rc">18.34 ± 2.07 / 43.26 ± 1.28</td> <!-- NQiI -->
   <td class="de ner">54.20 ± 1.00 / 48.58 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">15.43 ± 3.70 / 43.11 ± 2.77</td> <!-- SB10k -->
   <td class="de la">17.49 ± 1.23 / 57.46 ± 1.12</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 5.36 / 60.07 ± 4.46</td> <!-- GermanQuAD -->
   <td class="nl ner">53.93 ± 2.71 / 47.48 ± 2.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.83 ± 2.37 / 34.00 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">6.58 ± 3.36 / 48.51 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.45 ± 2.52 / 67.47 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="en ner">66.70 ± 0.99 / 61.08 ± 1.16</td> <!-- CoNLL-en -->
   <td class="en sent">55.62 ± 2.54 / 64.98 ± 2.03</td> <!-- SST5 -->
   <td class="en la">31.36 ± 2.63 / 65.21 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">72.58 ± 0.68 / 84.67 ± 0.91</td> <!-- SQuAD -->
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
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.0</td> <!-- SST5 version -->
   <td>12.10.0</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="da-rank">2.65</td> <!-- Danish rank -->
   <td class="no-rank">3.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.59</td> <!-- Swedish rank -->
   <td class="is-rank">3.96</td> <!-- Icelandic rank -->
   <td class="de-rank">2.65</td> <!-- German rank -->
   <td class="nl-rank">3.10</td> <!-- Dutch rank -->
   <td class="en-rank">1.98</td> <!-- English rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da rc">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">44.83 ± 1.58 / 40.11 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 1.65 / 41.63 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.59 / 45.73 ± 2.82</td> <!-- NoReC -->
   <td class="no la">3.57 ± 1.55 / 37.05 ± 2.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.61 ± 2.11 / 37.85 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no rc">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is rc">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="de ner">42.08 ± 1.65 / 36.90 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td class="nl ner">42.52 ± 2.25 / 37.46 ± 3.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="en ner">58.56 ± 1.99 / 54.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en rc">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="da-rank">3.15</td> <!-- Danish rank -->
   <td class="no-rank">3.04</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.76</td> <!-- Swedish rank -->
   <td class="is-rank">3.86</td> <!-- Icelandic rank -->
   <td class="de-rank">2.15</td> <!-- German rank -->
   <td class="nl-rank">3.09</td> <!-- Dutch rank -->
   <td class="en-rank">2.06</td> <!-- English rank -->
   <td class="da ner">4.51 ± 2.12 / 3.71 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">40.85 ± 1.26 / 59.79 ± 1.32</td> <!-- Angry Tweets -->
   <td class="da la">5.43 ± 1.74 / 46.21 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da rc">51.76 ± 0.73 / 58.44 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="no ner">52.18 ± 2.03 / 29.83 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">50.53 ± 1.49 / 31.94 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">33.30 ± 2.01 / 51.15 ± 2.93</td> <!-- NoReC -->
   <td class="no la">2.63 ± 2.56 / 40.21 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">4.00 ± 1.87 / 44.87 ± 3.17</td> <!-- ScaLA-nn -->
   <td class="no rc">37.08 ± 2.44 / 61.14 ± 2.01</td> <!-- NorQuAD -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="is ner">27.22 ± 3.65 / 24.21 ± 2.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.31 ± 1.28 / 39.67 ± 4.39</td> <!-- ScaLA-is -->
   <td class="is rc">17.24 ± 2.72 / 41.15 ± 1.57</td> <!-- NQiI -->
   <td class="de ner">55.36 ± 0.81 / 36.14 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">53.05 ± 2.34 / 65.57 ± 1.92</td> <!-- SB10k -->
   <td class="de la">23.08 ± 1.54 / 58.65 ± 2.04</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 1.09 / 62.02 ± 2.17</td> <!-- GermanQuAD -->
   <td class="nl ner">44.27 ± 2.14 / 34.47 ± 2.48</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.84 ± 1.82 / 36.64 ± 1.13</td> <!-- Dutch Social -->
   <td class="nl la">10.44 ± 1.58 / 48.93 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.40 ± 1.14 / 68.02 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="en ner">64.09 ± 0.96 / 49.92 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">46.77 ± 4.36 / 60.99 ± 2.15</td> <!-- SST5 -->
   <td class="en la">31.62 ± 2.25 / 63.73 ± 1.79</td> <!-- ScaLA-en -->
   <td class="en rc">71.25 ± 0.83 / 85.72 ± 0.57</td> <!-- SQuAD -->
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
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da-rank">2.94</td> <!-- Danish rank -->
   <td class="no-rank">3.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
   <td class="is-rank">3.74</td> <!-- Icelandic rank -->
   <td class="de-rank">2.72</td> <!-- German rank -->
   <td class="nl-rank">3.37</td> <!-- Dutch rank -->
   <td class="en-rank">2.34</td> <!-- English rank -->
   <td class="da ner">33.80 ± 2.66 / 25.32 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">31.57 ± 2.65 / 46.48 ± 3.84</td> <!-- Angry Tweets -->
   <td class="da la">2.76 ± 1.76 / 44.96 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da rc">54.20 ± 1.63 / 59.50 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="no ner">42.78 ± 1.09 / 37.34 ± 1.81</td> <!-- NorNE-nb -->
   <td class="no ner">42.85 ± 1.93 / 37.34 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">36.68 ± 2.11 / 46.78 ± 2.71</td> <!-- NoReC -->
   <td class="no la">2.39 ± 1.54 / 43.99 ± 3.66</td> <!-- ScaLA-nb -->
   <td class="no la">1.91 ± 1.37 / 44.20 ± 4.28</td> <!-- ScaLA-nn -->
   <td class="no rc">39.16 ± 2.56 / 62.28 ± 2.34</td> <!-- NorQuAD -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="is ner">27.44 ± 3.28 / 23.50 ± 3.29</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.46 ± 1.18 / 41.20 ± 3.25</td> <!-- ScaLA-is -->
   <td class="is rc">17.26 ± 3.80 / 39.06 ± 3.00</td> <!-- NQiI -->
   <td class="de ner">39.41 ± 2.30 / 36.17 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">49.42 ± 4.33 / 61.57 ± 5.43</td> <!-- SB10k -->
   <td class="de la">6.02 ± 2.53 / 46.41 ± 4.35</td> <!-- ScaLA-de -->
   <td class="de rc">27.69 ± 4.39 / 54.92 ± 5.38</td> <!-- GermanQuAD -->
   <td class="nl ner">46.95 ± 2.32 / 36.13 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.34 ± 2.10 / 19.37 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">3.46 ± 1.91 / 41.32 ± 3.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.07 ± 0.89 / 68.14 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="en ner">41.02 ± 3.86 / 40.03 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">66.43 ± 0.78 / 57.25 ± 0.33</td> <!-- SST5 -->
   <td class="en la">5.17 ± 1.55 / 37.03 ± 2.40</td> <!-- ScaLA-en -->
   <td class="en rc">76.04 ± 0.97 / 85.31 ± 0.82</td> <!-- SQuAD -->
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
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="da-rank">2.92</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="is-rank">3.34</td> <!-- Icelandic rank -->
   <td class="de-rank">3.25</td> <!-- German rank -->
   <td class="nl-rank">3.31</td> <!-- Dutch rank -->
   <td class="en-rank">2.40</td> <!-- English rank -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.23 ± 3.43 / 41.05 ± 4.38</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da rc">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.50 ± 1.29 / 42.21 ± 1.39</td> <!-- NoReC -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no rc">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">79.20 ± 1.03 / 79.87 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="is ner">27.54 ± 3.01 / 23.54 ± 2.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.61 ± 1.64 / 41.57 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is rc">28.12 ± 3.77 / 54.61 ± 3.42</td> <!-- NQiI -->
   <td class="de ner">36.17 ± 2.52 / 27.29 ± 1.74</td> <!-- GermEval -->
   <td class="de sent">34.17 ± 7.08 / 46.97 ± 8.28</td> <!-- SB10k -->
   <td class="de la">2.21 ± 1.64 / 38.29 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 3.04 / 30.89 ± 4.33</td> <!-- GermanQuAD -->
   <td class="nl ner">35.30 ± 3.76 / 33.68 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.67 ± 2.21 / 31.30 ± 4.51</td> <!-- Dutch Social -->
   <td class="nl la">1.76 ± 2.37 / 47.60 ± 1.68</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.05 ± 1.68 / 55.38 ± 1.66</td> <!-- SQuAD-nl -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en rc">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="da-rank">2.87</td> <!-- Danish rank -->
   <td class="no-rank">3.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.46</td> <!-- Swedish rank -->
   <td class="is-rank">3.85</td> <!-- Icelandic rank -->
   <td class="de-rank">2.96</td> <!-- German rank -->
   <td class="nl-rank">3.16</td> <!-- Dutch rank -->
   <td class="en-rank">2.23</td> <!-- English rank -->
   <td class="da ner">38.62 ± 3.40 / 27.71 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">35.47 ± 1.35 / 52.70 ± 2.05</td> <!-- Angry Tweets -->
   <td class="da la">5.07 ± 1.76 / 43.91 ± 4.86</td> <!-- ScaLA-da -->
   <td class="da rc">45.21 ± 0.84 / 50.96 ± 0.94</td> <!-- ScandiQA-da -->
   <td class="no ner">53.93 ± 3.93 / 48.95 ± 4.17</td> <!-- NorNE-nb -->
   <td class="no ner">54.04 ± 1.83 / 49.74 ± 2.48</td> <!-- NorNE-nn -->
   <td class="no sent">23.83 ± 3.47 / 45.39 ± 3.46</td> <!-- NoReC -->
   <td class="no la">3.91 ± 1.46 / 42.54 ± 4.53</td> <!-- ScaLA-nb -->
   <td class="no la">1.55 ± 2.39 / 40.63 ± 4.26</td> <!-- ScaLA-nn -->
   <td class="no rc">2.37 ± 0.20 / 12.14 ± 1.07</td> <!-- NorQuAD -->
   <td class="sv ner">51.76 ± 4.53 / 41.73 ± 6.65</td> <!-- SUC3 -->
   <td class="sv sent">70.61 ± 1.12 / 60.47 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">6.24 ± 3.11 / 46.34 ± 5.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.67 ± 1.34 / 50.56 ± 1.33</td> <!-- ScandiQA-sv -->
   <td class="is ner">38.52 ± 3.25 / 28.84 ± 5.49</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.94 ± 2.60 / 36.06 ± 2.17</td> <!-- NQiI -->
   <td class="de ner">49.38 ± 2.20 / 42.66 ± 3.24</td> <!-- GermEval -->
   <td class="de sent">41.72 ± 4.07 / 60.45 ± 3.07</td> <!-- SB10k -->
   <td class="de la">7.67 ± 1.52 / 46.66 ± 3.23</td> <!-- ScaLA-de -->
   <td class="de rc">13.70 ± 2.43 / 30.21 ± 3.80</td> <!-- GermanQuAD -->
   <td class="nl ner">50.88 ± 3.41 / 39.51 ± 3.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.39 ± 1.50 / 30.05 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">3.31 ± 1.19 / 37.97 ± 4.40</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.44 ± 1.06 / 58.85 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="en ner">60.64 ± 2.11 / 55.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">61.20 ± 1.16 / 61.92 ± 1.68</td> <!-- SST5 -->
   <td class="en la">7.63 ± 2.79 / 46.39 ± 3.79</td> <!-- ScaLA-en -->
   <td class="en rc">69.83 ± 2.12 / 80.15 ± 1.27</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="da-rank">3.39</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.37</td> <!-- Swedish rank -->
   <td class="is-rank">4.23</td> <!-- Icelandic rank -->
   <td class="de-rank">3.03</td> <!-- German rank -->
   <td class="nl-rank">3.31</td> <!-- Dutch rank -->
   <td class="en-rank">1.93</td> <!-- English rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da rc">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no rc">40.28 ± 3.58 / 62.78 ± 3.34</td> <!-- NorQuAD -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.95 ± 0.86 / 60.77 ± 0.75</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">16.91 ± 2.57 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 2.45 / 67.63 ± 1.87</td> <!-- SB10k -->
   <td class="de la">7.33 ± 2.53 / 37.69 ± 2.51</td> <!-- ScaLA-de -->
   <td class="de rc">30.05 ± 1.59 / 57.13 ± 2.48</td> <!-- GermanQuAD -->
   <td class="nl ner">46.34 ± 2.00 / 33.30 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.96 ± 1.44 / 18.10 ± 2.39</td> <!-- Dutch Social -->
   <td class="nl la">0.88 ± 1.23 / 33.53 ± 0.48</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.33 ± 1.28 / 66.50 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en rc">75.89 ± 1.84 / 85.86 ± 1.03</td> <!-- SQuAD -->
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
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.0</td> <!-- Dutch Social version -->
   <td>10.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.0</td> <!-- SST5 version -->
   <td>10.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.08</td> <!-- Danish rank -->
   <td class="no-rank">3.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.69</td> <!-- Swedish rank -->
   <td class="is-rank">3.75</td> <!-- Icelandic rank -->
   <td class="de-rank">3.07</td> <!-- German rank -->
   <td class="nl-rank">2.76</td> <!-- Dutch rank -->
   <td class="en-rank">2.86</td> <!-- English rank -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da rc">13.97 ± 1.75 / 19.76 ± 2.26</td> <!-- ScandiQA-da -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.36 ± 1.18 / 63.94 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
   <td class="is ner">63.36 ± 0.96 / 65.24 ± 0.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.02 ± 0.94 / 47.05 ± 2.13</td> <!-- ScaLA-is -->
   <td class="is rc">6.48 ± 0.37 / 27.44 ± 0.44</td> <!-- NQiI -->
   <td class="de ner">64.12 ± 0.92 / 62.50 ± 0.85</td> <!-- GermEval -->
   <td class="de sent">49.66 ± 1.68 / 66.33 ± 1.12</td> <!-- SB10k -->
   <td class="de la">0.58 ± 1.23 / 49.27 ± 0.86</td> <!-- ScaLA-de -->
   <td class="de rc">0.05 ± 0.06 / 0.36 ± 0.30</td> <!-- GermanQuAD -->
   <td class="nl ner">67.89 ± 1.61 / 74.48 ± 1.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">23.25 ± 6.95 / 44.88 ± 6.27</td> <!-- Dutch Social -->
   <td class="nl la">21.36 ± 7.80 / 59.50 ± 3.54</td> <!-- ScaLA-nl -->
   <td class="nl rc">4.50 ± 0.39 / 9.94 ± 0.33</td> <!-- SQuAD-nl -->
   <td class="en ner">81.71 ± 0.66 / 82.33 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">50.69 ± 1.19 / 50.90 ± 0.50</td> <!-- SST5 -->
   <td class="en la">2.16 ± 1.58 / 49.99 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en rc">4.19 ± 0.69 / 11.99 ± 0.62</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.10</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.80</td> <!-- Swedish rank -->
   <td class="is-rank">3.72</td> <!-- Icelandic rank -->
   <td class="de-rank">3.24</td> <!-- German rank -->
   <td class="nl-rank">3.31</td> <!-- Dutch rank -->
   <td class="en-rank">2.37</td> <!-- English rank -->
   <td class="da ner">15.94 ± 1.59 / 14.05 ± 1.45</td> <!-- DANSK -->
   <td class="da sent">32.78 ± 4.04 / 47.79 ± 5.25</td> <!-- Angry Tweets -->
   <td class="da la">7.86 ± 1.87 / 41.91 ± 2.25</td> <!-- ScaLA-da -->
   <td class="da rc">52.16 ± 0.84 / 60.27 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">23.95 ± 1.93 / 21.43 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">26.55 ± 1.50 / 25.06 ± 1.61</td> <!-- NorNE-nn -->
   <td class="no sent">40.89 ± 3.60 / 59.86 ± 3.59</td> <!-- NoReC -->
   <td class="no la">9.45 ± 1.58 / 44.62 ± 3.29</td> <!-- ScaLA-nb -->
   <td class="no la">8.32 ± 1.89 / 42.30 ± 2.78</td> <!-- ScaLA-nn -->
   <td class="no rc">43.19 ± 1.82 / 67.93 ± 1.55</td> <!-- NorQuAD -->
   <td class="sv ner">15.70 ± 1.54 / 14.65 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">68.23 ± 3.81 / 71.17 ± 3.07</td> <!-- SweReC -->
   <td class="sv la">12.39 ± 1.39 / 50.99 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.04 ± 0.97 / 60.86 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="is ner">21.20 ± 1.45 / 19.22 ± 1.47</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.95 ± 1.01 / 35.16 ± 0.86</td> <!-- ScaLA-is -->
   <td class="is rc">24.95 ± 3.00 / 53.88 ± 1.93</td> <!-- NQiI -->
   <td class="de ner">24.35 ± 1.72 / 21.90 ± 0.85</td> <!-- GermEval -->
   <td class="de sent">43.35 ± 3.81 / 60.49 ± 3.18</td> <!-- SB10k -->
   <td class="de la">2.38 ± 1.21 / 37.27 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">15.56 ± 2.24 / 34.68 ± 3.15</td> <!-- GermanQuAD -->
   <td class="nl ner">24.44 ± 1.62 / 25.02 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.40 ± 2.14 / 40.21 ± 2.51</td> <!-- Dutch Social -->
   <td class="nl la">4.85 ± 2.01 / 49.10 ± 2.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">39.83 ± 1.08 / 52.69 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="en ner">39.21 ± 1.52 / 34.08 ± 1.88</td> <!-- CoNLL-en -->
   <td class="en sent">65.58 ± 1.59 / 57.86 ± 1.13</td> <!-- SST5 -->
   <td class="en la">7.82 ± 1.43 / 51.19 ± 1.75</td> <!-- ScaLA-en -->
   <td class="en rc">72.25 ± 2.19 / 83.08 ± 1.30</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.49</td> <!-- Swedish rank -->
   <td class="is-rank">3.56</td> <!-- Icelandic rank -->
   <td class="de-rank">3.22</td> <!-- German rank -->
   <td class="nl-rank">3.63</td> <!-- Dutch rank -->
   <td class="en-rank">2.60</td> <!-- English rank -->
   <td class="da ner">28.60 ± 4.69 / 20.29 ± 3.37</td> <!-- DANSK -->
   <td class="da sent">48.71 ± 1.27 / 60.90 ± 2.95</td> <!-- Angry Tweets -->
   <td class="da la">2.30 ± 1.34 / 37.21 ± 2.50</td> <!-- ScaLA-da -->
   <td class="da rc">53.85 ± 1.73 / 58.96 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="no ner">26.76 ± 6.99 / 23.69 ± 3.73</td> <!-- NorNE-nb -->
   <td class="no ner">35.38 ± 5.87 / 27.52 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">29.22 ± 2.89 / 39.25 ± 1.86</td> <!-- NoReC -->
   <td class="no la">2.58 ± 2.68 / 36.11 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">2.79 ± 1.44 / 36.17 ± 1.51</td> <!-- ScaLA-nn -->
   <td class="no rc">34.41 ± 3.68 / 53.61 ± 4.28</td> <!-- NorQuAD -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td class="is ner">26.28 ± 5.09 / 22.73 ± 3.35</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.17 ± 1.98 / 48.03 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">22.65 ± 3.50 / 45.48 ± 2.99</td> <!-- NQiI -->
   <td class="de ner">34.53 ± 1.24 / 29.89 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">42.90 ± 2.66 / 56.64 ± 4.71</td> <!-- SB10k -->
   <td class="de la">1.51 ± 1.64 / 43.36 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">15.83 ± 1.42 / 29.77 ± 2.54</td> <!-- GermanQuAD -->
   <td class="nl ner">36.74 ± 3.36 / 32.36 ± 1.39</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 2.44 / 34.17 ± 2.59</td> <!-- Dutch Social -->
   <td class="nl la">3.01 ± 1.94 / 46.03 ± 4.19</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.32 ± 1.55 / 40.73 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="en ner">42.78 ± 4.24 / 40.64 ± 2.84</td> <!-- CoNLL-en -->
   <td class="en sent">59.90 ± 4.98 / 54.05 ± 2.70</td> <!-- SST5 -->
   <td class="en la">5.68 ± 1.91 / 50.82 ± 2.18</td> <!-- ScaLA-en -->
   <td class="en rc">58.52 ± 1.88 / 68.97 ± 1.86</td> <!-- SQuAD -->
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
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="da-rank">2.92</td> <!-- Danish rank -->
   <td class="no-rank">3.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.55</td> <!-- Swedish rank -->
   <td class="is-rank">4.20</td> <!-- Icelandic rank -->
   <td class="de-rank">2.86</td> <!-- German rank -->
   <td class="nl-rank">3.53</td> <!-- Dutch rank -->
   <td class="en-rank">2.31</td> <!-- English rank -->
   <td class="da ner">28.45 ± 1.61 / 22.90 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">39.09 ± 1.15 / 45.25 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.26 / 37.98 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da rc">51.67 ± 2.31 / 57.34 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="no ner">41.64 ± 3.64 / 39.43 ± 3.55</td> <!-- NorNE-nb -->
   <td class="no ner">42.37 ± 3.13 / 40.79 ± 3.10</td> <!-- NorNE-nn -->
   <td class="no sent">33.71 ± 2.57 / 55.00 ± 1.41</td> <!-- NoReC -->
   <td class="no la">-0.19 ± 0.77 / 33.29 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.25 / 34.51 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no rc">30.14 ± 2.44 / 50.96 ± 3.46</td> <!-- NorQuAD -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td class="is ner">32.19 ± 2.52 / 32.88 ± 2.18</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.37 ± 1.64 / 33.39 ± 0.55</td> <!-- ScaLA-is -->
   <td class="is rc">6.58 ± 2.15 / 27.03 ± 2.89</td> <!-- NQiI -->
   <td class="de ner">34.81 ± 2.51 / 30.33 ± 2.95</td> <!-- GermEval -->
   <td class="de sent">51.01 ± 2.18 / 65.35 ± 2.23</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.40 ± 3.91 / 49.38 ± 4.65</td> <!-- GermanQuAD -->
   <td class="nl ner">36.58 ± 3.88 / 33.82 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.32 ± 1.30 / 24.04 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">4.01 ± 2.01 / 36.03 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.81 ± 0.81 / 63.87 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="en ner">47.50 ± 1.70 / 41.85 ± 1.68</td> <!-- CoNLL-en -->
   <td class="en sent">64.69 ± 1.33 / 57.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">8.01 ± 1.97 / 51.78 ± 1.65</td> <!-- ScaLA-en -->
   <td class="en rc">71.81 ± 1.05 / 80.90 ± 0.72</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.8</td> <!-- ScaLA-is version -->
   <td>12.10.8</td> <!-- NQiI version -->
   <td>12.10.8</td> <!-- GermEval version -->
   <td>12.10.8</td> <!-- SB10k version -->
   <td>12.10.8</td> <!-- ScaLA-de version -->
   <td>12.10.8</td> <!-- GermanQuAD version -->
   <td>12.10.8</td> <!-- CoNLL-nl version -->
   <td>12.10.8</td> <!-- Dutch Social version -->
   <td>12.10.8</td> <!-- ScaLA-nl version -->
   <td>12.10.8</td> <!-- SQuAD-nl version -->
   <td>12.10.8</td> <!-- CoNLL-en version -->
   <td>12.10.8</td> <!-- SST5 version -->
   <td>12.10.8</td> <!-- ScaLA-en version -->
   <td>12.10.8</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="da-rank">2.75</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.47</td> <!-- Swedish rank -->
   <td class="is-rank">4.07</td> <!-- Icelandic rank -->
   <td class="de-rank">2.98</td> <!-- German rank -->
   <td class="nl-rank">3.39</td> <!-- Dutch rank -->
   <td class="en-rank">1.98</td> <!-- English rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da rc">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="no ner">32.12 ± 5.17 / 32.01 ± 2.80</td> <!-- NorNE-nb -->
   <td class="no ner">36.86 ± 3.53 / 35.46 ± 3.07</td> <!-- NorNE-nn -->
   <td class="no sent">36.97 ± 1.94 / 55.08 ± 2.30</td> <!-- NoReC -->
   <td class="no la">5.27 ± 3.31 / 40.91 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">1.40 ± 1.87 / 33.64 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no rc">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="de ner">31.52 ± 2.96 / 29.20 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de rc">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td class="nl ner">35.74 ± 3.22 / 31.74 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="en ner">55.45 ± 1.61 / 49.72 ± 1.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en rc">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">2.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.44</td> <!-- Swedish rank -->
   <td class="is-rank">4.08</td> <!-- Icelandic rank -->
   <td class="de-rank">3.20</td> <!-- German rank -->
   <td class="nl-rank">3.77</td> <!-- Dutch rank -->
   <td class="en-rank">2.75</td> <!-- English rank -->
   <td class="da ner">21.47 ± 3.87 / 16.98 ± 3.19</td> <!-- DANSK -->
   <td class="da sent">48.39 ± 0.66 / 64.51 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">12.46 ± 2.22 / 52.33 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">52.51 ± 1.57 / 58.49 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="no ner">21.09 ± 6.44 / 20.45 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">26.31 ± 4.64 / 26.42 ± 2.98</td> <!-- NorNE-nn -->
   <td class="no sent">49.00 ± 3.88 / 65.98 ± 2.95</td> <!-- NoReC -->
   <td class="no la">7.15 ± 2.14 / 40.83 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">7.98 ± 2.64 / 45.21 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no rc">47.70 ± 5.32 / 68.04 ± 5.37</td> <!-- NorQuAD -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">21.40 ± 2.86 / 19.64 ± 2.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.99 ± 1.30 / 35.84 ± 1.02</td> <!-- ScaLA-is -->
   <td class="is rc">13.84 ± 2.99 / 36.90 ± 2.08</td> <!-- NQiI -->
   <td class="de ner">19.29 ± 5.77 / 20.20 ± 3.59</td> <!-- GermEval -->
   <td class="de sent">43.88 ± 3.42 / 61.04 ± 2.69</td> <!-- SB10k -->
   <td class="de la">5.63 ± 1.32 / 49.95 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">17.02 ± 2.10 / 36.47 ± 2.53</td> <!-- GermanQuAD -->
   <td class="nl ner">24.15 ± 5.73 / 26.49 ± 4.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.31 ± 1.56 / 20.06 ± 1.06</td> <!-- Dutch Social -->
   <td class="nl la">1.60 ± 1.71 / 41.51 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.08 ± 1.76 / 49.32 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="en ner">35.84 ± 5.12 / 35.76 ± 4.29</td> <!-- CoNLL-en -->
   <td class="en sent">56.87 ± 8.16 / 59.62 ± 5.61</td> <!-- SST5 -->
   <td class="en la">3.08 ± 2.98 / 40.66 ± 4.63</td> <!-- ScaLA-en -->
   <td class="en rc">52.77 ± 1.53 / 66.64 ± 1.58</td> <!-- SQuAD -->
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
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da-rank">3.08</td> <!-- Danish rank -->
   <td class="no-rank">3.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.69</td> <!-- Swedish rank -->
   <td class="is-rank">3.80</td> <!-- Icelandic rank -->
   <td class="de-rank">3.08</td> <!-- German rank -->
   <td class="nl-rank">3.34</td> <!-- Dutch rank -->
   <td class="en-rank">2.86</td> <!-- English rank -->
   <td class="da ner">54.48 ± 2.16 / 52.85 ± 2.28</td> <!-- DANSK -->
   <td class="da sent">36.60 ± 1.60 / 56.93 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">8.84 ± 5.33 / 51.76 ± 3.80</td> <!-- ScaLA-da -->
   <td class="da rc">15.42 ± 1.70 / 21.36 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">77.81 ± 0.76 / 74.83 ± 0.79</td> <!-- NorNE-nb -->
   <td class="no ner">72.22 ± 0.95 / 68.32 ± 1.13</td> <!-- NorNE-nn -->
   <td class="no sent">44.59 ± 1.89 / 59.87 ± 1.84</td> <!-- NoReC -->
   <td class="no la">8.98 ± 3.55 / 52.49 ± 2.08</td> <!-- ScaLA-nb -->
   <td class="no la">5.72 ± 3.29 / 50.40 ± 3.21</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.33 ± 1.03 / 64.03 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
   <td class="is ner">59.15 ± 1.28 / 61.27 ± 1.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.80 ± 1.69 / 45.59 ± 3.23</td> <!-- ScaLA-is -->
   <td class="is rc">6.14 ± 0.74 / 28.02 ± 0.58</td> <!-- NQiI -->
   <td class="de ner">63.78 ± 0.75 / 62.34 ± 0.64</td> <!-- GermEval -->
   <td class="de sent">49.69 ± 1.56 / 66.32 ± 1.07</td> <!-- SB10k -->
   <td class="de la">0.74 ± 0.83 / 48.97 ± 0.85</td> <!-- ScaLA-de -->
   <td class="de rc">0.02 ± 0.02 / 0.20 ± 0.17</td> <!-- GermanQuAD -->
   <td class="nl ner">65.04 ± 1.07 / 70.94 ± 0.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.40 ± 6.56 / 39.25 ± 6.11</td> <!-- Dutch Social -->
   <td class="nl la">-0.95 ± 1.35 / 49.00 ± 0.64</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.94 ± 0.39 / 9.50 ± 0.40</td> <!-- SQuAD-nl -->
   <td class="en ner">81.71 ± 0.66 / 82.33 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">50.69 ± 1.19 / 50.90 ± 0.50</td> <!-- SST5 -->
   <td class="en la">2.16 ± 1.58 / 49.99 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en rc">4.16 ± 0.71 / 11.93 ± 0.61</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">2.91</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
   <td class="is-rank">3.85</td> <!-- Icelandic rank -->
   <td class="de-rank">3.02</td> <!-- German rank -->
   <td class="nl-rank">4.11</td> <!-- Dutch rank -->
   <td class="en-rank">2.92</td> <!-- English rank -->
   <td class="da ner">56.75 ± 1.91 / 53.43 ± 1.87</td> <!-- DANSK -->
   <td class="da sent">44.48 ± 1.32 / 63.11 ± 0.83</td> <!-- Angry Tweets -->
   <td class="da la">26.74 ± 1.94 / 62.19 ± 1.84</td> <!-- ScaLA-da -->
   <td class="da rc">17.89 ± 1.00 / 25.53 ± 1.05</td> <!-- ScandiQA-da -->
   <td class="no ner">78.31 ± 1.22 / 74.65 ± 1.36</td> <!-- NorNE-nb -->
   <td class="no ner">72.13 ± 0.90 / 67.28 ± 1.09</td> <!-- NorNE-nn -->
   <td class="no sent">47.53 ± 0.94 / 62.73 ± 1.07</td> <!-- NoReC -->
   <td class="no la">26.92 ± 3.12 / 61.93 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.63 ± 4.00 / 56.24 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">66.50 ± 1.49 / 59.99 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">72.19 ± 0.71 / 67.88 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">28.75 ± 5.58 / 63.30 ± 2.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">15.91 ± 0.87 / 23.08 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="is ner">62.44 ± 1.07 / 64.98 ± 0.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.91 ± 1.14 / 46.54 ± 2.46</td> <!-- ScaLA-is -->
   <td class="is rc">3.69 ± 0.48 / 27.48 ± 0.49</td> <!-- NQiI -->
   <td class="de ner">60.54 ± 1.96 / 59.68 ± 1.94</td> <!-- GermEval -->
   <td class="de sent">54.99 ± 2.05 / 70.00 ± 1.37</td> <!-- SB10k -->
   <td class="de la">0.52 ± 2.01 / 49.40 ± 1.06</td> <!-- ScaLA-de -->
   <td class="de rc">0.80 ± 0.23 / 7.76 ± 2.10</td> <!-- GermanQuAD -->
   <td class="nl ner">59.61 ± 2.40 / 67.02 ± 1.16</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 24.33 ± 0.14</td> <!-- Dutch Social -->
   <td class="nl la">-0.04 ± 1.84 / 48.65 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.28 ± 0.31 / 9.04 ± 0.28</td> <!-- SQuAD-nl -->
   <td class="en ner">77.50 ± 0.54 / 78.82 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">53.10 ± 1.18 / 51.88 ± 0.50</td> <!-- SST5 -->
   <td class="en la">-0.35 ± 1.84 / 48.74 ± 1.43</td> <!-- ScaLA-en -->
   <td class="en rc">3.13 ± 0.27 / 9.98 ± 0.25</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">3.24</td> <!-- Danish rank -->
   <td class="no-rank">3.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.37</td> <!-- Swedish rank -->
   <td class="is-rank">3.94</td> <!-- Icelandic rank -->
   <td class="de-rank">2.91</td> <!-- German rank -->
   <td class="nl-rank">3.54</td> <!-- Dutch rank -->
   <td class="en-rank">2.94</td> <!-- English rank -->
   <td class="da ner">47.61 ± 1.71 / 45.91 ± 1.91</td> <!-- DANSK -->
   <td class="da sent">24.17 ± 1.92 / 43.75 ± 2.75</td> <!-- Angry Tweets -->
   <td class="da la">8.14 ± 3.76 / 51.78 ± 1.81</td> <!-- ScaLA-da -->
   <td class="da rc">25.19 ± 1.29 / 30.51 ± 1.06</td> <!-- ScandiQA-da -->
   <td class="no ner">68.63 ± 1.64 / 64.83 ± 1.55</td> <!-- NorNE-nb -->
   <td class="no ner">67.70 ± 2.68 / 63.70 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">25.68 ± 2.17 / 41.65 ± 2.77</td> <!-- NoReC -->
   <td class="no la">6.73 ± 5.40 / 48.20 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">3.35 ± 2.61 / 47.52 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no rc">22.57 ± 1.57 / 34.64 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">68.83 ± 1.00 / 63.29 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">64.25 ± 1.66 / 63.62 ± 2.92</td> <!-- SweReC -->
   <td class="sv la">28.62 ± 9.43 / 59.33 ± 5.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.78 ± 2.01 / 34.26 ± 2.03</td> <!-- ScandiQA-sv -->
   <td class="is ner">56.62 ± 0.57 / 59.34 ± 0.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.21 ± 1.45 / 47.43 ± 1.67</td> <!-- ScaLA-is -->
   <td class="is rc">6.01 ± 0.45 / 29.08 ± 1.30</td> <!-- NQiI -->
   <td class="de ner">65.35 ± 1.08 / 63.62 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">37.77 ± 2.20 / 58.20 ± 1.43</td> <!-- SB10k -->
   <td class="de la">16.07 ± 3.83 / 54.09 ± 2.44</td> <!-- ScaLA-de -->
   <td class="de rc">5.67 ± 1.14 / 16.63 ± 2.52</td> <!-- GermanQuAD -->
   <td class="nl ner">56.69 ± 1.80 / 68.42 ± 0.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.29 ± 3.04 / 30.73 ± 2.40</td> <!-- Dutch Social -->
   <td class="nl la">3.02 ± 1.45 / 50.08 ± 1.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.14 ± 1.13 / 31.59 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="en ner">77.64 ± 0.74 / 79.56 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">12.42 ± 9.17 / 33.80 ± 4.31</td> <!-- SST5 -->
   <td class="en la">13.65 ± 6.22 / 53.84 ± 2.20</td> <!-- ScaLA-en -->
   <td class="en rc">33.29 ± 0.96 / 45.71 ± 0.70</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="da-rank">3.09</td> <!-- Danish rank -->
   <td class="no-rank">3.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.65</td> <!-- Swedish rank -->
   <td class="is-rank">4.08</td> <!-- Icelandic rank -->
   <td class="de-rank">2.85</td> <!-- German rank -->
   <td class="nl-rank">3.52</td> <!-- Dutch rank -->
   <td class="en-rank">2.34</td> <!-- English rank -->
   <td class="da ner">24.93 ± 4.36 / 22.23 ± 3.32</td> <!-- DANSK -->
   <td class="da sent">31.65 ± 2.94 / 51.95 ± 2.92</td> <!-- Angry Tweets -->
   <td class="da la">0.06 ± 1.20 / 34.30 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">51.47 ± 1.82 / 57.00 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="no ner">32.21 ± 1.63 / 31.19 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">36.62 ± 1.94 / 36.40 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">16.98 ± 3.42 / 27.01 ± 3.17</td> <!-- NoReC -->
   <td class="no la">1.57 ± 1.20 / 41.68 ± 4.20</td> <!-- ScaLA-nb -->
   <td class="no la">0.97 ± 1.79 / 40.10 ± 4.50</td> <!-- ScaLA-nn -->
   <td class="no rc">26.28 ± 1.51 / 44.62 ± 2.11</td> <!-- NorQuAD -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="is ner">28.06 ± 2.33 / 29.10 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.10 ± 1.11 / 33.70 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">11.07 ± 2.29 / 27.33 ± 1.88</td> <!-- NQiI -->
   <td class="de ner">37.68 ± 1.26 / 33.74 ± 1.78</td> <!-- GermEval -->
   <td class="de sent">46.00 ± 3.63 / 61.88 ± 2.94</td> <!-- SB10k -->
   <td class="de la">0.83 ± 0.84 / 33.38 ± 0.28</td> <!-- ScaLA-de -->
   <td class="de rc">26.65 ± 4.01 / 53.15 ± 4.26</td> <!-- GermanQuAD -->
   <td class="nl ner">37.39 ± 3.37 / 32.77 ± 1.97</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.51 ± 1.57 / 19.22 ± 1.72</td> <!-- Dutch Social -->
   <td class="nl la">3.11 ± 0.88 / 50.54 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.60 ± 1.28 / 61.06 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="en ner">47.76 ± 2.72 / 44.84 ± 2.71</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 0.85 / 65.96 ± 2.20</td> <!-- SST5 -->
   <td class="en la">5.76 ± 1.50 / 50.36 ± 2.34</td> <!-- ScaLA-en -->
   <td class="en rc">70.34 ± 1.81 / 81.54 ± 1.06</td> <!-- SQuAD -->
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
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="da-rank">3.12</td> <!-- Danish rank -->
   <td class="no-rank">3.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.00</td> <!-- Swedish rank -->
   <td class="is-rank">4.16</td> <!-- Icelandic rank -->
   <td class="de-rank">2.89</td> <!-- German rank -->
   <td class="nl-rank">3.18</td> <!-- Dutch rank -->
   <td class="en-rank">2.87</td> <!-- English rank -->
   <td class="da ner">41.09 ± 1.83 / 40.40 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">27.33 ± 1.92 / 49.78 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">21.58 ± 3.92 / 59.41 ± 2.63</td> <!-- ScaLA-da -->
   <td class="da rc">20.68 ± 0.82 / 26.68 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">49.92 ± 0.61 / 49.17 ± 0.71</td> <!-- NorNE-nb -->
   <td class="no ner">44.37 ± 1.15 / 43.43 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">19.81 ± 2.15 / 40.90 ± 2.60</td> <!-- NoReC -->
   <td class="no la">8.64 ± 3.57 / 53.17 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">3.11 ± 1.16 / 50.44 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no rc">15.89 ± 1.29 / 26.33 ± 2.41</td> <!-- NorQuAD -->
   <td class="sv ner">38.36 ± 1.60 / 37.63 ± 1.73</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 1.72 / 56.25 ± 1.72</td> <!-- SweReC -->
   <td class="sv la">19.40 ± 5.65 / 58.63 ± 3.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">19.23 ± 0.59 / 26.64 ± 0.90</td> <!-- ScandiQA-sv -->
   <td class="is ner">29.71 ± 1.94 / 28.69 ± 1.97</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.71 ± 1.10 / 49.68 ± 1.24</td> <!-- ScaLA-is -->
   <td class="is rc">6.50 ± 0.42 / 27.51 ± 0.99</td> <!-- NQiI -->
   <td class="de ner">49.95 ± 0.72 / 49.10 ± 0.71</td> <!-- GermEval -->
   <td class="de sent">40.29 ± 2.70 / 59.76 ± 1.78</td> <!-- SB10k -->
   <td class="de la">25.88 ± 6.61 / 61.54 ± 3.28</td> <!-- ScaLA-de -->
   <td class="de rc">2.59 ± 0.71 / 8.94 ± 2.03</td> <!-- GermanQuAD -->
   <td class="nl ner">49.54 ± 1.42 / 50.44 ± 1.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.86 ± 3.09 / 35.33 ± 1.77</td> <!-- Dutch Social -->
   <td class="nl la">27.90 ± 5.58 / 62.47 ± 3.34</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.65 ± 1.02 / 29.40 ± 1.29</td> <!-- SQuAD-nl -->
   <td class="en ner">71.43 ± 0.88 / 71.51 ± 0.79</td> <!-- CoNLL-en -->
   <td class="en sent">17.53 ± 2.21 / 38.67 ± 1.90</td> <!-- SST5 -->
   <td class="en la">23.93 ± 5.87 / 59.48 ± 3.40</td> <!-- ScaLA-en -->
   <td class="en rc">31.01 ± 0.89 / 42.98 ± 0.49</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.80</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="is-rank">4.42</td> <!-- Icelandic rank -->
   <td class="de-rank">3.43</td> <!-- German rank -->
   <td class="nl-rank">4.05</td> <!-- Dutch rank -->
   <td class="en-rank">2.71</td> <!-- English rank -->
   <td class="da ner">16.72 ± 2.23 / 15.96 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">45.89 ± 2.13 / 63.12 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">11.25 ± 2.33 / 51.88 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da rc">53.17 ± 0.79 / 59.30 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="no ner">31.45 ± 1.64 / 31.64 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">33.85 ± 1.95 / 34.29 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">36.06 ± 3.96 / 52.59 ± 4.67</td> <!-- NoReC -->
   <td class="no la">8.34 ± 2.97 / 45.11 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">6.84 ± 3.88 / 45.28 ± 5.45</td> <!-- ScaLA-nn -->
   <td class="no rc">48.31 ± 4.22 / 69.39 ± 4.10</td> <!-- NorQuAD -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.35 ± 0.70 / 9.74 ± 0.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.14 ± 0.97 / 35.56 ± 2.43</td> <!-- ScaLA-is -->
   <td class="is rc">7.51 ± 3.09 / 30.04 ± 2.02</td> <!-- NQiI -->
   <td class="de ner">25.69 ± 1.43 / 25.95 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">33.48 ± 2.83 / 47.14 ± 4.43</td> <!-- SB10k -->
   <td class="de la">3.73 ± 1.14 / 44.43 ± 4.17</td> <!-- ScaLA-de -->
   <td class="de rc">14.82 ± 2.69 / 35.50 ± 3.15</td> <!-- GermanQuAD -->
   <td class="nl ner">22.50 ± 2.27 / 24.09 ± 2.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.04 ± 1.51 / 18.08 ± 2.09</td> <!-- Dutch Social -->
   <td class="nl la">-0.61 ± 1.30 / 46.51 ± 2.55</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.96 ± 1.55 / 35.73 ± 1.87</td> <!-- SQuAD-nl -->
   <td class="en ner">38.51 ± 3.33 / 38.08 ± 2.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.60 ± 2.87 / 58.50 ± 1.25</td> <!-- SST5 -->
   <td class="en la">2.23 ± 1.32 / 34.15 ± 0.60</td> <!-- ScaLA-en -->
   <td class="en rc">45.44 ± 3.61 / 59.52 ± 2.98</td> <!-- SQuAD -->
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
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.99</td> <!-- Danish rank -->
   <td class="no-rank">3.49</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.78</td> <!-- Swedish rank -->
   <td class="is-rank">4.17</td> <!-- Icelandic rank -->
   <td class="de-rank">3.30</td> <!-- German rank -->
   <td class="nl-rank">3.70</td> <!-- Dutch rank -->
   <td class="en-rank">2.71</td> <!-- English rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da rc">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="no ner">15.53 ± 5.69 / 15.49 ± 5.08</td> <!-- NorNE-nb -->
   <td class="no ner">19.78 ± 4.54 / 18.86 ± 4.22</td> <!-- NorNE-nn -->
   <td class="no sent">32.89 ± 1.65 / 42.58 ± 3.16</td> <!-- NoReC -->
   <td class="no la">1.18 ± 1.00 / 33.34 ± 0.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="de ner">16.95 ± 2.96 / 15.80 ± 2.16</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de rc">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td class="nl ner">16.90 ± 4.91 / 17.38 ± 4.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td class="en ner">19.65 ± 5.96 / 18.64 ± 5.49</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en rc">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.33</td> <!-- ScandEval rank -->
   <td class="da-rank">3.10</td> <!-- Danish rank -->
   <td class="no-rank">3.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.20</td> <!-- Swedish rank -->
   <td class="is-rank">4.19</td> <!-- Icelandic rank -->
   <td class="de-rank">3.27</td> <!-- German rank -->
   <td class="nl-rank">3.41</td> <!-- Dutch rank -->
   <td class="en-rank">2.71</td> <!-- English rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
   <td class="no ner">39.78 ± 2.67 / 31.15 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">43.58 ± 2.49 / 36.60 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">22.01 ± 3.00 / 40.48 ± 2.81</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.35 / 44.34 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">1.45 ± 1.35 / 39.55 ± 3.53</td> <!-- ScaLA-nn -->
   <td class="no rc">32.42 ± 1.72 / 56.65 ± 0.92</td> <!-- NorQuAD -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is rc">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="de ner">36.62 ± 1.56 / 28.22 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de rc">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td class="nl ner">38.85 ± 3.77 / 32.18 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en rc">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="da-rank">3.15</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.72</td> <!-- Swedish rank -->
   <td class="is-rank">4.54</td> <!-- Icelandic rank -->
   <td class="de-rank">3.31</td> <!-- German rank -->
   <td class="nl-rank">3.67</td> <!-- Dutch rank -->
   <td class="en-rank">2.64</td> <!-- English rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da rc">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="no ner">34.42 ± 3.22 / 27.79 ± 2.40</td> <!-- NorNE-nb -->
   <td class="no ner">35.17 ± 4.05 / 30.70 ± 3.37</td> <!-- NorNE-nn -->
   <td class="no sent">21.46 ± 5.63 / 38.36 ± 6.18</td> <!-- NoReC -->
   <td class="no la">0.34 ± 1.25 / 33.60 ± 0.50</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.58 / 34.69 ± 3.11</td> <!-- ScaLA-nn -->
   <td class="no rc">0.12 ± 0.04 / 9.85 ± 0.17</td> <!-- NorQuAD -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="is ner">8.84 ± 2.72 / 8.59 ± 2.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.38 ± 1.52 / 34.73 ± 1.40</td> <!-- ScaLA-is -->
   <td class="is rc">5.08 ± 1.06 / 18.85 ± 2.62</td> <!-- NQiI -->
   <td class="de ner">30.85 ± 4.69 / 24.38 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.81 / 64.87 ± 2.42</td> <!-- SB10k -->
   <td class="de la">2.67 ± 1.77 / 41.55 ± 4.54</td> <!-- ScaLA-de -->
   <td class="de rc">4.09 ± 1.94 / 12.70 ± 2.66</td> <!-- GermanQuAD -->
   <td class="nl ner">37.37 ± 2.22 / 30.45 ± 2.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.55 ± 1.82 / 23.90 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">0.05 ± 1.35 / 35.78 ± 2.30</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.81 ± 1.54 / 46.37 ± 1.51</td> <!-- SQuAD-nl -->
   <td class="en ner">38.23 ± 3.10 / 36.38 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">60.70 ± 1.80 / 66.82 ± 1.12</td> <!-- SST5 -->
   <td class="en la">-0.19 ± 2.28 / 38.77 ± 3.32</td> <!-- ScaLA-en -->
   <td class="en rc">61.93 ± 1.98 / 73.71 ± 1.57</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="da-rank">3.36</td> <!-- Danish rank -->
   <td class="no-rank">3.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.09</td> <!-- Swedish rank -->
   <td class="is-rank">4.16</td> <!-- Icelandic rank -->
   <td class="de-rank">3.38</td> <!-- German rank -->
   <td class="nl-rank">3.31</td> <!-- Dutch rank -->
   <td class="en-rank">3.25</td> <!-- English rank -->
   <td class="da ner">46.78 ± 1.50 / 44.41 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">27.78 ± 2.22 / 49.38 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">3.04 ± 1.85 / 46.85 ± 3.03</td> <!-- ScaLA-da -->
   <td class="da rc">15.52 ± 0.98 / 23.22 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="no ner">60.76 ± 1.53 / 58.35 ± 1.41</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.19 / 55.90 ± 1.12</td> <!-- NorNE-nn -->
   <td class="no sent">25.98 ± 1.33 / 40.58 ± 0.60</td> <!-- NoReC -->
   <td class="no la">2.65 ± 2.08 / 48.09 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">3.47 ± 1.47 / 48.98 ± 1.75</td> <!-- ScaLA-nn -->
   <td class="no rc">0.20 ± 0.09 / 0.82 ± 0.39</td> <!-- NorQuAD -->
   <td class="sv ner">49.86 ± 1.85 / 44.53 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">60.06 ± 1.30 / 55.65 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">3.18 ± 1.63 / 48.38 ± 1.42</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.08 ± 2.60 / 23.46 ± 3.10</td> <!-- ScandiQA-sv -->
   <td class="is ner">45.47 ± 2.05 / 47.67 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.14 ± 1.81 / 48.47 ± 1.64</td> <!-- ScaLA-is -->
   <td class="is rc">1.63 ± 0.33 / 21.45 ± 1.39</td> <!-- NQiI -->
   <td class="de ner">28.29 ± 6.50 / 27.54 ± 6.33</td> <!-- GermEval -->
   <td class="de sent">51.70 ± 1.63 / 67.81 ± 1.08</td> <!-- SB10k -->
   <td class="de la">2.12 ± 2.30 / 49.13 ± 2.33</td> <!-- ScaLA-de -->
   <td class="de rc">0.03 ± 0.05 / 0.69 ± 0.53</td> <!-- GermanQuAD -->
   <td class="nl ner">58.67 ± 1.07 / 68.27 ± 0.94</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.82 ± 4.47 / 37.11 ± 2.75</td> <!-- Dutch Social -->
   <td class="nl la">9.27 ± 4.66 / 52.04 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">2.17 ± 0.34 / 8.02 ± 0.41</td> <!-- SQuAD-nl -->
   <td class="en ner">71.33 ± 0.75 / 73.43 ± 0.61</td> <!-- CoNLL-en -->
   <td class="en sent">36.75 ± 1.28 / 47.80 ± 1.46</td> <!-- SST5 -->
   <td class="en la">0.24 ± 1.44 / 47.55 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en rc">1.30 ± 0.31 / 9.37 ± 0.28</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="da-rank">3.35</td> <!-- Danish rank -->
   <td class="no-rank">3.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.15</td> <!-- Swedish rank -->
   <td class="is-rank">4.36</td> <!-- Icelandic rank -->
   <td class="de-rank">3.26</td> <!-- German rank -->
   <td class="nl-rank">3.86</td> <!-- Dutch rank -->
   <td class="en-rank">2.57</td> <!-- English rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da rc">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="no ner">26.99 ± 3.92 / 24.61 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">25.74 ± 3.76 / 24.51 ± 2.96</td> <!-- NorNE-nn -->
   <td class="no sent">19.85 ± 1.97 / 35.75 ± 1.74</td> <!-- NoReC -->
   <td class="no la">1.96 ± 1.33 / 44.22 ± 2.93</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.39 / 39.57 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no rc">16.33 ± 2.17 / 31.16 ± 3.40</td> <!-- NorQuAD -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="de ner">28.04 ± 2.71 / 24.08 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td class="nl ner">23.44 ± 5.09 / 25.00 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="en ner">40.89 ± 2.63 / 37.44 ± 2.39</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en rc">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="da-rank">3.65</td> <!-- Danish rank -->
   <td class="no-rank">3.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.14</td> <!-- Swedish rank -->
   <td class="is-rank">4.07</td> <!-- Icelandic rank -->
   <td class="de-rank">3.26</td> <!-- German rank -->
   <td class="nl-rank">3.62</td> <!-- Dutch rank -->
   <td class="en-rank">3.20</td> <!-- English rank -->
   <td class="da ner">26.96 ± 1.31 / 25.63 ± 1.35</td> <!-- DANSK -->
   <td class="da sent">30.13 ± 2.10 / 46.78 ± 4.49</td> <!-- Angry Tweets -->
   <td class="da la">2.01 ± 1.29 / 48.79 ± 1.65</td> <!-- ScaLA-da -->
   <td class="da rc">8.25 ± 1.03 / 16.49 ± 1.77</td> <!-- ScandiQA-da -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">63.04 ± 0.70 / 56.50 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.93 ± 1.00 / 17.75 ± 1.16</td> <!-- ScandiQA-sv -->
   <td class="is ner">47.62 ± 2.97 / 50.59 ± 2.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.64 ± 2.11 / 49.47 ± 1.79</td> <!-- ScaLA-is -->
   <td class="is rc">1.27 ± 0.46 / 12.20 ± 2.90</td> <!-- NQiI -->
   <td class="de ner">40.20 ± 3.20 / 40.33 ± 3.13</td> <!-- GermEval -->
   <td class="de sent">48.71 ± 1.60 / 65.32 ± 1.57</td> <!-- SB10k -->
   <td class="de la">5.53 ± 1.92 / 51.10 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">0.06 ± 0.06 / 1.12 ± 1.10</td> <!-- GermanQuAD -->
   <td class="nl ner">56.98 ± 1.37 / 66.91 ± 1.60</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.66 ± 4.65 / 31.17 ± 3.34</td> <!-- Dutch Social -->
   <td class="nl la">19.37 ± 4.34 / 56.74 ± 3.13</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.11 ± 0.37 / 7.91 ± 0.25</td> <!-- SQuAD-nl -->
   <td class="en ner">71.90 ± 1.49 / 74.21 ± 1.10</td> <!-- CoNLL-en -->
   <td class="en sent">36.22 ± 1.39 / 45.80 ± 1.20</td> <!-- SST5 -->
   <td class="en la">0.47 ± 1.65 / 48.67 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en rc">2.44 ± 0.17 / 8.50 ± 0.20</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.42</td> <!-- Danish rank -->
   <td class="no-rank">3.91</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.13</td> <!-- Swedish rank -->
   <td class="is-rank">4.42</td> <!-- Icelandic rank -->
   <td class="de-rank">3.55</td> <!-- German rank -->
   <td class="nl-rank">4.02</td> <!-- Dutch rank -->
   <td class="en-rank">2.41</td> <!-- English rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="no ner">12.10 ± 5.58 / 12.85 ± 4.80</td> <!-- NorNE-nb -->
   <td class="no ner">13.42 ± 6.02 / 13.82 ± 5.16</td> <!-- NorNE-nn -->
   <td class="no sent">22.82 ± 3.11 / 43.88 ± 3.10</td> <!-- NoReC -->
   <td class="no la">2.70 ± 2.16 / 47.68 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">2.21 ± 1.46 / 42.80 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no rc">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="de ner">9.23 ± 4.86 / 10.43 ± 3.83</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de rc">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td class="nl ner">11.66 ± 6.46 / 15.15 ± 4.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.65</td> <!-- Danish rank -->
   <td class="no-rank">3.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.14</td> <!-- Swedish rank -->
   <td class="is-rank">4.07</td> <!-- Icelandic rank -->
   <td class="de-rank">3.26</td> <!-- German rank -->
   <td class="nl-rank">4.08</td> <!-- Dutch rank -->
   <td class="en-rank">3.20</td> <!-- English rank -->
   <td class="da ner">26.96 ± 1.31 / 25.63 ± 1.35</td> <!-- DANSK -->
   <td class="da sent">30.13 ± 2.10 / 46.78 ± 4.49</td> <!-- Angry Tweets -->
   <td class="da la">2.01 ± 1.29 / 48.79 ± 1.65</td> <!-- ScaLA-da -->
   <td class="da rc">8.22 ± 1.11 / 16.40 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="no ner">63.79 ± 2.11 / 67.14 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">60.96 ± 1.11 / 64.65 ± 1.00</td> <!-- NorNE-nn -->
   <td class="no sent">32.83 ± 1.48 / 43.32 ± 0.69</td> <!-- NoReC -->
   <td class="no la">1.09 ± 1.93 / 48.72 ± 1.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.18 ± 1.93 / 47.30 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">62.71 ± 0.81 / 57.24 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.76 ± 1.03 / 17.62 ± 1.24</td> <!-- ScandiQA-sv -->
   <td class="is ner">48.62 ± 2.65 / 51.75 ± 2.37</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.64 ± 2.11 / 49.47 ± 1.79</td> <!-- ScaLA-is -->
   <td class="is rc">1.22 ± 0.49 / 12.16 ± 3.00</td> <!-- NQiI -->
   <td class="de ner">41.82 ± 3.25 / 42.03 ± 3.15</td> <!-- GermEval -->
   <td class="de sent">49.38 ± 1.72 / 66.10 ± 1.17</td> <!-- SB10k -->
   <td class="de la">4.77 ± 2.08 / 49.48 ± 2.07</td> <!-- ScaLA-de -->
   <td class="de rc">0.05 ± 0.06 / 0.92 ± 0.55</td> <!-- GermanQuAD -->
   <td class="nl ner">49.82 ± 2.71 / 62.06 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.70 ± 3.10 / 26.12 ± 2.40</td> <!-- Dutch Social -->
   <td class="nl la">6.60 ± 3.84 / 50.71 ± 1.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">2.13 ± 0.10 / 6.80 ± 0.37</td> <!-- SQuAD-nl -->
   <td class="en ner">71.90 ± 1.49 / 74.21 ± 1.10</td> <!-- CoNLL-en -->
   <td class="en sent">36.22 ± 1.39 / 45.80 ± 1.20</td> <!-- SST5 -->
   <td class="en la">0.47 ± 1.65 / 48.67 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en rc">2.40 ± 0.23 / 8.51 ± 0.21</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da-rank">3.53</td> <!-- Danish rank -->
   <td class="no-rank">4.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.87</td> <!-- Swedish rank -->
   <td class="is-rank">4.41</td> <!-- Icelandic rank -->
   <td class="de-rank">3.81</td> <!-- German rank -->
   <td class="nl-rank">4.06</td> <!-- Dutch rank -->
   <td class="en-rank">2.71</td> <!-- English rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da rc">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="no ner">9.06 ± 6.86 / 8.39 ± 6.41</td> <!-- NorNE-nb -->
   <td class="no ner">17.16 ± 6.21 / 16.00 ± 5.94</td> <!-- NorNE-nn -->
   <td class="no sent">25.52 ± 3.72 / 41.44 ± 4.44</td> <!-- NoReC -->
   <td class="no la">0.68 ± 1.54 / 45.09 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">0.17 ± 2.27 / 42.02 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no rc">0.46 ± 0.07 / 6.96 ± 0.13</td> <!-- NorQuAD -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.04 ± 5.36 / 9.25 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.08 ± 1.02 / 34.02 ± 0.68</td> <!-- ScaLA-is -->
   <td class="is rc">8.86 ± 2.70 / 27.28 ± 1.45</td> <!-- NQiI -->
   <td class="de ner">14.06 ± 5.31 / 12.90 ± 4.52</td> <!-- GermEval -->
   <td class="de sent">28.07 ± 6.33 / 38.61 ± 7.42</td> <!-- SB10k -->
   <td class="de la">2.31 ± 1.88 / 44.45 ± 4.23</td> <!-- ScaLA-de -->
   <td class="de rc">6.89 ± 2.35 / 17.95 ± 3.37</td> <!-- GermanQuAD -->
   <td class="nl ner">18.70 ± 5.76 / 19.58 ± 4.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.70 ± 1.69 / 17.91 ± 1.48</td> <!-- Dutch Social -->
   <td class="nl la">2.19 ± 2.08 / 45.43 ± 3.44</td> <!-- ScaLA-nl -->
   <td class="nl rc">38.08 ± 1.07 / 48.44 ± 1.55</td> <!-- SQuAD-nl -->
   <td class="en ner">25.36 ± 8.05 / 24.05 ± 7.34</td> <!-- CoNLL-en -->
   <td class="en sent">56.91 ± 2.41 / 66.15 ± 1.54</td> <!-- SST5 -->
   <td class="en la">7.10 ± 2.89 / 49.36 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en rc">58.60 ± 5.37 / 70.37 ± 4.71</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="da-rank">3.73</td> <!-- Danish rank -->
   <td class="no-rank">3.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.51</td> <!-- Swedish rank -->
   <td class="is-rank">3.77</td> <!-- Icelandic rank -->
   <td class="de-rank">3.71</td> <!-- German rank -->
   <td class="nl-rank">3.91</td> <!-- Dutch rank -->
   <td class="en-rank">3.66</td> <!-- English rank -->
   <td class="da ner">36.51 ± 2.44 / 36.31 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">22.07 ± 2.24 / 44.70 ± 3.72</td> <!-- Angry Tweets -->
   <td class="da la">1.63 ± 1.49 / 45.36 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da rc">3.09 ± 1.00 / 9.48 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="no ner">55.55 ± 3.71 / 52.52 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">53.53 ± 3.03 / 50.23 ± 3.00</td> <!-- NorNE-nn -->
   <td class="no sent">12.69 ± 4.51 / 32.23 ± 3.53</td> <!-- NoReC -->
   <td class="no la">2.79 ± 1.16 / 47.71 ± 2.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.66 ± 2.18 / 46.60 ± 2.87</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.60 ± 0.72</td> <!-- NorQuAD -->
   <td class="sv ner">42.78 ± 3.26 / 40.46 ± 3.04</td> <!-- SUC3 -->
   <td class="sv sent">44.95 ± 2.30 / 48.17 ± 1.06</td> <!-- SweReC -->
   <td class="sv la">1.43 ± 1.34 / 48.66 ± 2.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.71 ± 2.58 / 16.77 ± 2.50</td> <!-- ScandiQA-sv -->
   <td class="is ner">46.95 ± 2.05 / 50.04 ± 1.99</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.40 ± 1.40 / 48.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is rc">10.48 ± 1.75 / 28.80 ± 1.59</td> <!-- NQiI -->
   <td class="de ner">30.18 ± 6.85 / 29.11 ± 6.64</td> <!-- GermEval -->
   <td class="de sent">32.66 ± 3.87 / 53.17 ± 4.09</td> <!-- SB10k -->
   <td class="de la">2.10 ± 1.30 / 47.10 ± 2.29</td> <!-- ScaLA-de -->
   <td class="de rc">0.46 ± 0.39 / 4.04 ± 2.36</td> <!-- GermanQuAD -->
   <td class="nl ner">44.46 ± 2.24 / 60.04 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.39 ± 4.20 / 30.69 ± 2.83</td> <!-- Dutch Social -->
   <td class="nl la">2.07 ± 1.34 / 48.42 ± 1.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">4.30 ± 1.26 / 9.24 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="en ner">68.25 ± 2.50 / 70.44 ± 2.50</td> <!-- CoNLL-en -->
   <td class="en sent">1.92 ± 1.68 / 28.84 ± 2.38</td> <!-- SST5 -->
   <td class="en la">1.08 ± 1.34 / 47.42 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en rc">2.79 ± 0.93 / 10.00 ± 0.84</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da-rank">3.99</td> <!-- Danish rank -->
   <td class="no-rank">3.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.38</td> <!-- Swedish rank -->
   <td class="is-rank">4.69</td> <!-- Icelandic rank -->
   <td class="de-rank">3.28</td> <!-- German rank -->
   <td class="nl-rank">3.52</td> <!-- Dutch rank -->
   <td class="en-rank">3.63</td> <!-- English rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da rc">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no rc">26.86 ± 1.65 / 50.11 ± 1.80</td> <!-- NorQuAD -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is rc">1.04 ± 0.96 / 7.35 ± 3.52</td> <!-- NQiI -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 5.06 / 49.68 ± 5.74</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de rc">20.44 ± 3.29 / 45.50 ± 3.33</td> <!-- GermanQuAD -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.49 ± 1.37 / 47.34 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en rc">36.51 ± 2.07 / 50.66 ± 1.90</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da-rank">3.85</td> <!-- Danish rank -->
   <td class="no-rank">3.86</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.56</td> <!-- Swedish rank -->
   <td class="is-rank">4.05</td> <!-- Icelandic rank -->
   <td class="de-rank">3.69</td> <!-- German rank -->
   <td class="nl-rank">3.96</td> <!-- Dutch rank -->
   <td class="en-rank">3.39</td> <!-- English rank -->
   <td class="da ner">33.62 ± 1.57 / 31.69 ± 1.40</td> <!-- DANSK -->
   <td class="da sent">20.71 ± 1.68 / 40.07 ± 2.65</td> <!-- Angry Tweets -->
   <td class="da la">1.19 ± 1.08 / 48.46 ± 1.34</td> <!-- ScaLA-da -->
   <td class="da rc">4.19 ± 0.88 / 7.68 ± 1.59</td> <!-- ScandiQA-da -->
   <td class="no ner">46.11 ± 3.68 / 43.54 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">35.18 ± 4.90 / 33.22 ± 4.64</td> <!-- NorNE-nn -->
   <td class="no sent">19.19 ± 2.87 / 37.36 ± 1.97</td> <!-- NoReC -->
   <td class="no la">2.76 ± 1.42 / 50.99 ± 0.83</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 1.04 / 49.39 ± 0.80</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">26.87 ± 2.26 / 25.42 ± 2.14</td> <!-- SUC3 -->
   <td class="sv sent">57.41 ± 1.89 / 53.50 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">-1.06 ± 1.33 / 48.72 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv rc">5.54 ± 1.44 / 10.83 ± 2.62</td> <!-- ScandiQA-sv -->
   <td class="is ner">43.93 ± 1.57 / 46.59 ± 1.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.04 ± 1.75 / 47.53 ± 1.60</td> <!-- ScaLA-is -->
   <td class="is rc">6.13 ± 0.63 / 21.73 ± 0.95</td> <!-- NQiI -->
   <td class="de ner">33.18 ± 2.13 / 32.48 ± 2.13</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 2.23 / 55.01 ± 2.11</td> <!-- SB10k -->
   <td class="de la">1.83 ± 1.54 / 49.40 ± 1.24</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td class="nl ner">41.38 ± 2.82 / 56.29 ± 1.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.45 ± 2.80 / 29.85 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.55 ± 1.97 / 49.24 ± 1.16</td> <!-- ScaLA-nl -->
   <td class="nl rc">4.40 ± 0.22 / 6.62 ± 0.38</td> <!-- SQuAD-nl -->
   <td class="en ner">65.85 ± 0.80 / 68.72 ± 0.81</td> <!-- CoNLL-en -->
   <td class="en sent">25.85 ± 2.01 / 40.72 ± 0.85</td> <!-- SST5 -->
   <td class="en la">1.21 ± 1.72 / 50.03 ± 0.84</td> <!-- ScaLA-en -->
   <td class="en rc">4.00 ± 0.55 / 11.02 ± 0.40</td> <!-- SQuAD -->
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
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da-rank">3.79</td> <!-- Danish rank -->
   <td class="no-rank">4.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.45</td> <!-- Swedish rank -->
   <td class="is-rank">4.58</td> <!-- Icelandic rank -->
   <td class="de-rank">3.92</td> <!-- German rank -->
   <td class="nl-rank">3.95</td> <!-- Dutch rank -->
   <td class="en-rank">2.82</td> <!-- English rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da rc">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">29.52 ± 1.48 / 29.79 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">31.27 ± 1.30 / 31.91 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">11.49 ± 1.38 / 27.12 ± 1.98</td> <!-- NoReC -->
   <td class="no la">0.29 ± 1.58 / 40.21 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">-0.12 ± 1.48 / 39.92 ± 3.90</td> <!-- ScaLA-nn -->
   <td class="no rc">7.80 ± 1.19 / 17.09 ± 2.72</td> <!-- NorQuAD -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.50 ± 3.17 / 9.41 ± 3.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is rc">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
   <td class="nl ner">18.66 ± 4.43 / 17.56 ± 4.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en rc">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.82</td> <!-- ScandEval rank -->
   <td class="da-rank">3.81</td> <!-- Danish rank -->
   <td class="no-rank">4.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.50</td> <!-- Swedish rank -->
   <td class="is-rank">4.52</td> <!-- Icelandic rank -->
   <td class="de-rank">3.82</td> <!-- German rank -->
   <td class="nl-rank">4.08</td> <!-- Dutch rank -->
   <td class="en-rank">2.89</td> <!-- English rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da rc">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="no ner">34.46 ± 2.01 / 33.09 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">33.41 ± 2.21 / 33.91 ± 2.33</td> <!-- NorNE-nn -->
   <td class="no sent">6.31 ± 3.46 / 20.67 ± 2.69</td> <!-- NoReC -->
   <td class="no la">-1.59 ± 1.08 / 36.27 ± 3.71</td> <!-- ScaLA-nb -->
   <td class="no la">0.61 ± 1.41 / 38.84 ± 5.10</td> <!-- ScaLA-nn -->
   <td class="no rc">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td class="nl ner">28.30 ± 3.90 / 28.67 ± 3.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en rc">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="da-rank">3.85</td> <!-- Danish rank -->
   <td class="no-rank">4.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.54</td> <!-- Swedish rank -->
   <td class="is-rank">4.67</td> <!-- Icelandic rank -->
   <td class="de-rank">4.00</td> <!-- German rank -->
   <td class="nl-rank">4.29</td> <!-- Dutch rank -->
   <td class="en-rank">2.91</td> <!-- English rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td class="no ner">30.79 ± 1.95 / 32.18 ± 1.98</td> <!-- NorNE-nb -->
   <td class="no ner">31.12 ± 2.36 / 33.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">9.95 ± 3.92 / 29.01 ± 2.80</td> <!-- NoReC -->
   <td class="no la">-0.95 ± 1.87 / 39.37 ± 3.33</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 1.73 / 42.36 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.60 ± 2.38 / 14.36 ± 2.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.04 ± 0.90 / 34.46 ± 1.41</td> <!-- ScaLA-is -->
   <td class="is rc">1.51 ± 0.68 / 13.16 ± 3.12</td> <!-- NQiI -->
   <td class="de ner">21.46 ± 2.04 / 20.83 ± 1.63</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de rc">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td class="nl ner">22.58 ± 5.05 / 26.82 ± 3.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.92 ± 2.71 / 19.51 ± 4.22</td> <!-- Dutch Social -->
   <td class="nl la">-1.27 ± 1.85 / 41.38 ± 3.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">6.64 ± 1.96 / 11.74 ± 1.62</td> <!-- SQuAD-nl -->
   <td class="en ner">26.47 ± 6.25 / 28.27 ± 5.35</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en rc">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
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
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="da-rank">4.16</td> <!-- Danish rank -->
   <td class="no-rank">4.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.83</td> <!-- Swedish rank -->
   <td class="is-rank">4.61</td> <!-- Icelandic rank -->
   <td class="de-rank">4.17</td> <!-- German rank -->
   <td class="nl-rank">4.69</td> <!-- Dutch rank -->
   <td class="en-rank">4.09</td> <!-- English rank -->
   <td class="da ner">16.04 ± 2.47 / 15.60 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">17.37 ± 3.82 / 36.83 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">1.34 ± 0.97 / 35.45 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da rc">1.58 ± 0.51 / 6.64 ± 1.56</td> <!-- ScandiQA-da -->
   <td class="no ner">25.49 ± 3.39 / 23.54 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">25.94 ± 1.70 / 24.10 ± 1.64</td> <!-- NorNE-nn -->
   <td class="no sent">12.60 ± 2.97 / 32.27 ± 3.43</td> <!-- NoReC -->
   <td class="no la">0.50 ± 1.27 / 36.93 ± 4.00</td> <!-- ScaLA-nb -->
   <td class="no la">1.83 ± 1.64 / 37.67 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">11.91 ± 3.04 / 11.31 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.11 ± 5.32 / 50.09 ± 3.33</td> <!-- SweReC -->
   <td class="sv la">0.86 ± 0.82 / 39.16 ± 3.63</td> <!-- ScaLA-sv -->
   <td class="sv rc">2.00 ± 0.63 / 7.20 ± 1.68</td> <!-- ScandiQA-sv -->
   <td class="is ner">17.34 ± 1.13 / 16.43 ± 1.26</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.06 ± 0.99 / 36.73 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is rc">1.02 ± 0.30 / 21.61 ± 1.10</td> <!-- NQiI -->
   <td class="de ner">8.03 ± 1.35 / 8.63 ± 1.36</td> <!-- GermEval -->
   <td class="de sent">23.44 ± 7.21 / 42.87 ± 7.78</td> <!-- SB10k -->
   <td class="de la">-0.17 ± 1.13 / 39.21 ± 4.70</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td class="nl ner">13.09 ± 1.68 / 16.25 ± 2.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.92 ± 2.11 / 25.39 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.93 ± 1.37 / 40.76 ± 4.83</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.26 ± 0.09 / 2.70 ± 1.10</td> <!-- SQuAD-nl -->
   <td class="en ner">34.64 ± 1.25 / 34.41 ± 1.49</td> <!-- CoNLL-en -->
   <td class="en sent">4.00 ± 3.78 / 24.24 ± 3.94</td> <!-- SST5 -->
   <td class="en la">1.33 ± 1.00 / 42.07 ± 4.82</td> <!-- ScaLA-en -->
   <td class="en rc">0.43 ± 0.11 / 6.18 ± 1.24</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="da-rank">4.17</td> <!-- Danish rank -->
   <td class="no-rank">4.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.85</td> <!-- Swedish rank -->
   <td class="is-rank">4.71</td> <!-- Icelandic rank -->
   <td class="de-rank">4.29</td> <!-- German rank -->
   <td class="nl-rank">4.71</td> <!-- Dutch rank -->
   <td class="en-rank">4.17</td> <!-- English rank -->
   <td class="da ner">12.87 ± 1.63 / 13.23 ± 1.55</td> <!-- DANSK -->
   <td class="da sent">18.61 ± 4.17 / 35.23 ± 3.90</td> <!-- Angry Tweets -->
   <td class="da la">0.30 ± 1.39 / 37.84 ± 3.88</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-da -->
   <td class="no ner">18.38 ± 2.01 / 17.08 ± 1.97</td> <!-- NorNE-nb -->
   <td class="no ner">12.76 ± 1.29 / 11.65 ± 1.21</td> <!-- NorNE-nn -->
   <td class="no sent">15.29 ± 5.37 / 34.15 ± 4.23</td> <!-- NoReC -->
   <td class="no la">0.17 ± 0.84 / 36.29 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">0.37 ± 0.69 / 35.08 ± 2.81</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorQuAD -->
   <td class="sv ner">10.54 ± 1.12 / 9.71 ± 1.00</td> <!-- SUC3 -->
   <td class="sv sent">55.54 ± 2.75 / 52.75 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">-0.15 ± 0.52 / 35.33 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.02 ± 0.03 / 0.04 ± 0.05</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.96 ± 1.11 / 8.96 ± 1.05</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.10 ± 1.46 / 35.81 ± 3.45</td> <!-- ScaLA-is -->
   <td class="is rc">0.12 ± 0.10 / 4.48 ± 1.39</td> <!-- NQiI -->
   <td class="de ner">9.53 ± 0.71 / 9.93 ± 0.76</td> <!-- GermEval -->
   <td class="de sent">13.29 ± 8.29 / 29.94 ± 8.32</td> <!-- SB10k -->
   <td class="de la">-0.15 ± 0.77 / 33.37 ± 0.37</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td class="nl ner">11.66 ± 1.16 / 13.45 ± 1.20</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 24.33 ± 0.14</td> <!-- Dutch Social -->
   <td class="nl la">-0.21 ± 1.89 / 35.79 ± 2.99</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.17 ± 0.04 / 0.17 ± 0.04</td> <!-- SQuAD-nl -->
   <td class="en ner">30.77 ± 0.92 / 30.14 ± 1.03</td> <!-- CoNLL-en -->
   <td class="en sent">0.58 ± 1.45 / 20.82 ± 1.74</td> <!-- SST5 -->
   <td class="en la">-0.17 ± 0.47 / 37.18 ± 3.93</td> <!-- ScaLA-en -->
   <td class="en rc">0.46 ± 0.14 / 6.16 ± 0.24</td> <!-- SQuAD -->
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
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (zero-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,448 ± 488 / 708 ± 225</td> <!-- Model inference speed -->
   <td class="rank">4.40</td> <!-- ScandEval rank -->
   <td class="da-rank">4.42</td> <!-- Danish rank -->
   <td class="no-rank">4.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.60</td> <!-- Swedish rank -->
   <td class="is-rank">4.88</td> <!-- Icelandic rank -->
   <td class="de-rank">4.27</td> <!-- German rank -->
   <td class="nl-rank">4.65</td> <!-- Dutch rank -->
   <td class="en-rank">3.34</td> <!-- English rank -->
   <td class="da ner">0.26 ± 0.11 / 0.21 ± 0.09</td> <!-- DANSK -->
   <td class="da sent">2.42 ± 0.62 / 18.31 ± 0.16</td> <!-- Angry Tweets -->
   <td class="da la">15.18 ± 1.23 / 41.98 ± 0.53</td> <!-- ScaLA-da -->
   <td class="da rc">0.05 ± 0.02 / 16.11 ± 0.11</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no la">2.26 ± 0.56 / 33.38 ± 0.32</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.10 ± 0.04 / 32.34 ± 0.21</td> <!-- NorQuAD -->
   <td class="sv ner">3.65 ± 1.19 / 3.25 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">0.83 ± 0.68 / 19.20 ± 0.13</td> <!-- SweReC -->
   <td class="sv la">0.39 ± 1.03 / 33.40 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.18 ± 0.03 / 17.80 ± 0.09</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 21.65 ± 0.26</td> <!-- NQiI -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">25.66 ± 1.05 / 49.73 ± 0.65</td> <!-- ScaLA-de -->
   <td class="de rc">0.08 ± 0.03 / 32.26 ± 0.25</td> <!-- GermanQuAD -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 8.62 ± 0.30</td> <!-- Dutch Social -->
   <td class="nl la">17.12 ± 0.82 / 47.35 ± 0.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.08 ± 0.03 / 22.98 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">39.23 ± 0.88 / 55.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">42.71 ± 1.41 / 70.89 ± 0.70</td> <!-- ScaLA-en -->
   <td class="en rc">5.95 ± 0.18 / 40.91 ± 0.16</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="da-rank">4.17</td> <!-- Danish rank -->
   <td class="no-rank">4.31</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.14</td> <!-- Swedish rank -->
   <td class="is-rank">4.75</td> <!-- Icelandic rank -->
   <td class="de-rank">4.50</td> <!-- German rank -->
   <td class="nl-rank">4.82</td> <!-- Dutch rank -->
   <td class="en-rank">4.42</td> <!-- English rank -->
   <td class="da ner">12.82 ± 2.64 / 12.37 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">3.55 ± 3.64 / 22.75 ± 4.02</td> <!-- Angry Tweets -->
   <td class="da la">0.68 ± 1.41 / 35.13 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da rc">19.85 ± 1.75 / 24.31 ± 1.88</td> <!-- ScandiQA-da -->
   <td class="no ner">12.77 ± 3.48 / 14.13 ± 3.09</td> <!-- NorNE-nb -->
   <td class="no ner">10.51 ± 3.44 / 9.95 ± 3.51</td> <!-- NorNE-nn -->
   <td class="no sent">8.70 ± 4.43 / 25.39 ± 3.30</td> <!-- NoReC -->
   <td class="no la">0.00 ± 1.60 / 38.54 ± 3.41</td> <!-- ScaLA-nb -->
   <td class="no la">0.82 ± 1.39 / 37.77 ± 4.45</td> <!-- ScaLA-nn -->
   <td class="no rc">1.85 ± 0.82 / 10.19 ± 1.99</td> <!-- NorQuAD -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="is ner">3.69 ± 1.28 / 3.66 ± 1.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.24 ± 1.37 / 42.67 ± 4.99</td> <!-- ScaLA-is -->
   <td class="is rc">0.29 ± 0.19 / 5.14 ± 0.75</td> <!-- NQiI -->
   <td class="de ner">5.80 ± 1.56 / 5.41 ± 1.56</td> <!-- GermEval -->
   <td class="de sent">4.45 ± 1.73 / 29.26 ± 3.66</td> <!-- SB10k -->
   <td class="de la">-0.48 ± 1.33 / 43.09 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">0.08 ± 0.12 / 4.02 ± 1.17</td> <!-- GermanQuAD -->
   <td class="nl ner">3.80 ± 1.23 / 4.24 ± 1.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.97 ± 1.50 / 13.00 ± 2.52</td> <!-- Dutch Social -->
   <td class="nl la">-0.37 ± 0.55 / 33.40 ± 0.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.40 ± 0.25 / 2.98 ± 0.44</td> <!-- SQuAD-nl -->
   <td class="en ner">12.34 ± 2.70 / 12.41 ± 2.54</td> <!-- CoNLL-en -->
   <td class="en sent">-1.48 ± 3.09 / 21.17 ± 2.22</td> <!-- SST5 -->
   <td class="en la">-0.48 ± 1.52 / 42.45 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">0.72 ± 0.25 / 6.31 ± 0.51</td> <!-- SQuAD -->
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
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (zero-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,730 ± 294 / 655 ± 228</td> <!-- Model inference speed -->
   <td class="rank">4.45</td> <!-- ScandEval rank -->
   <td class="da-rank">4.30</td> <!-- Danish rank -->
   <td class="no-rank">4.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.68</td> <!-- Swedish rank -->
   <td class="is-rank">4.88</td> <!-- Icelandic rank -->
   <td class="de-rank">4.24</td> <!-- German rank -->
   <td class="nl-rank">4.74</td> <!-- Dutch rank -->
   <td class="en-rank">3.74</td> <!-- English rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">21.83 ± 0.71 / 32.57 ± 0.45</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.09 ± 0.04 / 35.77 ± 0.32</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">7.56 ± 0.61 / 12.76 ± 0.46</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 17.36 ± 0.23</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">1.39 ± 0.61 / 19.22 ± 0.13</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 10.21 ± 0.23</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 10.51 ± 0.36</td> <!-- NQiI -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">23.99 ± 1.10 / 37.11 ± 0.71</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.05 ± 0.02 / 2.05 ± 0.12</td> <!-- GermanQuAD -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.10 ± 1.04 / 17.06 ± 0.56</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.23 ± 0.05 / 3.68 ± 0.13</td> <!-- SQuAD-nl -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">52.31 ± 1.14 / 50.35 ± 0.64</td> <!-- SST5 -->
   <td class="en la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-en -->
   <td class="en rc">4.72 ± 0.23 / 7.12 ± 0.26</td> <!-- SQuAD -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.61</td> <!-- ScandEval rank -->
   <td class="da-rank">4.41</td> <!-- Danish rank -->
   <td class="no-rank">4.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.29</td> <!-- Swedish rank -->
   <td class="is-rank">4.88</td> <!-- Icelandic rank -->
   <td class="de-rank">4.65</td> <!-- German rank -->
   <td class="nl-rank">4.87</td> <!-- Dutch rank -->
   <td class="en-rank">4.54</td> <!-- English rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 12.39 ± 1.52</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 33.45 ± 0.27</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 8.92 ± 2.90</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 11.90 ± 2.74</td> <!-- NQiI -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 14.17 ± 0.79</td> <!-- GermanQuAD -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.95 ± 1.17 / 9.87 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 5.43 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en rc">0.00 ± 0.00 / 3.68 ± 0.43</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>9.3.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="da-rank">4.61</td> <!-- Danish rank -->
   <td class="no-rank">4.60</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.54</td> <!-- Swedish rank -->
   <td class="is-rank">4.88</td> <!-- Icelandic rank -->
   <td class="de-rank">4.65</td> <!-- German rank -->
   <td class="nl-rank">4.86</td> <!-- Dutch rank -->
   <td class="en-rank">4.43</td> <!-- English rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da rc">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.74 ± 0.05</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.19 ± 1.24 / 17.20 ± 1.22</td> <!-- SB10k -->
   <td class="de la">-0.12 ± 0.91 / 36.65 ± 3.92</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 1.29 ± 0.49</td> <!-- GermanQuAD -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en rc">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
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
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>11.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>11.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>11.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/germanic-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Germanic NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-sUmsN&quot; src=&quot;https://datawrapper.dwcdn.net/sUmsN/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
