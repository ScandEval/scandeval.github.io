---
layout: leaderboard
title: Germanic NLG 🇪🇺
---

<center>Last updated: 19/07/2024 11:42:15 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="germanic-nlg" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish summarization - BERTScore / ROUGE-L">Nordjylland-News</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">Danske Talemaader</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">Danish Citizen Tests</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian summarization - BERTScore / ROUGE-L">No Sammendrag</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact Match / F1-score">ScandiQA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish summarization - BERTScore / ROUGE-L">SweDN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">Winogrande-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German summarization - BERTScore / ROUGE-L">MLSum</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch question answering - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch summarization - BERTScore / ROUGE-L">Wiki-Lingua-NL</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English question answering - Exact Match / F1-score">SQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English summarization - BERTScore / ROUGE-L">CNN-DailyMail</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English knowledge - Matthews Correlation Coefficient / Accuracy">MMLU</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on DANSK">DANSK version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Angry Tweets">Angry Tweets version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-da">ScaLA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-da">ScandiQA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Nordjylland-News">Nordjylland-News version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Danske Talemaader">Danske Talemaader version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Danish Citizen Tests">Danish Citizen Tests version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-da">HellaSwag-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nb">NorNE-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorNE-nn">NorNE-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NoReC">NoReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on No Sammendrag">No Sammendrag version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nb">ScaLA-nb version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nn">ScaLA-nn version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NorQuAD">NorQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-no">MMLU-no version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-no">HellaSwag-no version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SUC3">SUC3 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweReC">SweReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-sv">ScaLA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-sv">ScandiQA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweDN">SweDN version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-sv">MMLU-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-sv">HellaSwag-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MIM-GOLD-NER">MIM-GOLD-NER version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-is">ScaLA-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on NQiI">NQiI version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on RRN">RRN version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-is">MMLU-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Winogrande-is">Winogrande-is version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermEval">GermEval version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SB10k">SB10k version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-de">ScaLA-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermanQuAD">GermanQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MLSum">MLSum version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-de">MMLU-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-de">HellaSwag-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-nl">CoNLL-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Dutch Social">Dutch Social version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nl">ScaLA-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD-nl">SQuAD-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Wiki-Lingua-NL">Wiki-Lingua-NL version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-nl">MMLU-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-nl">HellaSwag-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-en">CoNLL-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SST5">SST5 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-en">ScaLA-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD">SQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CNN-DailyMail">CNN-DailyMail version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU">MMLU version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag">HellaSwag version</span></th>
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
   <td class="rank">1.21</td> <!-- ScandEval rank -->
   <td class="da-rank">1.16</td> <!-- Danish rank -->
   <td class="no-rank">1.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.11</td> <!-- Swedish rank -->
   <td class="is-rank">1.52</td> <!-- Icelandic rank -->
   <td class="de-rank">1.18</td> <!-- German rank -->
   <td class="nl-rank">1.14</td> <!-- Dutch rank -->
   <td class="en-rank">1.20</td> <!-- English rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">56.43 ± 2.98 / 68.46 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="da summ">66.76 ± 0.34 / 18.99 ± 0.52</td> <!-- Nordjylland-News -->
   <td class="da know">94.93 ± 1.03 / 96.21 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">93.98 ± 2.15 / 95.94 ± 1.44</td> <!-- Danish Citizen Tests -->
   <td class="da reason">81.64 ± 1.80 / 86.17 ± 1.34</td> <!-- HellaSwag-da -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no summ">65.92 ± 0.28 / 19.24 ± 0.59</td> <!-- No Sammendrag -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">47.50 ± 2.86 / 75.24 ± 1.32</td> <!-- NorQuAD -->
   <td class="no know">68.77 ± 2.09 / 76.56 ± 1.57</td> <!-- MMLU-no -->
   <td class="no reason">88.30 ± 1.32 / 91.13 ± 0.98</td> <!-- HellaSwag-no -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.83 ± 0.15 / 22.67 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">72.53 ± 1.82 / 79.26 ± 1.44</td> <!-- MMLU-sv -->
   <td class="sv reason">85.67 ± 2.59 / 89.14 ± 2.05</td> <!-- HellaSwag-sv -->
   <td class="is ner">78.67 ± 2.16 / 59.54 ± 4.85</td> <!-- MIM-GOLD-NER -->
   <td class="is la">33.65 ± 3.19 / 60.56 ± 2.35</td> <!-- ScaLA-is -->
   <td class="is qa">32.25 ± 2.01 / 60.12 ± 1.31</td> <!-- NQiI -->
   <td class="is summ">69.21 ± 0.25 / 22.50 ± 0.53</td> <!-- RRN -->
   <td class="is know">57.27 ± 3.60 / 67.97 ± 2.68</td> <!-- MMLU-is -->
   <td class="is reason">74.02 ± 4.17 / 86.80 ± 2.02</td> <!-- Winogrande-is -->
   <td class="de ner">69.48 ± 2.32 / 54.66 ± 2.17</td> <!-- GermEval -->
   <td class="de sent">64.91 ± 1.86 / 75.96 ± 1.59</td> <!-- SB10k -->
   <td class="de la">50.23 ± 4.16 / 74.54 ± 2.10</td> <!-- ScaLA-de -->
   <td class="de qa">33.17 ± 1.86 / 65.14 ± 1.53</td> <!-- GermanQuAD -->
   <td class="de summ">66.35 ± 0.59 / 19.81 ± 1.46</td> <!-- MLSum -->
   <td class="de know">71.92 ± 2.22 / 78.79 ± 1.65</td> <!-- MMLU-de -->
   <td class="de reason">82.85 ± 1.48 / 86.99 ± 1.12</td> <!-- HellaSwag-de -->
   <td class="nl ner">73.35 ± 2.61 / 56.00 ± 2.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.92 ± 2.78 / 40.80 ± 2.43</td> <!-- Dutch Social -->
   <td class="nl la">76.70 ± 2.39 / 88.16 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.03 ± 1.96 / 76.47 ± 1.22</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.97 ± 0.41 / 22.66 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.71 ± 2.96 / 78.12 ± 2.24</td> <!-- MMLU-nl -->
   <td class="nl reason">90.07 ± 1.29 / 92.54 ± 0.98</td> <!-- HellaSwag-nl -->
   <td class="en ner">78.06 ± 2.73 / 70.76 ± 3.80</td> <!-- CoNLL-en -->
   <td class="en sent">69.06 ± 2.20 / 76.04 ± 1.60</td> <!-- SST5 -->
   <td class="en la">55.76 ± 3.84 / 76.34 ± 1.44</td> <!-- ScaLA-en -->
   <td class="en qa">67.35 ± 1.98 / 85.76 ± 0.77</td> <!-- SQuAD -->
   <td class="en summ">70.54 ± 0.24 / 26.98 ± 0.49</td> <!-- CNN-DailyMail -->
   <td class="en know">72.27 ± 2.36 / 78.75 ± 1.88</td> <!-- MMLU -->
   <td class="en reason">91.51 ± 2.15 / 93.59 ± 1.62</td> <!-- HellaSwag -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- No Sammendrag version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- MMLU-no version -->
   <td>9.3.2</td> <!-- HellaSwag-no version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.0</td> <!-- MMLU-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   <td>12.2.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.2.0</td> <!-- ScaLA-en version -->
   <td>12.2.0</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.25</td> <!-- ScandEval rank -->
   <td class="da-rank">1.20</td> <!-- Danish rank -->
   <td class="no-rank">1.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.19</td> <!-- Swedish rank -->
   <td class="is-rank">1.18</td> <!-- Icelandic rank -->
   <td class="de-rank">1.32</td> <!-- German rank -->
   <td class="nl-rank">1.43</td> <!-- Dutch rank -->
   <td class="en-rank">1.15</td> <!-- English rank -->
   <td class="da ner">66.80 ± 3.01 / 45.69 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">61.62 ± 2.17 / 73.99 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">66.84 ± 3.27 / 82.79 ± 1.86</td> <!-- ScaLA-da -->
   <td class="da qa">56.85 ± 2.62 / 68.83 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">66.21 ± 0.44 / 18.02 ± 0.61</td> <!-- Nordjylland-News -->
   <td class="da know">95.21 ± 0.55 / 96.41 ± 0.41</td> <!-- Danske Talemaader -->
   <td class="da know">97.19 ± 1.15 / 98.12 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">78.74 ± 3.12 / 83.91 ± 2.42</td> <!-- HellaSwag-da -->
   <td class="no ner">77.48 ± 2.32 / 55.87 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">78.70 ± 2.78 / 57.58 ± 4.23</td> <!-- NorNE-nn -->
   <td class="no sent">62.55 ± 2.82 / 72.41 ± 2.42</td> <!-- NoReC -->
   <td class="no summ">63.60 ± 0.15 / 13.15 ± 0.35</td> <!-- No Sammendrag -->
   <td class="no la">74.45 ± 4.27 / 86.22 ± 2.49</td> <!-- ScaLA-nb -->
   <td class="no la">56.31 ± 5.81 / 74.04 ± 4.03</td> <!-- ScaLA-nn -->
   <td class="no qa">44.67 ± 3.23 / 73.39 ± 1.83</td> <!-- NorQuAD -->
   <td class="no know">70.84 ± 1.92 / 78.12 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">86.30 ± 2.04 / 89.53 ± 1.60</td> <!-- HellaSwag-no -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.08 ± 0.14 / 17.19 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">71.32 ± 1.56 / 78.48 ± 1.15</td> <!-- MMLU-sv -->
   <td class="sv reason">84.09 ± 2.99 / 88.01 ± 2.26</td> <!-- HellaSwag-sv -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is qa">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">69.61 ± 0.61 / 23.98 ± 1.17</td> <!-- RRN -->
   <td class="is know">63.55 ± 3.26 / 72.66 ± 2.43</td> <!-- MMLU-is -->
   <td class="is reason">72.03 ± 3.91 / 86.09 ± 1.96</td> <!-- Winogrande-is -->
   <td class="de ner">68.94 ± 2.50 / 44.89 ± 2.85</td> <!-- GermEval -->
   <td class="de sent">60.47 ± 2.94 / 72.79 ± 1.90</td> <!-- SB10k -->
   <td class="de la">51.26 ± 4.94 / 74.76 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de qa">30.04 ± 1.30 / 58.77 ± 1.50</td> <!-- GermanQuAD -->
   <td class="de summ">63.62 ± 0.65 / 13.08 ± 0.87</td> <!-- MLSum -->
   <td class="de know">73.80 ± 2.03 / 80.31 ± 1.54</td> <!-- MMLU-de -->
   <td class="de reason">83.93 ± 2.38 / 87.85 ± 1.80</td> <!-- HellaSwag-de -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.22 ± 3.26 / 33.41 ± 3.24</td> <!-- Dutch Social -->
   <td class="nl la">72.30 ± 2.26 / 85.96 ± 1.13</td> <!-- ScaLA-nl -->
   <td class="nl qa">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.13 ± 0.50 / 17.61 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.04 ± 1.91 / 77.58 ± 1.42</td> <!-- MMLU-nl -->
   <td class="nl reason">88.29 ± 2.26 / 91.17 ± 1.70</td> <!-- HellaSwag-nl -->
   <td class="en ner">81.79 ± 1.39 / 65.51 ± 4.16</td> <!-- CoNLL-en -->
   <td class="en sent">67.55 ± 2.34 / 74.04 ± 1.80</td> <!-- SST5 -->
   <td class="en la">51.21 ± 4.96 / 75.11 ± 2.42</td> <!-- ScaLA-en -->
   <td class="en qa">66.60 ± 1.45 / 84.48 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">68.80 ± 0.43 / 21.84 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">81.71 ± 1.12 / 86.29 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">89.91 ± 1.81 / 92.38 ± 1.34</td> <!-- HellaSwag -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.2</td> <!-- Danske Talemaader version -->
   <td>12.10.2</td> <!-- Danish Citizen Tests version -->
   <td>12.10.2</td> <!-- HellaSwag-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.2</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- No Sammendrag version -->
   <td>12.10.2</td> <!-- ScaLA-nb version -->
   <td>12.10.2</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.2</td> <!-- MMLU-no version -->
   <td>12.10.2</td> <!-- HellaSwag-no version -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.2</td> <!-- MMLU-sv version -->
   <td>12.10.2</td> <!-- HellaSwag-sv version -->
   <td>12.5.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.5.1</td> <!-- RRN version -->
   <td>12.10.2</td> <!-- MMLU-is version -->
   <td>12.10.2</td> <!-- Winogrande-is version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.10.2</td> <!-- MMLU-de version -->
   <td>12.10.2</td> <!-- HellaSwag-de version -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.3.2</td> <!-- SQuAD-nl version -->
   <td>12.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.2</td> <!-- MMLU version -->
   <td>12.10.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="da-rank">1.22</td> <!-- Danish rank -->
   <td class="no-rank">1.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.19</td> <!-- Swedish rank -->
   <td class="is-rank">1.19</td> <!-- Icelandic rank -->
   <td class="de-rank">1.40</td> <!-- German rank -->
   <td class="nl-rank">1.52</td> <!-- Dutch rank -->
   <td class="en-rank">1.34</td> <!-- English rank -->
   <td class="da ner">71.15 ± 2.89 / 52.24 ± 3.76</td> <!-- DANSK -->
   <td class="da sent">49.42 ± 3.29 / 61.74 ± 2.59</td> <!-- Angry Tweets -->
   <td class="da la">64.59 ± 2.97 / 79.93 ± 1.88</td> <!-- ScaLA-da -->
   <td class="da qa">57.35 ± 2.51 / 67.87 ± 1.75</td> <!-- ScandiQA-da -->
   <td class="da summ">66.03 ± 0.24 / 17.74 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">96.41 ± 0.63 / 97.30 ± 0.48</td> <!-- Danske Talemaader -->
   <td class="da know">97.68 ± 1.06 / 98.44 ± 0.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">85.96 ± 1.48 / 89.41 ± 1.15</td> <!-- HellaSwag-da -->
   <td class="no ner">79.07 ± 3.01 / 64.17 ± 3.51</td> <!-- NorNE-nb -->
   <td class="no ner">81.56 ± 2.45 / 64.06 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">66.66 ± 1.91 / 77.70 ± 1.29</td> <!-- NoReC -->
   <td class="no summ">63.25 ± 0.26 / 13.02 ± 0.33</td> <!-- No Sammendrag -->
   <td class="no la">64.53 ± 6.09 / 79.17 ± 4.89</td> <!-- ScaLA-nb -->
   <td class="no la">54.70 ± 4.36 / 74.94 ± 3.26</td> <!-- ScaLA-nn -->
   <td class="no qa">43.51 ± 3.40 / 74.52 ± 1.79</td> <!-- NorQuAD -->
   <td class="no know">73.81 ± 1.88 / 80.39 ± 1.45</td> <!-- MMLU-no -->
   <td class="no reason">89.91 ± 1.13 / 92.42 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.00 ± 0.29 / 16.97 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">70.70 ± 1.32 / 77.97 ± 0.99</td> <!-- MMLU-sv -->
   <td class="sv reason">86.30 ± 2.23 / 89.65 ± 1.68</td> <!-- HellaSwag-sv -->
   <td class="is ner">81.19 ± 2.45 / 54.02 ± 5.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is qa">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="is summ">68.25 ± 0.27 / 19.22 ± 0.51</td> <!-- RRN -->
   <td class="is know">67.64 ± 2.43 / 75.70 ± 1.76</td> <!-- MMLU-is -->
   <td class="is reason">70.85 ± 5.98 / 85.55 ± 3.05</td> <!-- Winogrande-is -->
   <td class="de ner">69.99 ± 1.63 / 45.58 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">54.82 ± 2.19 / 68.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">43.66 ± 5.67 / 64.64 ± 4.65</td> <!-- ScaLA-de -->
   <td class="de qa">30.06 ± 1.04 / 60.77 ± 1.11</td> <!-- GermanQuAD -->
   <td class="de summ">63.80 ± 0.60 / 13.87 ± 1.05</td> <!-- MLSum -->
   <td class="de know">74.13 ± 1.60 / 80.59 ± 1.22</td> <!-- MMLU-de -->
   <td class="de reason">88.18 ± 1.79 / 91.13 ± 1.34</td> <!-- HellaSwag-de -->
   <td class="nl ner">76.75 ± 3.44 / 61.13 ± 4.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 2.24 / 32.52 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">56.26 ± 4.51 / 73.83 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.55 ± 2.54 / 76.28 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.86 ± 0.46 / 16.93 ± 0.91</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">73.11 ± 1.87 / 79.69 ± 1.46</td> <!-- MMLU-nl -->
   <td class="nl reason">92.69 ± 1.46 / 94.53 ± 1.09</td> <!-- HellaSwag-nl -->
   <td class="en ner">83.48 ± 1.52 / 75.51 ± 2.26</td> <!-- CoNLL-en -->
   <td class="en sent">62.74 ± 2.04 / 71.28 ± 1.46</td> <!-- SST5 -->
   <td class="en la">46.56 ± 3.35 / 71.13 ± 1.97</td> <!-- ScaLA-en -->
   <td class="en qa">65.41 ± 1.96 / 84.78 ± 0.68</td> <!-- SQuAD -->
   <td class="en summ">67.64 ± 0.97 / 20.90 ± 0.92</td> <!-- CNN-DailyMail -->
   <td class="en know">78.55 ± 1.82 / 83.91 ± 1.34</td> <!-- MMLU -->
   <td class="en reason">91.34 ± 1.66 / 93.48 ± 1.27</td> <!-- HellaSwag -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.2</td> <!-- Danske Talemaader version -->
   <td>12.10.2</td> <!-- Danish Citizen Tests version -->
   <td>12.10.2</td> <!-- HellaSwag-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.2</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- No Sammendrag version -->
   <td>12.10.2</td> <!-- ScaLA-nb version -->
   <td>12.10.2</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.2</td> <!-- MMLU-no version -->
   <td>12.10.2</td> <!-- HellaSwag-no version -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.2</td> <!-- MMLU-sv version -->
   <td>12.10.2</td> <!-- HellaSwag-sv version -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.2</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.2</td> <!-- MMLU-is version -->
   <td>12.10.2</td> <!-- Winogrande-is version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.2</td> <!-- MMLU-de version -->
   <td>12.10.2</td> <!-- HellaSwag-de version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.2</td> <!-- MMLU version -->
   <td>12.10.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.49</td> <!-- ScandEval rank -->
   <td class="da-rank">1.41</td> <!-- Danish rank -->
   <td class="no-rank">1.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.32</td> <!-- Swedish rank -->
   <td class="is-rank">2.38</td> <!-- Icelandic rank -->
   <td class="de-rank">1.34</td> <!-- German rank -->
   <td class="nl-rank">1.31</td> <!-- Dutch rank -->
   <td class="en-rank">1.31</td> <!-- English rank -->
   <td class="da ner">63.62 ± 3.74 / 53.29 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">60.19 ± 3.31 / 73.13 ± 2.17</td> <!-- Angry Tweets -->
   <td class="da la">50.07 ± 5.86 / 72.94 ± 4.16</td> <!-- ScaLA-da -->
   <td class="da qa">60.97 ± 2.76 / 66.71 ± 2.27</td> <!-- ScandiQA-da -->
   <td class="da summ">67.33 ± 1.41 / 22.84 ± 1.49</td> <!-- Nordjylland-News -->
   <td class="da know">83.94 ± 1.20 / 87.93 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">78.83 ± 3.17 / 85.39 ± 2.14</td> <!-- Danish Citizen Tests -->
   <td class="da reason">60.69 ± 4.11 / 69.38 ± 3.63</td> <!-- HellaSwag-da -->
   <td class="no ner">75.31 ± 3.84 / 64.90 ± 4.05</td> <!-- NorNE-nb -->
   <td class="no ner">75.94 ± 4.62 / 62.81 ± 5.25</td> <!-- NorNE-nn -->
   <td class="no sent">66.74 ± 4.50 / 74.89 ± 3.69</td> <!-- NoReC -->
   <td class="no summ">65.78 ± 1.11 / 20.46 ± 1.79</td> <!-- No Sammendrag -->
   <td class="no la">59.82 ± 3.52 / 79.17 ± 2.10</td> <!-- ScaLA-nb -->
   <td class="no la">47.56 ± 3.52 / 71.91 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">60.87 ± 4.82 / 82.30 ± 2.52</td> <!-- NorQuAD -->
   <td class="no know">62.45 ± 1.70 / 71.60 ± 1.37</td> <!-- MMLU-no -->
   <td class="no reason">65.29 ± 3.59 / 72.50 ± 3.24</td> <!-- HellaSwag-no -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.41 / 22.47 ± 0.82</td> <!-- SweDN -->
   <td class="sv know">61.55 ± 1.68 / 71.02 ± 1.21</td> <!-- MMLU-sv -->
   <td class="sv reason">66.21 ± 3.22 / 73.40 ± 2.77</td> <!-- HellaSwag-sv -->
   <td class="is ner">75.33 ± 3.06 / 62.43 ± 3.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">14.89 ± 3.28 / 51.55 ± 4.71</td> <!-- ScaLA-is -->
   <td class="is qa">34.36 ± 2.87 / 64.02 ± 2.94</td> <!-- NQiI -->
   <td class="is summ">68.38 ± 0.30 / 21.55 ± 0.76</td> <!-- RRN -->
   <td class="is know">44.34 ± 2.87 / 58.16 ± 2.15</td> <!-- MMLU-is -->
   <td class="is reason">29.46 ± 2.11 / 50.86 ± 1.68</td> <!-- Winogrande-is -->
   <td class="de ner">69.04 ± 2.51 / 61.10 ± 3.39</td> <!-- GermEval -->
   <td class="de sent">63.51 ± 2.57 / 75.01 ± 1.74</td> <!-- SB10k -->
   <td class="de la">37.41 ± 2.43 / 67.63 ± 1.05</td> <!-- ScaLA-de -->
   <td class="de qa">38.29 ± 3.54 / 69.69 ± 2.78</td> <!-- GermanQuAD -->
   <td class="de summ">70.00 ± 1.41 / 29.78 ± 3.58</td> <!-- MLSum -->
   <td class="de know">64.93 ± 2.76 / 73.71 ± 2.07</td> <!-- MMLU-de -->
   <td class="de reason">66.54 ± 4.29 / 74.45 ± 3.24</td> <!-- HellaSwag-de -->
   <td class="nl ner">72.91 ± 3.24 / 68.06 ± 4.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">19.08 ± 3.37 / 42.04 ± 2.31</td> <!-- Dutch Social -->
   <td class="nl la">54.33 ± 3.49 / 75.54 ± 2.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">63.99 ± 2.07 / 77.63 ± 1.16</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.41 ± 0.97 / 25.41 ± 1.66</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.33 ± 1.92 / 73.98 ± 1.56</td> <!-- MMLU-nl -->
   <td class="nl reason">71.06 ± 2.82 / 78.16 ± 2.22</td> <!-- HellaSwag-nl -->
   <td class="en ner">79.06 ± 2.34 / 74.41 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">65.53 ± 2.61 / 68.71 ± 2.08</td> <!-- SST5 -->
   <td class="en la">46.28 ± 4.01 / 72.38 ± 2.33</td> <!-- ScaLA-en -->
   <td class="en qa">75.20 ± 1.68 / 86.90 ± 1.14</td> <!-- SQuAD -->
   <td class="en summ">69.10 ± 0.33 / 21.34 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">72.64 ± 1.98 / 79.49 ± 1.48</td> <!-- MMLU -->
   <td class="en reason">77.49 ± 4.78 / 82.50 ± 3.93</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- No Sammendrag version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- MMLU-no version -->
   <td>12.7.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.7.0</td> <!-- MMLU-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="da-rank">1.65</td> <!-- Danish rank -->
   <td class="no-rank">1.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.80</td> <!-- Swedish rank -->
   <td class="is-rank">2.65</td> <!-- Icelandic rank -->
   <td class="de-rank">1.56</td> <!-- German rank -->
   <td class="nl-rank">1.54</td> <!-- Dutch rank -->
   <td class="en-rank">1.53</td> <!-- English rank -->
   <td class="da ner">63.10 ± 2.12 / 55.10 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">53.09 ± 3.85 / 68.18 ± 2.27</td> <!-- Angry Tweets -->
   <td class="da la">40.98 ± 4.46 / 69.10 ± 2.72</td> <!-- ScaLA-da -->
   <td class="da qa">51.13 ± 1.89 / 63.12 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="da summ">67.76 ± 0.99 / 23.19 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">85.18 ± 1.92 / 88.91 ± 1.44</td> <!-- Danske Talemaader -->
   <td class="da know">79.22 ± 2.40 / 85.70 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">70.19 ± 2.71 / 77.54 ± 2.05</td> <!-- HellaSwag-da -->
   <td class="no ner">80.50 ± 2.85 / 76.71 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">76.47 ± 3.13 / 73.94 ± 2.95</td> <!-- NorNE-nn -->
   <td class="no sent">59.29 ± 5.92 / 69.99 ± 4.80</td> <!-- NoReC -->
   <td class="no summ">65.70 ± 0.63 / 19.36 ± 0.99</td> <!-- No Sammendrag -->
   <td class="no la">47.28 ± 3.57 / 69.23 ± 3.04</td> <!-- ScaLA-nb -->
   <td class="no la">32.76 ± 3.80 / 60.66 ± 3.10</td> <!-- ScaLA-nn -->
   <td class="no qa">39.71 ± 2.59 / 71.60 ± 1.57</td> <!-- NorQuAD -->
   <td class="no know">63.58 ± 1.91 / 72.58 ± 1.42</td> <!-- MMLU-no -->
   <td class="no reason">63.41 ± 2.52 / 71.91 ± 1.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.25 ± 0.18 / 22.84 ± 0.44</td> <!-- SweDN -->
   <td class="sv know">61.31 ± 2.07 / 70.78 ± 1.60</td> <!-- MMLU-sv -->
   <td class="sv reason">66.73 ± 2.34 / 74.65 ± 1.78</td> <!-- HellaSwag-sv -->
   <td class="is ner">72.91 ± 3.48 / 68.22 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.01 ± 4.64 / 50.69 ± 3.23</td> <!-- ScaLA-is -->
   <td class="is qa">31.86 ± 1.86 / 60.66 ± 1.58</td> <!-- NQiI -->
   <td class="is summ">68.30 ± 0.30 / 21.80 ± 0.66</td> <!-- RRN -->
   <td class="is know">37.99 ± 4.28 / 53.36 ± 3.22</td> <!-- MMLU-is -->
   <td class="is reason">27.68 ± 4.21 / 60.39 ± 2.25</td> <!-- Winogrande-is -->
   <td class="de ner">75.20 ± 2.15 / 64.06 ± 3.60</td> <!-- GermEval -->
   <td class="de sent">54.38 ± 3.31 / 68.02 ± 2.21</td> <!-- SB10k -->
   <td class="de la">36.59 ± 4.24 / 67.36 ± 1.77</td> <!-- ScaLA-de -->
   <td class="de qa">26.90 ± 2.67 / 58.28 ± 2.22</td> <!-- GermanQuAD -->
   <td class="de summ">68.63 ± 1.20 / 26.12 ± 3.00</td> <!-- MLSum -->
   <td class="de know">62.69 ± 1.83 / 71.95 ± 1.40</td> <!-- MMLU-de -->
   <td class="de reason">69.18 ± 2.73 / 76.41 ± 2.08</td> <!-- HellaSwag-de -->
   <td class="nl ner">74.64 ± 3.67 / 71.84 ± 4.01</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.90 ± 2.04 / 41.93 ± 1.60</td> <!-- Dutch Social -->
   <td class="nl la">49.54 ± 4.22 / 74.03 ± 2.52</td> <!-- ScaLA-nl -->
   <td class="nl qa">44.77 ± 1.67 / 71.44 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.28 ± 0.65 / 22.72 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.80 ± 3.16 / 74.38 ± 2.37</td> <!-- MMLU-nl -->
   <td class="nl reason">76.21 ± 1.36 / 82.15 ± 1.01</td> <!-- HellaSwag-nl -->
   <td class="en ner">81.30 ± 1.35 / 76.64 ± 1.77</td> <!-- CoNLL-en -->
   <td class="en sent">66.18 ± 2.04 / 72.85 ± 1.27</td> <!-- SST5 -->
   <td class="en la">38.10 ± 2.32 / 68.58 ± 1.40</td> <!-- ScaLA-en -->
   <td class="en qa">53.31 ± 3.61 / 77.76 ± 1.59</td> <!-- SQuAD -->
   <td class="en summ">70.35 ± 0.46 / 26.71 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">72.39 ± 1.41 / 79.30 ± 1.05</td> <!-- MMLU -->
   <td class="en reason">83.86 ± 2.24 / 87.81 ± 1.71</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- No Sammendrag version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- MMLU-no version -->
   <td>12.7.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.7.0</td> <!-- MMLU-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="da-rank">1.71</td> <!-- Danish rank -->
   <td class="no-rank">2.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.69</td> <!-- Swedish rank -->
   <td class="is-rank">3.22</td> <!-- Icelandic rank -->
   <td class="de-rank">1.69</td> <!-- German rank -->
   <td class="nl-rank">1.52</td> <!-- Dutch rank -->
   <td class="en-rank">1.57</td> <!-- English rank -->
   <td class="da ner">56.96 ± 2.39 / 45.84 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">55.11 ± 4.11 / 69.60 ± 2.69</td> <!-- Angry Tweets -->
   <td class="da la">42.64 ± 3.22 / 71.04 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da qa">54.58 ± 2.19 / 64.12 ± 1.41</td> <!-- ScandiQA-da -->
   <td class="da summ">66.80 ± 1.09 / 20.36 ± 1.51</td> <!-- Nordjylland-News -->
   <td class="da know">83.94 ± 1.81 / 87.97 ± 1.38</td> <!-- Danske Talemaader -->
   <td class="da know">73.32 ± 4.97 / 81.64 ± 3.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">60.52 ± 3.33 / 70.08 ± 2.52</td> <!-- HellaSwag-da -->
   <td class="no ner">66.75 ± 2.07 / 58.61 ± 3.33</td> <!-- NorNE-nb -->
   <td class="no ner">66.81 ± 2.57 / 57.71 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">60.58 ± 4.96 / 70.33 ± 4.12</td> <!-- NoReC -->
   <td class="no summ">64.64 ± 0.63 / 16.59 ± 1.15</td> <!-- No Sammendrag -->
   <td class="no la">47.53 ± 4.07 / 72.24 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">17.14 ± 4.72 / 51.14 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">41.92 ± 3.36 / 72.51 ± 1.91</td> <!-- NorQuAD -->
   <td class="no know">51.01 ± 2.61 / 63.20 ± 1.96</td> <!-- MMLU-no -->
   <td class="no reason">58.23 ± 5.79 / 67.46 ± 4.92</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.30 / 21.60 ± 0.76</td> <!-- SweDN -->
   <td class="sv know">53.56 ± 2.20 / 64.88 ± 1.66</td> <!-- MMLU-sv -->
   <td class="sv reason">59.70 ± 4.69 / 69.38 ± 3.70</td> <!-- HellaSwag-sv -->
   <td class="is ner">61.13 ± 3.80 / 50.79 ± 5.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.75 ± 5.66 / 46.83 ± 4.00</td> <!-- ScaLA-is -->
   <td class="is qa">27.27 ± 4.08 / 60.91 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">67.20 ± 0.49 / 20.53 ± 0.86</td> <!-- RRN -->
   <td class="is know">16.65 ± 3.21 / 37.70 ± 2.23</td> <!-- MMLU-is -->
   <td class="is reason">5.54 ± 2.19 / 35.62 ± 2.11</td> <!-- Winogrande-is -->
   <td class="de ner">65.19 ± 2.58 / 56.17 ± 3.57</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 2.15 / 71.98 ± 1.46</td> <!-- SB10k -->
   <td class="de la">41.86 ± 5.44 / 69.70 ± 2.31</td> <!-- ScaLA-de -->
   <td class="de qa">25.51 ± 3.79 / 63.19 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.76 / 20.65 ± 1.59</td> <!-- MLSum -->
   <td class="de know">55.18 ± 3.35 / 66.48 ± 2.49</td> <!-- MMLU-de -->
   <td class="de reason">61.68 ± 3.07 / 70.78 ± 2.37</td> <!-- HellaSwag-de -->
   <td class="nl ner">67.00 ± 3.69 / 56.41 ± 4.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.33 ± 4.14 / 36.14 ± 2.91</td> <!-- Dutch Social -->
   <td class="nl la">55.48 ± 4.37 / 77.55 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl qa">61.02 ± 1.67 / 76.87 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.95 ± 0.75 / 21.31 ± 1.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">54.36 ± 1.61 / 65.70 ± 1.26</td> <!-- MMLU-nl -->
   <td class="nl reason">70.26 ± 3.64 / 77.62 ± 2.82</td> <!-- HellaSwag-nl -->
   <td class="en ner">71.83 ± 1.48 / 65.37 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.99 ± 3.04 / 69.81 ± 1.86</td> <!-- SST5 -->
   <td class="en la">39.97 ± 3.89 / 69.38 ± 1.87</td> <!-- ScaLA-en -->
   <td class="en qa">64.42 ± 3.17 / 80.97 ± 1.54</td> <!-- SQuAD -->
   <td class="en summ">71.27 ± 0.50 / 25.32 ± 0.64</td> <!-- CNN-DailyMail -->
   <td class="en know">64.27 ± 3.04 / 73.20 ± 2.27</td> <!-- MMLU -->
   <td class="en reason">77.60 ± 4.02 / 82.85 ± 3.10</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- No Sammendrag version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- MMLU-no version -->
   <td>12.7.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.7.0</td> <!-- MMLU-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="da-rank">1.55</td> <!-- Danish rank -->
   <td class="no-rank">1.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.74</td> <!-- Swedish rank -->
   <td class="is-rank">3.02</td> <!-- Icelandic rank -->
   <td class="de-rank">1.90</td> <!-- German rank -->
   <td class="nl-rank">2.01</td> <!-- Dutch rank -->
   <td class="en-rank">1.67</td> <!-- English rank -->
   <td class="da ner">61.31 ± 2.34 / 49.86 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">52.52 ± 2.05 / 68.10 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">57.63 ± 2.80 / 77.01 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da qa">57.03 ± 1.95 / 65.51 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 0.26 / 18.03 ± 0.27</td> <!-- Nordjylland-News -->
   <td class="da know">81.95 ± 2.61 / 86.33 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">77.66 ± 2.57 / 85.08 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">62.21 ± 2.60 / 71.05 ± 2.09</td> <!-- HellaSwag-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no summ">64.18 ± 0.22 / 14.10 ± 0.37</td> <!-- No Sammendrag -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">45.35 ± 2.97 / 73.47 ± 1.69</td> <!-- NorQuAD -->
   <td class="no know">40.26 ± 5.24 / 54.88 ± 3.85</td> <!-- MMLU-no -->
   <td class="no reason">59.02 ± 1.63 / 68.63 ± 1.34</td> <!-- HellaSwag-no -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.92 ± 0.16 / 19.00 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">40.73 ± 3.36 / 55.16 ± 2.75</td> <!-- MMLU-sv -->
   <td class="sv reason">50.51 ± 2.33 / 62.07 ± 1.95</td> <!-- HellaSwag-sv -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">23.78 ± 2.81 / 42.70 ± 2.13</td> <!-- MMLU-is -->
   <td class="is reason">18.61 ± 6.00 / 61.33 ± 2.93</td> <!-- Winogrande-is -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">64.90 ± 0.22 / 15.99 ± 0.32</td> <!-- MLSum -->
   <td class="de know">35.39 ± 3.89 / 51.41 ± 2.98</td> <!-- MMLU-de -->
   <td class="de reason">56.88 ± 2.50 / 66.76 ± 2.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.13 ± 0.41 / 21.32 ± 0.75</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.28 ± 2.88 / 56.45 ± 2.26</td> <!-- MMLU-nl -->
   <td class="nl reason">61.52 ± 2.69 / 70.62 ± 2.20</td> <!-- HellaSwag-nl -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.18 / 24.41 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">43.69 ± 3.59 / 57.38 ± 3.06</td> <!-- MMLU -->
   <td class="en reason">75.60 ± 3.04 / 81.48 ± 2.31</td> <!-- HellaSwag -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.0</td> <!-- HellaSwag-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- MMLU-no version -->
   <td>0.0.0</td> <!-- HellaSwag-no version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>0.0.0</td> <!-- MMLU-sv version -->
   <td>0.0.0</td> <!-- HellaSwag-sv version -->
   <td>0.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>0.0.0</td> <!-- ScaLA-is version -->
   <td>0.0.0</td> <!-- NQiI version -->
   <td>0.0.0</td> <!-- RRN version -->
   <td>0.0.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- MLSum version -->
   <td>0.0.0</td> <!-- MMLU-de version -->
   <td>0.0.0</td> <!-- HellaSwag-de version -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>0.0.0</td> <!-- MMLU-nl version -->
   <td>0.0.0</td> <!-- HellaSwag-nl version -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   <td>0.0.0</td> <!-- CNN-DailyMail version -->
   <td>0.0.0</td> <!-- MMLU version -->
   <td>0.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="da-rank">1.66</td> <!-- Danish rank -->
   <td class="no-rank">2.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.74</td> <!-- Swedish rank -->
   <td class="is-rank">3.22</td> <!-- Icelandic rank -->
   <td class="de-rank">1.65</td> <!-- German rank -->
   <td class="nl-rank">2.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.52</td> <!-- English rank -->
   <td class="da ner">58.06 ± 2.48 / 50.10 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">53.24 ± 4.04 / 67.81 ± 2.74</td> <!-- Angry Tweets -->
   <td class="da la">39.71 ± 4.96 / 65.90 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">62.51 ± 1.48 / 67.47 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="da summ">67.39 ± 1.23 / 23.85 ± 1.20</td> <!-- Nordjylland-News -->
   <td class="da know">84.43 ± 1.72 / 88.28 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">71.35 ± 2.55 / 80.47 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">54.31 ± 2.56 / 65.20 ± 2.09</td> <!-- HellaSwag-da -->
   <td class="no ner">62.46 ± 4.62 / 60.77 ± 4.36</td> <!-- NorNE-nb -->
   <td class="no ner">64.68 ± 3.04 / 61.69 ± 2.31</td> <!-- NorNE-nn -->
   <td class="no sent">59.68 ± 3.30 / 70.62 ± 3.08</td> <!-- NoReC -->
   <td class="no summ">66.09 ± 1.05 / 21.12 ± 1.52</td> <!-- No Sammendrag -->
   <td class="no la">27.34 ± 12.20 / 50.42 ± 9.24</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 4.66 / 36.08 ± 3.27</td> <!-- ScaLA-nn -->
   <td class="no qa">57.44 ± 4.59 / 78.69 ± 3.09</td> <!-- NorQuAD -->
   <td class="no know">43.88 ± 3.11 / 57.62 ± 2.27</td> <!-- MMLU-no -->
   <td class="no reason">53.85 ± 3.43 / 64.34 ± 2.65</td> <!-- HellaSwag-no -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv qa">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.43 ± 0.33 / 24.92 ± 0.74</td> <!-- SweDN -->
   <td class="sv know">46.16 ± 2.67 / 59.53 ± 2.04</td> <!-- MMLU-sv -->
   <td class="sv reason">50.41 ± 5.18 / 62.34 ± 3.86</td> <!-- HellaSwag-sv -->
   <td class="is ner">63.25 ± 4.52 / 53.70 ± 3.09</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.12 ± 0.74</td> <!-- ScaLA-is -->
   <td class="is qa">32.65 ± 4.82 / 61.15 ± 3.96</td> <!-- NQiI -->
   <td class="is summ">66.93 ± 0.49 / 20.59 ± 0.94</td> <!-- RRN -->
   <td class="is know">16.19 ± 4.15 / 36.91 ± 3.32</td> <!-- MMLU-is -->
   <td class="is reason">3.95 ± 4.13 / 37.03 ± 2.20</td> <!-- Winogrande-is -->
   <td class="de ner">63.71 ± 2.43 / 57.08 ± 2.70</td> <!-- GermEval -->
   <td class="de sent">58.17 ± 2.51 / 71.34 ± 1.62</td> <!-- SB10k -->
   <td class="de la">36.33 ± 5.00 / 64.51 ± 3.38</td> <!-- ScaLA-de -->
   <td class="de qa">36.06 ± 2.89 / 69.62 ± 2.81</td> <!-- GermanQuAD -->
   <td class="de summ">69.82 ± 1.03 / 30.79 ± 2.46</td> <!-- MLSum -->
   <td class="de know">46.44 ± 2.49 / 59.88 ± 1.74</td> <!-- MMLU-de -->
   <td class="de reason">48.89 ± 2.85 / 61.33 ± 2.06</td> <!-- HellaSwag-de -->
   <td class="nl ner">66.50 ± 3.72 / 57.66 ± 3.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.82 ± 4.30 / 34.91 ± 2.53</td> <!-- Dutch Social -->
   <td class="nl la">49.55 ± 4.95 / 73.43 ± 3.38</td> <!-- ScaLA-nl -->
   <td class="nl qa">65.26 ± 1.55 / 77.36 ± 1.41</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.28 ± 1.07 / 21.33 ± 1.39</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">49.41 ± 2.21 / 61.91 ± 1.74</td> <!-- MMLU-nl -->
   <td class="nl reason">54.50 ± 4.84 / 65.70 ± 3.64</td> <!-- HellaSwag-nl -->
   <td class="en ner">72.38 ± 1.28 / 66.44 ± 1.74</td> <!-- CoNLL-en -->
   <td class="en sent">60.98 ± 2.19 / 68.64 ± 2.17</td> <!-- SST5 -->
   <td class="en la">43.12 ± 5.21 / 70.12 ± 2.87</td> <!-- ScaLA-en -->
   <td class="en qa">74.50 ± 3.41 / 86.22 ± 1.70</td> <!-- SQuAD -->
   <td class="en summ">71.63 ± 0.35 / 26.83 ± 0.78</td> <!-- CNN-DailyMail -->
   <td class="en know">54.29 ± 1.91 / 65.78 ± 1.33</td> <!-- MMLU -->
   <td class="en reason">74.35 ± 4.59 / 80.47 ± 3.64</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- No Sammendrag version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- MMLU-no version -->
   <td>12.7.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.7.0</td> <!-- MMLU-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="da-rank">1.91</td> <!-- Danish rank -->
   <td class="no-rank">2.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.97</td> <!-- Swedish rank -->
   <td class="is-rank">3.26</td> <!-- Icelandic rank -->
   <td class="de-rank">1.55</td> <!-- German rank -->
   <td class="nl-rank">1.92</td> <!-- Dutch rank -->
   <td class="en-rank">1.43</td> <!-- English rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da qa">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">66.81 ± 1.08 / 22.82 ± 1.04</td> <!-- Nordjylland-News -->
   <td class="da know">64.79 ± 1.37 / 73.46 ± 1.07</td> <!-- Danske Talemaader -->
   <td class="da know">68.59 ± 2.23 / 78.59 ± 1.60</td> <!-- Danish Citizen Tests -->
   <td class="da reason">65.29 ± 0.94 / 73.54 ± 0.74</td> <!-- HellaSwag-da -->
   <td class="no ner">68.11 ± 1.83 / 57.57 ± 3.10</td> <!-- NorNE-nb -->
   <td class="no ner">68.19 ± 1.01 / 56.90 ± 2.54</td> <!-- NorNE-nn -->
   <td class="no sent">55.33 ± 1.95 / 69.71 ± 1.56</td> <!-- NoReC -->
   <td class="no summ">65.51 ± 1.32 / 19.63 ± 1.66</td> <!-- No Sammendrag -->
   <td class="no la">10.15 ± 3.24 / 36.27 ± 1.44</td> <!-- ScaLA-nb -->
   <td class="no la">7.51 ± 2.97 / 35.89 ± 1.30</td> <!-- ScaLA-nn -->
   <td class="no qa">55.33 ± 3.29 / 80.42 ± 1.68</td> <!-- NorQuAD -->
   <td class="no know">35.57 ± 0.78 / 51.45 ± 0.56</td> <!-- MMLU-no -->
   <td class="no reason">62.76 ± 1.85 / 71.77 ± 1.45</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv qa">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.19 ± 0.36 / 19.09 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">39.82 ± 0.69 / 54.84 ± 0.53</td> <!-- MMLU-sv -->
   <td class="sv reason">68.87 ± 1.35 / 76.46 ± 1.04</td> <!-- HellaSwag-sv -->
   <td class="is ner">62.08 ± 2.27 / 51.09 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.58 ± 1.03 / 44.38 ± 3.90</td> <!-- ScaLA-is -->
   <td class="is qa">29.66 ± 3.02 / 56.60 ± 2.22</td> <!-- NQiI -->
   <td class="is summ">66.11 ± 0.85 / 18.74 ± 0.90</td> <!-- RRN -->
   <td class="is know">11.88 ± 0.67 / 33.57 ± 0.49</td> <!-- MMLU-is -->
   <td class="is reason">7.64 ± 1.91 / 49.40 ± 1.45</td> <!-- Winogrande-is -->
   <td class="de ner">68.11 ± 1.32 / 56.25 ± 1.65</td> <!-- GermEval -->
   <td class="de sent">59.79 ± 1.60 / 71.47 ± 1.54</td> <!-- SB10k -->
   <td class="de la">35.45 ± 3.06 / 66.13 ± 1.28</td> <!-- ScaLA-de -->
   <td class="de qa">37.27 ± 1.23 / 68.54 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.95 / 28.82 ± 2.24</td> <!-- MLSum -->
   <td class="de know">41.20 ± 0.85 / 55.90 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">72.65 ± 0.69 / 79.18 ± 0.58</td> <!-- HellaSwag-de -->
   <td class="nl ner">65.37 ± 1.61 / 46.10 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.93 ± 1.80 / 34.67 ± 2.84</td> <!-- Dutch Social -->
   <td class="nl la">41.67 ± 1.53 / 69.81 ± 1.38</td> <!-- ScaLA-nl -->
   <td class="nl qa">67.75 ± 0.62 / 78.01 ± 0.45</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.83 ± 0.35 / 26.12 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.18 ± 0.57 / 55.06 ± 0.44</td> <!-- MMLU-nl -->
   <td class="nl reason">65.34 ± 1.05 / 73.48 ± 0.83</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.50 ± 1.14 / 63.41 ± 0.77</td> <!-- CoNLL-en -->
   <td class="en sent">70.01 ± 0.93 / 59.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">41.35 ± 2.01 / 70.11 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en qa">76.79 ± 0.43 / 89.35 ± 0.19</td> <!-- SQuAD -->
   <td class="en summ">71.16 ± 0.12 / 29.84 ± 0.23</td> <!-- CNN-DailyMail -->
   <td class="en know">51.95 ± 0.84 / 63.78 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">90.94 ± 0.54 / 93.17 ± 0.41</td> <!-- HellaSwag -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.5.3</td> <!-- Nordjylland-News version -->
   <td>12.5.3</td> <!-- Danske Talemaader version -->
   <td>12.5.3</td> <!-- Danish Citizen Tests version -->
   <td>12.5.3</td> <!-- HellaSwag-da version -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- No Sammendrag version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   <td>12.5.3</td> <!-- MMLU-no version -->
   <td>12.5.3</td> <!-- HellaSwag-no version -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   <td>12.5.3</td> <!-- SweDN version -->
   <td>12.5.3</td> <!-- MMLU-sv version -->
   <td>12.5.3</td> <!-- HellaSwag-sv version -->
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- RRN version -->
   <td>12.5.3</td> <!-- MMLU-is version -->
   <td>12.5.3</td> <!-- Winogrande-is version -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- MLSum version -->
   <td>12.5.3</td> <!-- MMLU-de version -->
   <td>12.5.3</td> <!-- HellaSwag-de version -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   <td>12.5.3</td> <!-- CNN-DailyMail version -->
   <td>12.5.3</td> <!-- MMLU version -->
   <td>12.5.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="da-rank">1.96</td> <!-- Danish rank -->
   <td class="no-rank">2.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.08</td> <!-- Swedish rank -->
   <td class="is-rank">3.59</td> <!-- Icelandic rank -->
   <td class="de-rank">1.85</td> <!-- German rank -->
   <td class="nl-rank">2.00</td> <!-- Dutch rank -->
   <td class="en-rank">1.46</td> <!-- English rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da qa">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 0.76 / 23.35 ± 0.88</td> <!-- Nordjylland-News -->
   <td class="da know">59.78 ± 1.61 / 69.68 ± 1.23</td> <!-- Danske Talemaader -->
   <td class="da know">58.63 ± 2.54 / 71.72 ± 1.82</td> <!-- Danish Citizen Tests -->
   <td class="da reason">50.74 ± 1.16 / 62.79 ± 0.92</td> <!-- HellaSwag-da -->
   <td class="no ner">66.22 ± 2.15 / 48.98 ± 4.65</td> <!-- NorNE-nb -->
   <td class="no ner">64.14 ± 1.26 / 49.59 ± 4.31</td> <!-- NorNE-nn -->
   <td class="no sent">55.48 ± 1.77 / 69.68 ± 1.45</td> <!-- NoReC -->
   <td class="no summ">65.32 ± 0.41 / 18.53 ± 0.65</td> <!-- No Sammendrag -->
   <td class="no la">26.13 ± 1.28 / 56.08 ± 2.05</td> <!-- ScaLA-nb -->
   <td class="no la">17.32 ± 0.77 / 54.57 ± 1.49</td> <!-- ScaLA-nn -->
   <td class="no qa">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td class="no know">29.72 ± 1.33 / 46.95 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">46.78 ± 2.83 / 59.65 ± 2.28</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.75 ± 0.16 / 20.23 ± 0.23</td> <!-- SweDN -->
   <td class="sv know">36.05 ± 1.10 / 51.86 ± 0.87</td> <!-- MMLU-sv -->
   <td class="sv reason">51.15 ± 1.71 / 63.20 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">49.20 ± 2.64 / 40.79 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.45 ± 1.40 / 51.11 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is qa">24.61 ± 3.36 / 54.99 ± 2.36</td> <!-- NQiI -->
   <td class="is summ">63.74 ± 2.25 / 18.29 ± 1.40</td> <!-- RRN -->
   <td class="is know">9.81 ± 0.66 / 32.34 ± 0.54</td> <!-- MMLU-is -->
   <td class="is reason">1.14 ± 0.97 / 50.10 ± 0.82</td> <!-- Winogrande-is -->
   <td class="de ner">65.01 ± 0.68 / 43.34 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">51.80 ± 1.29 / 67.45 ± 0.87</td> <!-- SB10k -->
   <td class="de la">36.18 ± 1.31 / 67.86 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de qa">32.12 ± 2.08 / 67.30 ± 1.66</td> <!-- GermanQuAD -->
   <td class="de summ">66.92 ± 0.41 / 23.23 ± 1.24</td> <!-- MLSum -->
   <td class="de know">37.90 ± 1.03 / 53.36 ± 0.80</td> <!-- MMLU-de -->
   <td class="de reason">60.66 ± 1.28 / 70.32 ± 1.01</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.47 ± 2.31 / 40.89 ± 2.81</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.83 ± 1.91 / 41.53 ± 1.23</td> <!-- Dutch Social -->
   <td class="nl la">45.69 ± 1.76 / 72.13 ± 1.39</td> <!-- ScaLA-nl -->
   <td class="nl qa">58.03 ± 1.37 / 73.17 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.34 ± 0.77 / 22.22 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">37.60 ± 0.83 / 53.13 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">54.33 ± 0.84 / 65.41 ± 0.59</td> <!-- HellaSwag-nl -->
   <td class="en ner">71.81 ± 1.02 / 59.93 ± 2.52</td> <!-- CoNLL-en -->
   <td class="en sent">69.98 ± 1.00 / 69.79 ± 0.76</td> <!-- SST5 -->
   <td class="en la">45.34 ± 2.51 / 72.10 ± 1.10</td> <!-- ScaLA-en -->
   <td class="en qa">72.49 ± 1.57 / 87.51 ± 0.74</td> <!-- SQuAD -->
   <td class="en summ">70.37 ± 0.32 / 27.70 ± 0.38</td> <!-- CNN-DailyMail -->
   <td class="en know">50.93 ± 1.34 / 62.98 ± 0.98</td> <!-- MMLU -->
   <td class="en reason">83.82 ± 0.80 / 87.83 ± 0.60</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- No Sammendrag version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- MMLU-no version -->
   <td>12.5.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="da-rank">2.23</td> <!-- Danish rank -->
   <td class="no-rank">2.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.19</td> <!-- Swedish rank -->
   <td class="is-rank">3.32</td> <!-- Icelandic rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.34</td> <!-- Dutch rank -->
   <td class="en-rank">1.92</td> <!-- English rank -->
   <td class="da ner">46.31 ± 3.22 / 29.09 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 1.47 / 66.35 ± 1.70</td> <!-- Angry Tweets -->
   <td class="da la">25.70 ± 4.59 / 55.65 ± 5.87</td> <!-- ScaLA-da -->
   <td class="da qa">59.79 ± 1.21 / 65.44 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">65.16 ± 0.48 / 18.74 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">56.20 ± 2.22 / 66.91 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">61.16 ± 2.54 / 73.63 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.99 ± 2.12 / 42.57 ± 1.91</td> <!-- HellaSwag-da -->
   <td class="no ner">61.48 ± 1.83 / 47.65 ± 2.94</td> <!-- NorNE-nb -->
   <td class="no ner">61.58 ± 2.21 / 50.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">49.87 ± 1.88 / 66.15 ± 1.44</td> <!-- NoReC -->
   <td class="no summ">63.38 ± 1.15 / 15.74 ± 1.68</td> <!-- No Sammendrag -->
   <td class="no la">21.20 ± 6.57 / 52.29 ± 7.43</td> <!-- ScaLA-nb -->
   <td class="no la">19.65 ± 4.32 / 56.66 ± 4.40</td> <!-- ScaLA-nn -->
   <td class="no qa">53.35 ± 4.33 / 74.98 ± 3.70</td> <!-- NorQuAD -->
   <td class="no know">33.02 ± 1.35 / 49.25 ± 1.04</td> <!-- MMLU-no -->
   <td class="no reason">24.93 ± 3.13 / 42.47 ± 2.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.81 ± 0.24 / 18.56 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">35.86 ± 0.90 / 51.39 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">26.49 ± 1.89 / 44.41 ± 1.56</td> <!-- HellaSwag-sv -->
   <td class="is ner">48.70 ± 3.02 / 34.52 ± 2.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.49 ± 2.51 / 43.40 ± 4.41</td> <!-- ScaLA-is -->
   <td class="is qa">29.56 ± 5.47 / 55.53 ± 5.79</td> <!-- NQiI -->
   <td class="is summ">66.34 ± 1.09 / 19.13 ± 0.96</td> <!-- RRN -->
   <td class="is know">16.97 ± 1.01 / 37.63 ± 0.74</td> <!-- MMLU-is -->
   <td class="is reason">7.41 ± 3.26 / 52.13 ± 1.97</td> <!-- Winogrande-is -->
   <td class="de ner">56.00 ± 1.94 / 43.49 ± 2.05</td> <!-- GermEval -->
   <td class="de sent">56.40 ± 3.89 / 70.17 ± 2.91</td> <!-- SB10k -->
   <td class="de la">22.01 ± 5.17 / 56.97 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de qa">35.39 ± 2.49 / 64.61 ± 2.42</td> <!-- GermanQuAD -->
   <td class="de summ">68.92 ± 0.99 / 26.93 ± 2.01</td> <!-- MLSum -->
   <td class="de know">38.12 ± 0.75 / 53.52 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">31.37 ± 1.37 / 47.65 ± 1.09</td> <!-- HellaSwag-de -->
   <td class="nl ner">62.26 ± 2.20 / 42.41 ± 2.02</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.45 ± 2.69 / 33.45 ± 1.99</td> <!-- Dutch Social -->
   <td class="nl la">30.30 ± 3.94 / 62.28 ± 2.89</td> <!-- ScaLA-nl -->
   <td class="nl qa">62.99 ± 1.00 / 73.73 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.17 ± 1.24 / 18.63 ± 1.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.38 ± 0.86 / 52.08 ± 0.66</td> <!-- MMLU-nl -->
   <td class="nl reason">28.33 ± 2.31 / 45.29 ± 1.78</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.31 ± 2.09 / 58.68 ± 1.95</td> <!-- CoNLL-en -->
   <td class="en sent">64.30 ± 0.65 / 69.26 ± 0.50</td> <!-- SST5 -->
   <td class="en la">28.18 ± 3.96 / 58.97 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en qa">70.38 ± 3.51 / 82.95 ± 2.38</td> <!-- SQuAD -->
   <td class="en summ">67.90 ± 0.49 / 21.54 ± 0.57</td> <!-- CNN-DailyMail -->
   <td class="en know">52.54 ± 0.88 / 64.26 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">41.19 ± 4.40 / 54.78 ± 3.62</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- No Sammendrag version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- MMLU-no version -->
   <td>12.6.1</td> <!-- HellaSwag-no version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.6.1</td> <!-- MMLU-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.29</td> <!-- Danish rank -->
   <td class="no-rank">2.42</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.31</td> <!-- Swedish rank -->
   <td class="is-rank">3.27</td> <!-- Icelandic rank -->
   <td class="de-rank">2.04</td> <!-- German rank -->
   <td class="nl-rank">2.32</td> <!-- Dutch rank -->
   <td class="en-rank">1.86</td> <!-- English rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da qa">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.36 ± 0.47 / 19.75 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">57.87 ± 1.67 / 67.43 ± 1.34</td> <!-- Danske Talemaader -->
   <td class="da know">50.42 ± 3.32 / 65.43 ± 2.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.17 ± 2.24 / 44.59 ± 2.00</td> <!-- HellaSwag-da -->
   <td class="no ner">74.47 ± 1.47 / 65.57 ± 2.39</td> <!-- NorNE-nb -->
   <td class="no ner">72.93 ± 1.00 / 65.44 ± 2.55</td> <!-- NorNE-nn -->
   <td class="no sent">50.62 ± 3.52 / 65.69 ± 3.50</td> <!-- NoReC -->
   <td class="no summ">63.98 ± 0.50 / 14.75 ± 0.79</td> <!-- No Sammendrag -->
   <td class="no la">27.77 ± 1.63 / 61.75 ± 1.77</td> <!-- ScaLA-nb -->
   <td class="no la">20.35 ± 1.92 / 57.74 ± 2.28</td> <!-- ScaLA-nn -->
   <td class="no qa">42.90 ± 3.57 / 69.90 ± 3.17</td> <!-- NorQuAD -->
   <td class="no know">33.44 ± 0.67 / 48.76 ± 0.58</td> <!-- MMLU-no -->
   <td class="no reason">30.91 ± 1.88 / 45.85 ± 1.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.60 ± 0.07 / 19.13 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">33.54 ± 1.40 / 49.20 ± 1.13</td> <!-- MMLU-sv -->
   <td class="sv reason">30.32 ± 2.27 / 45.96 ± 1.87</td> <!-- HellaSwag-sv -->
   <td class="is ner">61.69 ± 2.17 / 41.25 ± 3.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.10 ± 1.61 / 48.74 ± 3.05</td> <!-- ScaLA-is -->
   <td class="is qa">31.52 ± 2.08 / 58.96 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">66.98 ± 1.04 / 19.84 ± 1.97</td> <!-- RRN -->
   <td class="is know">14.81 ± 1.23 / 34.74 ± 0.94</td> <!-- MMLU-is -->
   <td class="is reason">1.50 ± 1.22 / 48.33 ± 1.21</td> <!-- Winogrande-is -->
   <td class="de ner">68.18 ± 0.95 / 57.72 ± 1.15</td> <!-- GermEval -->
   <td class="de sent">58.33 ± 2.83 / 69.31 ± 3.16</td> <!-- SB10k -->
   <td class="de la">29.12 ± 3.17 / 63.60 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de qa">28.68 ± 1.99 / 56.42 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.23 ± 0.49 / 16.56 ± 0.94</td> <!-- MLSum -->
   <td class="de know">38.44 ± 0.81 / 53.38 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">37.69 ± 1.00 / 51.24 ± 0.73</td> <!-- HellaSwag-de -->
   <td class="nl ner">68.72 ± 1.81 / 54.89 ± 2.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.67 ± 2.51 / 41.36 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">32.91 ± 2.56 / 64.93 ± 1.97</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.36 ± 1.31 / 67.50 ± 0.69</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.82 / 18.19 ± 1.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.18 ± 1.31 / 51.68 ± 1.05</td> <!-- MMLU-nl -->
   <td class="nl reason">33.91 ± 1.71 / 48.01 ± 1.47</td> <!-- HellaSwag-nl -->
   <td class="en ner">75.02 ± 1.31 / 69.47 ± 1.18</td> <!-- CoNLL-en -->
   <td class="en sent">67.64 ± 1.12 / 71.04 ± 1.17</td> <!-- SST5 -->
   <td class="en la">32.29 ± 3.05 / 64.85 ± 2.07</td> <!-- ScaLA-en -->
   <td class="en qa">54.84 ± 2.22 / 79.10 ± 1.10</td> <!-- SQuAD -->
   <td class="en summ">69.28 ± 0.17 / 25.48 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">53.77 ± 1.03 / 64.91 ± 0.80</td> <!-- MMLU -->
   <td class="en reason">57.64 ± 1.55 / 67.29 ± 1.30</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- No Sammendrag version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- MMLU-no version -->
   <td>12.6.1</td> <!-- HellaSwag-no version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.6.1</td> <!-- MMLU-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
   <td class="is-rank">3.50</td> <!-- Icelandic rank -->
   <td class="de-rank">2.00</td> <!-- German rank -->
   <td class="nl-rank">2.26</td> <!-- Dutch rank -->
   <td class="en-rank">1.87</td> <!-- English rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da qa">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
   <td class="da summ">67.33 ± 1.40 / 22.77 ± 1.39</td> <!-- Nordjylland-News -->
   <td class="da know">65.38 ± 2.59 / 73.95 ± 1.84</td> <!-- Danske Talemaader -->
   <td class="da know">62.78 ± 4.04 / 74.61 ± 2.90</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.07 ± 2.57 / 53.83 ± 2.06</td> <!-- HellaSwag-da -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no summ">65.74 ± 0.37 / 19.13 ± 0.54</td> <!-- No Sammendrag -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no qa">34.48 ± 2.13 / 65.43 ± 2.07</td> <!-- NorQuAD -->
   <td class="no know">28.39 ± 1.76 / 45.59 ± 1.28</td> <!-- MMLU-no -->
   <td class="no reason">35.19 ± 3.28 / 50.12 ± 3.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.35 ± 0.32 / 24.05 ± 0.66</td> <!-- SweDN -->
   <td class="sv know">32.30 ± 2.48 / 48.98 ± 1.96</td> <!-- MMLU-sv -->
   <td class="sv reason">38.78 ± 5.70 / 52.89 ± 4.91</td> <!-- HellaSwag-sv -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.48 ± 4.43 / 55.51 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">10.13 ± 2.94 / 32.62 ± 2.20</td> <!-- MMLU-is -->
   <td class="is reason">12.90 ± 6.92 / 56.88 ± 3.57</td> <!-- Winogrande-is -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de qa">25.22 ± 3.84 / 60.93 ± 2.99</td> <!-- GermanQuAD -->
   <td class="de summ">67.31 ± 1.05 / 24.72 ± 2.95</td> <!-- MLSum -->
   <td class="de know">35.84 ± 2.16 / 51.64 ± 1.56</td> <!-- MMLU-de -->
   <td class="de reason">49.13 ± 2.71 / 61.68 ± 2.03</td> <!-- HellaSwag-de -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.94 ± 1.12 / 70.12 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="nl summ">71.20 ± 0.46 / 23.47 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.23 ± 2.86 / 54.77 ± 2.16</td> <!-- MMLU-nl -->
   <td class="nl reason">47.87 ± 2.49 / 60.78 ± 1.85</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.37 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">70.55 ± 0.73 / 26.32 ± 0.97</td> <!-- CNN-DailyMail -->
   <td class="en know">51.74 ± 1.82 / 63.44 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">71.96 ± 2.38 / 78.87 ± 1.66</td> <!-- HellaSwag -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>9.3.2</td> <!-- No Sammendrag version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- MMLU-no version -->
   <td>9.3.2</td> <!-- HellaSwag-no version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>9.3.2</td> <!-- RRN version -->
   <td>9.3.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>9.3.2</td> <!-- MLSum version -->
   <td>9.3.2</td> <!-- MMLU-de version -->
   <td>9.3.2</td> <!-- HellaSwag-de version -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>9.3.2</td> <!-- CNN-DailyMail version -->
   <td>9.3.2</td> <!-- MMLU version -->
   <td>9.3.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.49</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.21</td> <!-- Swedish rank -->
   <td class="is-rank">3.71</td> <!-- Icelandic rank -->
   <td class="de-rank">2.06</td> <!-- German rank -->
   <td class="nl-rank">2.15</td> <!-- Dutch rank -->
   <td class="en-rank">1.82</td> <!-- English rank -->
   <td class="da ner">52.22 ± 2.07 / 38.82 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">50.66 ± 1.88 / 62.04 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">23.57 ± 3.82 / 56.09 ± 4.62</td> <!-- ScaLA-da -->
   <td class="da qa">53.82 ± 2.13 / 61.94 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="da summ">67.13 ± 0.72 / 21.62 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">69.26 ± 2.89 / 76.99 ± 2.16</td> <!-- Danske Talemaader -->
   <td class="da know">46.40 ± 2.92 / 59.45 ± 2.63</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.72 ± 2.48 / 53.83 ± 2.19</td> <!-- HellaSwag-da -->
   <td class="no ner">60.21 ± 1.86 / 47.06 ± 3.08</td> <!-- NorNE-nb -->
   <td class="no ner">62.99 ± 2.66 / 48.82 ± 5.49</td> <!-- NorNE-nn -->
   <td class="no sent">55.12 ± 5.10 / 66.55 ± 5.07</td> <!-- NoReC -->
   <td class="no summ">65.11 ± 0.66 / 17.82 ± 1.21</td> <!-- No Sammendrag -->
   <td class="no la">27.12 ± 4.90 / 54.26 ± 6.80</td> <!-- ScaLA-nb -->
   <td class="no la">6.82 ± 5.06 / 46.18 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">38.50 ± 3.93 / 69.99 ± 2.23</td> <!-- NorQuAD -->
   <td class="no know">32.30 ± 3.42 / 48.32 ± 2.61</td> <!-- MMLU-no -->
   <td class="no reason">34.43 ± 2.91 / 49.65 ± 2.23</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.24 / 21.77 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">37.60 ± 3.30 / 52.46 ± 2.31</td> <!-- MMLU-sv -->
   <td class="sv reason">31.78 ± 2.98 / 47.11 ± 2.71</td> <!-- HellaSwag-sv -->
   <td class="is ner">46.32 ± 5.10 / 35.77 ± 3.59</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-3.31 ± 3.91 / 38.63 ± 2.52</td> <!-- ScaLA-is -->
   <td class="is qa">24.26 ± 4.64 / 55.26 ± 2.41</td> <!-- NQiI -->
   <td class="is summ">66.16 ± 0.33 / 18.63 ± 0.56</td> <!-- RRN -->
   <td class="is know">8.27 ± 1.98 / 30.66 ± 1.24</td> <!-- MMLU-is -->
   <td class="is reason">2.75 ± 2.26 / 30.86 ± 1.74</td> <!-- Winogrande-is -->
   <td class="de ner">62.39 ± 2.72 / 50.86 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">53.16 ± 3.17 / 64.24 ± 3.42</td> <!-- SB10k -->
   <td class="de la">31.81 ± 5.15 / 62.15 ± 4.02</td> <!-- ScaLA-de -->
   <td class="de qa">28.99 ± 2.22 / 60.53 ± 2.92</td> <!-- GermanQuAD -->
   <td class="de summ">66.98 ± 0.87 / 22.66 ± 2.41</td> <!-- MLSum -->
   <td class="de know">35.72 ± 3.05 / 51.99 ± 2.09</td> <!-- MMLU-de -->
   <td class="de reason">35.26 ± 3.73 / 50.59 ± 3.17</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.00 ± 3.52 / 48.94 ± 3.83</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.30 ± 3.75 / 30.50 ± 2.48</td> <!-- Dutch Social -->
   <td class="nl la">30.88 ± 4.62 / 59.62 ± 4.50</td> <!-- ScaLA-nl -->
   <td class="nl qa">54.14 ± 1.55 / 70.96 ± 1.01</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.71 ± 0.70 / 19.82 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">45.47 ± 2.07 / 59.14 ± 1.69</td> <!-- MMLU-nl -->
   <td class="nl reason">42.91 ± 3.26 / 57.30 ± 2.39</td> <!-- HellaSwag-nl -->
   <td class="en ner">72.80 ± 1.65 / 64.88 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.76 ± 2.53 / 71.14 ± 1.90</td> <!-- SST5 -->
   <td class="en la">28.37 ± 4.76 / 62.85 ± 3.04</td> <!-- ScaLA-en -->
   <td class="en qa">64.70 ± 2.69 / 81.80 ± 1.41</td> <!-- SQuAD -->
   <td class="en summ">71.04 ± 0.42 / 25.68 ± 0.52</td> <!-- CNN-DailyMail -->
   <td class="en know">47.00 ± 2.21 / 60.12 ± 1.58</td> <!-- MMLU -->
   <td class="en reason">61.56 ± 2.97 / 70.27 ± 2.27</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.7.0</td> <!-- NorNE-nb version -->
   <td>12.7.0</td> <!-- NorNE-nn version -->
   <td>12.7.0</td> <!-- NoReC version -->
   <td>12.7.0</td> <!-- No Sammendrag version -->
   <td>12.7.0</td> <!-- ScaLA-nb version -->
   <td>12.7.0</td> <!-- ScaLA-nn version -->
   <td>12.7.0</td> <!-- NorQuAD version -->
   <td>12.7.0</td> <!-- MMLU-no version -->
   <td>12.7.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   <td>12.7.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.7.0</td> <!-- ScaLA-is version -->
   <td>12.7.0</td> <!-- NQiI version -->
   <td>12.7.0</td> <!-- RRN version -->
   <td>12.7.0</td> <!-- MMLU-is version -->
   <td>12.7.0</td> <!-- Winogrande-is version -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da-rank">2.30</td> <!-- Danish rank -->
   <td class="no-rank">2.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.37</td> <!-- Swedish rank -->
   <td class="is-rank">3.46</td> <!-- Icelandic rank -->
   <td class="de-rank">2.06</td> <!-- German rank -->
   <td class="nl-rank">2.28</td> <!-- Dutch rank -->
   <td class="en-rank">1.92</td> <!-- English rank -->
   <td class="da ner">52.61 ± 1.77 / 33.64 ± 2.67</td> <!-- DANSK -->
   <td class="da sent">49.81 ± 1.43 / 66.32 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">19.64 ± 1.63 / 54.22 ± 2.32</td> <!-- ScaLA-da -->
   <td class="da qa">48.03 ± 1.24 / 57.94 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">66.67 ± 0.87 / 21.08 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">57.65 ± 1.99 / 68.08 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">51.99 ± 3.67 / 66.43 ± 2.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">44.44 ± 1.52 / 58.16 ± 1.21</td> <!-- HellaSwag-da -->
   <td class="no ner">64.37 ± 2.17 / 52.81 ± 2.48</td> <!-- NorNE-nb -->
   <td class="no ner">62.77 ± 0.83 / 51.80 ± 2.77</td> <!-- NorNE-nn -->
   <td class="no sent">50.60 ± 4.90 / 66.76 ± 3.04</td> <!-- NoReC -->
   <td class="no summ">65.09 ± 0.31 / 17.27 ± 0.66</td> <!-- No Sammendrag -->
   <td class="no la">18.09 ± 2.04 / 52.56 ± 2.60</td> <!-- ScaLA-nb -->
   <td class="no la">12.25 ± 2.18 / 50.79 ± 2.42</td> <!-- ScaLA-nn -->
   <td class="no qa">38.34 ± 2.39 / 69.54 ± 1.96</td> <!-- NorQuAD -->
   <td class="no know">27.33 ± 0.72 / 45.16 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">41.59 ± 2.61 / 56.02 ± 2.08</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv qa">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.09 ± 0.17 / 19.64 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">31.76 ± 0.89 / 48.64 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">45.84 ± 1.47 / 59.27 ± 1.16</td> <!-- HellaSwag-sv -->
   <td class="is ner">56.71 ± 1.98 / 46.71 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is qa">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">65.39 ± 0.80 / 18.24 ± 1.00</td> <!-- RRN -->
   <td class="is know">9.81 ± 0.85 / 32.28 ± 0.65</td> <!-- MMLU-is -->
   <td class="is reason">3.30 ± 2.81 / 44.40 ± 1.61</td> <!-- Winogrande-is -->
   <td class="de ner">64.38 ± 1.60 / 50.26 ± 2.53</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.45 / 69.32 ± 1.02</td> <!-- SB10k -->
   <td class="de la">26.03 ± 2.23 / 61.88 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de qa">25.68 ± 2.81 / 62.48 ± 2.93</td> <!-- GermanQuAD -->
   <td class="de summ">68.16 ± 0.95 / 24.52 ± 2.45</td> <!-- MLSum -->
   <td class="de know">33.84 ± 1.54 / 50.24 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">50.99 ± 0.99 / 63.11 ± 0.75</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.25 ± 2.23 / 46.52 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.66 ± 1.99 / 39.45 ± 1.52</td> <!-- Dutch Social -->
   <td class="nl la">28.59 ± 1.48 / 61.24 ± 1.46</td> <!-- ScaLA-nl -->
   <td class="nl qa">49.64 ± 0.86 / 68.04 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.57 / 19.51 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.37 ± 1.30 / 51.43 ± 0.96</td> <!-- MMLU-nl -->
   <td class="nl reason">47.50 ± 1.75 / 60.41 ± 1.32</td> <!-- HellaSwag-nl -->
   <td class="en ner">70.62 ± 0.90 / 58.92 ± 2.15</td> <!-- CoNLL-en -->
   <td class="en sent">67.78 ± 1.03 / 72.29 ± 0.47</td> <!-- SST5 -->
   <td class="en la">30.99 ± 2.94 / 62.20 ± 2.56</td> <!-- ScaLA-en -->
   <td class="en qa">49.56 ± 2.85 / 76.72 ± 1.15</td> <!-- SQuAD -->
   <td class="en summ">70.76 ± 0.56 / 24.95 ± 1.03</td> <!-- CNN-DailyMail -->
   <td class="en know">44.11 ± 4.39 / 57.76 ± 3.36</td> <!-- MMLU -->
   <td class="en reason">69.20 ± 2.71 / 76.75 ± 2.06</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   <td>12.6.1</td> <!-- NorNE-nb version -->
   <td>12.6.1</td> <!-- NorNE-nn version -->
   <td>12.6.1</td> <!-- NoReC version -->
   <td>12.6.1</td> <!-- No Sammendrag version -->
   <td>12.6.1</td> <!-- ScaLA-nb version -->
   <td>12.6.1</td> <!-- ScaLA-nn version -->
   <td>12.6.1</td> <!-- NorQuAD version -->
   <td>12.6.1</td> <!-- MMLU-no version -->
   <td>12.6.1</td> <!-- HellaSwag-no version -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   <td>12.6.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.6.1</td> <!-- ScaLA-is version -->
   <td>12.6.1</td> <!-- NQiI version -->
   <td>12.6.1</td> <!-- RRN version -->
   <td>12.6.1</td> <!-- MMLU-is version -->
   <td>12.6.1</td> <!-- Winogrande-is version -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
   <td class="is-rank">3.49</td> <!-- Icelandic rank -->
   <td class="de-rank">2.07</td> <!-- German rank -->
   <td class="nl-rank">2.59</td> <!-- Dutch rank -->
   <td class="en-rank">2.05</td> <!-- English rank -->
   <td class="da ner">19.59 ± 2.54 / 15.47 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">46.55 ± 1.89 / 59.52 ± 3.56</td> <!-- Angry Tweets -->
   <td class="da la">32.64 ± 2.91 / 63.84 ± 1.69</td> <!-- ScaLA-da -->
   <td class="da qa">59.40 ± 1.02 / 64.81 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">66.63 ± 0.82 / 22.82 ± 0.62</td> <!-- Nordjylland-News -->
   <td class="da know">74.32 ± 0.96 / 80.31 ± 0.79</td> <!-- Danske Talemaader -->
   <td class="da know">65.58 ± 2.10 / 76.41 ± 1.54</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.74 ± 2.86 / 39.03 ± 1.70</td> <!-- HellaSwag-da -->
   <td class="no ner">26.43 ± 3.36 / 26.32 ± 2.35</td> <!-- NorNE-nb -->
   <td class="no ner">32.66 ± 3.42 / 29.43 ± 1.74</td> <!-- NorNE-nn -->
   <td class="no sent">41.82 ± 3.69 / 53.06 ± 5.15</td> <!-- NoReC -->
   <td class="no summ">64.02 ± 1.35 / 17.65 ± 1.59</td> <!-- No Sammendrag -->
   <td class="no la">25.82 ± 4.43 / 59.85 ± 4.07</td> <!-- ScaLA-nb -->
   <td class="no la">20.16 ± 3.43 / 53.83 ± 5.61</td> <!-- ScaLA-nn -->
   <td class="no qa">52.68 ± 3.58 / 75.16 ± 2.44</td> <!-- NorQuAD -->
   <td class="no know">39.96 ± 0.97 / 53.03 ± 0.89</td> <!-- MMLU-no -->
   <td class="no reason">27.82 ± 4.59 / 41.21 ± 4.09</td> <!-- HellaSwag-no -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.44 ± 0.29 / 18.70 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">39.94 ± 1.17 / 53.25 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">25.96 ± 3.94 / 40.33 ± 3.17</td> <!-- HellaSwag-sv -->
   <td class="is ner">30.61 ± 4.61 / 25.80 ± 3.57</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.60 ± 1.68 / 38.26 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">32.22 ± 3.19 / 55.22 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.03 ± 1.82 / 18.15 ± 2.24</td> <!-- RRN -->
   <td class="is know">17.73 ± 0.90 / 35.47 ± 0.83</td> <!-- MMLU-is -->
   <td class="is reason">1.14 ± 1.26 / 39.92 ± 1.92</td> <!-- Winogrande-is -->
   <td class="de ner">39.88 ± 2.56 / 35.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">56.23 ± 3.17 / 68.87 ± 2.73</td> <!-- SB10k -->
   <td class="de la">32.71 ± 1.60 / 64.55 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de qa">36.58 ± 2.81 / 64.92 ± 2.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.41 ± 1.20 / 29.96 ± 3.00</td> <!-- MLSum -->
   <td class="de know">41.56 ± 0.82 / 54.79 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">30.77 ± 2.85 / 43.20 ± 2.53</td> <!-- HellaSwag-de -->
   <td class="nl ner">47.75 ± 2.33 / 35.64 ± 1.89</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.68 ± 0.61 / 26.25 ± 1.18</td> <!-- Dutch Social -->
   <td class="nl la">28.28 ± 2.48 / 62.81 ± 1.70</td> <!-- ScaLA-nl -->
   <td class="nl qa">61.49 ± 1.15 / 73.19 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.60 ± 1.18 / 19.95 ± 1.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.19 ± 0.97 / 55.52 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">31.45 ± 2.79 / 44.15 ± 3.09</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.20 ± 3.34 / 41.96 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.88 ± 2.24 / 66.49 ± 0.81</td> <!-- SST5 -->
   <td class="en la">35.75 ± 2.65 / 66.41 ± 2.26</td> <!-- ScaLA-en -->
   <td class="en qa">69.40 ± 4.29 / 82.46 ± 2.86</td> <!-- SQuAD -->
   <td class="en summ">69.25 ± 0.80 / 24.32 ± 0.95</td> <!-- CNN-DailyMail -->
   <td class="en know">50.57 ± 1.00 / 61.48 ± 0.80</td> <!-- MMLU -->
   <td class="en reason">35.79 ± 4.89 / 46.37 ± 3.67</td> <!-- HellaSwag -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- Nordjylland-News version -->
   <td>12.9.1</td> <!-- Danske Talemaader version -->
   <td>12.9.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.1</td> <!-- HellaSwag-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.9.1</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.9.1</td> <!-- No Sammendrag version -->
   <td>12.9.1</td> <!-- ScaLA-nb version -->
   <td>12.9.1</td> <!-- ScaLA-nn version -->
   <td>12.9.1</td> <!-- NorQuAD version -->
   <td>12.9.1</td> <!-- MMLU-no version -->
   <td>12.9.1</td> <!-- HellaSwag-no version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   <td>12.9.1</td> <!-- SweDN version -->
   <td>12.9.1</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.9.1</td> <!-- RRN version -->
   <td>12.9.1</td> <!-- MMLU-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.9.1</td> <!-- MLSum version -->
   <td>12.9.1</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.9.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.9.1</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   <td>12.9.1</td> <!-- CNN-DailyMail version -->
   <td>12.9.1</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="da-rank">2.34</td> <!-- Danish rank -->
   <td class="no-rank">2.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="is-rank">3.62</td> <!-- Icelandic rank -->
   <td class="de-rank">2.12</td> <!-- German rank -->
   <td class="nl-rank">2.35</td> <!-- Dutch rank -->
   <td class="en-rank">2.01</td> <!-- English rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da qa">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">66.62 ± 0.96 / 21.03 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">60.03 ± 5.14 / 70.04 ± 3.73</td> <!-- Danske Talemaader -->
   <td class="da know">59.83 ± 4.38 / 72.27 ± 3.40</td> <!-- Danish Citizen Tests -->
   <td class="da reason">40.40 ± 3.24 / 55.04 ± 2.57</td> <!-- HellaSwag-da -->
   <td class="no ner">61.90 ± 2.57 / 57.16 ± 2.81</td> <!-- NorNE-nb -->
   <td class="no ner">66.92 ± 2.52 / 57.81 ± 3.54</td> <!-- NorNE-nn -->
   <td class="no sent">48.80 ± 4.56 / 63.38 ± 3.06</td> <!-- NoReC -->
   <td class="no summ">64.72 ± 0.39 / 17.40 ± 0.60</td> <!-- No Sammendrag -->
   <td class="no la">19.53 ± 5.49 / 51.96 ± 4.90</td> <!-- ScaLA-nb -->
   <td class="no la">9.83 ± 4.57 / 47.95 ± 2.22</td> <!-- ScaLA-nn -->
   <td class="no qa">30.27 ± 2.28 / 62.04 ± 2.19</td> <!-- NorQuAD -->
   <td class="no know">28.18 ± 1.89 / 45.23 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">36.20 ± 3.97 / 50.74 ± 3.38</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.94 ± 0.21 / 22.99 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">27.51 ± 3.08 / 45.43 ± 2.37</td> <!-- MMLU-sv -->
   <td class="sv reason">42.29 ± 5.08 / 55.43 ± 4.50</td> <!-- HellaSwag-sv -->
   <td class="is ner">50.85 ± 4.15 / 42.91 ± 5.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.80 ± 3.84 / 49.12 ± 2.51</td> <!-- ScaLA-is -->
   <td class="is qa">20.23 ± 3.73 / 52.99 ± 2.11</td> <!-- NQiI -->
   <td class="is summ">64.46 ± 1.03 / 17.62 ± 1.10</td> <!-- RRN -->
   <td class="is know">9.92 ± 2.10 / 32.19 ± 1.69</td> <!-- MMLU-is -->
   <td class="is reason">9.09 ± 6.37 / 49.53 ± 5.40</td> <!-- Winogrande-is -->
   <td class="de ner">63.36 ± 2.68 / 51.59 ± 3.44</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 3.18 / 72.32 ± 2.23</td> <!-- SB10k -->
   <td class="de la">22.98 ± 8.11 / 60.88 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de qa">20.96 ± 3.59 / 57.36 ± 2.94</td> <!-- GermanQuAD -->
   <td class="de summ">67.58 ± 1.11 / 24.69 ± 2.94</td> <!-- MLSum -->
   <td class="de know">36.08 ± 1.55 / 51.68 ± 1.14</td> <!-- MMLU-de -->
   <td class="de reason">47.99 ± 2.87 / 60.55 ± 2.08</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.71 ± 5.15 / 53.58 ± 3.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.14 ± 3.37 / 38.64 ± 2.36</td> <!-- Dutch Social -->
   <td class="nl la">25.22 ± 5.45 / 61.28 ± 2.51</td> <!-- ScaLA-nl -->
   <td class="nl qa">46.34 ± 1.07 / 66.56 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.71 ± 0.59 / 17.76 ± 0.71</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.49 ± 2.59 / 53.52 ± 2.03</td> <!-- MMLU-nl -->
   <td class="nl reason">47.66 ± 2.91 / 60.31 ± 2.30</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.19 ± 2.03 / 55.64 ± 3.53</td> <!-- CoNLL-en -->
   <td class="en sent">63.77 ± 2.55 / 71.13 ± 1.83</td> <!-- SST5 -->
   <td class="en la">28.43 ± 3.97 / 62.28 ± 1.86</td> <!-- ScaLA-en -->
   <td class="en qa">44.39 ± 2.68 / 71.79 ± 1.25</td> <!-- SQuAD -->
   <td class="en summ">69.77 ± 0.76 / 24.60 ± 1.13</td> <!-- CNN-DailyMail -->
   <td class="en know">46.53 ± 2.54 / 59.53 ± 1.87</td> <!-- MMLU -->
   <td class="en reason">71.36 ± 3.95 / 78.36 ± 2.91</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- No Sammendrag version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- MMLU-no version -->
   <td>12.5.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.48</td> <!-- Danish rank -->
   <td class="no-rank">2.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.39</td> <!-- Swedish rank -->
   <td class="is-rank">3.64</td> <!-- Icelandic rank -->
   <td class="de-rank">2.20</td> <!-- German rank -->
   <td class="nl-rank">2.66</td> <!-- Dutch rank -->
   <td class="en-rank">1.93</td> <!-- English rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="da summ">66.47 ± 1.00 / 22.11 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">53.26 ± 1.94 / 64.50 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">58.26 ± 2.62 / 71.56 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.53 ± 2.03 / 37.79 ± 1.68</td> <!-- HellaSwag-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no summ">63.49 ± 1.49 / 16.48 ± 1.62</td> <!-- No Sammendrag -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">46.86 ± 3.27 / 70.86 ± 2.79</td> <!-- NorQuAD -->
   <td class="no know">27.78 ± 1.08 / 45.76 ± 0.79</td> <!-- MMLU-no -->
   <td class="no reason">10.88 ± 3.63 / 32.43 ± 2.67</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.87 ± 0.31 / 19.30 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">35.52 ± 1.01 / 51.52 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">19.67 ± 2.31 / 38.98 ± 1.98</td> <!-- HellaSwag-sv -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">25.70 ± 5.36 / 49.31 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.96 ± 3.10 / 16.11 ± 1.80</td> <!-- RRN -->
   <td class="is know">10.31 ± 1.06 / 32.74 ± 0.64</td> <!-- MMLU-is -->
   <td class="is reason">1.99 ± 2.95 / 54.48 ± 1.27</td> <!-- Winogrande-is -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
   <td class="de summ">68.24 ± 0.70 / 25.71 ± 1.33</td> <!-- MLSum -->
   <td class="de know">35.63 ± 1.12 / 51.69 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">26.40 ± 1.86 / 43.98 ± 1.58</td> <!-- HellaSwag-de -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl qa">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.24 ± 0.91 / 17.54 ± 1.10</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.49 ± 0.57 / 51.51 ± 0.42</td> <!-- MMLU-nl -->
   <td class="nl reason">19.88 ± 1.80 / 39.13 ± 1.56</td> <!-- HellaSwag-nl -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
   <td class="en summ">69.11 ± 0.31 / 23.70 ± 0.53</td> <!-- CNN-DailyMail -->
   <td class="en know">47.74 ± 1.26 / 60.63 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">34.96 ± 4.19 / 49.62 ± 3.28</td> <!-- HellaSwag -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.1.2</td> <!-- MMLU-no version -->
   <td>9.1.2</td> <!-- HellaSwag-no version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.1.2</td> <!-- MMLU-sv version -->
   <td>9.1.2</td> <!-- HellaSwag-sv version -->
   <td>9.1.2</td> <!-- MIM-GOLD-NER version -->
   <td>9.1.2</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>9.1.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.1.2</td> <!-- GermEval version -->
   <td>9.1.2</td> <!-- SB10k version -->
   <td>9.1.2</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>11.0.0</td> <!-- MLSum version -->
   <td>9.1.2</td> <!-- MMLU-de version -->
   <td>9.2.0</td> <!-- HellaSwag-de version -->
   <td>9.1.2</td> <!-- CoNLL-nl version -->
   <td>9.1.2</td> <!-- Dutch Social version -->
   <td>9.1.2</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   <td>9.1.2</td> <!-- CoNLL-en version -->
   <td>9.1.2</td> <!-- SST5 version -->
   <td>9.1.2</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>11.0.0</td> <!-- CNN-DailyMail version -->
   <td>9.2.0</td> <!-- MMLU version -->
   <td>9.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="is-rank">3.62</td> <!-- Icelandic rank -->
   <td class="de-rank">2.19</td> <!-- German rank -->
   <td class="nl-rank">2.68</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
   <td class="da ner">43.60 ± 2.94 / 32.17 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.92 ± 1.50 / 61.91 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">15.43 ± 3.79 / 46.20 ± 5.54</td> <!-- ScaLA-da -->
   <td class="da qa">59.13 ± 0.86 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.33 ± 0.98 / 22.03 ± 0.96</td> <!-- Nordjylland-News -->
   <td class="da know">53.81 ± 1.88 / 64.81 ± 1.53</td> <!-- Danske Talemaader -->
   <td class="da know">61.06 ± 2.83 / 73.89 ± 2.00</td> <!-- Danish Citizen Tests -->
   <td class="da reason">20.64 ± 1.95 / 39.21 ± 1.79</td> <!-- HellaSwag-da -->
   <td class="no ner">50.56 ± 2.04 / 44.38 ± 1.85</td> <!-- NorNE-nb -->
   <td class="no ner">52.65 ± 2.27 / 46.48 ± 3.65</td> <!-- NorNE-nn -->
   <td class="no sent">44.61 ± 2.28 / 62.22 ± 2.10</td> <!-- NoReC -->
   <td class="no summ">63.13 ± 1.63 / 16.19 ± 1.73</td> <!-- No Sammendrag -->
   <td class="no la">12.10 ± 4.22 / 43.27 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">9.30 ± 0.99 / 46.11 ± 3.47</td> <!-- ScaLA-nn -->
   <td class="no qa">45.15 ± 3.72 / 68.61 ± 3.30</td> <!-- NorQuAD -->
   <td class="no know">28.31 ± 1.01 / 45.93 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">13.59 ± 2.44 / 33.95 ± 1.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.79 ± 0.32 / 19.30 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.51 ± 1.13 / 50.46 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">20.84 ± 2.19 / 39.88 ± 1.85</td> <!-- HellaSwag-sv -->
   <td class="is ner">44.68 ± 3.50 / 36.20 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.12 ± 1.68 / 35.09 ± 1.17</td> <!-- ScaLA-is -->
   <td class="is qa">25.52 ± 5.24 / 49.15 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.40 ± 2.38 / 14.90 ± 1.60</td> <!-- RRN -->
   <td class="is know">10.43 ± 0.98 / 32.74 ± 0.69</td> <!-- MMLU-is -->
   <td class="is reason">5.24 ± 1.65 / 52.80 ± 2.41</td> <!-- Winogrande-is -->
   <td class="de ner">55.41 ± 1.45 / 48.39 ± 1.46</td> <!-- GermEval -->
   <td class="de sent">52.58 ± 2.42 / 67.52 ± 1.82</td> <!-- SB10k -->
   <td class="de la">24.10 ± 2.12 / 59.47 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de qa">31.52 ± 2.95 / 60.03 ± 3.81</td> <!-- GermanQuAD -->
   <td class="de summ">68.96 ± 1.13 / 28.26 ± 2.32</td> <!-- MLSum -->
   <td class="de know">35.06 ± 0.54 / 51.20 ± 0.43</td> <!-- MMLU-de -->
   <td class="de reason">28.85 ± 1.70 / 45.83 ± 1.39</td> <!-- HellaSwag-de -->
   <td class="nl ner">56.52 ± 1.42 / 41.84 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.02 ± 1.21 / 26.40 ± 2.96</td> <!-- Dutch Social -->
   <td class="nl la">23.41 ± 2.91 / 59.14 ± 3.11</td> <!-- ScaLA-nl -->
   <td class="nl qa">61.90 ± 1.07 / 72.49 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.74 / 17.69 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.93 ± 1.11 / 51.02 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">23.73 ± 1.97 / 41.93 ± 1.68</td> <!-- HellaSwag-nl -->
   <td class="en ner">61.02 ± 2.74 / 55.65 ± 2.55</td> <!-- CoNLL-en -->
   <td class="en sent">67.29 ± 0.80 / 70.81 ± 0.84</td> <!-- SST5 -->
   <td class="en la">30.10 ± 5.12 / 62.99 ± 4.71</td> <!-- ScaLA-en -->
   <td class="en qa">73.59 ± 1.75 / 84.31 ± 1.35</td> <!-- SQuAD -->
   <td class="en summ">69.04 ± 0.56 / 23.86 ± 0.77</td> <!-- CNN-DailyMail -->
   <td class="en know">47.63 ± 1.17 / 60.45 ± 0.88</td> <!-- MMLU -->
   <td class="en reason">35.63 ± 4.21 / 49.72 ± 3.73</td> <!-- HellaSwag -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.41</td> <!-- Danish rank -->
   <td class="no-rank">2.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="is-rank">3.65</td> <!-- Icelandic rank -->
   <td class="de-rank">2.19</td> <!-- German rank -->
   <td class="nl-rank">2.66</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da qa">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.30 ± 1.02 / 21.99 ± 1.01</td> <!-- Nordjylland-News -->
   <td class="da know">53.67 ± 1.74 / 64.67 ± 1.45</td> <!-- Danske Talemaader -->
   <td class="da know">54.52 ± 2.51 / 68.59 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">20.51 ± 2.03 / 39.10 ± 1.86</td> <!-- HellaSwag-da -->
   <td class="no ner">50.63 ± 2.12 / 44.59 ± 1.80</td> <!-- NorNE-nb -->
   <td class="no ner">52.69 ± 2.30 / 46.51 ± 3.63</td> <!-- NorNE-nn -->
   <td class="no sent">44.05 ± 2.51 / 61.80 ± 2.28</td> <!-- NoReC -->
   <td class="no summ">63.11 ± 1.66 / 16.14 ± 1.73</td> <!-- No Sammendrag -->
   <td class="no la">11.60 ± 4.10 / 43.01 ± 5.07</td> <!-- ScaLA-nb -->
   <td class="no la">9.26 ± 1.14 / 46.28 ± 3.60</td> <!-- ScaLA-nn -->
   <td class="no qa">45.23 ± 3.73 / 68.68 ± 3.29</td> <!-- NorQuAD -->
   <td class="no know">28.19 ± 0.84 / 45.83 ± 0.68</td> <!-- MMLU-no -->
   <td class="no reason">13.65 ± 2.51 / 34.00 ± 1.87</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.33 / 19.24 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.52 ± 1.19 / 50.47 ± 0.93</td> <!-- MMLU-sv -->
   <td class="sv reason">20.96 ± 1.96 / 39.95 ± 1.66</td> <!-- HellaSwag-sv -->
   <td class="is ner">44.85 ± 3.44 / 36.23 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.69 ± 2.06 / 35.01 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is qa">25.52 ± 5.27 / 49.12 ± 5.22</td> <!-- NQiI -->
   <td class="is summ">61.54 ± 2.35 / 15.01 ± 1.61</td> <!-- RRN -->
   <td class="is know">10.42 ± 0.56 / 32.72 ± 0.36</td> <!-- MMLU-is -->
   <td class="is reason">4.46 ± 1.81 / 51.42 ± 2.60</td> <!-- Winogrande-is -->
   <td class="de ner">55.32 ± 1.55 / 48.33 ± 1.45</td> <!-- GermEval -->
   <td class="de sent">52.49 ± 2.16 / 67.50 ± 1.61</td> <!-- SB10k -->
   <td class="de la">24.34 ± 2.29 / 59.66 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de qa">31.54 ± 3.00 / 59.96 ± 3.89</td> <!-- GermanQuAD -->
   <td class="de summ">68.98 ± 1.14 / 28.30 ± 2.36</td> <!-- MLSum -->
   <td class="de know">35.12 ± 0.59 / 51.23 ± 0.46</td> <!-- MMLU-de -->
   <td class="de reason">28.89 ± 1.81 / 45.85 ± 1.47</td> <!-- HellaSwag-de -->
   <td class="nl ner">56.76 ± 1.52 / 42.03 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.11 ± 1.17 / 26.36 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">23.55 ± 2.76 / 59.14 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl qa">61.89 ± 1.10 / 72.41 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.33 ± 0.72 / 17.66 ± 0.87</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.92 ± 1.07 / 51.02 ± 0.85</td> <!-- MMLU-nl -->
   <td class="nl reason">23.87 ± 1.80 / 42.03 ± 1.58</td> <!-- HellaSwag-nl -->
   <td class="en ner">61.02 ± 2.70 / 55.57 ± 2.50</td> <!-- CoNLL-en -->
   <td class="en sent">67.10 ± 0.81 / 70.66 ± 0.76</td> <!-- SST5 -->
   <td class="en la">29.82 ± 5.18 / 62.86 ± 4.72</td> <!-- ScaLA-en -->
   <td class="en qa">73.50 ± 1.67 / 84.26 ± 1.30</td> <!-- SQuAD -->
   <td class="en summ">69.02 ± 0.55 / 23.87 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">47.13 ± 1.24 / 60.08 ± 0.92</td> <!-- MMLU -->
   <td class="en reason">35.88 ± 4.42 / 49.95 ± 3.87</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.1</td> <!-- Angry Tweets version -->
   <td>12.5.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.1</td> <!-- Danske Talemaader version -->
   <td>12.5.1</td> <!-- Danish Citizen Tests version -->
   <td>12.5.1</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.1</td> <!-- NoReC version -->
   <td>12.5.1</td> <!-- No Sammendrag version -->
   <td>12.5.1</td> <!-- ScaLA-nb version -->
   <td>12.5.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>12.5.1</td> <!-- MMLU-no version -->
   <td>12.5.1</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.1</td> <!-- SweReC version -->
   <td>12.5.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.5.1</td> <!-- SweDN version -->
   <td>12.5.1</td> <!-- MMLU-sv version -->
   <td>12.5.1</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">2.78</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.29</td> <!-- Swedish rank -->
   <td class="is-rank">3.76</td> <!-- Icelandic rank -->
   <td class="de-rank">2.46</td> <!-- German rank -->
   <td class="nl-rank">2.99</td> <!-- Dutch rank -->
   <td class="en-rank">2.08</td> <!-- English rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da qa">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
   <td class="da summ">65.43 ± 1.12 / 20.36 ± 0.95</td> <!-- Nordjylland-News -->
   <td class="da know">50.76 ± 1.75 / 62.66 ± 1.43</td> <!-- Danske Talemaader -->
   <td class="da know">50.82 ± 1.17 / 66.66 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.47 ± 2.35 / 34.86 ± 1.97</td> <!-- HellaSwag-da -->
   <td class="no ner">48.97 ± 2.42 / 39.15 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">51.52 ± 2.96 / 40.17 ± 3.62</td> <!-- NorNE-nn -->
   <td class="no sent">49.05 ± 2.73 / 63.94 ± 2.42</td> <!-- NoReC -->
   <td class="no summ">63.32 ± 1.58 / 16.33 ± 1.63</td> <!-- No Sammendrag -->
   <td class="no la">14.37 ± 2.18 / 47.80 ± 4.36</td> <!-- ScaLA-nb -->
   <td class="no la">9.96 ± 1.34 / 48.97 ± 3.77</td> <!-- ScaLA-nn -->
   <td class="no qa">44.07 ± 3.40 / 68.49 ± 2.97</td> <!-- NorQuAD -->
   <td class="no know">25.07 ± 1.48 / 43.13 ± 1.15</td> <!-- MMLU-no -->
   <td class="no reason">15.56 ± 3.55 / 35.85 ± 2.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.15 ± 0.31 / 18.72 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">33.24 ± 0.85 / 49.69 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">25.50 ± 2.25 / 43.44 ± 2.03</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.47 ± 4.24 / 30.33 ± 3.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is qa">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="is summ">63.68 ± 1.75 / 16.38 ± 1.24</td> <!-- RRN -->
   <td class="is know">6.94 ± 0.88 / 30.23 ± 0.46</td> <!-- MMLU-is -->
   <td class="is reason">8.30 ± 1.28 / 57.35 ± 0.75</td> <!-- Winogrande-is -->
   <td class="de ner">50.66 ± 1.53 / 39.89 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">54.79 ± 3.53 / 68.79 ± 3.00</td> <!-- SB10k -->
   <td class="de la">20.17 ± 1.69 / 58.67 ± 1.13</td> <!-- ScaLA-de -->
   <td class="de qa">27.86 ± 4.70 / 54.38 ± 5.91</td> <!-- GermanQuAD -->
   <td class="de summ">65.53 ± 1.07 / 19.46 ± 1.48</td> <!-- MLSum -->
   <td class="de know">27.04 ± 1.04 / 44.99 ± 0.77</td> <!-- MMLU-de -->
   <td class="de reason">17.47 ± 3.26 / 36.70 ± 2.93</td> <!-- HellaSwag-de -->
   <td class="nl ner">54.56 ± 2.96 / 37.86 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.43 ± 1.27 / 24.23 ± 0.94</td> <!-- Dutch Social -->
   <td class="nl la">10.99 ± 2.55 / 50.46 ± 4.17</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.91 ± 1.08 / 66.78 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.88 ± 1.41 / 12.36 ± 1.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.12 ± 1.17 / 43.50 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">10.65 ± 1.55 / 31.51 ± 1.52</td> <!-- HellaSwag-nl -->
   <td class="en ner">59.10 ± 1.87 / 51.31 ± 1.87</td> <!-- CoNLL-en -->
   <td class="en sent">68.41 ± 1.17 / 70.85 ± 0.74</td> <!-- SST5 -->
   <td class="en la">25.43 ± 4.22 / 60.79 ± 3.45</td> <!-- ScaLA-en -->
   <td class="en qa">71.89 ± 2.20 / 82.99 ± 1.78</td> <!-- SQuAD -->
   <td class="en summ">67.99 ± 0.41 / 22.12 ± 0.52</td> <!-- CNN-DailyMail -->
   <td class="en know">44.09 ± 1.21 / 56.37 ± 0.96</td> <!-- MMLU -->
   <td class="en reason">32.29 ± 4.57 / 45.16 ± 4.28</td> <!-- HellaSwag -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.3</td> <!-- Danske Talemaader version -->
   <td>12.5.3</td> <!-- Danish Citizen Tests version -->
   <td>12.5.3</td> <!-- HellaSwag-da version -->
   <td>12.5.3</td> <!-- NorNE-nb version -->
   <td>12.5.3</td> <!-- NorNE-nn version -->
   <td>12.5.3</td> <!-- NoReC version -->
   <td>12.5.3</td> <!-- No Sammendrag version -->
   <td>12.5.3</td> <!-- ScaLA-nb version -->
   <td>12.5.3</td> <!-- ScaLA-nn version -->
   <td>12.5.3</td> <!-- NorQuAD version -->
   <td>12.5.3</td> <!-- MMLU-no version -->
   <td>12.5.3</td> <!-- HellaSwag-no version -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   <td>12.5.3</td> <!-- SweDN version -->
   <td>12.5.3</td> <!-- MMLU-sv version -->
   <td>12.5.3</td> <!-- HellaSwag-sv version -->
   <td>12.5.3</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.3</td> <!-- ScaLA-is version -->
   <td>12.5.3</td> <!-- NQiI version -->
   <td>12.5.3</td> <!-- RRN version -->
   <td>12.5.3</td> <!-- MMLU-is version -->
   <td>12.5.3</td> <!-- Winogrande-is version -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- MLSum version -->
   <td>12.5.3</td> <!-- MMLU-de version -->
   <td>12.5.3</td> <!-- HellaSwag-de version -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   <td>12.5.3</td> <!-- CNN-DailyMail version -->
   <td>12.5.3</td> <!-- MMLU version -->
   <td>12.5.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.93</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.60</td> <!-- Swedish rank -->
   <td class="is-rank">3.75</td> <!-- Icelandic rank -->
   <td class="de-rank">2.41</td> <!-- German rank -->
   <td class="nl-rank">2.65</td> <!-- Dutch rank -->
   <td class="en-rank">2.20</td> <!-- English rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da qa">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
   <td class="da summ">66.84 ± 0.77 / 21.21 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">51.60 ± 1.33 / 63.50 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.85 ± 2.68 / 52.62 ± 2.08</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.21 ± 1.60 / 40.78 ± 1.32</td> <!-- HellaSwag-da -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no summ">64.43 ± 0.45 / 16.11 ± 0.97</td> <!-- No Sammendrag -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no qa">35.74 ± 2.44 / 64.27 ± 2.42</td> <!-- NorQuAD -->
   <td class="no know">20.37 ± 1.34 / 39.32 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">21.16 ± 2.07 / 39.85 ± 1.73</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.11 ± 0.18 / 19.64 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">25.60 ± 1.10 / 43.53 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">21.75 ± 1.61 / 40.57 ± 1.45</td> <!-- HellaSwag-sv -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is qa">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.01 ± 1.51 / 18.34 ± 1.35</td> <!-- RRN -->
   <td class="is know">7.55 ± 0.67 / 29.89 ± 0.47</td> <!-- MMLU-is -->
   <td class="is reason">0.24 ± 0.71 / 38.95 ± 0.84</td> <!-- Winogrande-is -->
   <td class="de ner">55.10 ± 1.35 / 41.89 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">47.69 ± 2.35 / 64.93 ± 1.71</td> <!-- SB10k -->
   <td class="de la">24.14 ± 2.09 / 60.83 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de qa">23.93 ± 2.11 / 57.64 ± 1.89</td> <!-- GermanQuAD -->
   <td class="de summ">67.51 ± 0.71 / 22.63 ± 1.73</td> <!-- MLSum -->
   <td class="de know">26.06 ± 1.65 / 44.13 ± 1.29</td> <!-- MMLU-de -->
   <td class="de reason">31.09 ± 1.35 / 47.48 ± 0.98</td> <!-- HellaSwag-de -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.99 ± 0.49 / 19.54 ± 0.55</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.86 ± 1.89 / 41.71 ± 1.45</td> <!-- MMLU-nl -->
   <td class="nl reason">24.80 ± 1.77 / 42.93 ± 1.38</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
   <td class="en summ">69.75 ± 0.63 / 24.71 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">34.93 ± 1.35 / 50.71 ± 1.00</td> <!-- MMLU -->
   <td class="en reason">44.91 ± 2.44 / 58.07 ± 1.93</td> <!-- HellaSwag -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- MMLU-no version -->
   <td>9.3.2</td> <!-- HellaSwag-no version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.2</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.2</td> <!-- MMLU version -->
   <td>9.3.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="da-rank">2.65</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.41</td> <!-- Swedish rank -->
   <td class="is-rank">3.88</td> <!-- Icelandic rank -->
   <td class="de-rank">2.33</td> <!-- German rank -->
   <td class="nl-rank">2.84</td> <!-- Dutch rank -->
   <td class="en-rank">2.14</td> <!-- English rank -->
   <td class="da ner">41.28 ± 3.92 / 31.98 ± 3.26</td> <!-- DANSK -->
   <td class="da sent">23.01 ± 3.87 / 36.55 ± 6.42</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 2.75 / 58.11 ± 3.45</td> <!-- ScaLA-da -->
   <td class="da qa">60.29 ± 0.81 / 65.52 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.28 ± 1.20 / 21.69 ± 1.21</td> <!-- Nordjylland-News -->
   <td class="da know">50.30 ± 2.37 / 61.85 ± 1.93</td> <!-- Danske Talemaader -->
   <td class="da know">56.24 ± 2.29 / 70.27 ± 1.64</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.43 ± 0.95 / 35.31 ± 0.71</td> <!-- HellaSwag-da -->
   <td class="no ner">51.12 ± 3.13 / 47.26 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">55.35 ± 1.60 / 49.99 ± 2.21</td> <!-- NorNE-nn -->
   <td class="no sent">23.75 ± 3.25 / 42.92 ± 4.45</td> <!-- NoReC -->
   <td class="no summ">64.56 ± 1.30 / 18.13 ± 1.51</td> <!-- No Sammendrag -->
   <td class="no la">14.00 ± 4.25 / 42.71 ± 5.83</td> <!-- ScaLA-nb -->
   <td class="no la">7.61 ± 2.57 / 45.86 ± 3.96</td> <!-- ScaLA-nn -->
   <td class="no qa">49.24 ± 4.28 / 72.68 ± 3.66</td> <!-- NorQuAD -->
   <td class="no know">23.60 ± 1.05 / 42.20 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">16.55 ± 2.83 / 35.97 ± 1.94</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.59 ± 0.34 / 18.56 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">25.51 ± 0.81 / 43.68 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">14.97 ± 1.73 / 34.85 ± 1.34</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.56 ± 3.03 / 34.23 ± 3.45</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.73 ± 1.56 / 45.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is qa">21.97 ± 4.26 / 46.27 ± 3.94</td> <!-- NQiI -->
   <td class="is summ">63.50 ± 2.92 / 16.51 ± 2.19</td> <!-- RRN -->
   <td class="is know">6.74 ± 1.22 / 30.40 ± 0.79</td> <!-- MMLU-is -->
   <td class="is reason">-5.80 ± 2.91 / 46.82 ± 2.65</td> <!-- Winogrande-is -->
   <td class="de ner">52.08 ± 1.86 / 46.67 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">46.38 ± 2.70 / 60.32 ± 2.80</td> <!-- SB10k -->
   <td class="de la">22.39 ± 3.96 / 57.26 ± 4.22</td> <!-- ScaLA-de -->
   <td class="de qa">33.43 ± 2.38 / 62.65 ± 2.83</td> <!-- GermanQuAD -->
   <td class="de summ">69.50 ± 1.29 / 29.74 ± 3.10</td> <!-- MLSum -->
   <td class="de know">28.79 ± 1.53 / 45.87 ± 1.26</td> <!-- MMLU-de -->
   <td class="de reason">21.50 ± 2.52 / 39.80 ± 2.47</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.55 ± 1.64 / 43.32 ± 1.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.26 ± 2.09 / 28.32 ± 2.68</td> <!-- Dutch Social -->
   <td class="nl la">24.57 ± 3.54 / 54.94 ± 5.33</td> <!-- ScaLA-nl -->
   <td class="nl qa">60.99 ± 0.95 / 72.74 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.02 ± 0.84 / 16.97 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.73 ± 0.90 / 45.62 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">19.43 ± 1.53 / 38.57 ± 1.39</td> <!-- HellaSwag-nl -->
   <td class="en ner">63.75 ± 2.50 / 59.28 ± 2.20</td> <!-- CoNLL-en -->
   <td class="en sent">61.85 ± 1.70 / 69.02 ± 0.76</td> <!-- SST5 -->
   <td class="en la">26.41 ± 4.93 / 59.67 ± 4.84</td> <!-- ScaLA-en -->
   <td class="en qa">73.48 ± 2.06 / 85.27 ± 1.15</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.58 / 22.39 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">38.04 ± 1.30 / 53.30 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">28.16 ± 3.07 / 44.80 ± 2.46</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">2.94</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.62</td> <!-- Swedish rank -->
   <td class="is-rank">3.75</td> <!-- Icelandic rank -->
   <td class="de-rank">2.23</td> <!-- German rank -->
   <td class="nl-rank">2.79</td> <!-- Dutch rank -->
   <td class="en-rank">2.21</td> <!-- English rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da qa">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="da summ">66.68 ± 0.81 / 22.38 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">44.30 ± 2.46 / 57.00 ± 2.30</td> <!-- Danske Talemaader -->
   <td class="da know">48.76 ± 2.39 / 65.51 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.44 ± 1.66 / 35.82 ± 1.14</td> <!-- HellaSwag-da -->
   <td class="no ner">45.50 ± 2.71 / 40.02 ± 3.16</td> <!-- NorNE-nb -->
   <td class="no ner">45.96 ± 2.67 / 41.28 ± 2.25</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 3.40 / 62.00 ± 2.71</td> <!-- NoReC -->
   <td class="no summ">63.95 ± 0.42 / 16.91 ± 0.61</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">52.19 ± 2.88 / 74.97 ± 2.11</td> <!-- NorQuAD -->
   <td class="no know">20.61 ± 1.27 / 39.79 ± 1.10</td> <!-- MMLU-no -->
   <td class="no reason">16.18 ± 1.88 / 36.19 ± 1.66</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.07 ± 0.34 / 19.59 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">25.52 ± 1.30 / 43.68 ± 1.03</td> <!-- MMLU-sv -->
   <td class="sv reason">14.06 ± 1.68 / 35.12 ± 1.47</td> <!-- HellaSwag-sv -->
   <td class="is ner">40.71 ± 2.93 / 34.57 ± 4.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is qa">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="is summ">65.25 ± 0.97 / 19.09 ± 1.05</td> <!-- RRN -->
   <td class="is know">8.10 ± 0.93 / 29.90 ± 0.88</td> <!-- MMLU-is -->
   <td class="is reason">0.35 ± 2.49 / 51.16 ± 2.74</td> <!-- Winogrande-is -->
   <td class="de ner">52.63 ± 1.89 / 42.99 ± 2.40</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de qa">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.43 ± 0.97 / 29.48 ± 2.59</td> <!-- MLSum -->
   <td class="de know">32.56 ± 1.16 / 49.02 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">23.61 ± 2.42 / 41.55 ± 2.14</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.78 ± 1.86 / 41.29 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl qa">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.46 ± 0.67 / 19.49 ± 0.92</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.37 ± 0.99 / 45.81 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">15.25 ± 1.71 / 35.83 ± 1.42</td> <!-- HellaSwag-nl -->
   <td class="en ner">56.90 ± 3.08 / 51.16 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.63 ± 0.46 / 25.61 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">38.48 ± 1.10 / 53.32 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">27.67 ± 2.08 / 43.61 ± 2.08</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.2.0</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.1</td> <!-- Danske Talemaader version -->
   <td>12.3.1</td> <!-- Danish Citizen Tests version -->
   <td>12.3.1</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.2.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.3.1</td> <!-- ScaLA-nb version -->
   <td>12.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.3.1</td> <!-- MMLU-no version -->
   <td>12.3.1</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.2.0</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.1</td> <!-- MMLU-sv version -->
   <td>12.3.1</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.3.1</td> <!-- MMLU-is version -->
   <td>12.3.1</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.2.0</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.3.1</td> <!-- MMLU-de version -->
   <td>12.3.1</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.2.0</td> <!-- Dutch Social version -->
   <td>12.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.3.1</td> <!-- MMLU-nl version -->
   <td>12.3.1</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.3.1</td> <!-- MMLU version -->
   <td>12.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.82</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.86</td> <!-- Swedish rank -->
   <td class="is-rank">4.00</td> <!-- Icelandic rank -->
   <td class="de-rank">1.98</td> <!-- German rank -->
   <td class="nl-rank">2.76</td> <!-- Dutch rank -->
   <td class="en-rank">1.70</td> <!-- English rank -->
   <td class="da ner">41.37 ± 2.50 / 24.64 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">42.60 ± 1.06 / 61.52 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">6.52 ± 1.34 / 45.01 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da qa">50.57 ± 1.03 / 57.75 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">64.55 ± 0.78 / 19.26 ± 0.48</td> <!-- Nordjylland-News -->
   <td class="da know">38.64 ± 1.52 / 53.92 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">42.12 ± 2.16 / 61.23 ± 1.46</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.66 ± 1.32 / 35.16 ± 1.02</td> <!-- HellaSwag-da -->
   <td class="no ner">56.33 ± 1.63 / 36.68 ± 3.27</td> <!-- NorNE-nb -->
   <td class="no ner">54.68 ± 1.29 / 37.85 ± 3.79</td> <!-- NorNE-nn -->
   <td class="no sent">37.18 ± 1.30 / 55.44 ± 1.46</td> <!-- NoReC -->
   <td class="no summ">61.44 ± 0.71 / 13.62 ± 0.60</td> <!-- No Sammendrag -->
   <td class="no la">6.76 ± 2.81 / 41.69 ± 2.82</td> <!-- ScaLA-nb -->
   <td class="no la">6.79 ± 1.51 / 45.45 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no qa">30.11 ± 2.09 / 52.56 ± 2.38</td> <!-- NorQuAD -->
   <td class="no know">15.54 ± 0.89 / 36.69 ± 0.67</td> <!-- MMLU-no -->
   <td class="no reason">17.55 ± 0.88 / 37.93 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.20 ± 0.99 / 15.57 ± 0.62</td> <!-- SweDN -->
   <td class="sv know">21.33 ± 1.03 / 41.04 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">16.12 ± 1.15 / 36.99 ± 0.85</td> <!-- HellaSwag-sv -->
   <td class="is ner">33.05 ± 4.29 / 29.75 ± 3.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 1.18 / 34.80 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is qa">17.23 ± 2.51 / 39.88 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">60.08 ± 1.45 / 13.80 ± 0.81</td> <!-- RRN -->
   <td class="is know">6.40 ± 1.04 / 29.45 ± 0.75</td> <!-- MMLU-is -->
   <td class="is reason">2.74 ± 2.28 / 53.18 ± 0.93</td> <!-- Winogrande-is -->
   <td class="de ner">59.68 ± 0.41 / 48.00 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.75 ± 2.36 / 68.54 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.22 ± 2.94 / 64.51 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de qa">29.27 ± 1.03 / 59.19 ± 2.46</td> <!-- GermanQuAD -->
   <td class="de summ">66.64 ± 0.91 / 22.90 ± 2.24</td> <!-- MLSum -->
   <td class="de know">39.50 ± 0.93 / 54.61 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">51.29 ± 1.38 / 63.10 ± 1.12</td> <!-- HellaSwag-de -->
   <td class="nl ner">50.31 ± 1.94 / 41.54 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.58 ± 1.62 / 36.56 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">14.72 ± 1.84 / 50.23 ± 3.10</td> <!-- ScaLA-nl -->
   <td class="nl qa">56.19 ± 0.80 / 66.72 ± 0.92</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.40 ± 0.77 / 17.47 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.31 ± 0.70 / 46.18 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">21.25 ± 1.25 / 40.78 ± 1.02</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.13 ± 1.16 / 53.55 ± 2.73</td> <!-- CoNLL-en -->
   <td class="en sent">63.66 ± 1.31 / 70.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">34.07 ± 2.32 / 66.51 ± 1.23</td> <!-- ScaLA-en -->
   <td class="en qa">68.10 ± 1.44 / 83.46 ± 1.01</td> <!-- SQuAD -->
   <td class="en summ">69.32 ± 0.53 / 24.97 ± 0.93</td> <!-- CNN-DailyMail -->
   <td class="en know">59.24 ± 1.04 / 69.46 ± 0.78</td> <!-- MMLU -->
   <td class="en reason">74.58 ± 0.91 / 80.88 ± 0.69</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.5</td> <!-- MMLU-is version -->
   <td>12.10.5</td> <!-- Winogrande-is version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.5</td> <!-- MMLU-de version -->
   <td>12.10.5</td> <!-- HellaSwag-de version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.5</td> <!-- MMLU-nl version -->
   <td>12.10.5</td> <!-- HellaSwag-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.5</td> <!-- MMLU version -->
   <td>12.10.5</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="da-rank">2.72</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="is-rank">3.89</td> <!-- Icelandic rank -->
   <td class="de-rank">2.31</td> <!-- German rank -->
   <td class="nl-rank">2.91</td> <!-- Dutch rank -->
   <td class="en-rank">2.31</td> <!-- English rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="da summ">66.05 ± 1.13 / 21.82 ± 0.96</td> <!-- Nordjylland-News -->
   <td class="da know">38.54 ± 1.47 / 53.57 ± 1.26</td> <!-- Danske Talemaader -->
   <td class="da know">45.89 ± 3.00 / 63.14 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">12.38 ± 1.99 / 33.54 ± 1.61</td> <!-- HellaSwag-da -->
   <td class="no ner">45.28 ± 3.06 / 41.73 ± 2.14</td> <!-- NorNE-nb -->
   <td class="no ner">46.00 ± 4.26 / 42.96 ± 3.38</td> <!-- NorNE-nn -->
   <td class="no sent">44.95 ± 3.19 / 61.88 ± 2.88</td> <!-- NoReC -->
   <td class="no summ">63.26 ± 1.07 / 16.04 ± 1.34</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no qa">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td class="no know">20.87 ± 1.54 / 39.98 ± 1.27</td> <!-- MMLU-no -->
   <td class="no reason">13.10 ± 2.04 / 34.20 ± 1.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.45 / 18.79 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">23.68 ± 1.41 / 42.15 ± 1.14</td> <!-- MMLU-sv -->
   <td class="sv reason">14.05 ± 1.60 / 34.81 ± 1.58</td> <!-- HellaSwag-sv -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="is summ">62.55 ± 3.03 / 15.26 ± 2.31</td> <!-- RRN -->
   <td class="is know">7.64 ± 0.91 / 29.55 ± 1.22</td> <!-- MMLU-is -->
   <td class="is reason">-0.51 ± 1.95 / 47.23 ± 2.39</td> <!-- Winogrande-is -->
   <td class="de ner">51.39 ± 1.35 / 44.47 ± 2.77</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de qa">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.68 / 28.27 ± 1.70</td> <!-- MLSum -->
   <td class="de know">32.49 ± 0.91 / 48.82 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">22.25 ± 2.13 / 40.28 ± 1.67</td> <!-- HellaSwag-de -->
   <td class="nl ner">51.31 ± 2.32 / 42.95 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl qa">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.66 ± 0.74 / 18.22 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.12 ± 0.86 / 44.36 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">13.99 ± 2.04 / 34.45 ± 1.89</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.37 ± 2.94 / 51.08 ± 2.87</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en qa">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
   <td class="en summ">68.61 ± 0.55 / 23.48 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">37.04 ± 1.33 / 52.33 ± 1.02</td> <!-- MMLU -->
   <td class="en reason">23.54 ± 2.08 / 40.78 ± 1.59</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.2.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.2.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.2.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.2.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.2.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.2.0</td> <!-- MMLU-nl version -->
   <td>12.2.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.2.0</td> <!-- MMLU version -->
   <td>12.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.72</td> <!-- Swedish rank -->
   <td class="is-rank">3.89</td> <!-- Icelandic rank -->
   <td class="de-rank">2.52</td> <!-- German rank -->
   <td class="nl-rank">2.95</td> <!-- Dutch rank -->
   <td class="en-rank">2.12</td> <!-- English rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="da summ">65.80 ± 0.93 / 19.91 ± 1.41</td> <!-- Nordjylland-News -->
   <td class="da know">45.07 ± 1.34 / 58.18 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.36 ± 2.19 / 55.82 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.85 ± 1.19 / 35.26 ± 1.24</td> <!-- HellaSwag-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no summ">62.39 ± 0.76 / 14.24 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.23 ± 3.15 / 63.67 ± 2.98</td> <!-- NorQuAD -->
   <td class="no know">20.44 ± 1.03 / 39.51 ± 0.72</td> <!-- MMLU-no -->
   <td class="no reason">15.87 ± 1.29 / 35.89 ± 1.06</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.10 ± 0.60 / 18.05 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">24.03 ± 1.09 / 42.32 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">15.37 ± 0.71 / 35.78 ± 0.69</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">62.80 ± 1.69 / 15.23 ± 1.01</td> <!-- RRN -->
   <td class="is know">7.22 ± 1.33 / 29.40 ± 1.04</td> <!-- MMLU-is -->
   <td class="is reason">6.35 ± 2.71 / 50.49 ± 1.57</td> <!-- Winogrande-is -->
   <td class="de ner">47.19 ± 3.74 / 33.02 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">47.26 ± 3.14 / 63.48 ± 2.94</td> <!-- SB10k -->
   <td class="de la">22.32 ± 1.78 / 56.73 ± 4.00</td> <!-- ScaLA-de -->
   <td class="de qa">24.36 ± 3.78 / 54.61 ± 4.44</td> <!-- GermanQuAD -->
   <td class="de summ">67.75 ± 1.10 / 25.91 ± 2.95</td> <!-- MLSum -->
   <td class="de know">26.79 ± 1.01 / 44.58 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">20.33 ± 1.63 / 39.63 ± 1.09</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl qa">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.97 / 16.55 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.06 ± 0.77 / 44.08 ± 0.51</td> <!-- MMLU-nl -->
   <td class="nl reason">14.26 ± 1.48 / 35.14 ± 1.18</td> <!-- HellaSwag-nl -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
   <td class="en summ">69.62 ± 0.31 / 24.65 ± 0.44</td> <!-- CNN-DailyMail -->
   <td class="en know">38.40 ± 0.98 / 53.43 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">35.72 ± 1.56 / 49.69 ± 1.42</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="da-rank">3.11</td> <!-- Danish rank -->
   <td class="no-rank">3.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.99</td> <!-- Swedish rank -->
   <td class="is-rank">4.01</td> <!-- Icelandic rank -->
   <td class="de-rank">2.03</td> <!-- German rank -->
   <td class="nl-rank">2.76</td> <!-- Dutch rank -->
   <td class="en-rank">1.93</td> <!-- English rank -->
   <td class="da ner">4.51 ± 2.12 / 3.71 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">40.85 ± 1.26 / 59.79 ± 1.32</td> <!-- Angry Tweets -->
   <td class="da la">5.43 ± 1.74 / 46.21 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da qa">51.76 ± 0.73 / 58.44 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="da summ">64.64 ± 0.66 / 19.18 ± 0.74</td> <!-- Nordjylland-News -->
   <td class="da know">37.45 ± 1.45 / 52.86 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">36.39 ± 2.23 / 56.50 ± 1.51</td> <!-- Danish Citizen Tests -->
   <td class="da reason">17.42 ± 0.78 / 38.06 ± 0.55</td> <!-- HellaSwag-da -->
   <td class="no ner">52.18 ± 2.03 / 29.83 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">50.53 ± 1.49 / 31.94 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">33.30 ± 2.01 / 51.15 ± 2.93</td> <!-- NoReC -->
   <td class="no summ">60.69 ± 0.97 / 12.72 ± 0.74</td> <!-- No Sammendrag -->
   <td class="no la">2.63 ± 2.56 / 40.21 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">4.00 ± 1.87 / 44.87 ± 3.17</td> <!-- ScaLA-nn -->
   <td class="no qa">37.08 ± 2.44 / 61.14 ± 2.01</td> <!-- NorQuAD -->
   <td class="no know">17.34 ± 0.74 / 38.04 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">17.43 ± 1.21 / 38.01 ± 0.91</td> <!-- HellaSwag-no -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.28 ± 0.86 / 15.52 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">22.99 ± 1.08 / 42.27 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">20.19 ± 0.99 / 40.11 ± 0.71</td> <!-- HellaSwag-sv -->
   <td class="is ner">27.22 ± 3.65 / 24.21 ± 2.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.31 ± 1.28 / 39.67 ± 4.39</td> <!-- ScaLA-is -->
   <td class="is qa">17.24 ± 2.72 / 41.15 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.66 / 15.80 ± 1.12</td> <!-- RRN -->
   <td class="is know">7.06 ± 0.86 / 30.16 ± 0.67</td> <!-- MMLU-is -->
   <td class="is reason">1.06 ± 2.84 / 47.19 ± 2.14</td> <!-- Winogrande-is -->
   <td class="de ner">55.36 ± 0.81 / 36.14 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">53.05 ± 2.34 / 65.57 ± 1.92</td> <!-- SB10k -->
   <td class="de la">23.08 ± 1.54 / 58.65 ± 2.04</td> <!-- ScaLA-de -->
   <td class="de qa">31.55 ± 1.09 / 62.02 ± 2.17</td> <!-- GermanQuAD -->
   <td class="de summ">67.33 ± 0.98 / 24.07 ± 2.44</td> <!-- MLSum -->
   <td class="de know">39.57 ± 0.74 / 54.67 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">51.26 ± 0.93 / 63.03 ± 0.69</td> <!-- HellaSwag-de -->
   <td class="nl ner">44.27 ± 2.14 / 34.47 ± 2.48</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.84 ± 1.82 / 36.64 ± 1.13</td> <!-- Dutch Social -->
   <td class="nl la">10.44 ± 1.58 / 48.93 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl qa">56.40 ± 1.14 / 68.02 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.60 ± 0.62 / 15.63 ± 0.45</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.63 ± 0.84 / 46.39 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">22.58 ± 0.97 / 41.78 ± 0.71</td> <!-- HellaSwag-nl -->
   <td class="en ner">64.09 ± 0.96 / 49.92 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">46.77 ± 4.36 / 60.99 ± 2.15</td> <!-- SST5 -->
   <td class="en la">31.62 ± 2.25 / 63.73 ± 1.79</td> <!-- ScaLA-en -->
   <td class="en qa">71.25 ± 0.83 / 85.72 ± 0.57</td> <!-- SQuAD -->
   <td class="en summ">69.54 ± 0.57 / 24.79 ± 0.89</td> <!-- CNN-DailyMail -->
   <td class="en know">57.66 ± 1.17 / 68.22 ± 0.88</td> <!-- MMLU -->
   <td class="en reason">72.26 ± 0.86 / 79.10 ± 0.64</td> <!-- HellaSwag -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- Nordjylland-News version -->
   <td>12.10.0</td> <!-- Danske Talemaader version -->
   <td>12.10.0</td> <!-- Danish Citizen Tests version -->
   <td>12.10.0</td> <!-- HellaSwag-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.9.1</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- No Sammendrag version -->
   <td>12.9.1</td> <!-- ScaLA-nb version -->
   <td>12.9.1</td> <!-- ScaLA-nn version -->
   <td>12.9.1</td> <!-- NorQuAD version -->
   <td>12.10.0</td> <!-- MMLU-no version -->
   <td>12.10.0</td> <!-- HellaSwag-no version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   <td>12.9.1</td> <!-- MIM-GOLD-NER version -->
   <td>12.9.1</td> <!-- ScaLA-is version -->
   <td>12.9.1</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.0</td> <!-- MMLU-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.0</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="da-rank">2.86</td> <!-- Danish rank -->
   <td class="no-rank">2.91</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.03</td> <!-- Swedish rank -->
   <td class="is-rank">3.83</td> <!-- Icelandic rank -->
   <td class="de-rank">2.83</td> <!-- German rank -->
   <td class="nl-rank">2.79</td> <!-- Dutch rank -->
   <td class="en-rank">2.17</td> <!-- English rank -->
   <td class="da ner">43.83 ± 1.93 / 34.03 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">29.21 ± 1.92 / 52.86 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">12.96 ± 1.67 / 55.83 ± 0.88</td> <!-- ScaLA-da -->
   <td class="da qa">49.76 ± 0.59 / 56.52 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="da summ">65.36 ± 1.08 / 19.65 ± 1.01</td> <!-- Nordjylland-News -->
   <td class="da know">41.30 ± 1.79 / 54.09 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">31.26 ± 2.75 / 52.68 ± 2.10</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.02 ± 1.01 / 34.38 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">59.77 ± 2.77 / 56.12 ± 2.72</td> <!-- NorNE-nb -->
   <td class="no ner">60.98 ± 2.01 / 57.99 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">28.14 ± 1.90 / 49.76 ± 1.59</td> <!-- NoReC -->
   <td class="no summ">60.86 ± 1.60 / 13.66 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">14.01 ± 2.15 / 56.43 ± 1.08</td> <!-- ScaLA-nb -->
   <td class="no la">10.15 ± 1.06 / 54.56 ± 0.71</td> <!-- ScaLA-nn -->
   <td class="no qa">51.08 ± 2.83 / 74.34 ± 1.55</td> <!-- NorQuAD -->
   <td class="no know">19.07 ± 1.42 / 37.82 ± 1.42</td> <!-- MMLU-no -->
   <td class="no reason">16.52 ± 1.25 / 35.24 ± 1.25</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv qa">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.88 ± 0.30 / 18.58 ± 0.16</td> <!-- SweDN -->
   <td class="sv know">17.95 ± 1.18 / 36.41 ± 1.02</td> <!-- MMLU-sv -->
   <td class="sv reason">13.55 ± 1.32 / 33.39 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">37.69 ± 3.97 / 34.52 ± 3.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.11 ± 1.49 / 48.48 ± 2.77</td> <!-- ScaLA-is -->
   <td class="is qa">18.34 ± 2.07 / 43.26 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">63.71 ± 1.04 / 16.63 ± 0.98</td> <!-- RRN -->
   <td class="is know">7.59 ± 0.73 / 28.78 ± 0.60</td> <!-- MMLU-is -->
   <td class="is reason">-5.17 ± 2.94 / 53.84 ± 1.87</td> <!-- Winogrande-is -->
   <td class="de ner">54.20 ± 1.00 / 48.58 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">15.43 ± 3.70 / 43.11 ± 2.77</td> <!-- SB10k -->
   <td class="de la">17.49 ± 1.23 / 57.46 ± 1.12</td> <!-- ScaLA-de -->
   <td class="de qa">28.68 ± 5.36 / 60.07 ± 4.46</td> <!-- GermanQuAD -->
   <td class="de summ">64.87 ± 0.47 / 22.25 ± 1.89</td> <!-- MLSum -->
   <td class="de know">22.10 ± 0.68 / 40.39 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">18.58 ± 1.48 / 36.49 ± 1.24</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.93 ± 2.71 / 47.48 ± 2.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.83 ± 2.37 / 34.00 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">6.58 ± 3.36 / 48.51 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.45 ± 2.52 / 67.47 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.89 ± 0.38 / 17.99 ± 0.46</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">19.58 ± 1.24 / 38.76 ± 1.06</td> <!-- MMLU-nl -->
   <td class="nl reason">13.68 ± 1.08 / 32.30 ± 0.99</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.70 ± 0.99 / 61.08 ± 1.16</td> <!-- CoNLL-en -->
   <td class="en sent">55.62 ± 2.54 / 64.98 ± 2.03</td> <!-- SST5 -->
   <td class="en la">31.36 ± 2.63 / 65.21 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">72.58 ± 0.68 / 84.67 ± 0.91</td> <!-- SQuAD -->
   <td class="en summ">67.24 ± 0.71 / 21.99 ± 0.99</td> <!-- CNN-DailyMail -->
   <td class="en know">35.27 ± 1.22 / 50.12 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">32.54 ± 1.77 / 46.58 ± 1.66</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   <td>12.10.0</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.10.0</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- No Sammendrag version -->
   <td>12.10.0</td> <!-- ScaLA-nb version -->
   <td>12.10.0</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.0</td> <!-- MMLU-no version -->
   <td>12.10.0</td> <!-- HellaSwag-no version -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   <td>12.10.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.0</td> <!-- ScaLA-is version -->
   <td>12.10.0</td> <!-- NQiI version -->
   <td>12.10.0</td> <!-- RRN version -->
   <td>12.10.0</td> <!-- MMLU-is version -->
   <td>12.10.0</td> <!-- Winogrande-is version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.0</td> <!-- SST5 version -->
   <td>12.10.0</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.0</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="da-rank">2.76</td> <!-- Danish rank -->
   <td class="no-rank">3.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.82</td> <!-- Swedish rank -->
   <td class="is-rank">3.97</td> <!-- Icelandic rank -->
   <td class="de-rank">2.69</td> <!-- German rank -->
   <td class="nl-rank">2.93</td> <!-- Dutch rank -->
   <td class="en-rank">2.27</td> <!-- English rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">66.15 ± 0.67 / 19.69 ± 0.94</td> <!-- Nordjylland-News -->
   <td class="da know">32.17 ± 2.28 / 46.67 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">35.74 ± 2.46 / 55.18 ± 1.81</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.32 ± 0.41 / 32.24 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no summ">63.59 ± 0.40 / 14.15 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.77 ± 2.11 / 61.99 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">14.81 ± 0.79 / 34.79 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">12.69 ± 0.77 / 31.84 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.92 ± 0.05 / 18.51 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">17.73 ± 0.98 / 37.55 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">12.85 ± 0.93 / 33.37 ± 0.90</td> <!-- HellaSwag-sv -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">62.30 ± 0.90 / 13.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.27 ± 0.84 / 26.91 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">1.84 ± 2.19 / 43.79 ± 0.73</td> <!-- Winogrande-is -->
   <td class="de ner">50.09 ± 1.33 / 38.59 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">46.52 ± 2.85 / 63.64 ± 2.10</td> <!-- SB10k -->
   <td class="de la">15.23 ± 1.71 / 55.08 ± 1.88</td> <!-- ScaLA-de -->
   <td class="de qa">25.54 ± 3.58 / 56.07 ± 3.76</td> <!-- GermanQuAD -->
   <td class="de summ">67.62 ± 0.89 / 23.52 ± 2.43</td> <!-- MLSum -->
   <td class="de know">20.12 ± 1.13 / 39.48 ± 1.02</td> <!-- MMLU-de -->
   <td class="de reason">13.98 ± 1.56 / 34.07 ± 1.30</td> <!-- HellaSwag-de -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.59 ± 0.56 / 18.45 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.19 ± 1.26 / 39.24 ± 1.03</td> <!-- MMLU-nl -->
   <td class="nl reason">11.42 ± 1.29 / 32.50 ± 1.10</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
   <td class="en summ">69.95 ± 0.32 / 25.22 ± 0.33</td> <!-- CNN-DailyMail -->
   <td class="en know">30.47 ± 0.70 / 46.82 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">30.18 ± 1.87 / 45.85 ± 1.98</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da-rank">2.81</td> <!-- Danish rank -->
   <td class="no-rank">3.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.89</td> <!-- Swedish rank -->
   <td class="is-rank">4.16</td> <!-- Icelandic rank -->
   <td class="de-rank">2.68</td> <!-- German rank -->
   <td class="nl-rank">2.91</td> <!-- Dutch rank -->
   <td class="en-rank">2.13</td> <!-- English rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da qa">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="da summ">63.22 ± 1.14 / 16.73 ± 1.50</td> <!-- Nordjylland-News -->
   <td class="da know">37.79 ± 1.24 / 52.64 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">29.62 ± 1.33 / 52.29 ± 1.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.87 ± 1.18 / 37.41 ± 0.90</td> <!-- HellaSwag-da -->
   <td class="no ner">44.83 ± 1.58 / 40.11 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 1.65 / 41.63 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">32.70 ± 1.59 / 45.73 ± 2.82</td> <!-- NoReC -->
   <td class="no summ">60.53 ± 1.97 / 12.86 ± 1.03</td> <!-- No Sammendrag -->
   <td class="no la">3.57 ± 1.55 / 37.05 ± 2.34</td> <!-- ScaLA-nb -->
   <td class="no la">1.61 ± 2.11 / 37.85 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td class="no know">17.00 ± 1.21 / 37.67 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">16.18 ± 1.00 / 36.91 ± 0.64</td> <!-- HellaSwag-no -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.90 ± 0.87 / 17.34 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">20.95 ± 0.97 / 40.87 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">16.59 ± 1.45 / 36.76 ± 1.20</td> <!-- HellaSwag-sv -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is qa">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="is summ">62.11 ± 2.22 / 14.98 ± 1.53</td> <!-- RRN -->
   <td class="is know">6.32 ± 1.09 / 29.87 ± 0.80</td> <!-- MMLU-is -->
   <td class="is reason">-1.89 ± 2.66 / 43.72 ± 0.92</td> <!-- Winogrande-is -->
   <td class="de ner">42.08 ± 1.65 / 36.90 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de qa">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td class="de summ">65.56 ± 1.65 / 20.45 ± 2.68</td> <!-- MLSum -->
   <td class="de know">23.76 ± 0.70 / 42.77 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">20.92 ± 1.16 / 40.56 ± 0.86</td> <!-- HellaSwag-de -->
   <td class="nl ner">42.52 ± 2.25 / 37.46 ± 3.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.75 ± 0.84 / 14.83 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.25 ± 1.22 / 43.08 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">16.21 ± 1.51 / 37.11 ± 1.16</td> <!-- HellaSwag-nl -->
   <td class="en ner">58.56 ± 1.99 / 54.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en qa">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">67.27 ± 0.39 / 19.77 ± 0.31</td> <!-- CNN-DailyMail -->
   <td class="en know">38.68 ± 1.02 / 53.45 ± 0.74</td> <!-- MMLU -->
   <td class="en reason">47.47 ± 1.28 / 60.44 ± 1.02</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="da-rank">2.88</td> <!-- Danish rank -->
   <td class="no-rank">3.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.74</td> <!-- Swedish rank -->
   <td class="is-rank">4.01</td> <!-- Icelandic rank -->
   <td class="de-rank">2.63</td> <!-- German rank -->
   <td class="nl-rank">3.11</td> <!-- Dutch rank -->
   <td class="en-rank">2.43</td> <!-- English rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="da summ">65.50 ± 0.82 / 19.96 ± 0.95</td> <!-- Nordjylland-News -->
   <td class="da know">20.18 ± 1.80 / 38.69 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">35.69 ± 2.31 / 57.05 ± 1.60</td> <!-- Danish Citizen Tests -->
   <td class="da reason">7.93 ± 1.49 / 29.76 ± 0.92</td> <!-- HellaSwag-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no summ">62.30 ± 1.81 / 14.85 ± 1.88</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">44.19 ± 4.13 / 66.18 ± 4.05</td> <!-- NorQuAD -->
   <td class="no know">14.48 ± 1.33 / 35.35 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">6.49 ± 1.39 / 28.64 ± 0.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.63 ± 0.39 / 18.68 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">15.65 ± 0.55 / 36.32 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">8.74 ± 1.34 / 29.87 ± 1.40</td> <!-- HellaSwag-sv -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">5.05 ± 1.56 / 28.95 ± 1.00</td> <!-- MMLU-is -->
   <td class="is reason">-0.00 ± 2.41 / 44.93 ± 0.92</td> <!-- Winogrande-is -->
   <td class="de ner">43.02 ± 1.93 / 32.69 ± 1.98</td> <!-- GermEval -->
   <td class="de sent">50.21 ± 2.43 / 65.81 ± 1.82</td> <!-- SB10k -->
   <td class="de la">15.79 ± 2.35 / 53.25 ± 4.45</td> <!-- ScaLA-de -->
   <td class="de qa">28.57 ± 5.09 / 55.54 ± 6.14</td> <!-- GermanQuAD -->
   <td class="de summ">68.68 ± 0.96 / 26.95 ± 1.81</td> <!-- MLSum -->
   <td class="de know">18.38 ± 1.36 / 38.12 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">8.45 ± 1.86 / 30.07 ± 1.49</td> <!-- HellaSwag-de -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">59.92 ± 0.61 / 70.24 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.58 ± 1.13 / 16.33 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.36 ± 1.12 / 37.44 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">6.68 ± 1.82 / 29.30 ± 1.02</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
   <td class="en summ">68.82 ± 0.54 / 23.58 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">25.98 ± 0.90 / 42.52 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">11.77 ± 1.81 / 31.25 ± 1.99</td> <!-- HellaSwag -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- MMLU-no version -->
   <td>9.2.0</td> <!-- HellaSwag-no version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   <td>9.2.0</td> <!-- MIM-GOLD-NER version -->
   <td>9.2.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>11.0.0</td> <!-- RRN version -->
   <td>9.2.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   <td>9.2.0</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.2.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   <td>9.2.0</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.2.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>9.2.0</td> <!-- MMLU version -->
   <td>9.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="da-rank">3.21</td> <!-- Danish rank -->
   <td class="no-rank">3.07</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.68</td> <!-- Swedish rank -->
   <td class="is-rank">4.25</td> <!-- Icelandic rank -->
   <td class="de-rank">2.92</td> <!-- German rank -->
   <td class="nl-rank">3.06</td> <!-- Dutch rank -->
   <td class="en-rank">1.96</td> <!-- English rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">64.15 ± 1.03 / 18.95 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">34.07 ± 2.13 / 50.17 ± 1.60</td> <!-- Danske Talemaader -->
   <td class="da know">33.75 ± 2.28 / 54.22 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.61 ± 1.51 / 34.38 ± 1.20</td> <!-- HellaSwag-da -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no summ">61.98 ± 1.45 / 14.38 ± 1.20</td> <!-- No Sammendrag -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.28 ± 3.58 / 62.78 ± 3.34</td> <!-- NorQuAD -->
   <td class="no know">23.14 ± 0.98 / 41.88 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">16.50 ± 1.60 / 36.98 ± 1.27</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.95 ± 0.86 / 60.77 ± 0.75</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.70 ± 0.76 / 17.52 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">25.28 ± 0.72 / 43.71 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">19.20 ± 1.18 / 38.76 ± 0.96</td> <!-- HellaSwag-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">16.91 ± 2.57 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="is summ">60.02 ± 3.15 / 14.22 ± 1.52</td> <!-- RRN -->
   <td class="is know">8.44 ± 0.73 / 31.23 ± 0.59</td> <!-- MMLU-is -->
   <td class="is reason">0.72 ± 2.33 / 52.54 ± 2.18</td> <!-- Winogrande-is -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 2.45 / 67.63 ± 1.87</td> <!-- SB10k -->
   <td class="de la">7.33 ± 2.53 / 37.69 ± 2.51</td> <!-- ScaLA-de -->
   <td class="de qa">30.05 ± 1.59 / 57.13 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.09 ± 1.28 / 23.20 ± 2.54</td> <!-- MLSum -->
   <td class="de know">30.33 ± 0.78 / 47.68 ± 0.54</td> <!-- MMLU-de -->
   <td class="de reason">22.89 ± 1.14 / 41.15 ± 1.08</td> <!-- HellaSwag-de -->
   <td class="nl ner">46.34 ± 2.00 / 33.30 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.96 ± 1.44 / 18.10 ± 2.39</td> <!-- Dutch Social -->
   <td class="nl la">0.88 ± 1.23 / 33.53 ± 0.48</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.33 ± 1.28 / 66.50 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.35 ± 1.57 / 14.29 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.33 ± 0.91 / 46.94 ± 0.68</td> <!-- MMLU-nl -->
   <td class="nl reason">20.27 ± 1.38 / 39.32 ± 1.12</td> <!-- HellaSwag-nl -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en qa">75.89 ± 1.84 / 85.86 ± 1.03</td> <!-- SQuAD -->
   <td class="en summ">64.51 ± 0.30 / 18.84 ± 0.32</td> <!-- CNN-DailyMail -->
   <td class="en know">50.89 ± 0.77 / 63.01 ± 0.60</td> <!-- MMLU -->
   <td class="en reason">68.29 ± 0.74 / 75.90 ± 0.62</td> <!-- HellaSwag -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>12.0.0</td> <!-- No Sammendrag version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   <td>9.3.2</td> <!-- MIM-GOLD-NER version -->
   <td>10.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>10.0.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.0</td> <!-- Dutch Social version -->
   <td>10.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>12.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>10.0.1</td> <!-- MMLU-nl version -->
   <td>10.0.1</td> <!-- HellaSwag-nl version -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.0</td> <!-- SST5 version -->
   <td>10.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>10.0.1</td> <!-- MMLU version -->
   <td>10.0.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.83</td> <!-- Swedish rank -->
   <td class="is-rank">4.08</td> <!-- Icelandic rank -->
   <td class="de-rank">2.78</td> <!-- German rank -->
   <td class="nl-rank">3.24</td> <!-- Dutch rank -->
   <td class="en-rank">2.47</td> <!-- English rank -->
   <td class="da ner">33.80 ± 2.66 / 25.32 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">31.57 ± 2.65 / 46.48 ± 3.84</td> <!-- Angry Tweets -->
   <td class="da la">2.76 ± 1.76 / 44.96 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da qa">54.20 ± 1.63 / 59.50 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="da summ">64.19 ± 1.01 / 17.67 ± 1.44</td> <!-- Nordjylland-News -->
   <td class="da know">17.75 ± 1.41 / 35.70 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">28.24 ± 2.88 / 52.50 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.50 ± 0.85 / 27.33 ± 0.64</td> <!-- HellaSwag-da -->
   <td class="no ner">42.78 ± 1.09 / 37.34 ± 1.81</td> <!-- NorNE-nb -->
   <td class="no ner">42.85 ± 1.93 / 37.34 ± 3.04</td> <!-- NorNE-nn -->
   <td class="no sent">36.68 ± 2.11 / 46.78 ± 2.71</td> <!-- NoReC -->
   <td class="no summ">59.58 ± 1.88 / 12.71 ± 1.18</td> <!-- No Sammendrag -->
   <td class="no la">2.39 ± 1.54 / 43.99 ± 3.66</td> <!-- ScaLA-nb -->
   <td class="no la">1.91 ± 1.37 / 44.20 ± 4.28</td> <!-- ScaLA-nn -->
   <td class="no qa">39.16 ± 2.56 / 62.28 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">13.41 ± 0.92 / 33.01 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">7.83 ± 1.64 / 29.50 ± 1.51</td> <!-- HellaSwag-no -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.90 ± 0.52 / 17.15 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">16.18 ± 0.78 / 34.88 ± 0.66</td> <!-- MMLU-sv -->
   <td class="sv reason">8.52 ± 1.90 / 29.96 ± 1.75</td> <!-- HellaSwag-sv -->
   <td class="is ner">27.44 ± 3.28 / 23.50 ± 3.29</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.46 ± 1.18 / 41.20 ± 3.25</td> <!-- ScaLA-is -->
   <td class="is qa">17.26 ± 3.80 / 39.06 ± 3.00</td> <!-- NQiI -->
   <td class="is summ">58.30 ± 4.50 / 14.03 ± 2.00</td> <!-- RRN -->
   <td class="is know">3.90 ± 0.95 / 26.12 ± 0.67</td> <!-- MMLU-is -->
   <td class="is reason">2.43 ± 2.93 / 55.15 ± 1.40</td> <!-- Winogrande-is -->
   <td class="de ner">39.41 ± 2.30 / 36.17 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">49.42 ± 4.33 / 61.57 ± 5.43</td> <!-- SB10k -->
   <td class="de la">6.02 ± 2.53 / 46.41 ± 4.35</td> <!-- ScaLA-de -->
   <td class="de qa">27.69 ± 4.39 / 54.92 ± 5.38</td> <!-- GermanQuAD -->
   <td class="de summ">66.75 ± 0.68 / 23.16 ± 0.88</td> <!-- MLSum -->
   <td class="de know">20.77 ± 0.92 / 39.29 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">10.47 ± 1.51 / 31.09 ± 1.36</td> <!-- HellaSwag-de -->
   <td class="nl ner">46.95 ± 2.32 / 36.13 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.34 ± 2.10 / 19.37 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">3.46 ± 1.91 / 41.32 ± 3.08</td> <!-- ScaLA-nl -->
   <td class="nl qa">57.07 ± 0.89 / 68.14 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.31 ± 0.64 / 17.24 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">18.21 ± 0.70 / 37.51 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">9.03 ± 1.04 / 29.35 ± 0.77</td> <!-- HellaSwag-nl -->
   <td class="en ner">41.02 ± 3.86 / 40.03 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">66.43 ± 0.78 / 57.25 ± 0.33</td> <!-- SST5 -->
   <td class="en la">5.17 ± 1.55 / 37.03 ± 2.40</td> <!-- ScaLA-en -->
   <td class="en qa">76.04 ± 0.97 / 85.31 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">70.28 ± 0.06 / 28.85 ± 0.17</td> <!-- CNN-DailyMail -->
   <td class="en know">34.92 ± 0.75 / 50.82 ± 0.73</td> <!-- MMLU -->
   <td class="en reason">18.73 ± 1.32 / 34.76 ± 0.91</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="da-rank">2.90</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.40</td> <!-- Swedish rank -->
   <td class="is-rank">4.34</td> <!-- Icelandic rank -->
   <td class="de-rank">2.87</td> <!-- German rank -->
   <td class="nl-rank">3.17</td> <!-- Dutch rank -->
   <td class="en-rank">2.09</td> <!-- English rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da qa">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">62.74 ± 1.62 / 16.48 ± 1.77</td> <!-- Nordjylland-News -->
   <td class="da know">37.49 ± 1.84 / 51.62 ± 1.43</td> <!-- Danske Talemaader -->
   <td class="da know">29.21 ± 3.46 / 52.40 ± 2.50</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.58 ± 1.48 / 36.33 ± 1.08</td> <!-- HellaSwag-da -->
   <td class="no ner">32.12 ± 5.17 / 32.01 ± 2.80</td> <!-- NorNE-nb -->
   <td class="no ner">36.86 ± 3.53 / 35.46 ± 3.07</td> <!-- NorNE-nn -->
   <td class="no sent">36.97 ± 1.94 / 55.08 ± 2.30</td> <!-- NoReC -->
   <td class="no summ">57.64 ± 2.16 / 11.53 ± 1.29</td> <!-- No Sammendrag -->
   <td class="no la">5.27 ± 3.31 / 40.91 ± 5.24</td> <!-- ScaLA-nb -->
   <td class="no la">1.40 ± 1.87 / 33.64 ± 0.74</td> <!-- ScaLA-nn -->
   <td class="no qa">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td class="no know">16.50 ± 1.40 / 36.63 ± 1.17</td> <!-- MMLU-no -->
   <td class="no reason">13.27 ± 2.02 / 34.42 ± 1.54</td> <!-- HellaSwag-no -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.24 ± 1.76 / 16.02 ± 0.88</td> <!-- SweDN -->
   <td class="sv know">22.04 ± 0.60 / 41.36 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">14.76 ± 1.28 / 35.27 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is qa">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">57.17 ± 3.07 / 11.73 ± 1.00</td> <!-- RRN -->
   <td class="is know">6.15 ± 0.90 / 29.29 ± 0.65</td> <!-- MMLU-is -->
   <td class="is reason">-1.71 ± 3.79 / 50.88 ± 1.29</td> <!-- Winogrande-is -->
   <td class="de ner">31.52 ± 2.96 / 29.20 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de qa">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.88 ± 1.25 / 21.37 ± 1.87</td> <!-- MLSum -->
   <td class="de know">21.32 ± 1.14 / 40.66 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">21.35 ± 0.89 / 40.77 ± 0.65</td> <!-- HellaSwag-de -->
   <td class="nl ner">35.74 ± 3.22 / 31.74 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.90 ± 1.59 / 14.17 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.20 ± 1.53 / 41.49 ± 1.08</td> <!-- MMLU-nl -->
   <td class="nl reason">13.11 ± 1.85 / 33.86 ± 1.69</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.45 ± 1.61 / 49.72 ± 1.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en qa">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
   <td class="en summ">68.67 ± 0.11 / 21.65 ± 0.21</td> <!-- CNN-DailyMail -->
   <td class="en know">39.82 ± 0.76 / 54.62 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">51.82 ± 1.03 / 63.79 ± 0.79</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.34</td> <!-- Danish rank -->
   <td class="no-rank">3.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.16</td> <!-- Swedish rank -->
   <td class="is-rank">4.40</td> <!-- Icelandic rank -->
   <td class="de-rank">3.03</td> <!-- German rank -->
   <td class="nl-rank">3.57</td> <!-- Dutch rank -->
   <td class="en-rank">2.41</td> <!-- English rank -->
   <td class="da ner">28.45 ± 1.61 / 22.90 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">39.09 ± 1.15 / 45.25 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.26 / 37.98 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da qa">51.67 ± 2.31 / 57.34 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="da summ">57.67 ± 0.91 / 11.58 ± 0.72</td> <!-- Nordjylland-News -->
   <td class="da know">11.94 ± 1.37 / 32.30 ± 0.94</td> <!-- Danske Talemaader -->
   <td class="da know">18.18 ± 2.76 / 45.98 ± 1.68</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.67 ± 1.70 / 26.59 ± 1.10</td> <!-- HellaSwag-da -->
   <td class="no ner">41.64 ± 3.64 / 39.43 ± 3.55</td> <!-- NorNE-nb -->
   <td class="no ner">42.37 ± 3.13 / 40.79 ± 3.10</td> <!-- NorNE-nn -->
   <td class="no sent">33.71 ± 2.57 / 55.00 ± 1.41</td> <!-- NoReC -->
   <td class="no summ">49.22 ± 1.24 / 6.32 ± 0.45</td> <!-- No Sammendrag -->
   <td class="no la">-0.19 ± 0.77 / 33.29 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.25 / 34.51 ± 2.09</td> <!-- ScaLA-nn -->
   <td class="no qa">30.14 ± 2.44 / 50.96 ± 3.46</td> <!-- NorQuAD -->
   <td class="no know">6.67 ± 0.74 / 28.30 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">3.50 ± 1.56 / 26.82 ± 1.38</td> <!-- HellaSwag-no -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.63 ± 1.02 / 13.45 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">8.72 ± 0.93 / 30.92 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">3.19 ± 0.62 / 26.88 ± 0.62</td> <!-- HellaSwag-sv -->
   <td class="is ner">32.19 ± 2.52 / 32.88 ± 2.18</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.37 ± 1.64 / 33.39 ± 0.55</td> <!-- ScaLA-is -->
   <td class="is qa">6.58 ± 2.15 / 27.03 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">51.86 ± 5.51 / 9.69 ± 2.07</td> <!-- RRN -->
   <td class="is know">2.35 ± 0.68 / 26.83 ± 0.58</td> <!-- MMLU-is -->
   <td class="is reason">-5.46 ± 3.10 / 45.95 ± 2.15</td> <!-- Winogrande-is -->
   <td class="de ner">34.81 ± 2.51 / 30.33 ± 2.95</td> <!-- GermEval -->
   <td class="de sent">51.01 ± 2.18 / 65.35 ± 2.23</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de qa">25.40 ± 3.91 / 49.38 ± 4.65</td> <!-- GermanQuAD -->
   <td class="de summ">63.53 ± 2.45 / 17.65 ± 2.20</td> <!-- MLSum -->
   <td class="de know">11.23 ± 0.71 / 33.23 ± 0.76</td> <!-- MMLU-de -->
   <td class="de reason">7.25 ± 1.63 / 29.15 ± 1.35</td> <!-- HellaSwag-de -->
   <td class="nl ner">36.58 ± 3.88 / 33.82 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.32 ± 1.30 / 24.04 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">4.01 ± 2.01 / 36.03 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl qa">52.81 ± 0.81 / 63.87 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.24 ± 1.79 / 10.76 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.24 ± 1.06 / 31.02 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">6.75 ± 0.83 / 28.50 ± 0.84</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.50 ± 1.70 / 41.85 ± 1.68</td> <!-- CoNLL-en -->
   <td class="en sent">64.69 ± 1.33 / 57.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">8.01 ± 1.97 / 51.78 ± 1.65</td> <!-- ScaLA-en -->
   <td class="en qa">71.81 ± 1.05 / 80.90 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.71 ± 0.11 / 27.72 ± 0.26</td> <!-- CNN-DailyMail -->
   <td class="en know">18.92 ± 0.73 / 38.74 ± 0.53</td> <!-- MMLU -->
   <td class="en reason">54.53 ± 0.89 / 65.79 ± 0.65</td> <!-- HellaSwag -->
   <td>12.10.8</td> <!-- DANSK version -->
   <td>12.10.8</td> <!-- Angry Tweets version -->
   <td>12.10.8</td> <!-- ScaLA-da version -->
   <td>12.10.8</td> <!-- ScandiQA-da version -->
   <td>12.10.8</td> <!-- Nordjylland-News version -->
   <td>12.10.8</td> <!-- Danske Talemaader version -->
   <td>12.10.8</td> <!-- Danish Citizen Tests version -->
   <td>12.10.8</td> <!-- HellaSwag-da version -->
   <td>12.10.8</td> <!-- NorNE-nb version -->
   <td>12.10.8</td> <!-- NorNE-nn version -->
   <td>12.10.8</td> <!-- NoReC version -->
   <td>12.10.8</td> <!-- No Sammendrag version -->
   <td>12.10.8</td> <!-- ScaLA-nb version -->
   <td>12.10.8</td> <!-- ScaLA-nn version -->
   <td>12.10.8</td> <!-- NorQuAD version -->
   <td>12.10.8</td> <!-- MMLU-no version -->
   <td>12.10.8</td> <!-- HellaSwag-no version -->
   <td>12.10.8</td> <!-- SUC3 version -->
   <td>12.10.8</td> <!-- SweReC version -->
   <td>12.10.8</td> <!-- ScaLA-sv version -->
   <td>12.10.8</td> <!-- ScandiQA-sv version -->
   <td>12.10.8</td> <!-- SweDN version -->
   <td>12.10.8</td> <!-- MMLU-sv version -->
   <td>12.10.8</td> <!-- HellaSwag-sv version -->
   <td>12.10.8</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.8</td> <!-- ScaLA-is version -->
   <td>12.10.8</td> <!-- NQiI version -->
   <td>12.10.8</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- MMLU-is version -->
   <td>12.10.8</td> <!-- Winogrande-is version -->
   <td>12.10.8</td> <!-- GermEval version -->
   <td>12.10.8</td> <!-- SB10k version -->
   <td>12.10.8</td> <!-- ScaLA-de version -->
   <td>12.10.8</td> <!-- GermanQuAD version -->
   <td>12.10.8</td> <!-- MLSum version -->
   <td>12.10.8</td> <!-- MMLU-de version -->
   <td>12.10.8</td> <!-- HellaSwag-de version -->
   <td>12.10.8</td> <!-- CoNLL-nl version -->
   <td>12.10.8</td> <!-- Dutch Social version -->
   <td>12.10.8</td> <!-- ScaLA-nl version -->
   <td>12.10.8</td> <!-- SQuAD-nl version -->
   <td>12.10.8</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   <td>12.10.8</td> <!-- CoNLL-en version -->
   <td>12.10.8</td> <!-- SST5 version -->
   <td>12.10.8</td> <!-- ScaLA-en version -->
   <td>12.10.8</td> <!-- SQuAD version -->
   <td>12.10.8</td> <!-- CNN-DailyMail version -->
   <td>12.10.8</td> <!-- MMLU version -->
   <td>12.10.8</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da-rank">3.27</td> <!-- Danish rank -->
   <td class="no-rank">3.73</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.24</td> <!-- Swedish rank -->
   <td class="is-rank">4.33</td> <!-- Icelandic rank -->
   <td class="de-rank">2.99</td> <!-- German rank -->
   <td class="nl-rank">3.43</td> <!-- Dutch rank -->
   <td class="en-rank">2.57</td> <!-- English rank -->
   <td class="da ner">24.93 ± 4.36 / 22.23 ± 3.32</td> <!-- DANSK -->
   <td class="da sent">31.65 ± 2.94 / 51.95 ± 2.92</td> <!-- Angry Tweets -->
   <td class="da la">0.06 ± 1.20 / 34.30 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da qa">51.47 ± 1.82 / 57.00 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="da summ">62.67 ± 1.16 / 17.33 ± 1.12</td> <!-- Nordjylland-News -->
   <td class="da know">16.13 ± 2.67 / 36.80 ± 2.07</td> <!-- Danske Talemaader -->
   <td class="da know">24.21 ± 2.83 / 49.43 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.27 ± 0.82 / 25.59 ± 0.52</td> <!-- HellaSwag-da -->
   <td class="no ner">32.21 ± 1.63 / 31.19 ± 1.29</td> <!-- NorNE-nb -->
   <td class="no ner">36.62 ± 1.94 / 36.40 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">16.98 ± 3.42 / 27.01 ± 3.17</td> <!-- NoReC -->
   <td class="no summ">55.91 ± 2.53 / 9.21 ± 1.23</td> <!-- No Sammendrag -->
   <td class="no la">1.57 ± 1.20 / 41.68 ± 4.20</td> <!-- ScaLA-nb -->
   <td class="no la">0.97 ± 1.79 / 40.10 ± 4.50</td> <!-- ScaLA-nn -->
   <td class="no qa">26.28 ± 1.51 / 44.62 ± 2.11</td> <!-- NorQuAD -->
   <td class="no know">8.41 ± 1.26 / 29.77 ± 1.22</td> <!-- MMLU-no -->
   <td class="no reason">2.47 ± 1.34 / 26.33 ± 1.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.86 ± 1.75 / 11.38 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">11.71 ± 0.83 / 32.71 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">0.81 ± 0.88 / 25.27 ± 0.59</td> <!-- HellaSwag-sv -->
   <td class="is ner">28.06 ± 2.33 / 29.10 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.10 ± 1.11 / 33.70 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is qa">11.07 ± 2.29 / 27.33 ± 1.88</td> <!-- NQiI -->
   <td class="is summ">56.42 ± 3.79 / 11.91 ± 1.72</td> <!-- RRN -->
   <td class="is know">4.14 ± 0.86 / 27.59 ± 0.82</td> <!-- MMLU-is -->
   <td class="is reason">-0.82 ± 2.52 / 53.16 ± 3.17</td> <!-- Winogrande-is -->
   <td class="de ner">37.68 ± 1.26 / 33.74 ± 1.78</td> <!-- GermEval -->
   <td class="de sent">46.00 ± 3.63 / 61.88 ± 2.94</td> <!-- SB10k -->
   <td class="de la">0.83 ± 0.84 / 33.38 ± 0.28</td> <!-- ScaLA-de -->
   <td class="de qa">26.65 ± 4.01 / 53.15 ± 4.26</td> <!-- GermanQuAD -->
   <td class="de summ">64.14 ± 0.38 / 18.78 ± 0.63</td> <!-- MLSum -->
   <td class="de know">18.12 ± 0.96 / 37.66 ± 1.06</td> <!-- MMLU-de -->
   <td class="de reason">9.92 ± 2.59 / 31.17 ± 1.75</td> <!-- HellaSwag-de -->
   <td class="nl ner">37.39 ± 3.37 / 32.77 ± 1.97</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.51 ± 1.57 / 19.22 ± 1.72</td> <!-- Dutch Social -->
   <td class="nl la">3.11 ± 0.88 / 50.54 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl qa">49.60 ± 1.28 / 61.06 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.63 ± 1.86 / 12.27 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.52 ± 1.25 / 35.34 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">6.60 ± 1.13 / 29.30 ± 0.97</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.76 ± 2.72 / 44.84 ± 2.71</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 0.85 / 65.96 ± 2.20</td> <!-- SST5 -->
   <td class="en la">5.76 ± 1.50 / 50.36 ± 2.34</td> <!-- ScaLA-en -->
   <td class="en qa">70.34 ± 1.81 / 81.54 ± 1.06</td> <!-- SQuAD -->
   <td class="en summ">65.88 ± 1.55 / 19.75 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">29.83 ± 1.09 / 47.45 ± 0.69</td> <!-- MMLU -->
   <td class="en reason">18.44 ± 2.21 / 36.96 ± 2.10</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.8</td> <!-- Danske Talemaader version -->
   <td>12.10.8</td> <!-- Danish Citizen Tests version -->
   <td>12.10.8</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- No Sammendrag version -->
   <td>12.10.5</td> <!-- ScaLA-nb version -->
   <td>12.10.5</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.8</td> <!-- MMLU-no version -->
   <td>12.10.8</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.8</td> <!-- SweDN version -->
   <td>12.10.8</td> <!-- MMLU-sv version -->
   <td>12.10.8</td> <!-- HellaSwag-sv version -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.8</td> <!-- MMLU-is version -->
   <td>12.10.8</td> <!-- Winogrande-is version -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.8</td> <!-- MMLU-de version -->
   <td>12.10.8</td> <!-- HellaSwag-de version -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.8</td> <!-- CNN-DailyMail version -->
   <td>12.10.8</td> <!-- MMLU version -->
   <td>12.10.8</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="da-rank">2.83</td> <!-- Danish rank -->
   <td class="no-rank">3.15</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.98</td> <!-- Swedish rank -->
   <td class="is-rank">4.36</td> <!-- Icelandic rank -->
   <td class="de-rank">3.51</td> <!-- German rank -->
   <td class="nl-rank">3.62</td> <!-- Dutch rank -->
   <td class="en-rank">3.19</td> <!-- English rank -->
   <td class="da ner">21.47 ± 3.87 / 16.98 ± 3.19</td> <!-- DANSK -->
   <td class="da sent">48.39 ± 0.66 / 64.51 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">12.46 ± 2.22 / 52.33 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da qa">52.51 ± 1.57 / 58.49 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.53 ± 1.15 / 21.82 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">36.65 ± 2.42 / 48.70 ± 2.50</td> <!-- Danske Talemaader -->
   <td class="da know">49.97 ± 2.70 / 65.62 ± 1.94</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.64 ± 1.49 / 28.33 ± 0.91</td> <!-- HellaSwag-da -->
   <td class="no ner">21.09 ± 6.44 / 20.45 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">26.31 ± 4.64 / 26.42 ± 2.98</td> <!-- NorNE-nn -->
   <td class="no sent">49.00 ± 3.88 / 65.98 ± 2.95</td> <!-- NoReC -->
   <td class="no summ">63.87 ± 1.60 / 17.88 ± 1.49</td> <!-- No Sammendrag -->
   <td class="no la">7.15 ± 2.14 / 40.83 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">7.98 ± 2.64 / 45.21 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no qa">47.70 ± 5.32 / 68.04 ± 5.37</td> <!-- NorQuAD -->
   <td class="no know">5.83 ± 1.04 / 27.83 ± 1.08</td> <!-- MMLU-no -->
   <td class="no reason">5.39 ± 1.69 / 27.82 ± 1.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.63 / 18.68 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">6.62 ± 0.88 / 27.61 ± 0.74</td> <!-- MMLU-sv -->
   <td class="sv reason">2.66 ± 1.04 / 26.32 ± 0.72</td> <!-- HellaSwag-sv -->
   <td class="is ner">21.40 ± 2.86 / 19.64 ± 2.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.99 ± 1.30 / 35.84 ± 1.02</td> <!-- ScaLA-is -->
   <td class="is qa">13.84 ± 2.99 / 36.90 ± 2.08</td> <!-- NQiI -->
   <td class="is summ">54.12 ± 2.64 / 11.76 ± 1.19</td> <!-- RRN -->
   <td class="is know">0.77 ± 0.87 / 24.46 ± 0.82</td> <!-- MMLU-is -->
   <td class="is reason">-0.68 ± 2.06 / 52.11 ± 2.31</td> <!-- Winogrande-is -->
   <td class="de ner">19.29 ± 5.77 / 20.20 ± 3.59</td> <!-- GermEval -->
   <td class="de sent">43.88 ± 3.42 / 61.04 ± 2.69</td> <!-- SB10k -->
   <td class="de la">5.63 ± 1.32 / 49.95 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de qa">17.02 ± 2.10 / 36.47 ± 2.53</td> <!-- GermanQuAD -->
   <td class="de summ">54.94 ± 1.06 / 14.92 ± 1.40</td> <!-- MLSum -->
   <td class="de know">5.89 ± 0.78 / 27.89 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">4.11 ± 0.97 / 27.05 ± 0.97</td> <!-- HellaSwag-de -->
   <td class="nl ner">24.15 ± 5.73 / 26.49 ± 4.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.31 ± 1.56 / 20.06 ± 1.06</td> <!-- Dutch Social -->
   <td class="nl la">1.60 ± 1.71 / 41.51 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.08 ± 1.76 / 49.32 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.43 ± 1.17 / 14.57 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.04 ± 1.28 / 26.56 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">3.70 ± 1.54 / 26.98 ± 1.26</td> <!-- HellaSwag-nl -->
   <td class="en ner">35.84 ± 5.12 / 35.76 ± 4.29</td> <!-- CoNLL-en -->
   <td class="en sent">56.87 ± 8.16 / 59.62 ± 5.61</td> <!-- SST5 -->
   <td class="en la">3.08 ± 2.98 / 40.66 ± 4.63</td> <!-- ScaLA-en -->
   <td class="en qa">52.77 ± 1.53 / 66.64 ± 1.58</td> <!-- SQuAD -->
   <td class="en summ">63.96 ± 1.61 / 19.20 ± 1.54</td> <!-- CNN-DailyMail -->
   <td class="en know">7.42 ± 1.60 / 28.95 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">2.24 ± 1.08 / 25.72 ± 0.82</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="da-rank">3.19</td> <!-- Danish rank -->
   <td class="no-rank">3.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.23</td> <!-- Swedish rank -->
   <td class="is-rank">4.25</td> <!-- Icelandic rank -->
   <td class="de-rank">3.30</td> <!-- German rank -->
   <td class="nl-rank">3.52</td> <!-- Dutch rank -->
   <td class="en-rank">2.91</td> <!-- English rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da qa">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">63.07 ± 1.07 / 16.98 ± 0.98</td> <!-- Nordjylland-News -->
   <td class="da know">15.04 ± 1.21 / 35.51 ± 0.80</td> <!-- Danske Talemaader -->
   <td class="da know">30.63 ± 3.36 / 50.02 ± 2.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.90 ± 0.95 / 28.18 ± 0.88</td> <!-- HellaSwag-da -->
   <td class="no ner">15.53 ± 5.69 / 15.49 ± 5.08</td> <!-- NorNE-nb -->
   <td class="no ner">19.78 ± 4.54 / 18.86 ± 4.22</td> <!-- NorNE-nn -->
   <td class="no sent">32.89 ± 1.65 / 42.58 ± 3.16</td> <!-- NoReC -->
   <td class="no summ">57.65 ± 2.16 / 10.13 ± 1.30</td> <!-- No Sammendrag -->
   <td class="no la">1.18 ± 1.00 / 33.34 ± 0.26</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td class="no know">11.27 ± 1.41 / 32.73 ± 1.25</td> <!-- MMLU-no -->
   <td class="no reason">5.10 ± 1.44 / 28.63 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.72 ± 1.46 / 15.26 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">10.98 ± 0.98 / 31.92 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">4.24 ± 0.47 / 27.53 ± 0.44</td> <!-- HellaSwag-sv -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="is summ">60.00 ± 2.62 / 13.07 ± 1.31</td> <!-- RRN -->
   <td class="is know">4.71 ± 1.02 / 26.81 ± 0.83</td> <!-- MMLU-is -->
   <td class="is reason">0.00 ± 2.53 / 56.42 ± 0.98</td> <!-- Winogrande-is -->
   <td class="de ner">16.95 ± 2.96 / 15.80 ± 2.16</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.96 / 22.24 ± 1.37</td> <!-- MLSum -->
   <td class="de know">12.11 ± 0.94 / 33.12 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">7.32 ± 1.40 / 30.11 ± 1.16</td> <!-- HellaSwag-de -->
   <td class="nl ner">16.90 ± 4.91 / 17.38 ± 4.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.61 ± 2.22 / 13.67 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.94 ± 0.50 / 31.87 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">3.29 ± 0.95 / 26.85 ± 0.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">19.65 ± 5.96 / 18.64 ± 5.49</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en qa">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
   <td class="en summ">66.51 ± 0.85 / 21.76 ± 0.84</td> <!-- CNN-DailyMail -->
   <td class="en know">20.38 ± 0.82 / 38.44 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">7.41 ± 1.01 / 29.08 ± 0.61</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="da-rank">3.13</td> <!-- Danish rank -->
   <td class="no-rank">3.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.12</td> <!-- Swedish rank -->
   <td class="is-rank">4.01</td> <!-- Icelandic rank -->
   <td class="de-rank">3.44</td> <!-- German rank -->
   <td class="nl-rank">3.76</td> <!-- Dutch rank -->
   <td class="en-rank">3.10</td> <!-- English rank -->
   <td class="da ner">28.60 ± 4.69 / 20.29 ± 3.37</td> <!-- DANSK -->
   <td class="da sent">48.71 ± 1.27 / 60.90 ± 2.95</td> <!-- Angry Tweets -->
   <td class="da la">2.30 ± 1.34 / 37.21 ± 2.50</td> <!-- ScaLA-da -->
   <td class="da qa">53.85 ± 1.73 / 58.96 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="da summ">64.05 ± 0.93 / 16.99 ± 1.44</td> <!-- Nordjylland-News -->
   <td class="da know">0.55 ± 0.59 / 24.15 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 2.29 / 35.66 ± 1.43</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.36 ± 1.09 / 25.24 ± 0.60</td> <!-- HellaSwag-da -->
   <td class="no ner">26.76 ± 6.99 / 23.69 ± 3.73</td> <!-- NorNE-nb -->
   <td class="no ner">35.38 ± 5.87 / 27.52 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">29.22 ± 2.89 / 39.25 ± 1.86</td> <!-- NoReC -->
   <td class="no summ">56.69 ± 2.08 / 8.56 ± 1.22</td> <!-- No Sammendrag -->
   <td class="no la">2.58 ± 2.68 / 36.11 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">2.79 ± 1.44 / 36.17 ± 1.51</td> <!-- ScaLA-nn -->
   <td class="no qa">34.41 ± 3.68 / 53.61 ± 4.28</td> <!-- NorQuAD -->
   <td class="no know">-0.56 ± 0.87 / 21.99 ± 0.62</td> <!-- MMLU-no -->
   <td class="no reason">-0.43 ± 1.02 / 24.54 ± 0.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.05 ± 1.20 / 13.94 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">1.32 ± 1.02 / 23.28 ± 0.65</td> <!-- MMLU-sv -->
   <td class="sv reason">0.35 ± 0.66 / 25.33 ± 0.66</td> <!-- HellaSwag-sv -->
   <td class="is ner">26.28 ± 5.09 / 22.73 ± 3.35</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.17 ± 1.98 / 48.03 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is qa">22.65 ± 3.50 / 45.48 ± 2.99</td> <!-- NQiI -->
   <td class="is summ">62.07 ± 1.73 / 11.04 ± 1.91</td> <!-- RRN -->
   <td class="is know">0.90 ± 1.25 / 23.69 ± 0.95</td> <!-- MMLU-is -->
   <td class="is reason">-2.92 ± 4.86 / 53.55 ± 3.32</td> <!-- Winogrande-is -->
   <td class="de ner">34.53 ± 1.24 / 29.89 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">42.90 ± 2.66 / 56.64 ± 4.71</td> <!-- SB10k -->
   <td class="de la">1.51 ± 1.64 / 43.36 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de qa">15.83 ± 1.42 / 29.77 ± 2.54</td> <!-- GermanQuAD -->
   <td class="de summ">61.40 ± 3.15 / 14.84 ± 2.07</td> <!-- MLSum -->
   <td class="de know">-1.84 ± 1.09 / 23.98 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">-0.12 ± 1.30 / 24.41 ± 0.96</td> <!-- HellaSwag-de -->
   <td class="nl ner">36.74 ± 3.36 / 32.36 ± 1.39</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 2.44 / 34.17 ± 2.59</td> <!-- Dutch Social -->
   <td class="nl la">3.01 ± 1.94 / 46.03 ± 4.19</td> <!-- ScaLA-nl -->
   <td class="nl qa">32.32 ± 1.55 / 40.73 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.76 ± 1.36 / 10.67 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.67 ± 1.15 / 24.89 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.30 ± 1.01 / 23.52 ± 0.38</td> <!-- HellaSwag-nl -->
   <td class="en ner">42.78 ± 4.24 / 40.64 ± 2.84</td> <!-- CoNLL-en -->
   <td class="en sent">59.90 ± 4.98 / 54.05 ± 2.70</td> <!-- SST5 -->
   <td class="en la">5.68 ± 1.91 / 50.82 ± 2.18</td> <!-- ScaLA-en -->
   <td class="en qa">58.52 ± 1.88 / 68.97 ± 1.86</td> <!-- SQuAD -->
   <td class="en summ">64.83 ± 0.95 / 18.37 ± 0.46</td> <!-- CNN-DailyMail -->
   <td class="en know">1.63 ± 0.89 / 23.51 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">0.54 ± 1.01 / 24.93 ± 0.46</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   <td>12.10.5</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.5</td> <!-- ScaLA-is version -->
   <td>12.10.5</td> <!-- NQiI version -->
   <td>12.10.5</td> <!-- RRN version -->
   <td>12.10.5</td> <!-- MMLU-is version -->
   <td>12.10.5</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.5</td> <!-- MMLU version -->
   <td>12.10.5</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="da-rank">3.01</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.03</td> <!-- Swedish rank -->
   <td class="is-rank">4.53</td> <!-- Icelandic rank -->
   <td class="de-rank">3.49</td> <!-- German rank -->
   <td class="nl-rank">3.95</td> <!-- Dutch rank -->
   <td class="en-rank">3.14</td> <!-- English rank -->
   <td class="da ner">16.72 ± 2.23 / 15.96 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">45.89 ± 2.13 / 63.12 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">11.25 ± 2.33 / 51.88 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da qa">53.17 ± 0.79 / 59.30 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="da summ">66.51 ± 1.29 / 22.13 ± 1.19</td> <!-- Nordjylland-News -->
   <td class="da know">14.84 ± 2.11 / 33.02 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">27.95 ± 3.54 / 48.55 ± 2.35</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.41 ± 1.06 / 26.59 ± 0.72</td> <!-- HellaSwag-da -->
   <td class="no ner">31.45 ± 1.64 / 31.64 ± 1.89</td> <!-- NorNE-nb -->
   <td class="no ner">33.85 ± 1.95 / 34.29 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">36.06 ± 3.96 / 52.59 ± 4.67</td> <!-- NoReC -->
   <td class="no summ">63.06 ± 2.34 / 17.34 ± 1.88</td> <!-- No Sammendrag -->
   <td class="no la">8.34 ± 2.97 / 45.11 ± 4.57</td> <!-- ScaLA-nb -->
   <td class="no la">6.84 ± 3.88 / 45.28 ± 5.45</td> <!-- ScaLA-nn -->
   <td class="no qa">48.31 ± 4.22 / 69.39 ± 4.10</td> <!-- NorQuAD -->
   <td class="no know">3.28 ± 1.19 / 25.97 ± 1.25</td> <!-- MMLU-no -->
   <td class="no reason">1.87 ± 1.03 / 26.44 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.60 ± 1.09 / 18.36 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">3.83 ± 1.03 / 26.46 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">4.40 ± 1.42 / 28.14 ± 1.05</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.35 ± 0.70 / 9.74 ± 0.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.14 ± 0.97 / 35.56 ± 2.43</td> <!-- ScaLA-is -->
   <td class="is qa">7.51 ± 3.09 / 30.04 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">51.60 ± 4.52 / 10.43 ± 2.18</td> <!-- RRN -->
   <td class="is know">1.52 ± 1.11 / 24.53 ± 0.83</td> <!-- MMLU-is -->
   <td class="is reason">0.47 ± 1.85 / 55.99 ± 1.13</td> <!-- Winogrande-is -->
   <td class="de ner">25.69 ± 1.43 / 25.95 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">33.48 ± 2.83 / 47.14 ± 4.43</td> <!-- SB10k -->
   <td class="de la">3.73 ± 1.14 / 44.43 ± 4.17</td> <!-- ScaLA-de -->
   <td class="de qa">14.82 ± 2.69 / 35.50 ± 3.15</td> <!-- GermanQuAD -->
   <td class="de summ">63.85 ± 2.30 / 21.16 ± 3.79</td> <!-- MLSum -->
   <td class="de know">2.96 ± 0.44 / 26.82 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">1.88 ± 0.93 / 26.35 ± 1.20</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.50 ± 2.27 / 24.09 ± 2.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.04 ± 1.51 / 18.08 ± 2.09</td> <!-- Dutch Social -->
   <td class="nl la">-0.61 ± 1.30 / 46.51 ± 2.55</td> <!-- ScaLA-nl -->
   <td class="nl qa">26.96 ± 1.55 / 35.73 ± 1.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">56.55 ± 3.05 / 13.22 ± 1.01</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.27 ± 1.29 / 24.94 ± 0.91</td> <!-- MMLU-nl -->
   <td class="nl reason">1.47 ± 0.79 / 25.75 ± 0.39</td> <!-- HellaSwag-nl -->
   <td class="en ner">38.51 ± 3.33 / 38.08 ± 2.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.60 ± 2.87 / 58.50 ± 1.25</td> <!-- SST5 -->
   <td class="en la">2.23 ± 1.32 / 34.15 ± 0.60</td> <!-- ScaLA-en -->
   <td class="en qa">45.44 ± 3.61 / 59.52 ± 2.98</td> <!-- SQuAD -->
   <td class="en summ">67.11 ± 0.90 / 21.77 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">5.02 ± 1.22 / 25.76 ± 1.01</td> <!-- MMLU -->
   <td class="en reason">2.08 ± 0.75 / 25.95 ± 0.35</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="da-rank">3.40</td> <!-- Danish rank -->
   <td class="no-rank">3.62</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.83</td> <!-- Swedish rank -->
   <td class="is-rank">4.32</td> <!-- Icelandic rank -->
   <td class="de-rank">3.30</td> <!-- German rank -->
   <td class="nl-rank">3.47</td> <!-- Dutch rank -->
   <td class="en-rank">2.97</td> <!-- English rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da qa">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
   <td class="da summ">62.41 ± 1.21 / 17.66 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">15.16 ± 1.35 / 31.61 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">12.67 ± 1.89 / 41.99 ± 1.17</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.67 ± 1.17 / 26.82 ± 0.69</td> <!-- HellaSwag-da -->
   <td class="no ner">39.78 ± 2.67 / 31.15 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">43.58 ± 2.49 / 36.60 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">22.01 ± 3.00 / 40.48 ± 2.81</td> <!-- NoReC -->
   <td class="no summ">55.43 ± 4.07 / 11.54 ± 0.87</td> <!-- No Sammendrag -->
   <td class="no la">2.76 ± 1.35 / 44.34 ± 3.05</td> <!-- ScaLA-nb -->
   <td class="no la">1.45 ± 1.35 / 39.55 ± 3.53</td> <!-- ScaLA-nn -->
   <td class="no qa">32.42 ± 1.72 / 56.65 ± 0.92</td> <!-- NorQuAD -->
   <td class="no know">7.68 ± 0.87 / 29.15 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">1.06 ± 1.38 / 25.48 ± 1.00</td> <!-- HellaSwag-no -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="sv summ">40.55 ± 6.41 / 11.10 ± 1.63</td> <!-- SweDN -->
   <td class="sv know">11.06 ± 0.98 / 31.69 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">1.03 ± 0.85 / 25.55 ± 0.60</td> <!-- HellaSwag-sv -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is qa">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 0.96 / 9.92 ± 1.05</td> <!-- RRN -->
   <td class="is know">2.42 ± 0.70 / 23.15 ± 0.70</td> <!-- MMLU-is -->
   <td class="is reason">0.62 ± 1.42 / 56.02 ± 0.95</td> <!-- Winogrande-is -->
   <td class="de ner">36.62 ± 1.56 / 28.22 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de qa">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td class="de summ">63.02 ± 2.00 / 19.54 ± 1.33</td> <!-- MLSum -->
   <td class="de know">12.27 ± 1.33 / 33.40 ± 1.08</td> <!-- MMLU-de -->
   <td class="de reason">6.57 ± 0.74 / 28.60 ± 0.70</td> <!-- HellaSwag-de -->
   <td class="nl ner">38.85 ± 3.77 / 32.18 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.99 ± 8.25 / 12.75 ± 2.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.97 ± 0.92 / 32.28 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">1.45 ± 1.15 / 24.79 ± 0.52</td> <!-- HellaSwag-nl -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en qa">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
   <td class="en summ">67.28 ± 0.27 / 22.84 ± 0.41</td> <!-- CNN-DailyMail -->
   <td class="en know">18.21 ± 0.70 / 37.61 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">10.84 ± 1.23 / 31.84 ± 1.00</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.4.0</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="da-rank">3.59</td> <!-- Danish rank -->
   <td class="no-rank">3.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.43</td> <!-- Swedish rank -->
   <td class="is-rank">4.41</td> <!-- Icelandic rank -->
   <td class="de-rank">3.34</td> <!-- German rank -->
   <td class="nl-rank">3.59</td> <!-- Dutch rank -->
   <td class="en-rank">2.75</td> <!-- English rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da qa">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">57.19 ± 1.18 / 11.87 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">22.17 ± 1.31 / 39.97 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">12.85 ± 3.11 / 42.13 ± 2.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">7.01 ± 0.62 / 30.16 ± 0.46</td> <!-- HellaSwag-da -->
   <td class="no ner">26.99 ± 3.92 / 24.61 ± 2.74</td> <!-- NorNE-nb -->
   <td class="no ner">25.74 ± 3.76 / 24.51 ± 2.96</td> <!-- NorNE-nn -->
   <td class="no sent">19.85 ± 1.97 / 35.75 ± 1.74</td> <!-- NoReC -->
   <td class="no summ">55.08 ± 0.83 / 8.11 ± 0.35</td> <!-- No Sammendrag -->
   <td class="no la">1.96 ± 1.33 / 44.22 ± 2.93</td> <!-- ScaLA-nb -->
   <td class="no la">-0.01 ± 1.39 / 39.57 ± 2.97</td> <!-- ScaLA-nn -->
   <td class="no qa">16.33 ± 2.17 / 31.16 ± 3.40</td> <!-- NorQuAD -->
   <td class="no know">7.79 ± 0.78 / 29.50 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">5.61 ± 1.32 / 28.45 ± 1.02</td> <!-- HellaSwag-no -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.19 ± 0.69 / 15.92 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">10.74 ± 0.92 / 32.65 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">4.83 ± 0.62 / 28.76 ± 0.55</td> <!-- HellaSwag-sv -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">57.27 ± 1.42 / 10.43 ± 0.97</td> <!-- RRN -->
   <td class="is know">3.87 ± 0.97 / 26.29 ± 0.94</td> <!-- MMLU-is -->
   <td class="is reason">1.92 ± 2.32 / 50.07 ± 2.68</td> <!-- Winogrande-is -->
   <td class="de ner">28.04 ± 2.71 / 24.08 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de qa">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td class="de summ">61.47 ± 1.67 / 12.62 ± 1.40</td> <!-- MLSum -->
   <td class="de know">13.44 ± 1.22 / 34.26 ± 0.98</td> <!-- MMLU-de -->
   <td class="de reason">8.31 ± 1.08 / 31.05 ± 0.84</td> <!-- HellaSwag-de -->
   <td class="nl ner">23.44 ± 5.09 / 25.00 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl qa">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.91 ± 0.99 / 12.65 ± 0.41</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">12.11 ± 0.90 / 33.62 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.41 ± 1.13 / 29.73 ± 0.82</td> <!-- HellaSwag-nl -->
   <td class="en ner">40.89 ± 2.63 / 37.44 ± 2.39</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en qa">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">67.23 ± 0.14 / 18.87 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">26.84 ± 0.41 / 44.86 ± 0.31</td> <!-- MMLU -->
   <td class="en reason">23.89 ± 1.20 / 42.78 ± 0.95</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.5.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da-rank">3.64</td> <!-- Danish rank -->
   <td class="no-rank">3.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.49</td> <!-- Swedish rank -->
   <td class="is-rank">4.46</td> <!-- Icelandic rank -->
   <td class="de-rank">3.51</td> <!-- German rank -->
   <td class="nl-rank">3.89</td> <!-- Dutch rank -->
   <td class="en-rank">2.62</td> <!-- English rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">56.43 ± 1.74 / 11.67 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">14.86 ± 1.85 / 33.52 ± 1.63</td> <!-- Danske Talemaader -->
   <td class="da know">17.56 ± 2.63 / 45.31 ± 1.78</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.78 ± 1.48 / 27.73 ± 1.32</td> <!-- HellaSwag-da -->
   <td class="no ner">12.10 ± 5.58 / 12.85 ± 4.80</td> <!-- NorNE-nb -->
   <td class="no ner">13.42 ± 6.02 / 13.82 ± 5.16</td> <!-- NorNE-nn -->
   <td class="no sent">22.82 ± 3.11 / 43.88 ± 3.10</td> <!-- NoReC -->
   <td class="no summ">54.48 ± 1.91 / 8.22 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">2.70 ± 2.16 / 47.68 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">2.21 ± 1.46 / 42.80 ± 4.36</td> <!-- ScaLA-nn -->
   <td class="no qa">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td class="no know">9.57 ± 1.11 / 30.18 ± 0.83</td> <!-- MMLU-no -->
   <td class="no reason">6.02 ± 0.84 / 28.58 ± 1.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.82 ± 1.62 / 14.43 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">11.54 ± 0.73 / 32.55 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">7.19 ± 1.40 / 29.76 ± 1.22</td> <!-- HellaSwag-sv -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is qa">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.79 ± 1.12 / 25.76 ± 0.91</td> <!-- MMLU-is -->
   <td class="is reason">1.13 ± 3.74 / 52.30 ± 2.26</td> <!-- Winogrande-is -->
   <td class="de ner">9.23 ± 4.86 / 10.43 ± 3.83</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de qa">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td class="de summ">61.74 ± 1.58 / 14.71 ± 1.12</td> <!-- MLSum -->
   <td class="de know">13.65 ± 1.17 / 33.35 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">8.86 ± 0.99 / 30.21 ± 0.77</td> <!-- HellaSwag-de -->
   <td class="nl ner">11.66 ± 6.46 / 15.15 ± 4.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl qa">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">55.00 ± 1.73 / 11.21 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.56 ± 0.64 / 34.17 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">5.89 ± 0.82 / 29.17 ± 0.66</td> <!-- HellaSwag-nl -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
   <td class="en summ">68.15 ± 0.13 / 22.11 ± 0.19</td> <!-- CNN-DailyMail -->
   <td class="en know">27.24 ± 1.14 / 44.95 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">22.84 ± 1.16 / 41.75 ± 0.99</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="da-rank">3.71</td> <!-- Danish rank -->
   <td class="no-rank">4.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.60</td> <!-- Swedish rank -->
   <td class="is-rank">4.82</td> <!-- Icelandic rank -->
   <td class="de-rank">3.84</td> <!-- German rank -->
   <td class="nl-rank">3.86</td> <!-- Dutch rank -->
   <td class="en-rank">3.37</td> <!-- English rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="da summ">50.86 ± 0.68 / 9.46 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">0.26 ± 1.33 / 23.32 ± 0.83</td> <!-- Danske Talemaader -->
   <td class="da know">6.94 ± 1.82 / 37.66 ± 1.18</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.11 ± 0.71 / 24.99 ± 0.40</td> <!-- HellaSwag-da -->
   <td class="no ner">34.42 ± 3.22 / 27.79 ± 2.40</td> <!-- NorNE-nb -->
   <td class="no ner">35.17 ± 4.05 / 30.70 ± 3.37</td> <!-- NorNE-nn -->
   <td class="no sent">21.46 ± 5.63 / 38.36 ± 6.18</td> <!-- NoReC -->
   <td class="no summ">45.34 ± 0.64 / 5.61 ± 0.21</td> <!-- No Sammendrag -->
   <td class="no la">0.34 ± 1.25 / 33.60 ± 0.50</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.58 / 34.69 ± 3.11</td> <!-- ScaLA-nn -->
   <td class="no qa">0.12 ± 0.04 / 9.85 ± 0.17</td> <!-- NorQuAD -->
   <td class="no know">2.61 ± 1.38 / 27.69 ± 0.74</td> <!-- MMLU-no -->
   <td class="no reason">0.96 ± 1.02 / 25.05 ± 0.84</td> <!-- HellaSwag-no -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.03 ± 0.33 / 4.86 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.83 ± 1.04 / 25.47 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.62 ± 0.73 / 24.51 ± 0.53</td> <!-- HellaSwag-sv -->
   <td class="is ner">8.84 ± 2.72 / 8.59 ± 2.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.38 ± 1.52 / 34.73 ± 1.40</td> <!-- ScaLA-is -->
   <td class="is qa">5.08 ± 1.06 / 18.85 ± 2.62</td> <!-- NQiI -->
   <td class="is summ">42.35 ± 0.38 / 6.36 ± 0.24</td> <!-- RRN -->
   <td class="is know">2.31 ± 1.36 / 25.90 ± 1.45</td> <!-- MMLU-is -->
   <td class="is reason">-1.79 ± 3.44 / 45.33 ± 2.32</td> <!-- Winogrande-is -->
   <td class="de ner">30.85 ± 4.69 / 24.38 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.81 / 64.87 ± 2.42</td> <!-- SB10k -->
   <td class="de la">2.67 ± 1.77 / 41.55 ± 4.54</td> <!-- ScaLA-de -->
   <td class="de qa">4.09 ± 1.94 / 12.70 ± 2.66</td> <!-- GermanQuAD -->
   <td class="de summ">42.64 ± 0.22 / 4.37 ± 0.10</td> <!-- MLSum -->
   <td class="de know">1.94 ± 0.76 / 26.86 ± 0.44</td> <!-- MMLU-de -->
   <td class="de reason">1.24 ± 0.75 / 25.78 ± 0.82</td> <!-- HellaSwag-de -->
   <td class="nl ner">37.37 ± 2.22 / 30.45 ± 2.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.55 ± 1.82 / 23.90 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">0.05 ± 1.35 / 35.78 ± 2.30</td> <!-- ScaLA-nl -->
   <td class="nl qa">34.81 ± 1.54 / 46.37 ± 1.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.22 ± 0.39 / 8.61 ± 0.17</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.92 ± 1.04 / 27.22 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">0.16 ± 0.55 / 25.29 ± 0.61</td> <!-- HellaSwag-nl -->
   <td class="en ner">38.23 ± 3.10 / 36.38 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">60.70 ± 1.80 / 66.82 ± 1.12</td> <!-- SST5 -->
   <td class="en la">-0.19 ± 2.28 / 38.77 ± 3.32</td> <!-- ScaLA-en -->
   <td class="en qa">61.93 ± 1.98 / 73.71 ± 1.57</td> <!-- SQuAD -->
   <td class="en summ">51.32 ± 0.91 / 11.96 ± 0.57</td> <!-- CNN-DailyMail -->
   <td class="en know">5.00 ± 1.53 / 27.59 ± 1.14</td> <!-- MMLU -->
   <td class="en reason">1.10 ± 1.02 / 25.71 ± 0.66</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- No Sammendrag version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- MMLU-no version -->
   <td>12.5.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="da-rank">3.97</td> <!-- Danish rank -->
   <td class="no-rank">4.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.85</td> <!-- Swedish rank -->
   <td class="is-rank">4.54</td> <!-- Icelandic rank -->
   <td class="de-rank">3.82</td> <!-- German rank -->
   <td class="nl-rank">3.92</td> <!-- Dutch rank -->
   <td class="en-rank">3.17</td> <!-- English rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="da summ">55.57 ± 1.04 / 8.04 ± 0.82</td> <!-- Nordjylland-News -->
   <td class="da know">7.21 ± 1.78 / 29.73 ± 1.08</td> <!-- Danske Talemaader -->
   <td class="da know">16.56 ± 3.13 / 42.30 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.62 ± 1.30 / 25.65 ± 0.72</td> <!-- HellaSwag-da -->
   <td class="no ner">34.46 ± 2.01 / 33.09 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">33.41 ± 2.21 / 33.91 ± 2.33</td> <!-- NorNE-nn -->
   <td class="no sent">6.31 ± 3.46 / 20.67 ± 2.69</td> <!-- NoReC -->
   <td class="no summ">49.88 ± 3.11 / 5.75 ± 0.88</td> <!-- No Sammendrag -->
   <td class="no la">-1.59 ± 1.08 / 36.27 ± 3.71</td> <!-- ScaLA-nb -->
   <td class="no la">0.61 ± 1.41 / 38.84 ± 5.10</td> <!-- ScaLA-nn -->
   <td class="no qa">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td class="no know">2.81 ± 1.18 / 25.21 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">2.92 ± 0.88 / 26.67 ± 0.60</td> <!-- HellaSwag-no -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.36 ± 1.44 / 12.82 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">6.52 ± 1.02 / 28.83 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">1.91 ± 1.30 / 26.10 ± 0.65</td> <!-- HellaSwag-sv -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">2.71 ± 0.84 / 24.35 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">0.85 ± 1.91 / 52.12 ± 2.92</td> <!-- Winogrande-is -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de qa">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td class="de summ">59.71 ± 2.14 / 12.23 ± 1.08</td> <!-- MLSum -->
   <td class="de know">6.34 ± 1.10 / 29.19 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">2.94 ± 0.65 / 27.16 ± 0.61</td> <!-- HellaSwag-de -->
   <td class="nl ner">28.30 ± 3.90 / 28.67 ± 3.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.40 ± 2.03 / 10.34 ± 0.54</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.44 ± 0.51 / 29.86 ± 0.35</td> <!-- MMLU-nl -->
   <td class="nl reason">1.70 ± 1.42 / 26.04 ± 0.91</td> <!-- HellaSwag-nl -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en qa">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
   <td class="en summ">65.22 ± 0.29 / 19.22 ± 0.18</td> <!-- CNN-DailyMail -->
   <td class="en know">18.24 ± 1.14 / 37.15 ± 0.82</td> <!-- MMLU -->
   <td class="en reason">10.89 ± 1.01 / 32.65 ± 0.85</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="da-rank">4.18</td> <!-- Danish rank -->
   <td class="no-rank">4.00</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.77</td> <!-- Swedish rank -->
   <td class="is-rank">4.70</td> <!-- Icelandic rank -->
   <td class="de-rank">3.46</td> <!-- German rank -->
   <td class="nl-rank">3.42</td> <!-- Dutch rank -->
   <td class="en-rank">3.97</td> <!-- English rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
   <td class="da summ">56.92 ± 0.98 / 8.57 ± 0.76</td> <!-- Nordjylland-News -->
   <td class="da know">0.10 ± 1.50 / 26.50 ± 1.00</td> <!-- Danske Talemaader -->
   <td class="da know">4.29 ± 5.87 / 35.00 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 1.17 / 24.43 ± 0.74</td> <!-- HellaSwag-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no summ">53.49 ± 5.64 / 9.38 ± 1.34</td> <!-- No Sammendrag -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.86 ± 1.65 / 50.11 ± 1.80</td> <!-- NorQuAD -->
   <td class="no know">0.21 ± 0.83 / 26.88 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">-0.30 ± 1.13 / 24.48 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.44 ± 0.79 / 12.95 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">1.12 ± 0.42 / 25.27 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.91 ± 0.96 / 24.26 ± 0.64</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.35 ± 3.52</td> <!-- NQiI -->
   <td class="is summ">55.16 ± 1.26 / 10.52 ± 1.13</td> <!-- RRN -->
   <td class="is know">0.74 ± 0.76 / 25.88 ± 1.33</td> <!-- MMLU-is -->
   <td class="is reason">-0.16 ± 0.86 / 32.02 ± 2.77</td> <!-- Winogrande-is -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 5.06 / 49.68 ± 5.74</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.44 ± 3.29 / 45.50 ± 3.33</td> <!-- GermanQuAD -->
   <td class="de summ">60.50 ± 0.63 / 13.71 ± 0.75</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.49 ± 1.37 / 47.34 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.24 ± 0.86 / 15.62 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.41 ± 1.15 / 27.75 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">0.15 ± 0.98 / 25.59 ± 0.57</td> <!-- HellaSwag-nl -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.51 ± 2.07 / 50.66 ± 1.90</td> <!-- SQuAD -->
   <td class="en summ">60.11 ± 1.39 / 16.29 ± 0.69</td> <!-- CNN-DailyMail -->
   <td class="en know">3.71 ± 0.75 / 28.35 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">0.62 ± 0.99 / 24.68 ± 0.55</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>9.3.1</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.4.0</td> <!-- RRN version -->
   <td>9.3.1</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="da-rank">3.93</td> <!-- Danish rank -->
   <td class="no-rank">4.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.91</td> <!-- Swedish rank -->
   <td class="is-rank">4.50</td> <!-- Icelandic rank -->
   <td class="de-rank">3.77</td> <!-- German rank -->
   <td class="nl-rank">3.75</td> <!-- Dutch rank -->
   <td class="en-rank">3.14</td> <!-- English rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da qa">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">55.87 ± 5.22 / 11.87 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">4.56 ± 1.88 / 25.87 ± 1.72</td> <!-- Danske Talemaader -->
   <td class="da know">22.41 ± 3.16 / 42.73 ± 0.96</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.71 ± 0.99 / 25.84 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">29.52 ± 1.48 / 29.79 ± 1.62</td> <!-- NorNE-nb -->
   <td class="no ner">31.27 ± 1.30 / 31.91 ± 1.31</td> <!-- NorNE-nn -->
   <td class="no sent">11.49 ± 1.38 / 27.12 ± 1.98</td> <!-- NoReC -->
   <td class="no summ">9.92 ± 8.37 / 1.42 ± 1.14</td> <!-- No Sammendrag -->
   <td class="no la">0.29 ± 1.58 / 40.21 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">-0.12 ± 1.48 / 39.92 ± 3.90</td> <!-- ScaLA-nn -->
   <td class="no qa">7.80 ± 1.19 / 17.09 ± 2.72</td> <!-- NorQuAD -->
   <td class="no know">0.29 ± 1.08 / 24.63 ± 0.79</td> <!-- MMLU-no -->
   <td class="no reason">0.49 ± 1.19 / 24.95 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv qa">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.29 ± 6.52 / 13.04 ± 1.68</td> <!-- SweDN -->
   <td class="sv know">2.59 ± 0.72 / 26.87 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.84 ± 1.01 / 24.44 ± 0.61</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.50 ± 3.17 / 9.41 ± 3.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is qa">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="is summ">58.92 ± 1.57 / 10.09 ± 1.41</td> <!-- RRN -->
   <td class="is know">2.82 ± 0.73 / 26.56 ± 0.56</td> <!-- MMLU-is -->
   <td class="is reason">1.48 ± 3.56 / 53.95 ± 2.45</td> <!-- Winogrande-is -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de qa">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">56.42 ± 7.64 / 11.68 ± 1.75</td> <!-- MLSum -->
   <td class="de know">2.75 ± 0.91 / 27.17 ± 0.72</td> <!-- MMLU-de -->
   <td class="de reason">3.41 ± 1.30 / 27.45 ± 0.79</td> <!-- HellaSwag-de -->
   <td class="nl ner">18.66 ± 4.43 / 17.56 ± 4.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl qa">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.36 ± 0.81 / 11.72 ± 0.73</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.09 ± 1.13 / 25.90 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">1.44 ± 1.12 / 26.50 ± 0.68</td> <!-- HellaSwag-nl -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en qa">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
   <td class="en summ">65.81 ± 1.90 / 20.88 ± 0.66</td> <!-- CNN-DailyMail -->
   <td class="en know">11.66 ± 1.13 / 32.84 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">5.22 ± 1.17 / 27.95 ± 1.10</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.5.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.5.0</td> <!-- NQiI version -->
   <td>12.5.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.09</td> <!-- ScandEval rank -->
   <td class="da-rank">3.91</td> <!-- Danish rank -->
   <td class="no-rank">4.28</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.73</td> <!-- Swedish rank -->
   <td class="is-rank">4.83</td> <!-- Icelandic rank -->
   <td class="de-rank">4.11</td> <!-- German rank -->
   <td class="nl-rank">4.16</td> <!-- Dutch rank -->
   <td class="en-rank">3.59</td> <!-- English rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da qa">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="da summ">53.01 ± 1.10 / 10.72 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">2.17 ± 1.53 / 23.73 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">0.22 ± 2.74 / 35.08 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.65 ± 1.58 / 24.75 ± 1.03</td> <!-- HellaSwag-da -->
   <td class="no ner">9.06 ± 6.86 / 8.39 ± 6.41</td> <!-- NorNE-nb -->
   <td class="no ner">17.16 ± 6.21 / 16.00 ± 5.94</td> <!-- NorNE-nn -->
   <td class="no sent">25.52 ± 3.72 / 41.44 ± 4.44</td> <!-- NoReC -->
   <td class="no summ">40.94 ± 0.78 / 5.09 ± 0.25</td> <!-- No Sammendrag -->
   <td class="no la">0.68 ± 1.54 / 45.09 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">0.17 ± 2.27 / 42.02 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.46 ± 0.07 / 6.96 ± 0.13</td> <!-- NorQuAD -->
   <td class="no know">2.43 ± 1.10 / 24.94 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">2.35 ± 0.86 / 26.35 ± 0.78</td> <!-- HellaSwag-no -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">39.53 ± 0.34 / 5.71 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">0.69 ± 0.90 / 24.20 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">0.12 ± 1.51 / 24.97 ± 1.28</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.04 ± 5.36 / 9.25 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.08 ± 1.02 / 34.02 ± 0.68</td> <!-- ScaLA-is -->
   <td class="is qa">8.86 ± 2.70 / 27.28 ± 1.45</td> <!-- NQiI -->
   <td class="is summ">40.35 ± 0.29 / 6.83 ± 0.14</td> <!-- RRN -->
   <td class="is know">1.17 ± 1.14 / 23.52 ± 1.31</td> <!-- MMLU-is -->
   <td class="is reason">-3.46 ± 3.64 / 47.67 ± 2.88</td> <!-- Winogrande-is -->
   <td class="de ner">14.06 ± 5.31 / 12.90 ± 4.52</td> <!-- GermEval -->
   <td class="de sent">28.07 ± 6.33 / 38.61 ± 7.42</td> <!-- SB10k -->
   <td class="de la">2.31 ± 1.88 / 44.45 ± 4.23</td> <!-- ScaLA-de -->
   <td class="de qa">6.89 ± 2.35 / 17.95 ± 3.37</td> <!-- GermanQuAD -->
   <td class="de summ">43.42 ± 0.26 / 5.42 ± 0.11</td> <!-- MLSum -->
   <td class="de know">1.66 ± 1.18 / 25.51 ± 0.86</td> <!-- MMLU-de -->
   <td class="de reason">1.50 ± 0.90 / 26.46 ± 0.95</td> <!-- HellaSwag-de -->
   <td class="nl ner">18.70 ± 5.76 / 19.58 ± 4.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.70 ± 1.69 / 17.91 ± 1.48</td> <!-- Dutch Social -->
   <td class="nl la">2.19 ± 2.08 / 45.43 ± 3.44</td> <!-- ScaLA-nl -->
   <td class="nl qa">38.08 ± 1.07 / 48.44 ± 1.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.79 ± 0.51 / 7.59 ± 0.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.65 ± 1.39 / 25.05 ± 1.02</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.02 ± 0.92 / 24.75 ± 0.66</td> <!-- HellaSwag-nl -->
   <td class="en ner">25.36 ± 8.05 / 24.05 ± 7.34</td> <!-- CoNLL-en -->
   <td class="en sent">56.91 ± 2.41 / 66.15 ± 1.54</td> <!-- SST5 -->
   <td class="en la">7.10 ± 2.89 / 49.36 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.60 ± 5.37 / 70.37 ± 4.71</td> <!-- SQuAD -->
   <td class="en summ">46.16 ± 1.28 / 11.33 ± 0.70</td> <!-- CNN-DailyMail -->
   <td class="en know">0.71 ± 0.85 / 24.97 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">0.82 ± 1.01 / 25.62 ± 0.74</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.5.2</td> <!-- NoReC version -->
   <td>12.5.2</td> <!-- No Sammendrag version -->
   <td>12.5.2</td> <!-- ScaLA-nb version -->
   <td>12.5.2</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>12.5.2</td> <!-- MMLU-no version -->
   <td>12.5.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.5.2</td> <!-- ScaLA-is version -->
   <td>12.5.2</td> <!-- NQiI version -->
   <td>12.5.2</td> <!-- RRN version -->
   <td>12.5.2</td> <!-- MMLU-is version -->
   <td>12.5.2</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="da-rank">4.27</td> <!-- Danish rank -->
   <td class="no-rank">4.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.18</td> <!-- Swedish rank -->
   <td class="is-rank">5.00</td> <!-- Icelandic rank -->
   <td class="de-rank">4.35</td> <!-- German rank -->
   <td class="nl-rank">4.38</td> <!-- Dutch rank -->
   <td class="en-rank">3.76</td> <!-- English rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da qa">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td class="da summ">48.87 ± 1.42 / 5.39 ± 0.62</td> <!-- Nordjylland-News -->
   <td class="da know">-0.33 ± 0.61 / 23.91 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">0.05 ± 2.96 / 34.67 ± 1.78</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.08 ± 0.81 / 25.21 ± 0.56</td> <!-- HellaSwag-da -->
   <td class="no ner">30.79 ± 1.95 / 32.18 ± 1.98</td> <!-- NorNE-nb -->
   <td class="no ner">31.12 ± 2.36 / 33.10 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">9.95 ± 3.92 / 29.01 ± 2.80</td> <!-- NoReC -->
   <td class="no summ">40.45 ± 0.43 / 4.00 ± 0.12</td> <!-- No Sammendrag -->
   <td class="no la">-0.95 ± 1.87 / 39.37 ± 3.33</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 1.73 / 42.36 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">0.32 ± 1.03 / 24.22 ± 1.37</td> <!-- MMLU-no -->
   <td class="no reason">0.12 ± 0.91 / 24.92 ± 0.59</td> <!-- HellaSwag-no -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">43.75 ± 0.28 / 4.67 ± 0.12</td> <!-- SweDN -->
   <td class="sv know">-0.22 ± 0.80 / 23.76 ± 0.84</td> <!-- MMLU-sv -->
   <td class="sv reason">0.75 ± 1.00 / 25.27 ± 0.56</td> <!-- HellaSwag-sv -->
   <td class="is ner">13.60 ± 2.38 / 14.36 ± 2.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.04 ± 0.90 / 34.46 ± 1.41</td> <!-- ScaLA-is -->
   <td class="is qa">1.51 ± 0.68 / 13.16 ± 3.12</td> <!-- NQiI -->
   <td class="is summ">37.41 ± 0.29 / 5.10 ± 0.15</td> <!-- RRN -->
   <td class="is know">-0.09 ± 0.72 / 22.80 ± 0.92</td> <!-- MMLU-is -->
   <td class="is reason">-1.03 ± 1.32 / 56.25 ± 0.87</td> <!-- Winogrande-is -->
   <td class="de ner">21.46 ± 2.04 / 20.83 ± 1.63</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de qa">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td class="de summ">39.77 ± 0.20 / 4.80 ± 0.05</td> <!-- MLSum -->
   <td class="de know">-0.08 ± 0.53 / 25.19 ± 1.04</td> <!-- MMLU-de -->
   <td class="de reason">-0.63 ± 0.73 / 24.55 ± 0.49</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.58 ± 5.05 / 26.82 ± 3.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.92 ± 2.71 / 19.51 ± 4.22</td> <!-- Dutch Social -->
   <td class="nl la">-1.27 ± 1.85 / 41.38 ± 3.59</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.64 ± 1.96 / 11.74 ± 1.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.43 ± 0.37 / 7.83 ± 0.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.56 ± 1.27 / 24.38 ± 0.98</td> <!-- MMLU-nl -->
   <td class="nl reason">0.29 ± 1.06 / 25.10 ± 0.83</td> <!-- HellaSwag-nl -->
   <td class="en ner">26.47 ± 6.25 / 28.27 ± 5.35</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en qa">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
   <td class="en summ">46.18 ± 1.20 / 10.06 ± 0.67</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.87 ± 0.99 / 23.08 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">0.20 ± 1.12 / 24.94 ± 0.86</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.1.0</td> <!-- NoReC version -->
   <td>12.1.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.1.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   <td>12.5.2</td> <!-- MIM-GOLD-NER version -->
   <td>12.1.0</td> <!-- ScaLA-is version -->
   <td>12.1.0</td> <!-- NQiI version -->
   <td>12.1.0</td> <!-- RRN version -->
   <td>12.1.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da-rank">4.34</td> <!-- Danish rank -->
   <td class="no-rank">4.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.38</td> <!-- Swedish rank -->
   <td class="is-rank">5.02</td> <!-- Icelandic rank -->
   <td class="de-rank">4.66</td> <!-- German rank -->
   <td class="nl-rank">4.77</td> <!-- Dutch rank -->
   <td class="en-rank">4.88</td> <!-- English rank -->
   <td class="da ner">12.82 ± 2.64 / 12.37 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">3.55 ± 3.64 / 22.75 ± 4.02</td> <!-- Angry Tweets -->
   <td class="da la">0.68 ± 1.41 / 35.13 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da qa">19.85 ± 1.75 / 24.31 ± 1.88</td> <!-- ScandiQA-da -->
   <td class="da summ">55.58 ± 0.58 / 10.39 ± 0.63</td> <!-- Nordjylland-News -->
   <td class="da know">-0.11 ± 1.59 / 25.69 ± 0.65</td> <!-- Danske Talemaader -->
   <td class="da know">-2.13 ± 4.41 / 33.89 ± 3.03</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.88 ± 0.62 / 25.49 ± 0.74</td> <!-- HellaSwag-da -->
   <td class="no ner">12.77 ± 3.48 / 14.13 ± 3.09</td> <!-- NorNE-nb -->
   <td class="no ner">10.51 ± 3.44 / 9.95 ± 3.51</td> <!-- NorNE-nn -->
   <td class="no sent">8.70 ± 4.43 / 25.39 ± 3.30</td> <!-- NoReC -->
   <td class="no summ">49.76 ± 2.04 / 6.51 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 1.60 / 38.54 ± 3.41</td> <!-- ScaLA-nb -->
   <td class="no la">0.82 ± 1.39 / 37.77 ± 4.45</td> <!-- ScaLA-nn -->
   <td class="no qa">1.85 ± 0.82 / 10.19 ± 1.99</td> <!-- NorQuAD -->
   <td class="no know">-2.42 ± 1.29 / 21.73 ± 0.58</td> <!-- MMLU-no -->
   <td class="no reason">1.23 ± 1.22 / 25.06 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv qa">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">48.74 ± 1.72 / 10.30 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">-0.62 ± 1.15 / 22.04 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">0.99 ± 1.35 / 25.36 ± 0.92</td> <!-- HellaSwag-sv -->
   <td class="is ner">3.69 ± 1.28 / 3.66 ± 1.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.24 ± 1.37 / 42.67 ± 4.99</td> <!-- ScaLA-is -->
   <td class="is qa">0.29 ± 0.19 / 5.14 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">40.18 ± 1.07 / 4.07 ± 0.27</td> <!-- RRN -->
   <td class="is know">-0.42 ± 1.47 / 21.76 ± 0.69</td> <!-- MMLU-is -->
   <td class="is reason">-3.06 ± 3.24 / 55.32 ± 1.69</td> <!-- Winogrande-is -->
   <td class="de ner">5.80 ± 1.56 / 5.41 ± 1.56</td> <!-- GermEval -->
   <td class="de sent">4.45 ± 1.73 / 29.26 ± 3.66</td> <!-- SB10k -->
   <td class="de la">-0.48 ± 1.33 / 43.09 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de qa">0.08 ± 0.12 / 4.02 ± 1.17</td> <!-- GermanQuAD -->
   <td class="de summ">35.92 ± 0.71 / 3.53 ± 0.24</td> <!-- MLSum -->
   <td class="de know">0.77 ± 0.60 / 23.33 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">-0.34 ± 1.16 / 24.39 ± 0.86</td> <!-- HellaSwag-de -->
   <td class="nl ner">3.80 ± 1.23 / 4.24 ± 1.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.97 ± 1.50 / 13.00 ± 2.52</td> <!-- Dutch Social -->
   <td class="nl la">-0.37 ± 0.55 / 33.40 ± 0.35</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.40 ± 0.25 / 2.98 ± 0.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.25 ± 4.22 / 6.15 ± 1.03</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.98 ± 0.91 / 24.82 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.05 ± 1.07 / 24.51 ± 0.88</td> <!-- HellaSwag-nl -->
   <td class="en ner">12.34 ± 2.70 / 12.41 ± 2.54</td> <!-- CoNLL-en -->
   <td class="en sent">-1.48 ± 3.09 / 21.17 ± 2.22</td> <!-- SST5 -->
   <td class="en la">-0.48 ± 1.52 / 42.45 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en qa">0.72 ± 0.25 / 6.31 ± 0.51</td> <!-- SQuAD -->
   <td class="en summ">49.61 ± 1.17 / 9.59 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.12 ± 0.65 / 22.69 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">-0.01 ± 0.01 / 24.59 ± 0.43</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   <td>12.10.4</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.10.4</td> <!-- NQiI version -->
   <td>12.10.4</td> <!-- RRN version -->
   <td>12.10.4</td> <!-- MMLU-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.07</td> <!-- ScandEval rank -->
   <td class="da-rank">5.15</td> <!-- Danish rank -->
   <td class="no-rank">4.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.01</td> <!-- Swedish rank -->
   <td class="is-rank">5.44</td> <!-- Icelandic rank -->
   <td class="de-rank">4.87</td> <!-- German rank -->
   <td class="nl-rank">5.05</td> <!-- Dutch rank -->
   <td class="en-rank">5.16</td> <!-- English rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da qa">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="da summ">35.64 ± 4.11 / 4.70 ± 2.01</td> <!-- Nordjylland-News -->
   <td class="da know">-0.61 ± 0.54 / 24.71 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">6.94 ± 3.67 / 38.18 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.12 ± 0.87 / 24.71 ± 0.88</td> <!-- HellaSwag-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no summ">31.66 ± 0.51 / 0.93 ± 0.29</td> <!-- No Sammendrag -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.74 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">0.72 ± 0.81 / 22.86 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">-0.20 ± 1.06 / 24.94 ± 0.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">31.89 ± 0.27 / 2.03 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">-0.37 ± 1.08 / 22.43 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">0.36 ± 0.83 / 25.08 ± 0.77</td> <!-- HellaSwag-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">0.69 ± 0.98 / 23.34 ± 0.72</td> <!-- MMLU-is -->
   <td class="is reason">0.47 ± 4.14 / 46.93 ± 3.13</td> <!-- Winogrande-is -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.19 ± 1.24 / 17.20 ± 1.22</td> <!-- SB10k -->
   <td class="de la">-0.12 ± 0.91 / 36.65 ± 3.92</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.29 ± 0.49</td> <!-- GermanQuAD -->
   <td class="de summ">29.43 ± 1.80 / 2.35 ± 0.59</td> <!-- MLSum -->
   <td class="de know">-0.69 ± 0.79 / 22.79 ± 0.51</td> <!-- MMLU-de -->
   <td class="de reason">0.15 ± 0.35 / 24.25 ± 0.59</td> <!-- HellaSwag-de -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">30.20 ± 0.68 / 2.14 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.45 ± 0.84 / 24.91 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.56 ± 0.80 / 23.53 ± 0.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en qa">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
   <td class="en summ">34.62 ± 0.17 / 2.18 ± 0.04</td> <!-- CNN-DailyMail -->
   <td class="en know">0.37 ± 0.93 / 24.18 ± 0.90</td> <!-- MMLU -->
   <td class="en reason">-0.17 ± 0.50 / 24.82 ± 0.41</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.0.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   <td>9.3.1</td> <!-- MIM-GOLD-NER version -->
   <td>11.0.0</td> <!-- ScaLA-is version -->
   <td>12.5.1</td> <!-- NQiI version -->
   <td>12.0.0</td> <!-- RRN version -->
   <td>11.0.0</td> <!-- MMLU-is version -->
   <td>12.1.0</td> <!-- Winogrande-is version -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>11.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>12.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>11.0.0</td> <!-- MMLU-nl version -->
   <td>11.0.0</td> <!-- HellaSwag-nl version -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>11.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>11.0.0</td> <!-- MMLU version -->
   <td>11.0.0</td> <!-- HellaSwag version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/germanic-nlg.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Germanic NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-21Nfi&quot; src=&quot;https://datawrapper.dwcdn.net/21Nfi/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
