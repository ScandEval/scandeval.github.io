---
layout: leaderboard
title: Germanic NLU 🇪🇺
---

<center>Last updated: 10/01/2025 11:27:50 CET</center>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model on Faroese tasks">Faroese Rank</span></th>
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Hotter-and-Colder-sentiment</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic reading comprehension - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">FoSent</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese reading comprehension - Exact Match / F1-score">FoQA</span></th>
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Hotter-and-Colder-sentiment">Hotter-and-Colder-sentiment version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoNE">FoNE version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoSent">FoSent version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-fo">ScaLA-fo version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoQA">FoQA version</span></th>
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
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.44</td> <!-- ScandEval rank -->
   <td class="da-rank">1.19</td> <!-- Danish rank -->
   <td class="no-rank">1.44</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.16</td> <!-- Swedish rank -->
   <td class="is-rank">1.24</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.72</td> <!-- Faroese rank -->
   <td class="de-rank">1.46</td> <!-- German rank -->
   <td class="nl-rank">1.99</td> <!-- Dutch rank -->
   <td class="en-rank">1.36</td> <!-- English rank -->
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
   <td class="is sent">49.59 ± 2.76 / 62.50 ± 2.08</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="fo ner">86.51 ± 2.01 / 85.01 ± 2.45</td> <!-- FoNE -->
   <td class="fo sent">38.22 ± 8.49 / 52.33 ± 6.78</td> <!-- FoSent -->
   <td class="fo la">35.09 ± 5.70 / 65.72 ± 3.27</td> <!-- ScaLA-fo -->
   <td class="fo rc">58.65 ± 3.25 / 81.93 ± 2.20</td> <!-- FoQA -->
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
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.5.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.5.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="da-rank">1.34</td> <!-- Danish rank -->
   <td class="no-rank">1.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.20</td> <!-- Swedish rank -->
   <td class="is-rank">1.25</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.89</td> <!-- Faroese rank -->
   <td class="de-rank">1.65</td> <!-- German rank -->
   <td class="nl-rank">2.12</td> <!-- Dutch rank -->
   <td class="en-rank">1.44</td> <!-- English rank -->
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
   <td class="is sent">49.86 ± 5.14 / 64.51 ± 3.68</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is rc">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="fo ner">81.86 ± 2.08 / 67.98 ± 3.64</td> <!-- FoNE -->
   <td class="fo sent">27.30 ± 11.60 / 55.31 ± 9.21</td> <!-- FoSent -->
   <td class="fo la">-0.97 ± 2.82 / 33.64 ± 0.85</td> <!-- ScaLA-fo -->
   <td class="fo rc">56.45 ± 2.88 / 78.76 ± 1.86</td> <!-- FoQA -->
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
   <td>13.2.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.10.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="da-rank">1.63</td> <!-- Danish rank -->
   <td class="no-rank">1.42</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.37</td> <!-- Swedish rank -->
   <td class="is-rank">1.32</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.48</td> <!-- Faroese rank -->
   <td class="de-rank">1.65</td> <!-- German rank -->
   <td class="nl-rank">2.20</td> <!-- Dutch rank -->
   <td class="en-rank">1.35</td> <!-- English rank -->
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
   <td class="is sent">45.30 ± 1.76 / 62.84 ± 1.27</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">54.11 ± 2.40 / 76.46 ± 1.28</td> <!-- ScaLA-is -->
   <td class="is rc">30.93 ± 0.96 / 56.17 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">88.60 ± 0.60 / 89.37 ± 0.54</td> <!-- FoNE -->
   <td class="fo sent">6.70 ± 4.85 / 25.36 ± 7.25</td> <!-- FoSent -->
   <td class="fo la">46.81 ± 2.12 / 72.76 ± 1.40</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.96 ± 1.19 / 30.59 ± 1.61</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="da-rank">1.59</td> <!-- Danish rank -->
   <td class="no-rank">1.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.31</td> <!-- Swedish rank -->
   <td class="is-rank">1.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.02</td> <!-- Faroese rank -->
   <td class="de-rank">1.17</td> <!-- German rank -->
   <td class="nl-rank">2.26</td> <!-- Dutch rank -->
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
   <td class="is sent">36.87 ± 3.38 / 56.59 ± 2.94</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">48.29 ± 2.59 / 73.54 ± 1.99</td> <!-- ScaLA-is -->
   <td class="is rc">29.38 ± 1.81 / 52.42 ± 3.00</td> <!-- NQiI -->
   <td class="fo ner">87.35 ± 0.94 / 87.65 ± 0.94</td> <!-- FoNE -->
   <td class="fo sent">0.04 ± 3.09 / 17.28 ± 2.02</td> <!-- FoSent -->
   <td class="fo la">14.65 ± 11.12 / 46.36 ± 10.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">36.10 ± 1.91 / 48.41 ± 2.09</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>gpt-4o-2024-05-13 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">637 ± 306 / 92 ± 31</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="da-rank">1.48</td> <!-- Danish rank -->
   <td class="no-rank">1.96</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.31</td> <!-- Swedish rank -->
   <td class="is-rank">1.38</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.32</td> <!-- Faroese rank -->
   <td class="de-rank">1.80</td> <!-- German rank -->
   <td class="nl-rank">2.26</td> <!-- Dutch rank -->
   <td class="en-rank">1.54</td> <!-- English rank -->
   <td class="da ner">64.80 ± 1.56 / 45.57 ± 1.47</td> <!-- DANSK -->
   <td class="da sent">53.07 ± 1.45 / 68.64 ± 1.04</td> <!-- Angry Tweets -->
   <td class="da la">64.18 ± 3.36 / 81.90 ± 1.68</td> <!-- ScaLA-da -->
   <td class="da rc">49.02 ± 1.18 / 63.09 ± 1.29</td> <!-- ScandiQA-da -->
   <td class="no ner">77.72 ± 1.59 / 57.89 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">71.70 ± 2.52 / 50.78 ± 2.60</td> <!-- NorNE-nn -->
   <td class="no sent">36.27 ± 1.67 / 35.73 ± 0.92</td> <!-- NoReC -->
   <td class="no la">71.70 ± 2.39 / 85.59 ± 1.30</td> <!-- ScaLA-nb -->
   <td class="no la">58.79 ± 1.33 / 76.83 ± 0.92</td> <!-- ScaLA-nn -->
   <td class="no rc">40.95 ± 1.31 / 72.82 ± 0.88</td> <!-- NorQuAD -->
   <td class="sv ner">75.06 ± 2.26 / 44.92 ± 1.50</td> <!-- SUC3 -->
   <td class="sv sent">74.85 ± 2.89 / 74.58 ± 2.54</td> <!-- SweReC -->
   <td class="sv la">65.23 ± 2.16 / 80.52 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.02 ± 1.40 / 63.85 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="is ner">72.85 ± 2.10 / 33.36 ± 1.59</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">53.43 ± 2.20 / 66.07 ± 1.59</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">49.26 ± 4.89 / 73.99 ± 2.32</td> <!-- ScaLA-is -->
   <td class="is rc">27.36 ± 0.94 / 48.73 ± 0.97</td> <!-- NQiI -->
   <td class="fo ner">68.00 ± 1.08 / 37.75 ± 1.09</td> <!-- FoNE -->
   <td class="fo sent">27.30 ± 4.69 / 30.12 ± 3.11</td> <!-- FoSent -->
   <td class="fo la">28.09 ± 3.31 / 54.91 ± 2.24</td> <!-- ScaLA-fo -->
   <td class="fo rc">58.59 ± 1.88 / 77.38 ± 1.63</td> <!-- FoQA -->
   <td class="de ner">67.18 ± 1.47 / 35.10 ± 1.57</td> <!-- GermEval -->
   <td class="de sent">50.12 ± 2.00 / 65.79 ± 1.25</td> <!-- SB10k -->
   <td class="de la">44.98 ± 4.97 / 71.63 ± 2.39</td> <!-- ScaLA-de -->
   <td class="de rc">27.01 ± 1.67 / 55.19 ± 1.49</td> <!-- GermanQuAD -->
   <td class="nl ner">69.12 ± 2.60 / 41.51 ± 2.79</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.36 ± 2.16 / 19.95 ± 1.34</td> <!-- Dutch Social -->
   <td class="nl la">58.88 ± 2.34 / 79.01 ± 1.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.88 ± 1.32 / 70.93 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="en ner">81.23 ± 1.31 / 72.72 ± 1.69</td> <!-- CoNLL-en -->
   <td class="en sent">63.46 ± 1.00 / 69.35 ± 1.28</td> <!-- SST5 -->
   <td class="en la">46.45 ± 4.58 / 72.89 ± 2.30</td> <!-- ScaLA-en -->
   <td class="en rc">57.64 ± 1.26 / 81.53 ± 0.66</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.0.3</td> <!-- NorNE-nb version -->
   <td>14.0.3</td> <!-- NorNE-nn version -->
   <td>14.0.3</td> <!-- NoReC version -->
   <td>14.0.3</td> <!-- ScaLA-nb version -->
   <td>14.0.3</td> <!-- ScaLA-nn version -->
   <td>14.0.3</td> <!-- NorQuAD version -->
   <td>14.0.3</td> <!-- SUC3 version -->
   <td>14.0.3</td> <!-- SweReC version -->
   <td>14.0.3</td> <!-- ScaLA-sv version -->
   <td>14.0.3</td> <!-- ScandiQA-sv version -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   <td>14.0.3</td> <!-- GermEval version -->
   <td>14.0.3</td> <!-- SB10k version -->
   <td>14.0.3</td> <!-- ScaLA-de version -->
   <td>14.0.3</td> <!-- GermanQuAD version -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="da-rank">1.53</td> <!-- Danish rank -->
   <td class="no-rank">1.49</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.37</td> <!-- Swedish rank -->
   <td class="is-rank">2.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.19</td> <!-- Faroese rank -->
   <td class="de-rank">1.32</td> <!-- German rank -->
   <td class="nl-rank">1.35</td> <!-- Dutch rank -->
   <td class="en-rank">1.30</td> <!-- English rank -->
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
   <td class="is sent">48.52 ± 1.18 / 64.38 ± 1.18</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">10.78 ± 7.04 / 53.28 ± 3.97</td> <!-- ScaLA-is -->
   <td class="is rc">13.79 ± 0.96 / 54.20 ± 1.31</td> <!-- NQiI -->
   <td class="fo ner">88.39 ± 0.86 / 88.75 ± 0.75</td> <!-- FoNE -->
   <td class="fo sent">18.28 ± 3.38 / 39.08 ± 2.62</td> <!-- FoSent -->
   <td class="fo la">2.85 ± 1.32 / 48.43 ± 2.29</td> <!-- ScaLA-fo -->
   <td class="fo rc">31.03 ± 1.94 / 43.72 ± 2.89</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="da-rank">1.77</td> <!-- Danish rank -->
   <td class="no-rank">1.59</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.53</td> <!-- Swedish rank -->
   <td class="is-rank">2.06</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.70</td> <!-- Faroese rank -->
   <td class="de-rank">1.51</td> <!-- German rank -->
   <td class="nl-rank">1.43</td> <!-- Dutch rank -->
   <td class="en-rank">1.59</td> <!-- English rank -->
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
   <td class="is sent">46.40 ± 1.18 / 63.25 ± 0.79</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">36.92 ± 7.62 / 66.07 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is rc">11.75 ± 0.66 / 46.17 ± 1.42</td> <!-- NQiI -->
   <td class="fo ner">89.16 ± 0.66 / 89.62 ± 0.62</td> <!-- FoNE -->
   <td class="fo sent">21.57 ± 4.96 / 45.40 ± 4.23</td> <!-- FoSent -->
   <td class="fo la">22.76 ± 10.57 / 60.04 ± 5.76</td> <!-- ScaLA-fo -->
   <td class="fo rc">30.55 ± 1.05 / 41.85 ± 1.13</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>claude-3-5-sonnet-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">193 ± 87 / 55 ± 19</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="da-rank">1.29</td> <!-- Danish rank -->
   <td class="no-rank">1.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.36</td> <!-- Swedish rank -->
   <td class="is-rank">1.70</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.55</td> <!-- Faroese rank -->
   <td class="de-rank">1.81</td> <!-- German rank -->
   <td class="nl-rank">2.37</td> <!-- Dutch rank -->
   <td class="en-rank">1.53</td> <!-- English rank -->
   <td class="da ner">65.88 ± 2.11 / 55.11 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">63.61 ± 1.57 / 76.00 ± 1.07</td> <!-- Angry Tweets -->
   <td class="da la">71.03 ± 2.52 / 85.46 ± 1.24</td> <!-- ScaLA-da -->
   <td class="da rc">46.24 ± 1.37 / 59.56 ± 1.25</td> <!-- ScandiQA-da -->
   <td class="no ner">74.23 ± 1.86 / 70.66 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">70.50 ± 2.19 / 65.71 ± 2.34</td> <!-- NorNE-nn -->
   <td class="no sent">50.92 ± 2.29 / 63.00 ± 1.71</td> <!-- NoReC -->
   <td class="no la">76.10 ± 3.28 / 88.02 ± 1.64</td> <!-- ScaLA-nb -->
   <td class="no la">72.03 ± 2.05 / 85.28 ± 1.07</td> <!-- ScaLA-nn -->
   <td class="no rc">40.57 ± 1.42 / 67.69 ± 0.75</td> <!-- NorQuAD -->
   <td class="sv ner">70.22 ± 2.34 / 58.75 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">77.70 ± 2.39 / 77.22 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">74.34 ± 2.79 / 87.04 ± 1.39</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.32 ± 1.33 / 60.05 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="is ner">61.70 ± 2.37 / 41.44 ± 1.76</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">51.24 ± 1.69 / 65.49 ± 1.06</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">52.43 ± 2.29 / 73.78 ± 1.09</td> <!-- ScaLA-is -->
   <td class="is rc">22.92 ± 1.06 / 47.06 ± 1.02</td> <!-- NQiI -->
   <td class="fo ner">72.52 ± 0.65 / 60.99 ± 0.78</td> <!-- FoNE -->
   <td class="fo sent">8.17 ± 5.22 / 27.16 ± 4.39</td> <!-- FoSent -->
   <td class="fo la">32.38 ± 4.28 / 56.38 ± 2.60</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.34 ± 1.90 / 69.24 ± 1.30</td> <!-- FoQA -->
   <td class="de ner">61.83 ± 1.50 / 46.40 ± 1.54</td> <!-- GermEval -->
   <td class="de sent">61.59 ± 4.13 / 73.65 ± 2.62</td> <!-- SB10k -->
   <td class="de la">46.40 ± 3.16 / 69.51 ± 1.58</td> <!-- ScaLA-de -->
   <td class="de rc">23.77 ± 1.57 / 48.70 ± 1.26</td> <!-- GermanQuAD -->
   <td class="nl ner">62.41 ± 2.92 / 52.27 ± 2.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.64 ± 2.16 / 33.98 ± 1.59</td> <!-- Dutch Social -->
   <td class="nl la">74.06 ± 2.21 / 86.59 ± 1.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">35.77 ± 1.20 / 68.02 ± 1.47</td> <!-- SQuAD-nl -->
   <td class="en ner">82.11 ± 1.42 / 79.77 ± 1.03</td> <!-- CoNLL-en -->
   <td class="en sent">67.01 ± 2.34 / 71.49 ± 1.89</td> <!-- SST5 -->
   <td class="en la">51.09 ± 5.20 / 74.48 ± 2.70</td> <!-- ScaLA-en -->
   <td class="en rc">52.41 ± 1.56 / 77.79 ± 1.01</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.0.3</td> <!-- NorNE-nb version -->
   <td>14.0.3</td> <!-- NorNE-nn version -->
   <td>14.0.3</td> <!-- NoReC version -->
   <td>14.0.3</td> <!-- ScaLA-nb version -->
   <td>14.0.3</td> <!-- ScaLA-nn version -->
   <td>14.0.3</td> <!-- NorQuAD version -->
   <td>14.0.3</td> <!-- SUC3 version -->
   <td>14.0.3</td> <!-- SweReC version -->
   <td>14.0.3</td> <!-- ScaLA-sv version -->
   <td>14.0.3</td> <!-- ScandiQA-sv version -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   <td>14.0.3</td> <!-- GermEval version -->
   <td>14.0.3</td> <!-- SB10k version -->
   <td>14.0.3</td> <!-- ScaLA-de version -->
   <td>14.0.3</td> <!-- GermanQuAD version -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="da-rank">1.41</td> <!-- Danish rank -->
   <td class="no-rank">1.96</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.50</td> <!-- Swedish rank -->
   <td class="is-rank">2.27</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.11</td> <!-- Faroese rank -->
   <td class="de-rank">1.68</td> <!-- German rank -->
   <td class="nl-rank">2.36</td> <!-- Dutch rank -->
   <td class="en-rank">1.46</td> <!-- English rank -->
   <td class="da ner">66.50 ± 2.00 / 45.33 ± 2.92</td> <!-- DANSK -->
   <td class="da sent">58.93 ± 1.72 / 72.70 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">57.27 ± 1.30 / 78.52 ± 0.62</td> <!-- ScaLA-da -->
   <td class="da rc">55.02 ± 0.88 / 64.14 ± 0.46</td> <!-- ScandiQA-da -->
   <td class="no ner">76.25 ± 1.39 / 60.31 ± 3.22</td> <!-- NorNE-nb -->
   <td class="no ner">77.91 ± 0.47 / 61.81 ± 3.84</td> <!-- NorNE-nn -->
   <td class="no sent">40.54 ± 0.72 / 39.96 ± 0.60</td> <!-- NoReC -->
   <td class="no la">59.75 ± 1.66 / 78.91 ± 1.21</td> <!-- ScaLA-nb -->
   <td class="no la">47.82 ± 2.00 / 73.51 ± 1.21</td> <!-- ScaLA-nn -->
   <td class="no rc">40.99 ± 1.38 / 69.77 ± 1.17</td> <!-- NorQuAD -->
   <td class="sv ner">62.91 ± 1.46 / 47.13 ± 3.48</td> <!-- SUC3 -->
   <td class="sv sent">79.51 ± 0.63 / 79.57 ± 0.65</td> <!-- SweReC -->
   <td class="sv la">60.28 ± 1.19 / 79.99 ± 0.66</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.44 ± 0.92 / 64.81 ± 0.62</td> <!-- ScandiQA-sv -->
   <td class="is ner">67.23 ± 2.77 / 45.61 ± 4.86</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">50.38 ± 1.18 / 66.21 ± 1.00</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">20.01 ± 1.09 / 59.74 ± 0.60</td> <!-- ScaLA-is -->
   <td class="is rc">21.18 ± 1.67 / 49.26 ± 0.93</td> <!-- NQiI -->
   <td class="fo ner">81.30 ± 1.24 / 73.31 ± 3.51</td> <!-- FoNE -->
   <td class="fo sent">60.99 ± 2.59 / 72.95 ± 1.68</td> <!-- FoSent -->
   <td class="fo la">12.49 ± 3.30 / 49.82 ± 2.65</td> <!-- ScaLA-fo -->
   <td class="fo rc">48.47 ± 1.72 / 70.99 ± 1.42</td> <!-- FoQA -->
   <td class="de ner">73.31 ± 1.01 / 59.78 ± 2.14</td> <!-- GermEval -->
   <td class="de sent">58.02 ± 1.62 / 71.81 ± 1.10</td> <!-- SB10k -->
   <td class="de la">45.12 ± 0.99 / 70.92 ± 0.38</td> <!-- ScaLA-de -->
   <td class="de rc">24.67 ± 1.03 / 55.19 ± 1.27</td> <!-- GermanQuAD -->
   <td class="nl ner">68.17 ± 1.75 / 51.61 ± 2.73</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.56 ± 1.04 / 19.29 ± 0.63</td> <!-- Dutch Social -->
   <td class="nl la">56.89 ± 0.82 / 78.31 ± 0.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.05 ± 2.18 / 71.82 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="en ner">81.06 ± 0.87 / 75.22 ± 1.31</td> <!-- CoNLL-en -->
   <td class="en sent">68.92 ± 1.04 / 72.90 ± 0.74</td> <!-- SST5 -->
   <td class="en la">49.06 ± 1.46 / 72.52 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">61.27 ± 1.63 / 81.48 ± 0.86</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.0.4</td> <!-- Angry Tweets version -->
   <td>14.0.4</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.0.4</td> <!-- NoReC version -->
   <td>14.0.4</td> <!-- ScaLA-nb version -->
   <td>14.0.4</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.0.4</td> <!-- SB10k version -->
   <td>14.0.4</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="da-rank">1.79</td> <!-- Danish rank -->
   <td class="no-rank">1.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.45</td> <!-- Swedish rank -->
   <td class="is-rank">2.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.09</td> <!-- Faroese rank -->
   <td class="de-rank">1.32</td> <!-- German rank -->
   <td class="nl-rank">1.61</td> <!-- Dutch rank -->
   <td class="en-rank">1.26</td> <!-- English rank -->
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
   <td class="is sent">50.10 ± 1.59 / 64.91 ± 2.07</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">8.11 ± 3.77 / 50.71 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">13.93 ± 1.14 / 53.59 ± 1.62</td> <!-- NQiI -->
   <td class="fo ner">88.64 ± 0.34 / 89.11 ± 0.29</td> <!-- FoNE -->
   <td class="fo sent">23.63 ± 6.26 / 44.37 ± 7.53</td> <!-- FoSent -->
   <td class="fo la">2.05 ± 2.30 / 47.88 ± 2.17</td> <!-- ScaLA-fo -->
   <td class="fo rc">24.09 ± 4.66 / 37.60 ± 4.39</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="da-rank">1.60</td> <!-- Danish rank -->
   <td class="no-rank">1.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.52</td> <!-- Swedish rank -->
   <td class="is-rank">2.09</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.58</td> <!-- Faroese rank -->
   <td class="de-rank">1.22</td> <!-- German rank -->
   <td class="nl-rank">2.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.71</td> <!-- English rank -->
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
   <td class="is sent">48.41 ± 6.83 / 64.09 ± 6.26</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">22.78 ± 12.25 / 57.07 ± 8.18</td> <!-- ScaLA-is -->
   <td class="is rc">15.72 ± 1.39 / 55.29 ± 1.30</td> <!-- NQiI -->
   <td class="fo ner">87.85 ± 0.95 / 88.21 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">5.14 ± 5.42 / 22.03 ± 5.69</td> <!-- FoSent -->
   <td class="fo la">1.17 ± 2.11 / 40.94 ± 5.07</td> <!-- ScaLA-fo -->
   <td class="fo rc">27.72 ± 1.48 / 39.88 ± 2.04</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>gpt-4o-mini-2024-07-18 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">784 ± 310 / 95 ± 28</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="da-rank">1.91</td> <!-- Danish rank -->
   <td class="no-rank">2.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
   <td class="is-rank">1.84</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.59</td> <!-- Faroese rank -->
   <td class="de-rank">1.87</td> <!-- German rank -->
   <td class="nl-rank">2.29</td> <!-- Dutch rank -->
   <td class="en-rank">1.62</td> <!-- English rank -->
   <td class="da ner">59.96 ± 1.64 / 41.55 ± 2.90</td> <!-- DANSK -->
   <td class="da sent">56.91 ± 2.34 / 71.25 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">67.13 ± 4.29 / 83.05 ± 2.24</td> <!-- ScaLA-da -->
   <td class="da rc">17.52 ± 2.69 / 33.63 ± 2.10</td> <!-- ScandiQA-da -->
   <td class="no ner">72.74 ± 1.75 / 57.58 ± 4.14</td> <!-- NorNE-nb -->
   <td class="no ner">69.17 ± 2.61 / 56.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">67.45 ± 4.03 / 77.50 ± 2.90</td> <!-- NoReC -->
   <td class="no la">74.27 ± 2.57 / 86.86 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">54.83 ± 3.96 / 76.91 ± 1.98</td> <!-- ScaLA-nn -->
   <td class="no rc">3.67 ± 1.64 / 43.45 ± 1.90</td> <!-- NorQuAD -->
   <td class="sv ner">62.45 ± 2.79 / 46.68 ± 4.08</td> <!-- SUC3 -->
   <td class="sv sent">77.69 ± 2.28 / 78.73 ± 2.17</td> <!-- SweReC -->
   <td class="sv la">68.93 ± 3.67 / 84.15 ± 2.01</td> <!-- ScaLA-sv -->
   <td class="sv rc">12.11 ± 4.65 / 31.14 ± 3.37</td> <!-- ScandiQA-sv -->
   <td class="is ner">64.69 ± 1.77 / 37.89 ± 3.23</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">56.18 ± 4.37 / 69.53 ± 2.97</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">45.52 ± 4.15 / 71.51 ± 2.48</td> <!-- ScaLA-is -->
   <td class="is rc">15.80 ± 6.24 / 55.19 ± 4.14</td> <!-- NQiI -->
   <td class="fo ner">73.80 ± 2.44 / 63.06 ± 3.84</td> <!-- FoNE -->
   <td class="fo sent">39.45 ± 8.53 / 62.38 ± 6.69</td> <!-- FoSent -->
   <td class="fo la">34.78 ± 4.81 / 63.14 ± 2.83</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.87 ± 1.17 / 19.37 ± 1.52</td> <!-- FoQA -->
   <td class="de ner">65.51 ± 1.91 / 48.61 ± 3.73</td> <!-- GermEval -->
   <td class="de sent">55.16 ± 3.05 / 69.81 ± 1.96</td> <!-- SB10k -->
   <td class="de la">44.60 ± 3.19 / 67.35 ± 2.53</td> <!-- ScaLA-de -->
   <td class="de rc">21.87 ± 3.80 / 59.67 ± 2.67</td> <!-- GermanQuAD -->
   <td class="nl ner">68.71 ± 3.85 / 53.19 ± 4.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">20.33 ± 2.51 / 40.68 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">49.52 ± 5.39 / 72.59 ± 3.64</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.06 ± 3.24 / 61.15 ± 2.69</td> <!-- SQuAD-nl -->
   <td class="en ner">77.38 ± 1.61 / 66.97 ± 2.42</td> <!-- CoNLL-en -->
   <td class="en sent">66.75 ± 2.50 / 73.93 ± 1.51</td> <!-- SST5 -->
   <td class="en la">52.43 ± 3.69 / 74.46 ± 2.17</td> <!-- ScaLA-en -->
   <td class="en rc">41.03 ± 6.90 / 67.96 ± 4.99</td> <!-- SQuAD -->
   <td>14.0.0</td> <!-- DANSK version -->
   <td>14.0.0</td> <!-- Angry Tweets version -->
   <td>14.0.0</td> <!-- ScaLA-da version -->
   <td>14.0.0</td> <!-- ScandiQA-da version -->
   <td>14.0.0</td> <!-- NorNE-nb version -->
   <td>14.0.0</td> <!-- NorNE-nn version -->
   <td>14.0.0</td> <!-- NoReC version -->
   <td>14.0.0</td> <!-- ScaLA-nb version -->
   <td>14.0.0</td> <!-- ScaLA-nn version -->
   <td>14.0.0</td> <!-- NorQuAD version -->
   <td>14.0.0</td> <!-- SUC3 version -->
   <td>14.0.0</td> <!-- SweReC version -->
   <td>14.0.0</td> <!-- ScaLA-sv version -->
   <td>14.0.0</td> <!-- ScandiQA-sv version -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.0</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.0</td> <!-- FoNE version -->
   <td>14.0.0</td> <!-- FoSent version -->
   <td>14.0.0</td> <!-- ScaLA-fo version -->
   <td>14.0.0</td> <!-- FoQA version -->
   <td>14.0.0</td> <!-- GermEval version -->
   <td>14.0.0</td> <!-- SB10k version -->
   <td>14.0.0</td> <!-- ScaLA-de version -->
   <td>14.0.0</td> <!-- GermanQuAD version -->
   <td>14.0.0</td> <!-- CoNLL-nl version -->
   <td>14.0.0</td> <!-- Dutch Social version -->
   <td>14.0.0</td> <!-- ScaLA-nl version -->
   <td>14.0.0</td> <!-- SQuAD-nl version -->
   <td>14.0.0</td> <!-- CoNLL-en version -->
   <td>14.0.0</td> <!-- SST5 version -->
   <td>14.0.0</td> <!-- ScaLA-en version -->
   <td>14.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">436 ± 152 / 57 ± 21</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="da-rank">1.83</td> <!-- Danish rank -->
   <td class="no-rank">2.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.67</td> <!-- Swedish rank -->
   <td class="is-rank">2.05</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.73</td> <!-- Faroese rank -->
   <td class="de-rank">1.69</td> <!-- German rank -->
   <td class="nl-rank">2.29</td> <!-- Dutch rank -->
   <td class="en-rank">1.96</td> <!-- English rank -->
   <td class="da ner">35.79 ± 2.45 / 25.86 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">53.69 ± 2.27 / 67.91 ± 1.55</td> <!-- Angry Tweets -->
   <td class="da la">62.98 ± 2.61 / 81.27 ± 1.31</td> <!-- ScaLA-da -->
   <td class="da rc">51.96 ± 1.07 / 64.87 ± 0.92</td> <!-- ScandiQA-da -->
   <td class="no ner">60.16 ± 3.63 / 49.38 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">48.74 ± 2.05 / 40.98 ± 1.83</td> <!-- NorNE-nn -->
   <td class="no sent">39.62 ± 1.29 / 38.68 ± 0.94</td> <!-- NoReC -->
   <td class="no la">71.38 ± 2.71 / 85.52 ± 1.38</td> <!-- ScaLA-nb -->
   <td class="no la">42.94 ± 3.66 / 71.26 ± 1.76</td> <!-- ScaLA-nn -->
   <td class="no rc">36.04 ± 1.53 / 69.46 ± 0.84</td> <!-- NorQuAD -->
   <td class="sv ner">51.31 ± 4.64 / 43.84 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">73.54 ± 3.03 / 68.68 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">66.39 ± 2.24 / 82.10 ± 1.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.22 ± 1.51 / 63.21 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="is ner">30.39 ± 3.49 / 25.88 ± 1.98</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">47.47 ± 3.03 / 63.45 ± 2.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">43.30 ± 3.41 / 71.54 ± 1.71</td> <!-- ScaLA-is -->
   <td class="is rc">29.82 ± 1.09 / 51.48 ± 0.89</td> <!-- NQiI -->
   <td class="fo ner">57.52 ± 2.17 / 36.36 ± 1.53</td> <!-- FoNE -->
   <td class="fo sent">13.18 ± 5.13 / 19.41 ± 3.41</td> <!-- FoSent -->
   <td class="fo la">28.03 ± 3.90 / 62.26 ± 2.03</td> <!-- ScaLA-fo -->
   <td class="fo rc">59.06 ± 2.40 / 76.65 ± 1.98</td> <!-- FoQA -->
   <td class="de ner">57.47 ± 2.20 / 36.29 ± 1.91</td> <!-- GermEval -->
   <td class="de sent">58.67 ± 2.30 / 71.20 ± 1.34</td> <!-- SB10k -->
   <td class="de la">54.55 ± 3.18 / 75.08 ± 1.71</td> <!-- ScaLA-de -->
   <td class="de rc">27.02 ± 1.33 / 53.97 ± 1.74</td> <!-- GermanQuAD -->
   <td class="nl ner">55.72 ± 3.68 / 40.53 ± 2.95</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.13 ± 1.98 / 18.38 ± 1.21</td> <!-- Dutch Social -->
   <td class="nl la">67.28 ± 2.42 / 83.06 ± 1.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 2.18 / 72.73 ± 1.79</td> <!-- SQuAD-nl -->
   <td class="en ner">42.40 ± 2.22 / 34.09 ± 2.02</td> <!-- CoNLL-en -->
   <td class="en sent">65.24 ± 2.14 / 72.51 ± 1.77</td> <!-- SST5 -->
   <td class="en la">44.59 ± 4.02 / 71.93 ± 2.06</td> <!-- ScaLA-en -->
   <td class="en rc">62.94 ± 1.37 / 82.84 ± 0.53</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.0.3</td> <!-- NorNE-nb version -->
   <td>14.0.3</td> <!-- NorNE-nn version -->
   <td>14.0.3</td> <!-- NoReC version -->
   <td>14.0.3</td> <!-- ScaLA-nb version -->
   <td>14.0.3</td> <!-- ScaLA-nn version -->
   <td>14.0.3</td> <!-- NorQuAD version -->
   <td>14.0.3</td> <!-- SUC3 version -->
   <td>14.0.3</td> <!-- SweReC version -->
   <td>14.0.3</td> <!-- ScaLA-sv version -->
   <td>14.0.3</td> <!-- ScandiQA-sv version -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   <td>14.0.3</td> <!-- GermEval version -->
   <td>14.0.3</td> <!-- SB10k version -->
   <td>14.0.3</td> <!-- ScaLA-de version -->
   <td>14.0.3</td> <!-- GermanQuAD version -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">908 ± 303 / 96 ± 36</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="da-rank">1.70</td> <!-- Danish rank -->
   <td class="no-rank">2.41</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.85</td> <!-- Swedish rank -->
   <td class="is-rank">2.27</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.47</td> <!-- Faroese rank -->
   <td class="de-rank">1.90</td> <!-- German rank -->
   <td class="nl-rank">2.32</td> <!-- Dutch rank -->
   <td class="en-rank">1.65</td> <!-- English rank -->
   <td class="da ner">57.52 ± 2.21 / 35.79 ± 1.78</td> <!-- DANSK -->
   <td class="da sent">49.73 ± 3.09 / 65.95 ± 2.22</td> <!-- Angry Tweets -->
   <td class="da la">57.56 ± 2.67 / 77.16 ± 1.35</td> <!-- ScaLA-da -->
   <td class="da rc">51.79 ± 1.50 / 64.34 ± 1.32</td> <!-- ScandiQA-da -->
   <td class="no ner">60.43 ± 2.46 / 37.82 ± 2.68</td> <!-- NorNE-nb -->
   <td class="no ner">55.59 ± 2.84 / 32.20 ± 2.11</td> <!-- NorNE-nn -->
   <td class="no sent">39.82 ± 1.20 / 37.70 ± 1.08</td> <!-- NoReC -->
   <td class="no la">54.84 ± 2.09 / 74.79 ± 1.33</td> <!-- ScaLA-nb -->
   <td class="no la">33.80 ± 3.42 / 62.11 ± 2.19</td> <!-- ScaLA-nn -->
   <td class="no rc">36.55 ± 1.71 / 70.12 ± 0.99</td> <!-- NorQuAD -->
   <td class="sv ner">52.47 ± 2.22 / 29.74 ± 0.97</td> <!-- SUC3 -->
   <td class="sv sent">73.55 ± 2.73 / 71.66 ± 2.30</td> <!-- SweReC -->
   <td class="sv la">52.27 ± 2.34 / 71.55 ± 1.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.95 ± 1.41 / 61.75 ± 1.16</td> <!-- ScandiQA-sv -->
   <td class="is ner">31.11 ± 2.16 / 14.28 ± 0.85</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">50.02 ± 2.61 / 65.44 ± 1.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">35.85 ± 1.55 / 66.14 ± 0.82</td> <!-- ScaLA-is -->
   <td class="is rc">26.93 ± 1.10 / 49.25 ± 1.18</td> <!-- NQiI -->
   <td class="fo ner">53.92 ± 1.55 / 28.59 ± 1.28</td> <!-- FoNE -->
   <td class="fo sent">35.05 ± 3.84 / 34.41 ± 2.93</td> <!-- FoSent -->
   <td class="fo la">23.12 ± 4.18 / 60.20 ± 2.01</td> <!-- ScaLA-fo -->
   <td class="fo rc">54.99 ± 2.45 / 76.60 ± 1.29</td> <!-- FoQA -->
   <td class="de ner">59.19 ± 1.52 / 30.16 ± 1.22</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 3.86 / 68.10 ± 2.51</td> <!-- SB10k -->
   <td class="de la">46.66 ± 4.45 / 72.82 ± 2.13</td> <!-- ScaLA-de -->
   <td class="de rc">26.02 ± 1.78 / 51.63 ± 1.54</td> <!-- GermanQuAD -->
   <td class="nl ner">64.15 ± 2.49 / 38.77 ± 2.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.67 ± 2.02 / 18.63 ± 1.37</td> <!-- Dutch Social -->
   <td class="nl la">62.44 ± 3.24 / 80.58 ± 1.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.65 ± 1.56 / 70.43 ± 1.29</td> <!-- SQuAD-nl -->
   <td class="en ner">75.80 ± 0.83 / 52.95 ± 1.04</td> <!-- CoNLL-en -->
   <td class="en sent">61.65 ± 2.17 / 71.46 ± 1.72</td> <!-- SST5 -->
   <td class="en la">47.74 ± 4.29 / 73.28 ± 2.23</td> <!-- ScaLA-en -->
   <td class="en rc">56.98 ± 1.46 / 79.90 ± 0.76</td> <!-- SQuAD -->
   <td>14.0.1</td> <!-- DANSK version -->
   <td>14.0.1</td> <!-- Angry Tweets version -->
   <td>14.0.1</td> <!-- ScaLA-da version -->
   <td>14.0.1</td> <!-- ScandiQA-da version -->
   <td>14.0.1</td> <!-- NorNE-nb version -->
   <td>14.0.1</td> <!-- NorNE-nn version -->
   <td>14.0.1</td> <!-- NoReC version -->
   <td>14.0.1</td> <!-- ScaLA-nb version -->
   <td>14.0.1</td> <!-- ScaLA-nn version -->
   <td>14.0.1</td> <!-- NorQuAD version -->
   <td>14.0.1</td> <!-- SUC3 version -->
   <td>14.0.1</td> <!-- SweReC version -->
   <td>14.0.1</td> <!-- ScaLA-sv version -->
   <td>14.0.1</td> <!-- ScandiQA-sv version -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.1</td> <!-- FoNE version -->
   <td>14.0.1</td> <!-- FoSent version -->
   <td>14.0.1</td> <!-- ScaLA-fo version -->
   <td>14.0.1</td> <!-- FoQA version -->
   <td>14.0.1</td> <!-- GermEval version -->
   <td>14.0.1</td> <!-- SB10k version -->
   <td>14.0.1</td> <!-- ScaLA-de version -->
   <td>14.0.1</td> <!-- GermanQuAD version -->
   <td>14.0.1</td> <!-- CoNLL-nl version -->
   <td>14.0.1</td> <!-- Dutch Social version -->
   <td>14.0.1</td> <!-- ScaLA-nl version -->
   <td>14.0.1</td> <!-- SQuAD-nl version -->
   <td>14.0.1</td> <!-- CoNLL-en version -->
   <td>14.0.1</td> <!-- SST5 version -->
   <td>14.0.1</td> <!-- ScaLA-en version -->
   <td>14.0.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="da-rank">1.86</td> <!-- Danish rank -->
   <td class="no-rank">2.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.64</td> <!-- Swedish rank -->
   <td class="is-rank">2.56</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.34</td> <!-- Faroese rank -->
   <td class="de-rank">1.79</td> <!-- German rank -->
   <td class="nl-rank">1.98</td> <!-- Dutch rank -->
   <td class="en-rank">1.50</td> <!-- English rank -->
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
   <td class="is sent">42.08 ± 1.98 / 59.90 ± 1.47</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">15.21 ± 8.62 / 54.40 ± 5.57</td> <!-- ScaLA-is -->
   <td class="is rc">10.82 ± 0.92 / 43.65 ± 2.51</td> <!-- NQiI -->
   <td class="fo ner">87.44 ± 0.35 / 88.01 ± 0.28</td> <!-- FoNE -->
   <td class="fo sent">10.97 ± 3.84 / 30.74 ± 5.68</td> <!-- FoSent -->
   <td class="fo la">7.38 ± 6.28 / 47.69 ± 4.51</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.80 ± 3.56 / 22.12 ± 5.23</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="da-rank">1.30</td> <!-- Danish rank -->
   <td class="no-rank">1.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.17</td> <!-- Swedish rank -->
   <td class="is-rank">2.87</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.41</td> <!-- Faroese rank -->
   <td class="de-rank">2.62</td> <!-- German rank -->
   <td class="nl-rank">3.29</td> <!-- Dutch rank -->
   <td class="en-rank">1.34</td> <!-- English rank -->
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
   <td class="is sent">38.53 ± 2.56 / 56.94 ± 2.26</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.06 ± 2.43 / 37.04 ± 4.14</td> <!-- ScaLA-is -->
   <td class="is rc">11.47 ± 0.96 / 48.11 ± 0.94</td> <!-- NQiI -->
   <td class="fo ner">88.24 ± 0.58 / 88.48 ± 0.54</td> <!-- FoNE -->
   <td class="fo sent">6.42 ± 5.53 / 24.34 ± 7.55</td> <!-- FoSent -->
   <td class="fo la">1.73 ± 1.70 / 42.32 ± 5.16</td> <!-- ScaLA-fo -->
   <td class="fo rc">35.08 ± 2.58 / 47.03 ± 3.42</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>10.0.1</td> <!-- ScaLA-is version -->
   <td>10.0.1</td> <!-- NQiI version -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,007 ± 316 / 162 ± 45</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="da-rank">2.12</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.04</td> <!-- Swedish rank -->
   <td class="is-rank">2.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.60</td> <!-- Faroese rank -->
   <td class="de-rank">1.82</td> <!-- German rank -->
   <td class="nl-rank">2.56</td> <!-- Dutch rank -->
   <td class="en-rank">1.78</td> <!-- English rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da rc">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="no ner">74.47 ± 1.47 / 65.57 ± 2.39</td> <!-- NorNE-nb -->
   <td class="no ner">72.93 ± 1.00 / 65.44 ± 2.55</td> <!-- NorNE-nn -->
   <td class="no sent">34.44 ± 0.42 / 37.94 ± 0.39</td> <!-- NoReC -->
   <td class="no la">27.77 ± 1.63 / 61.75 ± 1.77</td> <!-- ScaLA-nb -->
   <td class="no la">20.35 ± 1.92 / 57.74 ± 2.28</td> <!-- ScaLA-nn -->
   <td class="no rc">42.90 ± 3.57 / 69.90 ± 3.17</td> <!-- NorQuAD -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="is ner">60.20 ± 2.76 / 40.38 ± 4.22</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">38.09 ± 2.38 / 54.51 ± 2.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">9.14 ± 0.98 / 49.56 ± 2.11</td> <!-- ScaLA-is -->
   <td class="is rc">28.66 ± 1.28 / 58.93 ± 1.41</td> <!-- NQiI -->
   <td class="fo ner">70.61 ± 1.12 / 68.27 ± 1.76</td> <!-- FoNE -->
   <td class="fo sent">45.78 ± 2.05 / 47.72 ± 1.15</td> <!-- FoSent -->
   <td class="fo la">4.58 ± 2.43 / 36.78 ± 1.86</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.67 ± 1.56 / 72.73 ± 1.11</td> <!-- FoQA -->
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
   <td>14.0.4</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
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
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,005 ± 330 / 196 ± 74</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da-rank">1.95</td> <!-- Danish rank -->
   <td class="no-rank">2.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.97</td> <!-- Swedish rank -->
   <td class="is-rank">2.61</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.73</td> <!-- Faroese rank -->
   <td class="de-rank">1.85</td> <!-- German rank -->
   <td class="nl-rank">2.70</td> <!-- Dutch rank -->
   <td class="en-rank">1.81</td> <!-- English rank -->
   <td class="da ner">54.70 ± 1.69 / 38.11 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">54.81 ± 1.51 / 67.88 ± 1.39</td> <!-- Angry Tweets -->
   <td class="da la">32.11 ± 1.93 / 63.11 ± 1.61</td> <!-- ScaLA-da -->
   <td class="da rc">48.87 ± 1.18 / 59.47 ± 0.67</td> <!-- ScandiQA-da -->
   <td class="no ner">64.55 ± 1.69 / 56.81 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">66.44 ± 1.38 / 60.02 ± 3.36</td> <!-- NorNE-nn -->
   <td class="no sent">35.17 ± 0.32 / 38.11 ± 0.29</td> <!-- NoReC -->
   <td class="no la">27.41 ± 1.97 / 54.94 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">15.60 ± 2.05 / 46.51 ± 2.41</td> <!-- ScaLA-nn -->
   <td class="no rc">43.11 ± 2.22 / 69.74 ± 1.60</td> <!-- NorQuAD -->
   <td class="sv ner">55.80 ± 2.68 / 34.65 ± 1.98</td> <!-- SUC3 -->
   <td class="sv sent">79.23 ± 0.48 / 76.86 ± 0.80</td> <!-- SweReC -->
   <td class="sv la">32.67 ± 2.18 / 63.89 ± 1.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.88 ± 1.47 / 58.66 ± 0.84</td> <!-- ScandiQA-sv -->
   <td class="is ner">46.48 ± 1.98 / 24.57 ± 1.73</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">39.91 ± 2.35 / 57.39 ± 1.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">11.72 ± 1.81 / 51.67 ± 1.45</td> <!-- ScaLA-is -->
   <td class="is rc">25.91 ± 0.99 / 53.39 ± 1.83</td> <!-- NQiI -->
   <td class="fo ner">67.67 ± 1.31 / 59.86 ± 2.12</td> <!-- FoNE -->
   <td class="fo sent">48.54 ± 2.43 / 49.17 ± 1.48</td> <!-- FoSent -->
   <td class="fo la">3.89 ± 2.71 / 36.33 ± 1.50</td> <!-- ScaLA-fo -->
   <td class="fo rc">47.07 ± 2.63 / 69.50 ± 1.68</td> <!-- FoQA -->
   <td class="de ner">67.61 ± 1.23 / 60.39 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">58.07 ± 2.32 / 70.76 ± 1.84</td> <!-- SB10k -->
   <td class="de la">28.25 ± 3.57 / 59.54 ± 3.88</td> <!-- ScaLA-de -->
   <td class="de rc">28.79 ± 2.02 / 55.82 ± 3.28</td> <!-- GermanQuAD -->
   <td class="nl ner">69.76 ± 1.36 / 57.66 ± 1.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.09 ± 1.42 / 20.14 ± 0.84</td> <!-- Dutch Social -->
   <td class="nl la">37.58 ± 3.42 / 66.98 ± 2.22</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.26 ± 2.09 / 65.63 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="en ner">76.95 ± 0.95 / 72.47 ± 0.82</td> <!-- CoNLL-en -->
   <td class="en sent">68.12 ± 0.92 / 72.48 ± 0.53</td> <!-- SST5 -->
   <td class="en la">34.34 ± 3.37 / 65.84 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en rc">47.88 ± 3.37 / 76.21 ± 1.69</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.1.2</td> <!-- NorNE-nb version -->
   <td>14.1.2</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.1.2</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.1</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.1</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>14.0.4</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.32</td> <!-- Danish rank -->
   <td class="no-rank">2.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.92</td> <!-- Swedish rank -->
   <td class="is-rank">2.86</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.51</td> <!-- Faroese rank -->
   <td class="de-rank">2.12</td> <!-- German rank -->
   <td class="nl-rank">1.87</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
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
   <td class="is sent">46.33 ± 1.12 / 62.80 ± 1.39</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.47 ± 1.14 / 47.14 ± 3.33</td> <!-- ScaLA-is -->
   <td class="is rc">7.67 ± 0.80 / 32.31 ± 0.81</td> <!-- NQiI -->
   <td class="fo ner">84.14 ± 0.67 / 84.82 ± 0.64</td> <!-- FoNE -->
   <td class="fo sent">21.20 ± 3.85 / 43.97 ± 3.72</td> <!-- FoSent -->
   <td class="fo la">1.33 ± 2.18 / 48.85 ± 1.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.20 ± 1.78 / 22.95 ± 2.71</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,986 ± 823 / 276 ± 94</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.70</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.99</td> <!-- Swedish rank -->
   <td class="is-rank">2.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.19</td> <!-- Faroese rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.45</td> <!-- Dutch rank -->
   <td class="en-rank">1.73</td> <!-- English rank -->
   <td class="da ner">50.92 ± 1.88 / 34.24 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">47.86 ± 1.66 / 62.47 ± 1.97</td> <!-- Angry Tweets -->
   <td class="da la">29.19 ± 2.02 / 59.61 ± 3.20</td> <!-- ScaLA-da -->
   <td class="da rc">48.38 ± 5.07 / 55.27 ± 4.71</td> <!-- ScandiQA-da -->
   <td class="no ner">65.17 ± 2.02 / 52.91 ± 2.25</td> <!-- NorNE-nb -->
   <td class="no ner">60.22 ± 2.29 / 50.51 ± 3.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.02 ± 0.93 / 37.19 ± 0.86</td> <!-- NoReC -->
   <td class="no la">32.48 ± 3.31 / 63.48 ± 2.97</td> <!-- ScaLA-nb -->
   <td class="no la">18.38 ± 4.77 / 49.87 ± 5.55</td> <!-- ScaLA-nn -->
   <td class="no rc">33.06 ± 4.39 / 58.56 ± 4.32</td> <!-- NorQuAD -->
   <td class="sv ner">62.19 ± 2.34 / 43.29 ± 4.62</td> <!-- SUC3 -->
   <td class="sv sent">80.31 ± 0.45 / 76.50 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">30.29 ± 3.08 / 56.52 ± 4.71</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.78 ± 7.55 / 49.56 ± 7.91</td> <!-- ScandiQA-sv -->
   <td class="is ner">52.97 ± 1.54 / 38.17 ± 4.65</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">41.29 ± 2.30 / 59.30 ± 1.75</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">5.95 ± 2.81 / 40.86 ± 3.68</td> <!-- ScaLA-is -->
   <td class="is rc">31.99 ± 2.60 / 60.26 ± 1.51</td> <!-- NQiI -->
   <td class="fo ner">65.65 ± 3.31 / 63.81 ± 2.72</td> <!-- FoNE -->
   <td class="fo sent">24.30 ± 7.03 / 35.85 ± 7.35</td> <!-- FoSent -->
   <td class="fo la">0.61 ± 1.75 / 35.51 ± 2.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.01 ± 1.79 / 65.74 ± 1.54</td> <!-- FoQA -->
   <td class="de ner">59.45 ± 1.64 / 46.60 ± 2.02</td> <!-- GermEval -->
   <td class="de sent">53.39 ± 5.35 / 65.74 ± 5.74</td> <!-- SB10k -->
   <td class="de la">23.87 ± 5.74 / 57.17 ± 6.01</td> <!-- ScaLA-de -->
   <td class="de rc">34.85 ± 3.43 / 64.05 ± 3.68</td> <!-- GermanQuAD -->
   <td class="nl ner">64.79 ± 1.96 / 45.48 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.83 / 37.12 ± 2.19</td> <!-- Dutch Social -->
   <td class="nl la">32.97 ± 2.68 / 58.52 ± 2.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.89 ± 1.06 / 74.73 ± 1.02</td> <!-- SQuAD-nl -->
   <td class="en ner">69.86 ± 2.10 / 62.68 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">66.76 ± 0.72 / 68.58 ± 0.72</td> <!-- SST5 -->
   <td class="en la">30.96 ± 2.46 / 61.29 ± 3.61</td> <!-- ScaLA-en -->
   <td class="en rc">71.39 ± 2.20 / 84.24 ± 1.55</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.1.2</td> <!-- NorNE-nb version -->
   <td>14.1.2</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.1.2</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
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
   <td class="speed">1,335 ± 338 / 260 ± 88</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.97</td> <!-- Swedish rank -->
   <td class="is-rank">2.56</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.27</td> <!-- Faroese rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.58</td> <!-- Dutch rank -->
   <td class="en-rank">1.81</td> <!-- English rank -->
   <td class="da ner">49.46 ± 1.88 / 32.11 ± 2.41</td> <!-- DANSK -->
   <td class="da sent">51.16 ± 2.15 / 67.00 ± 1.51</td> <!-- Angry Tweets -->
   <td class="da la">23.01 ± 3.93 / 49.99 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da rc">49.75 ± 5.10 / 56.13 ± 4.89</td> <!-- ScandiQA-da -->
   <td class="no ner">61.48 ± 1.83 / 47.65 ± 2.94</td> <!-- NorNE-nb -->
   <td class="no ner">61.58 ± 2.21 / 50.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">32.94 ± 0.86 / 37.52 ± 0.43</td> <!-- NoReC -->
   <td class="no la">21.20 ± 6.57 / 52.29 ± 7.43</td> <!-- ScaLA-nb -->
   <td class="no la">19.65 ± 4.32 / 56.66 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no rc">53.35 ± 4.33 / 74.98 ± 3.70</td> <!-- NorQuAD -->
   <td class="sv ner">59.92 ± 2.46 / 40.98 ± 4.90</td> <!-- SUC3 -->
   <td class="sv sent">80.91 ± 0.41 / 78.09 ± 1.22</td> <!-- SweReC -->
   <td class="sv la">26.39 ± 3.47 / 52.38 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.69 ± 6.29 / 54.30 ± 6.65</td> <!-- ScandiQA-sv -->
   <td class="is ner">50.45 ± 1.95 / 37.62 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">34.68 ± 3.74 / 53.39 ± 3.75</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">8.69 ± 2.70 / 44.84 ± 4.03</td> <!-- ScaLA-is -->
   <td class="is rc">31.94 ± 2.16 / 59.26 ± 1.50</td> <!-- NQiI -->
   <td class="fo ner">61.11 ± 4.21 / 58.55 ± 4.19</td> <!-- FoNE -->
   <td class="fo sent">19.40 ± 8.13 / 32.14 ± 7.75</td> <!-- FoSent -->
   <td class="fo la">2.02 ± 1.68 / 39.88 ± 3.56</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.34 ± 1.74 / 71.74 ± 1.27</td> <!-- FoQA -->
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
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.1</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,302 ± 323 / 253 ± 86</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.20</td> <!-- Danish rank -->
   <td class="no-rank">2.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.08</td> <!-- Swedish rank -->
   <td class="is-rank">2.80</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.11</td> <!-- Faroese rank -->
   <td class="de-rank">2.03</td> <!-- German rank -->
   <td class="nl-rank">2.45</td> <!-- Dutch rank -->
   <td class="en-rank">1.67</td> <!-- English rank -->
   <td class="da ner">55.49 ± 2.05 / 34.11 ± 1.79</td> <!-- DANSK -->
   <td class="da sent">49.18 ± 1.89 / 65.27 ± 1.69</td> <!-- Angry Tweets -->
   <td class="da la">7.40 ± 1.81 / 35.19 ± 0.73</td> <!-- ScaLA-da -->
   <td class="da rc">57.72 ± 0.54 / 64.99 ± 0.45</td> <!-- ScandiQA-da -->
   <td class="no ner">67.24 ± 1.06 / 45.38 ± 2.20</td> <!-- NorNE-nb -->
   <td class="no ner">66.08 ± 1.05 / 47.58 ± 3.27</td> <!-- NorNE-nn -->
   <td class="no sent">31.41 ± 0.86 / 33.56 ± 0.97</td> <!-- NoReC -->
   <td class="no la">28.72 ± 2.42 / 58.62 ± 3.68</td> <!-- ScaLA-nb -->
   <td class="no la">20.55 ± 3.71 / 54.24 ± 4.15</td> <!-- ScaLA-nn -->
   <td class="no rc">40.60 ± 2.39 / 68.91 ± 2.08</td> <!-- NorQuAD -->
   <td class="sv ner">54.76 ± 1.82 / 31.21 ± 2.67</td> <!-- SUC3 -->
   <td class="sv sent">73.32 ± 1.59 / 75.58 ± 1.15</td> <!-- SweReC -->
   <td class="sv la">16.17 ± 2.98 / 42.93 ± 2.72</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.94 ± 0.58 / 65.27 ± 0.58</td> <!-- ScandiQA-sv -->
   <td class="is ner">47.10 ± 1.90 / 22.63 ± 2.03</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">24.43 ± 2.98 / 39.27 ± 3.37</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">7.19 ± 2.76 / 44.62 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">28.73 ± 1.45 / 54.38 ± 2.28</td> <!-- NQiI -->
   <td class="fo ner">65.55 ± 1.39 / 51.57 ± 3.35</td> <!-- FoNE -->
   <td class="fo sent">29.49 ± 2.40 / 47.06 ± 2.82</td> <!-- FoSent -->
   <td class="fo la">2.05 ± 1.58 / 35.92 ± 2.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">47.72 ± 2.10 / 65.78 ± 1.43</td> <!-- FoQA -->
   <td class="de ner">60.50 ± 1.22 / 40.72 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">50.39 ± 2.45 / 66.39 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.86 ± 1.37 / 53.78 ± 1.61</td> <!-- ScaLA-de -->
   <td class="de rc">30.53 ± 1.21 / 58.26 ± 1.93</td> <!-- GermanQuAD -->
   <td class="nl ner">66.51 ± 1.38 / 52.40 ± 2.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.91 ± 1.03 / 34.21 ± 1.08</td> <!-- Dutch Social -->
   <td class="nl la">34.46 ± 2.79 / 65.61 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.23 ± 1.16 / 72.56 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="en ner">72.40 ± 0.80 / 65.83 ± 1.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.46 ± 2.10 / 69.49 ± 1.15</td> <!-- SST5 -->
   <td class="en la">35.86 ± 7.94 / 65.20 ± 6.98</td> <!-- ScaLA-en -->
   <td class="en rc">68.42 ± 1.21 / 83.97 ± 0.74</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>14.1.2</td> <!-- NorNE-nb version -->
   <td>14.1.2</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.1.2</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.0</td> <!-- ScaLA-is version -->
   <td>14.0.0</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.1.2</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
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
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,136 ± 1,282 / 668 ± 326</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da-rank">2.22</td> <!-- Danish rank -->
   <td class="no-rank">2.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="is-rank">3.09</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.49</td> <!-- Faroese rank -->
   <td class="de-rank">2.17</td> <!-- German rank -->
   <td class="nl-rank">2.64</td> <!-- Dutch rank -->
   <td class="en-rank">1.62</td> <!-- English rank -->
   <td class="da ner">51.94 ± 2.00 / 27.59 ± 1.79</td> <!-- DANSK -->
   <td class="da sent">51.97 ± 1.36 / 68.62 ± 0.93</td> <!-- Angry Tweets -->
   <td class="da la">29.99 ± 0.73 / 60.05 ± 1.33</td> <!-- ScaLA-da -->
   <td class="da rc">38.99 ± 2.82 / 52.38 ± 2.25</td> <!-- ScandiQA-da -->
   <td class="no ner">66.22 ± 2.15 / 48.98 ± 4.65</td> <!-- NorNE-nb -->
   <td class="no ner">64.14 ± 1.26 / 49.59 ± 4.31</td> <!-- NorNE-nn -->
   <td class="no sent">55.48 ± 1.77 / 69.68 ± 1.45</td> <!-- NoReC -->
   <td class="no la">26.13 ± 1.28 / 56.08 ± 2.05</td> <!-- ScaLA-nb -->
   <td class="no la">17.32 ± 0.77 / 54.57 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no rc">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td class="sv ner">56.28 ± 1.55 / 28.71 ± 3.39</td> <!-- SUC3 -->
   <td class="sv sent">77.51 ± 0.55 / 76.88 ± 0.58</td> <!-- SweReC -->
   <td class="sv la">23.25 ± 2.19 / 50.00 ± 2.40</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.09 ± 2.61 / 59.76 ± 2.06</td> <!-- ScandiQA-sv -->
   <td class="is ner">42.23 ± 4.22 / 25.96 ± 4.27</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">27.93 ± 2.80 / 48.93 ± 1.43</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">6.38 ± 0.99 / 49.63 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is rc">19.39 ± 3.38 / 53.87 ± 1.59</td> <!-- NQiI -->
   <td class="fo ner">62.20 ± 1.42 / 45.92 ± 2.03</td> <!-- FoNE -->
   <td class="fo sent">26.68 ± 6.93 / 47.94 ± 8.20</td> <!-- FoSent -->
   <td class="fo la">7.07 ± 2.30 / 44.94 ± 2.71</td> <!-- ScaLA-fo -->
   <td class="fo rc">11.97 ± 3.61 / 31.80 ± 3.65</td> <!-- FoQA -->
   <td class="de ner">61.37 ± 1.04 / 36.06 ± 2.27</td> <!-- GermEval -->
   <td class="de sent">51.38 ± 2.17 / 67.66 ± 1.45</td> <!-- SB10k -->
   <td class="de la">35.58 ± 1.85 / 66.99 ± 0.83</td> <!-- ScaLA-de -->
   <td class="de rc">19.92 ± 3.88 / 57.70 ± 2.99</td> <!-- GermanQuAD -->
   <td class="nl ner">62.86 ± 2.07 / 33.76 ± 1.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.11 ± 1.83 / 40.18 ± 1.61</td> <!-- Dutch Social -->
   <td class="nl la">39.11 ± 1.22 / 68.00 ± 1.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">36.48 ± 2.80 / 59.22 ± 2.19</td> <!-- SQuAD-nl -->
   <td class="en ner">72.77 ± 1.02 / 57.29 ± 1.58</td> <!-- CoNLL-en -->
   <td class="en sent">70.12 ± 0.78 / 74.54 ± 0.50</td> <!-- SST5 -->
   <td class="en la">44.68 ± 0.97 / 71.05 ± 0.52</td> <!-- ScaLA-en -->
   <td class="en rc">57.17 ± 2.60 / 80.36 ± 1.40</td> <!-- SQuAD -->
   <td>14.0.3</td> <!-- DANSK version -->
   <td>14.0.3</td> <!-- Angry Tweets version -->
   <td>14.0.3</td> <!-- ScaLA-da version -->
   <td>14.0.3</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.1.2</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da-rank">2.09</td> <!-- Danish rank -->
   <td class="no-rank">2.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.84</td> <!-- Swedish rank -->
   <td class="is-rank">2.62</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.98</td> <!-- Faroese rank -->
   <td class="de-rank">2.26</td> <!-- German rank -->
   <td class="nl-rank">2.34</td> <!-- Dutch rank -->
   <td class="en-rank">2.23</td> <!-- English rank -->
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
   <td class="is sent">35.62 ± 1.32 / 55.40 ± 1.15</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">28.72 ± 5.29 / 60.29 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">8.46 ± 0.51 / 31.01 ± 0.72</td> <!-- NQiI -->
   <td class="fo ner">83.96 ± 0.80 / 84.63 ± 0.76</td> <!-- FoNE -->
   <td class="fo sent">5.16 ± 3.25 / 23.12 ± 4.48</td> <!-- FoSent -->
   <td class="fo la">1.05 ± 1.66 / 41.31 ± 4.91</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,686 ± 685 / 491 ± 164</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.60</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.06</td> <!-- Swedish rank -->
   <td class="is-rank">3.19</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.15</td> <!-- Faroese rank -->
   <td class="de-rank">2.07</td> <!-- German rank -->
   <td class="nl-rank">2.53</td> <!-- Dutch rank -->
   <td class="en-rank">1.78</td> <!-- English rank -->
   <td class="da ner">51.32 ± 3.82 / 25.54 ± 2.10</td> <!-- DANSK -->
   <td class="da sent">52.00 ± 1.67 / 66.25 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">18.48 ± 2.44 / 52.18 ± 4.28</td> <!-- ScaLA-da -->
   <td class="da rc">52.43 ± 1.19 / 62.08 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="no ner">66.55 ± 2.12 / 39.28 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">63.63 ± 1.62 / 37.25 ± 3.49</td> <!-- NorNE-nn -->
   <td class="no sent">38.61 ± 2.28 / 51.46 ± 2.62</td> <!-- NoReC -->
   <td class="no la">15.80 ± 2.22 / 51.42 ± 3.79</td> <!-- ScaLA-nb -->
   <td class="no la">12.30 ± 2.38 / 51.96 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no rc">43.26 ± 2.53 / 71.49 ± 2.01</td> <!-- NorQuAD -->
   <td class="sv ner">57.38 ± 1.93 / 29.69 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">78.43 ± 0.93 / 74.54 ± 2.40</td> <!-- SweReC -->
   <td class="sv la">14.52 ± 2.43 / 45.18 ± 4.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.14 ± 1.81 / 63.00 ± 0.50</td> <!-- ScandiQA-sv -->
   <td class="is ner">28.98 ± 2.63 / 21.75 ± 1.89</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">19.83 ± 4.76 / 41.64 ± 3.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">4.93 ± 1.06 / 49.69 ± 2.65</td> <!-- ScaLA-is -->
   <td class="is rc">24.72 ± 2.22 / 54.41 ± 1.43</td> <!-- NQiI -->
   <td class="fo ner">64.72 ± 1.73 / 47.25 ± 4.90</td> <!-- FoNE -->
   <td class="fo sent">28.57 ± 4.08 / 50.22 ± 2.92</td> <!-- FoSent -->
   <td class="fo la">5.12 ± 1.16 / 51.09 ± 0.89</td> <!-- ScaLA-fo -->
   <td class="fo rc">38.83 ± 3.81 / 56.89 ± 3.51</td> <!-- FoQA -->
   <td class="de ner">59.95 ± 1.43 / 39.14 ± 2.24</td> <!-- GermEval -->
   <td class="de sent">55.39 ± 1.97 / 69.86 ± 1.34</td> <!-- SB10k -->
   <td class="de la">30.59 ± 1.76 / 64.21 ± 1.65</td> <!-- ScaLA-de -->
   <td class="de rc">26.94 ± 1.06 / 57.13 ± 1.35</td> <!-- GermanQuAD -->
   <td class="nl ner">62.07 ± 1.67 / 37.68 ± 1.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.70 ± 1.36 / 34.90 ± 0.68</td> <!-- Dutch Social -->
   <td class="nl la">35.14 ± 2.33 / 66.66 ± 1.50</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.48 / 68.82 ± 0.68</td> <!-- SQuAD-nl -->
   <td class="en ner">67.33 ± 1.57 / 53.00 ± 0.88</td> <!-- CoNLL-en -->
   <td class="en sent">68.67 ± 0.74 / 66.23 ± 0.49</td> <!-- SST5 -->
   <td class="en la">31.18 ± 1.63 / 65.23 ± 0.69</td> <!-- ScaLA-en -->
   <td class="en rc">68.33 ± 2.04 / 84.26 ± 1.04</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.1.2</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,446 ± 354 / 295 ± 100</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.09</td> <!-- Swedish rank -->
   <td class="is-rank">2.85</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.15</td> <!-- Faroese rank -->
   <td class="de-rank">2.05</td> <!-- German rank -->
   <td class="nl-rank">2.75</td> <!-- Dutch rank -->
   <td class="en-rank">1.74</td> <!-- English rank -->
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
   <td class="is ner">50.69 ± 3.67 / 41.90 ± 4.06</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">24.38 ± 5.21 / 44.65 ± 5.83</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.46 ± 1.66 / 38.73 ± 2.27</td> <!-- ScaLA-is -->
   <td class="is rc">27.11 ± 3.11 / 51.14 ± 2.22</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo sent">25.57 ± 6.07 / 44.34 ± 6.18</td> <!-- FoSent -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td class="fo rc">44.06 ± 1.93 / 60.40 ± 2.37</td> <!-- FoQA -->
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
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>9.1.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>9.1.2</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">2.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.11</td> <!-- Swedish rank -->
   <td class="is-rank">3.30</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.24</td> <!-- Faroese rank -->
   <td class="de-rank">2.12</td> <!-- German rank -->
   <td class="nl-rank">2.66</td> <!-- Dutch rank -->
   <td class="en-rank">1.66</td> <!-- English rank -->
   <td class="da ner">44.92 ± 3.05 / 32.65 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">49.31 ± 1.35 / 66.02 ± 1.10</td> <!-- Angry Tweets -->
   <td class="da la">10.14 ± 2.87 / 44.99 ± 4.82</td> <!-- ScaLA-da -->
   <td class="da rc">57.34 ± 0.99 / 63.24 ± 0.44</td> <!-- ScandiQA-da -->
   <td class="no ner">53.79 ± 1.52 / 46.58 ± 1.73</td> <!-- NorNE-nb -->
   <td class="no ner">56.13 ± 0.91 / 47.13 ± 2.04</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 2.53 / 66.19 ± 2.08</td> <!-- NoReC -->
   <td class="no la">6.83 ± 2.54 / 38.36 ± 3.81</td> <!-- ScaLA-nb -->
   <td class="no la">8.09 ± 2.03 / 41.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no rc">48.01 ± 2.52 / 73.03 ± 1.99</td> <!-- NorQuAD -->
   <td class="sv ner">44.94 ± 2.91 / 35.67 ± 3.53</td> <!-- SUC3 -->
   <td class="sv sent">76.78 ± 1.63 / 78.27 ± 1.22</td> <!-- SweReC -->
   <td class="sv la">16.96 ± 2.77 / 55.03 ± 3.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.83 ± 1.02 / 63.13 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="is ner">42.67 ± 3.13 / 35.40 ± 3.93</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.95 ± 3.78 / 30.20 ± 5.91</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.11 ± 1.45 / 34.61 ± 0.82</td> <!-- ScaLA-is -->
   <td class="is rc">22.25 ± 2.78 / 49.58 ± 2.19</td> <!-- NQiI -->
   <td class="fo ner">59.96 ± 2.42 / 58.61 ± 2.57</td> <!-- FoNE -->
   <td class="fo sent">28.33 ± 7.70 / 49.72 ± 6.84</td> <!-- FoSent -->
   <td class="fo la">2.24 ± 1.78 / 41.32 ± 3.70</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.52 ± 1.83 / 57.16 ± 2.10</td> <!-- FoQA -->
   <td class="de ner">54.68 ± 1.38 / 46.36 ± 2.67</td> <!-- GermEval -->
   <td class="de sent">55.48 ± 2.67 / 69.91 ± 1.90</td> <!-- SB10k -->
   <td class="de la">26.89 ± 0.86 / 62.51 ± 0.48</td> <!-- ScaLA-de -->
   <td class="de rc">31.27 ± 1.89 / 62.30 ± 2.09</td> <!-- GermanQuAD -->
   <td class="nl ner">53.62 ± 2.29 / 40.51 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.37 ± 1.25 / 36.94 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">23.47 ± 1.79 / 60.17 ± 1.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.20 ± 1.02 / 72.98 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="en ner">66.17 ± 1.74 / 57.76 ± 1.30</td> <!-- CoNLL-en -->
   <td class="en sent">68.03 ± 0.81 / 69.65 ± 1.18</td> <!-- SST5 -->
   <td class="en la">39.76 ± 2.51 / 69.54 ± 1.18</td> <!-- ScaLA-en -->
   <td class="en rc">71.21 ± 1.53 / 84.07 ± 0.91</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,364 ± 343 / 266 ± 90</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.31</td> <!-- Danish rank -->
   <td class="no-rank">2.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.10</td> <!-- Swedish rank -->
   <td class="is-rank">2.97</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.26</td> <!-- Faroese rank -->
   <td class="de-rank">2.13</td> <!-- German rank -->
   <td class="nl-rank">2.91</td> <!-- Dutch rank -->
   <td class="en-rank">1.81</td> <!-- English rank -->
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
   <td class="is ner">46.73 ± 3.51 / 38.01 ± 4.18</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">26.28 ± 4.82 / 46.42 ± 4.24</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.50 ± 1.18 / 36.24 ± 1.65</td> <!-- ScaLA-is -->
   <td class="is rc">25.17 ± 3.82 / 50.14 ± 2.43</td> <!-- NQiI -->
   <td class="fo ner">61.32 ± 4.26 / 59.28 ± 4.43</td> <!-- FoNE -->
   <td class="fo sent">26.73 ± 4.70 / 45.03 ± 5.25</td> <!-- FoSent -->
   <td class="fo la">1.30 ± 1.64 / 45.10 ± 3.27</td> <!-- ScaLA-fo -->
   <td class="fo rc">44.98 ± 1.62 / 62.38 ± 1.68</td> <!-- FoQA -->
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
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.11</td> <!-- Danish rank -->
   <td class="no-rank">2.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.05</td> <!-- Swedish rank -->
   <td class="is-rank">3.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.24</td> <!-- Faroese rank -->
   <td class="de-rank">2.11</td> <!-- German rank -->
   <td class="nl-rank">2.63</td> <!-- Dutch rank -->
   <td class="en-rank">2.10</td> <!-- English rank -->
   <td class="da ner">34.00 ± 2.69 / 25.49 ± 2.06</td> <!-- DANSK -->
   <td class="da sent">53.97 ± 1.21 / 68.40 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">32.21 ± 4.81 / 56.97 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da rc">57.10 ± 0.99 / 63.73 ± 0.85</td> <!-- ScandiQA-da -->
   <td class="no ner">40.91 ± 2.56 / 33.22 ± 1.88</td> <!-- NorNE-nb -->
   <td class="no ner">42.91 ± 2.34 / 35.61 ± 2.22</td> <!-- NorNE-nn -->
   <td class="no sent">52.62 ± 2.01 / 68.10 ± 2.25</td> <!-- NoReC -->
   <td class="no la">9.70 ± 4.22 / 36.58 ± 1.69</td> <!-- ScaLA-nb -->
   <td class="no la">11.98 ± 2.76 / 39.37 ± 2.76</td> <!-- ScaLA-nn -->
   <td class="no rc">47.36 ± 4.28 / 72.71 ± 4.10</td> <!-- NorQuAD -->
   <td class="sv ner">40.59 ± 1.98 / 28.19 ± 1.47</td> <!-- SUC3 -->
   <td class="sv sent">76.02 ± 2.40 / 77.86 ± 1.70</td> <!-- SweReC -->
   <td class="sv la">33.98 ± 5.90 / 57.44 ± 6.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.98 ± 0.58 / 63.97 ± 0.66</td> <!-- ScandiQA-sv -->
   <td class="is ner">24.92 ± 3.54 / 23.09 ± 3.30</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">9.76 ± 7.16 / 26.68 ± 6.80</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.15 ± 0.29 / 33.01 ± 0.31</td> <!-- ScaLA-is -->
   <td class="is rc">28.18 ± 1.51 / 54.08 ± 0.71</td> <!-- NQiI -->
   <td class="fo ner">54.79 ± 2.33 / 46.30 ± 4.57</td> <!-- FoNE -->
   <td class="fo sent">35.84 ± 8.64 / 48.22 ± 7.58</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.54</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.94 ± 2.59 / 62.06 ± 2.17</td> <!-- FoQA -->
   <td class="de ner">40.85 ± 2.21 / 34.64 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">56.53 ± 2.49 / 69.48 ± 1.70</td> <!-- SB10k -->
   <td class="de la">24.74 ± 4.45 / 56.60 ± 5.56</td> <!-- ScaLA-de -->
   <td class="de rc">38.20 ± 1.47 / 67.94 ± 2.19</td> <!-- GermanQuAD -->
   <td class="nl ner">43.06 ± 1.89 / 30.50 ± 1.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.25 / 33.40 ± 1.41</td> <!-- Dutch Social -->
   <td class="nl la">40.85 ± 3.31 / 68.94 ± 2.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.42 ± 0.63 / 74.62 ± 0.52</td> <!-- SQuAD-nl -->
   <td class="en ner">44.81 ± 2.07 / 39.51 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.54 ± 2.18 / 68.78 ± 1.18</td> <!-- SST5 -->
   <td class="en la">28.10 ± 4.55 / 62.46 ± 4.36</td> <!-- ScaLA-en -->
   <td class="en rc">71.71 ± 2.21 / 84.31 ± 1.69</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 625 / 476 ± 159</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.03</td> <!-- Swedish rank -->
   <td class="is-rank">3.54</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.30</td> <!-- Faroese rank -->
   <td class="de-rank">2.22</td> <!-- German rank -->
   <td class="nl-rank">2.79</td> <!-- Dutch rank -->
   <td class="en-rank">1.84</td> <!-- English rank -->
   <td class="da ner">44.58 ± 2.62 / 33.50 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.36 / 64.63 ± 1.18</td> <!-- Angry Tweets -->
   <td class="da la">19.20 ± 2.44 / 53.44 ± 4.36</td> <!-- ScaLA-da -->
   <td class="da rc">58.41 ± 1.36 / 63.32 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="no ner">49.94 ± 2.13 / 46.49 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">52.17 ± 1.02 / 46.44 ± 2.72</td> <!-- NorNE-nn -->
   <td class="no sent">53.27 ± 1.54 / 66.73 ± 1.31</td> <!-- NoReC -->
   <td class="no la">17.22 ± 3.50 / 50.42 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">12.01 ± 2.47 / 47.98 ± 4.37</td> <!-- ScaLA-nn -->
   <td class="no rc">45.04 ± 3.42 / 69.52 ± 2.79</td> <!-- NorQuAD -->
   <td class="sv ner">44.80 ± 2.36 / 34.91 ± 2.67</td> <!-- SUC3 -->
   <td class="sv sent">75.92 ± 2.44 / 75.77 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">24.84 ± 2.78 / 59.88 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.71 ± 1.65 / 62.01 ± 1.64</td> <!-- ScandiQA-sv -->
   <td class="is ner">37.82 ± 3.63 / 32.97 ± 3.97</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.29 ± 1.16 / 15.66 ± 0.37</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.12 ± 1.31 / 33.78 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">21.59 ± 2.22 / 47.09 ± 1.09</td> <!-- NQiI -->
   <td class="fo ner">61.47 ± 1.57 / 58.60 ± 2.31</td> <!-- FoNE -->
   <td class="fo sent">24.35 ± 6.38 / 30.32 ± 5.04</td> <!-- FoSent -->
   <td class="fo la">1.44 ± 1.85 / 34.71 ± 1.84</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.54 ± 1.49 / 58.90 ± 1.24</td> <!-- FoQA -->
   <td class="de ner">50.43 ± 1.80 / 41.26 ± 3.08</td> <!-- GermEval -->
   <td class="de sent">57.84 ± 3.59 / 71.20 ± 2.77</td> <!-- SB10k -->
   <td class="de la">22.58 ± 5.59 / 53.17 ± 6.23</td> <!-- ScaLA-de -->
   <td class="de rc">27.96 ± 1.39 / 54.99 ± 1.75</td> <!-- GermanQuAD -->
   <td class="nl ner">52.26 ± 1.87 / 42.18 ± 1.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.46 ± 1.09 / 21.30 ± 0.67</td> <!-- Dutch Social -->
   <td class="nl la">42.42 ± 3.42 / 68.81 ± 2.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.11 ± 1.79 / 63.80 ± 1.61</td> <!-- SQuAD-nl -->
   <td class="en ner">55.76 ± 2.15 / 52.69 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">66.89 ± 1.11 / 69.52 ± 0.94</td> <!-- SST5 -->
   <td class="en la">36.60 ± 2.37 / 67.85 ± 1.19</td> <!-- ScaLA-en -->
   <td class="en rc">67.55 ± 1.46 / 80.25 ± 1.22</td> <!-- SQuAD -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.1.2</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="da-rank">2.24</td> <!-- Danish rank -->
   <td class="no-rank">2.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.21</td> <!-- Swedish rank -->
   <td class="is-rank">3.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="de-rank">2.10</td> <!-- German rank -->
   <td class="nl-rank">2.59</td> <!-- Dutch rank -->
   <td class="en-rank">1.94</td> <!-- English rank -->
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
   <td class="is sent">7.92 ± 3.63 / 32.79 ± 2.05</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="fo ner">67.42 ± 2.21 / 60.87 ± 3.22</td> <!-- FoNE -->
   <td class="fo sent">20.01 ± 4.67 / 38.23 ± 3.04</td> <!-- FoSent -->
   <td class="fo la">7.02 ± 1.56 / 49.32 ± 2.91</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.65 ± 0.17 / 7.03 ± 0.26</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.15</td> <!-- Swedish rank -->
   <td class="is-rank">2.79</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.94</td> <!-- Faroese rank -->
   <td class="de-rank">2.12</td> <!-- German rank -->
   <td class="nl-rank">2.71</td> <!-- Dutch rank -->
   <td class="en-rank">2.64</td> <!-- English rank -->
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
   <td class="is sent">38.76 ± 2.04 / 56.09 ± 2.02</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">5.92 ± 1.91 / 46.95 ± 3.38</td> <!-- ScaLA-is -->
   <td class="is rc">10.47 ± 1.42 / 43.32 ± 3.55</td> <!-- NQiI -->
   <td class="fo ner">85.97 ± 1.12 / 86.52 ± 1.08</td> <!-- FoNE -->
   <td class="fo sent">2.54 ± 4.09 / 19.42 ± 4.54</td> <!-- FoSent -->
   <td class="fo la">0.02 ± 1.38 / 44.65 ± 2.65</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.72 ± 0.93 / 1.00 ± 1.31</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,707 ± 688 / 497 ± 166</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.06</td> <!-- Swedish rank -->
   <td class="is-rank">3.39</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.48</td> <!-- Faroese rank -->
   <td class="de-rank">2.36</td> <!-- German rank -->
   <td class="nl-rank">2.65</td> <!-- Dutch rank -->
   <td class="en-rank">1.91</td> <!-- English rank -->
   <td class="da ner">47.08 ± 3.39 / 32.34 ± 2.97</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.21 / 63.47 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">8.41 ± 2.40 / 37.31 ± 1.66</td> <!-- ScaLA-da -->
   <td class="da rc">58.83 ± 0.73 / 63.96 ± 0.56</td> <!-- ScandiQA-da -->
   <td class="no ner">60.94 ± 2.30 / 53.33 ± 3.53</td> <!-- NorNE-nb -->
   <td class="no ner">59.61 ± 1.37 / 50.84 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">35.73 ± 1.26 / 50.42 ± 1.67</td> <!-- NoReC -->
   <td class="no la">6.18 ± 1.69 / 35.40 ± 1.06</td> <!-- ScaLA-nb -->
   <td class="no la">4.00 ± 1.01 / 36.17 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no rc">46.52 ± 2.15 / 71.95 ± 1.63</td> <!-- NorQuAD -->
   <td class="sv ner">60.04 ± 1.22 / 43.93 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 0.85 / 67.87 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">7.54 ± 2.52 / 35.42 ± 1.33</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.60 ± 0.59 / 63.65 ± 0.30</td> <!-- ScandiQA-sv -->
   <td class="is ner">47.16 ± 2.83 / 38.60 ± 4.04</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.33 ± 0.93 / 15.64 ± 1.01</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.84 ± 1.27 / 40.06 ± 3.79</td> <!-- ScaLA-is -->
   <td class="is rc">21.75 ± 2.21 / 48.25 ± 2.02</td> <!-- NQiI -->
   <td class="fo ner">62.22 ± 2.10 / 58.79 ± 2.20</td> <!-- FoNE -->
   <td class="fo sent">17.34 ± 5.56 / 37.16 ± 5.28</td> <!-- FoSent -->
   <td class="fo la">0.01 ± 2.43 / 37.74 ± 4.20</td> <!-- ScaLA-fo -->
   <td class="fo rc">38.70 ± 1.22 / 54.70 ± 0.93</td> <!-- FoQA -->
   <td class="de ner">51.20 ± 4.11 / 41.29 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">47.79 ± 3.34 / 64.03 ± 2.90</td> <!-- SB10k -->
   <td class="de la">18.04 ± 1.40 / 54.89 ± 2.23</td> <!-- ScaLA-de -->
   <td class="de rc">29.46 ± 1.12 / 55.85 ± 1.72</td> <!-- GermanQuAD -->
   <td class="nl ner">60.81 ± 1.94 / 46.59 ± 3.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.63 / 24.82 ± 0.95</td> <!-- Dutch Social -->
   <td class="nl la">31.12 ± 2.35 / 64.29 ± 1.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.00 ± 1.23 / 74.60 ± 0.67</td> <!-- SQuAD-nl -->
   <td class="en ner">56.16 ± 3.59 / 51.12 ± 2.58</td> <!-- CoNLL-en -->
   <td class="en sent">68.27 ± 0.53 / 60.37 ± 0.57</td> <!-- SST5 -->
   <td class="en la">23.82 ± 2.16 / 60.83 ± 1.63</td> <!-- ScaLA-en -->
   <td class="en rc">74.23 ± 1.31 / 85.11 ± 0.73</td> <!-- SQuAD -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   <td>14.1.2</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.1.2</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da-rank">2.43</td> <!-- Danish rank -->
   <td class="no-rank">2.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.02</td> <!-- Swedish rank -->
   <td class="is-rank">2.84</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.91</td> <!-- Faroese rank -->
   <td class="de-rank">2.25</td> <!-- German rank -->
   <td class="nl-rank">2.99</td> <!-- Dutch rank -->
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
   <td class="is sent">40.22 ± 1.03 / 58.56 ± 1.02</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">11.09 ± 6.94 / 51.60 ± 5.19</td> <!-- ScaLA-is -->
   <td class="is rc">7.67 ± 0.74 / 30.52 ± 0.52</td> <!-- NQiI -->
   <td class="fo ner">84.00 ± 1.30 / 84.83 ± 1.28</td> <!-- FoNE -->
   <td class="fo sent">3.05 ± 3.68 / 27.70 ± 4.19</td> <!-- FoSent -->
   <td class="fo la">1.94 ± 2.58 / 46.27 ± 2.74</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.02 ± 0.05 / 0.02 ± 0.05</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.23</td> <!-- Swedish rank -->
   <td class="is-rank">3.38</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.49</td> <!-- Faroese rank -->
   <td class="de-rank">2.28</td> <!-- German rank -->
   <td class="nl-rank">2.76</td> <!-- Dutch rank -->
   <td class="en-rank">1.86</td> <!-- English rank -->
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
   <td class="is sent">9.52 ± 4.25 / 29.57 ± 4.96</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.50 ± 0.94 / 33.77 ± 0.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.43 ± 3.38 / 41.32 ± 3.18</td> <!-- NQiI -->
   <td class="fo ner">66.82 ± 2.36 / 65.84 ± 2.35</td> <!-- FoNE -->
   <td class="fo sent">21.19 ± 5.19 / 32.96 ± 5.05</td> <!-- FoSent -->
   <td class="fo la">-0.36 ± 1.67 / 37.57 ± 3.35</td> <!-- ScaLA-fo -->
   <td class="fo rc">36.47 ± 0.96 / 51.89 ± 1.05</td> <!-- FoQA -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,370 ± 416 / 711 ± 242</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.34</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.15</td> <!-- Faroese rank -->
   <td class="de-rank">2.36</td> <!-- German rank -->
   <td class="nl-rank">2.83</td> <!-- Dutch rank -->
   <td class="en-rank">2.08</td> <!-- English rank -->
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
   <td class="is ner">34.80 ± 1.37 / 24.03 ± 2.32</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">17.64 ± 3.40 / 40.55 ± 3.17</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">5.46 ± 1.31 / 51.42 ± 1.10</td> <!-- ScaLA-is -->
   <td class="is rc">12.66 ± 2.33 / 45.06 ± 2.27</td> <!-- NQiI -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo sent">32.07 ± 3.55 / 51.69 ± 3.46</td> <!-- FoSent -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.00 ± 1.21 / 59.78 ± 1.14</td> <!-- FoQA -->
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
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.3</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.30</td> <!-- Danish rank -->
   <td class="no-rank">2.59</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.96</td> <!-- Swedish rank -->
   <td class="is-rank">3.49</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.71</td> <!-- Faroese rank -->
   <td class="de-rank">2.31</td> <!-- German rank -->
   <td class="nl-rank">3.06</td> <!-- Dutch rank -->
   <td class="en-rank">1.94</td> <!-- English rank -->
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
   <td class="is sent">1.84 ± 3.02 / 23.26 ± 3.53</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is rc">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="fo ner">58.96 ± 2.05 / 52.20 ± 2.50</td> <!-- FoNE -->
   <td class="fo sent">8.97 ± 6.97 / 27.85 ± 5.18</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.20 ± 1.10 / 54.89 ± 1.25</td> <!-- FoQA -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.5.3</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">2.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.25</td> <!-- Swedish rank -->
   <td class="is-rank">3.13</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.90</td> <!-- Faroese rank -->
   <td class="de-rank">2.57</td> <!-- German rank -->
   <td class="nl-rank">2.38</td> <!-- Dutch rank -->
   <td class="en-rank">2.23</td> <!-- English rank -->
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
   <td class="is sent">33.26 ± 1.68 / 52.59 ± 1.73</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.15 ± 1.57 / 49.60 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">9.56 ± 0.42 / 27.88 ± 0.44</td> <!-- NQiI -->
   <td class="fo ner">80.92 ± 0.59 / 81.63 ± 0.56</td> <!-- FoNE -->
   <td class="fo sent">12.97 ± 2.96 / 31.99 ± 2.53</td> <!-- FoSent -->
   <td class="fo la">1.19 ± 2.37 / 43.13 ± 4.70</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da-rank">2.52</td> <!-- Danish rank -->
   <td class="no-rank">2.68</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="is-rank">3.02</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.65</td> <!-- Faroese rank -->
   <td class="de-rank">2.54</td> <!-- German rank -->
   <td class="nl-rank">2.80</td> <!-- Dutch rank -->
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
   <td class="is sent">37.79 ± 2.49 / 56.10 ± 1.91</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.04 ± 0.78 / 45.96 ± 2.83</td> <!-- ScaLA-is -->
   <td class="is rc">10.04 ± 0.99 / 28.66 ± 0.92</td> <!-- NQiI -->
   <td class="fo ner">82.97 ± 0.83 / 83.62 ± 0.81</td> <!-- FoNE -->
   <td class="fo sent">18.07 ± 4.85 / 39.76 ± 3.32</td> <!-- FoSent -->
   <td class="fo la">2.93 ± 1.96 / 46.51 ± 4.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.56</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.25</td> <!-- Swedish rank -->
   <td class="is-rank">3.29</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.60</td> <!-- Faroese rank -->
   <td class="de-rank">2.24</td> <!-- German rank -->
   <td class="nl-rank">2.94</td> <!-- Dutch rank -->
   <td class="en-rank">2.07</td> <!-- English rank -->
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
   <td class="is sent">14.70 ± 7.78 / 36.09 ± 6.06</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is rc">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="fo ner">60.37 ± 3.60 / 59.38 ± 3.85</td> <!-- FoNE -->
   <td class="fo sent">8.21 ± 5.06 / 27.79 ± 5.76</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">43.69 ± 2.03 / 60.55 ± 1.76</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.51</td> <!-- Danish rank -->
   <td class="no-rank">2.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
   <td class="is-rank">3.07</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.98</td> <!-- Faroese rank -->
   <td class="de-rank">2.26</td> <!-- German rank -->
   <td class="nl-rank">2.99</td> <!-- Dutch rank -->
   <td class="en-rank">2.03</td> <!-- English rank -->
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
   <td class="is sent">32.07 ± 2.95 / 50.25 ± 3.47</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.20 ± 2.00 / 43.42 ± 4.87</td> <!-- ScaLA-is -->
   <td class="is rc">8.19 ± 0.76 / 33.02 ± 1.85</td> <!-- NQiI -->
   <td class="fo ner">84.73 ± 1.49 / 85.19 ± 1.59</td> <!-- FoNE -->
   <td class="fo sent">-0.64 ± 3.87 / 22.47 ± 3.96</td> <!-- FoSent -->
   <td class="fo la">1.37 ± 2.46 / 39.78 ± 3.24</td> <!-- ScaLA-fo -->
   <td class="fo rc">4.15 ± 4.39 / 5.74 ± 6.06</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.57</td> <!-- Danish rank -->
   <td class="no-rank">2.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
   <td class="is-rank">3.40</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.67</td> <!-- Faroese rank -->
   <td class="de-rank">2.20</td> <!-- German rank -->
   <td class="nl-rank">3.03</td> <!-- Dutch rank -->
   <td class="en-rank">2.11</td> <!-- English rank -->
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
   <td class="is sent">16.23 ± 4.59 / 35.37 ± 4.49</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="fo ner">58.67 ± 3.95 / 58.47 ± 3.96</td> <!-- FoNE -->
   <td class="fo sent">10.39 ± 7.55 / 30.73 ± 6.92</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">40.95 ± 1.80 / 55.82 ± 1.95</td> <!-- FoQA -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">3.04</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
   <td class="is-rank">3.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.04</td> <!-- Faroese rank -->
   <td class="de-rank">2.60</td> <!-- German rank -->
   <td class="nl-rank">3.09</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
   <td class="da ner">41.12 ± 3.39 / 32.50 ± 2.74</td> <!-- DANSK -->
   <td class="da sent">42.77 ± 2.76 / 54.70 ± 4.19</td> <!-- Angry Tweets -->
   <td class="da la">11.52 ± 3.01 / 49.37 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">51.14 ± 1.03 / 60.18 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="no ner">49.66 ± 1.79 / 39.31 ± 2.55</td> <!-- NorNE-nb -->
   <td class="no ner">51.98 ± 1.55 / 42.48 ± 3.10</td> <!-- NorNE-nn -->
   <td class="no sent">44.13 ± 2.80 / 60.09 ± 3.10</td> <!-- NoReC -->
   <td class="no la">0.67 ± 1.18 / 33.81 ± 0.33</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 0.93 / 33.03 ± 0.39</td> <!-- ScaLA-nn -->
   <td class="no rc">28.62 ± 4.16 / 56.91 ± 4.14</td> <!-- NorQuAD -->
   <td class="sv ner">43.74 ± 2.58 / 34.37 ± 2.59</td> <!-- SUC3 -->
   <td class="sv sent">76.98 ± 1.31 / 71.38 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">16.01 ± 2.24 / 51.83 ± 3.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.38 ± 1.78 / 57.83 ± 0.99</td> <!-- ScandiQA-sv -->
   <td class="is ner">27.57 ± 1.71 / 22.52 ± 1.18</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">10.07 ± 5.45 / 28.32 ± 4.30</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.39 ± 1.30 / 34.40 ± 1.96</td> <!-- ScaLA-is -->
   <td class="is rc">22.98 ± 2.48 / 50.74 ± 1.59</td> <!-- NQiI -->
   <td class="fo ner">58.24 ± 3.73 / 47.44 ± 4.83</td> <!-- FoNE -->
   <td class="fo sent">32.79 ± 2.01 / 41.82 ± 1.09</td> <!-- FoSent -->
   <td class="fo la">1.77 ± 2.13 / 45.44 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.13 ± 1.12 / 64.71 ± 0.74</td> <!-- FoQA -->
   <td class="de ner">55.52 ± 2.07 / 46.18 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">50.52 ± 2.29 / 62.39 ± 2.63</td> <!-- SB10k -->
   <td class="de la">9.87 ± 2.95 / 42.20 ± 3.60</td> <!-- ScaLA-de -->
   <td class="de rc">20.20 ± 3.28 / 47.02 ± 5.20</td> <!-- GermanQuAD -->
   <td class="nl ner">43.66 ± 2.01 / 40.23 ± 1.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.87 ± 1.32 / 37.23 ± 1.55</td> <!-- Dutch Social -->
   <td class="nl la">17.94 ± 3.48 / 55.88 ± 3.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.77 ± 1.82 / 64.44 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="en ner">68.44 ± 1.14 / 56.80 ± 2.31</td> <!-- CoNLL-en -->
   <td class="en sent">66.00 ± 1.41 / 70.47 ± 1.02</td> <!-- SST5 -->
   <td class="en la">32.04 ± 3.44 / 65.62 ± 1.88</td> <!-- ScaLA-en -->
   <td class="en rc">49.54 ± 3.13 / 75.26 ± 1.64</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.62</td> <!-- Danish rank -->
   <td class="no-rank">2.60</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.28</td> <!-- Swedish rank -->
   <td class="is-rank">3.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.91</td> <!-- Faroese rank -->
   <td class="de-rank">2.41</td> <!-- German rank -->
   <td class="nl-rank">2.83</td> <!-- Dutch rank -->
   <td class="en-rank">2.29</td> <!-- English rank -->
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
   <td class="is sent">29.56 ± 1.49 / 50.69 ± 1.62</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.08 ± 1.89 / 48.68 ± 2.96</td> <!-- ScaLA-is -->
   <td class="is rc">6.81 ± 0.33 / 30.96 ± 0.65</td> <!-- NQiI -->
   <td class="fo ner">83.21 ± 0.53 / 83.81 ± 0.45</td> <!-- FoNE -->
   <td class="fo sent">3.90 ± 4.05 / 25.25 ± 5.25</td> <!-- FoSent -->
   <td class="fo la">2.37 ± 4.63 / 48.46 ± 3.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">1.35 ± 1.03 / 2.54 ± 1.88</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.27</td> <!-- Swedish rank -->
   <td class="is-rank">3.60</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.55</td> <!-- Faroese rank -->
   <td class="de-rank">2.57</td> <!-- German rank -->
   <td class="nl-rank">2.88</td> <!-- Dutch rank -->
   <td class="en-rank">1.96</td> <!-- English rank -->
   <td class="da ner">45.90 ± 2.53 / 33.00 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">37.11 ± 1.88 / 56.47 ± 1.59</td> <!-- Angry Tweets -->
   <td class="da la">11.70 ± 2.16 / 50.31 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">50.11 ± 0.83 / 55.71 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="no ner">66.91 ± 1.50 / 54.98 ± 2.20</td> <!-- NorNE-nb -->
   <td class="no ner">62.82 ± 1.23 / 53.14 ± 3.17</td> <!-- NorNE-nn -->
   <td class="no sent">40.71 ± 1.63 / 59.35 ± 1.58</td> <!-- NoReC -->
   <td class="no la">9.50 ± 1.68 / 46.31 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">6.74 ± 1.70 / 42.10 ± 4.67</td> <!-- ScaLA-nn -->
   <td class="no rc">32.83 ± 1.83 / 55.30 ± 2.35</td> <!-- NorQuAD -->
   <td class="sv ner">52.85 ± 2.76 / 35.11 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">73.93 ± 1.58 / 73.97 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">8.27 ± 2.90 / 43.29 ± 4.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.49 ± 0.77 / 54.50 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="is ner">43.20 ± 3.61 / 32.10 ± 3.76</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.54 ± 2.60 / 17.05 ± 2.70</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">14.28 ± 2.94 / 38.21 ± 2.38</td> <!-- NQiI -->
   <td class="fo ner">60.46 ± 2.53 / 58.29 ± 2.53</td> <!-- FoNE -->
   <td class="fo sent">21.59 ± 6.94 / 40.68 ± 5.50</td> <!-- FoSent -->
   <td class="fo la">0.51 ± 0.78 / 36.20 ± 2.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">33.54 ± 1.00 / 49.02 ± 0.91</td> <!-- FoQA -->
   <td class="de ner">54.45 ± 1.17 / 42.36 ± 2.59</td> <!-- GermEval -->
   <td class="de sent">43.62 ± 3.18 / 59.82 ± 2.70</td> <!-- SB10k -->
   <td class="de la">15.24 ± 1.87 / 55.49 ± 2.89</td> <!-- ScaLA-de -->
   <td class="de rc">26.00 ± 2.28 / 51.82 ± 2.70</td> <!-- GermanQuAD -->
   <td class="nl ner">60.72 ± 2.14 / 45.52 ± 2.46</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.38 ± 1.62 / 29.91 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">10.96 ± 1.47 / 47.97 ± 3.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.20 ± 0.91 / 61.75 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="en ner">72.59 ± 0.91 / 65.83 ± 1.30</td> <!-- CoNLL-en -->
   <td class="en sent">61.61 ± 1.45 / 67.09 ± 1.38</td> <!-- SST5 -->
   <td class="en la">18.37 ± 2.07 / 56.26 ± 2.62</td> <!-- ScaLA-en -->
   <td class="en rc">66.68 ± 3.56 / 78.95 ± 2.38</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.48</td> <!-- Danish rank -->
   <td class="no-rank">2.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.31</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.63</td> <!-- Faroese rank -->
   <td class="de-rank">2.46</td> <!-- German rank -->
   <td class="nl-rank">3.05</td> <!-- Dutch rank -->
   <td class="en-rank">1.96</td> <!-- English rank -->
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
   <td class="is sent">12.93 ± 5.42 / 30.40 ± 3.15</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo sent">15.85 ± 6.84 / 36.28 ± 7.13</td> <!-- FoSent -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">33.54 ± 1.29 / 50.80 ± 1.31</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>claude-3-5-haiku-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">277 ± 77 / 70 ± 25</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.11</td> <!-- Danish rank -->
   <td class="no-rank">3.15</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.53</td> <!-- Swedish rank -->
   <td class="is-rank">3.34</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.82</td> <!-- Faroese rank -->
   <td class="de-rank">2.52</td> <!-- German rank -->
   <td class="nl-rank">2.71</td> <!-- Dutch rank -->
   <td class="en-rank">2.53</td> <!-- English rank -->
   <td class="da ner">59.48 ± 1.97 / 42.21 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">56.46 ± 2.39 / 71.07 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">20.57 ± 3.78 / 49.85 ± 2.21</td> <!-- ScaLA-da -->
   <td class="da rc">38.23 ± 1.71 / 57.70 ± 1.22</td> <!-- ScandiQA-da -->
   <td class="no ner">69.39 ± 2.58 / 47.10 ± 3.14</td> <!-- NorNE-nb -->
   <td class="no ner">62.76 ± 2.10 / 42.75 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">3.97 ± 1.70 / 32.77 ± 0.95</td> <!-- NoReC -->
   <td class="no la">31.65 ± 2.14 / 54.96 ± 1.11</td> <!-- ScaLA-nb -->
   <td class="no la">5.86 ± 3.28 / 38.81 ± 1.69</td> <!-- ScaLA-nn -->
   <td class="no rc">36.65 ± 1.08 / 66.51 ± 0.83</td> <!-- NorQuAD -->
   <td class="sv ner">57.06 ± 2.15 / 38.72 ± 1.61</td> <!-- SUC3 -->
   <td class="sv sent">59.89 ± 3.67 / 62.05 ± 2.71</td> <!-- SweReC -->
   <td class="sv la">9.30 ± 1.88 / 35.59 ± 0.94</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.97 ± 1.52 / 58.05 ± 1.05</td> <!-- ScandiQA-sv -->
   <td class="is ner">34.99 ± 2.03 / 17.39 ± 1.24</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">31.19 ± 1.29 / 43.32 ± 1.05</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-10.68 ± 2.75 / 33.95 ± 1.08</td> <!-- ScaLA-is -->
   <td class="is rc">23.65 ± 1.16 / 46.35 ± 1.25</td> <!-- NQiI -->
   <td class="fo ner">51.06 ± 1.45 / 30.27 ± 1.00</td> <!-- FoNE -->
   <td class="fo sent">-3.58 ± 4.03 / 14.94 ± 2.38</td> <!-- FoSent -->
   <td class="fo la">4.10 ± 4.03 / 37.28 ± 1.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.29 ± 1.54 / 72.97 ± 1.19</td> <!-- FoQA -->
   <td class="de ner">55.59 ± 1.42 / 31.16 ± 1.29</td> <!-- GermEval -->
   <td class="de sent">43.73 ± 2.53 / 61.91 ± 1.47</td> <!-- SB10k -->
   <td class="de la">23.74 ± 3.03 / 45.75 ± 2.40</td> <!-- ScaLA-de -->
   <td class="de rc">21.36 ± 1.42 / 50.29 ± 1.55</td> <!-- GermanQuAD -->
   <td class="nl ner">61.15 ± 3.04 / 43.60 ± 2.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.71 ± 2.21 / 30.22 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">35.26 ± 2.46 / 59.55 ± 1.69</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.27 ± 1.25 / 68.96 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="en ner">74.35 ± 1.24 / 63.12 ± 1.09</td> <!-- CoNLL-en -->
   <td class="en sent">31.19 ± 2.30 / 44.96 ± 1.92</td> <!-- SST5 -->
   <td class="en la">21.76 ± 3.56 / 59.95 ± 1.92</td> <!-- ScaLA-en -->
   <td class="en rc">45.70 ± 1.03 / 74.84 ± 0.76</td> <!-- SQuAD -->
   <td>14.0.1</td> <!-- DANSK version -->
   <td>14.0.1</td> <!-- Angry Tweets version -->
   <td>14.0.1</td> <!-- ScaLA-da version -->
   <td>14.0.1</td> <!-- ScandiQA-da version -->
   <td>14.0.3</td> <!-- NorNE-nb version -->
   <td>14.0.3</td> <!-- NorNE-nn version -->
   <td>14.0.2</td> <!-- NoReC version -->
   <td>14.0.3</td> <!-- ScaLA-nb version -->
   <td>14.0.3</td> <!-- ScaLA-nn version -->
   <td>14.0.3</td> <!-- NorQuAD version -->
   <td>14.0.2</td> <!-- SUC3 version -->
   <td>14.0.2</td> <!-- SweReC version -->
   <td>14.0.3</td> <!-- ScaLA-sv version -->
   <td>14.0.3</td> <!-- ScandiQA-sv version -->
   <td>14.0.3</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.3</td> <!-- ScaLA-is version -->
   <td>14.0.3</td> <!-- NQiI version -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.2</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   <td>14.0.3</td> <!-- GermEval version -->
   <td>14.0.2</td> <!-- SB10k version -->
   <td>14.0.3</td> <!-- ScaLA-de version -->
   <td>14.0.3</td> <!-- GermanQuAD version -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.2</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.2</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
   <td class="is-rank">3.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.75</td> <!-- Faroese rank -->
   <td class="de-rank">2.59</td> <!-- German rank -->
   <td class="nl-rank">3.06</td> <!-- Dutch rank -->
   <td class="en-rank">2.06</td> <!-- English rank -->
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
   <td class="is sent">13.59 ± 6.27 / 36.87 ± 4.51</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo sent">13.24 ± 5.37 / 38.49 ± 4.97</td> <!-- FoSent -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td class="fo rc">31.87 ± 2.20 / 46.21 ± 1.15</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="da-rank">2.91</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.34</td> <!-- Swedish rank -->
   <td class="is-rank">3.45</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.70</td> <!-- Faroese rank -->
   <td class="de-rank">3.21</td> <!-- German rank -->
   <td class="nl-rank">3.24</td> <!-- Dutch rank -->
   <td class="en-rank">2.29</td> <!-- English rank -->
   <td class="da ner">28.18 ± 3.39 / 24.25 ± 3.30</td> <!-- DANSK -->
   <td class="da sent">29.32 ± 7.19 / 41.08 ± 8.29</td> <!-- Angry Tweets -->
   <td class="da la">2.90 ± 2.18 / 37.93 ± 4.98</td> <!-- ScaLA-da -->
   <td class="da rc">56.48 ± 1.11 / 62.92 ± 0.96</td> <!-- ScandiQA-da -->
   <td class="no ner">36.96 ± 3.10 / 34.68 ± 3.19</td> <!-- NorNE-nb -->
   <td class="no ner">39.38 ± 3.30 / 37.06 ± 3.49</td> <!-- NorNE-nn -->
   <td class="no sent">32.67 ± 2.52 / 44.37 ± 3.06</td> <!-- NoReC -->
   <td class="no la">2.18 ± 2.36 / 38.05 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">5.33 ± 2.97 / 44.30 ± 4.99</td> <!-- ScaLA-nn -->
   <td class="no rc">45.23 ± 5.03 / 67.75 ± 4.41</td> <!-- NorQuAD -->
   <td class="sv ner">41.49 ± 2.82 / 38.09 ± 2.86</td> <!-- SUC3 -->
   <td class="sv sent">75.64 ± 1.51 / 76.06 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">0.66 ± 1.97 / 33.73 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.48 ± 0.54 / 63.85 ± 0.46</td> <!-- ScandiQA-sv -->
   <td class="is ner">31.81 ± 1.93 / 29.47 ± 2.02</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">18.33 ± 5.09 / 30.21 ± 5.80</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">3.63 ± 1.69 / 44.49 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is rc">16.72 ± 7.29 / 46.83 ± 5.93</td> <!-- NQiI -->
   <td class="fo ner">40.18 ± 3.60 / 39.95 ± 3.38</td> <!-- FoNE -->
   <td class="fo sent">14.19 ± 8.12 / 28.15 ± 8.15</td> <!-- FoSent -->
   <td class="fo la">0.31 ± 1.71 / 41.35 ± 4.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.60 ± 2.49 / 60.78 ± 2.12</td> <!-- FoQA -->
   <td class="de ner">32.33 ± 2.48 / 30.20 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">26.39 ± 5.23 / 36.06 ± 6.62</td> <!-- SB10k -->
   <td class="de la">1.44 ± 1.38 / 33.60 ± 0.42</td> <!-- ScaLA-de -->
   <td class="de rc">28.15 ± 5.57 / 54.13 ± 6.75</td> <!-- GermanQuAD -->
   <td class="nl ner">36.61 ± 3.37 / 31.91 ± 2.20</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.77 ± 1.80 / 25.31 ± 1.42</td> <!-- Dutch Social -->
   <td class="nl la">3.52 ± 2.07 / 35.34 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.51 ± 0.97 / 70.33 ± 0.64</td> <!-- SQuAD-nl -->
   <td class="en ner">47.20 ± 3.39 / 44.00 ± 3.43</td> <!-- CoNLL-en -->
   <td class="en sent">64.82 ± 1.13 / 67.11 ± 1.41</td> <!-- SST5 -->
   <td class="en la">7.57 ± 2.31 / 45.83 ± 3.97</td> <!-- ScaLA-en -->
   <td class="en rc">73.88 ± 1.02 / 83.56 ± 0.75</td> <!-- SQuAD -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="da-rank">2.89</td> <!-- Danish rank -->
   <td class="no-rank">3.20</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="is-rank">3.82</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.06</td> <!-- Faroese rank -->
   <td class="de-rank">2.53</td> <!-- German rank -->
   <td class="nl-rank">3.09</td> <!-- Dutch rank -->
   <td class="en-rank">2.15</td> <!-- English rank -->
   <td class="da ner">37.37 ± 2.46 / 26.81 ± 2.24</td> <!-- DANSK -->
   <td class="da sent">31.44 ± 1.82 / 48.96 ± 2.35</td> <!-- Angry Tweets -->
   <td class="da la">5.27 ± 2.40 / 40.63 ± 4.68</td> <!-- ScaLA-da -->
   <td class="da rc">48.41 ± 1.10 / 55.05 ± 0.97</td> <!-- ScandiQA-da -->
   <td class="no ner">44.89 ± 2.26 / 34.93 ± 2.45</td> <!-- NorNE-nb -->
   <td class="no ner">48.08 ± 1.68 / 34.39 ± 2.61</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 1.15 / 51.91 ± 2.66</td> <!-- NoReC -->
   <td class="no la">7.49 ± 1.65 / 47.79 ± 3.81</td> <!-- ScaLA-nb -->
   <td class="no la">4.65 ± 1.91 / 45.75 ± 5.13</td> <!-- ScaLA-nn -->
   <td class="no rc">26.37 ± 1.51 / 47.59 ± 2.41</td> <!-- NorQuAD -->
   <td class="sv ner">40.68 ± 2.32 / 24.33 ± 2.43</td> <!-- SUC3 -->
   <td class="sv sent">68.96 ± 2.04 / 72.76 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">4.77 ± 1.97 / 43.64 ± 5.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.73 ± 0.76 / 56.63 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="is ner">23.14 ± 2.08 / 23.09 ± 2.24</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">5.07 ± 2.69 / 27.01 ± 2.31</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.18 ± 1.67 / 33.93 ± 0.34</td> <!-- ScaLA-is -->
   <td class="is rc">14.15 ± 2.49 / 36.10 ± 1.65</td> <!-- NQiI -->
   <td class="fo ner">45.56 ± 1.92 / 42.78 ± 1.78</td> <!-- FoNE -->
   <td class="fo sent">7.44 ± 3.71 / 28.90 ± 5.97</td> <!-- FoSent -->
   <td class="fo la">0.92 ± 2.19 / 40.29 ± 3.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.82 ± 1.22 / 31.49 ± 1.49</td> <!-- FoQA -->
   <td class="de ner">47.31 ± 1.67 / 31.36 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">48.28 ± 4.28 / 64.07 ± 3.81</td> <!-- SB10k -->
   <td class="de la">14.08 ± 1.29 / 52.67 ± 2.70</td> <!-- ScaLA-de -->
   <td class="de rc">28.37 ± 4.07 / 55.92 ± 4.76</td> <!-- GermanQuAD -->
   <td class="nl ner">49.25 ± 2.57 / 36.48 ± 2.14</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.45 ± 1.76 / 39.66 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">11.87 ± 2.68 / 47.32 ± 3.85</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 1.44 / 67.04 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="en ner">52.79 ± 4.09 / 43.45 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">65.92 ± 1.02 / 70.47 ± 0.75</td> <!-- SST5 -->
   <td class="en la">16.74 ± 2.67 / 55.45 ± 3.35</td> <!-- ScaLA-en -->
   <td class="en rc">64.92 ± 2.84 / 80.88 ± 1.27</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="da-rank">3.00</td> <!-- Danish rank -->
   <td class="no-rank">3.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="is-rank">3.25</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="de-rank">3.09</td> <!-- German rank -->
   <td class="nl-rank">2.71</td> <!-- Dutch rank -->
   <td class="en-rank">2.87</td> <!-- English rank -->
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
   <td class="is sent">33.10 ± 1.86 / 52.77 ± 1.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.02 ± 0.94 / 47.05 ± 2.13</td> <!-- ScaLA-is -->
   <td class="is rc">6.48 ± 0.37 / 27.44 ± 0.44</td> <!-- NQiI -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">9.77 ± 3.39 / 32.64 ± 2.55</td> <!-- FoSent -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="da-rank">2.85</td> <!-- Danish rank -->
   <td class="no-rank">3.59</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.42</td> <!-- Swedish rank -->
   <td class="is-rank">3.73</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.15</td> <!-- Faroese rank -->
   <td class="de-rank">2.96</td> <!-- German rank -->
   <td class="nl-rank">3.11</td> <!-- Dutch rank -->
   <td class="en-rank">2.14</td> <!-- English rank -->
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
   <td class="is sent">4.29 ± 3.60 / 23.24 ± 4.11</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.94 ± 2.60 / 36.06 ± 2.17</td> <!-- NQiI -->
   <td class="fo ner">60.88 ± 2.03 / 60.02 ± 1.84</td> <!-- FoNE -->
   <td class="fo sent">0.16 ± 0.32 / 14.73 ± 2.24</td> <!-- FoSent -->
   <td class="fo la">-0.35 ± 1.18 / 34.50 ± 1.25</td> <!-- ScaLA-fo -->
   <td class="fo rc">18.54 ± 1.93 / 29.79 ± 1.35</td> <!-- FoQA -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="da-rank">3.00</td> <!-- Danish rank -->
   <td class="no-rank">3.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="is-rank">3.28</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.87</td> <!-- Faroese rank -->
   <td class="de-rank">3.09</td> <!-- German rank -->
   <td class="nl-rank">3.27</td> <!-- Dutch rank -->
   <td class="en-rank">2.87</td> <!-- English rank -->
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
   <td class="is sent">33.10 ± 1.86 / 52.77 ± 1.64</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.80 ± 1.69 / 45.59 ± 3.23</td> <!-- ScaLA-is -->
   <td class="is rc">6.14 ± 0.74 / 28.02 ± 0.58</td> <!-- NQiI -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">9.77 ± 3.39 / 32.64 ± 2.55</td> <!-- FoSent -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.90</td> <!-- Danish rank -->
   <td class="no-rank">3.24</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="is-rank">3.91</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.13</td> <!-- Faroese rank -->
   <td class="de-rank">2.89</td> <!-- German rank -->
   <td class="nl-rank">3.27</td> <!-- Dutch rank -->
   <td class="en-rank">2.27</td> <!-- English rank -->
   <td class="da ner">37.21 ± 2.75 / 27.74 ± 2.59</td> <!-- DANSK -->
   <td class="da sent">31.54 ± 2.39 / 50.61 ± 2.88</td> <!-- Angry Tweets -->
   <td class="da la">6.30 ± 1.61 / 49.09 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da rc">44.86 ± 0.80 / 51.51 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="no ner">53.78 ± 2.43 / 49.41 ± 2.56</td> <!-- NorNE-nb -->
   <td class="no ner">55.14 ± 1.27 / 51.07 ± 1.78</td> <!-- NorNE-nn -->
   <td class="no sent">26.21 ± 1.63 / 43.33 ± 1.46</td> <!-- NoReC -->
   <td class="no la">3.90 ± 1.45 / 43.86 ± 4.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.42 ± 1.39 / 41.58 ± 3.89</td> <!-- ScaLA-nn -->
   <td class="no rc">24.86 ± 1.34 / 45.77 ± 1.85</td> <!-- NorQuAD -->
   <td class="sv ner">50.10 ± 4.30 / 42.80 ± 5.47</td> <!-- SUC3 -->
   <td class="sv sent">65.67 ± 3.92 / 64.00 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">4.55 ± 2.18 / 45.11 ± 4.32</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.83 ± 1.02 / 49.35 ± 1.09</td> <!-- ScandiQA-sv -->
   <td class="is ner">33.57 ± 2.48 / 33.47 ± 2.48</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.60 ± 2.01 / 16.42 ± 1.16</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">11.27 ± 2.38 / 33.54 ± 1.64</td> <!-- NQiI -->
   <td class="fo ner">56.88 ± 2.51 / 57.68 ± 2.14</td> <!-- FoNE -->
   <td class="fo sent">3.80 ± 5.87 / 28.41 ± 4.70</td> <!-- FoSent -->
   <td class="fo la">-0.21 ± 2.20 / 34.20 ± 1.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">13.72 ± 2.56 / 24.11 ± 2.40</td> <!-- FoQA -->
   <td class="de ner">49.16 ± 2.12 / 40.34 ± 2.81</td> <!-- GermEval -->
   <td class="de sent">35.17 ± 4.48 / 51.15 ± 4.55</td> <!-- SB10k -->
   <td class="de la">9.79 ± 2.06 / 50.77 ± 3.64</td> <!-- ScaLA-de -->
   <td class="de rc">22.48 ± 2.59 / 45.90 ± 3.03</td> <!-- GermanQuAD -->
   <td class="nl ner">48.53 ± 3.89 / 38.20 ± 2.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.15 ± 1.55 / 22.01 ± 1.44</td> <!-- Dutch Social -->
   <td class="nl la">4.88 ± 2.27 / 38.78 ± 3.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.38 ± 0.93 / 56.09 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="en ner">58.30 ± 2.16 / 53.45 ± 1.98</td> <!-- CoNLL-en -->
   <td class="en sent">59.01 ± 2.14 / 62.37 ± 1.73</td> <!-- SST5 -->
   <td class="en la">10.33 ± 3.06 / 53.28 ± 2.21</td> <!-- ScaLA-en -->
   <td class="en rc">65.04 ± 2.20 / 75.93 ± 1.50</td> <!-- SQuAD -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">2.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.44</td> <!-- Swedish rank -->
   <td class="is-rank">3.32</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.94</td> <!-- Faroese rank -->
   <td class="de-rank">3.04</td> <!-- German rank -->
   <td class="nl-rank">4.09</td> <!-- Dutch rank -->
   <td class="en-rank">2.95</td> <!-- English rank -->
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
   <td class="is sent">31.32 ± 1.98 / 51.09 ± 1.51</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.91 ± 1.14 / 46.54 ± 2.46</td> <!-- ScaLA-is -->
   <td class="is rc">3.69 ± 0.48 / 27.48 ± 0.49</td> <!-- NQiI -->
   <td class="fo ner">82.24 ± 0.85 / 82.84 ± 0.78</td> <!-- FoNE -->
   <td class="fo sent">6.35 ± 5.07 / 29.58 ± 4.89</td> <!-- FoSent -->
   <td class="fo la">2.84 ± 1.41 / 50.47 ± 1.13</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="da-rank">3.17</td> <!-- Danish rank -->
   <td class="no-rank">3.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.32</td> <!-- Swedish rank -->
   <td class="is-rank">3.46</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.04</td> <!-- Faroese rank -->
   <td class="de-rank">2.85</td> <!-- German rank -->
   <td class="nl-rank">3.48</td> <!-- Dutch rank -->
   <td class="en-rank">2.92</td> <!-- English rank -->
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
   <td class="is sent">24.79 ± 3.07 / 45.25 ± 3.48</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-1.21 ± 1.45 / 47.43 ± 1.67</td> <!-- ScaLA-is -->
   <td class="is rc">6.01 ± 0.45 / 29.08 ± 1.30</td> <!-- NQiI -->
   <td class="fo ner">80.45 ± 1.48 / 81.32 ± 1.42</td> <!-- FoNE -->
   <td class="fo sent">0.90 ± 2.61 / 26.49 ± 2.31</td> <!-- FoSent -->
   <td class="fo la">2.52 ± 1.88 / 47.78 ± 1.67</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.58 ± 0.81 / 1.12 ± 1.62</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="da-rank">3.39</td> <!-- Danish rank -->
   <td class="no-rank">3.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="is-rank">4.06</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.28</td> <!-- Faroese rank -->
   <td class="de-rank">3.01</td> <!-- German rank -->
   <td class="nl-rank">3.24</td> <!-- Dutch rank -->
   <td class="en-rank">2.30</td> <!-- English rank -->
   <td class="da ner">31.80 ± 2.87 / 23.06 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">6.85 ± 2.25 / 19.42 ± 0.91</td> <!-- Angry Tweets -->
   <td class="da la">0.97 ± 1.10 / 36.48 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">49.83 ± 1.73 / 55.19 ± 1.84</td> <!-- ScandiQA-da -->
   <td class="no ner">40.08 ± 2.60 / 33.17 ± 1.81</td> <!-- NorNE-nb -->
   <td class="no ner">43.96 ± 1.65 / 32.96 ± 2.24</td> <!-- NorNE-nn -->
   <td class="no sent">31.90 ± 1.50 / 53.03 ± 1.81</td> <!-- NoReC -->
   <td class="no la">-0.07 ± 0.97 / 35.01 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 2.35 / 38.10 ± 4.51</td> <!-- ScaLA-nn -->
   <td class="no rc">23.32 ± 2.39 / 43.13 ± 3.33</td> <!-- NorQuAD -->
   <td class="sv ner">36.01 ± 3.07 / 24.61 ± 4.22</td> <!-- SUC3 -->
   <td class="sv sent">57.18 ± 5.33 / 62.72 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 2.14 / 38.30 ± 3.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.04 ± 0.95 / 56.97 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="is ner">18.07 ± 3.62 / 18.73 ± 2.54</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.65 ± 3.12 / 18.97 ± 1.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.72 ± 1.22 / 33.96 ± 0.50</td> <!-- ScaLA-is -->
   <td class="is rc">12.27 ± 2.81 / 30.66 ± 1.47</td> <!-- NQiI -->
   <td class="fo ner">41.27 ± 4.31 / 40.85 ± 4.31</td> <!-- FoNE -->
   <td class="fo sent">5.40 ± 3.00 / 17.90 ± 2.95</td> <!-- FoSent -->
   <td class="fo la">-0.20 ± 2.17 / 43.01 ± 3.39</td> <!-- ScaLA-fo -->
   <td class="fo rc">19.69 ± 2.66 / 29.77 ± 2.80</td> <!-- FoQA -->
   <td class="de ner">40.61 ± 2.18 / 28.49 ± 2.11</td> <!-- GermEval -->
   <td class="de sent">31.86 ± 3.60 / 42.96 ± 3.98</td> <!-- SB10k -->
   <td class="de la">5.36 ± 3.96 / 37.83 ± 4.03</td> <!-- ScaLA-de -->
   <td class="de rc">25.99 ± 3.85 / 47.72 ± 4.74</td> <!-- GermanQuAD -->
   <td class="nl ner">42.52 ± 3.31 / 33.08 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.91 ± 1.71 / 35.24 ± 2.62</td> <!-- Dutch Social -->
   <td class="nl la">0.69 ± 2.82 / 36.10 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.95 ± 1.18 / 66.87 ± 1.37</td> <!-- SQuAD-nl -->
   <td class="en ner">49.44 ± 3.68 / 39.69 ± 2.34</td> <!-- CoNLL-en -->
   <td class="en sent">66.65 ± 1.04 / 65.72 ± 1.32</td> <!-- SST5 -->
   <td class="en la">12.56 ± 2.15 / 54.20 ± 3.42</td> <!-- ScaLA-en -->
   <td class="en rc">63.29 ± 4.61 / 75.62 ± 3.79</td> <!-- SQuAD -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da-rank">3.10</td> <!-- Danish rank -->
   <td class="no-rank">3.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.00</td> <!-- Swedish rank -->
   <td class="is-rank">3.54</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.24</td> <!-- Faroese rank -->
   <td class="de-rank">3.01</td> <!-- German rank -->
   <td class="nl-rank">3.15</td> <!-- Dutch rank -->
   <td class="en-rank">2.88</td> <!-- English rank -->
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
   <td class="is sent">36.28 ± 1.79 / 56.00 ± 1.23</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.71 ± 1.10 / 49.68 ± 1.24</td> <!-- ScaLA-is -->
   <td class="is rc">6.50 ± 0.42 / 27.51 ± 0.99</td> <!-- NQiI -->
   <td class="fo ner">59.50 ± 1.56 / 58.98 ± 1.55</td> <!-- FoNE -->
   <td class="fo sent">0.94 ± 4.40 / 23.64 ± 4.57</td> <!-- FoSent -->
   <td class="fo la">3.25 ± 2.04 / 49.77 ± 1.40</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.56 ± 1.52 / 10.14 ± 2.41</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.77</td> <!-- Swedish rank -->
   <td class="is-rank">3.78</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.91</td> <!-- Faroese rank -->
   <td class="de-rank">3.07</td> <!-- German rank -->
   <td class="nl-rank">3.45</td> <!-- Dutch rank -->
   <td class="en-rank">2.97</td> <!-- English rank -->
   <td class="da ner">34.66 ± 1.19 / 21.37 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">21.93 ± 3.72 / 31.67 ± 4.68</td> <!-- Angry Tweets -->
   <td class="da la">1.50 ± 1.04 / 33.84 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">52.36 ± 0.70 / 60.53 ± 0.63</td> <!-- ScandiQA-da -->
   <td class="no ner">37.36 ± 1.61 / 24.19 ± 1.65</td> <!-- NorNE-nb -->
   <td class="no ner">42.83 ± 1.41 / 28.06 ± 1.69</td> <!-- NorNE-nn -->
   <td class="no sent">16.02 ± 6.40 / 30.81 ± 5.11</td> <!-- NoReC -->
   <td class="no la">-0.08 ± 0.82 / 33.74 ± 0.41</td> <!-- ScaLA-nb -->
   <td class="no la">2.29 ± 1.78 / 35.36 ± 1.11</td> <!-- ScaLA-nn -->
   <td class="no rc">31.60 ± 1.36 / 56.15 ± 1.66</td> <!-- NorQuAD -->
   <td class="sv ner">35.02 ± 2.08 / 17.87 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">51.80 ± 4.28 / 57.15 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">6.15 ± 0.86 / 36.62 ± 0.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.85 ± 0.74 / 60.00 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">28.74 ± 2.37 / 19.43 ± 1.48</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">4.30 ± 1.28 / 19.35 ± 2.86</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.06 ± 1.39 / 34.20 ± 1.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.41 ± 2.45 / 45.55 ± 1.65</td> <!-- NQiI -->
   <td class="fo ner">46.64 ± 1.91 / 35.58 ± 2.47</td> <!-- FoNE -->
   <td class="fo sent">16.72 ± 4.87 / 41.68 ± 4.39</td> <!-- FoSent -->
   <td class="fo la">-1.54 ± 2.60 / 36.21 ± 2.51</td> <!-- ScaLA-fo -->
   <td class="fo rc">18.69 ± 5.12 / 38.94 ± 4.72</td> <!-- FoQA -->
   <td class="de ner">39.39 ± 2.50 / 23.55 ± 1.34</td> <!-- GermEval -->
   <td class="de sent">23.60 ± 3.12 / 34.73 ± 3.27</td> <!-- SB10k -->
   <td class="de la">7.68 ± 1.29 / 36.93 ± 0.75</td> <!-- ScaLA-de -->
   <td class="de rc">25.30 ± 0.79 / 52.63 ± 1.81</td> <!-- GermanQuAD -->
   <td class="nl ner">39.24 ± 2.43 / 24.25 ± 1.34</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.25 ± 1.28 / 18.15 ± 3.08</td> <!-- Dutch Social -->
   <td class="nl la">11.48 ± 1.02 / 52.86 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.18 ± 0.98 / 65.58 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="en ner">50.73 ± 2.64 / 38.64 ± 1.60</td> <!-- CoNLL-en -->
   <td class="en sent">27.52 ± 3.38 / 31.81 ± 3.98</td> <!-- SST5 -->
   <td class="en la">2.96 ± 2.64 / 35.23 ± 1.82</td> <!-- ScaLA-en -->
   <td class="en rc">63.42 ± 1.34 / 76.38 ± 1.18</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.0.4</td> <!-- Angry Tweets version -->
   <td>14.0.4</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.0.4</td> <!-- NoReC version -->
   <td>14.0.4</td> <!-- ScaLA-nb version -->
   <td>14.0.4</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.0.4</td> <!-- SB10k version -->
   <td>14.0.4</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.71</td> <!-- Swedish rank -->
   <td class="is-rank">4.05</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.50</td> <!-- Faroese rank -->
   <td class="de-rank">3.14</td> <!-- German rank -->
   <td class="nl-rank">3.51</td> <!-- Dutch rank -->
   <td class="en-rank">2.60</td> <!-- English rank -->
   <td class="da ner">19.61 ± 2.68 / 17.44 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">37.92 ± 1.74 / 46.23 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">2.81 ± 1.13 / 38.15 ± 2.81</td> <!-- ScaLA-da -->
   <td class="da rc">50.05 ± 1.02 / 56.82 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="no ner">31.43 ± 1.78 / 30.82 ± 2.35</td> <!-- NorNE-nb -->
   <td class="no ner">36.92 ± 1.75 / 37.80 ± 1.67</td> <!-- NorNE-nn -->
   <td class="no sent">30.63 ± 1.48 / 37.24 ± 1.90</td> <!-- NoReC -->
   <td class="no la">0.98 ± 1.59 / 42.00 ± 2.28</td> <!-- ScaLA-nb -->
   <td class="no la">1.67 ± 1.96 / 34.92 ± 1.93</td> <!-- ScaLA-nn -->
   <td class="no rc">33.24 ± 2.51 / 55.11 ± 2.82</td> <!-- NorQuAD -->
   <td class="sv ner">27.41 ± 2.70 / 24.45 ± 3.82</td> <!-- SUC3 -->
   <td class="sv sent">72.24 ± 0.82 / 68.89 ± 2.63</td> <!-- SweReC -->
   <td class="sv la">0.13 ± 1.85 / 36.22 ± 3.14</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.77 ± 0.63 / 56.59 ± 0.54</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.29 ± 2.33 / 14.72 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.83 ± 5.62 / 31.41 ± 4.70</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.92 ± 1.51 / 42.09 ± 3.39</td> <!-- ScaLA-is -->
   <td class="is rc">7.49 ± 1.26 / 24.16 ± 1.95</td> <!-- NQiI -->
   <td class="fo ner">33.53 ± 3.87 / 35.41 ± 3.77</td> <!-- FoNE -->
   <td class="fo sent">4.25 ± 5.04 / 26.21 ± 4.24</td> <!-- FoSent -->
   <td class="fo la">-2.32 ± 2.11 / 45.19 ± 2.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">15.41 ± 2.05 / 25.07 ± 1.98</td> <!-- FoQA -->
   <td class="de ner">28.49 ± 2.30 / 24.73 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">43.18 ± 2.89 / 58.22 ± 3.50</td> <!-- SB10k -->
   <td class="de la">2.92 ± 1.40 / 44.65 ± 3.51</td> <!-- ScaLA-de -->
   <td class="de rc">23.26 ± 3.37 / 48.47 ± 3.57</td> <!-- GermanQuAD -->
   <td class="nl ner">32.45 ± 2.17 / 30.83 ± 2.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.03 ± 2.08 / 34.16 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">5.58 ± 1.32 / 44.79 ± 3.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.18 ± 1.19 / 61.82 ± 1.19</td> <!-- SQuAD-nl -->
   <td class="en ner">37.47 ± 1.64 / 32.39 ± 2.53</td> <!-- CoNLL-en -->
   <td class="en sent">58.61 ± 2.46 / 62.78 ± 1.22</td> <!-- SST5 -->
   <td class="en la">5.30 ± 1.43 / 46.95 ± 3.51</td> <!-- ScaLA-en -->
   <td class="en rc">63.26 ± 0.73 / 74.41 ± 0.65</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="da-rank">3.23</td> <!-- Danish rank -->
   <td class="no-rank">3.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="is-rank">3.76</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.41</td> <!-- Faroese rank -->
   <td class="de-rank">3.32</td> <!-- German rank -->
   <td class="nl-rank">3.86</td> <!-- Dutch rank -->
   <td class="en-rank">2.20</td> <!-- English rank -->
   <td class="da ner">29.44 ± 1.81 / 20.31 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">18.49 ± 2.47 / 35.29 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">1.73 ± 1.63 / 38.18 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da rc">44.39 ± 0.80 / 50.40 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="no ner">37.60 ± 2.17 / 29.30 ± 2.43</td> <!-- NorNE-nb -->
   <td class="no ner">38.38 ± 2.48 / 30.13 ± 2.95</td> <!-- NorNE-nn -->
   <td class="no sent">24.05 ± 3.58 / 40.36 ± 4.22</td> <!-- NoReC -->
   <td class="no la">3.56 ± 1.93 / 38.60 ± 3.52</td> <!-- ScaLA-nb -->
   <td class="no la">2.61 ± 2.57 / 38.57 ± 3.89</td> <!-- ScaLA-nn -->
   <td class="no rc">13.58 ± 3.16 / 25.34 ± 5.83</td> <!-- NorQuAD -->
   <td class="sv ner">37.37 ± 1.87 / 26.31 ± 3.34</td> <!-- SUC3 -->
   <td class="sv sent">64.46 ± 3.06 / 69.83 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">4.49 ± 1.96 / 46.63 ± 4.39</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.92 ± 1.06 / 49.57 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="is ner">26.23 ± 3.53 / 23.26 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">6.86 ± 5.25 / 23.96 ± 4.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.69 ± 1.42 / 45.61 ± 2.69</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.59 / 28.57 ± 2.09</td> <!-- NQiI -->
   <td class="fo ner">40.28 ± 3.29 / 42.15 ± 2.85</td> <!-- FoNE -->
   <td class="fo sent">3.94 ± 3.10 / 30.51 ± 3.43</td> <!-- FoSent -->
   <td class="fo la">-0.26 ± 1.92 / 38.29 ± 4.03</td> <!-- ScaLA-fo -->
   <td class="fo rc">10.68 ± 1.75 / 17.52 ± 1.85</td> <!-- FoQA -->
   <td class="de ner">32.54 ± 1.57 / 26.92 ± 1.87</td> <!-- GermEval -->
   <td class="de sent">27.03 ± 2.54 / 42.80 ± 3.28</td> <!-- SB10k -->
   <td class="de la">8.95 ± 1.62 / 51.86 ± 2.23</td> <!-- ScaLA-de -->
   <td class="de rc">18.38 ± 1.26 / 39.18 ± 2.13</td> <!-- GermanQuAD -->
   <td class="nl ner">31.84 ± 3.39 / 28.66 ± 1.77</td> <!-- CoNLL-nl -->
   <td class="nl sent">1.56 ± 3.25 / 28.78 ± 2.60</td> <!-- Dutch Social -->
   <td class="nl la">5.05 ± 1.34 / 43.99 ± 4.14</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.55 ± 0.77 / 48.56 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="en ner">47.58 ± 2.41 / 39.52 ± 1.41</td> <!-- CoNLL-en -->
   <td class="en sent">66.78 ± 0.76 / 61.52 ± 0.99</td> <!-- SST5 -->
   <td class="en la">20.53 ± 3.83 / 58.47 ± 2.90</td> <!-- ScaLA-en -->
   <td class="en rc">58.07 ± 2.23 / 69.96 ± 1.63</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="da-rank">3.33</td> <!-- Danish rank -->
   <td class="no-rank">3.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.04</td> <!-- Swedish rank -->
   <td class="is-rank">3.53</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.90</td> <!-- Faroese rank -->
   <td class="de-rank">3.51</td> <!-- German rank -->
   <td class="nl-rank">3.24</td> <!-- Dutch rank -->
   <td class="en-rank">3.27</td> <!-- English rank -->
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
   <td class="is sent">35.18 ± 2.10 / 55.52 ± 1.45</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.14 ± 1.81 / 48.47 ± 1.64</td> <!-- ScaLA-is -->
   <td class="is rc">1.63 ± 0.33 / 21.45 ± 1.39</td> <!-- NQiI -->
   <td class="fo ner">75.63 ± 1.41 / 76.23 ± 1.36</td> <!-- FoNE -->
   <td class="fo sent">9.82 ± 2.60 / 36.40 ± 2.64</td> <!-- FoSent -->
   <td class="fo la">3.65 ± 1.93 / 48.34 ± 1.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="da-rank">3.65</td> <!-- Danish rank -->
   <td class="no-rank">3.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.06</td> <!-- Swedish rank -->
   <td class="is-rank">3.51</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.88</td> <!-- Faroese rank -->
   <td class="de-rank">3.33</td> <!-- German rank -->
   <td class="nl-rank">3.49</td> <!-- Dutch rank -->
   <td class="en-rank">3.24</td> <!-- English rank -->
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
   <td class="is sent">33.35 ± 1.84 / 53.45 ± 3.04</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.64 ± 2.11 / 49.47 ± 1.79</td> <!-- ScaLA-is -->
   <td class="is rc">1.27 ± 0.46 / 12.20 ± 2.90</td> <!-- NQiI -->
   <td class="fo ner">77.16 ± 0.93 / 78.00 ± 0.91</td> <!-- FoNE -->
   <td class="fo sent">10.41 ± 3.80 / 34.36 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="da-rank">3.26</td> <!-- Danish rank -->
   <td class="no-rank">3.54</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.17</td> <!-- Swedish rank -->
   <td class="is-rank">3.82</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.00</td> <!-- Faroese rank -->
   <td class="de-rank">3.49</td> <!-- German rank -->
   <td class="nl-rank">3.67</td> <!-- Dutch rank -->
   <td class="en-rank">2.97</td> <!-- English rank -->
   <td class="da ner">29.49 ± 2.73 / 21.57 ± 2.07</td> <!-- DANSK -->
   <td class="da sent">13.77 ± 3.72 / 23.78 ± 3.10</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.49 ± 0.27</td> <!-- ScaLA-da -->
   <td class="da rc">51.53 ± 1.01 / 59.23 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="no ner">34.78 ± 2.34 / 27.42 ± 1.71</td> <!-- NorNE-nb -->
   <td class="no ner">39.00 ± 3.24 / 31.27 ± 2.29</td> <!-- NorNE-nn -->
   <td class="no sent">10.69 ± 5.81 / 26.94 ± 3.14</td> <!-- NoReC -->
   <td class="no la">6.17 ± 1.50 / 50.50 ± 1.78</td> <!-- ScaLA-nb -->
   <td class="no la">5.90 ± 1.38 / 49.15 ± 2.88</td> <!-- ScaLA-nn -->
   <td class="no rc">31.25 ± 2.01 / 55.30 ± 2.29</td> <!-- NorQuAD -->
   <td class="sv ner">37.17 ± 2.59 / 25.25 ± 1.61</td> <!-- SUC3 -->
   <td class="sv sent">20.20 ± 4.93 / 21.73 ± 5.47</td> <!-- SweReC -->
   <td class="sv la">6.13 ± 1.52 / 39.55 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.66 ± 1.19 / 56.90 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="is ner">26.58 ± 1.47 / 22.13 ± 2.38</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.79 ± 2.98 / 26.06 ± 1.66</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.63 ± 1.36 / 43.80 ± 3.59</td> <!-- ScaLA-is -->
   <td class="is rc">15.14 ± 2.49 / 44.23 ± 2.12</td> <!-- NQiI -->
   <td class="fo ner">39.78 ± 1.79 / 31.09 ± 2.58</td> <!-- FoNE -->
   <td class="fo sent">16.03 ± 6.81 / 39.68 ± 7.16</td> <!-- FoSent -->
   <td class="fo la">-0.48 ± 1.85 / 33.39 ± 0.49</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.04 ± 4.63 / 38.93 ± 4.09</td> <!-- FoQA -->
   <td class="de ner">38.81 ± 2.72 / 27.14 ± 1.94</td> <!-- GermEval -->
   <td class="de sent">10.59 ± 3.02 / 21.22 ± 2.19</td> <!-- SB10k -->
   <td class="de la">0.91 ± 1.67 / 33.45 ± 0.28</td> <!-- ScaLA-de -->
   <td class="de rc">22.54 ± 1.17 / 48.13 ± 1.67</td> <!-- GermanQuAD -->
   <td class="nl ner">42.35 ± 2.49 / 29.29 ± 1.66</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.78 ± 0.93 / 8.63 ± 0.29</td> <!-- Dutch Social -->
   <td class="nl la">-0.02 ± 1.29 / 38.46 ± 1.55</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.61 ± 1.96 / 59.25 ± 1.42</td> <!-- SQuAD-nl -->
   <td class="en ner">44.48 ± 3.17 / 36.31 ± 2.23</td> <!-- CoNLL-en -->
   <td class="en sent">23.69 ± 3.36 / 25.98 ± 3.59</td> <!-- SST5 -->
   <td class="en la">8.52 ± 2.60 / 51.57 ± 2.62</td> <!-- ScaLA-en -->
   <td class="en rc">56.97 ± 1.53 / 71.38 ± 1.28</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.0.4</td> <!-- Angry Tweets version -->
   <td>14.0.4</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.0.4</td> <!-- NoReC version -->
   <td>14.0.4</td> <!-- ScaLA-nb version -->
   <td>14.0.4</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.0.4</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.0.4</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.0.4</td> <!-- SB10k version -->
   <td>14.0.4</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da-rank">3.65</td> <!-- Danish rank -->
   <td class="no-rank">3.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.06</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.88</td> <!-- Faroese rank -->
   <td class="de-rank">3.33</td> <!-- German rank -->
   <td class="nl-rank">3.98</td> <!-- Dutch rank -->
   <td class="en-rank">3.24</td> <!-- English rank -->
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
   <td class="is sent">34.19 ± 1.88 / 53.26 ± 3.44</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">2.64 ± 2.11 / 49.47 ± 1.79</td> <!-- ScaLA-is -->
   <td class="is rc">1.22 ± 0.49 / 12.16 ± 3.00</td> <!-- NQiI -->
   <td class="fo ner">77.00 ± 1.08 / 77.85 ± 1.05</td> <!-- FoNE -->
   <td class="fo sent">9.59 ± 3.69 / 32.95 ± 3.64</td> <!-- FoSent -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="da-rank">3.50</td> <!-- Danish rank -->
   <td class="no-rank">3.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.69</td> <!-- Swedish rank -->
   <td class="is-rank">3.83</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.56</td> <!-- Faroese rank -->
   <td class="de-rank">3.53</td> <!-- German rank -->
   <td class="nl-rank">3.89</td> <!-- Dutch rank -->
   <td class="en-rank">2.50</td> <!-- English rank -->
   <td class="da ner">24.47 ± 3.42 / 18.70 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">9.93 ± 2.70 / 23.57 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 1.81 / 35.31 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da rc">42.09 ± 2.63 / 47.54 ± 2.94</td> <!-- ScandiQA-da -->
   <td class="no ner">26.70 ± 4.42 / 24.56 ± 2.10</td> <!-- NorNE-nb -->
   <td class="no ner">28.23 ± 3.78 / 28.27 ± 2.80</td> <!-- NorNE-nn -->
   <td class="no sent">23.25 ± 4.16 / 36.07 ± 4.20</td> <!-- NoReC -->
   <td class="no la">-0.47 ± 1.05 / 33.93 ± 0.92</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.74 / 33.32 ± 0.79</td> <!-- ScaLA-nn -->
   <td class="no rc">13.40 ± 2.83 / 26.51 ± 4.94</td> <!-- NorQuAD -->
   <td class="sv ner">35.96 ± 3.50 / 26.41 ± 4.11</td> <!-- SUC3 -->
   <td class="sv sent">68.31 ± 1.43 / 72.51 ± 1.03</td> <!-- SweReC -->
   <td class="sv la">3.61 ± 1.79 / 49.47 ± 1.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.26 ± 1.85 / 49.32 ± 1.97</td> <!-- ScandiQA-sv -->
   <td class="is ner">20.50 ± 4.51 / 18.93 ± 3.84</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">10.09 ± 3.91 / 29.11 ± 2.96</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.83 ± 1.65 / 45.84 ± 2.02</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.45 / 28.36 ± 1.48</td> <!-- NQiI -->
   <td class="fo ner">27.91 ± 4.97 / 30.98 ± 4.28</td> <!-- FoNE -->
   <td class="fo sent">0.77 ± 4.14 / 23.56 ± 3.58</td> <!-- FoSent -->
   <td class="fo la">-0.48 ± 0.89 / 33.97 ± 1.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">16.56 ± 1.66 / 26.11 ± 1.42</td> <!-- FoQA -->
   <td class="de ner">28.67 ± 3.31 / 25.27 ± 2.68</td> <!-- GermEval -->
   <td class="de sent">19.69 ± 2.50 / 29.00 ± 2.22</td> <!-- SB10k -->
   <td class="de la">5.07 ± 0.89 / 47.60 ± 2.39</td> <!-- ScaLA-de -->
   <td class="de rc">18.43 ± 2.31 / 38.33 ± 2.91</td> <!-- GermanQuAD -->
   <td class="nl ner">22.84 ± 5.42 / 25.11 ± 3.52</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.60 ± 2.12 / 29.94 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">2.55 ± 1.41 / 40.88 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.33 ± 1.19 / 48.35 ± 1.31</td> <!-- SQuAD-nl -->
   <td class="en ner">41.57 ± 4.29 / 37.51 ± 3.05</td> <!-- CoNLL-en -->
   <td class="en sent">62.32 ± 1.12 / 67.09 ± 0.96</td> <!-- SST5 -->
   <td class="en la">8.04 ± 3.17 / 48.16 ± 5.38</td> <!-- ScaLA-en -->
   <td class="en rc">56.01 ± 3.10 / 67.43 ± 2.41</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">3.69</td> <!-- ScandEval rank -->
   <td class="da-rank">3.25</td> <!-- Danish rank -->
   <td class="no-rank">3.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.19</td> <!-- Swedish rank -->
   <td class="is-rank">4.04</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.58</td> <!-- Faroese rank -->
   <td class="de-rank">3.61</td> <!-- German rank -->
   <td class="nl-rank">3.78</td> <!-- Dutch rank -->
   <td class="en-rank">3.19</td> <!-- English rank -->
   <td class="da ner">28.30 ± 2.45 / 22.93 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">28.95 ± 4.05 / 48.32 ± 5.01</td> <!-- Angry Tweets -->
   <td class="da la">0.20 ± 0.52 / 34.12 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da rc">36.39 ± 0.84 / 43.32 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="no ner">38.96 ± 2.67 / 36.82 ± 3.28</td> <!-- NorNE-nb -->
   <td class="no ner">40.42 ± 2.43 / 38.81 ± 2.83</td> <!-- NorNE-nn -->
   <td class="no sent">19.42 ± 3.09 / 26.64 ± 4.19</td> <!-- NoReC -->
   <td class="no la">-0.13 ± 0.55 / 33.43 ± 0.23</td> <!-- ScaLA-nb -->
   <td class="no la">0.77 ± 1.22 / 33.80 ± 0.25</td> <!-- ScaLA-nn -->
   <td class="no rc">4.70 ± 1.89 / 8.66 ± 3.16</td> <!-- NorQuAD -->
   <td class="sv ner">36.29 ± 4.00 / 31.64 ± 3.95</td> <!-- SUC3 -->
   <td class="sv sent">39.68 ± 11.06 / 47.78 ± 9.30</td> <!-- SweReC -->
   <td class="sv la">0.96 ± 1.25 / 36.56 ± 2.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.64 ± 1.84 / 38.42 ± 1.95</td> <!-- ScandiQA-sv -->
   <td class="is ner">22.56 ± 3.90 / 22.69 ± 3.50</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">0.53 ± 2.22 / 20.28 ± 1.55</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.26 ± 0.43 / 33.59 ± 1.01</td> <!-- ScaLA-is -->
   <td class="is rc">11.77 ± 1.87 / 31.39 ± 2.24</td> <!-- NQiI -->
   <td class="fo ner">38.91 ± 4.57 / 39.53 ± 3.74</td> <!-- FoNE -->
   <td class="fo sent">-1.72 ± 2.43 / 16.58 ± 3.29</td> <!-- FoSent -->
   <td class="fo la">0.66 ± 0.95 / 33.60 ± 0.66</td> <!-- ScaLA-fo -->
   <td class="fo rc">4.82 ± 3.70 / 7.41 ± 5.58</td> <!-- FoQA -->
   <td class="de ner">34.68 ± 3.56 / 30.00 ± 2.82</td> <!-- GermEval -->
   <td class="de sent">21.76 ± 5.01 / 39.73 ± 5.21</td> <!-- SB10k -->
   <td class="de la">0.85 ± 1.86 / 38.42 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de rc">14.30 ± 0.97 / 30.11 ± 2.25</td> <!-- GermanQuAD -->
   <td class="nl ner">38.22 ± 3.45 / 35.62 ± 3.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.99 ± 3.86 / 29.17 ± 2.70</td> <!-- Dutch Social -->
   <td class="nl la">1.85 ± 1.45 / 40.34 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">27.77 ± 1.34 / 36.19 ± 1.60</td> <!-- SQuAD-nl -->
   <td class="en ner">40.45 ± 3.27 / 37.90 ± 2.99</td> <!-- CoNLL-en -->
   <td class="en sent">47.89 ± 3.76 / 56.99 ± 2.11</td> <!-- SST5 -->
   <td class="en la">0.28 ± 1.01 / 44.40 ± 3.07</td> <!-- ScaLA-en -->
   <td class="en rc">26.77 ± 5.45 / 35.60 ± 6.25</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="da-rank">3.69</td> <!-- Danish rank -->
   <td class="no-rank">3.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.42</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.21</td> <!-- Faroese rank -->
   <td class="de-rank">3.67</td> <!-- German rank -->
   <td class="nl-rank">3.94</td> <!-- Dutch rank -->
   <td class="en-rank">3.69</td> <!-- English rank -->
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
   <td class="is sent">20.94 ± 2.82 / 42.72 ± 2.88</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.40 ± 1.40 / 48.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is rc">10.48 ± 1.75 / 28.80 ± 1.59</td> <!-- NQiI -->
   <td class="fo ner">73.34 ± 1.57 / 74.24 ± 1.56</td> <!-- FoNE -->
   <td class="fo sent">1.49 ± 2.48 / 20.15 ± 3.56</td> <!-- FoSent -->
   <td class="fo la">0.97 ± 2.25 / 44.25 ± 3.12</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.01 ± 0.02</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="da-rank">3.82</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.58</td> <!-- Swedish rank -->
   <td class="is-rank">3.79</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.20</td> <!-- Faroese rank -->
   <td class="de-rank">3.69</td> <!-- German rank -->
   <td class="nl-rank">3.94</td> <!-- Dutch rank -->
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
   <td class="is sent">9.46 ± 4.02 / 28.69 ± 4.13</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.04 ± 1.75 / 47.53 ± 1.60</td> <!-- ScaLA-is -->
   <td class="is rc">6.13 ± 0.63 / 21.73 ± 0.95</td> <!-- NQiI -->
   <td class="fo ner">72.08 ± 1.25 / 72.93 ± 1.20</td> <!-- FoNE -->
   <td class="fo sent">-1.81 ± 2.47 / 15.54 ± 0.87</td> <!-- FoSent -->
   <td class="fo la">2.65 ± 2.40 / 48.48 ± 1.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="da-rank">3.70</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.32</td> <!-- Swedish rank -->
   <td class="is-rank">4.21</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.76</td> <!-- Faroese rank -->
   <td class="de-rank">3.82</td> <!-- German rank -->
   <td class="nl-rank">3.78</td> <!-- Dutch rank -->
   <td class="en-rank">3.70</td> <!-- English rank -->
   <td class="da ner">15.93 ± 3.91 / 14.68 ± 2.81</td> <!-- DANSK -->
   <td class="da sent">13.01 ± 2.33 / 28.28 ± 4.63</td> <!-- Angry Tweets -->
   <td class="da la">0.05 ± 1.37 / 40.73 ± 3.78</td> <!-- ScaLA-da -->
   <td class="da rc">36.85 ± 1.28 / 41.96 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="no ner">28.82 ± 3.76 / 28.03 ± 3.72</td> <!-- NorNE-nb -->
   <td class="no ner">27.81 ± 4.34 / 26.00 ± 4.14</td> <!-- NorNE-nn -->
   <td class="no sent">18.74 ± 2.86 / 27.39 ± 3.91</td> <!-- NoReC -->
   <td class="no la">-0.46 ± 1.39 / 36.22 ± 3.32</td> <!-- ScaLA-nb -->
   <td class="no la">-0.84 ± 1.32 / 37.42 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no rc">12.66 ± 1.66 / 21.98 ± 3.16</td> <!-- NorQuAD -->
   <td class="sv ner">21.42 ± 6.21 / 20.27 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">45.75 ± 7.94 / 50.33 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">-0.25 ± 1.25 / 44.95 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.71 ± 2.02 / 37.44 ± 2.20</td> <!-- ScandiQA-sv -->
   <td class="is ner">18.86 ± 5.30 / 18.63 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-0.67 ± 2.61 / 21.03 ± 3.38</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.76 ± 0.76 / 33.16 ± 0.37</td> <!-- ScaLA-is -->
   <td class="is rc">8.09 ± 1.59 / 26.19 ± 2.53</td> <!-- NQiI -->
   <td class="fo ner">22.75 ± 5.63 / 23.52 ± 4.86</td> <!-- FoNE -->
   <td class="fo sent">-0.03 ± 6.54 / 23.66 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">-0.78 ± 1.59 / 33.93 ± 0.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.75 ± 1.53 / 12.38 ± 1.36</td> <!-- FoQA -->
   <td class="de ner">23.08 ± 4.90 / 21.68 ± 4.10</td> <!-- GermEval -->
   <td class="de sent">7.41 ± 5.97 / 23.37 ± 5.40</td> <!-- SB10k -->
   <td class="de la">0.89 ± 1.81 / 40.64 ± 3.86</td> <!-- ScaLA-de -->
   <td class="de rc">17.32 ± 1.06 / 33.36 ± 2.38</td> <!-- GermanQuAD -->
   <td class="nl ner">31.13 ± 3.71 / 29.34 ± 2.26</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.24 ± 2.08 / 29.45 ± 4.63</td> <!-- Dutch Social -->
   <td class="nl la">1.23 ± 1.73 / 44.71 ± 3.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.13 ± 0.85 / 39.28 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="en ner">27.37 ± 4.57 / 26.50 ± 4.52</td> <!-- CoNLL-en -->
   <td class="en sent">36.35 ± 7.92 / 45.58 ± 8.18</td> <!-- SST5 -->
   <td class="en la">-0.37 ± 1.89 / 44.67 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en rc">7.42 ± 2.13 / 16.44 ± 2.71</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="da-rank">3.41</td> <!-- Danish rank -->
   <td class="no-rank">4.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.69</td> <!-- Swedish rank -->
   <td class="is-rank">4.10</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.80</td> <!-- Faroese rank -->
   <td class="de-rank">3.97</td> <!-- German rank -->
   <td class="nl-rank">3.92</td> <!-- Dutch rank -->
   <td class="en-rank">3.41</td> <!-- English rank -->
   <td class="da ner">16.17 ± 3.44 / 14.33 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">29.12 ± 4.09 / 49.93 ± 4.45</td> <!-- Angry Tweets -->
   <td class="da la">-0.47 ± 0.62 / 33.18 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da rc">34.80 ± 1.08 / 41.23 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="no ner">27.47 ± 4.87 / 27.10 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">23.82 ± 4.37 / 27.33 ± 3.71</td> <!-- NorNE-nn -->
   <td class="no sent">22.22 ± 1.30 / 32.60 ± 1.49</td> <!-- NoReC -->
   <td class="no la">-2.06 ± 1.97 / 35.29 ± 1.70</td> <!-- ScaLA-nb -->
   <td class="no la">-0.77 ± 1.41 / 35.74 ± 1.76</td> <!-- ScaLA-nn -->
   <td class="no rc">2.48 ± 1.20 / 5.33 ± 1.94</td> <!-- NorQuAD -->
   <td class="sv ner">14.09 ± 5.11 / 15.95 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">23.71 ± 6.92 / 32.87 ± 7.00</td> <!-- SweReC -->
   <td class="sv la">1.74 ± 1.73 / 38.94 ± 3.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.00 ± 1.48 / 37.80 ± 1.63</td> <!-- ScandiQA-sv -->
   <td class="is ner">9.90 ± 5.26 / 15.24 ± 2.90</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.13 ± 2.07 / 21.55 ± 2.63</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.02 ± 1.43 / 34.31 ± 2.24</td> <!-- ScaLA-is -->
   <td class="is rc">10.64 ± 2.56 / 31.31 ± 1.47</td> <!-- NQiI -->
   <td class="fo ner">20.76 ± 6.32 / 22.79 ± 5.85</td> <!-- FoNE -->
   <td class="fo sent">-1.78 ± 2.38 / 16.36 ± 2.94</td> <!-- FoSent -->
   <td class="fo la">0.87 ± 1.94 / 34.86 ± 1.71</td> <!-- ScaLA-fo -->
   <td class="fo rc">3.58 ± 2.75 / 6.25 ± 4.69</td> <!-- FoQA -->
   <td class="de ner">24.32 ± 2.91 / 22.08 ± 1.97</td> <!-- GermEval -->
   <td class="de sent">15.58 ± 3.73 / 29.45 ± 4.32</td> <!-- SB10k -->
   <td class="de la">1.25 ± 1.70 / 37.57 ± 3.82</td> <!-- ScaLA-de -->
   <td class="de rc">6.82 ± 2.39 / 20.51 ± 3.06</td> <!-- GermanQuAD -->
   <td class="nl ner">23.58 ± 4.08 / 26.01 ± 4.43</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 3.56 / 33.04 ± 3.49</td> <!-- Dutch Social -->
   <td class="nl la">1.79 ± 1.38 / 40.53 ± 3.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.11 ± 2.05 / 35.07 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="en ner">21.60 ± 4.23 / 23.22 ± 3.33</td> <!-- CoNLL-en -->
   <td class="en sent">45.04 ± 5.19 / 50.60 ± 4.14</td> <!-- SST5 -->
   <td class="en la">-0.46 ± 1.47 / 44.56 ± 3.38</td> <!-- ScaLA-en -->
   <td class="en rc">33.46 ± 2.84 / 44.25 ± 3.38</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.03</td> <!-- ScandEval rank -->
   <td class="da-rank">4.10</td> <!-- Danish rank -->
   <td class="no-rank">4.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.83</td> <!-- Swedish rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.68</td> <!-- Faroese rank -->
   <td class="de-rank">3.93</td> <!-- German rank -->
   <td class="nl-rank">4.17</td> <!-- Dutch rank -->
   <td class="en-rank">2.92</td> <!-- English rank -->
   <td class="da ner">8.97 ± 3.18 / 8.62 ± 2.72</td> <!-- DANSK -->
   <td class="da sent">2.66 ± 2.70 / 16.29 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.38 / 44.50 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">24.92 ± 1.68 / 28.73 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="no ner">20.37 ± 5.55 / 21.57 ± 3.57</td> <!-- NorNE-nb -->
   <td class="no ner">21.27 ± 5.10 / 22.34 ± 4.41</td> <!-- NorNE-nn -->
   <td class="no sent">7.60 ± 2.24 / 26.47 ± 2.89</td> <!-- NoReC -->
   <td class="no la">1.31 ± 1.92 / 45.75 ± 3.36</td> <!-- ScaLA-nb -->
   <td class="no la">0.51 ± 1.81 / 38.71 ± 2.95</td> <!-- ScaLA-nn -->
   <td class="no rc">4.80 ± 1.18 / 10.53 ± 2.12</td> <!-- NorQuAD -->
   <td class="sv ner">13.64 ± 5.84 / 16.38 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">9.34 ± 6.26 / 26.00 ± 3.56</td> <!-- SweReC -->
   <td class="sv la">2.20 ± 1.59 / 41.62 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">26.06 ± 2.35 / 30.05 ± 2.29</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.60 ± 1.50 / 13.99 ± 1.39</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.12 ± 4.92 / 27.55 ± 4.21</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.28 ± 1.41 / 37.58 ± 4.34</td> <!-- ScaLA-is -->
   <td class="is rc">4.09 ± 1.03 / 16.34 ± 2.86</td> <!-- NQiI -->
   <td class="fo ner">26.85 ± 3.99 / 27.35 ± 3.60</td> <!-- FoNE -->
   <td class="fo sent">3.07 ± 2.88 / 28.68 ± 2.63</td> <!-- FoSent -->
   <td class="fo la">-0.12 ± 1.62 / 45.84 ± 3.59</td> <!-- ScaLA-fo -->
   <td class="fo rc">1.39 ± 0.54 / 4.02 ± 0.64</td> <!-- FoQA -->
   <td class="de ner">18.77 ± 3.96 / 18.65 ± 3.26</td> <!-- GermEval -->
   <td class="de sent">12.59 ± 3.85 / 22.64 ± 2.25</td> <!-- SB10k -->
   <td class="de la">1.64 ± 1.30 / 34.84 ± 2.12</td> <!-- ScaLA-de -->
   <td class="de rc">9.27 ± 1.07 / 21.58 ± 1.37</td> <!-- GermanQuAD -->
   <td class="nl ner">15.68 ± 5.54 / 22.21 ± 5.42</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.73 ± 2.20 / 27.67 ± 4.00</td> <!-- Dutch Social -->
   <td class="nl la">0.63 ± 1.05 / 43.48 ± 2.98</td> <!-- ScaLA-nl -->
   <td class="nl rc">19.73 ± 1.42 / 27.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="en ner">30.73 ± 4.30 / 29.47 ± 4.10</td> <!-- CoNLL-en -->
   <td class="en sent">59.51 ± 3.73 / 54.82 ± 2.43</td> <!-- SST5 -->
   <td class="en la">1.55 ± 1.90 / 43.18 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en rc">49.03 ± 1.47 / 60.00 ± 1.53</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.03</td> <!-- ScandEval rank -->
   <td class="da-rank">3.98</td> <!-- Danish rank -->
   <td class="no-rank">4.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.86</td> <!-- Swedish rank -->
   <td class="is-rank">4.28</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.77</td> <!-- Faroese rank -->
   <td class="de-rank">3.87</td> <!-- German rank -->
   <td class="nl-rank">4.12</td> <!-- Dutch rank -->
   <td class="en-rank">3.11</td> <!-- English rank -->
   <td class="da ner">12.68 ± 1.39 / 12.32 ± 1.19</td> <!-- DANSK -->
   <td class="da sent">3.61 ± 2.69 / 19.01 ± 3.95</td> <!-- Angry Tweets -->
   <td class="da la">1.79 ± 0.97 / 36.23 ± 3.19</td> <!-- ScaLA-da -->
   <td class="da rc">28.12 ± 3.14 / 32.48 ± 3.57</td> <!-- ScandiQA-da -->
   <td class="no ner">26.60 ± 1.99 / 23.60 ± 2.05</td> <!-- NorNE-nb -->
   <td class="no ner">23.70 ± 1.58 / 23.04 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">6.21 ± 2.55 / 23.74 ± 3.28</td> <!-- NoReC -->
   <td class="no la">-0.39 ± 0.76 / 33.40 ± 0.31</td> <!-- ScaLA-nb -->
   <td class="no la">0.21 ± 0.41 / 35.33 ± 3.02</td> <!-- ScaLA-nn -->
   <td class="no rc">4.65 ± 1.00 / 10.23 ± 1.68</td> <!-- NorQuAD -->
   <td class="sv ner">18.22 ± 1.75 / 17.97 ± 2.10</td> <!-- SUC3 -->
   <td class="sv sent">11.52 ± 7.20 / 29.30 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.72 ± 1.21 / 34.96 ± 1.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">27.27 ± 3.03 / 31.25 ± 3.24</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.43 ± 1.36 / 13.81 ± 1.45</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.82 ± 2.09 / 24.09 ± 2.81</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">1.14 ± 1.52 / 36.93 ± 3.69</td> <!-- ScaLA-is -->
   <td class="is rc">3.71 ± 1.14 / 16.21 ± 2.86</td> <!-- NQiI -->
   <td class="fo ner">28.14 ± 2.42 / 28.12 ± 2.55</td> <!-- FoNE -->
   <td class="fo sent">-0.56 ± 5.13 / 23.83 ± 3.35</td> <!-- FoSent -->
   <td class="fo la">-0.06 ± 0.67 / 33.85 ± 0.68</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.43 ± 0.73 / 6.05 ± 0.59</td> <!-- FoQA -->
   <td class="de ner">19.94 ± 0.96 / 18.01 ± 0.59</td> <!-- GermEval -->
   <td class="de sent">19.64 ± 5.59 / 36.97 ± 5.41</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.32 ± 0.30</td> <!-- ScaLA-de -->
   <td class="de rc">8.78 ± 1.33 / 20.50 ± 1.50</td> <!-- GermanQuAD -->
   <td class="nl ner">20.95 ± 2.02 / 25.63 ± 1.96</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.84 ± 1.76 / 27.74 ± 5.49</td> <!-- Dutch Social -->
   <td class="nl la">-1.50 ± 1.30 / 34.07 ± 0.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.67 ± 1.77 / 30.14 ± 1.68</td> <!-- SQuAD-nl -->
   <td class="en ner">31.14 ± 1.79 / 28.54 ± 0.86</td> <!-- CoNLL-en -->
   <td class="en sent">43.97 ± 5.28 / 55.08 ± 4.26</td> <!-- SST5 -->
   <td class="en la">3.49 ± 2.49 / 46.52 ± 4.13</td> <!-- ScaLA-en -->
   <td class="en rc">47.91 ± 4.97 / 60.41 ± 3.91</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">4.14</td> <!-- ScandEval rank -->
   <td class="da-rank">3.92</td> <!-- Danish rank -->
   <td class="no-rank">4.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.94</td> <!-- Swedish rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.68</td> <!-- Faroese rank -->
   <td class="de-rank">3.94</td> <!-- German rank -->
   <td class="nl-rank">4.32</td> <!-- Dutch rank -->
   <td class="en-rank">3.74</td> <!-- English rank -->
   <td class="da ner">13.84 ± 1.95 / 13.12 ± 1.60</td> <!-- DANSK -->
   <td class="da sent">9.47 ± 3.30 / 25.66 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.36 ± 1.60 / 39.52 ± 3.19</td> <!-- ScaLA-da -->
   <td class="da rc">22.10 ± 2.03 / 26.85 ± 2.16</td> <!-- ScandiQA-da -->
   <td class="no ner">26.59 ± 2.14 / 26.61 ± 2.49</td> <!-- NorNE-nb -->
   <td class="no ner">26.78 ± 1.46 / 26.94 ± 1.92</td> <!-- NorNE-nn -->
   <td class="no sent">7.91 ± 2.20 / 17.44 ± 3.42</td> <!-- NoReC -->
   <td class="no la">0.28 ± 1.08 / 36.00 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">0.04 ± 1.65 / 41.17 ± 5.30</td> <!-- ScaLA-nn -->
   <td class="no rc">0.65 ± 0.40 / 2.88 ± 1.01</td> <!-- NorQuAD -->
   <td class="sv ner">22.09 ± 2.91 / 21.86 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">14.15 ± 7.21 / 25.90 ± 4.05</td> <!-- SweReC -->
   <td class="sv la">-0.04 ± 1.25 / 36.18 ± 3.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">21.60 ± 1.52 / 26.25 ± 1.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">17.73 ± 1.58 / 18.22 ± 1.53</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.38 ± 2.00 / 21.79 ± 2.03</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.18 ± 1.21 / 37.94 ± 4.17</td> <!-- ScaLA-is -->
   <td class="is rc">1.59 ± 0.83 / 12.57 ± 3.10</td> <!-- NQiI -->
   <td class="fo ner">31.99 ± 3.53 / 32.31 ± 3.75</td> <!-- FoNE -->
   <td class="fo sent">0.00 ± 0.00 / 13.57 ± 0.43</td> <!-- FoSent -->
   <td class="fo la">0.48 ± 1.60 / 37.69 ± 4.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.29 ± 0.29 / 0.89 ± 0.74</td> <!-- FoQA -->
   <td class="de ner">25.30 ± 2.32 / 24.21 ± 2.13</td> <!-- GermEval -->
   <td class="de sent">13.90 ± 5.43 / 30.42 ± 6.17</td> <!-- SB10k -->
   <td class="de la">-0.25 ± 1.90 / 39.25 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de rc">6.12 ± 0.63 / 15.65 ± 1.66</td> <!-- GermanQuAD -->
   <td class="nl ner">24.47 ± 2.03 / 26.64 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.57 ± 2.03 / 16.42 ± 3.18</td> <!-- Dutch Social -->
   <td class="nl la">-2.03 ± 1.35 / 39.46 ± 4.09</td> <!-- ScaLA-nl -->
   <td class="nl rc">10.18 ± 1.78 / 17.17 ± 2.17</td> <!-- SQuAD-nl -->
   <td class="en ner">31.79 ± 3.88 / 31.32 ± 2.81</td> <!-- CoNLL-en -->
   <td class="en sent">19.13 ± 9.92 / 33.51 ± 6.97</td> <!-- SST5 -->
   <td class="en la">-0.03 ± 1.07 / 36.37 ± 2.34</td> <!-- ScaLA-en -->
   <td class="en rc">12.35 ± 1.80 / 21.93 ± 1.63</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="da-rank">4.02</td> <!-- Danish rank -->
   <td class="no-rank">4.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.91</td> <!-- Swedish rank -->
   <td class="is-rank">4.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.81</td> <!-- Faroese rank -->
   <td class="de-rank">4.06</td> <!-- German rank -->
   <td class="nl-rank">4.33</td> <!-- Dutch rank -->
   <td class="en-rank">3.75</td> <!-- English rank -->
   <td class="da ner">10.59 ± 2.24 / 10.29 ± 1.37</td> <!-- DANSK -->
   <td class="da sent">13.31 ± 3.23 / 34.38 ± 3.13</td> <!-- Angry Tweets -->
   <td class="da la">0.52 ± 0.78 / 33.76 ± 0.37</td> <!-- ScaLA-da -->
   <td class="da rc">16.61 ± 2.60 / 20.46 ± 2.96</td> <!-- ScandiQA-da -->
   <td class="no ner">25.02 ± 2.09 / 25.54 ± 2.29</td> <!-- NorNE-nb -->
   <td class="no ner">21.59 ± 3.84 / 21.51 ± 4.17</td> <!-- NorNE-nn -->
   <td class="no sent">8.05 ± 2.35 / 22.59 ± 2.42</td> <!-- NoReC -->
   <td class="no la">-0.15 ± 1.40 / 36.65 ± 4.39</td> <!-- ScaLA-nb -->
   <td class="no la">-0.97 ± 1.78 / 39.00 ± 3.45</td> <!-- ScaLA-nn -->
   <td class="no rc">0.37 ± 0.29 / 2.47 ± 0.84</td> <!-- NorQuAD -->
   <td class="sv ner">16.28 ± 4.73 / 16.34 ± 4.84</td> <!-- SUC3 -->
   <td class="sv sent">17.38 ± 10.26 / 34.60 ± 5.85</td> <!-- SweReC -->
   <td class="sv la">-0.45 ± 0.67 / 36.19 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.78 ± 2.45 / 22.13 ± 2.29</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.80 ± 3.19 / 14.46 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">2.17 ± 2.73 / 22.31 ± 3.55</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.63 ± 0.78 / 36.66 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is rc">1.29 ± 0.69 / 10.96 ± 2.80</td> <!-- NQiI -->
   <td class="fo ner">22.55 ± 5.84 / 22.62 ± 6.04</td> <!-- FoNE -->
   <td class="fo sent">0.67 ± 1.52 / 13.76 ± 0.51</td> <!-- FoSent -->
   <td class="fo la">0.87 ± 1.83 / 38.38 ± 4.75</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.27 ± 0.26 / 0.91 ± 0.72</td> <!-- FoQA -->
   <td class="de ner">21.03 ± 2.96 / 21.02 ± 2.73</td> <!-- GermEval -->
   <td class="de sent">10.99 ± 6.72 / 27.88 ± 6.96</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.96 / 36.48 ± 3.10</td> <!-- ScaLA-de -->
   <td class="de rc">3.61 ± 0.37 / 11.45 ± 1.56</td> <!-- GermanQuAD -->
   <td class="nl ner">21.32 ± 2.14 / 22.20 ± 2.65</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.37 ± 2.16 / 18.06 ± 2.83</td> <!-- Dutch Social -->
   <td class="nl la">-0.19 ± 1.24 / 41.66 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">9.38 ± 1.20 / 15.78 ± 1.26</td> <!-- SQuAD-nl -->
   <td class="en ner">27.45 ± 4.13 / 27.11 ± 3.47</td> <!-- CoNLL-en -->
   <td class="en sent">27.39 ± 8.29 / 39.38 ± 6.65</td> <!-- SST5 -->
   <td class="en la">0.31 ± 1.47 / 39.37 ± 3.75</td> <!-- ScaLA-en -->
   <td class="en rc">15.62 ± 2.29 / 26.76 ± 1.43</td> <!-- SQuAD -->
   <td>14.0.4</td> <!-- DANSK version -->
   <td>14.1.2</td> <!-- Angry Tweets version -->
   <td>14.1.2</td> <!-- ScaLA-da version -->
   <td>14.0.4</td> <!-- ScandiQA-da version -->
   <td>14.0.4</td> <!-- NorNE-nb version -->
   <td>14.0.4</td> <!-- NorNE-nn version -->
   <td>14.1.2</td> <!-- NoReC version -->
   <td>14.1.2</td> <!-- ScaLA-nb version -->
   <td>14.1.2</td> <!-- ScaLA-nn version -->
   <td>14.0.4</td> <!-- NorQuAD version -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.1.2</td> <!-- SweReC version -->
   <td>14.1.2</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   <td>14.0.4</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>14.1.2</td> <!-- ScaLA-is version -->
   <td>14.0.4</td> <!-- NQiI version -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   <td>14.0.4</td> <!-- GermEval version -->
   <td>14.1.2</td> <!-- SB10k version -->
   <td>14.1.2</td> <!-- ScaLA-de version -->
   <td>14.0.4</td> <!-- GermanQuAD version -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.1.2</td> <!-- SST5 version -->
   <td>14.1.2</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="da-rank">4.11</td> <!-- Danish rank -->
   <td class="no-rank">4.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.89</td> <!-- Swedish rank -->
   <td class="is-rank">4.01</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.44</td> <!-- Faroese rank -->
   <td class="de-rank">4.18</td> <!-- German rank -->
   <td class="nl-rank">4.63</td> <!-- Dutch rank -->
   <td class="en-rank">4.13</td> <!-- English rank -->
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
   <td class="is sent">25.25 ± 3.12 / 44.40 ± 4.52</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.06 ± 0.99 / 36.73 ± 3.00</td> <!-- ScaLA-is -->
   <td class="is rc">1.02 ± 0.30 / 21.61 ± 1.10</td> <!-- NQiI -->
   <td class="fo ner">48.70 ± 1.57 / 48.51 ± 1.57</td> <!-- FoNE -->
   <td class="fo sent">1.07 ± 2.10 / 17.71 ± 4.10</td> <!-- FoSent -->
   <td class="fo la">2.37 ± 2.06 / 37.68 ± 3.25</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
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
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="da-rank">4.13</td> <!-- Danish rank -->
   <td class="no-rank">4.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.18</td> <!-- Swedish rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.75</td> <!-- Faroese rank -->
   <td class="de-rank">4.42</td> <!-- German rank -->
   <td class="nl-rank">4.59</td> <!-- Dutch rank -->
   <td class="en-rank">3.66</td> <!-- English rank -->
   <td class="da ner">13.72 ± 1.83 / 13.41 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">3.79 ± 3.11 / 21.06 ± 4.74</td> <!-- Angry Tweets -->
   <td class="da la">-0.45 ± 0.70 / 39.69 ± 4.95</td> <!-- ScaLA-da -->
   <td class="da rc">14.69 ± 2.86 / 17.28 ± 3.01</td> <!-- ScandiQA-da -->
   <td class="no ner">24.37 ± 2.17 / 26.91 ± 2.28</td> <!-- NorNE-nb -->
   <td class="no ner">24.69 ± 1.85 / 27.60 ± 2.48</td> <!-- NorNE-nn -->
   <td class="no sent">8.84 ± 4.19 / 29.74 ± 3.45</td> <!-- NoReC -->
   <td class="no la">-1.20 ± 1.10 / 36.09 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">-0.50 ± 1.21 / 36.68 ± 3.16</td> <!-- ScaLA-nn -->
   <td class="no rc">0.16 ± 0.13 / 2.31 ± 0.44</td> <!-- NorQuAD -->
   <td class="sv ner">19.15 ± 1.75 / 20.52 ± 1.77</td> <!-- SUC3 -->
   <td class="sv sent">-3.03 ± 7.40 / 24.39 ± 3.87</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.12 / 36.05 ± 2.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.18 ± 3.82 / 16.55 ± 4.25</td> <!-- ScandiQA-sv -->
   <td class="is ner">14.74 ± 2.42 / 16.01 ± 2.04</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.13 ± 3.12 / 22.51 ± 2.62</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.25 ± 0.60 / 34.69 ± 3.02</td> <!-- ScaLA-is -->
   <td class="is rc">1.35 ± 0.73 / 10.92 ± 2.52</td> <!-- NQiI -->
   <td class="fo ner">25.51 ± 2.40 / 26.43 ± 1.77</td> <!-- FoNE -->
   <td class="fo sent">-0.24 ± 2.92 / 26.18 ± 4.52</td> <!-- FoSent -->
   <td class="fo la">0.46 ± 1.43 / 36.19 ± 3.30</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.15 ± 0.20 / 3.01 ± 0.44</td> <!-- FoQA -->
   <td class="de ner">16.89 ± 1.62 / 16.63 ± 1.80</td> <!-- GermEval -->
   <td class="de sent">2.74 ± 3.46 / 23.30 ± 3.11</td> <!-- SB10k -->
   <td class="de la">-0.34 ± 1.06 / 39.21 ± 4.13</td> <!-- ScaLA-de -->
   <td class="de rc">0.28 ± 0.27 / 2.91 ± 0.92</td> <!-- GermanQuAD -->
   <td class="nl ner">17.49 ± 2.94 / 18.59 ± 2.66</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.01 ± 1.88 / 15.88 ± 1.32</td> <!-- Dutch Social -->
   <td class="nl la">-0.02 ± 0.15 / 34.86 ± 2.12</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.53 ± 0.36 / 3.23 ± 0.51</td> <!-- SQuAD-nl -->
   <td class="en ner">31.26 ± 3.84 / 30.44 ± 3.28</td> <!-- CoNLL-en -->
   <td class="en sent">26.69 ± 10.82 / 34.46 ± 8.00</td> <!-- SST5 -->
   <td class="en la">1.78 ± 1.67 / 43.50 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">13.88 ± 1.36 / 22.49 ± 2.14</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="da-rank">4.22</td> <!-- Danish rank -->
   <td class="no-rank">4.41</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.12</td> <!-- Swedish rank -->
   <td class="is-rank">4.35</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.71</td> <!-- Faroese rank -->
   <td class="de-rank">4.39</td> <!-- German rank -->
   <td class="nl-rank">4.63</td> <!-- Dutch rank -->
   <td class="en-rank">3.71</td> <!-- English rank -->
   <td class="da ner">12.11 ± 1.07 / 11.48 ± 1.07</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 3.22 / 18.95 ± 3.93</td> <!-- Angry Tweets -->
   <td class="da la">0.25 ± 1.87 / 39.65 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da rc">14.02 ± 2.56 / 16.74 ± 2.74</td> <!-- ScandiQA-da -->
   <td class="no ner">20.89 ± 2.55 / 22.28 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">19.62 ± 1.91 / 21.82 ± 2.35</td> <!-- NorNE-nn -->
   <td class="no sent">2.78 ± 4.25 / 26.17 ± 3.37</td> <!-- NoReC -->
   <td class="no la">-0.98 ± 1.80 / 40.63 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">0.93 ± 2.26 / 40.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no rc">0.15 ± 0.13 / 2.19 ± 0.57</td> <!-- NorQuAD -->
   <td class="sv ner">17.09 ± 2.33 / 18.78 ± 2.11</td> <!-- SUC3 -->
   <td class="sv sent">7.41 ± 9.32 / 28.42 ± 3.18</td> <!-- SweReC -->
   <td class="sv la">0.47 ± 1.48 / 38.19 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">11.73 ± 3.22 / 13.94 ± 3.48</td> <!-- ScandiQA-sv -->
   <td class="is ner">13.70 ± 2.05 / 15.01 ± 2.07</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">3.01 ± 2.55 / 22.58 ± 2.22</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">-0.83 ± 0.71 / 32.99 ± 0.27</td> <!-- ScaLA-is -->
   <td class="is rc">0.94 ± 0.54 / 10.22 ± 2.52</td> <!-- NQiI -->
   <td class="fo ner">23.22 ± 3.22 / 24.30 ± 2.81</td> <!-- FoNE -->
   <td class="fo sent">3.78 ± 2.95 / 27.36 ± 2.62</td> <!-- FoSent -->
   <td class="fo la">0.41 ± 2.39 / 39.64 ± 3.47</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.54 ± 0.33 / 3.34 ± 0.61</td> <!-- FoQA -->
   <td class="de ner">15.54 ± 1.74 / 15.29 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">2.51 ± 1.90 / 21.27 ± 3.22</td> <!-- SB10k -->
   <td class="de la">0.36 ± 1.07 / 39.04 ± 3.21</td> <!-- ScaLA-de -->
   <td class="de rc">1.77 ± 0.67 / 5.69 ± 0.96</td> <!-- GermanQuAD -->
   <td class="nl ner">15.82 ± 3.13 / 16.46 ± 2.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.62 ± 1.55 / 16.18 ± 1.88</td> <!-- Dutch Social -->
   <td class="nl la">1.16 ± 1.38 / 34.30 ± 1.27</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.25 ± 1.17 / 5.89 ± 0.97</td> <!-- SQuAD-nl -->
   <td class="en ner">29.96 ± 3.19 / 28.98 ± 3.29</td> <!-- CoNLL-en -->
   <td class="en sent">18.64 ± 8.52 / 28.83 ± 5.86</td> <!-- SST5 -->
   <td class="en la">1.85 ± 1.20 / 44.03 ± 3.98</td> <!-- ScaLA-en -->
   <td class="en rc">26.90 ± 1.56 / 36.91 ± 1.53</td> <!-- SQuAD -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.3.0</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="da-rank">4.66</td> <!-- Danish rank -->
   <td class="no-rank">4.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.72</td> <!-- Swedish rank -->
   <td class="is-rank">4.63</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.14</td> <!-- Faroese rank -->
   <td class="de-rank">4.65</td> <!-- German rank -->
   <td class="nl-rank">4.90</td> <!-- Dutch rank -->
   <td class="en-rank">4.60</td> <!-- English rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.02 ± 0.02 / 0.03 ± 0.03</td> <!-- ScandiQA-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.09 ± 0.03</td> <!-- NorQuAD -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.16 ± 0.14</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is sent">-1.30 ± 1.45 / 18.79 ± 0.29</td> <!-- Hotter-and-Colder-sentiment -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo sent">0.74 ± 1.78 / 13.97 ± 0.80</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- GermanQuAD -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 8.62 ± 0.30</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 0.01 ± 0.00</td> <!-- SQuAD-nl -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">2.48 ± 1.94 / 34.52 ± 0.85</td> <!-- ScaLA-en -->
   <td class="en rc">0.01 ± 0.02 / 0.03 ± 0.02</td> <!-- SQuAD -->
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
   <td>14.1.2</td> <!-- Hotter-and-Colder-sentiment version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
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
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/germanic-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
