---
layout: leaderboard
title: Germanic NLG 🇪🇺
---

<center>Last updated: 04/11/2024 17:10:26 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="germanic-nlg-test" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian reading comprehension - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish reading comprehension - Exact Match / F1-score">ScandiQA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish summarization - BERTScore / ROUGE-L">SweDN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic reading comprehension - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">ARC-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">Winogrande-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German reading comprehension - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German summarization - BERTScore / ROUGE-L">MLSum</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch reading comprehension - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch summarization - BERTScore / ROUGE-L">Wiki-Lingua-NL</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English reading comprehension - Exact Match / F1-score">SQuAD</span></th>
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ARC-is">ARC-is version</span></th>
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
   <td class="rank">1.22</td> <!-- ScandEval rank -->
   <td class="da-rank">1.17</td> <!-- Danish rank -->
   <td class="no-rank">1.13</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.11</td> <!-- Swedish rank -->
   <td class="is-rank">1.49</td> <!-- Icelandic rank -->
   <td class="de-rank">1.18</td> <!-- German rank -->
   <td class="nl-rank">1.22</td> <!-- Dutch rank -->
   <td class="en-rank">1.22</td> <!-- English rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">56.43 ± 2.98 / 68.46 ± 1.64</td> <!-- ScandiQA-da -->
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
   <td class="no rc">47.50 ± 2.86 / 75.24 ± 1.32</td> <!-- NorQuAD -->
   <td class="no know">68.77 ± 2.09 / 76.56 ± 1.57</td> <!-- MMLU-no -->
   <td class="no reason">88.30 ± 1.32 / 91.13 ± 0.98</td> <!-- HellaSwag-no -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.83 ± 0.15 / 22.67 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">72.53 ± 1.82 / 79.26 ± 1.44</td> <!-- MMLU-sv -->
   <td class="sv reason">85.67 ± 2.59 / 89.14 ± 2.05</td> <!-- HellaSwag-sv -->
   <td class="is ner">78.67 ± 2.16 / 59.54 ± 4.85</td> <!-- MIM-GOLD-NER -->
   <td class="is la">33.65 ± 3.19 / 60.56 ± 2.35</td> <!-- ScaLA-is -->
   <td class="is rc">32.25 ± 2.01 / 60.12 ± 1.31</td> <!-- NQiI -->
   <td class="is summ">69.21 ± 0.25 / 22.50 ± 0.53</td> <!-- RRN -->
   <td class="is know">86.32 ± 1.50 / 89.65 ± 1.16</td> <!-- ARC-is -->
   <td class="is reason">74.02 ± 4.17 / 86.80 ± 2.02</td> <!-- Winogrande-is -->
   <td class="de ner">69.48 ± 2.32 / 54.66 ± 2.17</td> <!-- GermEval -->
   <td class="de sent">64.91 ± 1.86 / 75.96 ± 1.59</td> <!-- SB10k -->
   <td class="de la">50.23 ± 4.16 / 74.54 ± 2.10</td> <!-- ScaLA-de -->
   <td class="de rc">33.17 ± 1.86 / 65.14 ± 1.53</td> <!-- GermanQuAD -->
   <td class="de summ">66.35 ± 0.59 / 19.81 ± 1.46</td> <!-- MLSum -->
   <td class="de know">71.92 ± 2.22 / 78.79 ± 1.65</td> <!-- MMLU-de -->
   <td class="de reason">82.85 ± 1.48 / 86.99 ± 1.12</td> <!-- HellaSwag-de -->
   <td class="nl ner">73.35 ± 2.61 / 56.00 ± 2.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.92 ± 2.78 / 40.80 ± 2.43</td> <!-- Dutch Social -->
   <td class="nl la">76.70 ± 2.39 / 88.16 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.03 ± 1.96 / 76.47 ± 1.22</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.97 ± 0.41 / 22.66 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.71 ± 2.96 / 78.12 ± 2.24</td> <!-- MMLU-nl -->
   <td class="nl reason">90.07 ± 1.29 / 92.54 ± 0.98</td> <!-- HellaSwag-nl -->
   <td class="en ner">78.06 ± 2.73 / 70.76 ± 3.80</td> <!-- CoNLL-en -->
   <td class="en sent">69.06 ± 2.20 / 76.04 ± 1.60</td> <!-- SST5 -->
   <td class="en la">55.76 ± 3.84 / 76.34 ± 1.44</td> <!-- ScaLA-en -->
   <td class="en rc">67.35 ± 1.98 / 85.76 ± 0.77</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.27</td> <!-- ScandEval rank -->
   <td class="da-rank">1.19</td> <!-- Danish rank -->
   <td class="no-rank">1.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.19</td> <!-- Swedish rank -->
   <td class="is-rank">1.16</td> <!-- Icelandic rank -->
   <td class="de-rank">1.33</td> <!-- German rank -->
   <td class="nl-rank">1.52</td> <!-- Dutch rank -->
   <td class="en-rank">1.22</td> <!-- English rank -->
   <td class="da ner">66.80 ± 3.01 / 45.69 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">61.62 ± 2.17 / 73.99 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">66.84 ± 3.27 / 82.79 ± 1.86</td> <!-- ScaLA-da -->
   <td class="da rc">56.85 ± 2.62 / 68.83 ± 1.50</td> <!-- ScandiQA-da -->
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
   <td class="no rc">44.67 ± 3.23 / 73.39 ± 1.83</td> <!-- NorQuAD -->
   <td class="no know">70.84 ± 1.92 / 78.12 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">86.30 ± 2.04 / 89.53 ± 1.60</td> <!-- HellaSwag-no -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.08 ± 0.14 / 17.19 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">71.32 ± 1.56 / 78.48 ± 1.15</td> <!-- MMLU-sv -->
   <td class="sv reason">84.09 ± 2.99 / 88.01 ± 2.26</td> <!-- HellaSwag-sv -->
   <td class="is ner">86.37 ± 1.19 / 82.25 ± 2.73</td> <!-- MIM-GOLD-NER -->
   <td class="is la">43.03 ± 5.07 / 71.18 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">37.26 ± 2.60 / 66.04 ± 1.95</td> <!-- NQiI -->
   <td class="is summ">69.61 ± 0.61 / 23.98 ± 1.17</td> <!-- RRN -->
   <td class="is know">89.09 ± 1.59 / 91.76 ± 1.19</td> <!-- ARC-is -->
   <td class="is reason">72.03 ± 3.91 / 86.09 ± 1.96</td> <!-- Winogrande-is -->
   <td class="de ner">68.94 ± 2.50 / 44.89 ± 2.85</td> <!-- GermEval -->
   <td class="de sent">60.47 ± 2.94 / 72.79 ± 1.90</td> <!-- SB10k -->
   <td class="de la">51.26 ± 4.94 / 74.76 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">30.04 ± 1.30 / 58.77 ± 1.50</td> <!-- GermanQuAD -->
   <td class="de summ">63.62 ± 0.65 / 13.08 ± 0.87</td> <!-- MLSum -->
   <td class="de know">73.80 ± 2.03 / 80.31 ± 1.54</td> <!-- MMLU-de -->
   <td class="de reason">83.93 ± 2.38 / 87.85 ± 1.80</td> <!-- HellaSwag-de -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.22 ± 3.26 / 33.41 ± 3.24</td> <!-- Dutch Social -->
   <td class="nl la">72.30 ± 2.26 / 85.96 ± 1.13</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.13 ± 0.50 / 17.61 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.04 ± 1.91 / 77.58 ± 1.42</td> <!-- MMLU-nl -->
   <td class="nl reason">88.29 ± 2.26 / 91.17 ± 1.70</td> <!-- HellaSwag-nl -->
   <td class="en ner">81.79 ± 1.39 / 65.51 ± 4.16</td> <!-- CoNLL-en -->
   <td class="en sent">67.55 ± 2.34 / 74.04 ± 1.80</td> <!-- SST5 -->
   <td class="en la">51.21 ± 4.96 / 75.11 ± 2.42</td> <!-- ScaLA-en -->
   <td class="en rc">66.60 ± 1.45 / 84.48 ± 0.76</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.33</td> <!-- ScandEval rank -->
   <td class="da-rank">1.25</td> <!-- Danish rank -->
   <td class="no-rank">1.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.18</td> <!-- Swedish rank -->
   <td class="is-rank">1.21</td> <!-- Icelandic rank -->
   <td class="de-rank">1.40</td> <!-- German rank -->
   <td class="nl-rank">1.65</td> <!-- Dutch rank -->
   <td class="en-rank">1.37</td> <!-- English rank -->
   <td class="da ner">71.15 ± 2.89 / 52.24 ± 3.76</td> <!-- DANSK -->
   <td class="da sent">49.42 ± 3.29 / 61.74 ± 2.59</td> <!-- Angry Tweets -->
   <td class="da la">64.59 ± 2.97 / 79.93 ± 1.88</td> <!-- ScaLA-da -->
   <td class="da rc">57.35 ± 2.51 / 67.87 ± 1.75</td> <!-- ScandiQA-da -->
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
   <td class="no rc">43.51 ± 3.40 / 74.52 ± 1.79</td> <!-- NorQuAD -->
   <td class="no know">73.81 ± 1.88 / 80.39 ± 1.45</td> <!-- MMLU-no -->
   <td class="no reason">89.91 ± 1.13 / 92.42 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.00 ± 0.29 / 16.97 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">70.70 ± 1.32 / 77.97 ± 0.99</td> <!-- MMLU-sv -->
   <td class="sv reason">86.30 ± 2.23 / 89.65 ± 1.68</td> <!-- HellaSwag-sv -->
   <td class="is ner">81.19 ± 2.45 / 54.02 ± 5.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">51.10 ± 5.09 / 73.25 ± 3.42</td> <!-- ScaLA-is -->
   <td class="is rc">29.64 ± 2.12 / 55.46 ± 1.12</td> <!-- NQiI -->
   <td class="is summ">68.25 ± 0.27 / 19.22 ± 0.51</td> <!-- RRN -->
   <td class="is know">91.27 ± 1.41 / 93.40 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">70.85 ± 5.98 / 85.55 ± 3.05</td> <!-- Winogrande-is -->
   <td class="de ner">69.99 ± 1.63 / 45.58 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">54.82 ± 2.19 / 68.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">43.66 ± 5.67 / 64.64 ± 4.65</td> <!-- ScaLA-de -->
   <td class="de rc">30.06 ± 1.04 / 60.77 ± 1.11</td> <!-- GermanQuAD -->
   <td class="de summ">63.80 ± 0.60 / 13.87 ± 1.05</td> <!-- MLSum -->
   <td class="de know">74.13 ± 1.60 / 80.59 ± 1.22</td> <!-- MMLU-de -->
   <td class="de reason">88.18 ± 1.79 / 91.13 ± 1.34</td> <!-- HellaSwag-de -->
   <td class="nl ner">76.75 ± 3.44 / 61.13 ± 4.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 2.24 / 32.52 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">56.26 ± 4.51 / 73.83 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.55 ± 2.54 / 76.28 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.86 ± 0.46 / 16.93 ± 0.91</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">73.11 ± 1.87 / 79.69 ± 1.46</td> <!-- MMLU-nl -->
   <td class="nl reason">92.69 ± 1.46 / 94.53 ± 1.09</td> <!-- HellaSwag-nl -->
   <td class="en ner">83.48 ± 1.52 / 75.51 ± 2.26</td> <!-- CoNLL-en -->
   <td class="en sent">62.74 ± 2.04 / 71.28 ± 1.46</td> <!-- SST5 -->
   <td class="en la">46.56 ± 3.35 / 71.13 ± 1.97</td> <!-- ScaLA-en -->
   <td class="en rc">65.41 ± 1.96 / 84.78 ± 0.68</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="da-rank">1.43</td> <!-- Danish rank -->
   <td class="no-rank">1.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.57</td> <!-- Swedish rank -->
   <td class="is-rank">2.64</td> <!-- Icelandic rank -->
   <td class="de-rank">1.45</td> <!-- German rank -->
   <td class="nl-rank">1.85</td> <!-- Dutch rank -->
   <td class="en-rank">1.46</td> <!-- English rank -->
   <td class="da ner">59.94 ± 1.58 / 38.00 ± 1.88</td> <!-- DANSK -->
   <td class="da sent">59.06 ± 0.91 / 72.86 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">58.57 ± 2.19 / 78.63 ± 1.31</td> <!-- ScaLA-da -->
   <td class="da rc">57.48 ± 0.75 / 65.60 ± 0.65</td> <!-- ScandiQA-da -->
   <td class="da summ">68.12 ± 1.10 / 23.96 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">85.20 ± 0.83 / 88.80 ± 0.65</td> <!-- Danske Talemaader -->
   <td class="da know">84.02 ± 1.63 / 89.32 ± 1.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">71.26 ± 1.64 / 78.17 ± 1.28</td> <!-- HellaSwag-da -->
   <td class="no ner">67.35 ± 2.33 / 56.75 ± 3.04</td> <!-- NorNE-nb -->
   <td class="no ner">66.61 ± 1.81 / 57.24 ± 4.35</td> <!-- NorNE-nn -->
   <td class="no sent">67.14 ± 1.22 / 78.63 ± 0.96</td> <!-- NoReC -->
   <td class="no summ">66.24 ± 0.95 / 20.99 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">64.66 ± 1.38 / 81.94 ± 0.79</td> <!-- ScaLA-nb -->
   <td class="no la">52.49 ± 2.01 / 75.95 ± 1.15</td> <!-- ScaLA-nn -->
   <td class="no rc">44.85 ± 2.17 / 73.41 ± 1.61</td> <!-- NorQuAD -->
   <td class="no know">58.34 ± 1.14 / 68.54 ± 0.88</td> <!-- MMLU-no -->
   <td class="no reason">70.87 ± 2.22 / 77.92 ± 1.72</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.59 ± 2.04 / 45.11 ± 4.50</td> <!-- SUC3 -->
   <td class="sv sent">80.73 ± 0.52 / 81.25 ± 0.57</td> <!-- SweReC -->
   <td class="sv la">61.37 ± 2.06 / 79.34 ± 1.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.76 ± 1.03 / 66.73 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.54 ± 0.91 / 19.89 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">58.15 ± 1.11 / 68.33 ± 0.83</td> <!-- MMLU-sv -->
   <td class="sv reason">68.94 ± 1.51 / 76.41 ± 1.17</td> <!-- HellaSwag-sv -->
   <td class="is ner">55.48 ± 2.38 / 47.46 ± 2.77</td> <!-- MIM-GOLD-NER -->
   <td class="is la">20.10 ± 1.79 / 59.68 ± 0.93</td> <!-- ScaLA-is -->
   <td class="is rc">27.18 ± 1.05 / 53.76 ± 1.19</td> <!-- NQiI -->
   <td class="is summ">68.83 ± 0.22 / 22.98 ± 0.43</td> <!-- RRN -->
   <td class="is know">67.22 ± 1.40 / 75.44 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">35.27 ± 2.45 / 67.79 ± 1.24</td> <!-- Winogrande-is -->
   <td class="de ner">64.13 ± 1.65 / 55.46 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">60.28 ± 1.75 / 73.37 ± 1.43</td> <!-- SB10k -->
   <td class="de la">46.69 ± 1.99 / 71.96 ± 0.73</td> <!-- ScaLA-de -->
   <td class="de rc">28.54 ± 1.38 / 59.38 ± 1.85</td> <!-- GermanQuAD -->
   <td class="de summ">67.87 ± 0.99 / 24.26 ± 2.65</td> <!-- MLSum -->
   <td class="de know">59.43 ± 0.82 / 69.41 ± 0.61</td> <!-- MMLU-de -->
   <td class="de reason">71.59 ± 1.49 / 78.30 ± 1.23</td> <!-- HellaSwag-de -->
   <td class="nl ner">65.20 ± 1.76 / 53.16 ± 2.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.80 ± 0.93 / 36.86 ± 1.08</td> <!-- Dutch Social -->
   <td class="nl la">59.02 ± 1.53 / 79.44 ± 0.78</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.60 ± 1.51 / 74.99 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.03 ± 1.25 / 20.76 ± 1.31</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">59.71 ± 0.83 / 69.70 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">70.70 ± 1.31 / 77.81 ± 0.99</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.40 ± 1.15 / 59.91 ± 1.66</td> <!-- CoNLL-en -->
   <td class="en sent">68.68 ± 0.87 / 73.25 ± 0.48</td> <!-- SST5 -->
   <td class="en la">54.17 ± 2.59 / 76.02 ± 1.67</td> <!-- ScaLA-en -->
   <td class="en rc">66.96 ± 1.51 / 84.76 ± 0.92</td> <!-- SQuAD -->
   <td class="en summ">69.79 ± 0.37 / 26.34 ± 0.54</td> <!-- CNN-DailyMail -->
   <td class="en know">68.71 ± 0.72 / 76.45 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">81.25 ± 1.38 / 85.84 ± 1.05</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="da-rank">1.68</td> <!-- Danish rank -->
   <td class="no-rank">1.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.77</td> <!-- Swedish rank -->
   <td class="is-rank">2.92</td> <!-- Icelandic rank -->
   <td class="de-rank">1.68</td> <!-- German rank -->
   <td class="nl-rank">2.06</td> <!-- Dutch rank -->
   <td class="en-rank">1.64</td> <!-- English rank -->
   <td class="da ner">49.05 ± 2.41 / 30.91 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">52.26 ± 1.31 / 64.13 ± 1.93</td> <!-- Angry Tweets -->
   <td class="da la">58.38 ± 1.21 / 78.98 ± 0.68</td> <!-- ScaLA-da -->
   <td class="da rc">55.34 ± 0.82 / 64.41 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="da summ">67.67 ± 1.05 / 23.18 ± 1.13</td> <!-- Nordjylland-News -->
   <td class="da know">80.62 ± 0.77 / 85.41 ± 0.58</td> <!-- Danske Talemaader -->
   <td class="da know">75.37 ± 2.23 / 83.59 ± 1.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">66.17 ± 1.45 / 74.39 ± 1.13</td> <!-- HellaSwag-da -->
   <td class="no ner">61.82 ± 2.72 / 44.91 ± 3.62</td> <!-- NorNE-nb -->
   <td class="no ner">60.41 ± 2.62 / 46.29 ± 3.79</td> <!-- NorNE-nn -->
   <td class="no sent">61.06 ± 1.21 / 73.45 ± 0.94</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.37 / 19.22 ± 0.79</td> <!-- No Sammendrag -->
   <td class="no la">62.46 ± 1.49 / 81.11 ± 0.72</td> <!-- ScaLA-nb -->
   <td class="no la">52.99 ± 1.89 / 76.14 ± 1.20</td> <!-- ScaLA-nn -->
   <td class="no rc">39.10 ± 1.50 / 70.14 ± 1.53</td> <!-- NorQuAD -->
   <td class="no know">49.45 ± 0.93 / 61.63 ± 0.72</td> <!-- MMLU-no -->
   <td class="no reason">67.96 ± 1.93 / 75.79 ± 1.47</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.50 ± 1.02 / 37.38 ± 2.57</td> <!-- SUC3 -->
   <td class="sv sent">78.51 ± 0.93 / 76.24 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">61.28 ± 1.63 / 80.07 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.22 ± 1.03 / 64.60 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.30 ± 0.12 / 19.72 ± 0.19</td> <!-- SweDN -->
   <td class="sv know">51.58 ± 0.83 / 63.27 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">66.61 ± 1.12 / 74.72 ± 0.93</td> <!-- HellaSwag-sv -->
   <td class="is ner">45.42 ± 1.86 / 36.69 ± 2.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">24.23 ± 0.89 / 61.40 ± 0.70</td> <!-- ScaLA-is -->
   <td class="is rc">24.96 ± 1.52 / 55.04 ± 0.80</td> <!-- NQiI -->
   <td class="is summ">68.19 ± 0.25 / 22.04 ± 0.48</td> <!-- RRN -->
   <td class="is know">54.30 ± 1.60 / 65.62 ± 1.20</td> <!-- ARC-is -->
   <td class="is reason">24.35 ± 2.31 / 62.81 ± 1.08</td> <!-- Winogrande-is -->
   <td class="de ner">50.35 ± 2.81 / 39.72 ± 2.62</td> <!-- GermEval -->
   <td class="de sent">58.60 ± 2.21 / 71.12 ± 1.12</td> <!-- SB10k -->
   <td class="de la">45.78 ± 1.55 / 70.64 ± 0.61</td> <!-- ScaLA-de -->
   <td class="de rc">30.46 ± 0.98 / 60.56 ± 2.25</td> <!-- GermanQuAD -->
   <td class="de summ">67.99 ± 1.12 / 24.07 ± 2.91</td> <!-- MLSum -->
   <td class="de know">53.61 ± 0.60 / 64.92 ± 0.47</td> <!-- MMLU-de -->
   <td class="de reason">68.16 ± 0.75 / 75.71 ± 0.65</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.62 ± 2.15 / 39.41 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.78 ± 1.31 / 32.80 ± 0.87</td> <!-- Dutch Social -->
   <td class="nl la">59.23 ± 1.58 / 79.42 ± 0.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.78 ± 0.87 / 72.71 ± 0.70</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.39 ± 0.71 / 20.04 ± 1.05</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.99 ± 0.77 / 65.31 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">65.58 ± 1.18 / 73.75 ± 0.94</td> <!-- HellaSwag-nl -->
   <td class="en ner">58.07 ± 2.46 / 51.39 ± 2.35</td> <!-- CoNLL-en -->
   <td class="en sent">68.40 ± 1.17 / 71.79 ± 0.65</td> <!-- SST5 -->
   <td class="en la">51.58 ± 2.03 / 74.57 ± 1.48</td> <!-- ScaLA-en -->
   <td class="en rc">62.03 ± 1.62 / 81.91 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">69.72 ± 0.42 / 25.66 ± 0.38</td> <!-- CNN-DailyMail -->
   <td class="en know">63.99 ± 0.76 / 72.84 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">75.87 ± 1.74 / 81.61 ± 1.30</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.01</td> <!-- ScandEval rank -->
   <td class="da-rank">1.61</td> <!-- Danish rank -->
   <td class="no-rank">1.91</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.75</td> <!-- Swedish rank -->
   <td class="is-rank">2.98</td> <!-- Icelandic rank -->
   <td class="de-rank">1.97</td> <!-- German rank -->
   <td class="nl-rank">2.15</td> <!-- Dutch rank -->
   <td class="en-rank">1.73</td> <!-- English rank -->
   <td class="da ner">61.31 ± 2.34 / 49.86 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">52.52 ± 2.05 / 68.10 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">57.63 ± 2.80 / 77.01 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da rc">57.03 ± 1.95 / 65.51 ± 1.48</td> <!-- ScandiQA-da -->
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
   <td class="no rc">45.35 ± 2.97 / 73.47 ± 1.69</td> <!-- NorQuAD -->
   <td class="no know">40.26 ± 5.24 / 54.88 ± 3.85</td> <!-- MMLU-no -->
   <td class="no reason">59.02 ± 1.63 / 68.63 ± 1.34</td> <!-- HellaSwag-no -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.92 ± 0.16 / 19.00 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">40.73 ± 3.36 / 55.16 ± 2.75</td> <!-- MMLU-sv -->
   <td class="sv reason">50.51 ± 2.33 / 62.07 ± 1.95</td> <!-- HellaSwag-sv -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is rc">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">49.88 ± 2.38 / 62.27 ± 1.75</td> <!-- ARC-is -->
   <td class="is reason">18.61 ± 6.00 / 61.33 ± 2.93</td> <!-- Winogrande-is -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de rc">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">64.90 ± 0.22 / 15.99 ± 0.32</td> <!-- MLSum -->
   <td class="de know">35.39 ± 3.89 / 51.41 ± 2.98</td> <!-- MMLU-de -->
   <td class="de reason">56.88 ± 2.50 / 66.76 ± 2.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.13 ± 0.41 / 21.32 ± 0.75</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.28 ± 2.88 / 56.45 ± 2.26</td> <!-- MMLU-nl -->
   <td class="nl reason">61.52 ± 2.69 / 70.62 ± 2.20</td> <!-- HellaSwag-nl -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en rc">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="da-rank">1.94</td> <!-- Danish rank -->
   <td class="no-rank">2.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.94</td> <!-- Swedish rank -->
   <td class="is-rank">2.71</td> <!-- Icelandic rank -->
   <td class="de-rank">1.77</td> <!-- German rank -->
   <td class="nl-rank">2.44</td> <!-- Dutch rank -->
   <td class="en-rank">1.57</td> <!-- English rank -->
   <td class="da ner">63.59 ± 2.16 / 42.42 ± 3.34</td> <!-- DANSK -->
   <td class="da sent">29.47 ± 4.78 / 50.59 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">38.37 ± 9.13 / 60.56 ± 8.53</td> <!-- ScaLA-da -->
   <td class="da rc">54.63 ± 0.51 / 65.79 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="da summ">65.94 ± 0.11 / 17.32 ± 0.29</td> <!-- Nordjylland-News -->
   <td class="da know">80.46 ± 4.74 / 84.69 ± 3.92</td> <!-- Danske Talemaader -->
   <td class="da know">76.16 ± 4.99 / 83.11 ± 4.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">62.12 ± 2.52 / 70.60 ± 2.10</td> <!-- HellaSwag-da -->
   <td class="no ner">75.05 ± 1.56 / 57.52 ± 4.29</td> <!-- NorNE-nb -->
   <td class="no ner">74.08 ± 1.43 / 62.50 ± 4.89</td> <!-- NorNE-nn -->
   <td class="no sent">37.79 ± 4.47 / 55.88 ± 3.23</td> <!-- NoReC -->
   <td class="no summ">63.80 ± 0.16 / 13.40 ± 0.32</td> <!-- No Sammendrag -->
   <td class="no la">31.59 ± 11.25 / 54.68 ± 10.28</td> <!-- ScaLA-nb -->
   <td class="no la">39.25 ± 7.82 / 62.90 ± 7.12</td> <!-- ScaLA-nn -->
   <td class="no rc">39.43 ± 2.31 / 72.15 ± 1.71</td> <!-- NorQuAD -->
   <td class="no know">51.93 ± 1.39 / 62.52 ± 1.41</td> <!-- MMLU-no -->
   <td class="no reason">68.29 ± 1.51 / 75.45 ± 1.24</td> <!-- HellaSwag-no -->
   <td class="sv ner">67.38 ± 1.52 / 52.86 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 4.81 / 67.01 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">29.41 ± 10.34 / 52.38 ± 8.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.67 ± 0.89 / 66.26 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.70 ± 0.71 / 16.98 ± 0.75</td> <!-- SweDN -->
   <td class="sv know">50.06 ± 2.65 / 61.33 ± 2.36</td> <!-- MMLU-sv -->
   <td class="sv reason">64.58 ± 2.48 / 72.57 ± 2.06</td> <!-- HellaSwag-sv -->
   <td class="is ner">67.56 ± 1.93 / 43.20 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">23.28 ± 7.61 / 52.43 ± 7.20</td> <!-- ScaLA-is -->
   <td class="is rc">24.91 ± 1.14 / 52.48 ± 0.90</td> <!-- NQiI -->
   <td class="is summ">67.32 ± 0.95 / 17.55 ± 1.32</td> <!-- RRN -->
   <td class="is know">67.57 ± 3.31 / 75.27 ± 2.62</td> <!-- ARC-is -->
   <td class="is reason">15.36 ± 5.77 / 49.21 ± 3.61</td> <!-- Winogrande-is -->
   <td class="de ner">67.90 ± 1.07 / 45.53 ± 3.11</td> <!-- GermEval -->
   <td class="de sent">51.88 ± 5.19 / 67.24 ± 3.71</td> <!-- SB10k -->
   <td class="de la">46.77 ± 2.33 / 69.48 ± 2.55</td> <!-- ScaLA-de -->
   <td class="de rc">24.70 ± 1.31 / 56.87 ± 0.77</td> <!-- GermanQuAD -->
   <td class="de summ">64.65 ± 0.10 / 14.11 ± 0.26</td> <!-- MLSum -->
   <td class="de know">51.72 ± 2.53 / 62.88 ± 2.10</td> <!-- MMLU-de -->
   <td class="de reason">62.80 ± 1.97 / 70.65 ± 1.80</td> <!-- HellaSwag-de -->
   <td class="nl ner">68.20 ± 1.93 / 49.92 ± 2.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.65 ± 1.80 / 14.84 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">31.15 ± 7.70 / 52.16 ± 7.03</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.17 ± 1.82 / 72.08 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.45 / 18.21 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">54.56 ± 1.84 / 64.78 ± 1.89</td> <!-- MMLU-nl -->
   <td class="nl reason">65.27 ± 1.51 / 72.80 ± 1.37</td> <!-- HellaSwag-nl -->
   <td class="en ner">78.84 ± 1.47 / 68.25 ± 3.41</td> <!-- CoNLL-en -->
   <td class="en sent">60.72 ± 1.81 / 67.08 ± 1.16</td> <!-- SST5 -->
   <td class="en la">50.99 ± 1.31 / 72.72 ± 1.34</td> <!-- ScaLA-en -->
   <td class="en rc">61.45 ± 1.95 / 83.59 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">68.66 ± 0.07 / 21.97 ± 0.19</td> <!-- CNN-DailyMail -->
   <td class="en know">62.15 ± 1.02 / 71.31 ± 0.77</td> <!-- MMLU -->
   <td class="en reason">79.13 ± 1.02 / 83.93 ± 0.81</td> <!-- HellaSwag -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- Nordjylland-News version -->
   <td>12.11.0</td> <!-- Danske Talemaader version -->
   <td>12.11.0</td> <!-- Danish Citizen Tests version -->
   <td>12.11.0</td> <!-- HellaSwag-da version -->
   <td>12.11.0</td> <!-- NorNE-nb version -->
   <td>12.11.0</td> <!-- NorNE-nn version -->
   <td>12.11.0</td> <!-- NoReC version -->
   <td>12.11.0</td> <!-- No Sammendrag version -->
   <td>12.11.0</td> <!-- ScaLA-nb version -->
   <td>12.11.0</td> <!-- ScaLA-nn version -->
   <td>12.11.0</td> <!-- NorQuAD version -->
   <td>12.11.0</td> <!-- MMLU-no version -->
   <td>12.11.0</td> <!-- HellaSwag-no version -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   <td>12.11.0</td> <!-- SweDN version -->
   <td>12.11.0</td> <!-- MMLU-sv version -->
   <td>12.11.0</td> <!-- HellaSwag-sv version -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- RRN version -->
   <td>12.11.0</td> <!-- ARC-is version -->
   <td>12.11.0</td> <!-- Winogrande-is version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- MLSum version -->
   <td>12.11.0</td> <!-- MMLU-de version -->
   <td>12.11.0</td> <!-- HellaSwag-de version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.11.0</td> <!-- MMLU-nl version -->
   <td>12.11.0</td> <!-- HellaSwag-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.11.0</td> <!-- SST5 version -->
   <td>12.11.0</td> <!-- ScaLA-en version -->
   <td>12.11.0</td> <!-- SQuAD version -->
   <td>12.11.0</td> <!-- CNN-DailyMail version -->
   <td>12.11.0</td> <!-- MMLU version -->
   <td>12.11.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="da-rank">2.00</td> <!-- Danish rank -->
   <td class="no-rank">1.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.89</td> <!-- Swedish rank -->
   <td class="is-rank">3.32</td> <!-- Icelandic rank -->
   <td class="de-rank">1.64</td> <!-- German rank -->
   <td class="nl-rank">2.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.73</td> <!-- English rank -->
   <td class="da ner">44.16 ± 3.11 / 25.93 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">38.84 ± 2.31 / 45.52 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">43.42 ± 3.95 / 69.40 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">60.11 ± 0.96 / 66.24 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 1.14 / 24.10 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">81.68 ± 0.62 / 86.22 ± 0.47</td> <!-- Danske Talemaader -->
   <td class="da know">77.77 ± 1.30 / 85.06 ± 0.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">50.04 ± 3.99 / 61.09 ± 3.31</td> <!-- HellaSwag-da -->
   <td class="no ner">54.08 ± 2.08 / 34.62 ± 1.80</td> <!-- NorNE-nb -->
   <td class="no ner">54.33 ± 3.02 / 37.70 ± 2.97</td> <!-- NorNE-nn -->
   <td class="no sent">62.54 ± 1.17 / 75.53 ± 0.73</td> <!-- NoReC -->
   <td class="no summ">65.67 ± 0.85 / 20.11 ± 0.92</td> <!-- No Sammendrag -->
   <td class="no la">50.88 ± 2.84 / 74.69 ± 1.56</td> <!-- ScaLA-nb -->
   <td class="no la">41.01 ± 1.91 / 69.35 ± 1.67</td> <!-- ScaLA-nn -->
   <td class="no rc">46.25 ± 3.89 / 72.99 ± 3.16</td> <!-- NorQuAD -->
   <td class="no know">50.81 ± 1.18 / 62.98 ± 0.88</td> <!-- MMLU-no -->
   <td class="no reason">53.37 ± 3.87 / 63.52 ± 3.49</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.43 ± 3.97 / 27.20 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">80.55 ± 1.46 / 77.22 ± 3.78</td> <!-- SweReC -->
   <td class="sv la">50.86 ± 3.91 / 72.14 ± 3.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.35 ± 1.16 / 65.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.63 ± 0.26 / 19.75 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">52.06 ± 0.97 / 63.92 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">49.80 ± 3.86 / 60.88 ± 3.42</td> <!-- HellaSwag-sv -->
   <td class="is ner">30.89 ± 4.28 / 24.06 ± 1.93</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.29 ± 3.38 / 35.79 ± 2.12</td> <!-- ScaLA-is -->
   <td class="is rc">32.25 ± 1.89 / 58.20 ± 1.70</td> <!-- NQiI -->
   <td class="is summ">67.58 ± 0.63 / 21.53 ± 0.99</td> <!-- RRN -->
   <td class="is know">55.69 ± 1.49 / 66.84 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">17.50 ± 2.56 / 58.33 ± 1.75</td> <!-- Winogrande-is -->
   <td class="de ner">47.39 ± 1.96 / 34.14 ± 1.70</td> <!-- GermEval -->
   <td class="de sent">62.89 ± 2.21 / 74.51 ± 1.63</td> <!-- SB10k -->
   <td class="de la">37.22 ± 4.67 / 67.37 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de rc">39.11 ± 2.14 / 67.67 ± 2.90</td> <!-- GermanQuAD -->
   <td class="de summ">70.44 ± 1.18 / 30.83 ± 2.69</td> <!-- MLSum -->
   <td class="de know">53.28 ± 1.15 / 64.86 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">54.51 ± 2.74 / 64.51 ± 2.33</td> <!-- HellaSwag-de -->
   <td class="nl ner">57.13 ± 2.73 / 36.21 ± 1.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.43 ± 2.17 / 40.83 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">31.39 ± 5.53 / 56.70 ± 5.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.33 ± 1.35 / 73.56 ± 0.52</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.59 ± 1.21 / 21.08 ± 1.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.71 ± 0.86 / 65.15 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">53.26 ± 3.38 / 63.65 ± 2.84</td> <!-- HellaSwag-nl -->
   <td class="en ner">50.90 ± 2.39 / 44.74 ± 1.46</td> <!-- CoNLL-en -->
   <td class="en sent">68.91 ± 0.89 / 70.46 ± 1.23</td> <!-- SST5 -->
   <td class="en la">43.79 ± 3.15 / 71.10 ± 1.74</td> <!-- ScaLA-en -->
   <td class="en rc">69.17 ± 1.55 / 84.25 ± 1.13</td> <!-- SQuAD -->
   <td class="en summ">69.67 ± 0.46 / 25.26 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">61.34 ± 0.86 / 70.95 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">62.23 ± 3.55 / 70.69 ± 3.11</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="da-rank">2.01</td> <!-- Danish rank -->
   <td class="no-rank">2.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.07</td> <!-- Swedish rank -->
   <td class="is-rank">3.50</td> <!-- Icelandic rank -->
   <td class="de-rank">1.53</td> <!-- German rank -->
   <td class="nl-rank">2.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.46</td> <!-- English rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da rc">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
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
   <td class="no rc">55.33 ± 3.29 / 80.42 ± 1.68</td> <!-- NorQuAD -->
   <td class="no know">35.57 ± 0.78 / 51.45 ± 0.56</td> <!-- MMLU-no -->
   <td class="no reason">62.76 ± 1.85 / 71.77 ± 1.45</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.19 ± 0.36 / 19.09 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">39.82 ± 0.69 / 54.84 ± 0.53</td> <!-- MMLU-sv -->
   <td class="sv reason">68.87 ± 1.35 / 76.46 ± 1.04</td> <!-- HellaSwag-sv -->
   <td class="is ner">62.08 ± 2.27 / 51.09 ± 4.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.58 ± 1.03 / 44.38 ± 3.90</td> <!-- ScaLA-is -->
   <td class="is rc">29.66 ± 3.02 / 56.60 ± 2.22</td> <!-- NQiI -->
   <td class="is summ">66.11 ± 0.85 / 18.74 ± 0.90</td> <!-- RRN -->
   <td class="is know">18.75 ± 1.02 / 38.96 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">7.64 ± 1.91 / 49.40 ± 1.45</td> <!-- Winogrande-is -->
   <td class="de ner">68.11 ± 1.32 / 56.25 ± 1.65</td> <!-- GermEval -->
   <td class="de sent">59.79 ± 1.60 / 71.47 ± 1.54</td> <!-- SB10k -->
   <td class="de la">35.45 ± 3.06 / 66.13 ± 1.28</td> <!-- ScaLA-de -->
   <td class="de rc">37.27 ± 1.23 / 68.54 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.95 / 28.82 ± 2.24</td> <!-- MLSum -->
   <td class="de know">41.20 ± 0.85 / 55.90 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">72.65 ± 0.69 / 79.18 ± 0.58</td> <!-- HellaSwag-de -->
   <td class="nl ner">65.37 ± 1.61 / 46.10 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.93 ± 1.80 / 34.67 ± 2.84</td> <!-- Dutch Social -->
   <td class="nl la">41.67 ± 1.53 / 69.81 ± 1.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">67.75 ± 0.62 / 78.01 ± 0.45</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.83 ± 0.35 / 26.12 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.18 ± 0.57 / 55.06 ± 0.44</td> <!-- MMLU-nl -->
   <td class="nl reason">65.34 ± 1.05 / 73.48 ± 0.83</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.50 ± 1.14 / 63.41 ± 0.77</td> <!-- CoNLL-en -->
   <td class="en sent">70.01 ± 0.93 / 59.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">41.35 ± 2.01 / 70.11 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">76.79 ± 0.43 / 89.35 ± 0.19</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="da-rank">2.07</td> <!-- Danish rank -->
   <td class="no-rank">2.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.14</td> <!-- Swedish rank -->
   <td class="is-rank">3.21</td> <!-- Icelandic rank -->
   <td class="de-rank">1.72</td> <!-- German rank -->
   <td class="nl-rank">2.30</td> <!-- Dutch rank -->
   <td class="en-rank">1.60</td> <!-- English rank -->
   <td class="da ner">53.95 ± 2.29 / 34.84 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">48.97 ± 1.81 / 64.19 ± 1.99</td> <!-- Angry Tweets -->
   <td class="da la">31.78 ± 4.52 / 61.53 ± 5.44</td> <!-- ScaLA-da -->
   <td class="da rc">56.44 ± 1.24 / 65.53 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">66.24 ± 0.66 / 20.00 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">67.09 ± 1.38 / 74.85 ± 1.04</td> <!-- Danske Talemaader -->
   <td class="da know">72.87 ± 2.11 / 81.97 ± 1.42</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.77 ± 2.30 / 55.61 ± 2.33</td> <!-- HellaSwag-da -->
   <td class="no ner">70.14 ± 1.60 / 51.03 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">68.74 ± 1.21 / 51.48 ± 2.96</td> <!-- NorNE-nn -->
   <td class="no sent">60.64 ± 2.52 / 73.91 ± 1.86</td> <!-- NoReC -->
   <td class="no summ">64.61 ± 0.40 / 16.10 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">35.59 ± 2.29 / 61.96 ± 3.72</td> <!-- ScaLA-nb -->
   <td class="no la">29.22 ± 2.86 / 60.98 ± 4.02</td> <!-- ScaLA-nn -->
   <td class="no rc">49.87 ± 4.84 / 76.01 ± 3.10</td> <!-- NorQuAD -->
   <td class="no know">39.07 ± 0.84 / 53.89 ± 0.69</td> <!-- MMLU-no -->
   <td class="no reason">37.95 ± 3.53 / 51.35 ± 3.17</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.86 ± 1.95 / 36.42 ± 3.49</td> <!-- SUC3 -->
   <td class="sv sent">70.54 ± 6.38 / 73.39 ± 6.37</td> <!-- SweReC -->
   <td class="sv la">37.50 ± 2.48 / 66.32 ± 1.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.00 ± 0.85 / 65.98 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.93 ± 0.19 / 19.24 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">40.58 ± 1.17 / 55.16 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">42.99 ± 2.04 / 56.16 ± 1.93</td> <!-- HellaSwag-sv -->
   <td class="is ner">59.70 ± 1.67 / 41.69 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.64 ± 3.09 / 38.48 ± 2.74</td> <!-- ScaLA-is -->
   <td class="is rc">29.68 ± 1.85 / 58.88 ± 0.87</td> <!-- NQiI -->
   <td class="is summ">68.13 ± 0.31 / 20.42 ± 0.65</td> <!-- RRN -->
   <td class="is know">41.76 ± 1.72 / 56.28 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">13.24 ± 4.12 / 56.22 ± 1.89</td> <!-- Winogrande-is -->
   <td class="de ner">66.27 ± 1.13 / 49.86 ± 1.62</td> <!-- GermEval -->
   <td class="de sent">57.70 ± 2.68 / 71.63 ± 1.94</td> <!-- SB10k -->
   <td class="de la">35.54 ± 4.25 / 60.12 ± 5.53</td> <!-- ScaLA-de -->
   <td class="de rc">34.45 ± 1.61 / 66.90 ± 2.58</td> <!-- GermanQuAD -->
   <td class="de summ">68.65 ± 1.15 / 25.16 ± 2.66</td> <!-- MLSum -->
   <td class="de know">47.05 ± 1.12 / 60.01 ± 0.86</td> <!-- MMLU-de -->
   <td class="de reason">52.68 ± 3.39 / 63.07 ± 2.88</td> <!-- HellaSwag-de -->
   <td class="nl ner">66.57 ± 1.86 / 48.40 ± 2.67</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.10 ± 1.55 / 33.62 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">40.31 ± 2.25 / 69.53 ± 1.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.99 ± 0.95 / 74.24 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.68 / 20.75 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.50 ± 0.84 / 56.53 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">48.51 ± 1.44 / 60.59 ± 1.34</td> <!-- HellaSwag-nl -->
   <td class="en ner">75.24 ± 0.84 / 67.78 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">63.05 ± 1.41 / 70.34 ± 0.52</td> <!-- SST5 -->
   <td class="en la">44.75 ± 2.73 / 71.43 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en rc">67.70 ± 1.57 / 83.88 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">70.56 ± 0.58 / 25.57 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">57.55 ± 1.00 / 68.02 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">67.97 ± 1.89 / 75.51 ± 1.48</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da-rank">2.13</td> <!-- Danish rank -->
   <td class="no-rank">2.32</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.10</td> <!-- Swedish rank -->
   <td class="is-rank">3.46</td> <!-- Icelandic rank -->
   <td class="de-rank">1.66</td> <!-- German rank -->
   <td class="nl-rank">2.13</td> <!-- Dutch rank -->
   <td class="en-rank">1.71</td> <!-- English rank -->
   <td class="da ner">52.49 ± 1.89 / 38.85 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">49.67 ± 1.40 / 65.83 ± 1.40</td> <!-- Angry Tweets -->
   <td class="da la">22.80 ± 5.31 / 55.25 ± 6.92</td> <!-- ScaLA-da -->
   <td class="da rc">57.07 ± 0.68 / 64.46 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">66.75 ± 0.97 / 21.86 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">59.57 ± 1.49 / 69.19 ± 1.13</td> <!-- Danske Talemaader -->
   <td class="da know">65.34 ± 2.38 / 76.95 ± 1.56</td> <!-- Danish Citizen Tests -->
   <td class="da reason">53.97 ± 2.40 / 64.76 ± 2.17</td> <!-- HellaSwag-da -->
   <td class="no ner">69.85 ± 2.00 / 59.43 ± 3.23</td> <!-- NorNE-nb -->
   <td class="no ner">68.83 ± 1.07 / 59.51 ± 2.63</td> <!-- NorNE-nn -->
   <td class="no sent">54.49 ± 2.44 / 69.23 ± 2.00</td> <!-- NoReC -->
   <td class="no summ">64.05 ± 0.67 / 16.34 ± 1.01</td> <!-- No Sammendrag -->
   <td class="no la">28.55 ± 2.65 / 61.53 ± 3.21</td> <!-- ScaLA-nb -->
   <td class="no la">17.47 ± 3.61 / 52.60 ± 5.26</td> <!-- ScaLA-nn -->
   <td class="no rc">43.55 ± 3.42 / 71.05 ± 3.22</td> <!-- NorQuAD -->
   <td class="no know">34.93 ± 1.01 / 50.67 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">49.83 ± 2.75 / 61.44 ± 2.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">67.49 ± 2.20 / 51.10 ± 4.76</td> <!-- SUC3 -->
   <td class="sv sent">76.74 ± 1.27 / 75.66 ± 1.17</td> <!-- SweReC -->
   <td class="sv la">22.37 ± 3.11 / 54.47 ± 4.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.15 ± 0.72 / 64.47 ± 0.58</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.37 ± 0.39 / 19.85 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">37.50 ± 0.73 / 52.72 ± 0.63</td> <!-- MMLU-sv -->
   <td class="sv reason">55.01 ± 2.40 / 65.64 ± 2.12</td> <!-- HellaSwag-sv -->
   <td class="is ner">56.09 ± 3.29 / 42.39 ± 2.51</td> <!-- MIM-GOLD-NER -->
   <td class="is la">8.51 ± 1.55 / 50.18 ± 2.85</td> <!-- ScaLA-is -->
   <td class="is rc">29.23 ± 1.41 / 57.06 ± 0.62</td> <!-- NQiI -->
   <td class="is summ">65.90 ± 0.71 / 18.54 ± 0.92</td> <!-- RRN -->
   <td class="is know">30.58 ± 1.40 / 47.95 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">6.77 ± 2.10 / 53.92 ± 1.32</td> <!-- Winogrande-is -->
   <td class="de ner">66.00 ± 1.13 / 54.14 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.76 ± 3.11 / 68.36 ± 2.92</td> <!-- SB10k -->
   <td class="de la">33.55 ± 4.69 / 63.49 ± 2.99</td> <!-- ScaLA-de -->
   <td class="de rc">32.69 ± 1.98 / 64.23 ± 2.89</td> <!-- GermanQuAD -->
   <td class="de summ">69.65 ± 1.12 / 27.94 ± 2.90</td> <!-- MLSum -->
   <td class="de know">43.46 ± 0.81 / 57.37 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">68.11 ± 1.40 / 75.60 ± 1.16</td> <!-- HellaSwag-de -->
   <td class="nl ner">66.51 ± 1.38 / 52.40 ± 2.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.55 ± 2.14 / 37.36 ± 1.32</td> <!-- Dutch Social -->
   <td class="nl la">34.46 ± 2.79 / 65.61 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.23 ± 1.16 / 72.56 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.87 ± 0.72 / 21.06 ± 1.13</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.81 ± 1.05 / 55.44 ± 0.80</td> <!-- MMLU-nl -->
   <td class="nl reason">60.68 ± 1.04 / 70.24 ± 0.85</td> <!-- HellaSwag-nl -->
   <td class="en ner">72.40 ± 0.80 / 65.83 ± 1.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.46 ± 2.10 / 69.49 ± 1.15</td> <!-- SST5 -->
   <td class="en la">35.86 ± 7.94 / 65.20 ± 6.98</td> <!-- ScaLA-en -->
   <td class="en rc">68.42 ± 1.21 / 83.97 ± 0.74</td> <!-- SQuAD -->
   <td class="en summ">69.38 ± 0.48 / 24.96 ± 0.47</td> <!-- CNN-DailyMail -->
   <td class="en know">53.42 ± 0.91 / 64.98 ± 0.74</td> <!-- MMLU -->
   <td class="en reason">78.36 ± 2.31 / 83.62 ± 1.78</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da-rank">2.03</td> <!-- Danish rank -->
   <td class="no-rank">2.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.18</td> <!-- Swedish rank -->
   <td class="is-rank">3.91</td> <!-- Icelandic rank -->
   <td class="de-rank">1.84</td> <!-- German rank -->
   <td class="nl-rank">2.14</td> <!-- Dutch rank -->
   <td class="en-rank">1.50</td> <!-- English rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da rc">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
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
   <td class="no rc">49.75 ± 1.22 / 77.08 ± 0.60</td> <!-- NorQuAD -->
   <td class="no know">29.72 ± 1.33 / 46.95 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">46.78 ± 2.83 / 59.65 ± 2.28</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.75 ± 0.16 / 20.23 ± 0.23</td> <!-- SweDN -->
   <td class="sv know">36.05 ± 1.10 / 51.86 ± 0.87</td> <!-- MMLU-sv -->
   <td class="sv reason">51.15 ± 1.71 / 63.20 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">49.20 ± 2.64 / 40.79 ± 4.46</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.45 ± 1.40 / 51.11 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">24.61 ± 3.36 / 54.99 ± 2.36</td> <!-- NQiI -->
   <td class="is summ">63.74 ± 2.25 / 18.29 ± 1.40</td> <!-- RRN -->
   <td class="is know">8.45 ± 1.35 / 31.54 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">1.14 ± 0.97 / 50.10 ± 0.82</td> <!-- Winogrande-is -->
   <td class="de ner">65.01 ± 0.68 / 43.34 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">51.80 ± 1.29 / 67.45 ± 0.87</td> <!-- SB10k -->
   <td class="de la">36.18 ± 1.31 / 67.86 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de rc">32.12 ± 2.08 / 67.30 ± 1.66</td> <!-- GermanQuAD -->
   <td class="de summ">66.92 ± 0.41 / 23.23 ± 1.24</td> <!-- MLSum -->
   <td class="de know">37.90 ± 1.03 / 53.36 ± 0.80</td> <!-- MMLU-de -->
   <td class="de reason">60.66 ± 1.28 / 70.32 ± 1.01</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.47 ± 2.31 / 40.89 ± 2.81</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.83 ± 1.91 / 41.53 ± 1.23</td> <!-- Dutch Social -->
   <td class="nl la">45.69 ± 1.76 / 72.13 ± 1.39</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.03 ± 1.37 / 73.17 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.34 ± 0.77 / 22.22 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">37.60 ± 0.83 / 53.13 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">54.33 ± 0.84 / 65.41 ± 0.59</td> <!-- HellaSwag-nl -->
   <td class="en ner">71.81 ± 1.02 / 59.93 ± 2.52</td> <!-- CoNLL-en -->
   <td class="en sent">69.98 ± 1.00 / 69.79 ± 0.76</td> <!-- SST5 -->
   <td class="en la">45.34 ± 2.51 / 72.10 ± 1.10</td> <!-- ScaLA-en -->
   <td class="en rc">72.49 ± 1.57 / 87.51 ± 0.74</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="da-rank">2.30</td> <!-- Danish rank -->
   <td class="no-rank">2.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
   <td class="is-rank">3.38</td> <!-- Icelandic rank -->
   <td class="de-rank">1.98</td> <!-- German rank -->
   <td class="nl-rank">2.40</td> <!-- Dutch rank -->
   <td class="en-rank">1.83</td> <!-- English rank -->
   <td class="da ner">57.19 ± 1.73 / 44.34 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">51.30 ± 1.32 / 64.44 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">10.31 ± 3.91 / 42.59 ± 5.19</td> <!-- ScaLA-da -->
   <td class="da rc">48.80 ± 1.66 / 60.46 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="da summ">67.38 ± 1.09 / 23.21 ± 0.94</td> <!-- Nordjylland-News -->
   <td class="da know">61.78 ± 1.70 / 71.28 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">66.61 ± 1.90 / 77.73 ± 1.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.62 ± 2.26 / 53.92 ± 1.96</td> <!-- HellaSwag-da -->
   <td class="no ner">74.77 ± 0.84 / 71.87 ± 0.97</td> <!-- NorNE-nb -->
   <td class="no ner">72.80 ± 1.57 / 69.98 ± 1.84</td> <!-- NorNE-nn -->
   <td class="no sent">57.30 ± 0.98 / 71.58 ± 0.90</td> <!-- NoReC -->
   <td class="no summ">66.08 ± 0.56 / 19.80 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">5.23 ± 1.83 / 34.90 ± 0.81</td> <!-- ScaLA-nb -->
   <td class="no la">11.51 ± 3.24 / 45.73 ± 5.97</td> <!-- ScaLA-nn -->
   <td class="no rc">43.93 ± 3.73 / 70.96 ± 3.00</td> <!-- NorQuAD -->
   <td class="no know">38.10 ± 0.57 / 52.64 ± 0.47</td> <!-- MMLU-no -->
   <td class="no reason">39.30 ± 1.01 / 54.03 ± 0.82</td> <!-- HellaSwag-no -->
   <td class="sv ner">71.52 ± 1.43 / 59.28 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">80.46 ± 0.83 / 78.67 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">12.29 ± 3.59 / 40.53 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.54 ± 1.52 / 62.08 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.27 ± 0.15 / 19.05 ± 0.30</td> <!-- SweDN -->
   <td class="sv know">39.40 ± 1.44 / 53.87 ± 1.19</td> <!-- MMLU-sv -->
   <td class="sv reason">38.88 ± 1.25 / 53.72 ± 0.91</td> <!-- HellaSwag-sv -->
   <td class="is ner">55.09 ± 1.76 / 40.34 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">8.45 ± 1.33 / 51.00 ± 1.95</td> <!-- ScaLA-is -->
   <td class="is rc">29.65 ± 1.09 / 56.96 ± 1.35</td> <!-- NQiI -->
   <td class="is summ">68.27 ± 0.25 / 22.14 ± 0.62</td> <!-- RRN -->
   <td class="is know">30.33 ± 1.72 / 47.81 ± 1.31</td> <!-- ARC-is -->
   <td class="is reason">10.48 ± 2.28 / 54.89 ± 1.49</td> <!-- Winogrande-is -->
   <td class="de ner">67.61 ± 1.23 / 60.39 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">59.96 ± 2.00 / 70.71 ± 1.80</td> <!-- SB10k -->
   <td class="de la">28.25 ± 3.57 / 59.54 ± 3.88</td> <!-- ScaLA-de -->
   <td class="de rc">28.79 ± 2.02 / 55.82 ± 3.28</td> <!-- GermanQuAD -->
   <td class="de summ">66.87 ± 0.54 / 21.31 ± 1.47</td> <!-- MLSum -->
   <td class="de know">40.00 ± 0.97 / 54.88 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">45.93 ± 1.38 / 58.95 ± 1.06</td> <!-- HellaSwag-de -->
   <td class="nl ner">69.76 ± 1.36 / 57.66 ± 1.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.51 ± 1.59 / 39.71 ± 1.21</td> <!-- Dutch Social -->
   <td class="nl la">37.58 ± 3.42 / 66.98 ± 2.22</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.26 ± 2.09 / 65.63 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.84 ± 0.62 / 21.41 ± 1.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.98 ± 0.71 / 55.51 ± 0.59</td> <!-- MMLU-nl -->
   <td class="nl reason">39.98 ± 1.59 / 54.32 ± 1.27</td> <!-- HellaSwag-nl -->
   <td class="en ner">76.95 ± 0.95 / 72.47 ± 0.82</td> <!-- CoNLL-en -->
   <td class="en sent">68.12 ± 0.92 / 72.48 ± 0.53</td> <!-- SST5 -->
   <td class="en la">34.34 ± 3.37 / 65.84 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en rc">47.88 ± 3.37 / 76.21 ± 1.69</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.25 / 26.30 ± 0.35</td> <!-- CNN-DailyMail -->
   <td class="en know">56.62 ± 0.49 / 67.29 ± 0.39</td> <!-- MMLU -->
   <td class="en reason">69.03 ± 1.19 / 76.69 ± 0.89</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="da-rank">2.15</td> <!-- Danish rank -->
   <td class="no-rank">2.44</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
   <td class="is-rank">3.67</td> <!-- Icelandic rank -->
   <td class="de-rank">1.81</td> <!-- German rank -->
   <td class="nl-rank">2.52</td> <!-- Dutch rank -->
   <td class="en-rank">1.70</td> <!-- English rank -->
   <td class="da ner">49.17 ± 2.72 / 34.74 ± 2.27</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 1.63 / 66.73 ± 1.63</td> <!-- Angry Tweets -->
   <td class="da la">32.04 ± 2.30 / 64.63 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da rc">58.52 ± 0.97 / 66.15 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.83 ± 0.63 / 21.53 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">65.77 ± 2.06 / 74.26 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">77.56 ± 1.97 / 85.02 ± 1.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">30.34 ± 1.47 / 46.85 ± 1.17</td> <!-- HellaSwag-da -->
   <td class="no ner">62.52 ± 2.14 / 49.42 ± 3.83</td> <!-- NorNE-nb -->
   <td class="no ner">61.55 ± 1.68 / 47.53 ± 3.65</td> <!-- NorNE-nn -->
   <td class="no sent">52.09 ± 3.90 / 65.72 ± 4.14</td> <!-- NoReC -->
   <td class="no summ">64.70 ± 0.79 / 17.10 ± 1.35</td> <!-- No Sammendrag -->
   <td class="no la">21.99 ± 2.17 / 58.21 ± 2.38</td> <!-- ScaLA-nb -->
   <td class="no la">16.84 ± 2.07 / 51.76 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no rc">47.30 ± 4.17 / 72.60 ± 3.24</td> <!-- NorQuAD -->
   <td class="no know">39.99 ± 1.01 / 54.90 ± 0.76</td> <!-- MMLU-no -->
   <td class="no reason">32.16 ± 1.91 / 48.12 ± 1.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.14 ± 2.49 / 37.43 ± 3.05</td> <!-- SUC3 -->
   <td class="sv sent">78.27 ± 1.32 / 77.65 ± 1.28</td> <!-- SweReC -->
   <td class="sv la">32.49 ± 1.94 / 64.28 ± 2.18</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.95 ± 0.96 / 66.56 ± 0.62</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.86 ± 0.29 / 19.67 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">43.62 ± 0.82 / 57.61 ± 0.65</td> <!-- MMLU-sv -->
   <td class="sv reason">28.84 ± 2.65 / 45.75 ± 2.13</td> <!-- HellaSwag-sv -->
   <td class="is ner">42.15 ± 2.74 / 33.52 ± 3.32</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.49 ± 1.81 / 47.31 ± 3.24</td> <!-- ScaLA-is -->
   <td class="is rc">27.51 ± 3.63 / 56.11 ± 1.65</td> <!-- NQiI -->
   <td class="is summ">66.89 ± 0.34 / 19.60 ± 0.89</td> <!-- RRN -->
   <td class="is know">19.27 ± 1.47 / 39.42 ± 1.10</td> <!-- ARC-is -->
   <td class="is reason">9.45 ± 2.76 / 54.44 ± 1.24</td> <!-- Winogrande-is -->
   <td class="de ner">57.82 ± 1.85 / 43.22 ± 2.36</td> <!-- GermEval -->
   <td class="de sent">59.45 ± 1.95 / 72.95 ± 1.33</td> <!-- SB10k -->
   <td class="de la">36.75 ± 2.58 / 67.88 ± 1.50</td> <!-- ScaLA-de -->
   <td class="de rc">33.55 ± 2.29 / 63.95 ± 2.83</td> <!-- GermanQuAD -->
   <td class="de summ">69.37 ± 0.84 / 28.13 ± 2.16</td> <!-- MLSum -->
   <td class="de know">50.96 ± 0.60 / 63.17 ± 0.44</td> <!-- MMLU-de -->
   <td class="de reason">39.28 ± 2.50 / 52.23 ± 2.22</td> <!-- HellaSwag-de -->
   <td class="nl ner">62.16 ± 1.09 / 45.76 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.92 ± 1.08 / 24.28 ± 0.76</td> <!-- Dutch Social -->
   <td class="nl la">32.76 ± 2.94 / 65.17 ± 2.79</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.87 ± 0.92 / 72.57 ± 0.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.39 ± 0.73 / 20.83 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">46.17 ± 0.64 / 59.57 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">33.31 ± 1.83 / 49.12 ± 1.64</td> <!-- HellaSwag-nl -->
   <td class="en ner">67.43 ± 0.90 / 60.40 ± 1.08</td> <!-- CoNLL-en -->
   <td class="en sent">68.55 ± 1.35 / 69.63 ± 0.98</td> <!-- SST5 -->
   <td class="en la">39.75 ± 2.28 / 69.19 ± 1.17</td> <!-- ScaLA-en -->
   <td class="en rc">65.93 ± 2.77 / 82.86 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">70.90 ± 0.34 / 25.88 ± 0.75</td> <!-- CNN-DailyMail -->
   <td class="en know">59.14 ± 1.02 / 69.28 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">57.88 ± 2.80 / 67.75 ± 2.34</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da-rank">2.31</td> <!-- Danish rank -->
   <td class="no-rank">2.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.19</td> <!-- Swedish rank -->
   <td class="is-rank">3.47</td> <!-- Icelandic rank -->
   <td class="de-rank">1.97</td> <!-- German rank -->
   <td class="nl-rank">2.43</td> <!-- Dutch rank -->
   <td class="en-rank">1.91</td> <!-- English rank -->
   <td class="da ner">47.68 ± 2.50 / 32.67 ± 2.45</td> <!-- DANSK -->
   <td class="da sent">49.71 ± 1.43 / 64.00 ± 1.96</td> <!-- Angry Tweets -->
   <td class="da la">25.48 ± 2.83 / 58.45 ± 2.63</td> <!-- ScaLA-da -->
   <td class="da rc">60.31 ± 1.24 / 65.79 ± 0.84</td> <!-- ScandiQA-da -->
   <td class="da summ">64.74 ± 0.50 / 17.82 ± 0.98</td> <!-- Nordjylland-News -->
   <td class="da know">57.60 ± 1.58 / 67.81 ± 1.23</td> <!-- Danske Talemaader -->
   <td class="da know">65.98 ± 1.72 / 77.34 ± 1.16</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.65 ± 2.52 / 45.11 ± 2.33</td> <!-- HellaSwag-da -->
   <td class="no ner">64.62 ± 1.26 / 53.50 ± 3.27</td> <!-- NorNE-nb -->
   <td class="no ner">65.10 ± 1.86 / 56.43 ± 2.58</td> <!-- NorNE-nn -->
   <td class="no sent">52.87 ± 1.18 / 68.71 ± 1.01</td> <!-- NoReC -->
   <td class="no summ">63.88 ± 1.12 / 16.54 ± 1.58</td> <!-- No Sammendrag -->
   <td class="no la">28.34 ± 3.26 / 58.57 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">22.40 ± 3.12 / 53.51 ± 5.42</td> <!-- ScaLA-nn -->
   <td class="no rc">53.20 ± 3.15 / 75.98 ± 2.62</td> <!-- NorQuAD -->
   <td class="no know">35.80 ± 0.97 / 51.22 ± 0.67</td> <!-- MMLU-no -->
   <td class="no reason">30.31 ± 1.70 / 46.84 ± 1.59</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.49 / 44.62 ± 4.10</td> <!-- SUC3 -->
   <td class="sv sent">79.96 ± 0.93 / 75.75 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">31.70 ± 4.07 / 59.28 ± 5.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.33 ± 0.88 / 65.24 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.07 ± 0.28 / 18.94 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">37.48 ± 0.64 / 52.46 ± 0.52</td> <!-- MMLU-sv -->
   <td class="sv reason">31.27 ± 1.39 / 47.97 ± 1.30</td> <!-- HellaSwag-sv -->
   <td class="is ner">52.57 ± 2.04 / 36.81 ± 2.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.87 ± 2.28 / 40.95 ± 4.97</td> <!-- ScaLA-is -->
   <td class="is rc">30.12 ± 4.65 / 57.81 ± 4.78</td> <!-- NQiI -->
   <td class="is summ">66.17 ± 0.86 / 18.71 ± 0.89</td> <!-- RRN -->
   <td class="is know">25.93 ± 1.51 / 44.54 ± 1.14</td> <!-- ARC-is -->
   <td class="is reason">8.48 ± 2.66 / 53.76 ± 1.54</td> <!-- Winogrande-is -->
   <td class="de ner">60.46 ± 1.26 / 47.72 ± 1.69</td> <!-- GermEval -->
   <td class="de sent">58.57 ± 2.53 / 71.30 ± 1.70</td> <!-- SB10k -->
   <td class="de la">26.25 ± 5.90 / 61.41 ± 3.94</td> <!-- ScaLA-de -->
   <td class="de rc">34.85 ± 3.43 / 64.05 ± 3.68</td> <!-- GermanQuAD -->
   <td class="de summ">69.58 ± 1.37 / 28.95 ± 2.96</td> <!-- MLSum -->
   <td class="de know">38.77 ± 0.95 / 53.99 ± 0.67</td> <!-- MMLU-de -->
   <td class="de reason">34.29 ± 1.05 / 49.79 ± 0.88</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.79 ± 1.96 / 45.48 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.83 / 37.12 ± 2.19</td> <!-- Dutch Social -->
   <td class="nl la">32.97 ± 2.68 / 58.52 ± 2.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.89 ± 1.06 / 74.73 ± 1.02</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.29 ± 1.29 / 20.14 ± 1.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.44 ± 1.33 / 53.68 ± 1.01</td> <!-- MMLU-nl -->
   <td class="nl reason">30.88 ± 2.27 / 47.18 ± 1.81</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.86 ± 2.10 / 62.68 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">66.76 ± 0.72 / 68.58 ± 0.72</td> <!-- SST5 -->
   <td class="en la">30.96 ± 2.46 / 61.29 ± 3.61</td> <!-- ScaLA-en -->
   <td class="en rc">71.39 ± 2.20 / 84.24 ± 1.55</td> <!-- SQuAD -->
   <td class="en summ">67.93 ± 0.44 / 22.00 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">52.47 ± 0.85 / 64.25 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">43.95 ± 3.26 / 57.04 ± 2.74</td> <!-- HellaSwag -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>12.11.0</td> <!-- NorNE-nb version -->
   <td>12.11.0</td> <!-- NorNE-nn version -->
   <td>12.11.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>12.11.0</td> <!-- ScaLA-nb version -->
   <td>12.11.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.11.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.11.0</td> <!-- SST5 version -->
   <td>12.11.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
   <td class="is-rank">3.46</td> <!-- Icelandic rank -->
   <td class="de-rank">2.09</td> <!-- German rank -->
   <td class="nl-rank">2.50</td> <!-- Dutch rank -->
   <td class="en-rank">1.92</td> <!-- English rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da rc">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
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
   <td class="no rc">42.90 ± 3.57 / 69.90 ± 3.17</td> <!-- NorQuAD -->
   <td class="no know">33.44 ± 0.67 / 48.76 ± 0.58</td> <!-- MMLU-no -->
   <td class="no reason">30.91 ± 1.88 / 45.85 ± 1.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.60 ± 0.07 / 19.13 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">33.54 ± 1.40 / 49.20 ± 1.13</td> <!-- MMLU-sv -->
   <td class="sv reason">30.32 ± 2.27 / 45.96 ± 1.87</td> <!-- HellaSwag-sv -->
   <td class="is ner">61.69 ± 2.17 / 41.25 ± 3.12</td> <!-- MIM-GOLD-NER -->
   <td class="is la">6.10 ± 1.61 / 48.74 ± 3.05</td> <!-- ScaLA-is -->
   <td class="is rc">31.52 ± 2.08 / 58.96 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">66.98 ± 1.04 / 19.84 ± 1.97</td> <!-- RRN -->
   <td class="is know">25.16 ± 1.55 / 43.57 ± 1.26</td> <!-- ARC-is -->
   <td class="is reason">1.50 ± 1.22 / 48.33 ± 1.21</td> <!-- Winogrande-is -->
   <td class="de ner">68.18 ± 0.95 / 57.72 ± 1.15</td> <!-- GermEval -->
   <td class="de sent">58.33 ± 2.83 / 69.31 ± 3.16</td> <!-- SB10k -->
   <td class="de la">29.12 ± 3.17 / 63.60 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 1.99 / 56.42 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.23 ± 0.49 / 16.56 ± 0.94</td> <!-- MLSum -->
   <td class="de know">38.44 ± 0.81 / 53.38 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">37.69 ± 1.00 / 51.24 ± 0.73</td> <!-- HellaSwag-de -->
   <td class="nl ner">68.72 ± 1.81 / 54.89 ± 2.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.67 ± 2.51 / 41.36 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">32.91 ± 2.56 / 64.93 ± 1.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.36 ± 1.31 / 67.50 ± 0.69</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.82 / 18.19 ± 1.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.18 ± 1.31 / 51.68 ± 1.05</td> <!-- MMLU-nl -->
   <td class="nl reason">33.91 ± 1.71 / 48.01 ± 1.47</td> <!-- HellaSwag-nl -->
   <td class="en ner">75.02 ± 1.31 / 69.47 ± 1.18</td> <!-- CoNLL-en -->
   <td class="en sent">67.64 ± 1.12 / 71.04 ± 1.17</td> <!-- SST5 -->
   <td class="en la">32.29 ± 3.05 / 64.85 ± 2.07</td> <!-- ScaLA-en -->
   <td class="en rc">54.84 ± 2.22 / 79.10 ± 1.10</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
   <td class="is-rank">4.05</td> <!-- Icelandic rank -->
   <td class="de-rank">1.93</td> <!-- German rank -->
   <td class="nl-rank">2.24</td> <!-- Dutch rank -->
   <td class="en-rank">1.73</td> <!-- English rank -->
   <td class="da ner">51.32 ± 3.82 / 25.54 ± 2.10</td> <!-- DANSK -->
   <td class="da sent">52.00 ± 1.67 / 66.25 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">18.48 ± 2.44 / 52.18 ± 4.28</td> <!-- ScaLA-da -->
   <td class="da rc">52.43 ± 1.19 / 62.08 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="da summ">66.18 ± 0.84 / 21.10 ± 0.69</td> <!-- Nordjylland-News -->
   <td class="da know">41.32 ± 1.11 / 55.43 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">52.24 ± 1.55 / 68.01 ± 1.05</td> <!-- Danish Citizen Tests -->
   <td class="da reason">37.67 ± 0.80 / 53.26 ± 0.60</td> <!-- HellaSwag-da -->
   <td class="no ner">66.55 ± 2.12 / 39.28 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">63.63 ± 1.62 / 37.25 ± 3.49</td> <!-- NorNE-nn -->
   <td class="no sent">38.61 ± 2.28 / 51.46 ± 2.62</td> <!-- NoReC -->
   <td class="no summ">64.48 ± 0.61 / 17.46 ± 0.76</td> <!-- No Sammendrag -->
   <td class="no la">15.80 ± 2.22 / 51.42 ± 3.79</td> <!-- ScaLA-nb -->
   <td class="no la">12.30 ± 2.38 / 51.96 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no rc">43.26 ± 2.53 / 71.49 ± 2.01</td> <!-- NorQuAD -->
   <td class="no know">36.48 ± 0.85 / 52.32 ± 0.62</td> <!-- MMLU-no -->
   <td class="no reason">35.85 ± 1.48 / 51.83 ± 1.11</td> <!-- HellaSwag-no -->
   <td class="sv ner">57.38 ± 1.93 / 29.69 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">78.43 ± 0.93 / 74.54 ± 2.40</td> <!-- SweReC -->
   <td class="sv la">14.52 ± 2.43 / 45.18 ± 4.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.14 ± 1.81 / 63.00 ± 0.50</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.69 ± 0.22 / 19.95 ± 0.16</td> <!-- SweDN -->
   <td class="sv know">37.32 ± 0.70 / 52.95 ± 0.50</td> <!-- MMLU-sv -->
   <td class="sv reason">38.28 ± 1.31 / 53.70 ± 0.97</td> <!-- HellaSwag-sv -->
   <td class="is ner">28.98 ± 2.63 / 21.75 ± 1.89</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.93 ± 1.06 / 49.69 ± 2.65</td> <!-- ScaLA-is -->
   <td class="is rc">24.72 ± 2.22 / 54.41 ± 1.43</td> <!-- NQiI -->
   <td class="is summ">63.45 ± 1.92 / 16.81 ± 2.23</td> <!-- RRN -->
   <td class="is know">10.97 ± 1.13 / 33.51 ± 0.81</td> <!-- ARC-is -->
   <td class="is reason">4.23 ± 1.80 / 49.31 ± 0.84</td> <!-- Winogrande-is -->
   <td class="de ner">61.29 ± 1.06 / 39.58 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">59.19 ± 1.49 / 71.64 ± 1.07</td> <!-- SB10k -->
   <td class="de la">33.31 ± 3.00 / 64.35 ± 2.80</td> <!-- ScaLA-de -->
   <td class="de rc">22.29 ± 2.02 / 57.68 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">69.05 ± 1.11 / 26.68 ± 3.04</td> <!-- MLSum -->
   <td class="de know">44.87 ± 0.70 / 58.71 ± 0.53</td> <!-- MMLU-de -->
   <td class="de reason">63.66 ± 0.91 / 72.68 ± 0.68</td> <!-- HellaSwag-de -->
   <td class="nl ner">62.07 ± 1.67 / 37.68 ± 1.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.09 ± 1.67 / 31.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">35.14 ± 2.33 / 66.66 ± 1.50</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.48 / 68.82 ± 0.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">74.40 ± 0.20 / 31.66 ± 0.46</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">46.76 ± 0.71 / 60.01 ± 0.54</td> <!-- MMLU-nl -->
   <td class="nl reason">60.36 ± 0.88 / 70.23 ± 0.64</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.61 ± 1.39 / 47.49 ± 1.37</td> <!-- CoNLL-en -->
   <td class="en sent">68.71 ± 0.63 / 68.49 ± 1.70</td> <!-- SST5 -->
   <td class="en la">34.72 ± 2.23 / 66.80 ± 1.30</td> <!-- ScaLA-en -->
   <td class="en rc">57.90 ± 2.96 / 80.48 ± 1.34</td> <!-- SQuAD -->
   <td class="en summ">71.92 ± 0.17 / 29.79 ± 0.15</td> <!-- CNN-DailyMail -->
   <td class="en know">56.93 ± 0.67 / 67.67 ± 0.51</td> <!-- MMLU -->
   <td class="en reason">74.42 ± 0.88 / 80.74 ± 0.65</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.33</td> <!-- Danish rank -->
   <td class="no-rank">2.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.29</td> <!-- Swedish rank -->
   <td class="is-rank">3.53</td> <!-- Icelandic rank -->
   <td class="de-rank">2.13</td> <!-- German rank -->
   <td class="nl-rank">2.59</td> <!-- Dutch rank -->
   <td class="en-rank">2.04</td> <!-- English rank -->
   <td class="da ner">46.31 ± 3.22 / 29.09 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 1.47 / 66.35 ± 1.70</td> <!-- Angry Tweets -->
   <td class="da la">25.70 ± 4.59 / 55.65 ± 5.87</td> <!-- ScaLA-da -->
   <td class="da rc">59.79 ± 1.21 / 65.44 ± 0.76</td> <!-- ScandiQA-da -->
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
   <td class="no rc">53.35 ± 4.33 / 74.98 ± 3.70</td> <!-- NorQuAD -->
   <td class="no know">33.02 ± 1.35 / 49.25 ± 1.04</td> <!-- MMLU-no -->
   <td class="no reason">24.93 ± 3.13 / 42.47 ± 2.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.81 ± 0.24 / 18.56 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">35.86 ± 0.90 / 51.39 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">26.49 ± 1.89 / 44.41 ± 1.56</td> <!-- HellaSwag-sv -->
   <td class="is ner">48.70 ± 3.02 / 34.52 ± 2.66</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.49 ± 2.51 / 43.40 ± 4.41</td> <!-- ScaLA-is -->
   <td class="is rc">29.56 ± 5.47 / 55.53 ± 5.79</td> <!-- NQiI -->
   <td class="is summ">66.34 ± 1.09 / 19.13 ± 0.96</td> <!-- RRN -->
   <td class="is know">26.78 ± 1.59 / 45.17 ± 1.12</td> <!-- ARC-is -->
   <td class="is reason">7.41 ± 3.26 / 52.13 ± 1.97</td> <!-- Winogrande-is -->
   <td class="de ner">56.00 ± 1.94 / 43.49 ± 2.05</td> <!-- GermEval -->
   <td class="de sent">56.40 ± 3.89 / 70.17 ± 2.91</td> <!-- SB10k -->
   <td class="de la">22.01 ± 5.17 / 56.97 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de rc">35.39 ± 2.49 / 64.61 ± 2.42</td> <!-- GermanQuAD -->
   <td class="de summ">68.92 ± 0.99 / 26.93 ± 2.01</td> <!-- MLSum -->
   <td class="de know">38.12 ± 0.75 / 53.52 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">31.37 ± 1.37 / 47.65 ± 1.09</td> <!-- HellaSwag-de -->
   <td class="nl ner">62.26 ± 2.20 / 42.41 ± 2.02</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.45 ± 2.69 / 33.45 ± 1.99</td> <!-- Dutch Social -->
   <td class="nl la">30.30 ± 3.94 / 62.28 ± 2.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.99 ± 1.00 / 73.73 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.17 ± 1.24 / 18.63 ± 1.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.38 ± 0.86 / 52.08 ± 0.66</td> <!-- MMLU-nl -->
   <td class="nl reason">28.33 ± 2.31 / 45.29 ± 1.78</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.31 ± 2.09 / 58.68 ± 1.95</td> <!-- CoNLL-en -->
   <td class="en sent">64.30 ± 0.65 / 69.26 ± 0.50</td> <!-- SST5 -->
   <td class="en la">28.18 ± 3.96 / 58.97 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en rc">70.38 ± 3.51 / 82.95 ± 2.38</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.24</td> <!-- Danish rank -->
   <td class="no-rank">2.57</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.38</td> <!-- Swedish rank -->
   <td class="is-rank">3.77</td> <!-- Icelandic rank -->
   <td class="de-rank">2.05</td> <!-- German rank -->
   <td class="nl-rank">2.46</td> <!-- Dutch rank -->
   <td class="en-rank">1.95</td> <!-- English rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da rc">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
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
   <td class="no rc">34.48 ± 2.13 / 65.43 ± 2.07</td> <!-- NorQuAD -->
   <td class="no know">28.39 ± 1.76 / 45.59 ± 1.28</td> <!-- MMLU-no -->
   <td class="no reason">35.19 ± 3.28 / 50.12 ± 3.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.35 ± 0.32 / 24.05 ± 0.66</td> <!-- SweDN -->
   <td class="sv know">32.30 ± 2.48 / 48.98 ± 1.96</td> <!-- MMLU-sv -->
   <td class="sv reason">38.78 ± 5.70 / 52.89 ± 4.91</td> <!-- HellaSwag-sv -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is rc">22.48 ± 4.43 / 55.51 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">5.19 ± 3.15 / 28.44 ± 2.45</td> <!-- ARC-is -->
   <td class="is reason">12.90 ± 6.92 / 56.88 ± 3.57</td> <!-- Winogrande-is -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de rc">25.22 ± 3.84 / 60.93 ± 2.99</td> <!-- GermanQuAD -->
   <td class="de summ">67.31 ± 1.05 / 24.72 ± 2.95</td> <!-- MLSum -->
   <td class="de know">35.84 ± 2.16 / 51.64 ± 1.56</td> <!-- MMLU-de -->
   <td class="de reason">49.13 ± 2.71 / 61.68 ± 2.03</td> <!-- HellaSwag-de -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.94 ± 1.12 / 70.12 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="nl summ">71.20 ± 0.46 / 23.47 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.23 ± 2.86 / 54.77 ± 2.16</td> <!-- MMLU-nl -->
   <td class="nl reason">47.87 ± 2.49 / 60.78 ± 1.85</td> <!-- HellaSwag-nl -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en rc">52.69 ± 2.21 / 76.37 ± 1.27</td> <!-- SQuAD -->
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
   <td>9.3.2</td> <!-- ARC-is version -->
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
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.48</td> <!-- Swedish rank -->
   <td class="is-rank">3.87</td> <!-- Icelandic rank -->
   <td class="de-rank">2.06</td> <!-- German rank -->
   <td class="nl-rank">2.41</td> <!-- Dutch rank -->
   <td class="en-rank">1.98</td> <!-- English rank -->
   <td class="da ner">52.61 ± 1.77 / 33.64 ± 2.67</td> <!-- DANSK -->
   <td class="da sent">49.81 ± 1.43 / 66.32 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">19.64 ± 1.63 / 54.22 ± 2.32</td> <!-- ScaLA-da -->
   <td class="da rc">48.03 ± 1.24 / 57.94 ± 1.02</td> <!-- ScandiQA-da -->
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
   <td class="no rc">38.34 ± 2.39 / 69.54 ± 1.96</td> <!-- NorQuAD -->
   <td class="no know">27.33 ± 0.72 / 45.16 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">41.59 ± 2.61 / 56.02 ± 2.08</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.09 ± 0.17 / 19.64 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">31.76 ± 0.89 / 48.64 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">45.84 ± 1.47 / 59.27 ± 1.16</td> <!-- HellaSwag-sv -->
   <td class="is ner">56.71 ± 1.98 / 46.71 ± 5.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.44 ± 2.02 / 50.18 ± 1.14</td> <!-- ScaLA-is -->
   <td class="is rc">21.55 ± 2.79 / 54.79 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">65.39 ± 0.80 / 18.24 ± 1.00</td> <!-- RRN -->
   <td class="is know">9.11 ± 0.92 / 32.06 ± 0.70</td> <!-- ARC-is -->
   <td class="is reason">3.30 ± 2.81 / 44.40 ± 1.61</td> <!-- Winogrande-is -->
   <td class="de ner">64.38 ± 1.60 / 50.26 ± 2.53</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.45 / 69.32 ± 1.02</td> <!-- SB10k -->
   <td class="de la">26.03 ± 2.23 / 61.88 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">25.68 ± 2.81 / 62.48 ± 2.93</td> <!-- GermanQuAD -->
   <td class="de summ">68.16 ± 0.95 / 24.52 ± 2.45</td> <!-- MLSum -->
   <td class="de know">33.84 ± 1.54 / 50.24 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">50.99 ± 0.99 / 63.11 ± 0.75</td> <!-- HellaSwag-de -->
   <td class="nl ner">64.25 ± 2.23 / 46.52 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.66 ± 1.99 / 39.45 ± 1.52</td> <!-- Dutch Social -->
   <td class="nl la">28.59 ± 1.48 / 61.24 ± 1.46</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.64 ± 0.86 / 68.04 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.57 / 19.51 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.37 ± 1.30 / 51.43 ± 0.96</td> <!-- MMLU-nl -->
   <td class="nl reason">47.50 ± 1.75 / 60.41 ± 1.32</td> <!-- HellaSwag-nl -->
   <td class="en ner">70.62 ± 0.90 / 58.92 ± 2.15</td> <!-- CoNLL-en -->
   <td class="en sent">67.78 ± 1.03 / 72.29 ± 0.47</td> <!-- SST5 -->
   <td class="en la">30.99 ± 2.94 / 62.20 ± 2.56</td> <!-- ScaLA-en -->
   <td class="en rc">49.56 ± 2.85 / 76.72 ± 1.15</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.53</td> <!-- Danish rank -->
   <td class="no-rank">2.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="is-rank">4.19</td> <!-- Icelandic rank -->
   <td class="de-rank">1.98</td> <!-- German rank -->
   <td class="nl-rank">2.27</td> <!-- Dutch rank -->
   <td class="en-rank">1.84</td> <!-- English rank -->
   <td class="da ner">44.58 ± 2.62 / 33.50 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.36 / 64.63 ± 1.18</td> <!-- Angry Tweets -->
   <td class="da la">19.20 ± 2.44 / 53.44 ± 4.36</td> <!-- ScaLA-da -->
   <td class="da rc">58.41 ± 1.36 / 63.32 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="da summ">65.64 ± 0.99 / 21.12 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">32.05 ± 2.18 / 47.54 ± 1.78</td> <!-- Danske Talemaader -->
   <td class="da know">47.42 ± 1.74 / 65.02 ± 1.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.73 ± 1.32 / 46.04 ± 1.04</td> <!-- HellaSwag-da -->
   <td class="no ner">49.94 ± 2.13 / 46.49 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">52.17 ± 1.02 / 46.44 ± 2.72</td> <!-- NorNE-nn -->
   <td class="no sent">53.27 ± 1.54 / 66.73 ± 1.31</td> <!-- NoReC -->
   <td class="no summ">63.01 ± 1.50 / 15.82 ± 1.50</td> <!-- No Sammendrag -->
   <td class="no la">17.22 ± 3.50 / 50.42 ± 5.01</td> <!-- ScaLA-nb -->
   <td class="no la">12.01 ± 2.47 / 47.98 ± 4.37</td> <!-- ScaLA-nn -->
   <td class="no rc">45.04 ± 3.42 / 69.52 ± 2.79</td> <!-- NorQuAD -->
   <td class="no know">24.31 ± 1.12 / 42.68 ± 0.87</td> <!-- MMLU-no -->
   <td class="no reason">30.34 ± 1.41 / 47.38 ± 1.10</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.80 ± 2.36 / 34.91 ± 2.67</td> <!-- SUC3 -->
   <td class="sv sent">75.92 ± 2.44 / 75.77 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">24.84 ± 2.78 / 59.88 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.71 ± 1.65 / 62.01 ± 1.64</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.65 ± 0.52 / 18.25 ± 0.41</td> <!-- SweDN -->
   <td class="sv know">26.71 ± 1.53 / 44.61 ± 1.21</td> <!-- MMLU-sv -->
   <td class="sv reason">30.43 ± 0.92 / 47.06 ± 0.83</td> <!-- HellaSwag-sv -->
   <td class="is ner">37.82 ± 3.63 / 32.97 ± 3.97</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.12 ± 1.31 / 33.78 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">21.59 ± 2.22 / 47.09 ± 1.09</td> <!-- NQiI -->
   <td class="is summ">62.35 ± 3.34 / 16.15 ± 1.66</td> <!-- RRN -->
   <td class="is know">6.54 ± 1.30 / 28.63 ± 1.24</td> <!-- ARC-is -->
   <td class="is reason">1.83 ± 3.53 / 49.23 ± 2.07</td> <!-- Winogrande-is -->
   <td class="de ner">52.61 ± 1.79 / 42.68 ± 2.71</td> <!-- GermEval -->
   <td class="de sent">61.70 ± 1.45 / 74.22 ± 1.00</td> <!-- SB10k -->
   <td class="de la">23.89 ± 4.13 / 57.16 ± 4.48</td> <!-- ScaLA-de -->
   <td class="de rc">33.72 ± 1.25 / 62.41 ± 1.53</td> <!-- GermanQuAD -->
   <td class="de summ">70.32 ± 0.87 / 31.24 ± 2.42</td> <!-- MLSum -->
   <td class="de know">39.82 ± 0.77 / 54.72 ± 0.59</td> <!-- MMLU-de -->
   <td class="de reason">53.82 ± 1.15 / 64.95 ± 0.94</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.21 ± 1.37 / 42.13 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.72 ± 2.18 / 39.38 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">40.85 ± 4.16 / 67.34 ± 3.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.41 ± 0.99 / 74.19 ± 0.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.70 ± 0.37 / 19.34 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">39.74 ± 0.95 / 54.61 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">54.37 ± 0.74 / 65.48 ± 0.65</td> <!-- HellaSwag-nl -->
   <td class="en ner">53.37 ± 1.98 / 49.01 ± 1.29</td> <!-- CoNLL-en -->
   <td class="en sent">68.88 ± 1.24 / 70.64 ± 0.92</td> <!-- SST5 -->
   <td class="en la">37.17 ± 3.96 / 67.71 ± 2.64</td> <!-- ScaLA-en -->
   <td class="en rc">69.02 ± 2.58 / 83.72 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">68.38 ± 0.45 / 24.50 ± 0.64</td> <!-- CNN-DailyMail -->
   <td class="en know">51.00 ± 1.07 / 62.95 ± 0.81</td> <!-- MMLU -->
   <td class="en reason">78.18 ± 1.10 / 83.30 ± 0.85</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da-rank">2.48</td> <!-- Danish rank -->
   <td class="no-rank">2.70</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
   <td class="is-rank">3.69</td> <!-- Icelandic rank -->
   <td class="de-rank">2.09</td> <!-- German rank -->
   <td class="nl-rank">2.78</td> <!-- Dutch rank -->
   <td class="en-rank">2.13</td> <!-- English rank -->
   <td class="da ner">19.59 ± 2.54 / 15.47 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">46.55 ± 1.89 / 59.52 ± 3.56</td> <!-- Angry Tweets -->
   <td class="da la">32.64 ± 2.91 / 63.84 ± 1.69</td> <!-- ScaLA-da -->
   <td class="da rc">59.40 ± 1.02 / 64.81 ± 0.91</td> <!-- ScandiQA-da -->
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
   <td class="no rc">52.68 ± 3.58 / 75.16 ± 2.44</td> <!-- NorQuAD -->
   <td class="no know">39.96 ± 0.97 / 53.03 ± 0.89</td> <!-- MMLU-no -->
   <td class="no reason">27.82 ± 4.59 / 41.21 ± 4.09</td> <!-- HellaSwag-no -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.44 ± 0.29 / 18.70 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">39.94 ± 1.17 / 53.25 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">25.96 ± 3.94 / 40.33 ± 3.17</td> <!-- HellaSwag-sv -->
   <td class="is ner">30.61 ± 4.61 / 25.80 ± 3.57</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.60 ± 1.68 / 38.26 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">32.22 ± 3.19 / 55.22 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.03 ± 1.82 / 18.15 ± 2.24</td> <!-- RRN -->
   <td class="is know">32.53 ± 0.82 / 48.03 ± 0.80</td> <!-- ARC-is -->
   <td class="is reason">1.14 ± 1.26 / 39.92 ± 1.92</td> <!-- Winogrande-is -->
   <td class="de ner">39.88 ± 2.56 / 35.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">56.23 ± 3.17 / 68.87 ± 2.73</td> <!-- SB10k -->
   <td class="de la">32.71 ± 1.60 / 64.55 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">36.58 ± 2.81 / 64.92 ± 2.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.41 ± 1.20 / 29.96 ± 3.00</td> <!-- MLSum -->
   <td class="de know">41.56 ± 0.82 / 54.79 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">30.77 ± 2.85 / 43.20 ± 2.53</td> <!-- HellaSwag-de -->
   <td class="nl ner">47.75 ± 2.33 / 35.64 ± 1.89</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.68 ± 0.61 / 26.25 ± 1.18</td> <!-- Dutch Social -->
   <td class="nl la">28.28 ± 2.48 / 62.81 ± 1.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.49 ± 1.15 / 73.19 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.60 ± 1.18 / 19.95 ± 1.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.19 ± 0.97 / 55.52 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">31.45 ± 2.79 / 44.15 ± 3.09</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.20 ± 3.34 / 41.96 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.88 ± 2.24 / 66.49 ± 0.81</td> <!-- SST5 -->
   <td class="en la">35.75 ± 2.65 / 66.41 ± 2.26</td> <!-- ScaLA-en -->
   <td class="en rc">69.40 ± 4.29 / 82.46 ± 2.86</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="is-rank">4.17</td> <!-- Icelandic rank -->
   <td class="de-rank">1.87</td> <!-- German rank -->
   <td class="nl-rank">2.44</td> <!-- Dutch rank -->
   <td class="en-rank">1.83</td> <!-- English rank -->
   <td class="da ner">47.08 ± 3.39 / 32.34 ± 2.97</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.21 / 63.47 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">8.41 ± 2.40 / 37.31 ± 1.66</td> <!-- ScaLA-da -->
   <td class="da rc">58.83 ± 0.73 / 63.96 ± 0.56</td> <!-- ScandiQA-da -->
   <td class="da summ">65.03 ± 0.98 / 20.21 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">36.64 ± 1.30 / 49.92 ± 1.19</td> <!-- Danske Talemaader -->
   <td class="da know">39.24 ± 1.63 / 59.45 ± 1.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">27.29 ± 1.22 / 45.01 ± 0.99</td> <!-- HellaSwag-da -->
   <td class="no ner">60.94 ± 2.30 / 53.33 ± 3.53</td> <!-- NorNE-nb -->
   <td class="no ner">59.61 ± 1.37 / 50.84 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">35.73 ± 1.26 / 50.42 ± 1.67</td> <!-- NoReC -->
   <td class="no summ">62.45 ± 1.72 / 15.67 ± 1.26</td> <!-- No Sammendrag -->
   <td class="no la">6.18 ± 1.69 / 35.40 ± 1.06</td> <!-- ScaLA-nb -->
   <td class="no la">4.00 ± 1.01 / 36.17 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no rc">46.52 ± 2.15 / 71.95 ± 1.63</td> <!-- NorQuAD -->
   <td class="no know">20.14 ± 1.32 / 38.69 ± 0.99</td> <!-- MMLU-no -->
   <td class="no reason">27.50 ± 1.61 / 44.60 ± 1.39</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.04 ± 1.22 / 43.93 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 0.85 / 67.87 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">7.54 ± 2.52 / 35.42 ± 1.33</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.60 ± 0.59 / 63.65 ± 0.30</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.00 ± 0.55 / 18.11 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">20.97 ± 0.82 / 39.72 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">28.96 ± 2.18 / 46.32 ± 1.64</td> <!-- HellaSwag-sv -->
   <td class="is ner">47.16 ± 2.83 / 38.60 ± 4.04</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.84 ± 1.27 / 40.06 ± 3.79</td> <!-- ScaLA-is -->
   <td class="is rc">21.75 ± 2.21 / 48.25 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 2.91 / 14.91 ± 1.85</td> <!-- RRN -->
   <td class="is know">3.70 ± 1.01 / 27.71 ± 0.66</td> <!-- ARC-is -->
   <td class="is reason">-3.24 ± 3.16 / 49.96 ± 2.38</td> <!-- Winogrande-is -->
   <td class="de ner">58.69 ± 1.32 / 45.79 ± 2.60</td> <!-- GermEval -->
   <td class="de sent">56.49 ± 2.69 / 70.39 ± 2.14</td> <!-- SB10k -->
   <td class="de la">30.04 ± 2.28 / 62.58 ± 2.34</td> <!-- ScaLA-de -->
   <td class="de rc">36.36 ± 1.07 / 66.01 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">69.07 ± 1.43 / 28.50 ± 3.72</td> <!-- MLSum -->
   <td class="de know">32.49 ± 1.21 / 48.62 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">55.40 ± 1.43 / 65.83 ± 1.23</td> <!-- HellaSwag-de -->
   <td class="nl ner">60.81 ± 1.94 / 46.59 ± 3.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.63 / 24.82 ± 0.95</td> <!-- Dutch Social -->
   <td class="nl la">31.12 ± 2.35 / 64.29 ± 1.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.00 ± 1.23 / 74.60 ± 0.67</td> <!-- SQuAD-nl -->
   <td class="nl summ">72.90 ± 0.24 / 30.63 ± 0.42</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.37 ± 1.09 / 48.63 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">53.32 ± 1.89 / 64.30 ± 1.72</td> <!-- HellaSwag-nl -->
   <td class="en ner">61.14 ± 2.97 / 53.13 ± 1.91</td> <!-- CoNLL-en -->
   <td class="en sent">69.68 ± 0.65 / 67.92 ± 0.82</td> <!-- SST5 -->
   <td class="en la">32.57 ± 2.11 / 65.57 ± 1.69</td> <!-- ScaLA-en -->
   <td class="en rc">75.82 ± 1.63 / 87.24 ± 0.65</td> <!-- SQuAD -->
   <td class="en summ">68.14 ± 1.53 / 25.56 ± 0.98</td> <!-- CNN-DailyMail -->
   <td class="en know">40.73 ± 0.87 / 54.65 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">79.38 ± 0.82 / 84.41 ± 0.65</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da-rank">2.64</td> <!-- Danish rank -->
   <td class="no-rank">2.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.61</td> <!-- Swedish rank -->
   <td class="is-rank">4.11</td> <!-- Icelandic rank -->
   <td class="de-rank">2.23</td> <!-- German rank -->
   <td class="nl-rank">2.74</td> <!-- Dutch rank -->
   <td class="en-rank">1.75</td> <!-- English rank -->
   <td class="da ner">44.92 ± 3.05 / 32.65 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">49.31 ± 1.35 / 66.02 ± 1.10</td> <!-- Angry Tweets -->
   <td class="da la">10.14 ± 2.87 / 44.99 ± 4.82</td> <!-- ScaLA-da -->
   <td class="da rc">57.34 ± 0.99 / 63.24 ± 0.44</td> <!-- ScandiQA-da -->
   <td class="da summ">66.02 ± 0.75 / 20.91 ± 0.70</td> <!-- Nordjylland-News -->
   <td class="da know">33.71 ± 1.69 / 49.70 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">43.55 ± 3.67 / 62.50 ± 2.36</td> <!-- Danish Citizen Tests -->
   <td class="da reason">21.34 ± 1.27 / 39.77 ± 1.09</td> <!-- HellaSwag-da -->
   <td class="no ner">53.79 ± 1.52 / 46.58 ± 1.73</td> <!-- NorNE-nb -->
   <td class="no ner">56.13 ± 0.91 / 47.13 ± 2.04</td> <!-- NorNE-nn -->
   <td class="no sent">51.36 ± 2.53 / 66.19 ± 2.08</td> <!-- NoReC -->
   <td class="no summ">62.40 ± 1.11 / 13.68 ± 1.61</td> <!-- No Sammendrag -->
   <td class="no la">6.83 ± 2.54 / 38.36 ± 3.81</td> <!-- ScaLA-nb -->
   <td class="no la">8.09 ± 2.03 / 41.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no rc">48.01 ± 2.52 / 73.03 ± 1.99</td> <!-- NorQuAD -->
   <td class="no know">24.55 ± 0.94 / 42.12 ± 0.85</td> <!-- MMLU-no -->
   <td class="no reason">26.71 ± 1.68 / 44.15 ± 1.46</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.94 ± 2.91 / 35.67 ± 3.53</td> <!-- SUC3 -->
   <td class="sv sent">76.78 ± 1.63 / 78.27 ± 1.22</td> <!-- SweReC -->
   <td class="sv la">16.96 ± 2.77 / 55.03 ± 3.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.83 ± 1.02 / 63.13 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.09 ± 0.37 / 19.37 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">26.57 ± 1.18 / 44.19 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">24.62 ± 2.11 / 42.11 ± 1.50</td> <!-- HellaSwag-sv -->
   <td class="is ner">42.67 ± 3.13 / 35.40 ± 3.93</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.11 ± 1.45 / 34.61 ± 0.82</td> <!-- ScaLA-is -->
   <td class="is rc">22.25 ± 2.78 / 49.58 ± 2.19</td> <!-- NQiI -->
   <td class="is summ">63.81 ± 1.05 / 16.07 ± 1.19</td> <!-- RRN -->
   <td class="is know">5.12 ± 1.20 / 27.91 ± 0.90</td> <!-- ARC-is -->
   <td class="is reason">0.89 ± 2.37 / 53.27 ± 1.64</td> <!-- Winogrande-is -->
   <td class="de ner">54.68 ± 1.38 / 46.36 ± 2.67</td> <!-- GermEval -->
   <td class="de sent">55.48 ± 2.67 / 69.91 ± 1.90</td> <!-- SB10k -->
   <td class="de la">26.89 ± 0.86 / 62.51 ± 0.48</td> <!-- ScaLA-de -->
   <td class="de rc">31.27 ± 1.89 / 62.30 ± 2.09</td> <!-- GermanQuAD -->
   <td class="de summ">66.33 ± 0.75 / 20.58 ± 1.77</td> <!-- MLSum -->
   <td class="de know">33.98 ± 0.82 / 50.12 ± 0.65</td> <!-- MMLU-de -->
   <td class="de reason">34.59 ± 1.42 / 49.13 ± 1.25</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.62 ± 2.29 / 40.51 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.37 ± 1.25 / 36.94 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">23.47 ± 1.79 / 60.17 ± 1.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.20 ± 1.02 / 72.98 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.34 ± 3.24 / 18.49 ± 1.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.69 ± 0.59 / 50.59 ± 0.56</td> <!-- MMLU-nl -->
   <td class="nl reason">31.36 ± 1.90 / 46.78 ± 1.51</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.84 ± 1.74 / 56.61 ± 1.77</td> <!-- CoNLL-en -->
   <td class="en sent">68.55 ± 0.89 / 72.50 ± 1.04</td> <!-- SST5 -->
   <td class="en la">41.05 ± 2.87 / 69.78 ± 1.63</td> <!-- ScaLA-en -->
   <td class="en rc">66.25 ± 2.13 / 83.31 ± 0.91</td> <!-- SQuAD -->
   <td class="en summ">69.36 ± 0.50 / 25.91 ± 0.54</td> <!-- CNN-DailyMail -->
   <td class="en know">53.62 ± 0.83 / 65.00 ± 0.65</td> <!-- MMLU -->
   <td class="en reason">71.00 ± 2.12 / 77.45 ± 1.78</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">2.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="is-rank">3.97</td> <!-- Icelandic rank -->
   <td class="de-rank">2.23</td> <!-- German rank -->
   <td class="nl-rank">2.84</td> <!-- Dutch rank -->
   <td class="en-rank">1.97</td> <!-- English rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da rc">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
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
   <td class="no rc">46.86 ± 3.27 / 70.86 ± 2.79</td> <!-- NorQuAD -->
   <td class="no know">27.78 ± 1.08 / 45.76 ± 0.79</td> <!-- MMLU-no -->
   <td class="no reason">10.88 ± 3.63 / 32.43 ± 2.67</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.87 ± 0.31 / 19.30 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">35.52 ± 1.01 / 51.52 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">19.67 ± 2.31 / 38.98 ± 1.98</td> <!-- HellaSwag-sv -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.70 ± 5.36 / 49.31 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.96 ± 3.10 / 16.11 ± 1.80</td> <!-- RRN -->
   <td class="is know">10.25 ± 0.96 / 32.89 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">1.99 ± 2.95 / 54.48 ± 1.27</td> <!-- Winogrande-is -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de rc">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
   <td class="de summ">68.24 ± 0.70 / 25.71 ± 1.33</td> <!-- MLSum -->
   <td class="de know">35.63 ± 1.12 / 51.69 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">26.40 ± 1.86 / 43.98 ± 1.58</td> <!-- HellaSwag-de -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.24 ± 0.91 / 17.54 ± 1.10</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.49 ± 0.57 / 51.51 ± 0.42</td> <!-- MMLU-nl -->
   <td class="nl reason">19.88 ± 1.80 / 39.13 ± 1.56</td> <!-- HellaSwag-nl -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en rc">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="da-rank">2.50</td> <!-- Danish rank -->
   <td class="no-rank">2.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="is-rank">4.01</td> <!-- Icelandic rank -->
   <td class="de-rank">2.29</td> <!-- German rank -->
   <td class="nl-rank">2.89</td> <!-- Dutch rank -->
   <td class="en-rank">2.00</td> <!-- English rank -->
   <td class="da ner">43.60 ± 2.94 / 32.17 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.92 ± 1.50 / 61.91 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">15.43 ± 3.79 / 46.20 ± 5.54</td> <!-- ScaLA-da -->
   <td class="da rc">59.13 ± 0.86 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
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
   <td class="no rc">45.15 ± 3.72 / 68.61 ± 3.30</td> <!-- NorQuAD -->
   <td class="no know">28.31 ± 1.01 / 45.93 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">13.59 ± 2.44 / 33.95 ± 1.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.79 ± 0.32 / 19.30 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.51 ± 1.13 / 50.46 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">20.84 ± 2.19 / 39.88 ± 1.85</td> <!-- HellaSwag-sv -->
   <td class="is ner">44.68 ± 3.50 / 36.20 ± 4.20</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.12 ± 1.68 / 35.09 ± 1.17</td> <!-- ScaLA-is -->
   <td class="is rc">25.52 ± 5.24 / 49.15 ± 5.21</td> <!-- NQiI -->
   <td class="is summ">61.40 ± 2.38 / 14.90 ± 1.60</td> <!-- RRN -->
   <td class="is know">10.25 ± 1.54 / 32.81 ± 1.22</td> <!-- ARC-is -->
   <td class="is reason">5.24 ± 1.65 / 52.80 ± 2.41</td> <!-- Winogrande-is -->
   <td class="de ner">55.41 ± 1.45 / 48.39 ± 1.46</td> <!-- GermEval -->
   <td class="de sent">52.58 ± 2.42 / 67.52 ± 1.82</td> <!-- SB10k -->
   <td class="de la">24.10 ± 2.12 / 59.47 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">31.52 ± 2.95 / 60.03 ± 3.81</td> <!-- GermanQuAD -->
   <td class="de summ">68.96 ± 1.13 / 28.26 ± 2.32</td> <!-- MLSum -->
   <td class="de know">35.06 ± 0.54 / 51.20 ± 0.43</td> <!-- MMLU-de -->
   <td class="de reason">28.85 ± 1.70 / 45.83 ± 1.39</td> <!-- HellaSwag-de -->
   <td class="nl ner">56.52 ± 1.42 / 41.84 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.02 ± 1.21 / 26.40 ± 2.96</td> <!-- Dutch Social -->
   <td class="nl la">23.41 ± 2.91 / 59.14 ± 3.11</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.90 ± 1.07 / 72.49 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.74 / 17.69 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.93 ± 1.11 / 51.02 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">23.73 ± 1.97 / 41.93 ± 1.68</td> <!-- HellaSwag-nl -->
   <td class="en ner">61.02 ± 2.74 / 55.65 ± 2.55</td> <!-- CoNLL-en -->
   <td class="en sent">67.29 ± 0.80 / 70.81 ± 0.84</td> <!-- SST5 -->
   <td class="en la">30.10 ± 5.12 / 62.99 ± 4.71</td> <!-- ScaLA-en -->
   <td class="en rc">73.59 ± 1.75 / 84.31 ± 1.35</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.56</td> <!-- Danish rank -->
   <td class="no-rank">2.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="is-rank">4.16</td> <!-- Icelandic rank -->
   <td class="de-rank">2.38</td> <!-- German rank -->
   <td class="nl-rank">3.03</td> <!-- Dutch rank -->
   <td class="en-rank">2.20</td> <!-- English rank -->
   <td class="da ner">44.00 ± 2.63 / 29.00 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.41 ± 1.79 / 62.27 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">16.17 ± 2.17 / 56.93 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">57.06 ± 0.83 / 63.94 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">66.88 ± 0.98 / 21.84 ± 1.04</td> <!-- Nordjylland-News -->
   <td class="da know">45.21 ± 1.90 / 57.54 ± 1.55</td> <!-- Danske Talemaader -->
   <td class="da know">51.06 ± 2.13 / 67.44 ± 1.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.50 ± 1.48 / 36.77 ± 1.21</td> <!-- HellaSwag-da -->
   <td class="no ner">57.21 ± 1.51 / 40.40 ± 2.79</td> <!-- NorNE-nb -->
   <td class="no ner">59.62 ± 1.34 / 41.07 ± 2.58</td> <!-- NorNE-nn -->
   <td class="no sent">38.93 ± 3.56 / 57.45 ± 3.77</td> <!-- NoReC -->
   <td class="no summ">65.12 ± 0.35 / 17.27 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">8.65 ± 3.33 / 47.18 ± 3.98</td> <!-- ScaLA-nb -->
   <td class="no la">5.92 ± 1.58 / 47.50 ± 3.58</td> <!-- ScaLA-nn -->
   <td class="no rc">42.32 ± 2.80 / 69.24 ± 2.68</td> <!-- NorQuAD -->
   <td class="no know">23.88 ± 1.01 / 42.37 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">22.33 ± 1.67 / 41.00 ± 1.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.90 ± 2.28 / 35.48 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 2.05 / 79.13 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">14.67 ± 2.27 / 53.90 ± 2.24</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.12 ± 0.70 / 63.72 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.25 ± 0.10 / 19.64 ± 0.19</td> <!-- SweDN -->
   <td class="sv know">24.40 ± 1.20 / 42.73 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">19.30 ± 1.27 / 38.75 ± 1.05</td> <!-- HellaSwag-sv -->
   <td class="is ner">37.53 ± 3.42 / 30.51 ± 3.50</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.14 ± 1.96 / 39.45 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">20.91 ± 2.93 / 43.86 ± 1.90</td> <!-- NQiI -->
   <td class="is summ">66.15 ± 0.59 / 19.08 ± 1.08</td> <!-- RRN -->
   <td class="is know">7.17 ± 1.32 / 30.61 ± 0.94</td> <!-- ARC-is -->
   <td class="is reason">-0.55 ± 2.76 / 47.83 ± 2.20</td> <!-- Winogrande-is -->
   <td class="de ner">57.57 ± 1.46 / 44.84 ± 2.12</td> <!-- GermEval -->
   <td class="de sent">49.40 ± 2.11 / 63.02 ± 2.68</td> <!-- SB10k -->
   <td class="de la">23.32 ± 2.20 / 59.16 ± 2.36</td> <!-- ScaLA-de -->
   <td class="de rc">30.24 ± 1.18 / 61.10 ± 1.87</td> <!-- GermanQuAD -->
   <td class="de summ">68.01 ± 1.28 / 25.44 ± 3.23</td> <!-- MLSum -->
   <td class="de know">27.06 ± 0.92 / 45.06 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">26.96 ± 0.49 / 44.79 ± 0.39</td> <!-- HellaSwag-de -->
   <td class="nl ner">57.80 ± 1.53 / 39.43 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 1.27 / 29.84 ± 2.35</td> <!-- Dutch Social -->
   <td class="nl la">17.40 ± 1.54 / 57.26 ± 1.96</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.35 ± 0.85 / 69.69 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.11 ± 0.58 / 18.31 ± 0.61</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.15 ± 1.09 / 44.95 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">19.18 ± 1.46 / 38.84 ± 1.26</td> <!-- HellaSwag-nl -->
   <td class="en ner">68.75 ± 1.54 / 60.01 ± 1.57</td> <!-- CoNLL-en -->
   <td class="en sent">62.37 ± 1.68 / 67.79 ± 1.51</td> <!-- SST5 -->
   <td class="en la">25.07 ± 3.20 / 61.02 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en rc">61.56 ± 1.18 / 80.11 ± 0.70</td> <!-- SQuAD -->
   <td class="en summ">69.40 ± 0.49 / 24.79 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">38.00 ± 0.83 / 52.95 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">42.14 ± 2.47 / 55.96 ± 1.93</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.11.0</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.11.0</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   <td>12.11.0</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   <td>12.11.0</td> <!-- MIM-GOLD-NER version -->
   <td>12.10.4</td> <!-- ScaLA-is version -->
   <td>12.11.0</td> <!-- NQiI version -->
   <td>12.11.0</td> <!-- RRN version -->
   <td>12.11.0</td> <!-- ARC-is version -->
   <td>12.10.4</td> <!-- Winogrande-is version -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.11.0</td> <!-- SQuAD version -->
   <td>12.11.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="da-rank">2.62</td> <!-- Danish rank -->
   <td class="no-rank">3.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="is-rank">4.05</td> <!-- Icelandic rank -->
   <td class="de-rank">2.51</td> <!-- German rank -->
   <td class="nl-rank">2.85</td> <!-- Dutch rank -->
   <td class="en-rank">2.25</td> <!-- English rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da rc">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
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
   <td class="no rc">35.74 ± 2.44 / 64.27 ± 2.42</td> <!-- NorQuAD -->
   <td class="no know">20.37 ± 1.34 / 39.32 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">21.16 ± 2.07 / 39.85 ± 1.73</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.11 ± 0.18 / 19.64 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">25.60 ± 1.10 / 43.53 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">21.75 ± 1.61 / 40.57 ± 1.45</td> <!-- HellaSwag-sv -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is rc">19.18 ± 3.69 / 49.62 ± 2.59</td> <!-- NQiI -->
   <td class="is summ">65.01 ± 1.51 / 18.34 ± 1.35</td> <!-- RRN -->
   <td class="is know">5.49 ± 1.98 / 28.73 ± 1.39</td> <!-- ARC-is -->
   <td class="is reason">0.24 ± 0.71 / 38.95 ± 0.84</td> <!-- Winogrande-is -->
   <td class="de ner">55.10 ± 1.35 / 41.89 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">47.69 ± 2.35 / 64.93 ± 1.71</td> <!-- SB10k -->
   <td class="de la">24.14 ± 2.09 / 60.83 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">23.93 ± 2.11 / 57.64 ± 1.89</td> <!-- GermanQuAD -->
   <td class="de summ">67.51 ± 0.71 / 22.63 ± 1.73</td> <!-- MLSum -->
   <td class="de know">26.06 ± 1.65 / 44.13 ± 1.29</td> <!-- MMLU-de -->
   <td class="de reason">31.09 ± 1.35 / 47.48 ± 0.98</td> <!-- HellaSwag-de -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.99 ± 0.49 / 19.54 ± 0.55</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.86 ± 1.89 / 41.71 ± 1.45</td> <!-- MMLU-nl -->
   <td class="nl reason">24.80 ± 1.77 / 42.93 ± 1.38</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en rc">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="da-rank">2.61</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="is-rank">4.05</td> <!-- Icelandic rank -->
   <td class="de-rank">2.57</td> <!-- German rank -->
   <td class="nl-rank">3.33</td> <!-- Dutch rank -->
   <td class="en-rank">2.13</td> <!-- English rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
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
   <td class="no rc">44.07 ± 3.40 / 68.49 ± 2.97</td> <!-- NorQuAD -->
   <td class="no know">25.07 ± 1.48 / 43.13 ± 1.15</td> <!-- MMLU-no -->
   <td class="no reason">15.56 ± 3.55 / 35.85 ± 2.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.15 ± 0.31 / 18.72 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">33.24 ± 0.85 / 49.69 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">25.50 ± 2.25 / 43.44 ± 2.03</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.47 ± 4.24 / 30.33 ± 3.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.54 ± 1.29 / 50.66 ± 0.62</td> <!-- ScaLA-is -->
   <td class="is rc">18.66 ± 4.26 / 38.73 ± 3.66</td> <!-- NQiI -->
   <td class="is summ">63.68 ± 1.75 / 16.38 ± 1.24</td> <!-- RRN -->
   <td class="is know">5.12 ± 1.30 / 28.85 ± 0.99</td> <!-- ARC-is -->
   <td class="is reason">8.30 ± 1.28 / 57.35 ± 0.75</td> <!-- Winogrande-is -->
   <td class="de ner">50.66 ± 1.53 / 39.89 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">54.79 ± 3.53 / 68.79 ± 3.00</td> <!-- SB10k -->
   <td class="de la">20.17 ± 1.69 / 58.67 ± 1.13</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 4.70 / 54.38 ± 5.91</td> <!-- GermanQuAD -->
   <td class="de summ">65.53 ± 1.07 / 19.46 ± 1.48</td> <!-- MLSum -->
   <td class="de know">27.04 ± 1.04 / 44.99 ± 0.77</td> <!-- MMLU-de -->
   <td class="de reason">17.47 ± 3.26 / 36.70 ± 2.93</td> <!-- HellaSwag-de -->
   <td class="nl ner">54.56 ± 2.96 / 37.86 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.43 ± 1.27 / 24.23 ± 0.94</td> <!-- Dutch Social -->
   <td class="nl la">10.99 ± 2.55 / 50.46 ± 4.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.91 ± 1.08 / 66.78 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.88 ± 1.41 / 12.36 ± 1.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.12 ± 1.17 / 43.50 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">10.65 ± 1.55 / 31.51 ± 1.52</td> <!-- HellaSwag-nl -->
   <td class="en ner">59.10 ± 1.87 / 51.31 ± 1.87</td> <!-- CoNLL-en -->
   <td class="en sent">68.41 ± 1.17 / 70.85 ± 0.74</td> <!-- SST5 -->
   <td class="en la">25.43 ± 4.22 / 60.79 ± 3.45</td> <!-- ScaLA-en -->
   <td class="en rc">71.89 ± 2.20 / 82.99 ± 1.78</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">2.73</td> <!-- Danish rank -->
   <td class="no-rank">3.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="is-rank">4.25</td> <!-- Icelandic rank -->
   <td class="de-rank">2.38</td> <!-- German rank -->
   <td class="nl-rank">3.10</td> <!-- Dutch rank -->
   <td class="en-rank">2.20</td> <!-- English rank -->
   <td class="da ner">41.28 ± 3.92 / 31.98 ± 3.26</td> <!-- DANSK -->
   <td class="da sent">23.01 ± 3.87 / 36.55 ± 6.42</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 2.75 / 58.11 ± 3.45</td> <!-- ScaLA-da -->
   <td class="da rc">60.29 ± 0.81 / 65.52 ± 0.58</td> <!-- ScandiQA-da -->
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
   <td class="no rc">49.24 ± 4.28 / 72.68 ± 3.66</td> <!-- NorQuAD -->
   <td class="no know">23.60 ± 1.05 / 42.20 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">16.55 ± 2.83 / 35.97 ± 1.94</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.59 ± 0.34 / 18.56 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">25.51 ± 0.81 / 43.68 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">14.97 ± 1.73 / 34.85 ± 1.34</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.56 ± 3.03 / 34.23 ± 3.45</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.73 ± 1.56 / 45.02 ± 2.05</td> <!-- ScaLA-is -->
   <td class="is rc">21.97 ± 4.26 / 46.27 ± 3.94</td> <!-- NQiI -->
   <td class="is summ">63.50 ± 2.92 / 16.51 ± 2.19</td> <!-- RRN -->
   <td class="is know">5.60 ± 1.25 / 29.83 ± 1.00</td> <!-- ARC-is -->
   <td class="is reason">-5.80 ± 2.91 / 46.82 ± 2.65</td> <!-- Winogrande-is -->
   <td class="de ner">52.08 ± 1.86 / 46.67 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">46.38 ± 2.70 / 60.32 ± 2.80</td> <!-- SB10k -->
   <td class="de la">22.39 ± 3.96 / 57.26 ± 4.22</td> <!-- ScaLA-de -->
   <td class="de rc">33.43 ± 2.38 / 62.65 ± 2.83</td> <!-- GermanQuAD -->
   <td class="de summ">69.50 ± 1.29 / 29.74 ± 3.10</td> <!-- MLSum -->
   <td class="de know">28.79 ± 1.53 / 45.87 ± 1.26</td> <!-- MMLU-de -->
   <td class="de reason">21.50 ± 2.52 / 39.80 ± 2.47</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.55 ± 1.64 / 43.32 ± 1.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.26 ± 2.09 / 28.32 ± 2.68</td> <!-- Dutch Social -->
   <td class="nl la">24.57 ± 3.54 / 54.94 ± 5.33</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.99 ± 0.95 / 72.74 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.02 ± 0.84 / 16.97 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.73 ± 0.90 / 45.62 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">19.43 ± 1.53 / 38.57 ± 1.39</td> <!-- HellaSwag-nl -->
   <td class="en ner">63.75 ± 2.50 / 59.28 ± 2.20</td> <!-- CoNLL-en -->
   <td class="en sent">61.85 ± 1.70 / 69.02 ± 0.76</td> <!-- SST5 -->
   <td class="en la">26.41 ± 4.93 / 59.67 ± 4.84</td> <!-- ScaLA-en -->
   <td class="en rc">73.48 ± 2.06 / 85.27 ± 1.15</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da-rank">2.78</td> <!-- Danish rank -->
   <td class="no-rank">3.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.78</td> <!-- Swedish rank -->
   <td class="is-rank">4.11</td> <!-- Icelandic rank -->
   <td class="de-rank">2.28</td> <!-- German rank -->
   <td class="nl-rank">3.01</td> <!-- Dutch rank -->
   <td class="en-rank">2.26</td> <!-- English rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da rc">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
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
   <td class="no rc">52.19 ± 2.88 / 74.97 ± 2.11</td> <!-- NorQuAD -->
   <td class="no know">20.61 ± 1.27 / 39.79 ± 1.10</td> <!-- MMLU-no -->
   <td class="no reason">16.18 ± 1.88 / 36.19 ± 1.66</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.07 ± 0.34 / 19.59 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">25.52 ± 1.30 / 43.68 ± 1.03</td> <!-- MMLU-sv -->
   <td class="sv reason">14.06 ± 1.68 / 35.12 ± 1.47</td> <!-- HellaSwag-sv -->
   <td class="is ner">40.71 ± 2.93 / 34.57 ± 4.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is rc">20.66 ± 3.67 / 45.91 ± 3.45</td> <!-- NQiI -->
   <td class="is summ">65.25 ± 0.97 / 19.09 ± 1.05</td> <!-- RRN -->
   <td class="is know">5.35 ± 1.32 / 28.11 ± 1.13</td> <!-- ARC-is -->
   <td class="is reason">0.35 ± 2.49 / 51.16 ± 2.74</td> <!-- Winogrande-is -->
   <td class="de ner">52.63 ± 1.89 / 42.99 ± 2.40</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de rc">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.43 ± 0.97 / 29.48 ± 2.59</td> <!-- MLSum -->
   <td class="de know">32.56 ± 1.16 / 49.02 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">23.61 ± 2.42 / 41.55 ± 2.14</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.78 ± 1.86 / 41.29 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.46 ± 0.67 / 19.49 ± 0.92</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.37 ± 0.99 / 45.81 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">15.25 ± 1.71 / 35.83 ± 1.42</td> <!-- HellaSwag-nl -->
   <td class="en ner">56.90 ± 3.08 / 51.16 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en rc">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="da-rank">2.94</td> <!-- Danish rank -->
   <td class="no-rank">3.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.05</td> <!-- Swedish rank -->
   <td class="is-rank">4.36</td> <!-- Icelandic rank -->
   <td class="de-rank">2.01</td> <!-- German rank -->
   <td class="nl-rank">2.95</td> <!-- Dutch rank -->
   <td class="en-rank">1.74</td> <!-- English rank -->
   <td class="da ner">41.37 ± 2.50 / 24.64 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">42.60 ± 1.06 / 61.52 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">6.52 ± 1.34 / 45.01 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">50.57 ± 1.03 / 57.75 ± 0.64</td> <!-- ScandiQA-da -->
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
   <td class="no rc">30.11 ± 2.09 / 52.56 ± 2.38</td> <!-- NorQuAD -->
   <td class="no know">15.54 ± 0.89 / 36.69 ± 0.67</td> <!-- MMLU-no -->
   <td class="no reason">17.55 ± 0.88 / 37.93 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.20 ± 0.99 / 15.57 ± 0.62</td> <!-- SweDN -->
   <td class="sv know">21.33 ± 1.03 / 41.04 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">16.12 ± 1.15 / 36.99 ± 0.85</td> <!-- HellaSwag-sv -->
   <td class="is ner">33.05 ± 4.29 / 29.75 ± 3.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 1.18 / 34.80 ± 0.88</td> <!-- ScaLA-is -->
   <td class="is rc">17.23 ± 2.51 / 39.88 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">60.08 ± 1.45 / 13.80 ± 0.81</td> <!-- RRN -->
   <td class="is know">2.67 ± 1.35 / 27.04 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">2.74 ± 2.28 / 53.18 ± 0.93</td> <!-- Winogrande-is -->
   <td class="de ner">59.68 ± 0.41 / 48.00 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.75 ± 2.36 / 68.54 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.22 ± 2.94 / 64.51 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">29.27 ± 1.03 / 59.19 ± 2.46</td> <!-- GermanQuAD -->
   <td class="de summ">66.64 ± 0.91 / 22.90 ± 2.24</td> <!-- MLSum -->
   <td class="de know">39.50 ± 0.93 / 54.61 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">51.29 ± 1.38 / 63.10 ± 1.12</td> <!-- HellaSwag-de -->
   <td class="nl ner">50.31 ± 1.94 / 41.54 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.58 ± 1.62 / 36.56 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">14.72 ± 1.84 / 50.23 ± 3.10</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.19 ± 0.80 / 66.72 ± 0.92</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.40 ± 0.77 / 17.47 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.31 ± 0.70 / 46.18 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">21.25 ± 1.25 / 40.78 ± 1.02</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.13 ± 1.16 / 53.55 ± 2.73</td> <!-- CoNLL-en -->
   <td class="en sent">63.66 ± 1.31 / 70.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">34.07 ± 2.32 / 66.51 ± 1.23</td> <!-- ScaLA-en -->
   <td class="en rc">68.10 ± 1.44 / 83.46 ± 1.01</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="da-rank">2.77</td> <!-- Danish rank -->
   <td class="no-rank">3.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="is-rank">4.23</td> <!-- Icelandic rank -->
   <td class="de-rank">2.60</td> <!-- German rank -->
   <td class="nl-rank">2.96</td> <!-- Dutch rank -->
   <td class="en-rank">2.16</td> <!-- English rank -->
   <td class="da ner">41.12 ± 3.39 / 32.50 ± 2.74</td> <!-- DANSK -->
   <td class="da sent">42.77 ± 2.76 / 54.70 ± 4.19</td> <!-- Angry Tweets -->
   <td class="da la">11.52 ± 3.01 / 49.37 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">51.14 ± 1.03 / 60.18 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">65.19 ± 0.78 / 18.34 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">49.78 ± 1.52 / 62.29 ± 1.14</td> <!-- Danske Talemaader -->
   <td class="da know">45.88 ± 2.43 / 63.96 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">21.89 ± 1.77 / 41.16 ± 1.43</td> <!-- HellaSwag-da -->
   <td class="no ner">49.66 ± 1.79 / 39.31 ± 2.55</td> <!-- NorNE-nb -->
   <td class="no ner">51.98 ± 1.55 / 42.48 ± 3.10</td> <!-- NorNE-nn -->
   <td class="no sent">44.13 ± 2.80 / 60.09 ± 3.10</td> <!-- NoReC -->
   <td class="no summ">60.50 ± 0.73 / 10.91 ± 0.62</td> <!-- No Sammendrag -->
   <td class="no la">0.67 ± 1.18 / 33.81 ± 0.33</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 0.93 / 33.03 ± 0.39</td> <!-- ScaLA-nn -->
   <td class="no rc">28.62 ± 4.16 / 56.91 ± 4.14</td> <!-- NorQuAD -->
   <td class="no know">26.82 ± 1.08 / 45.32 ± 0.84</td> <!-- MMLU-no -->
   <td class="no reason">20.98 ± 1.40 / 40.34 ± 1.17</td> <!-- HellaSwag-no -->
   <td class="sv ner">43.74 ± 2.58 / 34.37 ± 2.59</td> <!-- SUC3 -->
   <td class="sv sent">76.98 ± 1.31 / 71.38 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">16.01 ± 2.24 / 51.83 ± 3.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.38 ± 1.78 / 57.83 ± 0.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.98 ± 0.47 / 17.53 ± 0.50</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 0.61 / 47.21 ± 0.47</td> <!-- MMLU-sv -->
   <td class="sv reason">22.42 ± 1.89 / 41.45 ± 1.49</td> <!-- HellaSwag-sv -->
   <td class="is ner">27.57 ± 1.71 / 22.52 ± 1.18</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.39 ± 1.30 / 34.40 ± 1.96</td> <!-- ScaLA-is -->
   <td class="is rc">22.98 ± 2.48 / 50.74 ± 1.59</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.89 / 14.40 ± 1.93</td> <!-- RRN -->
   <td class="is know">13.33 ± 1.23 / 35.42 ± 0.93</td> <!-- ARC-is -->
   <td class="is reason">0.74 ± 1.09 / 50.92 ± 0.73</td> <!-- Winogrande-is -->
   <td class="de ner">55.52 ± 2.07 / 46.18 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">50.52 ± 2.29 / 62.39 ± 2.63</td> <!-- SB10k -->
   <td class="de la">9.87 ± 2.95 / 42.20 ± 3.60</td> <!-- ScaLA-de -->
   <td class="de rc">20.20 ± 3.28 / 47.02 ± 5.20</td> <!-- GermanQuAD -->
   <td class="de summ">66.40 ± 0.98 / 21.21 ± 2.33</td> <!-- MLSum -->
   <td class="de know">33.58 ± 0.41 / 50.27 ± 0.28</td> <!-- MMLU-de -->
   <td class="de reason">28.97 ± 1.01 / 46.45 ± 0.80</td> <!-- HellaSwag-de -->
   <td class="nl ner">43.66 ± 2.01 / 40.23 ± 1.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.87 ± 1.32 / 37.23 ± 1.55</td> <!-- Dutch Social -->
   <td class="nl la">17.94 ± 3.48 / 55.88 ± 3.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.77 ± 1.82 / 64.44 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.74 ± 1.00 / 18.33 ± 1.28</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.80 ± 0.84 / 50.30 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">21.02 ± 1.29 / 40.27 ± 1.09</td> <!-- HellaSwag-nl -->
   <td class="en ner">68.44 ± 1.14 / 56.80 ± 2.31</td> <!-- CoNLL-en -->
   <td class="en sent">66.00 ± 1.41 / 70.47 ± 1.02</td> <!-- SST5 -->
   <td class="en la">32.04 ± 3.44 / 65.62 ± 1.88</td> <!-- ScaLA-en -->
   <td class="en rc">49.54 ± 3.13 / 75.26 ± 1.64</td> <!-- SQuAD -->
   <td class="en summ">69.23 ± 0.19 / 24.84 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">45.50 ± 0.74 / 58.96 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">46.50 ± 1.78 / 59.43 ± 1.44</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.79</td> <!-- Swedish rank -->
   <td class="is-rank">4.32</td> <!-- Icelandic rank -->
   <td class="de-rank">2.58</td> <!-- German rank -->
   <td class="nl-rank">3.03</td> <!-- Dutch rank -->
   <td class="en-rank">2.30</td> <!-- English rank -->
   <td class="da ner">28.22 ± 1.66 / 19.95 ± 1.55</td> <!-- DANSK -->
   <td class="da sent">47.11 ± 1.36 / 63.36 ± 1.39</td> <!-- Angry Tweets -->
   <td class="da la">19.99 ± 1.86 / 58.86 ± 1.11</td> <!-- ScaLA-da -->
   <td class="da rc">48.00 ± 0.98 / 58.49 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">66.73 ± 1.01 / 21.91 ± 1.06</td> <!-- Nordjylland-News -->
   <td class="da know">52.85 ± 1.36 / 63.72 ± 1.12</td> <!-- Danske Talemaader -->
   <td class="da know">52.74 ± 1.77 / 68.55 ± 1.20</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.94 ± 1.28 / 47.03 ± 1.01</td> <!-- HellaSwag-da -->
   <td class="no ner">35.56 ± 1.33 / 28.84 ± 2.19</td> <!-- NorNE-nb -->
   <td class="no ner">37.70 ± 3.04 / 30.22 ± 2.39</td> <!-- NorNE-nn -->
   <td class="no sent">46.84 ± 2.20 / 63.22 ± 1.89</td> <!-- NoReC -->
   <td class="no summ">64.58 ± 0.33 / 17.00 ± 0.45</td> <!-- No Sammendrag -->
   <td class="no la">17.15 ± 2.01 / 55.59 ± 2.04</td> <!-- ScaLA-nb -->
   <td class="no la">14.38 ± 1.96 / 54.95 ± 1.73</td> <!-- ScaLA-nn -->
   <td class="no rc">29.75 ± 1.52 / 63.79 ± 1.50</td> <!-- NorQuAD -->
   <td class="no know">23.02 ± 1.05 / 41.85 ± 0.86</td> <!-- MMLU-no -->
   <td class="no reason">33.13 ± 1.06 / 49.47 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">35.61 ± 2.19 / 26.05 ± 2.45</td> <!-- SUC3 -->
   <td class="sv sent">75.84 ± 1.41 / 77.22 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">15.62 ± 1.67 / 51.30 ± 3.09</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.76 ± 0.92 / 58.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.16 ± 0.13 / 18.88 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">27.00 ± 0.89 / 44.95 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">31.43 ± 1.21 / 47.99 ± 0.85</td> <!-- HellaSwag-sv -->
   <td class="is ner">14.79 ± 4.70 / 13.03 ± 2.92</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.10 ± 1.54 / 34.67 ± 0.87</td> <!-- ScaLA-is -->
   <td class="is rc">25.42 ± 1.09 / 51.72 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">62.67 ± 1.62 / 16.91 ± 1.38</td> <!-- RRN -->
   <td class="is know">10.76 ± 1.56 / 32.34 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-5.20 ± 1.82 / 53.08 ± 0.91</td> <!-- Winogrande-is -->
   <td class="de ner">37.31 ± 2.28 / 31.09 ± 2.10</td> <!-- GermEval -->
   <td class="de sent">46.23 ± 2.32 / 63.45 ± 1.57</td> <!-- SB10k -->
   <td class="de la">23.26 ± 1.16 / 60.73 ± 0.24</td> <!-- ScaLA-de -->
   <td class="de rc">28.01 ± 1.95 / 59.66 ± 2.10</td> <!-- GermanQuAD -->
   <td class="de summ">66.35 ± 0.99 / 21.43 ± 2.27</td> <!-- MLSum -->
   <td class="de know">30.11 ± 1.02 / 47.48 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">35.25 ± 0.64 / 50.80 ± 0.55</td> <!-- HellaSwag-de -->
   <td class="nl ner">40.58 ± 2.08 / 28.95 ± 1.56</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.17 ± 1.32 / 32.96 ± 1.96</td> <!-- Dutch Social -->
   <td class="nl la">19.63 ± 2.61 / 52.65 ± 2.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.30 ± 1.25 / 67.27 ± 0.73</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.83 ± 0.86 / 19.21 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.30 ± 1.02 / 46.88 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">31.43 ± 1.42 / 47.87 ± 1.30</td> <!-- HellaSwag-nl -->
   <td class="en ner">44.36 ± 1.46 / 38.51 ± 1.53</td> <!-- CoNLL-en -->
   <td class="en sent">66.37 ± 1.35 / 67.64 ± 1.35</td> <!-- SST5 -->
   <td class="en la">34.69 ± 2.50 / 67.16 ± 1.29</td> <!-- ScaLA-en -->
   <td class="en rc">55.07 ± 1.73 / 78.88 ± 0.80</td> <!-- SQuAD -->
   <td class="en summ">68.09 ± 0.20 / 23.58 ± 0.33</td> <!-- CNN-DailyMail -->
   <td class="en know">42.89 ± 1.25 / 57.03 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">45.52 ± 0.68 / 58.39 ± 0.55</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="da-rank">2.84</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.79</td> <!-- Swedish rank -->
   <td class="is-rank">4.22</td> <!-- Icelandic rank -->
   <td class="de-rank">2.38</td> <!-- German rank -->
   <td class="nl-rank">3.15</td> <!-- Dutch rank -->
   <td class="en-rank">2.38</td> <!-- English rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
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
   <td class="no rc">43.88 ± 4.07 / 66.65 ± 4.20</td> <!-- NorQuAD -->
   <td class="no know">20.87 ± 1.54 / 39.98 ± 1.27</td> <!-- MMLU-no -->
   <td class="no reason">13.10 ± 2.04 / 34.20 ± 1.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.45 / 18.79 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">23.68 ± 1.41 / 42.15 ± 1.14</td> <!-- MMLU-sv -->
   <td class="sv reason">14.05 ± 1.60 / 34.81 ± 1.58</td> <!-- HellaSwag-sv -->
   <td class="is ner">40.08 ± 2.82 / 37.15 ± 4.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="is summ">62.55 ± 3.03 / 15.26 ± 2.31</td> <!-- RRN -->
   <td class="is know">5.98 ± 1.66 / 28.18 ± 1.30</td> <!-- ARC-is -->
   <td class="is reason">-0.51 ± 1.95 / 47.23 ± 2.39</td> <!-- Winogrande-is -->
   <td class="de ner">51.39 ± 1.35 / 44.47 ± 2.77</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.68 / 28.27 ± 1.70</td> <!-- MLSum -->
   <td class="de know">32.49 ± 0.91 / 48.82 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">22.25 ± 2.13 / 40.28 ± 1.67</td> <!-- HellaSwag-de -->
   <td class="nl ner">51.31 ± 2.32 / 42.95 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.66 ± 0.74 / 18.22 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.12 ± 0.86 / 44.36 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">13.99 ± 2.04 / 34.45 ± 1.89</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.37 ± 2.94 / 51.08 ± 2.87</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en rc">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="da-rank">3.14</td> <!-- Danish rank -->
   <td class="no-rank">3.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.80</td> <!-- Swedish rank -->
   <td class="is-rank">4.15</td> <!-- Icelandic rank -->
   <td class="de-rank">2.61</td> <!-- German rank -->
   <td class="nl-rank">3.24</td> <!-- Dutch rank -->
   <td class="en-rank">1.85</td> <!-- English rank -->
   <td class="da ner">35.21 ± 2.52 / 23.65 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">12.73 ± 2.87 / 22.69 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">4.75 ± 2.45 / 35.71 ± 3.01</td> <!-- ScaLA-da -->
   <td class="da rc">55.95 ± 1.09 / 61.53 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">64.28 ± 0.93 / 18.81 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">46.17 ± 1.83 / 59.04 ± 1.44</td> <!-- Danske Talemaader -->
   <td class="da know">36.46 ± 2.46 / 57.64 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.01 ± 1.66 / 38.12 ± 1.37</td> <!-- HellaSwag-da -->
   <td class="no ner">46.02 ± 2.12 / 35.05 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">48.72 ± 1.76 / 35.97 ± 2.78</td> <!-- NorNE-nn -->
   <td class="no sent">27.86 ± 0.76 / 31.62 ± 0.80</td> <!-- NoReC -->
   <td class="no summ">60.92 ± 1.45 / 13.73 ± 1.28</td> <!-- No Sammendrag -->
   <td class="no la">2.41 ± 1.92 / 35.60 ± 2.65</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 2.05 / 34.90 ± 1.27</td> <!-- ScaLA-nn -->
   <td class="no rc">44.70 ± 3.79 / 67.06 ± 2.85</td> <!-- NorQuAD -->
   <td class="no know">23.93 ± 1.18 / 42.87 ± 0.91</td> <!-- MMLU-no -->
   <td class="no reason">22.39 ± 1.04 / 41.71 ± 0.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.55 ± 2.18 / 26.78 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">70.71 ± 1.99 / 71.19 ± 1.14</td> <!-- SweReC -->
   <td class="sv la">4.83 ± 3.48 / 36.64 ± 2.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.25 ± 1.21 / 61.21 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.18 ± 0.45 / 17.62 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">26.05 ± 0.80 / 44.56 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">27.09 ± 1.66 / 44.95 ± 1.30</td> <!-- HellaSwag-sv -->
   <td class="is ner">38.15 ± 2.30 / 28.10 ± 4.65</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.98 ± 1.44 / 35.86 ± 1.12</td> <!-- ScaLA-is -->
   <td class="is rc">20.39 ± 3.04 / 44.20 ± 2.72</td> <!-- NQiI -->
   <td class="is summ">61.23 ± 2.31 / 14.45 ± 1.79</td> <!-- RRN -->
   <td class="is know">7.59 ± 1.44 / 31.07 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">3.44 ± 2.28 / 46.89 ± 1.02</td> <!-- Winogrande-is -->
   <td class="de ner">48.20 ± 1.57 / 39.04 ± 2.38</td> <!-- GermEval -->
   <td class="de sent">47.12 ± 4.20 / 59.69 ± 4.45</td> <!-- SB10k -->
   <td class="de la">12.39 ± 1.39 / 45.13 ± 3.93</td> <!-- ScaLA-de -->
   <td class="de rc">30.50 ± 3.67 / 57.48 ± 4.51</td> <!-- GermanQuAD -->
   <td class="de summ">65.48 ± 1.73 / 22.72 ± 3.33</td> <!-- MLSum -->
   <td class="de know">30.83 ± 1.40 / 48.12 ± 1.03</td> <!-- MMLU-de -->
   <td class="de reason">24.90 ± 1.67 / 43.21 ± 1.49</td> <!-- HellaSwag-de -->
   <td class="nl ner">51.18 ± 1.62 / 35.45 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.23 ± 2.84 / 19.38 ± 4.37</td> <!-- Dutch Social -->
   <td class="nl la">1.99 ± 2.56 / 34.69 ± 1.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.66 ± 1.25 / 65.31 ± 1.06</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.81 ± 1.16 / 15.41 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.03 ± 1.02 / 45.90 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">23.64 ± 1.21 / 42.59 ± 0.96</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.51 ± 1.48 / 50.61 ± 1.37</td> <!-- CoNLL-en -->
   <td class="en sent">68.74 ± 0.81 / 58.25 ± 0.31</td> <!-- SST5 -->
   <td class="en la">40.81 ± 3.66 / 69.94 ± 1.98</td> <!-- ScaLA-en -->
   <td class="en rc">72.33 ± 2.68 / 84.50 ± 1.61</td> <!-- SQuAD -->
   <td class="en summ">67.71 ± 0.08 / 23.57 ± 0.14</td> <!-- CNN-DailyMail -->
   <td class="en know">48.36 ± 0.95 / 61.21 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">68.50 ± 0.63 / 76.04 ± 0.47</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="da-rank">2.81</td> <!-- Danish rank -->
   <td class="no-rank">3.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.88</td> <!-- Swedish rank -->
   <td class="is-rank">4.22</td> <!-- Icelandic rank -->
   <td class="de-rank">2.60</td> <!-- German rank -->
   <td class="nl-rank">3.16</td> <!-- Dutch rank -->
   <td class="en-rank">2.17</td> <!-- English rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da rc">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
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
   <td class="no rc">37.23 ± 3.15 / 63.67 ± 2.98</td> <!-- NorQuAD -->
   <td class="no know">20.44 ± 1.03 / 39.51 ± 0.72</td> <!-- MMLU-no -->
   <td class="no reason">15.87 ± 1.29 / 35.89 ± 1.06</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.10 ± 0.60 / 18.05 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">24.03 ± 1.09 / 42.32 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">15.37 ± 0.71 / 35.78 ± 0.69</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is rc">18.06 ± 3.16 / 42.57 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">62.80 ± 1.69 / 15.23 ± 1.01</td> <!-- RRN -->
   <td class="is know">5.44 ± 1.14 / 28.13 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">6.35 ± 2.71 / 50.49 ± 1.57</td> <!-- Winogrande-is -->
   <td class="de ner">47.19 ± 3.74 / 33.02 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">47.26 ± 3.14 / 63.48 ± 2.94</td> <!-- SB10k -->
   <td class="de la">22.32 ± 1.78 / 56.73 ± 4.00</td> <!-- ScaLA-de -->
   <td class="de rc">24.36 ± 3.78 / 54.61 ± 4.44</td> <!-- GermanQuAD -->
   <td class="de summ">67.75 ± 1.10 / 25.91 ± 2.95</td> <!-- MLSum -->
   <td class="de know">26.79 ± 1.01 / 44.58 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">20.33 ± 1.63 / 39.63 ± 1.09</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.97 / 16.55 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.06 ± 0.77 / 44.08 ± 0.51</td> <!-- MMLU-nl -->
   <td class="nl reason">14.26 ± 1.48 / 35.14 ± 1.18</td> <!-- HellaSwag-nl -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en rc">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="da-rank">2.87</td> <!-- Danish rank -->
   <td class="no-rank">3.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="is-rank">4.10</td> <!-- Icelandic rank -->
   <td class="de-rank">2.61</td> <!-- German rank -->
   <td class="nl-rank">3.34</td> <!-- Dutch rank -->
   <td class="en-rank">2.44</td> <!-- English rank -->
   <td class="da ner">41.13 ± 2.85 / 27.15 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">38.90 ± 1.93 / 44.34 ± 1.64</td> <!-- Angry Tweets -->
   <td class="da la">9.60 ± 2.51 / 44.34 ± 5.20</td> <!-- ScaLA-da -->
   <td class="da rc">56.85 ± 1.27 / 62.25 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="da summ">63.35 ± 0.50 / 15.11 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">45.46 ± 1.79 / 57.79 ± 1.31</td> <!-- Danske Talemaader -->
   <td class="da know">46.77 ± 2.98 / 64.61 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">12.19 ± 0.97 / 33.27 ± 0.89</td> <!-- HellaSwag-da -->
   <td class="no ner">49.57 ± 2.20 / 37.13 ± 2.52</td> <!-- NorNE-nb -->
   <td class="no ner">52.13 ± 3.94 / 38.26 ± 3.77</td> <!-- NorNE-nn -->
   <td class="no sent">39.96 ± 2.25 / 58.34 ± 1.66</td> <!-- NoReC -->
   <td class="no summ">58.99 ± 1.85 / 11.04 ± 1.25</td> <!-- No Sammendrag -->
   <td class="no la">3.20 ± 3.84 / 37.62 ± 4.94</td> <!-- ScaLA-nb -->
   <td class="no la">3.72 ± 3.66 / 38.51 ± 4.61</td> <!-- ScaLA-nn -->
   <td class="no rc">45.54 ± 3.50 / 68.67 ± 2.58</td> <!-- NorQuAD -->
   <td class="no know">21.88 ± 1.21 / 40.31 ± 1.01</td> <!-- MMLU-no -->
   <td class="no reason">14.24 ± 1.99 / 33.82 ± 1.72</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.06 ± 2.85 / 31.63 ± 3.67</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 1.09 / 67.88 ± 3.15</td> <!-- SweReC -->
   <td class="sv la">5.88 ± 3.89 / 38.51 ± 4.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.43 ± 1.04 / 62.93 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.73 ± 0.74 / 17.61 ± 0.49</td> <!-- SweDN -->
   <td class="sv know">27.05 ± 1.14 / 44.68 ± 0.87</td> <!-- MMLU-sv -->
   <td class="sv reason">13.30 ± 1.20 / 33.89 ± 1.04</td> <!-- HellaSwag-sv -->
   <td class="is ner">42.04 ± 3.53 / 25.31 ± 1.59</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 32.97 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is rc">24.07 ± 4.63 / 49.31 ± 4.59</td> <!-- NQiI -->
   <td class="is summ">61.80 ± 2.80 / 14.50 ± 2.00</td> <!-- RRN -->
   <td class="is know">13.79 ± 1.55 / 35.23 ± 1.26</td> <!-- ARC-is -->
   <td class="is reason">0.25 ± 2.45 / 48.10 ± 1.67</td> <!-- Winogrande-is -->
   <td class="de ner">49.85 ± 1.96 / 41.04 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.65 ± 1.58 / 65.94 ± 2.42</td> <!-- SB10k -->
   <td class="de la">3.17 ± 5.20 / 36.54 ± 5.71</td> <!-- ScaLA-de -->
   <td class="de rc">29.37 ± 3.48 / 58.09 ± 4.16</td> <!-- GermanQuAD -->
   <td class="de summ">67.96 ± 1.38 / 25.30 ± 2.54</td> <!-- MLSum -->
   <td class="de know">29.56 ± 0.63 / 46.21 ± 0.55</td> <!-- MMLU-de -->
   <td class="de reason">16.15 ± 1.34 / 35.40 ± 1.27</td> <!-- HellaSwag-de -->
   <td class="nl ner">47.40 ± 3.29 / 33.11 ± 2.04</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.98 / 30.71 ± 1.89</td> <!-- Dutch Social -->
   <td class="nl la">3.10 ± 1.93 / 34.24 ± 0.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.53 ± 1.48 / 68.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.27 ± 2.04 / 16.54 ± 1.58</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.18 ± 0.87 / 46.04 ± 0.54</td> <!-- MMLU-nl -->
   <td class="nl reason">10.34 ± 1.08 / 32.08 ± 1.06</td> <!-- HellaSwag-nl -->
   <td class="en ner">59.09 ± 1.44 / 52.03 ± 1.96</td> <!-- CoNLL-en -->
   <td class="en sent">63.29 ± 1.29 / 67.82 ± 0.74</td> <!-- SST5 -->
   <td class="en la">13.50 ± 4.14 / 50.33 ± 5.61</td> <!-- ScaLA-en -->
   <td class="en rc">68.15 ± 2.21 / 81.12 ± 1.18</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.51 / 22.02 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">40.10 ± 0.68 / 54.53 ± 0.48</td> <!-- MMLU -->
   <td class="en reason">20.88 ± 2.25 / 39.75 ± 1.62</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="da-rank">3.25</td> <!-- Danish rank -->
   <td class="no-rank">3.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.13</td> <!-- Swedish rank -->
   <td class="is-rank">4.38</td> <!-- Icelandic rank -->
   <td class="de-rank">2.15</td> <!-- German rank -->
   <td class="nl-rank">3.08</td> <!-- Dutch rank -->
   <td class="en-rank">1.97</td> <!-- English rank -->
   <td class="da ner">4.51 ± 2.12 / 3.71 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">40.85 ± 1.26 / 59.79 ± 1.32</td> <!-- Angry Tweets -->
   <td class="da la">5.43 ± 1.74 / 46.21 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da rc">51.76 ± 0.73 / 58.44 ± 0.54</td> <!-- ScandiQA-da -->
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
   <td class="no rc">37.08 ± 2.44 / 61.14 ± 2.01</td> <!-- NorQuAD -->
   <td class="no know">17.34 ± 0.74 / 38.04 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">17.43 ± 1.21 / 38.01 ± 0.91</td> <!-- HellaSwag-no -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.28 ± 0.86 / 15.52 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">22.99 ± 1.08 / 42.27 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">20.19 ± 0.99 / 40.11 ± 0.71</td> <!-- HellaSwag-sv -->
   <td class="is ner">27.22 ± 3.65 / 24.21 ± 2.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.31 ± 1.28 / 39.67 ± 4.39</td> <!-- ScaLA-is -->
   <td class="is rc">17.24 ± 2.72 / 41.15 ± 1.57</td> <!-- NQiI -->
   <td class="is summ">62.00 ± 1.66 / 15.80 ± 1.12</td> <!-- RRN -->
   <td class="is know">1.85 ± 1.18 / 26.88 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">1.06 ± 2.84 / 47.19 ± 2.14</td> <!-- Winogrande-is -->
   <td class="de ner">55.36 ± 0.81 / 36.14 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">53.05 ± 2.34 / 65.57 ± 1.92</td> <!-- SB10k -->
   <td class="de la">23.08 ± 1.54 / 58.65 ± 2.04</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 1.09 / 62.02 ± 2.17</td> <!-- GermanQuAD -->
   <td class="de summ">67.33 ± 0.98 / 24.07 ± 2.44</td> <!-- MLSum -->
   <td class="de know">39.57 ± 0.74 / 54.67 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">51.26 ± 0.93 / 63.03 ± 0.69</td> <!-- HellaSwag-de -->
   <td class="nl ner">44.27 ± 2.14 / 34.47 ± 2.48</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.84 ± 1.82 / 36.64 ± 1.13</td> <!-- Dutch Social -->
   <td class="nl la">10.44 ± 1.58 / 48.93 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.40 ± 1.14 / 68.02 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.60 ± 0.62 / 15.63 ± 0.45</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.63 ± 0.84 / 46.39 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">22.58 ± 0.97 / 41.78 ± 0.71</td> <!-- HellaSwag-nl -->
   <td class="en ner">64.09 ± 0.96 / 49.92 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">46.77 ± 4.36 / 60.99 ± 2.15</td> <!-- SST5 -->
   <td class="en la">31.62 ± 2.25 / 63.73 ± 1.79</td> <!-- ScaLA-en -->
   <td class="en rc">71.25 ± 0.83 / 85.72 ± 0.57</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.00</td> <!-- Danish rank -->
   <td class="no-rank">3.22</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.01</td> <!-- Swedish rank -->
   <td class="is-rank">4.47</td> <!-- Icelandic rank -->
   <td class="de-rank">2.68</td> <!-- German rank -->
   <td class="nl-rank">2.89</td> <!-- Dutch rank -->
   <td class="en-rank">2.09</td> <!-- English rank -->
   <td class="da ner">41.79 ± 2.11 / 32.67 ± 2.33</td> <!-- DANSK -->
   <td class="da sent">41.86 ± 1.28 / 61.22 ± 0.99</td> <!-- Angry Tweets -->
   <td class="da la">11.86 ± 1.80 / 50.92 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da rc">51.97 ± 0.76 / 59.28 ± 0.61</td> <!-- ScandiQA-da -->
   <td class="da summ">64.86 ± 0.75 / 19.26 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">29.55 ± 1.68 / 46.85 ± 1.40</td> <!-- Danske Talemaader -->
   <td class="da know">26.20 ± 2.23 / 51.29 ± 1.34</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.64 ± 0.91 / 27.01 ± 0.69</td> <!-- HellaSwag-da -->
   <td class="no ner">52.68 ± 2.02 / 46.01 ± 1.94</td> <!-- NorNE-nb -->
   <td class="no ner">53.17 ± 0.85 / 47.77 ± 2.12</td> <!-- NorNE-nn -->
   <td class="no sent">39.87 ± 1.73 / 55.71 ± 2.40</td> <!-- NoReC -->
   <td class="no summ">62.24 ± 0.54 / 14.11 ± 0.65</td> <!-- No Sammendrag -->
   <td class="no la">12.08 ± 2.13 / 51.41 ± 4.09</td> <!-- ScaLA-nb -->
   <td class="no la">7.18 ± 2.00 / 48.84 ± 3.17</td> <!-- ScaLA-nn -->
   <td class="no rc">36.00 ± 2.29 / 61.00 ± 2.15</td> <!-- NorQuAD -->
   <td class="no know">15.78 ± 1.22 / 36.32 ± 0.86</td> <!-- MMLU-no -->
   <td class="no reason">9.98 ± 1.73 / 31.35 ± 1.65</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.23 ± 3.64 / 37.99 ± 4.03</td> <!-- SUC3 -->
   <td class="sv sent">72.76 ± 2.25 / 72.65 ± 2.38</td> <!-- SweReC -->
   <td class="sv la">11.25 ± 2.04 / 51.22 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.22 ± 0.70 / 59.36 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.56 ± 0.78 / 17.51 ± 0.44</td> <!-- SweDN -->
   <td class="sv know">18.14 ± 1.00 / 38.28 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">6.77 ± 1.16 / 28.93 ± 0.94</td> <!-- HellaSwag-sv -->
   <td class="is ner">30.21 ± 4.29 / 29.79 ± 3.81</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.67 ± 1.87 / 48.02 ± 3.06</td> <!-- ScaLA-is -->
   <td class="is rc">15.12 ± 1.65 / 40.55 ± 1.13</td> <!-- NQiI -->
   <td class="is summ">56.75 ± 2.25 / 10.37 ± 1.58</td> <!-- RRN -->
   <td class="is know">3.22 ± 0.92 / 27.64 ± 0.84</td> <!-- ARC-is -->
   <td class="is reason">1.88 ± 2.37 / 49.26 ± 1.60</td> <!-- Winogrande-is -->
   <td class="de ner">53.30 ± 0.87 / 47.62 ± 1.30</td> <!-- GermEval -->
   <td class="de sent">44.95 ± 3.84 / 62.77 ± 2.82</td> <!-- SB10k -->
   <td class="de la">18.67 ± 1.83 / 57.35 ± 3.01</td> <!-- ScaLA-de -->
   <td class="de rc">28.10 ± 1.17 / 58.38 ± 1.45</td> <!-- GermanQuAD -->
   <td class="de summ">65.95 ± 0.58 / 20.96 ± 1.39</td> <!-- MLSum -->
   <td class="de know">23.84 ± 0.97 / 42.69 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">16.86 ± 1.12 / 35.87 ± 1.30</td> <!-- HellaSwag-de -->
   <td class="nl ner">52.52 ± 1.62 / 44.69 ± 2.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.85 ± 1.90 / 36.43 ± 2.11</td> <!-- Dutch Social -->
   <td class="nl la">17.72 ± 1.86 / 57.31 ± 1.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.50 ± 1.16 / 67.02 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.23 ± 0.48 / 18.18 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.62 ± 0.65 / 43.32 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">15.79 ± 1.37 / 35.56 ± 1.11</td> <!-- HellaSwag-nl -->
   <td class="en ner">61.97 ± 1.74 / 54.58 ± 1.53</td> <!-- CoNLL-en -->
   <td class="en sent">67.54 ± 1.33 / 66.16 ± 1.54</td> <!-- SST5 -->
   <td class="en la">31.70 ± 2.00 / 65.43 ± 1.09</td> <!-- ScaLA-en -->
   <td class="en rc">59.78 ± 1.66 / 78.74 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">68.61 ± 0.41 / 24.36 ± 0.58</td> <!-- CNN-DailyMail -->
   <td class="en know">39.82 ± 0.91 / 54.59 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">57.51 ± 0.92 / 67.67 ± 0.71</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.00</td> <!-- Danish rank -->
   <td class="no-rank">3.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.95</td> <!-- Swedish rank -->
   <td class="is-rank">4.21</td> <!-- Icelandic rank -->
   <td class="de-rank">2.65</td> <!-- German rank -->
   <td class="nl-rank">3.04</td> <!-- Dutch rank -->
   <td class="en-rank">2.39</td> <!-- English rank -->
   <td class="da ner">48.44 ± 1.69 / 36.99 ± 1.77</td> <!-- DANSK -->
   <td class="da sent">39.07 ± 1.03 / 56.85 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">9.72 ± 1.58 / 46.85 ± 3.66</td> <!-- ScaLA-da -->
   <td class="da rc">51.18 ± 0.92 / 56.54 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">63.93 ± 0.79 / 17.49 ± 0.73</td> <!-- Nordjylland-News -->
   <td class="da know">33.11 ± 2.59 / 49.31 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">18.96 ± 2.16 / 46.29 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.03 ± 1.28 / 31.42 ± 1.04</td> <!-- HellaSwag-da -->
   <td class="no ner">68.40 ± 1.16 / 62.53 ± 1.69</td> <!-- NorNE-nb -->
   <td class="no ner">65.15 ± 0.79 / 60.39 ± 2.11</td> <!-- NorNE-nn -->
   <td class="no sent">42.00 ± 1.78 / 59.90 ± 1.22</td> <!-- NoReC -->
   <td class="no summ">61.27 ± 0.80 / 13.34 ± 0.66</td> <!-- No Sammendrag -->
   <td class="no la">5.20 ± 2.23 / 36.33 ± 1.30</td> <!-- ScaLA-nb -->
   <td class="no la">3.32 ± 2.02 / 37.81 ± 3.26</td> <!-- ScaLA-nn -->
   <td class="no rc">37.51 ± 2.58 / 60.94 ± 3.06</td> <!-- NorQuAD -->
   <td class="no know">12.42 ± 1.42 / 34.82 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">8.32 ± 0.78 / 30.87 ± 0.75</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.77 ± 3.55 / 45.71 ± 4.91</td> <!-- SUC3 -->
   <td class="sv sent">74.45 ± 1.19 / 72.26 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">3.97 ± 1.50 / 34.79 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 1.05 / 56.07 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.61 ± 0.55 / 17.92 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">14.34 ± 0.73 / 35.93 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">7.40 ± 1.39 / 30.20 ± 1.23</td> <!-- HellaSwag-sv -->
   <td class="is ner">50.89 ± 2.90 / 35.75 ± 4.67</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.50 ± 0.94 / 33.77 ± 0.30</td> <!-- ScaLA-is -->
   <td class="is rc">17.43 ± 3.38 / 41.32 ± 3.18</td> <!-- NQiI -->
   <td class="is summ">59.94 ± 2.87 / 12.62 ± 1.91</td> <!-- RRN -->
   <td class="is know">5.52 ± 1.26 / 28.97 ± 0.97</td> <!-- ARC-is -->
   <td class="is reason">1.73 ± 2.31 / 50.89 ± 3.35</td> <!-- Winogrande-is -->
   <td class="de ner">59.07 ± 0.78 / 51.00 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.44 / 65.93 ± 1.66</td> <!-- SB10k -->
   <td class="de la">14.71 ± 2.21 / 53.75 ± 3.07</td> <!-- ScaLA-de -->
   <td class="de rc">29.45 ± 2.13 / 56.14 ± 2.53</td> <!-- GermanQuAD -->
   <td class="de summ">67.78 ± 1.54 / 26.66 ± 3.40</td> <!-- MLSum -->
   <td class="de know">16.39 ± 1.29 / 37.35 ± 0.95</td> <!-- MMLU-de -->
   <td class="de reason">10.68 ± 1.41 / 32.52 ± 1.35</td> <!-- HellaSwag-de -->
   <td class="nl ner">63.29 ± 2.51 / 52.18 ± 4.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.81 ± 1.66 / 36.99 ± 2.58</td> <!-- Dutch Social -->
   <td class="nl la">8.16 ± 1.97 / 44.29 ± 4.25</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.64 ± 0.68 / 66.29 ± 0.71</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.08 ± 0.90 / 15.69 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">16.86 ± 1.16 / 37.54 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">6.24 ± 0.78 / 29.25 ± 0.61</td> <!-- HellaSwag-nl -->
   <td class="en ner">72.76 ± 0.57 / 67.49 ± 0.90</td> <!-- CoNLL-en -->
   <td class="en sent">62.35 ± 1.68 / 67.34 ± 0.77</td> <!-- SST5 -->
   <td class="en la">21.57 ± 2.22 / 59.22 ± 1.69</td> <!-- ScaLA-en -->
   <td class="en rc">69.80 ± 3.60 / 81.37 ± 2.26</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.60 / 23.48 ± 0.91</td> <!-- CNN-DailyMail -->
   <td class="en know">25.63 ± 0.81 / 44.26 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">16.44 ± 1.84 / 36.73 ± 1.54</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="da-rank">2.96</td> <!-- Danish rank -->
   <td class="no-rank">3.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.13</td> <!-- Swedish rank -->
   <td class="is-rank">4.24</td> <!-- Icelandic rank -->
   <td class="de-rank">2.95</td> <!-- German rank -->
   <td class="nl-rank">3.08</td> <!-- Dutch rank -->
   <td class="en-rank">2.25</td> <!-- English rank -->
   <td class="da ner">43.83 ± 1.93 / 34.03 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">29.21 ± 1.92 / 52.86 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">12.96 ± 1.67 / 55.83 ± 0.88</td> <!-- ScaLA-da -->
   <td class="da rc">49.76 ± 0.59 / 56.52 ± 0.50</td> <!-- ScandiQA-da -->
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
   <td class="no rc">51.08 ± 2.83 / 74.34 ± 1.55</td> <!-- NorQuAD -->
   <td class="no know">19.07 ± 1.42 / 37.82 ± 1.42</td> <!-- MMLU-no -->
   <td class="no reason">16.52 ± 1.25 / 35.24 ± 1.25</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.88 ± 0.30 / 18.58 ± 0.16</td> <!-- SweDN -->
   <td class="sv know">17.95 ± 1.18 / 36.41 ± 1.02</td> <!-- MMLU-sv -->
   <td class="sv reason">13.55 ± 1.32 / 33.39 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">37.69 ± 3.97 / 34.52 ± 3.74</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.11 ± 1.49 / 48.48 ± 2.77</td> <!-- ScaLA-is -->
   <td class="is rc">18.34 ± 2.07 / 43.26 ± 1.28</td> <!-- NQiI -->
   <td class="is summ">63.71 ± 1.04 / 16.63 ± 0.98</td> <!-- RRN -->
   <td class="is know">7.70 ± 1.44 / 28.98 ± 1.20</td> <!-- ARC-is -->
   <td class="is reason">-5.17 ± 2.94 / 53.84 ± 1.87</td> <!-- Winogrande-is -->
   <td class="de ner">54.20 ± 1.00 / 48.58 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">15.43 ± 3.70 / 43.11 ± 2.77</td> <!-- SB10k -->
   <td class="de la">17.49 ± 1.23 / 57.46 ± 1.12</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 5.36 / 60.07 ± 4.46</td> <!-- GermanQuAD -->
   <td class="de summ">64.87 ± 0.47 / 22.25 ± 1.89</td> <!-- MLSum -->
   <td class="de know">22.10 ± 0.68 / 40.39 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">18.58 ± 1.48 / 36.49 ± 1.24</td> <!-- HellaSwag-de -->
   <td class="nl ner">53.93 ± 2.71 / 47.48 ± 2.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.83 ± 2.37 / 34.00 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">6.58 ± 3.36 / 48.51 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.45 ± 2.52 / 67.47 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.89 ± 0.38 / 17.99 ± 0.46</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">19.58 ± 1.24 / 38.76 ± 1.06</td> <!-- MMLU-nl -->
   <td class="nl reason">13.68 ± 1.08 / 32.30 ± 0.99</td> <!-- HellaSwag-nl -->
   <td class="en ner">66.70 ± 0.99 / 61.08 ± 1.16</td> <!-- CoNLL-en -->
   <td class="en sent">55.62 ± 2.54 / 64.98 ± 2.03</td> <!-- SST5 -->
   <td class="en la">31.36 ± 2.63 / 65.21 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">72.58 ± 0.68 / 84.67 ± 0.91</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="da-rank">2.85</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.97</td> <!-- Swedish rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="de-rank">2.73</td> <!-- German rank -->
   <td class="nl-rank">3.11</td> <!-- Dutch rank -->
   <td class="en-rank">2.38</td> <!-- English rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da rc">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
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
   <td class="no rc">33.77 ± 2.11 / 61.99 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">14.81 ± 0.79 / 34.79 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">12.69 ± 0.77 / 31.84 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.92 ± 0.05 / 18.51 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">17.73 ± 0.98 / 37.55 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">12.85 ± 0.93 / 33.37 ± 0.90</td> <!-- HellaSwag-sv -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is rc">16.13 ± 2.52 / 39.51 ± 1.98</td> <!-- NQiI -->
   <td class="is summ">62.30 ± 0.90 / 13.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.16 ± 0.79 / 27.40 ± 0.79</td> <!-- ARC-is -->
   <td class="is reason">1.84 ± 2.19 / 43.79 ± 0.73</td> <!-- Winogrande-is -->
   <td class="de ner">50.09 ± 1.33 / 38.59 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">46.52 ± 2.85 / 63.64 ± 2.10</td> <!-- SB10k -->
   <td class="de la">15.23 ± 1.71 / 55.08 ± 1.88</td> <!-- ScaLA-de -->
   <td class="de rc">25.54 ± 3.58 / 56.07 ± 3.76</td> <!-- GermanQuAD -->
   <td class="de summ">67.62 ± 0.89 / 23.52 ± 2.43</td> <!-- MLSum -->
   <td class="de know">20.12 ± 1.13 / 39.48 ± 1.02</td> <!-- MMLU-de -->
   <td class="de reason">13.98 ± 1.56 / 34.07 ± 1.30</td> <!-- HellaSwag-de -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.59 ± 0.56 / 18.45 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.19 ± 1.26 / 39.24 ± 1.03</td> <!-- MMLU-nl -->
   <td class="nl reason">11.42 ± 1.29 / 32.50 ± 1.10</td> <!-- HellaSwag-nl -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en rc">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="da-rank">3.20</td> <!-- Danish rank -->
   <td class="no-rank">3.32</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.10</td> <!-- Swedish rank -->
   <td class="is-rank">4.56</td> <!-- Icelandic rank -->
   <td class="de-rank">2.64</td> <!-- German rank -->
   <td class="nl-rank">2.90</td> <!-- Dutch rank -->
   <td class="en-rank">2.07</td> <!-- English rank -->
   <td class="da ner">32.34 ± 3.77 / 24.48 ± 3.17</td> <!-- DANSK -->
   <td class="da sent">29.50 ± 3.63 / 42.61 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">3.89 ± 1.49 / 37.29 ± 3.65</td> <!-- ScaLA-da -->
   <td class="da rc">53.67 ± 0.84 / 59.15 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">64.48 ± 0.83 / 19.25 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">24.40 ± 2.55 / 42.44 ± 1.87</td> <!-- Danske Talemaader -->
   <td class="da know">31.93 ± 1.90 / 54.43 ± 1.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">10.00 ± 1.73 / 32.31 ± 0.87</td> <!-- HellaSwag-da -->
   <td class="no ner">43.00 ± 2.81 / 35.39 ± 2.28</td> <!-- NorNE-nb -->
   <td class="no ner">45.08 ± 0.83 / 38.16 ± 1.91</td> <!-- NorNE-nn -->
   <td class="no sent">35.36 ± 2.31 / 54.88 ± 2.08</td> <!-- NoReC -->
   <td class="no summ">62.00 ± 0.62 / 14.22 ± 0.76</td> <!-- No Sammendrag -->
   <td class="no la">2.79 ± 1.92 / 41.90 ± 4.62</td> <!-- ScaLA-nb -->
   <td class="no la">1.95 ± 2.02 / 38.91 ± 3.27</td> <!-- ScaLA-nn -->
   <td class="no rc">37.33 ± 3.11 / 59.74 ± 2.74</td> <!-- NorQuAD -->
   <td class="no know">15.76 ± 1.18 / 36.68 ± 0.90</td> <!-- MMLU-no -->
   <td class="no reason">12.98 ± 1.32 / 34.07 ± 1.34</td> <!-- HellaSwag-no -->
   <td class="sv ner">36.54 ± 2.70 / 28.79 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">68.85 ± 5.19 / 70.02 ± 3.95</td> <!-- SweReC -->
   <td class="sv la">2.60 ± 2.58 / 40.21 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.58 ± 0.89 / 59.78 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.77 ± 1.85 / 17.01 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">16.19 ± 1.01 / 37.23 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">14.06 ± 1.52 / 34.80 ± 1.35</td> <!-- HellaSwag-sv -->
   <td class="is ner">29.51 ± 2.44 / 29.14 ± 2.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.32 ± 0.63 / 33.70 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.36 ± 2.12 / 34.06 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">59.43 ± 1.83 / 13.09 ± 1.58</td> <!-- RRN -->
   <td class="is know">2.35 ± 1.26 / 27.85 ± 0.87</td> <!-- ARC-is -->
   <td class="is reason">0.01 ± 2.73 / 45.18 ± 1.36</td> <!-- Winogrande-is -->
   <td class="de ner">45.81 ± 1.27 / 39.33 ± 2.24</td> <!-- GermEval -->
   <td class="de sent">34.61 ± 3.47 / 44.53 ± 3.65</td> <!-- SB10k -->
   <td class="de la">16.19 ± 3.33 / 54.43 ± 3.53</td> <!-- ScaLA-de -->
   <td class="de rc">28.25 ± 4.10 / 57.52 ± 4.47</td> <!-- GermanQuAD -->
   <td class="de summ">67.90 ± 0.72 / 26.38 ± 1.63</td> <!-- MLSum -->
   <td class="de know">28.28 ± 0.88 / 46.06 ± 0.73</td> <!-- MMLU-de -->
   <td class="de reason">28.25 ± 2.23 / 45.60 ± 2.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">47.28 ± 1.57 / 36.12 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.12 ± 1.92 / 35.44 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">12.74 ± 2.68 / 52.69 ± 2.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.36 ± 1.36 / 71.20 ± 0.77</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.26 ± 0.75 / 16.55 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.88 ± 0.86 / 44.76 ± 0.70</td> <!-- MMLU-nl -->
   <td class="nl reason">34.05 ± 1.57 / 50.08 ± 1.18</td> <!-- HellaSwag-nl -->
   <td class="en ner">57.78 ± 1.91 / 50.30 ± 2.29</td> <!-- CoNLL-en -->
   <td class="en sent">67.81 ± 1.00 / 61.89 ± 1.51</td> <!-- SST5 -->
   <td class="en la">22.81 ± 2.71 / 60.07 ± 2.49</td> <!-- ScaLA-en -->
   <td class="en rc">72.90 ± 1.16 / 83.67 ± 0.66</td> <!-- SQuAD -->
   <td class="en summ">67.33 ± 0.41 / 22.76 ± 0.60</td> <!-- CNN-DailyMail -->
   <td class="en know">37.80 ± 0.99 / 53.52 ± 0.78</td> <!-- MMLU -->
   <td class="en reason">67.23 ± 0.96 / 75.34 ± 0.74</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da-rank">2.93</td> <!-- Danish rank -->
   <td class="no-rank">3.30</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.04</td> <!-- Swedish rank -->
   <td class="is-rank">4.53</td> <!-- Icelandic rank -->
   <td class="de-rank">2.78</td> <!-- German rank -->
   <td class="nl-rank">3.13</td> <!-- Dutch rank -->
   <td class="en-rank">2.25</td> <!-- English rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da rc">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
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
   <td class="no rc">42.55 ± 3.36 / 67.11 ± 2.50</td> <!-- NorQuAD -->
   <td class="no know">17.00 ± 1.21 / 37.67 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">16.18 ± 1.00 / 36.91 ± 0.64</td> <!-- HellaSwag-no -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.90 ± 0.87 / 17.34 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">20.95 ± 0.97 / 40.87 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">16.59 ± 1.45 / 36.76 ± 1.20</td> <!-- HellaSwag-sv -->
   <td class="is ner">25.65 ± 2.99 / 22.30 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is rc">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="is summ">62.11 ± 2.22 / 14.98 ± 1.53</td> <!-- RRN -->
   <td class="is know">4.50 ± 1.47 / 28.86 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">-1.89 ± 2.66 / 43.72 ± 0.92</td> <!-- Winogrande-is -->
   <td class="de ner">42.08 ± 1.65 / 36.90 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td class="de summ">65.56 ± 1.65 / 20.45 ± 2.68</td> <!-- MLSum -->
   <td class="de know">23.76 ± 0.70 / 42.77 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">20.92 ± 1.16 / 40.56 ± 0.86</td> <!-- HellaSwag-de -->
   <td class="nl ner">42.52 ± 2.25 / 37.46 ± 3.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.75 ± 0.84 / 14.83 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.25 ± 1.22 / 43.08 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">16.21 ± 1.51 / 37.11 ± 1.16</td> <!-- HellaSwag-nl -->
   <td class="en ner">58.56 ± 1.99 / 54.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en rc">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="da-rank">3.02</td> <!-- Danish rank -->
   <td class="no-rank">3.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.89</td> <!-- Swedish rank -->
   <td class="is-rank">4.38</td> <!-- Icelandic rank -->
   <td class="de-rank">2.74</td> <!-- German rank -->
   <td class="nl-rank">3.36</td> <!-- Dutch rank -->
   <td class="en-rank">2.47</td> <!-- English rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
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
   <td class="no rc">44.19 ± 4.13 / 66.18 ± 4.05</td> <!-- NorQuAD -->
   <td class="no know">14.48 ± 1.33 / 35.35 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">6.49 ± 1.39 / 28.64 ± 0.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.63 ± 0.39 / 18.68 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">15.65 ± 0.55 / 36.32 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">8.74 ± 1.34 / 29.87 ± 1.40</td> <!-- HellaSwag-sv -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is rc">18.04 ± 4.05 / 41.40 ± 3.27</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.33 / 26.91 ± 1.00</td> <!-- ARC-is -->
   <td class="is reason">-0.00 ± 2.41 / 44.93 ± 0.92</td> <!-- Winogrande-is -->
   <td class="de ner">43.02 ± 1.93 / 32.69 ± 1.98</td> <!-- GermEval -->
   <td class="de sent">50.21 ± 2.43 / 65.81 ± 1.82</td> <!-- SB10k -->
   <td class="de la">15.79 ± 2.35 / 53.25 ± 4.45</td> <!-- ScaLA-de -->
   <td class="de rc">28.57 ± 5.09 / 55.54 ± 6.14</td> <!-- GermanQuAD -->
   <td class="de summ">68.68 ± 0.96 / 26.95 ± 1.81</td> <!-- MLSum -->
   <td class="de know">18.38 ± 1.36 / 38.12 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">8.45 ± 1.86 / 30.07 ± 1.49</td> <!-- HellaSwag-de -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.92 ± 0.61 / 70.24 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.58 ± 1.13 / 16.33 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.36 ± 1.12 / 37.44 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">6.68 ± 1.82 / 29.30 ± 1.02</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en rc">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.04</td> <!-- Swedish rank -->
   <td class="is-rank">4.55</td> <!-- Icelandic rank -->
   <td class="de-rank">2.78</td> <!-- German rank -->
   <td class="nl-rank">3.16</td> <!-- Dutch rank -->
   <td class="en-rank">2.45</td> <!-- English rank -->
   <td class="da ner">45.90 ± 2.53 / 33.00 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">37.11 ± 1.88 / 56.47 ± 1.59</td> <!-- Angry Tweets -->
   <td class="da la">11.70 ± 2.16 / 50.31 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">50.11 ± 0.83 / 55.71 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">63.86 ± 0.96 / 18.38 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">32.44 ± 2.29 / 46.63 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">7.46 ± 1.83 / 39.41 ± 1.17</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.62 ± 1.16 / 28.71 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">66.91 ± 1.50 / 54.98 ± 2.20</td> <!-- NorNE-nb -->
   <td class="no ner">62.82 ± 1.23 / 53.14 ± 3.17</td> <!-- NorNE-nn -->
   <td class="no sent">40.71 ± 1.63 / 59.35 ± 1.58</td> <!-- NoReC -->
   <td class="no summ">60.59 ± 0.99 / 12.74 ± 0.82</td> <!-- No Sammendrag -->
   <td class="no la">9.50 ± 1.68 / 46.31 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">6.74 ± 1.70 / 42.10 ± 4.67</td> <!-- ScaLA-nn -->
   <td class="no rc">32.83 ± 1.83 / 55.30 ± 2.35</td> <!-- NorQuAD -->
   <td class="no know">11.35 ± 1.23 / 32.01 ± 0.91</td> <!-- MMLU-no -->
   <td class="no reason">6.21 ± 0.99 / 29.05 ± 0.80</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.85 ± 2.76 / 35.11 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">73.93 ± 1.58 / 73.97 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">8.27 ± 2.90 / 43.29 ± 4.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.49 ± 0.77 / 54.50 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.98 ± 0.80 / 16.18 ± 0.48</td> <!-- SweDN -->
   <td class="sv know">13.69 ± 0.86 / 33.34 ± 0.46</td> <!-- MMLU-sv -->
   <td class="sv reason">5.68 ± 1.13 / 27.99 ± 1.11</td> <!-- HellaSwag-sv -->
   <td class="is ner">43.20 ± 3.61 / 32.10 ± 3.76</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">14.28 ± 2.94 / 38.21 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">49.66 ± 3.28 / 7.97 ± 1.43</td> <!-- RRN -->
   <td class="is know">3.07 ± 1.66 / 25.74 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">2.79 ± 3.13 / 47.97 ± 1.43</td> <!-- Winogrande-is -->
   <td class="de ner">54.45 ± 1.17 / 42.36 ± 2.59</td> <!-- GermEval -->
   <td class="de sent">43.62 ± 3.18 / 59.82 ± 2.70</td> <!-- SB10k -->
   <td class="de la">15.24 ± 1.87 / 55.49 ± 2.89</td> <!-- ScaLA-de -->
   <td class="de rc">26.00 ± 2.28 / 51.82 ± 2.70</td> <!-- GermanQuAD -->
   <td class="de summ">66.68 ± 1.30 / 24.80 ± 3.14</td> <!-- MLSum -->
   <td class="de know">15.81 ± 1.07 / 36.18 ± 0.94</td> <!-- MMLU-de -->
   <td class="de reason">9.60 ± 1.12 / 31.31 ± 1.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">60.72 ± 2.14 / 45.52 ± 2.46</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.38 ± 1.62 / 29.91 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">10.96 ± 1.47 / 47.97 ± 3.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.20 ± 0.91 / 61.75 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.23 ± 0.96 / 16.22 ± 0.74</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">15.26 ± 0.67 / 35.76 ± 0.34</td> <!-- MMLU-nl -->
   <td class="nl reason">4.03 ± 0.90 / 27.17 ± 0.73</td> <!-- HellaSwag-nl -->
   <td class="en ner">72.59 ± 0.91 / 65.83 ± 1.30</td> <!-- CoNLL-en -->
   <td class="en sent">61.61 ± 1.45 / 67.09 ± 1.38</td> <!-- SST5 -->
   <td class="en la">18.37 ± 2.07 / 56.26 ± 2.62</td> <!-- ScaLA-en -->
   <td class="en rc">66.68 ± 3.56 / 78.95 ± 2.38</td> <!-- SQuAD -->
   <td class="en summ">68.41 ± 0.33 / 24.66 ± 0.47</td> <!-- CNN-DailyMail -->
   <td class="en know">24.14 ± 0.58 / 42.17 ± 0.33</td> <!-- MMLU -->
   <td class="en reason">14.42 ± 2.00 / 34.50 ± 1.81</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="da-rank">3.30</td> <!-- Danish rank -->
   <td class="no-rank">3.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.86</td> <!-- Swedish rank -->
   <td class="is-rank">4.67</td> <!-- Icelandic rank -->
   <td class="de-rank">3.02</td> <!-- German rank -->
   <td class="nl-rank">3.33</td> <!-- Dutch rank -->
   <td class="en-rank">2.02</td> <!-- English rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da rc">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
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
   <td class="no rc">40.28 ± 3.58 / 62.78 ± 3.34</td> <!-- NorQuAD -->
   <td class="no know">23.14 ± 0.98 / 41.88 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">16.50 ± 1.60 / 36.98 ± 1.27</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.95 ± 0.86 / 60.77 ± 0.75</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.70 ± 0.76 / 17.52 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">25.28 ± 0.72 / 43.71 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">19.20 ± 1.18 / 38.76 ± 0.96</td> <!-- HellaSwag-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is rc">16.91 ± 2.57 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="is summ">60.02 ± 3.15 / 14.22 ± 1.52</td> <!-- RRN -->
   <td class="is know">4.35 ± 1.25 / 28.94 ± 1.09</td> <!-- ARC-is -->
   <td class="is reason">0.72 ± 2.33 / 52.54 ± 2.18</td> <!-- Winogrande-is -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 2.45 / 67.63 ± 1.87</td> <!-- SB10k -->
   <td class="de la">7.33 ± 2.53 / 37.69 ± 2.51</td> <!-- ScaLA-de -->
   <td class="de rc">30.05 ± 1.59 / 57.13 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.09 ± 1.28 / 23.20 ± 2.54</td> <!-- MLSum -->
   <td class="de know">30.33 ± 0.78 / 47.68 ± 0.54</td> <!-- MMLU-de -->
   <td class="de reason">22.89 ± 1.14 / 41.15 ± 1.08</td> <!-- HellaSwag-de -->
   <td class="nl ner">46.34 ± 2.00 / 33.30 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.96 ± 1.44 / 18.10 ± 2.39</td> <!-- Dutch Social -->
   <td class="nl la">0.88 ± 1.23 / 33.53 ± 0.48</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.33 ± 1.28 / 66.50 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.35 ± 1.57 / 14.29 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.33 ± 0.91 / 46.94 ± 0.68</td> <!-- MMLU-nl -->
   <td class="nl reason">20.27 ± 1.38 / 39.32 ± 1.12</td> <!-- HellaSwag-nl -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en rc">75.89 ± 1.84 / 85.86 ± 1.03</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="da-rank">3.27</td> <!-- Danish rank -->
   <td class="no-rank">3.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.19</td> <!-- Swedish rank -->
   <td class="is-rank">4.54</td> <!-- Icelandic rank -->
   <td class="de-rank">2.73</td> <!-- German rank -->
   <td class="nl-rank">3.15</td> <!-- Dutch rank -->
   <td class="en-rank">2.42</td> <!-- English rank -->
   <td class="da ner">37.37 ± 2.46 / 26.81 ± 2.24</td> <!-- DANSK -->
   <td class="da sent">31.44 ± 1.82 / 48.96 ± 2.35</td> <!-- Angry Tweets -->
   <td class="da la">5.27 ± 2.40 / 40.63 ± 4.68</td> <!-- ScaLA-da -->
   <td class="da rc">48.41 ± 1.10 / 55.05 ± 0.97</td> <!-- ScandiQA-da -->
   <td class="da summ">63.82 ± 0.97 / 18.09 ± 0.88</td> <!-- Nordjylland-News -->
   <td class="da know">18.25 ± 1.54 / 38.38 ± 1.12</td> <!-- Danske Talemaader -->
   <td class="da know">19.54 ± 2.59 / 46.35 ± 1.91</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.64 ± 1.03 / 26.88 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">44.89 ± 2.26 / 34.93 ± 2.45</td> <!-- NorNE-nb -->
   <td class="no ner">48.08 ± 1.68 / 34.39 ± 2.61</td> <!-- NorNE-nn -->
   <td class="no sent">32.29 ± 1.15 / 51.91 ± 2.66</td> <!-- NoReC -->
   <td class="no summ">59.77 ± 0.91 / 11.96 ± 0.65</td> <!-- No Sammendrag -->
   <td class="no la">7.49 ± 1.65 / 47.79 ± 3.81</td> <!-- ScaLA-nb -->
   <td class="no la">4.65 ± 1.91 / 45.75 ± 5.13</td> <!-- ScaLA-nn -->
   <td class="no rc">26.37 ± 1.51 / 47.59 ± 2.41</td> <!-- NorQuAD -->
   <td class="no know">11.54 ± 1.37 / 32.89 ± 1.10</td> <!-- MMLU-no -->
   <td class="no reason">3.42 ± 1.93 / 26.93 ± 1.47</td> <!-- HellaSwag-no -->
   <td class="sv ner">40.68 ± 2.32 / 24.33 ± 2.43</td> <!-- SUC3 -->
   <td class="sv sent">68.96 ± 2.04 / 72.76 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">4.77 ± 1.97 / 43.64 ± 5.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.73 ± 0.76 / 56.63 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.93 ± 0.49 / 14.76 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">13.55 ± 1.27 / 34.97 ± 0.99</td> <!-- MMLU-sv -->
   <td class="sv reason">5.27 ± 1.49 / 27.92 ± 1.10</td> <!-- HellaSwag-sv -->
   <td class="is ner">23.14 ± 2.08 / 23.09 ± 2.24</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.18 ± 1.67 / 33.93 ± 0.34</td> <!-- ScaLA-is -->
   <td class="is rc">14.15 ± 2.49 / 36.10 ± 1.65</td> <!-- NQiI -->
   <td class="is summ">60.80 ± 0.81 / 10.79 ± 1.85</td> <!-- RRN -->
   <td class="is know">2.86 ± 1.31 / 26.61 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">-1.31 ± 2.24 / 50.29 ± 1.93</td> <!-- Winogrande-is -->
   <td class="de ner">47.31 ± 1.67 / 31.36 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">48.28 ± 4.28 / 64.07 ± 3.81</td> <!-- SB10k -->
   <td class="de la">14.08 ± 1.29 / 52.67 ± 2.70</td> <!-- ScaLA-de -->
   <td class="de rc">28.37 ± 4.07 / 55.92 ± 4.76</td> <!-- GermanQuAD -->
   <td class="de summ">61.97 ± 1.94 / 19.06 ± 1.18</td> <!-- MLSum -->
   <td class="de know">22.99 ± 0.83 / 41.98 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">20.06 ± 1.95 / 38.69 ± 1.78</td> <!-- HellaSwag-de -->
   <td class="nl ner">49.25 ± 2.57 / 36.48 ± 2.14</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.45 ± 1.76 / 39.66 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">11.87 ± 2.68 / 47.32 ± 3.85</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 1.44 / 67.04 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.96 / 16.74 ± 0.86</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">21.52 ± 1.18 / 40.76 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">22.32 ± 2.02 / 39.89 ± 1.82</td> <!-- HellaSwag-nl -->
   <td class="en ner">52.79 ± 4.09 / 43.45 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">65.92 ± 1.02 / 70.47 ± 0.75</td> <!-- SST5 -->
   <td class="en la">16.74 ± 2.67 / 55.45 ± 3.35</td> <!-- ScaLA-en -->
   <td class="en rc">64.92 ± 2.84 / 80.88 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">65.50 ± 0.97 / 21.90 ± 0.40</td> <!-- CNN-DailyMail -->
   <td class="en know">33.84 ± 0.87 / 50.07 ± 0.67</td> <!-- MMLU -->
   <td class="en reason">49.84 ± 1.22 / 61.87 ± 1.03</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="da-rank">3.14</td> <!-- Danish rank -->
   <td class="no-rank">3.42</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.16</td> <!-- Swedish rank -->
   <td class="is-rank">3.99</td> <!-- Icelandic rank -->
   <td class="de-rank">2.97</td> <!-- German rank -->
   <td class="nl-rank">3.42</td> <!-- Dutch rank -->
   <td class="en-rank">2.99</td> <!-- English rank -->
   <td class="da ner">34.25 ± 2.28 / 30.39 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">45.67 ± 2.41 / 58.41 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">10.62 ± 2.37 / 53.20 ± 3.73</td> <!-- ScaLA-da -->
   <td class="da rc">50.77 ± 2.48 / 56.92 ± 2.42</td> <!-- ScandiQA-da -->
   <td class="da summ">65.67 ± 1.05 / 19.97 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">2.31 ± 1.92 / 24.65 ± 1.65</td> <!-- Danske Talemaader -->
   <td class="da know">10.57 ± 2.47 / 40.33 ± 1.67</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.64 ± 1.55 / 25.40 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">42.77 ± 2.42 / 40.31 ± 2.34</td> <!-- NorNE-nb -->
   <td class="no ner">45.69 ± 3.69 / 43.11 ± 3.62</td> <!-- NorNE-nn -->
   <td class="no sent">37.79 ± 2.38 / 56.41 ± 2.91</td> <!-- NoReC -->
   <td class="no summ">61.05 ± 1.44 / 13.39 ± 1.24</td> <!-- No Sammendrag -->
   <td class="no la">8.77 ± 1.96 / 49.11 ± 4.22</td> <!-- ScaLA-nb -->
   <td class="no la">8.47 ± 3.16 / 49.65 ± 4.39</td> <!-- ScaLA-nn -->
   <td class="no rc">44.24 ± 4.15 / 65.11 ± 3.79</td> <!-- NorQuAD -->
   <td class="no know">-1.34 ± 1.57 / 22.60 ± 0.91</td> <!-- MMLU-no -->
   <td class="no reason">-0.94 ± 1.03 / 24.17 ± 0.64</td> <!-- HellaSwag-no -->
   <td class="sv ner">42.87 ± 3.17 / 40.34 ± 2.52</td> <!-- SUC3 -->
   <td class="sv sent">79.18 ± 0.46 / 76.66 ± 1.44</td> <!-- SweReC -->
   <td class="sv la">8.65 ± 1.60 / 46.95 ± 3.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.56 ± 0.79 / 57.58 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.66 ± 0.41 / 18.04 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">2.37 ± 1.04 / 24.51 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">0.17 ± 0.83 / 25.26 ± 0.69</td> <!-- HellaSwag-sv -->
   <td class="is ner">36.02 ± 3.80 / 33.67 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">5.05 ± 2.42 / 48.46 ± 3.52</td> <!-- ScaLA-is -->
   <td class="is rc">25.83 ± 4.24 / 50.31 ± 4.16</td> <!-- NQiI -->
   <td class="is summ">66.77 ± 0.97 / 18.38 ± 1.96</td> <!-- RRN -->
   <td class="is know">1.70 ± 1.74 / 25.02 ± 1.35</td> <!-- ARC-is -->
   <td class="is reason">-1.88 ± 3.84 / 55.00 ± 1.77</td> <!-- Winogrande-is -->
   <td class="de ner">39.21 ± 2.29 / 36.08 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">58.36 ± 1.80 / 71.98 ± 1.17</td> <!-- SB10k -->
   <td class="de la">7.03 ± 3.09 / 50.18 ± 3.74</td> <!-- ScaLA-de -->
   <td class="de rc">27.02 ± 3.09 / 51.94 ± 4.17</td> <!-- GermanQuAD -->
   <td class="de summ">68.59 ± 0.76 / 25.49 ± 2.17</td> <!-- MLSum -->
   <td class="de know">3.52 ± 0.84 / 26.38 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">0.06 ± 0.82 / 24.56 ± 0.78</td> <!-- HellaSwag-de -->
   <td class="nl ner">48.24 ± 2.28 / 40.24 ± 1.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.37 ± 1.34 / 33.54 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">10.73 ± 1.76 / 48.26 ± 4.65</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.83 ± 1.16 / 65.28 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.32 ± 0.90 / 18.12 ± 1.06</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.72 ± 1.25 / 24.90 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.47 ± 0.87 / 24.28 ± 0.68</td> <!-- HellaSwag-nl -->
   <td class="en ner">45.89 ± 2.63 / 42.96 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">59.29 ± 1.35 / 65.59 ± 1.02</td> <!-- SST5 -->
   <td class="en la">9.11 ± 2.36 / 52.02 ± 2.16</td> <!-- ScaLA-en -->
   <td class="en rc">66.74 ± 1.21 / 77.75 ± 1.09</td> <!-- SQuAD -->
   <td class="en summ">68.17 ± 0.69 / 22.50 ± 0.73</td> <!-- CNN-DailyMail -->
   <td class="en know">0.92 ± 1.20 / 23.00 ± 0.81</td> <!-- MMLU -->
   <td class="en reason">0.61 ± 1.04 / 25.00 ± 0.60</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="da-rank">3.21</td> <!-- Danish rank -->
   <td class="no-rank">3.42</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.99</td> <!-- Swedish rank -->
   <td class="is-rank">4.45</td> <!-- Icelandic rank -->
   <td class="de-rank">2.93</td> <!-- German rank -->
   <td class="nl-rank">3.55</td> <!-- Dutch rank -->
   <td class="en-rank">2.52</td> <!-- English rank -->
   <td class="da ner">33.80 ± 2.66 / 25.32 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">31.57 ± 2.65 / 46.48 ± 3.84</td> <!-- Angry Tweets -->
   <td class="da la">2.76 ± 1.76 / 44.96 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da rc">54.20 ± 1.63 / 59.50 ± 1.54</td> <!-- ScandiQA-da -->
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
   <td class="no rc">39.16 ± 2.56 / 62.28 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">13.41 ± 0.92 / 33.01 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">7.83 ± 1.64 / 29.50 ± 1.51</td> <!-- HellaSwag-no -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.90 ± 0.52 / 17.15 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">16.18 ± 0.78 / 34.88 ± 0.66</td> <!-- MMLU-sv -->
   <td class="sv reason">8.52 ± 1.90 / 29.96 ± 1.75</td> <!-- HellaSwag-sv -->
   <td class="is ner">27.44 ± 3.28 / 23.50 ± 3.29</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.46 ± 1.18 / 41.20 ± 3.25</td> <!-- ScaLA-is -->
   <td class="is rc">17.26 ± 3.80 / 39.06 ± 3.00</td> <!-- NQiI -->
   <td class="is summ">58.30 ± 4.50 / 14.03 ± 2.00</td> <!-- RRN -->
   <td class="is know">2.14 ± 1.25 / 25.83 ± 1.11</td> <!-- ARC-is -->
   <td class="is reason">2.43 ± 2.93 / 55.15 ± 1.40</td> <!-- Winogrande-is -->
   <td class="de ner">39.41 ± 2.30 / 36.17 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">49.42 ± 4.33 / 61.57 ± 5.43</td> <!-- SB10k -->
   <td class="de la">6.02 ± 2.53 / 46.41 ± 4.35</td> <!-- ScaLA-de -->
   <td class="de rc">27.69 ± 4.39 / 54.92 ± 5.38</td> <!-- GermanQuAD -->
   <td class="de summ">66.75 ± 0.68 / 23.16 ± 0.88</td> <!-- MLSum -->
   <td class="de know">20.77 ± 0.92 / 39.29 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">10.47 ± 1.51 / 31.09 ± 1.36</td> <!-- HellaSwag-de -->
   <td class="nl ner">46.95 ± 2.32 / 36.13 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.34 ± 2.10 / 19.37 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">3.46 ± 1.91 / 41.32 ± 3.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.07 ± 0.89 / 68.14 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.31 ± 0.64 / 17.24 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">18.21 ± 0.70 / 37.51 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">9.03 ± 1.04 / 29.35 ± 0.77</td> <!-- HellaSwag-nl -->
   <td class="en ner">41.02 ± 3.86 / 40.03 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">66.43 ± 0.78 / 57.25 ± 0.33</td> <!-- SST5 -->
   <td class="en la">5.17 ± 1.55 / 37.03 ± 2.40</td> <!-- ScaLA-en -->
   <td class="en rc">76.04 ± 0.97 / 85.31 ± 0.82</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.51</td> <!-- Swedish rank -->
   <td class="is-rank">4.65</td> <!-- Icelandic rank -->
   <td class="de-rank">3.00</td> <!-- German rank -->
   <td class="nl-rank">3.43</td> <!-- Dutch rank -->
   <td class="en-rank">2.17</td> <!-- English rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da rc">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
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
   <td class="no rc">40.00 ± 2.26 / 62.87 ± 1.60</td> <!-- NorQuAD -->
   <td class="no know">16.50 ± 1.40 / 36.63 ± 1.17</td> <!-- MMLU-no -->
   <td class="no reason">13.27 ± 2.02 / 34.42 ± 1.54</td> <!-- HellaSwag-no -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.24 ± 1.76 / 16.02 ± 0.88</td> <!-- SweDN -->
   <td class="sv know">22.04 ± 0.60 / 41.36 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">14.76 ± 1.28 / 35.27 ± 1.32</td> <!-- HellaSwag-sv -->
   <td class="is ner">15.66 ± 5.89 / 15.78 ± 3.95</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is rc">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="is summ">57.17 ± 3.07 / 11.73 ± 1.00</td> <!-- RRN -->
   <td class="is know">5.46 ± 1.45 / 29.23 ± 1.11</td> <!-- ARC-is -->
   <td class="is reason">-1.71 ± 3.79 / 50.88 ± 1.29</td> <!-- Winogrande-is -->
   <td class="de ner">31.52 ± 2.96 / 29.20 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de rc">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.88 ± 1.25 / 21.37 ± 1.87</td> <!-- MLSum -->
   <td class="de know">21.32 ± 1.14 / 40.66 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">21.35 ± 0.89 / 40.77 ± 0.65</td> <!-- HellaSwag-de -->
   <td class="nl ner">35.74 ± 3.22 / 31.74 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.90 ± 1.59 / 14.17 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.20 ± 1.53 / 41.49 ± 1.08</td> <!-- MMLU-nl -->
   <td class="nl reason">13.11 ± 1.85 / 33.86 ± 1.69</td> <!-- HellaSwag-nl -->
   <td class="en ner">55.45 ± 1.61 / 49.72 ± 1.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en rc">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="da-rank">3.11</td> <!-- Danish rank -->
   <td class="no-rank">3.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.06</td> <!-- Swedish rank -->
   <td class="is-rank">4.43</td> <!-- Icelandic rank -->
   <td class="de-rank">2.95</td> <!-- German rank -->
   <td class="nl-rank">3.60</td> <!-- Dutch rank -->
   <td class="en-rank">2.78</td> <!-- English rank -->
   <td class="da ner">17.29 ± 2.84 / 13.87 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 2.71 / 42.58 ± 3.24</td> <!-- Angry Tweets -->
   <td class="da la">6.39 ± 2.41 / 45.03 ± 4.32</td> <!-- ScaLA-da -->
   <td class="da rc">54.94 ± 1.00 / 59.95 ± 1.03</td> <!-- ScandiQA-da -->
   <td class="da summ">64.82 ± 1.05 / 20.37 ± 1.06</td> <!-- Nordjylland-News -->
   <td class="da know">48.07 ± 1.24 / 60.50 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">45.03 ± 1.84 / 63.40 ± 1.23</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.10 ± 1.03 / 30.51 ± 1.01</td> <!-- HellaSwag-da -->
   <td class="no ner">20.47 ± 4.02 / 21.28 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">24.18 ± 4.24 / 24.41 ± 3.40</td> <!-- NorNE-nn -->
   <td class="no sent">32.61 ± 1.86 / 47.91 ± 2.11</td> <!-- NoReC -->
   <td class="no summ">60.17 ± 2.18 / 13.48 ± 1.53</td> <!-- No Sammendrag -->
   <td class="no la">3.22 ± 1.55 / 36.61 ± 2.49</td> <!-- ScaLA-nb -->
   <td class="no la">3.91 ± 2.50 / 45.37 ± 4.56</td> <!-- ScaLA-nn -->
   <td class="no rc">41.16 ± 3.73 / 63.31 ± 3.73</td> <!-- NorQuAD -->
   <td class="no know">19.03 ± 1.65 / 38.84 ± 1.33</td> <!-- MMLU-no -->
   <td class="no reason">7.35 ± 1.61 / 28.89 ± 1.54</td> <!-- HellaSwag-no -->
   <td class="sv ner">30.45 ± 3.49 / 23.98 ± 3.18</td> <!-- SUC3 -->
   <td class="sv sent">76.36 ± 1.10 / 65.98 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">6.06 ± 2.07 / 49.80 ± 2.71</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.19 ± 0.71 / 60.59 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.12 ± 0.69 / 17.92 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">20.80 ± 0.90 / 40.36 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">6.24 ± 1.13 / 28.87 ± 1.03</td> <!-- HellaSwag-sv -->
   <td class="is ner">10.67 ± 5.23 / 13.01 ± 3.26</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.21 ± 0.99 / 33.71 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">20.22 ± 3.01 / 43.48 ± 2.32</td> <!-- NQiI -->
   <td class="is summ">59.97 ± 2.49 / 13.32 ± 2.03</td> <!-- RRN -->
   <td class="is know">10.08 ± 1.82 / 32.08 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">1.16 ± 2.48 / 51.00 ± 1.70</td> <!-- Winogrande-is -->
   <td class="de ner">19.69 ± 4.71 / 19.53 ± 3.13</td> <!-- GermEval -->
   <td class="de sent">50.36 ± 2.83 / 60.36 ± 3.45</td> <!-- SB10k -->
   <td class="de la">9.07 ± 2.41 / 44.45 ± 4.37</td> <!-- ScaLA-de -->
   <td class="de rc">27.06 ± 4.74 / 53.36 ± 6.20</td> <!-- GermanQuAD -->
   <td class="de summ">68.52 ± 1.47 / 26.96 ± 3.01</td> <!-- MLSum -->
   <td class="de know">26.50 ± 0.89 / 44.19 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">9.36 ± 1.35 / 30.60 ± 1.18</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.63 ± 4.98 / 22.71 ± 2.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.11 ± 1.55 / 28.07 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">8.04 ± 1.79 / 48.95 ± 2.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.39 ± 2.14 / 65.22 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.90 ± 1.04 / 17.09 ± 0.93</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.76 ± 0.76 / 41.67 ± 0.80</td> <!-- MMLU-nl -->
   <td class="nl reason">8.50 ± 1.32 / 30.16 ± 1.11</td> <!-- HellaSwag-nl -->
   <td class="en ner">30.82 ± 4.46 / 27.49 ± 3.87</td> <!-- CoNLL-en -->
   <td class="en sent">66.28 ± 0.84 / 65.60 ± 1.23</td> <!-- SST5 -->
   <td class="en la">10.09 ± 2.52 / 48.92 ± 3.34</td> <!-- ScaLA-en -->
   <td class="en rc">64.96 ± 3.77 / 78.21 ± 2.16</td> <!-- SQuAD -->
   <td class="en summ">67.13 ± 0.54 / 21.94 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">35.14 ± 1.07 / 51.22 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">11.26 ± 1.35 / 31.40 ± 1.40</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="da-rank">3.56</td> <!-- Danish rank -->
   <td class="no-rank">3.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.36</td> <!-- Swedish rank -->
   <td class="is-rank">4.72</td> <!-- Icelandic rank -->
   <td class="de-rank">2.98</td> <!-- German rank -->
   <td class="nl-rank">3.28</td> <!-- Dutch rank -->
   <td class="en-rank">2.47</td> <!-- English rank -->
   <td class="da ner">31.80 ± 2.87 / 23.06 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">6.85 ± 2.25 / 19.42 ± 0.91</td> <!-- Angry Tweets -->
   <td class="da la">0.97 ± 1.10 / 36.48 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">49.83 ± 1.73 / 55.19 ± 1.84</td> <!-- ScandiQA-da -->
   <td class="da summ">63.43 ± 0.90 / 16.85 ± 1.02</td> <!-- Nordjylland-News -->
   <td class="da know">15.97 ± 1.54 / 36.37 ± 1.08</td> <!-- Danske Talemaader -->
   <td class="da know">17.19 ± 2.72 / 45.23 ± 1.84</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.07 ± 0.91 / 27.05 ± 0.83</td> <!-- HellaSwag-da -->
   <td class="no ner">40.08 ± 2.60 / 33.17 ± 1.81</td> <!-- NorNE-nb -->
   <td class="no ner">43.96 ± 1.65 / 32.96 ± 2.24</td> <!-- NorNE-nn -->
   <td class="no sent">31.90 ± 1.50 / 53.03 ± 1.81</td> <!-- NoReC -->
   <td class="no summ">59.98 ± 1.54 / 11.97 ± 1.13</td> <!-- No Sammendrag -->
   <td class="no la">-0.07 ± 0.97 / 35.01 ± 1.42</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 2.35 / 38.10 ± 4.51</td> <!-- ScaLA-nn -->
   <td class="no rc">23.32 ± 2.39 / 43.13 ± 3.33</td> <!-- NorQuAD -->
   <td class="no know">11.78 ± 1.09 / 33.75 ± 0.93</td> <!-- MMLU-no -->
   <td class="no reason">5.48 ± 1.23 / 28.09 ± 1.29</td> <!-- HellaSwag-no -->
   <td class="sv ner">36.01 ± 3.07 / 24.61 ± 4.22</td> <!-- SUC3 -->
   <td class="sv sent">57.18 ± 5.33 / 62.72 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 2.14 / 38.30 ± 3.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.04 ± 0.95 / 56.97 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.57 ± 0.73 / 15.09 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">13.42 ± 0.96 / 34.81 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">7.33 ± 1.70 / 29.31 ± 1.45</td> <!-- HellaSwag-sv -->
   <td class="is ner">18.07 ± 3.62 / 18.73 ± 2.54</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.72 ± 1.22 / 33.96 ± 0.50</td> <!-- ScaLA-is -->
   <td class="is rc">12.27 ± 2.81 / 30.66 ± 1.47</td> <!-- NQiI -->
   <td class="is summ">56.49 ± 3.33 / 8.77 ± 1.24</td> <!-- RRN -->
   <td class="is know">0.32 ± 1.35 / 24.82 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">1.00 ± 2.57 / 51.21 ± 2.91</td> <!-- Winogrande-is -->
   <td class="de ner">40.61 ± 2.18 / 28.49 ± 2.11</td> <!-- GermEval -->
   <td class="de sent">31.86 ± 3.60 / 42.96 ± 3.98</td> <!-- SB10k -->
   <td class="de la">5.36 ± 3.96 / 37.83 ± 4.03</td> <!-- ScaLA-de -->
   <td class="de rc">25.99 ± 3.85 / 47.72 ± 4.74</td> <!-- GermanQuAD -->
   <td class="de summ">66.77 ± 0.94 / 23.71 ± 1.90</td> <!-- MLSum -->
   <td class="de know">22.17 ± 1.05 / 41.55 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">22.61 ± 1.75 / 41.16 ± 1.46</td> <!-- HellaSwag-de -->
   <td class="nl ner">42.52 ± 3.31 / 33.08 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.91 ± 1.71 / 35.24 ± 2.62</td> <!-- Dutch Social -->
   <td class="nl la">0.69 ± 2.82 / 36.10 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.95 ± 1.18 / 66.87 ± 1.37</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.71 ± 0.60 / 17.04 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.93 ± 1.42 / 40.35 ± 1.23</td> <!-- MMLU-nl -->
   <td class="nl reason">24.42 ± 1.73 / 42.26 ± 1.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">49.44 ± 3.68 / 39.69 ± 2.34</td> <!-- CoNLL-en -->
   <td class="en sent">66.65 ± 1.04 / 65.72 ± 1.32</td> <!-- SST5 -->
   <td class="en la">12.56 ± 2.15 / 54.20 ± 3.42</td> <!-- ScaLA-en -->
   <td class="en rc">63.29 ± 4.61 / 75.62 ± 3.79</td> <!-- SQuAD -->
   <td class="en summ">66.38 ± 0.28 / 21.17 ± 0.41</td> <!-- CNN-DailyMail -->
   <td class="en know">32.06 ± 0.87 / 49.12 ± 0.61</td> <!-- MMLU -->
   <td class="en reason">58.21 ± 0.98 / 68.63 ± 0.74</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="da-rank">3.50</td> <!-- Danish rank -->
   <td class="no-rank">3.59</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.19</td> <!-- Swedish rank -->
   <td class="is-rank">4.26</td> <!-- Icelandic rank -->
   <td class="de-rank">3.38</td> <!-- German rank -->
   <td class="nl-rank">3.64</td> <!-- Dutch rank -->
   <td class="en-rank">2.72</td> <!-- English rank -->
   <td class="da ner">28.18 ± 3.39 / 24.25 ± 3.30</td> <!-- DANSK -->
   <td class="da sent">29.32 ± 7.19 / 41.08 ± 8.29</td> <!-- Angry Tweets -->
   <td class="da la">2.90 ± 2.18 / 37.93 ± 4.98</td> <!-- ScaLA-da -->
   <td class="da rc">56.48 ± 1.11 / 62.92 ± 0.96</td> <!-- ScandiQA-da -->
   <td class="da summ">53.81 ± 1.18 / 9.42 ± 0.33</td> <!-- Nordjylland-News -->
   <td class="da know">27.86 ± 1.78 / 43.42 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">34.62 ± 2.93 / 55.21 ± 2.08</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.73 ± 0.61 / 27.77 ± 0.53</td> <!-- HellaSwag-da -->
   <td class="no ner">36.96 ± 3.10 / 34.68 ± 3.19</td> <!-- NorNE-nb -->
   <td class="no ner">39.38 ± 3.30 / 37.06 ± 3.49</td> <!-- NorNE-nn -->
   <td class="no sent">32.67 ± 2.52 / 44.37 ± 3.06</td> <!-- NoReC -->
   <td class="no summ">51.44 ± 1.23 / 8.37 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">2.18 ± 2.36 / 38.05 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">5.33 ± 2.97 / 44.30 ± 4.99</td> <!-- ScaLA-nn -->
   <td class="no rc">45.23 ± 5.03 / 67.75 ± 4.41</td> <!-- NorQuAD -->
   <td class="no know">9.35 ± 1.27 / 30.22 ± 0.88</td> <!-- MMLU-no -->
   <td class="no reason">4.85 ± 0.63 / 27.55 ± 0.65</td> <!-- HellaSwag-no -->
   <td class="sv ner">41.49 ± 2.82 / 38.09 ± 2.86</td> <!-- SUC3 -->
   <td class="sv sent">75.64 ± 1.51 / 76.06 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">0.66 ± 1.97 / 33.73 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.48 ± 0.54 / 63.85 ± 0.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.94 ± 1.10 / 13.29 ± 0.34</td> <!-- SweDN -->
   <td class="sv know">10.56 ± 1.14 / 31.45 ± 0.92</td> <!-- MMLU-sv -->
   <td class="sv reason">5.03 ± 1.36 / 28.41 ± 0.76</td> <!-- HellaSwag-sv -->
   <td class="is ner">31.81 ± 1.93 / 29.47 ± 2.02</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.63 ± 1.69 / 44.49 ± 3.89</td> <!-- ScaLA-is -->
   <td class="is rc">16.72 ± 7.29 / 46.83 ± 5.93</td> <!-- NQiI -->
   <td class="is summ">58.72 ± 3.28 / 13.71 ± 1.35</td> <!-- RRN -->
   <td class="is know">12.62 ± 1.36 / 34.51 ± 1.27</td> <!-- ARC-is -->
   <td class="is reason">3.43 ± 2.18 / 44.56 ± 1.09</td> <!-- Winogrande-is -->
   <td class="de ner">32.33 ± 2.48 / 30.20 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">26.39 ± 5.23 / 36.06 ± 6.62</td> <!-- SB10k -->
   <td class="de la">1.44 ± 1.38 / 33.60 ± 0.42</td> <!-- ScaLA-de -->
   <td class="de rc">28.15 ± 5.57 / 54.13 ± 6.75</td> <!-- GermanQuAD -->
   <td class="de summ">58.62 ± 3.80 / 13.54 ± 2.20</td> <!-- MLSum -->
   <td class="de know">14.94 ± 1.09 / 35.44 ± 0.89</td> <!-- MMLU-de -->
   <td class="de reason">8.70 ± 0.96 / 31.09 ± 0.58</td> <!-- HellaSwag-de -->
   <td class="nl ner">36.61 ± 3.37 / 31.91 ± 2.20</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.77 ± 1.80 / 25.31 ± 1.42</td> <!-- Dutch Social -->
   <td class="nl la">3.52 ± 2.07 / 35.34 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.51 ± 0.97 / 70.33 ± 0.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.50 ± 5.78 / 15.01 ± 1.59</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.90 ± 1.44 / 35.20 ± 1.09</td> <!-- MMLU-nl -->
   <td class="nl reason">7.26 ± 1.56 / 29.91 ± 1.18</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.20 ± 3.39 / 44.00 ± 3.43</td> <!-- CoNLL-en -->
   <td class="en sent">64.82 ± 1.13 / 67.11 ± 1.41</td> <!-- SST5 -->
   <td class="en la">7.57 ± 2.31 / 45.83 ± 3.97</td> <!-- ScaLA-en -->
   <td class="en rc">73.88 ± 1.02 / 83.56 ± 0.75</td> <!-- SQuAD -->
   <td class="en summ">67.34 ± 0.38 / 21.61 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">16.59 ± 1.01 / 35.35 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">11.97 ± 1.35 / 32.72 ± 0.94</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.53</td> <!-- ScandEval rank -->
   <td class="da-rank">3.38</td> <!-- Danish rank -->
   <td class="no-rank">3.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.34</td> <!-- Swedish rank -->
   <td class="is-rank">4.43</td> <!-- Icelandic rank -->
   <td class="de-rank">3.27</td> <!-- German rank -->
   <td class="nl-rank">3.66</td> <!-- Dutch rank -->
   <td class="en-rank">2.90</td> <!-- English rank -->
   <td class="da ner">35.45 ± 2.41 / 30.39 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">36.94 ± 1.08 / 49.24 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">1.12 ± 2.21 / 44.63 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da rc">44.61 ± 0.84 / 53.34 ± 0.63</td> <!-- ScandiQA-da -->
   <td class="da summ">61.33 ± 1.47 / 15.38 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">27.14 ± 1.18 / 43.89 ± 1.09</td> <!-- Danske Talemaader -->
   <td class="da know">18.57 ± 1.82 / 46.35 ± 1.18</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.16 ± 0.85 / 26.86 ± 0.87</td> <!-- HellaSwag-da -->
   <td class="no ner">44.66 ± 0.68 / 41.13 ± 2.11</td> <!-- NorNE-nb -->
   <td class="no ner">47.78 ± 1.22 / 44.30 ± 1.57</td> <!-- NorNE-nn -->
   <td class="no sent">27.43 ± 1.89 / 42.83 ± 3.08</td> <!-- NoReC -->
   <td class="no summ">57.67 ± 1.45 / 10.42 ± 1.07</td> <!-- No Sammendrag -->
   <td class="no la">0.07 ± 1.51 / 34.07 ± 0.78</td> <!-- ScaLA-nb -->
   <td class="no la">1.14 ± 1.23 / 33.17 ± 0.47</td> <!-- ScaLA-nn -->
   <td class="no rc">18.00 ± 3.56 / 39.37 ± 4.69</td> <!-- NorQuAD -->
   <td class="no know">11.67 ± 1.20 / 33.08 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">3.53 ± 1.01 / 26.63 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">41.60 ± 2.74 / 37.22 ± 3.26</td> <!-- SUC3 -->
   <td class="sv sent">71.86 ± 2.01 / 71.15 ± 2.16</td> <!-- SweReC -->
   <td class="sv la">3.72 ± 1.40 / 48.04 ± 1.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.57 ± 1.35 / 52.90 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.69 ± 0.79 / 13.27 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">14.64 ± 0.91 / 35.56 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">3.10 ± 0.87 / 26.60 ± 0.68</td> <!-- HellaSwag-sv -->
   <td class="is ner">33.76 ± 3.44 / 32.21 ± 2.82</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.13 ± 1.34 / 42.66 ± 3.62</td> <!-- ScaLA-is -->
   <td class="is rc">12.43 ± 2.62 / 33.38 ± 1.39</td> <!-- NQiI -->
   <td class="is summ">59.46 ± 2.42 / 13.23 ± 1.87</td> <!-- RRN -->
   <td class="is know">2.09 ± 1.34 / 25.68 ± 0.67</td> <!-- ARC-is -->
   <td class="is reason">3.56 ± 2.07 / 56.72 ± 0.99</td> <!-- Winogrande-is -->
   <td class="de ner">42.51 ± 1.31 / 37.05 ± 1.59</td> <!-- GermEval -->
   <td class="de sent">38.26 ± 2.34 / 55.52 ± 2.66</td> <!-- SB10k -->
   <td class="de la">5.48 ± 1.36 / 48.23 ± 2.44</td> <!-- ScaLA-de -->
   <td class="de rc">19.43 ± 3.10 / 41.82 ± 3.29</td> <!-- GermanQuAD -->
   <td class="de summ">60.81 ± 1.75 / 13.79 ± 2.22</td> <!-- MLSum -->
   <td class="de know">16.06 ± 1.35 / 36.96 ± 0.92</td> <!-- MMLU-de -->
   <td class="de reason">6.64 ± 0.55 / 29.12 ± 0.60</td> <!-- HellaSwag-de -->
   <td class="nl ner">42.01 ± 2.06 / 37.16 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.15 ± 1.70 / 32.55 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">1.11 ± 2.15 / 36.71 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.04 ± 1.61 / 53.75 ± 1.10</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.72 ± 1.05 / 12.47 ± 0.62</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.71 ± 0.69 / 38.01 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.98 ± 1.11 / 28.05 ± 1.00</td> <!-- HellaSwag-nl -->
   <td class="en ner">56.41 ± 1.79 / 52.05 ± 1.57</td> <!-- CoNLL-en -->
   <td class="en sent">59.46 ± 1.16 / 65.61 ± 1.08</td> <!-- SST5 -->
   <td class="en la">8.36 ± 0.71 / 49.50 ± 2.90</td> <!-- ScaLA-en -->
   <td class="en rc">47.26 ± 3.09 / 67.95 ± 2.10</td> <!-- SQuAD -->
   <td class="en summ">66.61 ± 0.54 / 21.06 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">25.59 ± 0.93 / 43.75 ± 0.65</td> <!-- MMLU -->
   <td class="en reason">18.56 ± 1.15 / 38.13 ± 0.88</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="da-rank">3.42</td> <!-- Danish rank -->
   <td class="no-rank">3.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.52</td> <!-- Swedish rank -->
   <td class="is-rank">4.76</td> <!-- Icelandic rank -->
   <td class="de-rank">3.22</td> <!-- German rank -->
   <td class="nl-rank">3.60</td> <!-- Dutch rank -->
   <td class="en-rank">2.77</td> <!-- English rank -->
   <td class="da ner">37.21 ± 2.75 / 27.74 ± 2.59</td> <!-- DANSK -->
   <td class="da sent">31.54 ± 2.39 / 50.61 ± 2.88</td> <!-- Angry Tweets -->
   <td class="da la">6.30 ± 1.61 / 49.09 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da rc">44.86 ± 0.80 / 51.51 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">61.56 ± 0.49 / 13.64 ± 0.97</td> <!-- Nordjylland-News -->
   <td class="da know">17.92 ± 1.52 / 37.22 ± 1.29</td> <!-- Danske Talemaader -->
   <td class="da know">10.79 ± 2.32 / 40.86 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.70 ± 1.10 / 26.14 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">53.78 ± 2.43 / 49.41 ± 2.56</td> <!-- NorNE-nb -->
   <td class="no ner">55.14 ± 1.27 / 51.07 ± 1.78</td> <!-- NorNE-nn -->
   <td class="no sent">26.21 ± 1.63 / 43.33 ± 1.46</td> <!-- NoReC -->
   <td class="no summ">57.11 ± 1.08 / 10.81 ± 0.52</td> <!-- No Sammendrag -->
   <td class="no la">3.90 ± 1.45 / 43.86 ± 4.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.42 ± 1.39 / 41.58 ± 3.89</td> <!-- ScaLA-nn -->
   <td class="no rc">24.86 ± 1.34 / 45.77 ± 1.85</td> <!-- NorQuAD -->
   <td class="no know">10.36 ± 1.15 / 29.64 ± 1.06</td> <!-- MMLU-no -->
   <td class="no reason">5.85 ± 1.57 / 27.84 ± 1.21</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.10 ± 4.30 / 42.80 ± 5.47</td> <!-- SUC3 -->
   <td class="sv sent">65.67 ± 3.92 / 64.00 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">4.55 ± 2.18 / 45.11 ± 4.32</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.83 ± 1.02 / 49.35 ± 1.09</td> <!-- ScandiQA-sv -->
   <td class="sv summ">45.16 ± 0.70 / 11.84 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">7.58 ± 0.88 / 28.54 ± 0.85</td> <!-- MMLU-sv -->
   <td class="sv reason">3.79 ± 0.85 / 27.39 ± 0.57</td> <!-- HellaSwag-sv -->
   <td class="is ner">33.57 ± 2.48 / 33.47 ± 2.48</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">11.27 ± 2.38 / 33.54 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">49.32 ± 3.71 / 8.01 ± 2.04</td> <!-- RRN -->
   <td class="is know">1.37 ± 1.11 / 25.57 ± 1.36</td> <!-- ARC-is -->
   <td class="is reason">-4.04 ± 3.58 / 50.55 ± 3.65</td> <!-- Winogrande-is -->
   <td class="de ner">49.16 ± 2.12 / 40.34 ± 2.81</td> <!-- GermEval -->
   <td class="de sent">35.17 ± 4.48 / 51.15 ± 4.55</td> <!-- SB10k -->
   <td class="de la">9.79 ± 2.06 / 50.77 ± 3.64</td> <!-- ScaLA-de -->
   <td class="de rc">22.48 ± 2.59 / 45.90 ± 3.03</td> <!-- GermanQuAD -->
   <td class="de summ">60.81 ± 0.38 / 15.92 ± 0.54</td> <!-- MLSum -->
   <td class="de know">6.89 ± 0.76 / 28.82 ± 0.69</td> <!-- MMLU-de -->
   <td class="de reason">4.79 ± 0.91 / 28.40 ± 0.78</td> <!-- HellaSwag-de -->
   <td class="nl ner">48.53 ± 3.89 / 38.20 ± 2.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.15 ± 1.55 / 22.01 ± 1.44</td> <!-- Dutch Social -->
   <td class="nl la">4.88 ± 2.27 / 38.78 ± 3.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.38 ± 0.93 / 56.09 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.56 ± 1.09 / 15.20 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.38 ± 1.06 / 29.60 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">2.69 ± 0.56 / 25.85 ± 0.33</td> <!-- HellaSwag-nl -->
   <td class="en ner">58.30 ± 2.16 / 53.45 ± 1.98</td> <!-- CoNLL-en -->
   <td class="en sent">59.01 ± 2.14 / 62.37 ± 1.73</td> <!-- SST5 -->
   <td class="en la">10.33 ± 3.06 / 53.28 ± 2.21</td> <!-- ScaLA-en -->
   <td class="en rc">65.04 ± 2.20 / 75.93 ± 1.50</td> <!-- SQuAD -->
   <td class="en summ">67.46 ± 0.31 / 23.04 ± 0.42</td> <!-- CNN-DailyMail -->
   <td class="en know">14.10 ± 0.93 / 34.24 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">10.67 ± 0.81 / 32.66 ± 0.64</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="da-rank">3.30</td> <!-- Danish rank -->
   <td class="no-rank">3.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.54</td> <!-- Swedish rank -->
   <td class="is-rank">4.47</td> <!-- Icelandic rank -->
   <td class="de-rank">3.59</td> <!-- German rank -->
   <td class="nl-rank">3.57</td> <!-- Dutch rank -->
   <td class="en-rank">2.89</td> <!-- English rank -->
   <td class="da ner">38.62 ± 3.40 / 27.71 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">35.47 ± 1.35 / 52.70 ± 2.05</td> <!-- Angry Tweets -->
   <td class="da la">5.07 ± 1.76 / 43.91 ± 4.86</td> <!-- ScaLA-da -->
   <td class="da rc">45.21 ± 0.84 / 50.96 ± 0.94</td> <!-- ScandiQA-da -->
   <td class="da summ">62.50 ± 0.59 / 15.45 ± 0.50</td> <!-- Nordjylland-News -->
   <td class="da know">13.46 ± 2.03 / 33.24 ± 1.59</td> <!-- Danske Talemaader -->
   <td class="da know">15.31 ± 3.62 / 43.65 ± 2.19</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.00 ± 1.15 / 29.24 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">53.93 ± 3.93 / 48.95 ± 4.17</td> <!-- NorNE-nb -->
   <td class="no ner">54.04 ± 1.83 / 49.74 ± 2.48</td> <!-- NorNE-nn -->
   <td class="no sent">23.83 ± 3.47 / 45.39 ± 3.46</td> <!-- NoReC -->
   <td class="no summ">50.59 ± 3.68 / 7.28 ± 1.97</td> <!-- No Sammendrag -->
   <td class="no la">3.91 ± 1.46 / 42.54 ± 4.53</td> <!-- ScaLA-nb -->
   <td class="no la">1.55 ± 2.39 / 40.63 ± 4.26</td> <!-- ScaLA-nn -->
   <td class="no rc">2.37 ± 0.20 / 12.14 ± 1.07</td> <!-- NorQuAD -->
   <td class="no know">8.68 ± 1.17 / 31.15 ± 0.84</td> <!-- MMLU-no -->
   <td class="no reason">6.19 ± 0.85 / 29.29 ± 0.77</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.76 ± 4.53 / 41.73 ± 6.65</td> <!-- SUC3 -->
   <td class="sv sent">70.61 ± 1.12 / 60.47 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">6.24 ± 3.11 / 46.34 ± 5.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.67 ± 1.34 / 50.56 ± 1.33</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.31 ± 2.13 / 7.20 ± 1.44</td> <!-- SweDN -->
   <td class="sv know">7.41 ± 0.75 / 30.14 ± 0.39</td> <!-- MMLU-sv -->
   <td class="sv reason">5.42 ± 0.79 / 29.15 ± 0.59</td> <!-- HellaSwag-sv -->
   <td class="is ner">38.52 ± 3.25 / 28.84 ± 5.49</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">12.94 ± 2.60 / 36.06 ± 2.17</td> <!-- NQiI -->
   <td class="is summ">58.58 ± 4.00 / 12.91 ± 2.09</td> <!-- RRN -->
   <td class="is know">2.11 ± 1.02 / 27.80 ± 1.02</td> <!-- ARC-is -->
   <td class="is reason">-4.75 ± 2.84 / 50.40 ± 4.21</td> <!-- Winogrande-is -->
   <td class="de ner">49.38 ± 2.20 / 42.66 ± 3.24</td> <!-- GermEval -->
   <td class="de sent">41.72 ± 4.07 / 60.45 ± 3.07</td> <!-- SB10k -->
   <td class="de la">7.67 ± 1.52 / 46.66 ± 3.23</td> <!-- ScaLA-de -->
   <td class="de rc">13.70 ± 2.43 / 30.21 ± 3.80</td> <!-- GermanQuAD -->
   <td class="de summ">45.88 ± 3.36 / 8.30 ± 1.98</td> <!-- MLSum -->
   <td class="de know">8.73 ± 1.03 / 31.46 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">6.18 ± 1.33 / 29.78 ± 1.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">50.88 ± 3.41 / 39.51 ± 3.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.39 ± 1.50 / 30.05 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">3.31 ± 1.19 / 37.97 ± 4.40</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.44 ± 1.06 / 58.85 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.50 ± 2.95 / 10.11 ± 2.12</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">9.22 ± 0.79 / 31.06 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">4.45 ± 1.38 / 28.26 ± 1.08</td> <!-- HellaSwag-nl -->
   <td class="en ner">60.64 ± 2.11 / 55.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">61.20 ± 1.16 / 61.92 ± 1.68</td> <!-- SST5 -->
   <td class="en la">7.63 ± 2.79 / 46.39 ± 3.79</td> <!-- ScaLA-en -->
   <td class="en rc">69.83 ± 2.12 / 80.15 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">56.62 ± 3.70 / 13.80 ± 2.77</td> <!-- CNN-DailyMail -->
   <td class="en know">16.29 ± 0.76 / 36.25 ± 0.61</td> <!-- MMLU -->
   <td class="en reason">10.37 ± 1.17 / 32.60 ± 0.89</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da-rank">3.30</td> <!-- Danish rank -->
   <td class="no-rank">3.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.38</td> <!-- Swedish rank -->
   <td class="is-rank">4.63</td> <!-- Icelandic rank -->
   <td class="de-rank">3.43</td> <!-- German rank -->
   <td class="nl-rank">3.88</td> <!-- Dutch rank -->
   <td class="en-rank">3.11</td> <!-- English rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da rc">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
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
   <td class="no rc">33.33 ± 3.73 / 53.15 ± 4.42</td> <!-- NorQuAD -->
   <td class="no know">11.27 ± 1.41 / 32.73 ± 1.25</td> <!-- MMLU-no -->
   <td class="no reason">5.10 ± 1.44 / 28.63 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.72 ± 1.46 / 15.26 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">10.98 ± 0.98 / 31.92 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">4.24 ± 0.47 / 27.53 ± 0.44</td> <!-- HellaSwag-sv -->
   <td class="is ner">8.83 ± 5.85 / 9.93 ± 4.70</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="is summ">60.00 ± 2.62 / 13.07 ± 1.31</td> <!-- RRN -->
   <td class="is know">2.52 ± 1.20 / 26.23 ± 1.40</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 2.53 / 56.42 ± 0.98</td> <!-- Winogrande-is -->
   <td class="de ner">16.95 ± 2.96 / 15.80 ± 2.16</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de rc">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.96 / 22.24 ± 1.37</td> <!-- MLSum -->
   <td class="de know">12.11 ± 0.94 / 33.12 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">7.32 ± 1.40 / 30.11 ± 1.16</td> <!-- HellaSwag-de -->
   <td class="nl ner">16.90 ± 4.91 / 17.38 ± 4.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.61 ± 2.22 / 13.67 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.94 ± 0.50 / 31.87 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">3.29 ± 0.95 / 26.85 ± 0.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">19.65 ± 5.96 / 18.64 ± 5.49</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en rc">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="da-rank">3.29</td> <!-- Danish rank -->
   <td class="no-rank">3.79</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.31</td> <!-- Swedish rank -->
   <td class="is-rank">4.28</td> <!-- Icelandic rank -->
   <td class="de-rank">3.61</td> <!-- German rank -->
   <td class="nl-rank">4.08</td> <!-- Dutch rank -->
   <td class="en-rank">3.21</td> <!-- English rank -->
   <td class="da ner">28.60 ± 4.69 / 20.29 ± 3.37</td> <!-- DANSK -->
   <td class="da sent">48.71 ± 1.27 / 60.90 ± 2.95</td> <!-- Angry Tweets -->
   <td class="da la">2.30 ± 1.34 / 37.21 ± 2.50</td> <!-- ScaLA-da -->
   <td class="da rc">53.85 ± 1.73 / 58.96 ± 1.67</td> <!-- ScandiQA-da -->
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
   <td class="no rc">34.41 ± 3.68 / 53.61 ± 4.28</td> <!-- NorQuAD -->
   <td class="no know">-0.56 ± 0.87 / 21.99 ± 0.62</td> <!-- MMLU-no -->
   <td class="no reason">-0.43 ± 1.02 / 24.54 ± 0.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.05 ± 1.20 / 13.94 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">1.32 ± 1.02 / 23.28 ± 0.65</td> <!-- MMLU-sv -->
   <td class="sv reason">0.35 ± 0.66 / 25.33 ± 0.66</td> <!-- HellaSwag-sv -->
   <td class="is ner">26.28 ± 5.09 / 22.73 ± 3.35</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.17 ± 1.98 / 48.03 ± 2.64</td> <!-- ScaLA-is -->
   <td class="is rc">22.65 ± 3.50 / 45.48 ± 2.99</td> <!-- NQiI -->
   <td class="is summ">62.07 ± 1.73 / 11.04 ± 1.91</td> <!-- RRN -->
   <td class="is know">-0.07 ± 0.85 / 23.51 ± 0.95</td> <!-- ARC-is -->
   <td class="is reason">-2.92 ± 4.86 / 53.55 ± 3.32</td> <!-- Winogrande-is -->
   <td class="de ner">34.53 ± 1.24 / 29.89 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">42.90 ± 2.66 / 56.64 ± 4.71</td> <!-- SB10k -->
   <td class="de la">1.51 ± 1.64 / 43.36 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">15.83 ± 1.42 / 29.77 ± 2.54</td> <!-- GermanQuAD -->
   <td class="de summ">61.40 ± 3.15 / 14.84 ± 2.07</td> <!-- MLSum -->
   <td class="de know">-1.84 ± 1.09 / 23.98 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">-0.12 ± 1.30 / 24.41 ± 0.96</td> <!-- HellaSwag-de -->
   <td class="nl ner">36.74 ± 3.36 / 32.36 ± 1.39</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 2.44 / 34.17 ± 2.59</td> <!-- Dutch Social -->
   <td class="nl la">3.01 ± 1.94 / 46.03 ± 4.19</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.32 ± 1.55 / 40.73 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.76 ± 1.36 / 10.67 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.67 ± 1.15 / 24.89 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.30 ± 1.01 / 23.52 ± 0.38</td> <!-- HellaSwag-nl -->
   <td class="en ner">42.78 ± 4.24 / 40.64 ± 2.84</td> <!-- CoNLL-en -->
   <td class="en sent">59.90 ± 4.98 / 54.05 ± 2.70</td> <!-- SST5 -->
   <td class="en la">5.68 ± 1.91 / 50.82 ± 2.18</td> <!-- ScaLA-en -->
   <td class="en rc">58.52 ± 1.88 / 68.97 ± 1.86</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="da-rank">3.63</td> <!-- Danish rank -->
   <td class="no-rank">4.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.48</td> <!-- Swedish rank -->
   <td class="is-rank">4.46</td> <!-- Icelandic rank -->
   <td class="de-rank">3.53</td> <!-- German rank -->
   <td class="nl-rank">4.01</td> <!-- Dutch rank -->
   <td class="en-rank">2.61</td> <!-- English rank -->
   <td class="da ner">29.44 ± 1.81 / 20.31 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">18.49 ± 2.47 / 35.29 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">1.73 ± 1.63 / 38.18 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da rc">44.39 ± 0.80 / 50.40 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">61.76 ± 1.10 / 15.33 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">22.03 ± 1.83 / 37.29 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">12.61 ± 2.43 / 41.82 ± 1.61</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.06 ± 0.89 / 26.03 ± 0.67</td> <!-- HellaSwag-da -->
   <td class="no ner">37.60 ± 2.17 / 29.30 ± 2.43</td> <!-- NorNE-nb -->
   <td class="no ner">38.38 ± 2.48 / 30.13 ± 2.95</td> <!-- NorNE-nn -->
   <td class="no sent">24.05 ± 3.58 / 40.36 ± 4.22</td> <!-- NoReC -->
   <td class="no summ">48.55 ± 6.18 / 8.21 ± 1.30</td> <!-- No Sammendrag -->
   <td class="no la">3.56 ± 1.93 / 38.60 ± 3.52</td> <!-- ScaLA-nb -->
   <td class="no la">2.61 ± 2.57 / 38.57 ± 3.89</td> <!-- ScaLA-nn -->
   <td class="no rc">13.58 ± 3.16 / 25.34 ± 5.83</td> <!-- NorQuAD -->
   <td class="no know">9.52 ± 1.13 / 30.72 ± 1.12</td> <!-- MMLU-no -->
   <td class="no reason">3.62 ± 1.22 / 27.07 ± 1.15</td> <!-- HellaSwag-no -->
   <td class="sv ner">37.37 ± 1.87 / 26.31 ± 3.34</td> <!-- SUC3 -->
   <td class="sv sent">64.46 ± 3.06 / 69.83 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">4.49 ± 1.96 / 46.63 ± 4.39</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.92 ± 1.06 / 49.57 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.50 ± 1.26 / 12.92 ± 0.48</td> <!-- SweDN -->
   <td class="sv know">8.61 ± 1.25 / 29.95 ± 1.28</td> <!-- MMLU-sv -->
   <td class="sv reason">4.51 ± 0.96 / 27.64 ± 0.87</td> <!-- HellaSwag-sv -->
   <td class="is ner">26.23 ± 3.53 / 23.26 ± 2.30</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.69 ± 1.42 / 45.61 ± 2.69</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.59 / 28.57 ± 2.09</td> <!-- NQiI -->
   <td class="is summ">60.43 ± 2.70 / 15.28 ± 1.36</td> <!-- RRN -->
   <td class="is know">1.93 ± 1.38 / 25.06 ± 1.16</td> <!-- ARC-is -->
   <td class="is reason">3.27 ± 2.97 / 54.02 ± 1.79</td> <!-- Winogrande-is -->
   <td class="de ner">32.54 ± 1.57 / 26.92 ± 1.87</td> <!-- GermEval -->
   <td class="de sent">27.03 ± 2.54 / 42.80 ± 3.28</td> <!-- SB10k -->
   <td class="de la">8.95 ± 1.62 / 51.86 ± 2.23</td> <!-- ScaLA-de -->
   <td class="de rc">18.38 ± 1.26 / 39.18 ± 2.13</td> <!-- GermanQuAD -->
   <td class="de summ">59.91 ± 0.84 / 16.05 ± 0.61</td> <!-- MLSum -->
   <td class="de know">12.30 ± 1.16 / 32.60 ± 1.27</td> <!-- MMLU-de -->
   <td class="de reason">6.28 ± 1.36 / 27.82 ± 1.17</td> <!-- HellaSwag-de -->
   <td class="nl ner">31.84 ± 3.39 / 28.66 ± 1.77</td> <!-- CoNLL-nl -->
   <td class="nl sent">1.56 ± 3.25 / 28.78 ± 2.60</td> <!-- Dutch Social -->
   <td class="nl la">5.05 ± 1.34 / 43.99 ± 4.14</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.55 ± 0.77 / 48.56 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.35 ± 1.16 / 13.63 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.39 ± 0.96 / 34.55 ± 0.65</td> <!-- MMLU-nl -->
   <td class="nl reason">4.57 ± 0.96 / 27.42 ± 0.73</td> <!-- HellaSwag-nl -->
   <td class="en ner">47.58 ± 2.41 / 39.52 ± 1.41</td> <!-- CoNLL-en -->
   <td class="en sent">66.78 ± 0.76 / 61.52 ± 0.99</td> <!-- SST5 -->
   <td class="en la">20.53 ± 3.83 / 58.47 ± 2.90</td> <!-- ScaLA-en -->
   <td class="en rc">58.07 ± 2.23 / 69.96 ± 1.63</td> <!-- SQuAD -->
   <td class="en summ">62.45 ± 5.62 / 19.60 ± 1.85</td> <!-- CNN-DailyMail -->
   <td class="en know">32.90 ± 0.96 / 49.16 ± 0.95</td> <!-- MMLU -->
   <td class="en reason">25.32 ± 2.12 / 42.50 ± 2.39</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="da-rank">3.76</td> <!-- Danish rank -->
   <td class="no-rank">3.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.45</td> <!-- Swedish rank -->
   <td class="is-rank">4.65</td> <!-- Icelandic rank -->
   <td class="de-rank">3.55</td> <!-- German rank -->
   <td class="nl-rank">4.01</td> <!-- Dutch rank -->
   <td class="en-rank">2.85</td> <!-- English rank -->
   <td class="da ner">24.47 ± 3.42 / 18.70 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">9.93 ± 2.70 / 23.57 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 1.81 / 35.31 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da rc">42.09 ± 2.63 / 47.54 ± 2.94</td> <!-- ScandiQA-da -->
   <td class="da summ">61.62 ± 0.72 / 14.36 ± 0.73</td> <!-- Nordjylland-News -->
   <td class="da know">19.65 ± 1.47 / 36.46 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">19.01 ± 2.56 / 46.27 ± 1.71</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.34 ± 1.16 / 25.88 ± 0.65</td> <!-- HellaSwag-da -->
   <td class="no ner">26.70 ± 4.42 / 24.56 ± 2.10</td> <!-- NorNE-nb -->
   <td class="no ner">28.23 ± 3.78 / 28.27 ± 2.80</td> <!-- NorNE-nn -->
   <td class="no sent">23.25 ± 4.16 / 36.07 ± 4.20</td> <!-- NoReC -->
   <td class="no summ">56.31 ± 2.34 / 9.78 ± 0.93</td> <!-- No Sammendrag -->
   <td class="no la">-0.47 ± 1.05 / 33.93 ± 0.92</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 0.74 / 33.32 ± 0.79</td> <!-- ScaLA-nn -->
   <td class="no rc">13.40 ± 2.83 / 26.51 ± 4.94</td> <!-- NorQuAD -->
   <td class="no know">11.12 ± 0.88 / 33.35 ± 0.75</td> <!-- MMLU-no -->
   <td class="no reason">2.53 ± 0.82 / 26.29 ± 0.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">35.96 ± 3.50 / 26.41 ± 4.11</td> <!-- SUC3 -->
   <td class="sv sent">68.31 ± 1.43 / 72.51 ± 1.03</td> <!-- SweReC -->
   <td class="sv la">3.61 ± 1.79 / 49.47 ± 1.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.26 ± 1.85 / 49.32 ± 1.97</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.04 ± 0.95 / 13.24 ± 1.09</td> <!-- SweDN -->
   <td class="sv know">10.86 ± 1.20 / 31.65 ± 1.09</td> <!-- MMLU-sv -->
   <td class="sv reason">2.53 ± 0.98 / 26.17 ± 0.78</td> <!-- HellaSwag-sv -->
   <td class="is ner">20.50 ± 4.51 / 18.93 ± 3.84</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.83 ± 1.65 / 45.84 ± 2.02</td> <!-- ScaLA-is -->
   <td class="is rc">10.84 ± 2.45 / 28.36 ± 1.48</td> <!-- NQiI -->
   <td class="is summ">57.52 ± 4.61 / 13.43 ± 2.11</td> <!-- RRN -->
   <td class="is know">3.16 ± 0.85 / 26.13 ± 0.67</td> <!-- ARC-is -->
   <td class="is reason">-1.83 ± 3.11 / 49.80 ± 1.96</td> <!-- Winogrande-is -->
   <td class="de ner">28.67 ± 3.31 / 25.27 ± 2.68</td> <!-- GermEval -->
   <td class="de sent">19.69 ± 2.50 / 29.00 ± 2.22</td> <!-- SB10k -->
   <td class="de la">5.07 ± 0.89 / 47.60 ± 2.39</td> <!-- ScaLA-de -->
   <td class="de rc">18.43 ± 2.31 / 38.33 ± 2.91</td> <!-- GermanQuAD -->
   <td class="de summ">64.25 ± 1.99 / 18.90 ± 2.50</td> <!-- MLSum -->
   <td class="de know">15.15 ± 0.67 / 35.75 ± 0.46</td> <!-- MMLU-de -->
   <td class="de reason">6.23 ± 0.96 / 28.39 ± 0.87</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.84 ± 5.42 / 25.11 ± 3.52</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.60 ± 2.12 / 29.94 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">2.55 ± 1.41 / 40.88 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.33 ± 1.19 / 48.35 ± 1.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.31 ± 1.50 / 13.08 ± 0.51</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.32 ± 0.71 / 35.65 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">3.87 ± 1.02 / 27.14 ± 0.66</td> <!-- HellaSwag-nl -->
   <td class="en ner">41.57 ± 4.29 / 37.51 ± 3.05</td> <!-- CoNLL-en -->
   <td class="en sent">62.32 ± 1.12 / 67.09 ± 0.96</td> <!-- SST5 -->
   <td class="en la">8.04 ± 3.17 / 48.16 ± 5.38</td> <!-- ScaLA-en -->
   <td class="en rc">56.01 ± 3.10 / 67.43 ± 2.41</td> <!-- SQuAD -->
   <td class="en summ">65.06 ± 0.87 / 20.12 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">34.02 ± 0.87 / 50.12 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">22.81 ± 1.86 / 41.37 ± 1.41</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.76</td> <!-- ScandEval rank -->
   <td class="da-rank">3.56</td> <!-- Danish rank -->
   <td class="no-rank">3.75</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.98</td> <!-- Swedish rank -->
   <td class="is-rank">4.70</td> <!-- Icelandic rank -->
   <td class="de-rank">3.37</td> <!-- German rank -->
   <td class="nl-rank">3.83</td> <!-- Dutch rank -->
   <td class="en-rank">3.10</td> <!-- English rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
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
   <td class="no rc">32.42 ± 1.72 / 56.65 ± 0.92</td> <!-- NorQuAD -->
   <td class="no know">7.68 ± 0.87 / 29.15 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">1.06 ± 1.38 / 25.48 ± 1.00</td> <!-- HellaSwag-no -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="sv summ">40.55 ± 6.41 / 11.10 ± 1.63</td> <!-- SweDN -->
   <td class="sv know">11.06 ± 0.98 / 31.69 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">1.03 ± 0.85 / 25.55 ± 0.60</td> <!-- HellaSwag-sv -->
   <td class="is ner">20.49 ± 2.30 / 18.33 ± 1.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is rc">10.95 ± 2.39 / 37.64 ± 0.75</td> <!-- NQiI -->
   <td class="is summ">59.16 ± 0.96 / 9.92 ± 1.05</td> <!-- RRN -->
   <td class="is know">0.45 ± 1.44 / 22.94 ± 0.76</td> <!-- ARC-is -->
   <td class="is reason">0.62 ± 1.42 / 56.02 ± 0.95</td> <!-- Winogrande-is -->
   <td class="de ner">36.62 ± 1.56 / 28.22 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de rc">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td class="de summ">63.02 ± 2.00 / 19.54 ± 1.33</td> <!-- MLSum -->
   <td class="de know">12.27 ± 1.33 / 33.40 ± 1.08</td> <!-- MMLU-de -->
   <td class="de reason">6.57 ± 0.74 / 28.60 ± 0.70</td> <!-- HellaSwag-de -->
   <td class="nl ner">38.85 ± 3.77 / 32.18 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.99 ± 8.25 / 12.75 ± 2.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.97 ± 0.92 / 32.28 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">1.45 ± 1.15 / 24.79 ± 0.52</td> <!-- HellaSwag-nl -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en rc">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da-rank">3.75</td> <!-- Danish rank -->
   <td class="no-rank">4.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.56</td> <!-- Swedish rank -->
   <td class="is-rank">4.80</td> <!-- Icelandic rank -->
   <td class="de-rank">3.48</td> <!-- German rank -->
   <td class="nl-rank">3.92</td> <!-- Dutch rank -->
   <td class="en-rank">2.87</td> <!-- English rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da rc">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
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
   <td class="no rc">16.33 ± 2.17 / 31.16 ± 3.40</td> <!-- NorQuAD -->
   <td class="no know">7.79 ± 0.78 / 29.50 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">5.61 ± 1.32 / 28.45 ± 1.02</td> <!-- HellaSwag-no -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.19 ± 0.69 / 15.92 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">10.74 ± 0.92 / 32.65 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">4.83 ± 0.62 / 28.76 ± 0.55</td> <!-- HellaSwag-sv -->
   <td class="is ner">14.15 ± 1.92 / 14.96 ± 2.11</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is rc">7.80 ± 1.32 / 23.47 ± 1.64</td> <!-- NQiI -->
   <td class="is summ">57.27 ± 1.42 / 10.43 ± 0.97</td> <!-- RRN -->
   <td class="is know">1.62 ± 1.18 / 25.09 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">1.92 ± 2.32 / 50.07 ± 2.68</td> <!-- Winogrande-is -->
   <td class="de ner">28.04 ± 2.71 / 24.08 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td class="de summ">61.47 ± 1.67 / 12.62 ± 1.40</td> <!-- MLSum -->
   <td class="de know">13.44 ± 1.22 / 34.26 ± 0.98</td> <!-- MMLU-de -->
   <td class="de reason">8.31 ± 1.08 / 31.05 ± 0.84</td> <!-- HellaSwag-de -->
   <td class="nl ner">23.44 ± 5.09 / 25.00 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.91 ± 0.99 / 12.65 ± 0.41</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">12.11 ± 0.90 / 33.62 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.41 ± 1.13 / 29.73 ± 0.82</td> <!-- HellaSwag-nl -->
   <td class="en ner">40.89 ± 2.63 / 37.44 ± 2.39</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en rc">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">3.85</td> <!-- ScandEval rank -->
   <td class="da-rank">3.81</td> <!-- Danish rank -->
   <td class="no-rank">4.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.67</td> <!-- Swedish rank -->
   <td class="is-rank">4.79</td> <!-- Icelandic rank -->
   <td class="de-rank">3.66</td> <!-- German rank -->
   <td class="nl-rank">4.20</td> <!-- Dutch rank -->
   <td class="en-rank">2.74</td> <!-- English rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
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
   <td class="no rc">16.31 ± 2.22 / 30.78 ± 3.64</td> <!-- NorQuAD -->
   <td class="no know">9.57 ± 1.11 / 30.18 ± 0.83</td> <!-- MMLU-no -->
   <td class="no reason">6.02 ± 0.84 / 28.58 ± 1.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.82 ± 1.62 / 14.43 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">11.54 ± 0.73 / 32.55 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">7.19 ± 1.40 / 29.76 ± 1.22</td> <!-- HellaSwag-sv -->
   <td class="is ner">12.26 ± 4.13 / 12.77 ± 3.60</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is rc">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.65 ± 1.45 / 26.36 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.13 ± 3.74 / 52.30 ± 2.26</td> <!-- Winogrande-is -->
   <td class="de ner">9.23 ± 4.86 / 10.43 ± 3.83</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de rc">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td class="de summ">61.74 ± 1.58 / 14.71 ± 1.12</td> <!-- MLSum -->
   <td class="de know">13.65 ± 1.17 / 33.35 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">8.86 ± 0.99 / 30.21 ± 0.77</td> <!-- HellaSwag-de -->
   <td class="nl ner">11.66 ± 6.46 / 15.15 ± 4.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">55.00 ± 1.73 / 11.21 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.56 ± 0.64 / 34.17 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">5.89 ± 0.82 / 29.17 ± 0.66</td> <!-- HellaSwag-nl -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.89</td> <!-- ScandEval rank -->
   <td class="da-rank">3.64</td> <!-- Danish rank -->
   <td class="no-rank">3.94</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.57</td> <!-- Swedish rank -->
   <td class="is-rank">4.83</td> <!-- Icelandic rank -->
   <td class="de-rank">3.59</td> <!-- German rank -->
   <td class="nl-rank">4.25</td> <!-- Dutch rank -->
   <td class="en-rank">3.38</td> <!-- English rank -->
   <td class="da ner">19.82 ± 4.70 / 17.20 ± 3.57</td> <!-- DANSK -->
   <td class="da sent">35.97 ± 3.00 / 49.88 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">2.14 ± 2.61 / 44.16 ± 4.48</td> <!-- ScaLA-da -->
   <td class="da rc">46.59 ± 5.44 / 51.92 ± 6.14</td> <!-- ScandiQA-da -->
   <td class="da summ">58.65 ± 1.07 / 11.57 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">2.65 ± 1.26 / 25.17 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">9.51 ± 2.67 / 40.41 ± 1.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 1.13 / 24.79 ± 0.98</td> <!-- HellaSwag-da -->
   <td class="no ner">30.54 ± 3.75 / 29.88 ± 3.25</td> <!-- NorNE-nb -->
   <td class="no ner">31.34 ± 4.72 / 30.46 ± 4.56</td> <!-- NorNE-nn -->
   <td class="no sent">29.50 ± 4.18 / 49.19 ± 4.59</td> <!-- NoReC -->
   <td class="no summ">53.31 ± 0.98 / 7.37 ± 0.54</td> <!-- No Sammendrag -->
   <td class="no la">-0.13 ± 1.28 / 37.46 ± 3.25</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 1.75 / 39.49 ± 4.41</td> <!-- ScaLA-nn -->
   <td class="no rc">19.59 ± 5.61 / 34.02 ± 8.33</td> <!-- NorQuAD -->
   <td class="no know">2.49 ± 1.09 / 25.63 ± 0.78</td> <!-- MMLU-no -->
   <td class="no reason">2.53 ± 1.16 / 26.30 ± 0.82</td> <!-- HellaSwag-no -->
   <td class="sv ner">29.89 ± 7.13 / 27.65 ± 6.45</td> <!-- SUC3 -->
   <td class="sv sent">74.33 ± 1.07 / 73.73 ± 1.77</td> <!-- SweReC -->
   <td class="sv la">1.06 ± 1.79 / 43.95 ± 3.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.89 ± 2.72 / 52.70 ± 3.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.06 ± 2.11 / 12.53 ± 0.81</td> <!-- SweDN -->
   <td class="sv know">0.93 ± 1.44 / 26.10 ± 1.04</td> <!-- MMLU-sv -->
   <td class="sv reason">0.09 ± 1.37 / 24.84 ± 0.69</td> <!-- HellaSwag-sv -->
   <td class="is ner">17.77 ± 6.81 / 16.42 ± 6.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 1.50 / 34.29 ± 1.64</td> <!-- ScaLA-is -->
   <td class="is rc">8.15 ± 2.21 / 30.75 ± 2.05</td> <!-- NQiI -->
   <td class="is summ">54.21 ± 3.27 / 11.06 ± 1.56</td> <!-- RRN -->
   <td class="is know">0.71 ± 1.34 / 25.40 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">2.88 ± 1.84 / 54.45 ± 2.60</td> <!-- Winogrande-is -->
   <td class="de ner">24.79 ± 6.48 / 22.92 ± 5.74</td> <!-- GermEval -->
   <td class="de sent">47.65 ± 2.85 / 63.11 ± 2.17</td> <!-- SB10k -->
   <td class="de la">2.39 ± 1.46 / 39.92 ± 4.38</td> <!-- ScaLA-de -->
   <td class="de rc">13.39 ± 4.13 / 33.76 ± 5.50</td> <!-- GermanQuAD -->
   <td class="de summ">61.07 ± 4.19 / 16.72 ± 4.33</td> <!-- MLSum -->
   <td class="de know">3.94 ± 1.35 / 27.78 ± 1.07</td> <!-- MMLU-de -->
   <td class="de reason">0.90 ± 0.98 / 25.40 ± 0.65</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.03 ± 4.43 / 19.22 ± 3.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.25 ± 2.95 / 26.57 ± 3.31</td> <!-- Dutch Social -->
   <td class="nl la">1.46 ± 1.83 / 42.29 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.76 ± 1.92 / 52.60 ± 1.99</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.56 ± 1.45 / 10.34 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.46 ± 1.05 / 28.09 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.58 ± 0.81 / 23.58 ± 0.50</td> <!-- HellaSwag-nl -->
   <td class="en ner">35.08 ± 5.88 / 32.44 ± 4.89</td> <!-- CoNLL-en -->
   <td class="en sent">54.40 ± 2.92 / 64.38 ± 2.10</td> <!-- SST5 -->
   <td class="en la">2.97 ± 0.84 / 45.05 ± 4.18</td> <!-- ScaLA-en -->
   <td class="en rc">58.30 ± 2.84 / 71.04 ± 1.83</td> <!-- SQuAD -->
   <td class="en summ">62.19 ± 1.70 / 16.53 ± 1.13</td> <!-- CNN-DailyMail -->
   <td class="en know">7.91 ± 0.72 / 29.30 ± 0.46</td> <!-- MMLU -->
   <td class="en reason">1.60 ± 1.21 / 26.25 ± 0.85</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="da-rank">4.14</td> <!-- Danish rank -->
   <td class="no-rank">4.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.02</td> <!-- Swedish rank -->
   <td class="is-rank">4.86</td> <!-- Icelandic rank -->
   <td class="de-rank">3.90</td> <!-- German rank -->
   <td class="nl-rank">4.21</td> <!-- Dutch rank -->
   <td class="en-rank">3.29</td> <!-- English rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da rc">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
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
   <td class="no rc">5.95 ± 1.53 / 16.20 ± 1.93</td> <!-- NorQuAD -->
   <td class="no know">2.81 ± 1.18 / 25.21 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">2.92 ± 0.88 / 26.67 ± 0.60</td> <!-- HellaSwag-no -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.36 ± 1.44 / 12.82 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">6.52 ± 1.02 / 28.83 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">1.91 ± 1.30 / 26.10 ± 0.65</td> <!-- HellaSwag-sv -->
   <td class="is ner">16.20 ± 1.52 / 16.96 ± 1.71</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is rc">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">1.96 ± 1.72 / 25.55 ± 1.37</td> <!-- ARC-is -->
   <td class="is reason">0.85 ± 1.91 / 52.12 ± 2.92</td> <!-- Winogrande-is -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td class="de summ">59.71 ± 2.14 / 12.23 ± 1.08</td> <!-- MLSum -->
   <td class="de know">6.34 ± 1.10 / 29.19 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">2.94 ± 0.65 / 27.16 ± 0.61</td> <!-- HellaSwag-de -->
   <td class="nl ner">28.30 ± 3.90 / 28.67 ± 3.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.40 ± 2.03 / 10.34 ± 0.54</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.44 ± 0.51 / 29.86 ± 0.35</td> <!-- MMLU-nl -->
   <td class="nl reason">1.70 ± 1.42 / 26.04 ± 0.91</td> <!-- HellaSwag-nl -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en rc">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.14</td> <!-- ScandEval rank -->
   <td class="da-rank">3.83</td> <!-- Danish rank -->
   <td class="no-rank">4.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.73</td> <!-- Swedish rank -->
   <td class="is-rank">5.00</td> <!-- Icelandic rank -->
   <td class="de-rank">4.14</td> <!-- German rank -->
   <td class="nl-rank">4.58</td> <!-- Dutch rank -->
   <td class="en-rank">3.59</td> <!-- English rank -->
   <td class="da ner">17.58 ± 1.95 / 15.48 ± 1.39</td> <!-- DANSK -->
   <td class="da sent">10.47 ± 3.28 / 19.91 ± 2.67</td> <!-- Angry Tweets -->
   <td class="da la">1.23 ± 1.53 / 36.92 ± 3.53</td> <!-- ScaLA-da -->
   <td class="da rc">42.56 ± 1.07 / 49.37 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="da summ">62.56 ± 1.43 / 17.47 ± 1.30</td> <!-- Nordjylland-News -->
   <td class="da know">2.18 ± 1.10 / 24.56 ± 1.33</td> <!-- Danske Talemaader -->
   <td class="da know">4.94 ± 4.46 / 38.22 ± 2.74</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.84 ± 0.96 / 26.18 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">26.90 ± 1.65 / 24.65 ± 2.00</td> <!-- NorNE-nb -->
   <td class="no ner">34.59 ± 3.22 / 33.15 ± 3.49</td> <!-- NorNE-nn -->
   <td class="no sent">31.06 ± 2.28 / 45.42 ± 3.29</td> <!-- NoReC -->
   <td class="no summ">53.77 ± 2.82 / 9.67 ± 1.55</td> <!-- No Sammendrag -->
   <td class="no la">0.21 ± 1.21 / 36.38 ± 2.87</td> <!-- ScaLA-nb -->
   <td class="no la">-0.17 ± 2.08 / 40.22 ± 3.88</td> <!-- ScaLA-nn -->
   <td class="no rc">10.35 ± 0.92 / 22.83 ± 1.06</td> <!-- NorQuAD -->
   <td class="no know">-0.16 ± 0.81 / 23.32 ± 0.68</td> <!-- MMLU-no -->
   <td class="no reason">1.32 ± 1.12 / 25.63 ± 0.98</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.25 ± 1.99 / 20.55 ± 2.20</td> <!-- SUC3 -->
   <td class="sv sent">71.70 ± 1.09 / 71.01 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">-0.82 ± 2.23 / 40.80 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.48 ± 1.52 / 46.93 ± 1.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.39 ± 1.68 / 13.19 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">-0.43 ± 1.13 / 24.95 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">1.98 ± 0.99 / 26.14 ± 0.86</td> <!-- HellaSwag-sv -->
   <td class="is ner">18.38 ± 1.54 / 20.76 ± 1.34</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.49 ± 1.54 / 42.54 ± 4.23</td> <!-- ScaLA-is -->
   <td class="is rc">6.30 ± 2.23 / 23.24 ± 0.99</td> <!-- NQiI -->
   <td class="is summ">51.62 ± 2.09 / 8.63 ± 0.96</td> <!-- RRN -->
   <td class="is know">2.25 ± 1.26 / 26.07 ± 1.15</td> <!-- ARC-is -->
   <td class="is reason">-6.17 ± 1.44 / 52.90 ± 2.42</td> <!-- Winogrande-is -->
   <td class="de ner">21.96 ± 1.53 / 18.48 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">18.66 ± 3.01 / 35.11 ± 2.93</td> <!-- SB10k -->
   <td class="de la">0.16 ± 1.78 / 37.84 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">7.08 ± 1.91 / 18.42 ± 2.90</td> <!-- GermanQuAD -->
   <td class="de summ">56.47 ± 2.05 / 11.00 ± 1.46</td> <!-- MLSum -->
   <td class="de know">1.65 ± 1.53 / 26.62 ± 0.88</td> <!-- MMLU-de -->
   <td class="de reason">0.02 ± 1.24 / 25.61 ± 0.98</td> <!-- HellaSwag-de -->
   <td class="nl ner">22.95 ± 1.99 / 23.05 ± 1.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.40 ± 1.70 / 22.89 ± 4.81</td> <!-- Dutch Social -->
   <td class="nl la">3.12 ± 1.51 / 45.58 ± 4.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.40 ± 1.73 / 32.09 ± 1.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.36 ± 2.03 / 9.96 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.48 ± 0.81 / 24.57 ± 0.67</td> <!-- MMLU-nl -->
   <td class="nl reason">1.28 ± 1.03 / 26.62 ± 0.80</td> <!-- HellaSwag-nl -->
   <td class="en ner">28.63 ± 4.74 / 27.07 ± 4.13</td> <!-- CoNLL-en -->
   <td class="en sent">66.55 ± 0.72 / 58.18 ± 0.62</td> <!-- SST5 -->
   <td class="en la">1.47 ± 1.57 / 45.89 ± 2.92</td> <!-- ScaLA-en -->
   <td class="en rc">35.00 ± 2.01 / 47.83 ± 2.25</td> <!-- SQuAD -->
   <td class="en summ">62.05 ± 1.63 / 16.80 ± 1.01</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.41 ± 1.21 / 23.76 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">-0.04 ± 0.77 / 25.03 ± 0.52</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.15</td> <!-- ScandEval rank -->
   <td class="da-rank">4.29</td> <!-- Danish rank -->
   <td class="no-rank">4.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.96</td> <!-- Swedish rank -->
   <td class="is-rank">5.09</td> <!-- Icelandic rank -->
   <td class="de-rank">3.61</td> <!-- German rank -->
   <td class="nl-rank">3.77</td> <!-- Dutch rank -->
   <td class="en-rank">4.15</td> <!-- English rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da rc">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
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
   <td class="no rc">26.86 ± 1.65 / 50.11 ± 1.80</td> <!-- NorQuAD -->
   <td class="no know">0.21 ± 0.83 / 26.88 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">-0.30 ± 1.13 / 24.48 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.44 ± 0.79 / 12.95 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">1.12 ± 0.42 / 25.27 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.91 ± 0.96 / 24.26 ± 0.64</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is rc">1.04 ± 0.96 / 7.35 ± 3.52</td> <!-- NQiI -->
   <td class="is summ">55.16 ± 1.26 / 10.52 ± 1.13</td> <!-- RRN -->
   <td class="is know">-0.80 ± 2.00 / 23.89 ± 0.86</td> <!-- ARC-is -->
   <td class="is reason">-0.16 ± 0.86 / 32.02 ± 2.77</td> <!-- Winogrande-is -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 5.06 / 49.68 ± 5.74</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de rc">20.44 ± 3.29 / 45.50 ± 3.33</td> <!-- GermanQuAD -->
   <td class="de summ">60.50 ± 0.63 / 13.71 ± 0.75</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.49 ± 1.37 / 47.34 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.24 ± 0.86 / 15.62 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.41 ± 1.15 / 27.75 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">0.15 ± 0.98 / 25.59 ± 0.57</td> <!-- HellaSwag-nl -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en rc">36.51 ± 2.07 / 50.66 ± 1.90</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="da-rank">4.05</td> <!-- Danish rank -->
   <td class="no-rank">5.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.10</td> <!-- Swedish rank -->
   <td class="is-rank">4.90</td> <!-- Icelandic rank -->
   <td class="de-rank">4.07</td> <!-- German rank -->
   <td class="nl-rank">4.06</td> <!-- Dutch rank -->
   <td class="en-rank">3.31</td> <!-- English rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da rc">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
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
   <td class="no rc">7.80 ± 1.19 / 17.09 ± 2.72</td> <!-- NorQuAD -->
   <td class="no know">0.29 ± 1.08 / 24.63 ± 0.79</td> <!-- MMLU-no -->
   <td class="no reason">0.49 ± 1.19 / 24.95 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.29 ± 6.52 / 13.04 ± 1.68</td> <!-- SweDN -->
   <td class="sv know">2.59 ± 0.72 / 26.87 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.84 ± 1.01 / 24.44 ± 0.61</td> <!-- HellaSwag-sv -->
   <td class="is ner">9.50 ± 3.17 / 9.41 ± 3.40</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is rc">3.14 ± 0.71 / 17.84 ± 2.26</td> <!-- NQiI -->
   <td class="is summ">58.92 ± 1.57 / 10.09 ± 1.41</td> <!-- RRN -->
   <td class="is know">-1.28 ± 1.48 / 24.82 ± 0.92</td> <!-- ARC-is -->
   <td class="is reason">1.48 ± 3.56 / 53.95 ± 2.45</td> <!-- Winogrande-is -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">56.42 ± 7.64 / 11.68 ± 1.75</td> <!-- MLSum -->
   <td class="de know">2.75 ± 0.91 / 27.17 ± 0.72</td> <!-- MMLU-de -->
   <td class="de reason">3.41 ± 1.30 / 27.45 ± 0.79</td> <!-- HellaSwag-de -->
   <td class="nl ner">18.66 ± 4.43 / 17.56 ± 4.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.36 ± 0.81 / 11.72 ± 0.73</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.09 ± 1.13 / 25.90 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">1.44 ± 1.12 / 26.50 ± 0.68</td> <!-- HellaSwag-nl -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en rc">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="da-rank">4.31</td> <!-- Danish rank -->
   <td class="no-rank">4.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.44</td> <!-- Swedish rank -->
   <td class="is-rank">4.90</td> <!-- Icelandic rank -->
   <td class="de-rank">4.07</td> <!-- German rank -->
   <td class="nl-rank">4.35</td> <!-- Dutch rank -->
   <td class="en-rank">3.62</td> <!-- English rank -->
   <td class="da ner">12.68 ± 1.39 / 12.32 ± 1.19</td> <!-- DANSK -->
   <td class="da sent">3.61 ± 2.69 / 19.01 ± 3.95</td> <!-- Angry Tweets -->
   <td class="da la">1.79 ± 0.97 / 36.23 ± 3.19</td> <!-- ScaLA-da -->
   <td class="da rc">28.12 ± 3.14 / 32.48 ± 3.57</td> <!-- ScandiQA-da -->
   <td class="da summ">56.85 ± 1.37 / 10.17 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">-0.03 ± 0.59 / 23.99 ± 0.76</td> <!-- Danske Talemaader -->
   <td class="da know">6.03 ± 3.05 / 37.58 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.20 ± 0.86 / 25.12 ± 0.70</td> <!-- HellaSwag-da -->
   <td class="no ner">26.60 ± 1.99 / 23.60 ± 2.05</td> <!-- NorNE-nb -->
   <td class="no ner">23.70 ± 1.58 / 23.04 ± 2.17</td> <!-- NorNE-nn -->
   <td class="no sent">6.21 ± 2.55 / 23.74 ± 3.28</td> <!-- NoReC -->
   <td class="no summ">48.59 ± 1.59 / 6.80 ± 0.45</td> <!-- No Sammendrag -->
   <td class="no la">-0.39 ± 0.76 / 33.40 ± 0.31</td> <!-- ScaLA-nb -->
   <td class="no la">0.21 ± 0.41 / 35.33 ± 3.02</td> <!-- ScaLA-nn -->
   <td class="no rc">4.65 ± 1.00 / 10.23 ± 1.68</td> <!-- NorQuAD -->
   <td class="no know">-1.13 ± 0.96 / 21.80 ± 0.52</td> <!-- MMLU-no -->
   <td class="no reason">-0.51 ± 0.40 / 24.82 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.22 ± 1.75 / 17.97 ± 2.10</td> <!-- SUC3 -->
   <td class="sv sent">11.52 ± 7.20 / 29.30 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.72 ± 1.21 / 34.96 ± 1.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">27.27 ± 3.03 / 31.25 ± 3.24</td> <!-- ScandiQA-sv -->
   <td class="sv summ">45.57 ± 0.97 / 9.20 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">0.69 ± 0.65 / 22.10 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">0.68 ± 0.79 / 25.25 ± 0.76</td> <!-- HellaSwag-sv -->
   <td class="is ner">13.43 ± 1.36 / 13.81 ± 1.45</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.14 ± 1.52 / 36.93 ± 3.69</td> <!-- ScaLA-is -->
   <td class="is rc">3.71 ± 1.14 / 16.21 ± 2.86</td> <!-- NQiI -->
   <td class="is summ">51.93 ± 3.96 / 8.48 ± 0.87</td> <!-- RRN -->
   <td class="is know">0.95 ± 1.48 / 22.52 ± 1.05</td> <!-- ARC-is -->
   <td class="is reason">2.90 ± 2.91 / 56.72 ± 0.69</td> <!-- Winogrande-is -->
   <td class="de ner">19.94 ± 0.96 / 18.01 ± 0.59</td> <!-- GermEval -->
   <td class="de sent">19.64 ± 5.59 / 36.97 ± 5.41</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.32 ± 0.30</td> <!-- ScaLA-de -->
   <td class="de rc">8.78 ± 1.33 / 20.50 ± 1.50</td> <!-- GermanQuAD -->
   <td class="de summ">57.06 ± 3.46 / 11.78 ± 1.69</td> <!-- MLSum -->
   <td class="de know">0.32 ± 0.94 / 22.52 ± 0.61</td> <!-- MMLU-de -->
   <td class="de reason">-0.65 ± 0.72 / 24.04 ± 0.46</td> <!-- HellaSwag-de -->
   <td class="nl ner">20.95 ± 2.02 / 25.63 ± 1.96</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.84 ± 1.76 / 27.74 ± 5.49</td> <!-- Dutch Social -->
   <td class="nl la">-1.50 ± 1.30 / 34.07 ± 0.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.67 ± 1.77 / 30.14 ± 1.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">53.89 ± 2.61 / 10.53 ± 0.37</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.45 ± 1.59 / 24.24 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.31 ± 1.39 / 23.58 ± 0.40</td> <!-- HellaSwag-nl -->
   <td class="en ner">31.14 ± 1.79 / 28.54 ± 0.86</td> <!-- CoNLL-en -->
   <td class="en sent">43.97 ± 5.28 / 55.08 ± 4.26</td> <!-- SST5 -->
   <td class="en la">3.49 ± 2.49 / 46.52 ± 4.13</td> <!-- ScaLA-en -->
   <td class="en rc">47.91 ± 4.97 / 60.41 ± 3.91</td> <!-- SQuAD -->
   <td class="en summ">62.20 ± 1.04 / 17.61 ± 0.50</td> <!-- CNN-DailyMail -->
   <td class="en know">0.12 ± 1.55 / 23.00 ± 0.82</td> <!-- MMLU -->
   <td class="en reason">0.13 ± 1.34 / 24.53 ± 0.49</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.42</td> <!-- ScandEval rank -->
   <td class="da-rank">4.40</td> <!-- Danish rank -->
   <td class="no-rank">4.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.61</td> <!-- Swedish rank -->
   <td class="is-rank">5.05</td> <!-- Icelandic rank -->
   <td class="de-rank">4.35</td> <!-- German rank -->
   <td class="nl-rank">4.44</td> <!-- Dutch rank -->
   <td class="en-rank">3.59</td> <!-- English rank -->
   <td class="da ner">8.97 ± 3.18 / 8.62 ± 2.72</td> <!-- DANSK -->
   <td class="da sent">2.66 ± 2.70 / 16.29 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.38 / 44.50 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">24.92 ± 1.68 / 28.73 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="da summ">55.39 ± 0.68 / 10.01 ± 0.63</td> <!-- Nordjylland-News -->
   <td class="da know">0.28 ± 0.93 / 23.92 ± 0.72</td> <!-- Danske Talemaader -->
   <td class="da know">3.55 ± 3.45 / 35.45 ± 1.54</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.41 ± 1.41 / 25.02 ± 0.71</td> <!-- HellaSwag-da -->
   <td class="no ner">20.37 ± 5.55 / 21.57 ± 3.57</td> <!-- NorNE-nb -->
   <td class="no ner">21.27 ± 5.10 / 22.34 ± 4.41</td> <!-- NorNE-nn -->
   <td class="no sent">7.60 ± 2.24 / 26.47 ± 2.89</td> <!-- NoReC -->
   <td class="no summ">49.27 ± 1.15 / 7.39 ± 0.36</td> <!-- No Sammendrag -->
   <td class="no la">1.31 ± 1.92 / 45.75 ± 3.36</td> <!-- ScaLA-nb -->
   <td class="no la">0.51 ± 1.81 / 38.71 ± 2.95</td> <!-- ScaLA-nn -->
   <td class="no rc">4.80 ± 1.18 / 10.53 ± 2.12</td> <!-- NorQuAD -->
   <td class="no know">-0.90 ± 0.97 / 21.85 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">-1.00 ± 0.70 / 24.21 ± 0.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">13.64 ± 5.84 / 16.38 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">9.34 ± 6.26 / 26.00 ± 3.56</td> <!-- SweReC -->
   <td class="sv la">2.20 ± 1.59 / 41.62 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">26.06 ± 2.35 / 30.05 ± 2.29</td> <!-- ScandiQA-sv -->
   <td class="sv summ">37.49 ± 0.77 / 9.36 ± 0.25</td> <!-- SweDN -->
   <td class="sv know">-0.00 ± 0.96 / 22.03 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.78 ± 1.51 / 25.50 ± 0.87</td> <!-- HellaSwag-sv -->
   <td class="is ner">13.60 ± 1.50 / 13.99 ± 1.39</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.28 ± 1.41 / 37.58 ± 4.34</td> <!-- ScaLA-is -->
   <td class="is rc">4.09 ± 1.03 / 16.34 ± 2.86</td> <!-- NQiI -->
   <td class="is summ">50.00 ± 3.22 / 7.84 ± 0.71</td> <!-- RRN -->
   <td class="is know">-0.11 ± 0.95 / 22.28 ± 0.83</td> <!-- ARC-is -->
   <td class="is reason">2.51 ± 3.01 / 51.41 ± 3.27</td> <!-- Winogrande-is -->
   <td class="de ner">18.77 ± 3.96 / 18.65 ± 3.26</td> <!-- GermEval -->
   <td class="de sent">12.59 ± 3.85 / 22.64 ± 2.25</td> <!-- SB10k -->
   <td class="de la">1.64 ± 1.30 / 34.84 ± 2.12</td> <!-- ScaLA-de -->
   <td class="de rc">9.27 ± 1.07 / 21.58 ± 1.37</td> <!-- GermanQuAD -->
   <td class="de summ">46.31 ± 1.46 / 8.68 ± 0.61</td> <!-- MLSum -->
   <td class="de know">0.84 ± 0.81 / 22.50 ± 0.61</td> <!-- MMLU-de -->
   <td class="de reason">0.01 ± 1.07 / 24.43 ± 0.50</td> <!-- HellaSwag-de -->
   <td class="nl ner">15.68 ± 5.54 / 22.21 ± 5.42</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.73 ± 2.20 / 27.67 ± 4.00</td> <!-- Dutch Social -->
   <td class="nl la">0.63 ± 1.05 / 43.48 ± 2.98</td> <!-- ScaLA-nl -->
   <td class="nl rc">19.73 ± 1.42 / 27.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.53 ± 2.03 / 9.14 ± 0.47</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.30 ± 0.75 / 24.43 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.36 ± 0.85 / 24.09 ± 0.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">30.73 ± 4.30 / 29.47 ± 4.10</td> <!-- CoNLL-en -->
   <td class="en sent">59.51 ± 3.73 / 54.82 ± 2.43</td> <!-- SST5 -->
   <td class="en la">1.55 ± 1.90 / 43.18 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en rc">49.03 ± 1.47 / 60.00 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">57.73 ± 4.93 / 15.68 ± 1.21</td> <!-- CNN-DailyMail -->
   <td class="en know">0.11 ± 1.23 / 23.20 ± 0.56</td> <!-- MMLU -->
   <td class="en reason">-0.06 ± 0.39 / 24.60 ± 0.44</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da-rank">4.72</td> <!-- Danish rank -->
   <td class="no-rank">4.40</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.58</td> <!-- Swedish rank -->
   <td class="is-rank">5.01</td> <!-- Icelandic rank -->
   <td class="de-rank">4.45</td> <!-- German rank -->
   <td class="nl-rank">4.85</td> <!-- Dutch rank -->
   <td class="en-rank">4.43</td> <!-- English rank -->
   <td class="da ner">13.72 ± 1.83 / 13.41 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">3.79 ± 3.11 / 21.06 ± 4.74</td> <!-- Angry Tweets -->
   <td class="da la">-0.45 ± 0.70 / 39.69 ± 4.95</td> <!-- ScaLA-da -->
   <td class="da rc">14.69 ± 2.86 / 17.28 ± 3.01</td> <!-- ScandiQA-da -->
   <td class="da summ">47.44 ± 1.55 / 6.04 ± 0.58</td> <!-- Nordjylland-News -->
   <td class="da know">-0.58 ± 2.44 / 25.72 ± 1.40</td> <!-- Danske Talemaader -->
   <td class="da know">10.99 ± 5.42 / 38.26 ± 1.92</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.51 ± 1.30 / 24.79 ± 0.70</td> <!-- HellaSwag-da -->
   <td class="no ner">24.37 ± 2.17 / 26.91 ± 2.28</td> <!-- NorNE-nb -->
   <td class="no ner">24.69 ± 1.85 / 27.60 ± 2.48</td> <!-- NorNE-nn -->
   <td class="no sent">8.84 ± 4.19 / 29.74 ± 3.45</td> <!-- NoReC -->
   <td class="no summ">53.61 ± 2.33 / 6.64 ± 0.79</td> <!-- No Sammendrag -->
   <td class="no la">-1.20 ± 1.10 / 36.09 ± 3.06</td> <!-- ScaLA-nb -->
   <td class="no la">-0.50 ± 1.21 / 36.68 ± 3.16</td> <!-- ScaLA-nn -->
   <td class="no rc">0.16 ± 0.13 / 2.31 ± 0.44</td> <!-- NorQuAD -->
   <td class="no know">-0.81 ± 0.69 / 24.67 ± 1.24</td> <!-- MMLU-no -->
   <td class="no reason">-0.71 ± 1.01 / 24.42 ± 0.63</td> <!-- HellaSwag-no -->
   <td class="sv ner">19.15 ± 1.75 / 20.52 ± 1.77</td> <!-- SUC3 -->
   <td class="sv sent">-3.03 ± 7.40 / 24.39 ± 3.87</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.12 / 36.05 ± 2.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.18 ± 3.82 / 16.55 ± 4.25</td> <!-- ScandiQA-sv -->
   <td class="sv summ">51.51 ± 1.96 / 11.46 ± 0.73</td> <!-- SweDN -->
   <td class="sv know">0.02 ± 1.30 / 25.25 ± 0.94</td> <!-- MMLU-sv -->
   <td class="sv reason">0.04 ± 0.79 / 24.92 ± 0.73</td> <!-- HellaSwag-sv -->
   <td class="is ner">14.74 ± 2.42 / 16.01 ± 2.04</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.25 ± 0.60 / 34.69 ± 3.02</td> <!-- ScaLA-is -->
   <td class="is rc">1.35 ± 0.73 / 10.92 ± 2.52</td> <!-- NQiI -->
   <td class="is summ">52.66 ± 3.89 / 8.73 ± 0.71</td> <!-- RRN -->
   <td class="is know">1.21 ± 0.80 / 26.20 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">1.69 ± 2.26 / 49.46 ± 3.56</td> <!-- Winogrande-is -->
   <td class="de ner">16.89 ± 1.62 / 16.63 ± 1.80</td> <!-- GermEval -->
   <td class="de sent">2.74 ± 3.46 / 23.30 ± 3.11</td> <!-- SB10k -->
   <td class="de la">-0.34 ± 1.06 / 39.21 ± 4.13</td> <!-- ScaLA-de -->
   <td class="de rc">0.28 ± 0.27 / 2.91 ± 0.92</td> <!-- GermanQuAD -->
   <td class="de summ">54.79 ± 2.10 / 8.47 ± 1.10</td> <!-- MLSum -->
   <td class="de know">-0.32 ± 0.88 / 25.45 ± 0.97</td> <!-- MMLU-de -->
   <td class="de reason">0.18 ± 0.99 / 25.72 ± 0.91</td> <!-- HellaSwag-de -->
   <td class="nl ner">17.49 ± 2.94 / 18.59 ± 2.66</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.01 ± 1.88 / 15.88 ± 1.32</td> <!-- Dutch Social -->
   <td class="nl la">-0.02 ± 0.15 / 34.86 ± 2.12</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.53 ± 0.36 / 3.23 ± 0.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.46 ± 1.93 / 9.47 ± 0.33</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.33 ± 0.71 / 25.12 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.10 ± 0.85 / 24.87 ± 0.65</td> <!-- HellaSwag-nl -->
   <td class="en ner">31.26 ± 3.84 / 30.44 ± 3.28</td> <!-- CoNLL-en -->
   <td class="en sent">26.69 ± 10.82 / 34.46 ± 8.00</td> <!-- SST5 -->
   <td class="en la">1.78 ± 1.67 / 43.50 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">13.88 ± 1.36 / 22.49 ± 2.14</td> <!-- SQuAD -->
   <td class="en summ">52.05 ± 1.59 / 12.74 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">1.51 ± 0.81 / 25.05 ± 0.75</td> <!-- MMLU -->
   <td class="en reason">-0.76 ± 0.97 / 24.52 ± 0.59</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="da-rank">4.45</td> <!-- Danish rank -->
   <td class="no-rank">4.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.76</td> <!-- Swedish rank -->
   <td class="is-rank">5.13</td> <!-- Icelandic rank -->
   <td class="de-rank">4.58</td> <!-- German rank -->
   <td class="nl-rank">4.84</td> <!-- Dutch rank -->
   <td class="en-rank">4.32</td> <!-- English rank -->
   <td class="da ner">12.11 ± 1.07 / 11.48 ± 1.07</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 3.22 / 18.95 ± 3.93</td> <!-- Angry Tweets -->
   <td class="da la">0.25 ± 1.87 / 39.65 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da rc">14.02 ± 2.56 / 16.74 ± 2.74</td> <!-- ScandiQA-da -->
   <td class="da summ">56.53 ± 0.95 / 8.45 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">1.05 ± 1.51 / 26.37 ± 0.83</td> <!-- Danske Talemaader -->
   <td class="da know">10.81 ± 4.60 / 38.73 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.50 ± 0.85 / 24.15 ± 0.67</td> <!-- HellaSwag-da -->
   <td class="no ner">20.89 ± 2.55 / 22.28 ± 2.32</td> <!-- NorNE-nb -->
   <td class="no ner">19.62 ± 1.91 / 21.82 ± 2.35</td> <!-- NorNE-nn -->
   <td class="no sent">2.78 ± 4.25 / 26.17 ± 3.37</td> <!-- NoReC -->
   <td class="no summ">53.93 ± 2.39 / 6.60 ± 0.99</td> <!-- No Sammendrag -->
   <td class="no la">-0.98 ± 1.80 / 40.63 ± 4.03</td> <!-- ScaLA-nb -->
   <td class="no la">0.93 ± 2.26 / 40.91 ± 4.95</td> <!-- ScaLA-nn -->
   <td class="no rc">0.15 ± 0.13 / 2.19 ± 0.57</td> <!-- NorQuAD -->
   <td class="no know">-0.48 ± 1.78 / 25.53 ± 1.87</td> <!-- MMLU-no -->
   <td class="no reason">-0.53 ± 0.95 / 24.68 ± 0.62</td> <!-- HellaSwag-no -->
   <td class="sv ner">17.09 ± 2.33 / 18.78 ± 2.11</td> <!-- SUC3 -->
   <td class="sv sent">7.41 ± 9.32 / 28.42 ± 3.18</td> <!-- SweReC -->
   <td class="sv la">0.47 ± 1.48 / 38.19 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">11.73 ± 3.22 / 13.94 ± 3.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">38.30 ± 1.88 / 8.09 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">0.30 ± 0.87 / 25.76 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">0.06 ± 1.19 / 24.33 ± 0.53</td> <!-- HellaSwag-sv -->
   <td class="is ner">13.70 ± 2.05 / 15.01 ± 2.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.83 ± 0.71 / 32.99 ± 0.27</td> <!-- ScaLA-is -->
   <td class="is rc">0.94 ± 0.54 / 10.22 ± 2.52</td> <!-- NQiI -->
   <td class="is summ">50.30 ± 4.32 / 7.82 ± 0.77</td> <!-- RRN -->
   <td class="is know">1.10 ± 1.16 / 25.43 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">-0.07 ± 3.01 / 46.28 ± 3.42</td> <!-- Winogrande-is -->
   <td class="de ner">15.54 ± 1.74 / 15.29 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">2.51 ± 1.90 / 21.27 ± 3.22</td> <!-- SB10k -->
   <td class="de la">0.36 ± 1.07 / 39.04 ± 3.21</td> <!-- ScaLA-de -->
   <td class="de rc">1.77 ± 0.67 / 5.69 ± 0.96</td> <!-- GermanQuAD -->
   <td class="de summ">49.41 ± 1.73 / 7.27 ± 0.41</td> <!-- MLSum -->
   <td class="de know">-1.46 ± 0.84 / 24.84 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">-0.18 ± 1.25 / 24.79 ± 1.02</td> <!-- HellaSwag-de -->
   <td class="nl ner">15.82 ± 3.13 / 16.46 ± 2.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.62 ± 1.55 / 16.18 ± 1.88</td> <!-- Dutch Social -->
   <td class="nl la">1.16 ± 1.38 / 34.30 ± 1.27</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.25 ± 1.17 / 5.89 ± 0.97</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.82 ± 3.44 / 9.74 ± 0.58</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.36 ± 1.10 / 25.96 ± 0.81</td> <!-- MMLU-nl -->
   <td class="nl reason">0.34 ± 1.33 / 25.40 ± 0.83</td> <!-- HellaSwag-nl -->
   <td class="en ner">29.96 ± 3.19 / 28.98 ± 3.29</td> <!-- CoNLL-en -->
   <td class="en sent">18.64 ± 8.52 / 28.83 ± 5.86</td> <!-- SST5 -->
   <td class="en la">1.85 ± 1.20 / 44.03 ± 3.98</td> <!-- ScaLA-en -->
   <td class="en rc">26.90 ± 1.56 / 36.91 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">52.96 ± 1.38 / 14.23 ± 0.78</td> <!-- CNN-DailyMail -->
   <td class="en know">1.34 ± 0.74 / 25.67 ± 1.03</td> <!-- MMLU -->
   <td class="en reason">0.10 ± 1.29 / 24.71 ± 0.69</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   <td>13.1.0</td> <!-- NorNE-nb version -->
   <td>13.1.0</td> <!-- NorNE-nn version -->
   <td>13.1.0</td> <!-- NoReC version -->
   <td>13.1.0</td> <!-- No Sammendrag version -->
   <td>13.1.0</td> <!-- ScaLA-nb version -->
   <td>13.1.0</td> <!-- ScaLA-nn version -->
   <td>13.1.0</td> <!-- NorQuAD version -->
   <td>13.1.0</td> <!-- MMLU-no version -->
   <td>13.1.0</td> <!-- HellaSwag-no version -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   <td>13.1.0</td> <!-- SweDN version -->
   <td>13.1.0</td> <!-- MMLU-sv version -->
   <td>13.1.0</td> <!-- HellaSwag-sv version -->
   <td>13.1.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.1.0</td> <!-- ScaLA-is version -->
   <td>13.1.0</td> <!-- NQiI version -->
   <td>13.1.0</td> <!-- RRN version -->
   <td>13.1.0</td> <!-- ARC-is version -->
   <td>13.1.0</td> <!-- Winogrande-is version -->
   <td>13.1.0</td> <!-- GermEval version -->
   <td>13.1.0</td> <!-- SB10k version -->
   <td>13.1.0</td> <!-- ScaLA-de version -->
   <td>13.1.0</td> <!-- GermanQuAD version -->
   <td>13.1.0</td> <!-- MLSum version -->
   <td>13.1.0</td> <!-- MMLU-de version -->
   <td>13.1.0</td> <!-- HellaSwag-de version -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.19</td> <!-- ScandEval rank -->
   <td class="da-rank">5.17</td> <!-- Danish rank -->
   <td class="no-rank">4.94</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.11</td> <!-- Swedish rank -->
   <td class="is-rank">5.60</td> <!-- Icelandic rank -->
   <td class="de-rank">4.94</td> <!-- German rank -->
   <td class="nl-rank">5.25</td> <!-- Dutch rank -->
   <td class="en-rank">5.30</td> <!-- English rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.02 ± 0.02 / 0.03 ± 0.03</td> <!-- ScandiQA-da -->
   <td class="da summ">42.82 ± 0.93 / 0.20 ± 0.02</td> <!-- Nordjylland-News -->
   <td class="da know">4.55 ± 2.15 / 25.74 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">-1.17 ± 3.12 / 34.84 ± 1.63</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.26 ± 1.34 / 24.88 ± 0.69</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no summ">41.98 ± 0.64 / 0.21 ± 0.04</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.09 ± 0.03</td> <!-- NorQuAD -->
   <td class="no know">1.14 ± 1.04 / 24.51 ± 0.78</td> <!-- MMLU-no -->
   <td class="no reason">0.64 ± 1.18 / 24.68 ± 0.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.16 ± 0.14</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
   <td class="sv summ">40.82 ± 1.17 / 0.34 ± 0.05</td> <!-- SweDN -->
   <td class="sv know">1.19 ± 1.32 / 24.74 ± 1.06</td> <!-- MMLU-sv -->
   <td class="sv reason">1.55 ± 0.84 / 25.30 ± 0.69</td> <!-- HellaSwag-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- NQiI -->
   <td class="is summ">36.58 ± 2.96 / 0.16 ± 0.02</td> <!-- RRN -->
   <td class="is know">-0.00 ± 1.73 / 24.71 ± 1.42</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 43.48 ± 0.89</td> <!-- Winogrande-is -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- GermanQuAD -->
   <td class="de summ">37.66 ± 0.76 / 0.15 ± 0.02</td> <!-- MLSum -->
   <td class="de know">0.87 ± 0.51 / 24.67 ± 0.61</td> <!-- MMLU-de -->
   <td class="de reason">1.95 ± 1.33 / 25.62 ± 0.89</td> <!-- HellaSwag-de -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 8.62 ± 0.30</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 0.01 ± 0.00</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.74 ± 0.57 / 0.22 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.32 ± 0.67 / 24.79 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">1.73 ± 1.07 / 26.61 ± 0.61</td> <!-- HellaSwag-nl -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">2.48 ± 1.94 / 34.52 ± 0.85</td> <!-- ScaLA-en -->
   <td class="en rc">0.01 ± 0.02 / 0.03 ± 0.02</td> <!-- SQuAD -->
   <td class="en summ">44.80 ± 0.36 / 0.32 ± 0.04</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.69 ± 0.77 / 22.76 ± 0.40</td> <!-- MMLU -->
   <td class="en reason">0.37 ± 0.95 / 24.71 ± 0.44</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   <td>13.0.0</td> <!-- NorNE-nb version -->
   <td>13.0.0</td> <!-- NorNE-nn version -->
   <td>13.0.0</td> <!-- NoReC version -->
   <td>13.0.0</td> <!-- No Sammendrag version -->
   <td>13.0.0</td> <!-- ScaLA-nb version -->
   <td>13.0.0</td> <!-- ScaLA-nn version -->
   <td>13.0.0</td> <!-- NorQuAD version -->
   <td>13.0.0</td> <!-- MMLU-no version -->
   <td>13.0.0</td> <!-- HellaSwag-no version -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   <td>13.0.0</td> <!-- MIM-GOLD-NER version -->
   <td>13.0.0</td> <!-- ScaLA-is version -->
   <td>13.0.0</td> <!-- NQiI version -->
   <td>13.0.0</td> <!-- RRN version -->
   <td>13.0.0</td> <!-- ARC-is version -->
   <td>13.0.0</td> <!-- Winogrande-is version -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.40</td> <!-- ScandEval rank -->
   <td class="da-rank">5.31</td> <!-- Danish rank -->
   <td class="no-rank">5.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.21</td> <!-- Swedish rank -->
   <td class="is-rank">6.03</td> <!-- Icelandic rank -->
   <td class="de-rank">5.13</td> <!-- German rank -->
   <td class="nl-rank">5.54</td> <!-- Dutch rank -->
   <td class="en-rank">5.49</td> <!-- English rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da rc">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
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
   <td class="no rc">0.00 ± 0.00 / 0.74 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">0.72 ± 0.81 / 22.86 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">-0.20 ± 1.06 / 24.94 ± 0.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">31.89 ± 0.27 / 2.03 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">-0.37 ± 1.08 / 22.43 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">0.36 ± 0.83 / 25.08 ± 0.77</td> <!-- HellaSwag-sv -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">-0.02 ± 1.16 / 22.75 ± 0.50</td> <!-- ARC-is -->
   <td class="is reason">0.47 ± 4.14 / 46.93 ± 3.13</td> <!-- Winogrande-is -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.19 ± 1.24 / 17.20 ± 1.22</td> <!-- SB10k -->
   <td class="de la">-0.12 ± 0.91 / 36.65 ± 3.92</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 1.29 ± 0.49</td> <!-- GermanQuAD -->
   <td class="de summ">29.43 ± 1.80 / 2.35 ± 0.59</td> <!-- MLSum -->
   <td class="de know">-0.69 ± 0.79 / 22.79 ± 0.51</td> <!-- MMLU-de -->
   <td class="de reason">0.15 ± 0.35 / 24.25 ± 0.59</td> <!-- HellaSwag-de -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">30.20 ± 0.68 / 2.14 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.45 ± 0.84 / 24.91 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.56 ± 0.80 / 23.53 ± 0.49</td> <!-- HellaSwag-nl -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en rc">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
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
   <td>12.10.8</td> <!-- ARC-is version -->
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
  <a href="https://scandeval.com/germanic-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Germanic NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-Y2tgK&quot; src=&quot;https://datawrapper.dwcdn.net/Y2tgK/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
