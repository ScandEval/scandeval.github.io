---
layout: leaderboard
title: Mainland Scandinavian NLG 🇩🇰🇳🇴🇸🇪
---

<center>Last updated: 31/10/2024 16:24:31 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="mainland-scandinavian-nlg-test" class="sortable fixed centered small-font">
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
   <td class="rank">1.18</td> <!-- ScandEval rank -->
   <td class="da-rank">1.16</td> <!-- Danish rank -->
   <td class="no-rank">1.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.20</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.29</td> <!-- ScandEval rank -->
   <td class="da-rank">1.21</td> <!-- Danish rank -->
   <td class="no-rank">1.36</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.30</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.29</td> <!-- ScandEval rank -->
   <td class="da-rank">1.26</td> <!-- Danish rank -->
   <td class="no-rank">1.33</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.28</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.47</td> <!-- ScandEval rank -->
   <td class="da-rank">1.47</td> <!-- Danish rank -->
   <td class="no-rank">1.46</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.49</td> <!-- Swedish rank -->
   <td class="da ner">63.62 ± 3.74 / 53.29 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">60.19 ± 3.31 / 73.13 ± 2.17</td> <!-- Angry Tweets -->
   <td class="da la">50.07 ± 5.86 / 72.94 ± 4.16</td> <!-- ScaLA-da -->
   <td class="da rc">60.97 ± 2.76 / 66.71 ± 2.27</td> <!-- ScandiQA-da -->
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
   <td class="no rc">60.87 ± 4.82 / 82.30 ± 2.52</td> <!-- NorQuAD -->
   <td class="no know">62.45 ± 1.70 / 71.60 ± 1.37</td> <!-- MMLU-no -->
   <td class="no reason">65.29 ± 3.59 / 72.50 ± 3.24</td> <!-- HellaSwag-no -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.41 / 22.47 ± 0.82</td> <!-- SweDN -->
   <td class="sv know">61.55 ± 1.68 / 71.02 ± 1.21</td> <!-- MMLU-sv -->
   <td class="sv reason">66.21 ± 3.22 / 73.40 ± 2.77</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="da-rank">1.46</td> <!-- Danish rank -->
   <td class="no-rank">1.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.66</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,314 ± 1,202 / 776 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="da-rank">1.35</td> <!-- Danish rank -->
   <td class="no-rank">2.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.42</td> <!-- Swedish rank -->
   <td class="da ner">58.60 ± 1.62 / 47.13 ± 1.62</td> <!-- DANSK -->
   <td class="da sent">54.96 ± 1.30 / 68.41 ± 1.45</td> <!-- Angry Tweets -->
   <td class="da la">70.55 ± 1.00 / 85.14 ± 0.52</td> <!-- ScaLA-da -->
   <td class="da rc">60.95 ± 0.31 / 65.86 ± 0.36</td> <!-- ScandiQA-da -->
   <td class="da summ">66.99 ± 1.09 / 22.45 ± 1.09</td> <!-- Nordjylland-News -->
   <td class="da know">80.95 ± 1.28 / 85.57 ± 0.97</td> <!-- Danske Talemaader -->
   <td class="da know">76.88 ± 1.46 / 84.65 ± 0.97</td> <!-- Danish Citizen Tests -->
   <td class="da reason">73.73 ± 0.85 / 80.10 ± 0.64</td> <!-- HellaSwag-da -->
   <td class="no ner">85.07 ± 0.60 / 84.47 ± 0.48</td> <!-- NorNE-nb -->
   <td class="no ner">81.43 ± 0.59 / 79.70 ± 0.68</td> <!-- NorNE-nn -->
   <td class="no sent">38.52 ± 2.49 / 53.36 ± 2.80</td> <!-- NoReC -->
   <td class="no summ">65.02 ± 0.45 / 16.74 ± 0.52</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no rc">40.52 ± 2.89 / 66.67 ± 3.21</td> <!-- NorQuAD -->
   <td class="no know">41.57 ± 0.66 / 55.57 ± 0.53</td> <!-- MMLU-no -->
   <td class="no reason">72.25 ± 0.79 / 78.88 ± 0.64</td> <!-- HellaSwag-no -->
   <td class="sv ner">88.78 ± 1.05 / 85.30 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">81.73 ± 0.71 / 80.87 ± 0.96</td> <!-- SweReC -->
   <td class="sv la">75.83 ± 0.49 / 87.67 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.35 ± 0.70 / 65.90 ± 0.55</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.96 ± 0.09 / 23.17 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">41.07 ± 0.83 / 55.49 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">75.73 ± 0.72 / 81.68 ± 0.55</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.80</td> <!-- ScandEval rank -->
   <td class="da-rank">1.67</td> <!-- Danish rank -->
   <td class="no-rank">1.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.84</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="da-rank">1.68</td> <!-- Danish rank -->
   <td class="no-rank">1.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.92</td> <!-- Swedish rank -->
   <td class="da ner">63.10 ± 2.12 / 55.10 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">53.09 ± 3.85 / 68.18 ± 2.27</td> <!-- Angry Tweets -->
   <td class="da la">40.98 ± 4.46 / 69.10 ± 2.72</td> <!-- ScaLA-da -->
   <td class="da rc">51.13 ± 1.89 / 63.12 ± 1.61</td> <!-- ScandiQA-da -->
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
   <td class="no rc">39.71 ± 2.59 / 71.60 ± 1.57</td> <!-- NorQuAD -->
   <td class="no know">63.58 ± 1.91 / 72.58 ± 1.42</td> <!-- MMLU-no -->
   <td class="no reason">63.41 ± 2.52 / 71.91 ± 1.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.25 ± 0.18 / 22.84 ± 0.44</td> <!-- SweDN -->
   <td class="sv know">61.31 ± 2.07 / 70.78 ± 1.60</td> <!-- MMLU-sv -->
   <td class="sv reason">66.73 ± 2.34 / 74.65 ± 1.78</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="da-rank">1.60</td> <!-- Danish rank -->
   <td class="no-rank">2.02</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.95</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="da-rank">1.80</td> <!-- Danish rank -->
   <td class="no-rank">2.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.88</td> <!-- Swedish rank -->
   <td class="da ner">56.96 ± 2.39 / 45.84 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">55.11 ± 4.11 / 69.60 ± 2.69</td> <!-- Angry Tweets -->
   <td class="da la">42.64 ± 3.22 / 71.04 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da rc">54.58 ± 2.19 / 64.12 ± 1.41</td> <!-- ScandiQA-da -->
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
   <td class="no rc">41.92 ± 3.36 / 72.51 ± 1.91</td> <!-- NorQuAD -->
   <td class="no know">51.01 ± 2.61 / 63.20 ± 1.96</td> <!-- MMLU-no -->
   <td class="no reason">58.23 ± 5.79 / 67.46 ± 4.92</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.30 / 21.60 ± 0.76</td> <!-- SweDN -->
   <td class="sv know">53.56 ± 2.20 / 64.88 ± 1.66</td> <!-- MMLU-sv -->
   <td class="sv reason">59.70 ± 4.69 / 69.38 ± 3.70</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="da-rank">1.73</td> <!-- Danish rank -->
   <td class="no-rank">2.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">1.94</td> <!-- Swedish rank -->
   <td class="da ner">58.06 ± 2.48 / 50.10 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">53.24 ± 4.04 / 67.81 ± 2.74</td> <!-- Angry Tweets -->
   <td class="da la">39.71 ± 4.96 / 65.90 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da rc">62.51 ± 1.48 / 67.47 ± 1.39</td> <!-- ScandiQA-da -->
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
   <td class="no rc">57.44 ± 4.59 / 78.69 ± 3.09</td> <!-- NorQuAD -->
   <td class="no know">43.88 ± 3.11 / 57.62 ± 2.27</td> <!-- MMLU-no -->
   <td class="no reason">53.85 ± 3.43 / 64.34 ± 2.65</td> <!-- HellaSwag-no -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv rc">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.43 ± 0.33 / 24.92 ± 0.74</td> <!-- SweDN -->
   <td class="sv know">46.16 ± 2.67 / 59.53 ± 2.04</td> <!-- MMLU-sv -->
   <td class="sv reason">50.41 ± 5.18 / 62.34 ± 3.86</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="da-rank">2.04</td> <!-- Danish rank -->
   <td class="no-rank">2.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.00</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="da-rank">1.98</td> <!-- Danish rank -->
   <td class="no-rank">2.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.12</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/sol (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,701 ± 876 / 771 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="da-rank">2.08</td> <!-- Danish rank -->
   <td class="no-rank">2.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.16</td> <!-- Swedish rank -->
   <td class="da ner">54.91 ± 1.53 / 36.29 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">44.38 ± 2.83 / 57.19 ± 3.61</td> <!-- Angry Tweets -->
   <td class="da la">21.11 ± 3.23 / 45.43 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">58.96 ± 1.71 / 65.85 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">66.89 ± 0.89 / 22.65 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">61.12 ± 1.49 / 70.29 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">64.86 ± 2.64 / 76.05 ± 1.94</td> <!-- Danish Citizen Tests -->
   <td class="da reason">67.96 ± 1.07 / 75.68 ± 0.86</td> <!-- HellaSwag-da -->
   <td class="no ner">65.14 ± 1.62 / 52.85 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">65.88 ± 1.53 / 52.89 ± 2.29</td> <!-- NorNE-nn -->
   <td class="no sent">57.06 ± 1.54 / 71.09 ± 1.17</td> <!-- NoReC -->
   <td class="no summ">66.21 ± 0.76 / 20.29 ± 1.10</td> <!-- No Sammendrag -->
   <td class="no la">26.41 ± 3.80 / 51.92 ± 5.30</td> <!-- ScaLA-nb -->
   <td class="no la">19.58 ± 1.29 / 53.93 ± 2.90</td> <!-- ScaLA-nn -->
   <td class="no rc">51.60 ± 1.97 / 77.87 ± 1.44</td> <!-- NorQuAD -->
   <td class="no know">36.06 ± 0.69 / 51.47 ± 0.52</td> <!-- MMLU-no -->
   <td class="no reason">64.97 ± 1.25 / 73.41 ± 1.01</td> <!-- HellaSwag-no -->
   <td class="sv ner">57.51 ± 2.30 / 37.74 ± 3.15</td> <!-- SUC3 -->
   <td class="sv sent">77.31 ± 1.01 / 70.55 ± 2.26</td> <!-- SweReC -->
   <td class="sv la">25.06 ± 5.02 / 49.04 ± 4.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.77 / 67.43 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.22 ± 0.19 / 18.86 ± 0.30</td> <!-- SweDN -->
   <td class="sv know">39.52 ± 0.58 / 54.47 ± 0.38</td> <!-- MMLU-sv -->
   <td class="sv reason">70.93 ± 1.29 / 78.03 ± 1.01</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="da-rank">2.05</td> <!-- Danish rank -->
   <td class="no-rank">2.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.20</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da-rank">2.12</td> <!-- Danish rank -->
   <td class="no-rank">2.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.26</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="da-rank">2.03</td> <!-- Danish rank -->
   <td class="no-rank">2.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.31</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.24</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="da-rank">2.18</td> <!-- Danish rank -->
   <td class="no-rank">2.61</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.36</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da-rank">2.34</td> <!-- Danish rank -->
   <td class="no-rank">2.54</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.33</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da-rank">2.12</td> <!-- Danish rank -->
   <td class="no-rank">2.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.45</td> <!-- Swedish rank -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da rc">56.51 ± 1.80 / 64.01 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="da summ">68.06 ± 1.42 / 24.28 ± 1.31</td> <!-- Nordjylland-News -->
   <td class="da know">74.24 ± 2.14 / 80.62 ± 1.61</td> <!-- Danske Talemaader -->
   <td class="da know">70.86 ± 3.58 / 80.31 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">41.49 ± 2.88 / 55.86 ± 2.17</td> <!-- HellaSwag-da -->
   <td class="no ner">61.18 ± 2.76 / 56.36 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">65.16 ± 3.97 / 55.74 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">55.61 ± 4.02 / 68.27 ± 3.49</td> <!-- NoReC -->
   <td class="no summ">65.99 ± 0.31 / 19.46 ± 0.47</td> <!-- No Sammendrag -->
   <td class="no la">20.84 ± 5.41 / 49.36 ± 4.98</td> <!-- ScaLA-nb -->
   <td class="no la">9.12 ± 3.51 / 43.06 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no rc">42.92 ± 3.08 / 69.13 ± 2.85</td> <!-- NorQuAD -->
   <td class="no know">27.77 ± 2.86 / 45.43 ± 2.04</td> <!-- MMLU-no -->
   <td class="no reason">39.67 ± 4.37 / 54.26 ± 3.37</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.43 ± 1.59 / 65.06 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.58 ± 0.22 / 22.52 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">32.54 ± 2.61 / 49.30 ± 1.93</td> <!-- MMLU-sv -->
   <td class="sv reason">34.94 ± 3.79 / 50.39 ± 3.23</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da-rank">2.33</td> <!-- Danish rank -->
   <td class="no-rank">2.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.40</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da-rank">2.02</td> <!-- Danish rank -->
   <td class="no-rank">2.78</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.61</td> <!-- Swedish rank -->
   <td class="da ner">51.08 ± 1.60 / 35.83 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">54.69 ± 0.99 / 69.50 ± 0.93</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 1.48 / 62.15 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da rc">56.56 ± 0.76 / 64.32 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="da summ">66.90 ± 0.23 / 20.90 ± 0.64</td> <!-- Nordjylland-News -->
   <td class="da know">79.39 ± 1.11 / 84.29 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">73.22 ± 1.83 / 81.91 ± 1.32</td> <!-- Danish Citizen Tests -->
   <td class="da reason">48.16 ± 1.14 / 60.83 ± 0.97</td> <!-- HellaSwag-da -->
   <td class="no ner">62.43 ± 0.94 / 51.64 ± 2.45</td> <!-- NorNE-nb -->
   <td class="no ner">60.68 ± 0.74 / 48.91 ± 2.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.41 ± 1.46 / 69.49 ± 1.05</td> <!-- NoReC -->
   <td class="no summ">63.65 ± 0.26 / 13.19 ± 0.53</td> <!-- No Sammendrag -->
   <td class="no la">-1.16 ± 1.31 / 33.56 ± 0.43</td> <!-- ScaLA-nb -->
   <td class="no la">0.30 ± 0.71 / 34.08 ± 0.32</td> <!-- ScaLA-nn -->
   <td class="no rc">49.15 ± 2.79 / 76.77 ± 1.59</td> <!-- NorQuAD -->
   <td class="no know">38.47 ± 0.66 / 53.57 ± 0.50</td> <!-- MMLU-no -->
   <td class="no reason">40.13 ± 2.77 / 54.87 ± 2.11</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.37 ± 3.04 / 42.16 ± 4.00</td> <!-- SUC3 -->
   <td class="sv sent">75.98 ± 1.15 / 74.44 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">17.98 ± 1.97 / 56.01 ± 2.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.07 ± 0.74 / 64.24 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.09 / 14.42 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">32.81 ± 0.91 / 49.28 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">36.24 ± 1.44 / 51.96 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.0.0</td> <!-- DANSK version -->
   <td>12.0.0</td> <!-- Angry Tweets version -->
   <td>12.0.0</td> <!-- ScaLA-da version -->
   <td>12.0.0</td> <!-- ScandiQA-da version -->
   <td>12.0.0</td> <!-- Nordjylland-News version -->
   <td>12.0.0</td> <!-- Danske Talemaader version -->
   <td>12.0.0</td> <!-- Danish Citizen Tests version -->
   <td>12.0.0</td> <!-- HellaSwag-da version -->
   <td>12.0.0</td> <!-- NorNE-nb version -->
   <td>12.0.0</td> <!-- NorNE-nn version -->
   <td>12.0.0</td> <!-- NoReC version -->
   <td>12.0.0</td> <!-- No Sammendrag version -->
   <td>12.0.0</td> <!-- ScaLA-nb version -->
   <td>12.0.0</td> <!-- ScaLA-nn version -->
   <td>12.0.0</td> <!-- NorQuAD version -->
   <td>12.0.0</td> <!-- MMLU-no version -->
   <td>12.0.0</td> <!-- HellaSwag-no version -->
   <td>12.0.0</td> <!-- SUC3 version -->
   <td>12.0.0</td> <!-- SweReC version -->
   <td>12.0.0</td> <!-- ScaLA-sv version -->
   <td>12.0.0</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>12.0.0</td> <!-- MMLU-sv version -->
   <td>12.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da-rank">2.26</td> <!-- Danish rank -->
   <td class="no-rank">2.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.47</td> <!-- Swedish rank -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da rc">58.28 ± 1.98 / 64.33 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="da summ">68.04 ± 1.34 / 24.72 ± 1.42</td> <!-- Nordjylland-News -->
   <td class="da know">67.37 ± 4.12 / 75.55 ± 3.01</td> <!-- Danske Talemaader -->
   <td class="da know">66.75 ± 3.42 / 77.34 ± 2.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.21 ± 3.40 / 56.48 ± 2.62</td> <!-- HellaSwag-da -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no summ">66.08 ± 0.32 / 20.15 ± 0.64</td> <!-- No Sammendrag -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no rc">42.42 ± 2.92 / 69.53 ± 3.17</td> <!-- NorQuAD -->
   <td class="no know">27.31 ± 2.26 / 45.04 ± 1.66</td> <!-- MMLU-no -->
   <td class="no reason">41.63 ± 2.84 / 56.02 ± 2.19</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.75 ± 1.46 / 65.08 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.06 ± 0.31 / 23.91 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">33.71 ± 2.28 / 50.08 ± 1.68</td> <!-- MMLU-sv -->
   <td class="sv reason">41.45 ± 3.36 / 55.51 ± 2.69</td> <!-- HellaSwag-sv -->
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
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/orpo-llama-3-swe (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,974 ± 1,208 / 1,032 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.35</td> <!-- Danish rank -->
   <td class="no-rank">2.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.44</td> <!-- Swedish rank -->
   <td class="da ner">46.75 ± 2.79 / 29.40 ± 2.22</td> <!-- DANSK -->
   <td class="da sent">51.73 ± 1.40 / 66.43 ± 1.93</td> <!-- Angry Tweets -->
   <td class="da la">24.73 ± 4.78 / 53.98 ± 6.10</td> <!-- ScaLA-da -->
   <td class="da rc">59.97 ± 1.27 / 65.74 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">65.21 ± 0.51 / 18.86 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">55.72 ± 2.05 / 66.59 ± 1.56</td> <!-- Danske Talemaader -->
   <td class="da know">61.59 ± 2.64 / 73.95 ± 1.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.43 ± 2.44 / 43.11 ± 2.03</td> <!-- HellaSwag-da -->
   <td class="no ner">61.63 ± 1.64 / 48.09 ± 2.89</td> <!-- NorNE-nb -->
   <td class="no ner">61.30 ± 1.94 / 50.08 ± 2.60</td> <!-- NorNE-nn -->
   <td class="no sent">48.85 ± 2.22 / 64.93 ± 2.00</td> <!-- NoReC -->
   <td class="no summ">63.67 ± 1.11 / 16.08 ± 1.70</td> <!-- No Sammendrag -->
   <td class="no la">24.15 ± 6.12 / 56.29 ± 6.81</td> <!-- ScaLA-nb -->
   <td class="no la">21.33 ± 3.03 / 58.05 ± 2.59</td> <!-- ScaLA-nn -->
   <td class="no rc">53.66 ± 4.34 / 75.19 ± 3.59</td> <!-- NorQuAD -->
   <td class="no know">33.52 ± 1.36 / 49.78 ± 1.04</td> <!-- MMLU-no -->
   <td class="no reason">26.04 ± 2.54 / 43.74 ± 2.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.93 ± 2.85 / 38.87 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.68 / 75.13 ± 1.85</td> <!-- SweReC -->
   <td class="sv la">26.02 ± 4.38 / 52.19 ± 5.44</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.84 ± 0.92 / 65.92 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.99 ± 0.26 / 18.65 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">36.35 ± 1.03 / 51.91 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">27.22 ± 2.24 / 45.02 ± 1.74</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.25</td> <!-- Danish rank -->
   <td class="no-rank">2.72</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
   <td class="da ner">52.22 ± 2.07 / 38.82 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">50.66 ± 1.88 / 62.04 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">23.57 ± 3.82 / 56.09 ± 4.62</td> <!-- ScaLA-da -->
   <td class="da rc">53.82 ± 2.13 / 61.94 ± 1.63</td> <!-- ScandiQA-da -->
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
   <td class="no rc">38.50 ± 3.93 / 69.99 ± 2.23</td> <!-- NorQuAD -->
   <td class="no know">32.30 ± 3.42 / 48.32 ± 2.61</td> <!-- MMLU-no -->
   <td class="no reason">34.43 ± 2.91 / 49.65 ± 2.23</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.24 / 21.77 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">37.60 ± 3.30 / 52.46 ± 2.31</td> <!-- MMLU-sv -->
   <td class="sv reason">31.78 ± 2.98 / 47.11 ± 2.71</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da-rank">2.36</td> <!-- Danish rank -->
   <td class="no-rank">2.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.44</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="da-rank">2.30</td> <!-- Danish rank -->
   <td class="no-rank">2.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.39</td> <!-- Swedish rank -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da rc">57.26 ± 1.76 / 63.60 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="da summ">67.31 ± 1.40 / 23.24 ± 1.64</td> <!-- Nordjylland-News -->
   <td class="da know">66.49 ± 2.90 / 74.84 ± 2.12</td> <!-- Danske Talemaader -->
   <td class="da know">60.41 ± 1.95 / 72.97 ± 1.45</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.51 ± 3.95 / 45.74 ± 3.03</td> <!-- HellaSwag-da -->
   <td class="no ner">54.04 ± 2.86 / 48.50 ± 2.85</td> <!-- NorNE-nb -->
   <td class="no ner">62.21 ± 3.31 / 50.38 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">54.74 ± 3.71 / 67.81 ± 2.80</td> <!-- NoReC -->
   <td class="no summ">65.60 ± 0.49 / 19.07 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">14.51 ± 1.97 / 40.94 ± 1.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.38 ± 4.69 / 37.62 ± 2.92</td> <!-- ScaLA-nn -->
   <td class="no rc">42.83 ± 3.31 / 69.15 ± 2.50</td> <!-- NorQuAD -->
   <td class="no know">25.82 ± 1.66 / 43.75 ± 1.18</td> <!-- MMLU-no -->
   <td class="no reason">32.01 ± 3.74 / 48.40 ± 2.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.98 ± 1.65 / 65.44 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.89 ± 0.44 / 23.94 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">34.80 ± 2.79 / 50.82 ± 2.10</td> <!-- MMLU-sv -->
   <td class="sv reason">36.65 ± 5.07 / 51.56 ± 4.13</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>timpal0l/dolphin-2.9-llama3-8b-flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,018 ± 1,216 / 996 ± 324</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="da-rank">2.38</td> <!-- Danish rank -->
   <td class="no-rank">2.77</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.39</td> <!-- Swedish rank -->
   <td class="da ner">51.37 ± 2.38 / 37.56 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">52.17 ± 3.44 / 67.14 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">27.98 ± 7.51 / 60.57 ± 5.72</td> <!-- ScaLA-da -->
   <td class="da rc">51.65 ± 0.84 / 59.94 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">66.25 ± 1.15 / 19.93 ± 1.18</td> <!-- Nordjylland-News -->
   <td class="da know">57.31 ± 2.81 / 68.05 ± 2.05</td> <!-- Danske Talemaader -->
   <td class="da know">54.17 ± 2.95 / 68.20 ± 1.83</td> <!-- Danish Citizen Tests -->
   <td class="da reason">27.65 ± 3.28 / 44.53 ± 2.63</td> <!-- HellaSwag-da -->
   <td class="no ner">64.51 ± 3.28 / 51.06 ± 4.78</td> <!-- NorNE-nb -->
   <td class="no ner">65.66 ± 3.82 / 53.90 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">52.90 ± 4.31 / 65.38 ± 3.73</td> <!-- NoReC -->
   <td class="no summ">64.12 ± 0.39 / 15.41 ± 0.84</td> <!-- No Sammendrag -->
   <td class="no la">29.34 ± 4.34 / 59.36 ± 4.64</td> <!-- ScaLA-nb -->
   <td class="no la">17.42 ± 4.38 / 52.01 ± 3.50</td> <!-- ScaLA-nn -->
   <td class="no rc">38.49 ± 4.41 / 67.16 ± 3.41</td> <!-- NorQuAD -->
   <td class="no know">25.77 ± 3.46 / 43.40 ± 2.66</td> <!-- MMLU-no -->
   <td class="no reason">31.80 ± 2.89 / 46.80 ± 2.26</td> <!-- HellaSwag-no -->
   <td class="sv ner">65.33 ± 2.38 / 46.88 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">74.99 ± 3.45 / 76.76 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">32.65 ± 5.08 / 61.25 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.71 ± 1.34 / 64.54 ± 1.00</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.53 ± 0.29 / 19.24 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">33.16 ± 2.11 / 49.26 ± 1.55</td> <!-- MMLU-sv -->
   <td class="sv reason">32.51 ± 2.97 / 48.24 ± 2.10</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama3-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,695 ± 1,277 / 532 ± 183</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">2.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="da ner">51.40 ± 3.08 / 37.70 ± 3.28</td> <!-- DANSK -->
   <td class="da sent">42.13 ± 0.57 / 45.91 ± 0.39</td> <!-- Angry Tweets -->
   <td class="da la">3.91 ± 2.02 / 34.38 ± 0.47</td> <!-- ScaLA-da -->
   <td class="da rc">57.81 ± 1.03 / 66.28 ± 0.48</td> <!-- ScandiQA-da -->
   <td class="da summ">66.70 ± 0.98 / 21.56 ± 0.85</td> <!-- Nordjylland-News -->
   <td class="da know">65.15 ± 1.40 / 73.55 ± 1.05</td> <!-- Danske Talemaader -->
   <td class="da know">57.36 ± 2.49 / 70.88 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">44.55 ± 1.98 / 57.29 ± 1.77</td> <!-- HellaSwag-da -->
   <td class="no ner">66.94 ± 2.67 / 60.25 ± 3.14</td> <!-- NorNE-nb -->
   <td class="no ner">67.69 ± 1.87 / 61.57 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">48.40 ± 3.28 / 61.42 ± 3.56</td> <!-- NoReC -->
   <td class="no summ">65.84 ± 0.40 / 19.08 ± 0.78</td> <!-- No Sammendrag -->
   <td class="no la">24.26 ± 2.68 / 57.31 ± 2.64</td> <!-- ScaLA-nb -->
   <td class="no la">18.43 ± 1.34 / 52.28 ± 2.63</td> <!-- ScaLA-nn -->
   <td class="no rc">46.80 ± 2.74 / 74.57 ± 2.20</td> <!-- NorQuAD -->
   <td class="no know">33.55 ± 1.06 / 49.43 ± 0.76</td> <!-- MMLU-no -->
   <td class="no reason">47.32 ± 2.75 / 59.11 ± 2.44</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.19 ± 2.83 / 51.22 ± 3.61</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.64 / 61.59 ± 0.77</td> <!-- SweReC -->
   <td class="sv la">5.34 ± 1.42 / 34.32 ± 0.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.70 ± 0.87 / 66.00 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.25 ± 0.16 / 20.28 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">36.23 ± 0.91 / 51.68 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">43.60 ± 1.33 / 56.86 ± 1.15</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da-rank">2.25</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.51</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="da-rank">2.39</td> <!-- Danish rank -->
   <td class="no-rank">2.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.56</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.41</td> <!-- Danish rank -->
   <td class="no-rank">2.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da rc">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="da summ">67.69 ± 1.19 / 23.90 ± 1.25</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no rc">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
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
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="da-rank">2.41</td> <!-- Danish rank -->
   <td class="no-rank">2.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da rc">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="da summ">67.69 ± 1.19 / 23.88 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no rc">44.39 ± 3.95 / 70.76 ± 3.10</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
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
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da-rank">2.26</td> <!-- Danish rank -->
   <td class="no-rank">2.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da rc">58.17 ± 1.71 / 63.79 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="da summ">66.25 ± 1.29 / 20.33 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">65.32 ± 3.33 / 73.95 ± 2.50</td> <!-- Danske Talemaader -->
   <td class="da know">64.76 ± 3.24 / 75.94 ± 2.37</td> <!-- Danish Citizen Tests -->
   <td class="da reason">33.70 ± 2.78 / 50.16 ± 2.01</td> <!-- HellaSwag-da -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no summ">65.23 ± 0.55 / 18.64 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no rc">41.43 ± 3.34 / 67.26 ± 2.73</td> <!-- NorQuAD -->
   <td class="no know">27.42 ± 2.13 / 45.20 ± 1.58</td> <!-- MMLU-no -->
   <td class="no reason">36.05 ± 3.95 / 51.68 ± 2.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.92 ± 1.64 / 64.87 ± 1.47</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.62 ± 0.42 / 23.90 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">27.95 ± 2.57 / 45.86 ± 1.85</td> <!-- MMLU-sv -->
   <td class="sv reason">36.11 ± 3.54 / 51.60 ± 2.44</td> <!-- HellaSwag-sv -->
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
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.57</td> <!-- Danish rank -->
   <td class="no-rank">2.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.62</td> <!-- Swedish rank -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">57.26 ± 0.79 / 63.80 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="da summ">66.89 ± 0.71 / 21.43 ± 0.57</td> <!-- Nordjylland-News -->
   <td class="da know">64.32 ± 1.99 / 73.00 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">53.18 ± 2.37 / 67.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">43.42 ± 1.05 / 57.50 ± 0.80</td> <!-- HellaSwag-da -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no summ">65.72 ± 0.39 / 19.24 ± 0.78</td> <!-- No Sammendrag -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no rc">49.03 ± 4.22 / 74.38 ± 3.92</td> <!-- NorQuAD -->
   <td class="no know">32.37 ± 1.15 / 49.00 ± 0.91</td> <!-- MMLU-no -->
   <td class="no reason">47.62 ± 1.62 / 60.59 ± 1.18</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.16 ± 1.23 / 65.78 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.36 ± 0.14 / 18.81 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">35.01 ± 0.99 / 51.07 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">43.72 ± 0.69 / 57.66 ± 0.50</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
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
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
   <td class="da ner">45.94 ± 3.62 / 35.68 ± 3.35</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 4.52 / 62.28 ± 4.29</td> <!-- Angry Tweets -->
   <td class="da la">28.04 ± 3.83 / 58.31 ± 5.00</td> <!-- ScaLA-da -->
   <td class="da rc">57.65 ± 1.66 / 62.03 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">66.65 ± 1.28 / 21.98 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">68.88 ± 2.98 / 76.64 ± 2.22</td> <!-- Danske Talemaader -->
   <td class="da know">64.81 ± 3.96 / 75.78 ± 2.64</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.63 ± 2.25 / 42.03 ± 2.02</td> <!-- HellaSwag-da -->
   <td class="no ner">49.67 ± 3.12 / 43.26 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">61.11 ± 1.93 / 50.15 ± 4.14</td> <!-- NorNE-nn -->
   <td class="no sent">56.07 ± 5.22 / 68.93 ± 4.07</td> <!-- NoReC -->
   <td class="no summ">64.97 ± 0.59 / 18.14 ± 1.03</td> <!-- No Sammendrag -->
   <td class="no la">3.81 ± 3.09 / 34.47 ± 1.22</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no rc">44.98 ± 4.12 / 68.18 ± 3.39</td> <!-- NorQuAD -->
   <td class="no know">28.63 ± 2.26 / 45.94 ± 1.79</td> <!-- MMLU-no -->
   <td class="no reason">25.43 ± 4.85 / 43.48 ± 3.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.57 ± 3.34 / 33.94 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.53 ± 2.55 / 77.96 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">33.43 ± 3.89 / 61.87 ± 4.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.87 ± 1.52 / 64.53 ± 1.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.76 ± 0.41 / 21.92 ± 0.79</td> <!-- SweDN -->
   <td class="sv know">28.89 ± 2.22 / 46.41 ± 1.55</td> <!-- MMLU-sv -->
   <td class="sv reason">30.36 ± 2.80 / 47.15 ± 2.26</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
   <td class="da ner">46.06 ± 3.28 / 35.43 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 4.23 / 61.68 ± 4.43</td> <!-- Angry Tweets -->
   <td class="da la">27.68 ± 4.25 / 57.59 ± 5.15</td> <!-- ScaLA-da -->
   <td class="da rc">57.78 ± 1.43 / 62.26 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="da summ">66.62 ± 1.35 / 21.92 ± 1.28</td> <!-- Nordjylland-News -->
   <td class="da know">68.64 ± 3.34 / 76.45 ± 2.52</td> <!-- Danske Talemaader -->
   <td class="da know">66.17 ± 3.73 / 76.72 ± 2.55</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.95 ± 2.64 / 42.19 ± 2.42</td> <!-- HellaSwag-da -->
   <td class="no ner">49.69 ± 2.90 / 43.57 ± 2.90</td> <!-- NorNE-nb -->
   <td class="no ner">61.78 ± 2.03 / 49.91 ± 4.24</td> <!-- NorNE-nn -->
   <td class="no sent">55.87 ± 5.21 / 68.97 ± 3.95</td> <!-- NoReC -->
   <td class="no summ">64.94 ± 0.66 / 18.09 ± 1.08</td> <!-- No Sammendrag -->
   <td class="no la">2.99 ± 3.04 / 34.16 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no rc">44.62 ± 4.06 / 68.17 ± 3.48</td> <!-- NorQuAD -->
   <td class="no know">28.26 ± 2.85 / 45.78 ± 2.14</td> <!-- MMLU-no -->
   <td class="no reason">25.83 ± 5.55 / 43.63 ± 4.29</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.28 ± 3.05 / 34.01 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.62 ± 2.52 / 78.04 ± 2.98</td> <!-- SweReC -->
   <td class="sv la">33.23 ± 4.72 / 61.29 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.00 ± 1.69 / 64.62 ± 1.44</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.68 ± 0.43 / 21.83 ± 0.75</td> <!-- SweDN -->
   <td class="sv know">29.95 ± 1.74 / 47.23 ± 1.24</td> <!-- MMLU-sv -->
   <td class="sv reason">31.12 ± 3.68 / 47.85 ± 2.80</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.31</td> <!-- Danish rank -->
   <td class="no-rank">2.94</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.53</td> <!-- Swedish rank -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da rc">57.87 ± 2.32 / 64.53 ± 1.73</td> <!-- ScandiQA-da -->
   <td class="da summ">66.77 ± 0.99 / 21.60 ± 0.91</td> <!-- Nordjylland-News -->
   <td class="da know">72.92 ± 2.52 / 79.69 ± 1.88</td> <!-- Danske Talemaader -->
   <td class="da know">68.11 ± 3.00 / 78.52 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">40.62 ± 3.23 / 55.12 ± 2.44</td> <!-- HellaSwag-da -->
   <td class="no ner">53.68 ± 2.01 / 49.22 ± 2.67</td> <!-- NorNE-nb -->
   <td class="no ner">61.92 ± 4.06 / 49.03 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.19 / 57.76 ± 2.55</td> <!-- NoReC -->
   <td class="no summ">64.23 ± 0.75 / 16.90 ± 0.94</td> <!-- No Sammendrag -->
   <td class="no la">0.91 ± 1.78 / 33.51 ± 0.85</td> <!-- ScaLA-nb -->
   <td class="no la">1.24 ± 1.66 / 33.71 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no rc">47.76 ± 2.93 / 70.99 ± 2.39</td> <!-- NorQuAD -->
   <td class="no know">28.59 ± 2.31 / 46.48 ± 1.80</td> <!-- MMLU-no -->
   <td class="no reason">42.57 ± 2.86 / 56.64 ± 2.17</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 2.00 / 64.06 ± 1.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.13 ± 0.34 / 19.26 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">29.81 ± 2.25 / 47.46 ± 1.72</td> <!-- MMLU-sv -->
   <td class="sv reason">35.59 ± 3.75 / 51.76 ± 2.63</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da-rank">2.28</td> <!-- Danish rank -->
   <td class="no-rank">2.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.58</td> <!-- Swedish rank -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da rc">56.82 ± 1.75 / 62.40 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="da summ">65.58 ± 1.30 / 17.82 ± 1.12</td> <!-- Nordjylland-News -->
   <td class="da know">67.48 ± 3.13 / 75.62 ± 2.33</td> <!-- Danske Talemaader -->
   <td class="da know">63.69 ± 2.43 / 75.31 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">32.11 ± 3.47 / 48.55 ± 2.67</td> <!-- HellaSwag-da -->
   <td class="no ner">55.93 ± 2.70 / 50.51 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">63.85 ± 2.45 / 53.11 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">50.41 ± 5.49 / 64.49 ± 4.37</td> <!-- NoReC -->
   <td class="no summ">65.10 ± 0.51 / 18.12 ± 0.74</td> <!-- No Sammendrag -->
   <td class="no la">15.74 ± 4.15 / 41.16 ± 2.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.23 ± 4.69 / 34.70 ± 1.39</td> <!-- ScaLA-nn -->
   <td class="no rc">39.81 ± 2.81 / 65.65 ± 2.64</td> <!-- NorQuAD -->
   <td class="no know">26.34 ± 1.48 / 44.69 ± 1.13</td> <!-- MMLU-no -->
   <td class="no reason">34.85 ± 4.33 / 50.23 ± 3.39</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.75 ± 1.13 / 64.72 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.48 / 23.65 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">27.24 ± 2.07 / 45.51 ± 1.53</td> <!-- MMLU-sv -->
   <td class="sv reason">32.04 ± 4.21 / 48.67 ± 3.11</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.83</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.56</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.34</td> <!-- Danish rank -->
   <td class="no-rank">2.84</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.65</td> <!-- Swedish rank -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da rc">59.90 ± 0.84 / 65.47 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="da summ">67.50 ± 0.95 / 23.95 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">66.61 ± 0.93 / 74.86 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">64.80 ± 1.46 / 76.46 ± 1.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.18 ± 0.99 / 46.64 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">61.41 ± 1.71 / 52.32 ± 2.63</td> <!-- NorNE-nb -->
   <td class="no ner">59.49 ± 1.26 / 49.45 ± 3.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.19 ± 1.64 / 63.36 ± 1.52</td> <!-- NoReC -->
   <td class="no summ">64.22 ± 0.52 / 16.72 ± 0.66</td> <!-- No Sammendrag -->
   <td class="no la">15.17 ± 2.64 / 50.25 ± 4.51</td> <!-- ScaLA-nb -->
   <td class="no la">10.78 ± 1.99 / 50.08 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no rc">48.99 ± 2.91 / 73.08 ± 2.26</td> <!-- NorQuAD -->
   <td class="no know">27.64 ± 1.39 / 45.78 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">25.74 ± 1.87 / 43.95 ± 1.58</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.67 ± 0.96 / 64.58 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.18 ± 0.24 / 18.13 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">31.04 ± 1.08 / 48.29 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">23.57 ± 1.68 / 42.37 ± 1.34</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.5.0</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.0</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.81</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.62</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.51</td> <!-- Swedish rank -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da rc">56.46 ± 1.48 / 61.69 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="da summ">65.46 ± 1.23 / 17.73 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">61.29 ± 2.33 / 70.82 ± 1.78</td> <!-- Danske Talemaader -->
   <td class="da know">60.29 ± 2.58 / 72.97 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.33 ± 2.11 / 45.86 ± 1.72</td> <!-- HellaSwag-da -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no summ">64.96 ± 0.56 / 17.92 ± 0.82</td> <!-- No Sammendrag -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no rc">39.21 ± 3.48 / 64.09 ± 3.49</td> <!-- NorQuAD -->
   <td class="no know">26.64 ± 1.95 / 44.88 ± 1.41</td> <!-- MMLU-no -->
   <td class="no reason">31.14 ± 2.64 / 48.01 ± 2.14</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.42 ± 1.64 / 63.83 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.54 ± 0.48 / 23.67 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 2.34 / 46.95 ± 1.75</td> <!-- MMLU-sv -->
   <td class="sv reason">37.45 ± 3.61 / 52.85 ± 2.76</td> <!-- HellaSwag-sv -->
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
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="da-rank">2.55</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.50</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">2.93</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
   <td class="da ner">45.61 ± 3.06 / 35.04 ± 2.94</td> <!-- DANSK -->
   <td class="da sent">53.73 ± 3.06 / 67.51 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">17.08 ± 5.36 / 52.62 ± 5.62</td> <!-- ScaLA-da -->
   <td class="da rc">56.67 ± 1.19 / 61.18 ± 1.07</td> <!-- ScandiQA-da -->
   <td class="da summ">66.14 ± 1.40 / 20.98 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">60.58 ± 2.62 / 69.80 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">57.89 ± 3.66 / 70.00 ± 2.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.45 ± 1.87 / 35.47 ± 1.77</td> <!-- HellaSwag-da -->
   <td class="no ner">48.24 ± 3.18 / 42.53 ± 3.52</td> <!-- NorNE-nb -->
   <td class="no ner">61.50 ± 1.54 / 50.90 ± 4.58</td> <!-- NorNE-nn -->
   <td class="no sent">49.40 ± 3.40 / 60.71 ± 3.33</td> <!-- NoReC -->
   <td class="no summ">64.56 ± 0.80 / 17.62 ± 1.06</td> <!-- No Sammendrag -->
   <td class="no la">24.12 ± 3.24 / 59.38 ± 2.25</td> <!-- ScaLA-nb -->
   <td class="no la">13.20 ± 3.16 / 54.42 ± 3.04</td> <!-- ScaLA-nn -->
   <td class="no rc">47.93 ± 3.46 / 69.52 ± 3.06</td> <!-- NorQuAD -->
   <td class="no know">26.21 ± 2.32 / 42.54 ± 1.71</td> <!-- MMLU-no -->
   <td class="no reason">17.00 ± 2.59 / 33.52 ± 2.18</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.61 ± 3.11 / 34.10 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 2.01 / 78.30 ± 2.42</td> <!-- SweReC -->
   <td class="sv la">34.16 ± 4.39 / 60.06 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.77 ± 1.76 / 63.50 ± 1.47</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.77 ± 0.46 / 22.42 ± 0.84</td> <!-- SweDN -->
   <td class="sv know">29.77 ± 2.44 / 46.25 ± 1.64</td> <!-- MMLU-sv -->
   <td class="sv reason">25.38 ± 3.56 / 39.34 ± 3.89</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.67</td> <!-- Swedish rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da rc">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
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
   <td class="no rc">30.27 ± 2.28 / 62.04 ± 2.19</td> <!-- NorQuAD -->
   <td class="no know">28.18 ± 1.89 / 45.23 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">36.20 ± 3.97 / 50.74 ± 3.38</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.94 ± 0.21 / 22.99 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">27.51 ± 3.08 / 45.43 ± 2.37</td> <!-- MMLU-sv -->
   <td class="sv reason">42.29 ± 5.08 / 55.43 ± 4.50</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da-rank">2.40</td> <!-- Danish rank -->
   <td class="no-rank">2.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.72</td> <!-- Swedish rank -->
   <td class="da ner">39.12 ± 4.28 / 28.74 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">36.47 ± 4.90 / 50.72 ± 6.21</td> <!-- Angry Tweets -->
   <td class="da la">26.76 ± 4.78 / 57.02 ± 5.13</td> <!-- ScaLA-da -->
   <td class="da rc">58.75 ± 1.19 / 64.41 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="da summ">67.89 ± 1.20 / 24.67 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">91.32 ± 0.66 / 93.45 ± 0.50</td> <!-- Danske Talemaader -->
   <td class="da know">79.92 ± 1.83 / 85.82 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.76 ± 3.27 / 42.17 ± 2.72</td> <!-- HellaSwag-da -->
   <td class="no ner">50.43 ± 2.27 / 42.19 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">54.20 ± 1.81 / 43.92 ± 2.94</td> <!-- NorNE-nn -->
   <td class="no sent">39.21 ± 5.64 / 56.54 ± 6.43</td> <!-- NoReC -->
   <td class="no summ">65.46 ± 0.77 / 19.21 ± 1.10</td> <!-- No Sammendrag -->
   <td class="no la">20.51 ± 4.43 / 52.48 ± 5.96</td> <!-- ScaLA-nb -->
   <td class="no la">11.66 ± 4.10 / 48.13 ± 6.13</td> <!-- ScaLA-nn -->
   <td class="no rc">51.57 ± 3.87 / 73.95 ± 3.51</td> <!-- NorQuAD -->
   <td class="no know">28.97 ± 1.40 / 45.70 ± 1.02</td> <!-- MMLU-no -->
   <td class="no reason">25.41 ± 3.81 / 42.75 ± 3.44</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.10 ± 2.60 / 35.06 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">73.05 ± 5.27 / 74.56 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">30.29 ± 2.63 / 61.40 ± 3.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.38 / 63.51 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.69 ± 0.53 / 19.03 ± 0.41</td> <!-- SweDN -->
   <td class="sv know">27.40 ± 0.76 / 44.17 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">21.08 ± 3.28 / 38.46 ± 2.96</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.4.0</td> <!-- Nordjylland-News version -->
   <td>12.4.0</td> <!-- Danske Talemaader version -->
   <td>12.4.0</td> <!-- Danish Citizen Tests version -->
   <td>12.4.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.4.0</td> <!-- MMLU-no version -->
   <td>12.4.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.4.0</td> <!-- MMLU-sv version -->
   <td>12.4.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,431 ± 1,267 / 1,139 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">2.95</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.66</td> <!-- Swedish rank -->
   <td class="da ner">38.25 ± 3.75 / 28.14 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">39.37 ± 2.09 / 56.57 ± 1.90</td> <!-- Angry Tweets -->
   <td class="da la">29.76 ± 3.24 / 61.80 ± 2.22</td> <!-- ScaLA-da -->
   <td class="da rc">57.02 ± 1.28 / 63.16 ± 0.90</td> <!-- ScandiQA-da -->
   <td class="da summ">67.57 ± 1.27 / 24.15 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">83.45 ± 1.44 / 87.17 ± 1.20</td> <!-- Danske Talemaader -->
   <td class="da know">70.43 ± 2.76 / 79.43 ± 1.95</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.43 ± 1.75 / 33.75 ± 1.91</td> <!-- HellaSwag-da -->
   <td class="no ner">50.47 ± 2.96 / 43.31 ± 2.54</td> <!-- NorNE-nb -->
   <td class="no ner">51.97 ± 3.83 / 42.66 ± 5.03</td> <!-- NorNE-nn -->
   <td class="no sent">48.03 ± 1.71 / 65.89 ± 1.68</td> <!-- NoReC -->
   <td class="no summ">65.48 ± 1.22 / 19.57 ± 1.57</td> <!-- No Sammendrag -->
   <td class="no la">22.65 ± 3.80 / 51.83 ± 5.03</td> <!-- ScaLA-nb -->
   <td class="no la">17.10 ± 4.78 / 49.03 ± 6.45</td> <!-- ScaLA-nn -->
   <td class="no rc">44.72 ± 4.47 / 68.08 ± 4.22</td> <!-- NorQuAD -->
   <td class="no know">25.82 ± 0.84 / 42.08 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">21.35 ± 3.32 / 37.35 ± 3.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.19 ± 2.55 / 37.50 ± 3.62</td> <!-- SUC3 -->
   <td class="sv sent">79.95 ± 0.87 / 81.24 ± 0.64</td> <!-- SweReC -->
   <td class="sv la">32.85 ± 2.28 / 61.74 ± 3.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.52 / 63.58 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.95 ± 0.25 / 20.56 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">25.32 ± 0.99 / 42.09 ± 1.04</td> <!-- MMLU-sv -->
   <td class="sv reason">14.55 ± 2.32 / 31.99 ± 2.16</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da-rank">2.49</td> <!-- Danish rank -->
   <td class="no-rank">3.04</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.54</td> <!-- Swedish rank -->
   <td class="da ner">47.01 ± 2.76 / 36.47 ± 3.27</td> <!-- DANSK -->
   <td class="da sent">50.60 ± 3.33 / 65.49 ± 2.38</td> <!-- Angry Tweets -->
   <td class="da la">13.73 ± 3.33 / 52.15 ± 3.17</td> <!-- ScaLA-da -->
   <td class="da rc">56.35 ± 1.68 / 61.63 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="da summ">66.82 ± 1.02 / 22.26 ± 1.10</td> <!-- Nordjylland-News -->
   <td class="da know">57.53 ± 3.61 / 67.77 ± 2.64</td> <!-- Danske Talemaader -->
   <td class="da know">67.04 ± 2.33 / 78.12 ± 1.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.16 ± 1.56 / 40.90 ± 1.34</td> <!-- HellaSwag-da -->
   <td class="no ner">58.60 ± 4.42 / 52.72 ± 4.93</td> <!-- NorNE-nb -->
   <td class="no ner">63.15 ± 2.29 / 54.03 ± 4.33</td> <!-- NorNE-nn -->
   <td class="no sent">51.85 ± 3.51 / 64.28 ± 2.54</td> <!-- NoReC -->
   <td class="no summ">64.57 ± 0.59 / 17.58 ± 0.98</td> <!-- No Sammendrag -->
   <td class="no la">0.66 ± 1.29 / 33.42 ± 0.80</td> <!-- ScaLA-nb -->
   <td class="no la">0.53 ± 1.05 / 33.42 ± 0.73</td> <!-- ScaLA-nn -->
   <td class="no rc">43.22 ± 2.24 / 68.55 ± 2.42</td> <!-- NorQuAD -->
   <td class="no know">26.09 ± 2.24 / 44.41 ± 1.68</td> <!-- MMLU-no -->
   <td class="no reason">23.43 ± 2.86 / 42.30 ± 2.29</td> <!-- HellaSwag-no -->
   <td class="sv ner">56.21 ± 2.49 / 44.78 ± 4.19</td> <!-- SUC3 -->
   <td class="sv sent">78.30 ± 1.71 / 79.80 ± 2.03</td> <!-- SweReC -->
   <td class="sv la">14.35 ± 5.65 / 48.69 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.08 ± 1.47 / 65.72 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.96 ± 0.40 / 24.14 ± 0.74</td> <!-- SweDN -->
   <td class="sv know">31.74 ± 2.48 / 48.52 ± 1.88</td> <!-- MMLU-sv -->
   <td class="sv reason">30.12 ± 2.07 / 47.58 ± 1.29</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.3.2</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,141 ± 994 / 905 ± 299</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.44</td> <!-- Danish rank -->
   <td class="no-rank">2.97</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.76</td> <!-- Swedish rank -->
   <td class="da ner">36.72 ± 3.33 / 27.73 ± 2.57</td> <!-- DANSK -->
   <td class="da sent">46.48 ± 1.17 / 55.20 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">26.10 ± 3.17 / 59.19 ± 3.94</td> <!-- ScaLA-da -->
   <td class="da rc">58.00 ± 0.91 / 64.11 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">67.23 ± 1.11 / 23.15 ± 1.07</td> <!-- Nordjylland-News -->
   <td class="da know">82.84 ± 0.94 / 87.01 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">75.27 ± 1.67 / 83.44 ± 1.19</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.55 ± 2.72 / 33.99 ± 2.19</td> <!-- HellaSwag-da -->
   <td class="no ner">44.53 ± 2.58 / 36.59 ± 1.71</td> <!-- NorNE-nb -->
   <td class="no ner">47.02 ± 2.08 / 39.99 ± 2.76</td> <!-- NorNE-nn -->
   <td class="no sent">41.84 ± 2.46 / 56.79 ± 2.95</td> <!-- NoReC -->
   <td class="no summ">65.29 ± 1.50 / 19.34 ± 1.91</td> <!-- No Sammendrag -->
   <td class="no la">19.97 ± 3.99 / 47.40 ± 4.84</td> <!-- ScaLA-nb -->
   <td class="no la">15.61 ± 4.20 / 43.40 ± 4.90</td> <!-- ScaLA-nn -->
   <td class="no rc">50.91 ± 4.42 / 73.43 ± 3.55</td> <!-- NorQuAD -->
   <td class="no know">30.85 ± 1.15 / 46.02 ± 0.92</td> <!-- MMLU-no -->
   <td class="no reason">18.61 ± 3.08 / 36.62 ± 2.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">36.45 ± 2.44 / 27.24 ± 2.29</td> <!-- SUC3 -->
   <td class="sv sent">81.12 ± 1.02 / 77.04 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">26.80 ± 2.07 / 59.15 ± 2.72</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.16 ± 0.82 / 64.72 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.09 ± 0.31 / 20.48 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">29.01 ± 0.68 / 45.32 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">15.92 ± 1.74 / 35.28 ± 1.24</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   <td>12.10.5</td> <!-- NorNE-nb version -->
   <td>12.10.5</td> <!-- NorNE-nn version -->
   <td>12.10.5</td> <!-- NoReC version -->
   <td>12.10.5</td> <!-- No Sammendrag version -->
   <td>12.10.5</td> <!-- ScaLA-nb version -->
   <td>12.10.5</td> <!-- ScaLA-nn version -->
   <td>12.10.5</td> <!-- NorQuAD version -->
   <td>12.10.5</td> <!-- MMLU-no version -->
   <td>12.10.5</td> <!-- HellaSwag-no version -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.46</td> <!-- Danish rank -->
   <td class="no-rank">2.94</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.75</td> <!-- Swedish rank -->
   <td class="da ner">46.70 ± 3.49 / 36.30 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 3.90 / 55.98 ± 4.69</td> <!-- Angry Tweets -->
   <td class="da la">8.04 ± 5.32 / 36.02 ± 2.59</td> <!-- ScaLA-da -->
   <td class="da rc">60.05 ± 1.30 / 64.15 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">67.18 ± 1.23 / 22.71 ± 1.10</td> <!-- Nordjylland-News -->
   <td class="da know">70.49 ± 3.13 / 77.89 ± 2.32</td> <!-- Danske Talemaader -->
   <td class="da know">66.28 ± 4.60 / 76.88 ± 3.34</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.13 ± 3.45 / 43.24 ± 2.58</td> <!-- HellaSwag-da -->
   <td class="no ner">51.82 ± 4.16 / 44.64 ± 4.66</td> <!-- NorNE-nb -->
   <td class="no ner">62.55 ± 3.84 / 49.66 ± 5.87</td> <!-- NorNE-nn -->
   <td class="no sent">56.37 ± 4.27 / 69.55 ± 4.52</td> <!-- NoReC -->
   <td class="no summ">63.74 ± 1.20 / 16.64 ± 1.53</td> <!-- No Sammendrag -->
   <td class="no la">6.04 ± 5.92 / 36.34 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">-0.02 ± 0.04 / 33.47 ± 0.88</td> <!-- ScaLA-nn -->
   <td class="no rc">48.85 ± 4.11 / 70.75 ± 3.73</td> <!-- NorQuAD -->
   <td class="no know">28.43 ± 2.75 / 45.94 ± 2.14</td> <!-- MMLU-no -->
   <td class="no reason">20.49 ± 3.69 / 40.00 ± 2.80</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.34 ± 3.07 / 39.14 ± 4.60</td> <!-- SUC3 -->
   <td class="sv sent">77.66 ± 2.09 / 78.59 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.00 ± 4.15 / 36.34 ± 2.20</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.81 / 64.12 ± 1.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.54 ± 0.49 / 19.31 ± 0.71</td> <!-- SweDN -->
   <td class="sv know">31.83 ± 2.27 / 48.55 ± 1.67</td> <!-- MMLU-sv -->
   <td class="sv reason">20.55 ± 3.93 / 38.95 ± 3.23</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.1</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.1</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.1</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da-rank">2.56</td> <!-- Danish rank -->
   <td class="no-rank">3.00</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.61</td> <!-- Swedish rank -->
   <td class="da ner">45.39 ± 2.46 / 34.45 ± 2.56</td> <!-- DANSK -->
   <td class="da sent">51.95 ± 2.65 / 65.69 ± 2.11</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 6.27 / 45.66 ± 5.58</td> <!-- ScaLA-da -->
   <td class="da rc">58.51 ± 1.35 / 62.73 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="da summ">66.33 ± 1.33 / 21.24 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">57.16 ± 3.03 / 66.99 ± 2.44</td> <!-- Danske Talemaader -->
   <td class="da know">60.06 ± 3.26 / 71.17 ± 2.36</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.62 ± 3.14 / 33.40 ± 2.67</td> <!-- HellaSwag-da -->
   <td class="no ner">47.61 ± 2.50 / 42.16 ± 2.82</td> <!-- NorNE-nb -->
   <td class="no ner">60.57 ± 2.02 / 48.89 ± 4.48</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 4.10 / 52.31 ± 4.53</td> <!-- NoReC -->
   <td class="no summ">64.59 ± 0.86 / 17.61 ± 1.09</td> <!-- No Sammendrag -->
   <td class="no la">23.99 ± 5.54 / 60.60 ± 2.74</td> <!-- ScaLA-nb -->
   <td class="no la">11.60 ± 3.18 / 53.40 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no rc">47.02 ± 3.37 / 69.07 ± 2.64</td> <!-- NorQuAD -->
   <td class="no know">27.13 ± 1.80 / 42.23 ± 1.12</td> <!-- MMLU-no -->
   <td class="no reason">15.65 ± 2.90 / 31.76 ± 2.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.36 ± 3.07 / 34.48 ± 5.22</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 2.19 / 78.11 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">20.94 ± 5.55 / 44.72 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.07 ± 1.90 / 63.87 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.59 ± 0.50 / 22.19 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">31.44 ± 1.94 / 47.30 ± 1.54</td> <!-- MMLU-sv -->
   <td class="sv reason">26.04 ± 3.42 / 38.83 ± 4.24</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da-rank">2.58</td> <!-- Danish rank -->
   <td class="no-rank">2.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.69</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Llama-3-8B-flashback-v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,807 ± 1,152 / 979 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="da-rank">2.71</td> <!-- Danish rank -->
   <td class="no-rank">3.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.43</td> <!-- Swedish rank -->
   <td class="da ner">46.59 ± 4.16 / 31.16 ± 3.95</td> <!-- DANSK -->
   <td class="da sent">50.25 ± 1.25 / 66.18 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">14.46 ± 2.48 / 50.96 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da rc">56.86 ± 1.23 / 62.50 ± 0.92</td> <!-- ScandiQA-da -->
   <td class="da summ">61.98 ± 1.03 / 15.41 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">46.91 ± 1.59 / 59.57 ± 1.13</td> <!-- Danske Talemaader -->
   <td class="da know">50.98 ± 1.94 / 66.25 ± 1.43</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.33 ± 2.72 / 35.98 ± 2.43</td> <!-- HellaSwag-da -->
   <td class="no ner">59.09 ± 1.89 / 52.82 ± 2.60</td> <!-- NorNE-nb -->
   <td class="no ner">60.02 ± 1.44 / 52.04 ± 2.63</td> <!-- NorNE-nn -->
   <td class="no sent">47.58 ± 1.91 / 64.35 ± 1.95</td> <!-- NoReC -->
   <td class="no summ">58.88 ± 1.42 / 10.65 ± 1.13</td> <!-- No Sammendrag -->
   <td class="no la">10.52 ± 4.67 / 46.13 ± 6.95</td> <!-- ScaLA-nb -->
   <td class="no la">6.67 ± 4.53 / 40.61 ± 5.40</td> <!-- ScaLA-nn -->
   <td class="no rc">49.89 ± 4.89 / 71.90 ± 4.09</td> <!-- NorQuAD -->
   <td class="no know">29.17 ± 1.09 / 46.02 ± 0.72</td> <!-- MMLU-no -->
   <td class="no reason">17.46 ± 1.74 / 36.36 ± 1.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.03 ± 2.04 / 41.99 ± 4.35</td> <!-- SUC3 -->
   <td class="sv sent">81.13 ± 0.94 / 80.80 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">33.06 ± 3.65 / 61.21 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.21 ± 0.67 / 64.01 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.69 / 18.01 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">35.24 ± 0.83 / 50.70 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">25.14 ± 2.02 / 42.54 ± 1.99</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.63</td> <!-- Swedish rank -->
   <td class="da ner">46.03 ± 3.93 / 34.23 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">49.59 ± 3.26 / 63.45 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">12.72 ± 3.51 / 46.56 ± 5.33</td> <!-- ScaLA-da -->
   <td class="da rc">57.03 ± 1.13 / 61.58 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="da summ">65.24 ± 1.45 / 19.37 ± 1.48</td> <!-- Nordjylland-News -->
   <td class="da know">59.88 ± 2.64 / 69.41 ± 2.10</td> <!-- Danske Talemaader -->
   <td class="da know">59.51 ± 3.33 / 71.02 ± 2.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.86 ± 4.05 / 34.77 ± 3.07</td> <!-- HellaSwag-da -->
   <td class="no ner">47.26 ± 3.76 / 40.22 ± 3.43</td> <!-- NorNE-nb -->
   <td class="no ner">59.35 ± 2.82 / 45.26 ± 3.91</td> <!-- NorNE-nn -->
   <td class="no sent">54.93 ± 3.49 / 68.45 ± 2.61</td> <!-- NoReC -->
   <td class="no summ">64.25 ± 0.86 / 16.92 ± 1.27</td> <!-- No Sammendrag -->
   <td class="no la">9.00 ± 2.87 / 37.53 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">5.26 ± 3.15 / 39.01 ± 3.54</td> <!-- ScaLA-nn -->
   <td class="no rc">45.95 ± 3.12 / 68.00 ± 3.07</td> <!-- NorQuAD -->
   <td class="no know">21.89 ± 2.60 / 39.61 ± 2.11</td> <!-- MMLU-no -->
   <td class="no reason">15.32 ± 3.65 / 34.57 ± 2.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.12 ± 2.72 / 30.73 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">78.74 ± 2.13 / 80.11 ± 2.64</td> <!-- SweReC -->
   <td class="sv la">19.74 ± 6.09 / 46.97 ± 5.83</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.15 ± 1.71 / 65.22 ± 1.28</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.41 ± 0.46 / 21.90 ± 0.70</td> <!-- SweDN -->
   <td class="sv know">31.24 ± 3.01 / 47.77 ± 2.19</td> <!-- MMLU-sv -->
   <td class="sv reason">22.30 ± 3.50 / 39.45 ± 2.60</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.42</td> <!-- Danish rank -->
   <td class="no-rank">3.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.80</td> <!-- Swedish rank -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da rc">58.28 ± 0.73 / 64.76 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">67.91 ± 0.79 / 24.44 ± 0.46</td> <!-- Nordjylland-News -->
   <td class="da know">78.71 ± 1.22 / 83.82 ± 0.94</td> <!-- Danske Talemaader -->
   <td class="da know">63.74 ± 2.06 / 74.88 ± 1.46</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.58 ± 0.96 / 45.97 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">51.99 ± 1.85 / 37.40 ± 2.95</td> <!-- NorNE-nb -->
   <td class="no ner">52.74 ± 1.13 / 36.83 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">50.39 ± 1.38 / 66.42 ± 1.20</td> <!-- NoReC -->
   <td class="no summ">64.20 ± 0.44 / 16.28 ± 0.55</td> <!-- No Sammendrag -->
   <td class="no la">0.99 ± 1.03 / 33.56 ± 0.25</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 1.30 / 34.04 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no rc">47.95 ± 3.19 / 72.60 ± 2.57</td> <!-- NorQuAD -->
   <td class="no know">25.74 ± 0.98 / 43.89 ± 0.69</td> <!-- MMLU-no -->
   <td class="no reason">26.36 ± 1.73 / 44.31 ± 1.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.31 ± 0.92 / 63.73 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.23 ± 0.35 / 15.35 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">28.15 ± 0.90 / 45.69 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">23.58 ± 1.41 / 42.30 ± 1.04</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="da-rank">2.46</td> <!-- Danish rank -->
   <td class="no-rank">2.96</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.90</td> <!-- Swedish rank -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da rc">57.96 ± 0.80 / 63.50 ± 0.73</td> <!-- ScandiQA-da -->
   <td class="da summ">65.62 ± 1.30 / 17.98 ± 1.11</td> <!-- Nordjylland-News -->
   <td class="da know">62.80 ± 2.47 / 72.15 ± 1.80</td> <!-- Danske Talemaader -->
   <td class="da know">61.54 ± 2.29 / 73.98 ± 1.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.54 ± 2.80 / 43.01 ± 1.95</td> <!-- HellaSwag-da -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no summ">65.11 ± 0.51 / 18.04 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no rc">40.64 ± 2.58 / 66.46 ± 2.62</td> <!-- NorQuAD -->
   <td class="no know">25.61 ± 2.74 / 44.49 ± 2.07</td> <!-- MMLU-no -->
   <td class="no reason">27.67 ± 4.55 / 44.18 ± 3.63</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.26 ± 1.66 / 64.40 ± 1.35</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.55 ± 0.53 / 23.64 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">23.10 ± 2.38 / 42.58 ± 1.74</td> <!-- MMLU-sv -->
   <td class="sv reason">29.31 ± 5.03 / 47.11 ± 3.62</td> <!-- HellaSwag-sv -->
   <td>9.3.0</td> <!-- DANSK version -->
   <td>9.3.0</td> <!-- Angry Tweets version -->
   <td>9.3.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.0</td> <!-- HellaSwag-da version -->
   <td>9.3.0</td> <!-- NorNE-nb version -->
   <td>9.3.0</td> <!-- NorNE-nn version -->
   <td>9.3.0</td> <!-- NoReC version -->
   <td>9.3.0</td> <!-- No Sammendrag version -->
   <td>9.3.0</td> <!-- ScaLA-nb version -->
   <td>9.3.0</td> <!-- ScaLA-nn version -->
   <td>12.5.2</td> <!-- NorQuAD version -->
   <td>9.3.0</td> <!-- MMLU-no version -->
   <td>9.3.0</td> <!-- HellaSwag-no version -->
   <td>9.3.0</td> <!-- SUC3 version -->
   <td>9.3.0</td> <!-- SweReC version -->
   <td>9.3.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.0</td> <!-- SweDN version -->
   <td>9.3.0</td> <!-- MMLU-sv version -->
   <td>9.3.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="da-rank">2.68</td> <!-- Danish rank -->
   <td class="no-rank">3.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.57</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.60</td> <!-- Danish rank -->
   <td class="no-rank">3.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.73</td> <!-- Swedish rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da rc">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
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
   <td class="no rc">45.23 ± 3.73 / 68.68 ± 3.29</td> <!-- NorQuAD -->
   <td class="no know">28.19 ± 0.84 / 45.83 ± 0.68</td> <!-- MMLU-no -->
   <td class="no reason">13.65 ± 2.51 / 34.00 ± 1.87</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.33 / 19.24 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.52 ± 1.19 / 50.47 ± 0.93</td> <!-- MMLU-sv -->
   <td class="sv reason">20.96 ± 1.96 / 39.95 ± 1.66</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da-rank">2.58</td> <!-- Danish rank -->
   <td class="no-rank">3.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.73</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.57</td> <!-- Danish rank -->
   <td class="no-rank">3.18</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.77</td> <!-- Swedish rank -->
   <td class="da ner">40.14 ± 2.41 / 28.08 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">39.38 ± 1.56 / 49.16 ± 2.84</td> <!-- Angry Tweets -->
   <td class="da la">21.85 ± 3.24 / 53.75 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da rc">58.07 ± 1.13 / 63.63 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">67.06 ± 1.05 / 23.60 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">60.78 ± 1.64 / 69.96 ± 1.28</td> <!-- Danske Talemaader -->
   <td class="da know">61.29 ± 2.78 / 73.50 ± 1.95</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.26 ± 1.96 / 35.70 ± 1.73</td> <!-- HellaSwag-da -->
   <td class="no ner">50.10 ± 2.16 / 41.80 ± 2.77</td> <!-- NorNE-nb -->
   <td class="no ner">54.81 ± 1.88 / 45.95 ± 3.21</td> <!-- NorNE-nn -->
   <td class="no sent">48.64 ± 2.14 / 66.06 ± 1.47</td> <!-- NoReC -->
   <td class="no summ">62.29 ± 1.37 / 14.65 ± 1.36</td> <!-- No Sammendrag -->
   <td class="no la">10.31 ± 3.46 / 43.68 ± 5.10</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.48 / 36.52 ± 2.31</td> <!-- ScaLA-nn -->
   <td class="no rc">42.20 ± 3.02 / 65.18 ± 2.86</td> <!-- NorQuAD -->
   <td class="no know">27.39 ± 0.85 / 45.60 ± 0.64</td> <!-- MMLU-no -->
   <td class="no reason">11.76 ± 2.46 / 32.87 ± 2.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.43 ± 2.75 / 35.31 ± 2.80</td> <!-- SUC3 -->
   <td class="sv sent">79.43 ± 0.85 / 78.21 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">17.37 ± 2.57 / 52.91 ± 4.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.05 ± 1.22 / 62.72 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.81 ± 0.34 / 18.13 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">31.72 ± 0.55 / 48.70 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">15.69 ± 2.43 / 35.96 ± 2.03</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.70</td> <!-- Danish rank -->
   <td class="no-rank">3.03</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.78</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.74</td> <!-- Swedish rank -->
   <td class="da ner">44.90 ± 3.15 / 31.91 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">42.61 ± 1.79 / 53.47 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 3.44 / 38.18 ± 4.21</td> <!-- ScaLA-da -->
   <td class="da rc">59.62 ± 1.12 / 64.70 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">66.48 ± 0.99 / 22.13 ± 1.09</td> <!-- Nordjylland-News -->
   <td class="da know">52.83 ± 1.98 / 64.27 ± 1.66</td> <!-- Danske Talemaader -->
   <td class="da know">57.96 ± 2.76 / 71.31 ± 1.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.11 ± 3.15 / 37.65 ± 2.44</td> <!-- HellaSwag-da -->
   <td class="no ner">52.52 ± 1.85 / 43.46 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.60 ± 3.22 / 45.25 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">48.23 ± 3.31 / 65.51 ± 3.01</td> <!-- NoReC -->
   <td class="no summ">63.53 ± 1.47 / 16.54 ± 1.59</td> <!-- No Sammendrag -->
   <td class="no la">8.53 ± 3.72 / 38.61 ± 3.22</td> <!-- ScaLA-nb -->
   <td class="no la">6.65 ± 1.40 / 39.32 ± 2.51</td> <!-- ScaLA-nn -->
   <td class="no rc">46.89 ± 3.29 / 70.96 ± 2.84</td> <!-- NorQuAD -->
   <td class="no know">27.67 ± 0.91 / 45.77 ± 0.66</td> <!-- MMLU-no -->
   <td class="no reason">14.20 ± 3.45 / 34.89 ± 2.57</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.00 ± 2.53 / 39.09 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">79.70 ± 0.65 / 79.45 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">4.32 ± 2.19 / 34.43 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.03 ± 1.03 / 64.74 ± 0.84</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.89 ± 0.28 / 19.31 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">35.48 ± 0.99 / 51.54 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">20.54 ± 2.14 / 39.66 ± 1.80</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-13B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 645 / 709 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="da-rank">2.72</td> <!-- Danish rank -->
   <td class="no-rank">2.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.85</td> <!-- Swedish rank -->
   <td class="da ner">44.17 ± 3.14 / 31.63 ± 3.03</td> <!-- DANSK -->
   <td class="da sent">44.28 ± 1.94 / 55.59 ± 3.06</td> <!-- Angry Tweets -->
   <td class="da la">3.11 ± 1.88 / 34.35 ± 0.74</td> <!-- ScaLA-da -->
   <td class="da rc">55.59 ± 0.65 / 63.25 ± 0.37</td> <!-- ScandiQA-da -->
   <td class="da summ">66.63 ± 0.92 / 21.44 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">59.51 ± 1.28 / 69.11 ± 1.02</td> <!-- Danske Talemaader -->
   <td class="da know">50.89 ± 1.72 / 67.29 ± 1.12</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.32 ± 1.41 / 43.22 ± 1.13</td> <!-- HellaSwag-da -->
   <td class="no ner">56.72 ± 1.90 / 43.75 ± 2.72</td> <!-- NorNE-nb -->
   <td class="no ner">57.62 ± 1.35 / 43.81 ± 2.43</td> <!-- NorNE-nn -->
   <td class="no sent">48.86 ± 2.54 / 64.32 ± 2.46</td> <!-- NoReC -->
   <td class="no summ">64.86 ± 0.32 / 16.84 ± 0.69</td> <!-- No Sammendrag -->
   <td class="no la">9.87 ± 1.78 / 44.29 ± 3.62</td> <!-- ScaLA-nb -->
   <td class="no la">6.90 ± 1.65 / 48.96 ± 3.09</td> <!-- ScaLA-nn -->
   <td class="no rc">41.27 ± 3.42 / 69.36 ± 3.54</td> <!-- NorQuAD -->
   <td class="no know">24.51 ± 1.23 / 42.96 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">31.41 ± 1.81 / 47.68 ± 1.36</td> <!-- HellaSwag-no -->
   <td class="sv ner">49.26 ± 2.31 / 36.92 ± 4.05</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 0.80 / 77.87 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">0.22 ± 0.43 / 33.38 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.78 ± 1.02 / 63.61 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.99 ± 0.07 / 19.57 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">25.56 ± 0.86 / 43.67 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">28.26 ± 1.97 / 45.89 ± 1.42</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="da-rank">2.69</td> <!-- Danish rank -->
   <td class="no-rank">3.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.73</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="da-rank">2.47</td> <!-- Danish rank -->
   <td class="no-rank">3.34</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.81</td> <!-- Swedish rank -->
   <td class="da ner">40.60 ± 2.25 / 28.71 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">36.89 ± 2.27 / 43.77 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">26.41 ± 5.40 / 53.03 ± 6.56</td> <!-- ScaLA-da -->
   <td class="da rc">57.81 ± 1.11 / 63.44 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">67.27 ± 1.15 / 23.82 ± 0.97</td> <!-- Nordjylland-News -->
   <td class="da know">77.63 ± 1.33 / 83.01 ± 1.00</td> <!-- Danske Talemaader -->
   <td class="da know">67.83 ± 1.25 / 77.91 ± 0.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.16 ± 2.44 / 42.68 ± 2.10</td> <!-- HellaSwag-da -->
   <td class="no ner">48.89 ± 3.42 / 35.46 ± 2.58</td> <!-- NorNE-nb -->
   <td class="no ner">51.95 ± 1.59 / 36.45 ± 2.57</td> <!-- NorNE-nn -->
   <td class="no sent">20.54 ± 6.01 / 36.30 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">63.67 ± 1.16 / 15.98 ± 1.26</td> <!-- No Sammendrag -->
   <td class="no la">4.39 ± 3.94 / 35.23 ± 2.81</td> <!-- ScaLA-nb -->
   <td class="no la">1.20 ± 1.64 / 34.54 ± 1.31</td> <!-- ScaLA-nn -->
   <td class="no rc">47.16 ± 4.15 / 70.08 ± 3.96</td> <!-- NorQuAD -->
   <td class="no know">29.07 ± 1.15 / 46.18 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">19.15 ± 4.16 / 38.37 ± 3.10</td> <!-- HellaSwag-no -->
   <td class="sv ner">42.23 ± 2.44 / 30.30 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">78.80 ± 0.93 / 75.28 ± 1.78</td> <!-- SweReC -->
   <td class="sv la">15.47 ± 1.79 / 54.26 ± 3.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.75 ± 1.15 / 62.43 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.78 ± 0.76 / 16.74 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">30.86 ± 1.12 / 47.83 ± 0.93</td> <!-- MMLU-sv -->
   <td class="sv reason">19.11 ± 2.74 / 38.55 ± 2.29</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.4.0</td> <!-- Danske Talemaader version -->
   <td>12.4.0</td> <!-- Danish Citizen Tests version -->
   <td>12.4.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.4.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.4.0</td> <!-- ScaLA-nb version -->
   <td>12.4.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.4.0</td> <!-- MMLU-no version -->
   <td>12.4.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.4.0</td> <!-- MMLU-sv version -->
   <td>12.4.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="da-rank">2.66</td> <!-- Danish rank -->
   <td class="no-rank">3.15</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.79</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="da-rank">2.70</td> <!-- Danish rank -->
   <td class="no-rank">3.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.81</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="da-rank">2.70</td> <!-- Danish rank -->
   <td class="no-rank">3.14</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.92</td> <!-- Swedish rank -->
   <td class="da ner">43.17 ± 2.78 / 31.37 ± 2.95</td> <!-- DANSK -->
   <td class="da sent">43.40 ± 2.20 / 57.24 ± 3.52</td> <!-- Angry Tweets -->
   <td class="da la">11.08 ± 2.98 / 43.40 ± 4.66</td> <!-- ScaLA-da -->
   <td class="da rc">56.81 ± 0.70 / 63.10 ± 0.35</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 0.28 / 22.85 ± 0.60</td> <!-- Nordjylland-News -->
   <td class="da know">52.94 ± 1.40 / 64.04 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">41.65 ± 1.43 / 59.92 ± 0.88</td> <!-- Danish Citizen Tests -->
   <td class="da reason">17.57 ± 1.83 / 37.68 ± 1.55</td> <!-- HellaSwag-da -->
   <td class="no ner">58.61 ± 1.58 / 47.74 ± 2.83</td> <!-- NorNE-nb -->
   <td class="no ner">60.40 ± 1.25 / 47.53 ± 2.68</td> <!-- NorNE-nn -->
   <td class="no sent">41.36 ± 3.50 / 58.47 ± 3.79</td> <!-- NoReC -->
   <td class="no summ">65.33 ± 0.44 / 18.70 ± 0.55</td> <!-- No Sammendrag -->
   <td class="no la">6.52 ± 2.11 / 38.10 ± 2.56</td> <!-- ScaLA-nb -->
   <td class="no la">3.95 ± 2.52 / 42.37 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no rc">38.93 ± 2.43 / 65.76 ± 3.07</td> <!-- NorQuAD -->
   <td class="no know">23.32 ± 0.89 / 42.01 ± 0.76</td> <!-- MMLU-no -->
   <td class="no reason">22.30 ± 1.43 / 41.29 ± 1.19</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.85 ± 2.44 / 39.65 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">74.17 ± 2.12 / 76.62 ± 1.83</td> <!-- SweReC -->
   <td class="sv la">7.51 ± 1.94 / 37.81 ± 1.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.32 ± 0.63 / 63.28 ± 0.71</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.20 ± 0.45 / 19.06 ± 0.15</td> <!-- SweDN -->
   <td class="sv know">23.92 ± 0.88 / 42.25 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">17.67 ± 1.53 / 37.32 ± 1.20</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="da-rank">2.67</td> <!-- Danish rank -->
   <td class="no-rank">3.22</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.87</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="da-rank">2.83</td> <!-- Danish rank -->
   <td class="no-rank">3.24</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.72</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da-rank">2.75</td> <!-- Danish rank -->
   <td class="no-rank">3.22</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.90</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="da-rank">2.88</td> <!-- Danish rank -->
   <td class="no-rank">3.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.08</td> <!-- Swedish rank -->
   <td class="da ner">41.63 ± 2.33 / 28.51 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.52 / 60.64 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">54.25 ± 0.85 / 61.70 ± 0.71</td> <!-- ScandiQA-da -->
   <td class="da summ">66.02 ± 0.52 / 19.78 ± 0.57</td> <!-- Nordjylland-News -->
   <td class="da know">47.16 ± 1.82 / 59.60 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">38.28 ± 1.21 / 58.13 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.27 ± 1.19 / 41.07 ± 1.07</td> <!-- HellaSwag-da -->
   <td class="no ner">56.18 ± 3.05 / 49.39 ± 2.78</td> <!-- NorNE-nb -->
   <td class="no ner">56.96 ± 1.64 / 48.30 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">50.94 ± 1.41 / 66.55 ± 1.06</td> <!-- NoReC -->
   <td class="no summ">64.21 ± 0.23 / 15.54 ± 0.49</td> <!-- No Sammendrag -->
   <td class="no la">8.19 ± 1.95 / 45.17 ± 3.69</td> <!-- ScaLA-nb -->
   <td class="no la">5.55 ± 1.71 / 48.92 ± 2.94</td> <!-- ScaLA-nn -->
   <td class="no rc">41.35 ± 2.33 / 69.72 ± 2.52</td> <!-- NorQuAD -->
   <td class="no know">21.27 ± 1.03 / 40.69 ± 0.82</td> <!-- MMLU-no -->
   <td class="no reason">26.81 ± 1.72 / 44.27 ± 1.46</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.95 ± 1.89 / 42.16 ± 4.59</td> <!-- SUC3 -->
   <td class="sv sent">60.91 ± 2.35 / 59.47 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">0.32 ± 0.62 / 33.39 ± 0.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.28 ± 0.62 / 63.41 ± 0.55</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.73 ± 0.18 / 15.64 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">20.96 ± 0.77 / 40.70 ± 0.59</td> <!-- MMLU-sv -->
   <td class="sv reason">25.76 ± 1.39 / 43.71 ± 1.09</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="da-rank">2.86</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.93</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="da-rank">2.83</td> <!-- Danish rank -->
   <td class="no-rank">3.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.88</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da-rank">2.74</td> <!-- Danish rank -->
   <td class="no-rank">3.41</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.01</td> <!-- Swedish rank -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da rc">52.78 ± 1.15 / 60.80 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="da summ">65.65 ± 0.82 / 18.78 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">41.77 ± 1.71 / 55.65 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">35.86 ± 2.28 / 52.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.59 ± 1.75 / 32.81 ± 1.55</td> <!-- HellaSwag-da -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no summ">62.13 ± 0.30 / 12.18 ± 0.45</td> <!-- No Sammendrag -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no rc">32.75 ± 1.68 / 59.21 ± 2.11</td> <!-- NorQuAD -->
   <td class="no know">17.08 ± 1.29 / 37.00 ± 1.04</td> <!-- MMLU-no -->
   <td class="no reason">10.52 ± 2.25 / 31.85 ± 1.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.22 ± 0.88 / 61.85 ± 0.63</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.90 ± 0.14 / 16.99 ± 0.20</td> <!-- SweDN -->
   <td class="sv know">22.36 ± 1.17 / 41.14 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">12.52 ± 1.41 / 33.90 ± 1.11</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- MMLU-no version -->
   <td>9.2.0</td> <!-- HellaSwag-no version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="da-rank">2.87</td> <!-- Danish rank -->
   <td class="no-rank">3.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.01</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="da-rank">2.94</td> <!-- Danish rank -->
   <td class="no-rank">3.35</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.95</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="da-rank">2.96</td> <!-- Danish rank -->
   <td class="no-rank">3.38</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.92</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="da-rank">2.93</td> <!-- Danish rank -->
   <td class="no-rank">3.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.15</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da-rank">3.06</td> <!-- Danish rank -->
   <td class="no-rank">3.39</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.18</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da-rank">3.08</td> <!-- Danish rank -->
   <td class="no-rank">3.41</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.13</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da-rank">3.00</td> <!-- Danish rank -->
   <td class="no-rank">3.76</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.86</td> <!-- Swedish rank -->
   <td class="da ner">37.02 ± 5.66 / 27.64 ± 3.92</td> <!-- DANSK -->
   <td class="da sent">40.65 ± 2.10 / 57.47 ± 2.56</td> <!-- Angry Tweets -->
   <td class="da la">7.48 ± 2.51 / 46.56 ± 4.52</td> <!-- ScaLA-da -->
   <td class="da rc">52.71 ± 0.70 / 59.07 ± 0.65</td> <!-- ScandiQA-da -->
   <td class="da summ">64.46 ± 0.75 / 14.29 ± 0.40</td> <!-- Nordjylland-News -->
   <td class="da know">47.26 ± 2.07 / 60.38 ± 1.55</td> <!-- Danske Talemaader -->
   <td class="da know">49.54 ± 1.64 / 66.15 ± 1.06</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.02 ± 1.22 / 30.79 ± 0.64</td> <!-- HellaSwag-da -->
   <td class="no ner">50.34 ± 3.17 / 45.09 ± 2.65</td> <!-- NorNE-nb -->
   <td class="no ner">52.06 ± 2.41 / 46.88 ± 2.39</td> <!-- NorNE-nn -->
   <td class="no sent">32.19 ± 2.52 / 43.19 ± 4.63</td> <!-- NoReC -->
   <td class="no summ">58.71 ± 4.08 / 11.81 ± 0.96</td> <!-- No Sammendrag -->
   <td class="no la">-0.22 ± 0.43 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 33.86 ± 0.33</td> <!-- ScaLA-nn -->
   <td class="no rc">20.57 ± 0.64 / 40.19 ± 1.13</td> <!-- NorQuAD -->
   <td class="no know">22.27 ± 1.22 / 41.36 ± 0.93</td> <!-- MMLU-no -->
   <td class="no reason">11.71 ± 1.56 / 32.80 ± 1.22</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.74 ± 4.30 / 33.57 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">77.06 ± 1.82 / 79.02 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">14.00 ± 1.59 / 53.89 ± 3.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.74 ± 0.52 / 63.45 ± 0.49</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.56 ± 0.85 / 15.85 ± 0.34</td> <!-- SweDN -->
   <td class="sv know">30.87 ± 1.35 / 47.77 ± 1.01</td> <!-- MMLU-sv -->
   <td class="sv reason">15.79 ± 1.57 / 35.66 ± 0.84</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="da-rank">3.28</td> <!-- Danish rank -->
   <td class="no-rank">3.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">2.95</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="da-rank">3.02</td> <!-- Danish rank -->
   <td class="no-rank">3.25</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.38</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="da-rank">3.01</td> <!-- Danish rank -->
   <td class="no-rank">3.47</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.18</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Phi-3-mini-4k-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,360 ± 179 / 566 ± 190</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="da-rank">2.96</td> <!-- Danish rank -->
   <td class="no-rank">3.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.23</td> <!-- Swedish rank -->
   <td class="da ner">39.96 ± 3.11 / 25.49 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">44.93 ± 1.13 / 62.99 ± 0.87</td> <!-- Angry Tweets -->
   <td class="da la">4.01 ± 1.10 / 45.80 ± 2.61</td> <!-- ScaLA-da -->
   <td class="da rc">55.01 ± 0.80 / 60.67 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="da summ">65.29 ± 0.58 / 20.29 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">35.28 ± 1.37 / 51.43 ± 1.04</td> <!-- Danske Talemaader -->
   <td class="da know">41.62 ± 2.04 / 60.84 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.81 ± 1.05 / 33.65 ± 0.84</td> <!-- HellaSwag-da -->
   <td class="no ner">56.41 ± 2.05 / 37.55 ± 3.57</td> <!-- NorNE-nb -->
   <td class="no ner">53.95 ± 1.23 / 38.44 ± 4.85</td> <!-- NorNE-nn -->
   <td class="no sent">42.27 ± 1.52 / 56.76 ± 2.10</td> <!-- NoReC -->
   <td class="no summ">60.58 ± 0.98 / 12.77 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.21 ± 1.00 / 34.08 ± 0.56</td> <!-- ScaLA-nn -->
   <td class="no rc">29.35 ± 1.40 / 53.48 ± 2.01</td> <!-- NorQuAD -->
   <td class="no know">18.57 ± 0.90 / 39.13 ± 0.69</td> <!-- MMLU-no -->
   <td class="no reason">13.36 ± 1.66 / 34.70 ± 1.32</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.81 ± 2.60 / 27.94 ± 5.79</td> <!-- SUC3 -->
   <td class="sv sent">68.43 ± 2.12 / 68.82 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">3.63 ± 1.46 / 43.69 ± 4.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.03 ± 0.62 / 58.80 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.14 ± 0.47 / 11.16 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">23.29 ± 1.03 / 42.63 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">12.06 ± 1.23 / 33.77 ± 0.99</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   <td>12.10.4</td> <!-- NorNE-nb version -->
   <td>12.10.4</td> <!-- NorNE-nn version -->
   <td>12.10.4</td> <!-- NoReC version -->
   <td>12.10.4</td> <!-- No Sammendrag version -->
   <td>12.10.4</td> <!-- ScaLA-nb version -->
   <td>12.10.4</td> <!-- ScaLA-nn version -->
   <td>12.10.4</td> <!-- NorQuAD version -->
   <td>12.10.4</td> <!-- MMLU-no version -->
   <td>12.10.4</td> <!-- HellaSwag-no version -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="da-rank">3.12</td> <!-- Danish rank -->
   <td class="no-rank">3.55</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.04</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.52</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.21</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="da-rank">3.14</td> <!-- Danish rank -->
   <td class="no-rank">3.45</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.20</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.27</td> <!-- ScandEval rank -->
   <td class="da-rank">3.01</td> <!-- Danish rank -->
   <td class="no-rank">3.53</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.27</td> <!-- Swedish rank -->
   <td class="da ner">21.47 ± 3.87 / 16.98 ± 3.19</td> <!-- DANSK -->
   <td class="da sent">48.39 ± 0.66 / 64.51 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">12.46 ± 2.22 / 52.33 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">52.51 ± 1.57 / 58.49 ± 1.58</td> <!-- ScandiQA-da -->
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
   <td class="no rc">47.70 ± 5.32 / 68.04 ± 5.37</td> <!-- NorQuAD -->
   <td class="no know">5.83 ± 1.04 / 27.83 ± 1.08</td> <!-- MMLU-no -->
   <td class="no reason">5.39 ± 1.69 / 27.82 ± 1.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.63 / 18.68 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">6.62 ± 0.88 / 27.61 ± 0.74</td> <!-- MMLU-sv -->
   <td class="sv reason">2.66 ± 1.04 / 26.32 ± 0.72</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">3.27</td> <!-- ScandEval rank -->
   <td class="da-rank">3.05</td> <!-- Danish rank -->
   <td class="no-rank">3.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.17</td> <!-- Swedish rank -->
   <td class="da ner">30.16 ± 4.47 / 25.03 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">48.49 ± 2.41 / 63.06 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">5.52 ± 4.66 / 38.81 ± 4.27</td> <!-- ScaLA-da -->
   <td class="da rc">52.44 ± 1.32 / 57.22 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="da summ">64.24 ± 1.42 / 18.43 ± 1.20</td> <!-- Nordjylland-News -->
   <td class="da know">43.57 ± 3.32 / 56.56 ± 2.69</td> <!-- Danske Talemaader -->
   <td class="da know">35.60 ± 4.28 / 50.86 ± 3.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.76 ± 2.77 / 28.91 ± 2.38</td> <!-- HellaSwag-da -->
   <td class="no ner">35.98 ± 3.79 / 27.51 ± 2.13</td> <!-- NorNE-nb -->
   <td class="no ner">47.39 ± 2.31 / 36.42 ± 2.87</td> <!-- NorNE-nn -->
   <td class="no sent">38.98 ± 5.51 / 58.23 ± 4.01</td> <!-- NoReC -->
   <td class="no summ">61.99 ± 0.85 / 14.07 ± 0.75</td> <!-- No Sammendrag -->
   <td class="no la">11.54 ± 5.04 / 49.91 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">5.20 ± 3.47 / 46.19 ± 5.23</td> <!-- ScaLA-nn -->
   <td class="no rc">37.54 ± 3.00 / 56.56 ± 2.96</td> <!-- NorQuAD -->
   <td class="no know">10.40 ± 2.03 / 29.84 ± 1.34</td> <!-- MMLU-no -->
   <td class="no reason">2.52 ± 1.76 / 24.84 ± 1.48</td> <!-- HellaSwag-no -->
   <td class="sv ner">32.37 ± 3.05 / 24.60 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">75.33 ± 2.41 / 77.99 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">12.73 ± 6.32 / 45.51 ± 7.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.05 ± 1.83 / 58.32 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.74 ± 0.74 / 19.59 ± 0.87</td> <!-- SweDN -->
   <td class="sv know">15.60 ± 1.96 / 33.16 ± 1.77</td> <!-- MMLU-sv -->
   <td class="sv reason">9.81 ± 2.55 / 28.12 ± 2.70</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>10.0.1</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.29</td> <!-- ScandEval rank -->
   <td class="da-rank">3.43</td> <!-- Danish rank -->
   <td class="no-rank">3.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.01</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-40b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">39927</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">409 ± 53 / 182 ± 54</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da-rank">3.03</td> <!-- Danish rank -->
   <td class="no-rank">3.67</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.23</td> <!-- Swedish rank -->
   <td class="da ner">26.57 ± 5.22 / 17.35 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">47.81 ± 1.32 / 64.26 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">11.13 ± 2.06 / 51.34 ± 3.02</td> <!-- ScaLA-da -->
   <td class="da rc">53.78 ± 0.70 / 60.13 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">66.21 ± 1.17 / 21.48 ± 1.27</td> <!-- Nordjylland-News -->
   <td class="da know">33.48 ± 3.59 / 46.04 ± 3.05</td> <!-- Danske Talemaader -->
   <td class="da know">29.86 ± 1.89 / 49.82 ± 1.71</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.67 ± 1.87 / 29.53 ± 1.25</td> <!-- HellaSwag-da -->
   <td class="no ner">24.07 ± 5.59 / 19.09 ± 2.55</td> <!-- NorNE-nb -->
   <td class="no ner">26.67 ± 6.24 / 21.18 ± 2.80</td> <!-- NorNE-nn -->
   <td class="no sent">31.05 ± 7.03 / 45.69 ± 8.29</td> <!-- NoReC -->
   <td class="no summ">61.58 ± 2.25 / 15.13 ± 2.44</td> <!-- No Sammendrag -->
   <td class="no la">10.80 ± 1.96 / 52.29 ± 2.55</td> <!-- ScaLA-nb -->
   <td class="no la">8.89 ± 2.52 / 47.62 ± 4.31</td> <!-- ScaLA-nn -->
   <td class="no rc">48.78 ± 3.64 / 71.66 ± 3.34</td> <!-- NorQuAD -->
   <td class="no know">6.67 ± 1.51 / 28.84 ± 1.19</td> <!-- MMLU-no -->
   <td class="no reason">6.25 ± 1.29 / 29.00 ± 1.15</td> <!-- HellaSwag-no -->
   <td class="sv ner">32.00 ± 3.27 / 17.02 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">80.44 ± 0.54 / 77.81 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">10.73 ± 2.53 / 51.37 ± 4.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.80 ± 0.86 / 60.53 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.16 ± 0.50 / 19.50 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">8.35 ± 0.95 / 30.38 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">5.74 ± 1.30 / 28.98 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- Nordjylland-News version -->
   <td>12.9.1</td> <!-- Danske Talemaader version -->
   <td>12.9.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.1</td> <!-- HellaSwag-da version -->
   <td>12.9.0</td> <!-- NorNE-nb version -->
   <td>12.9.0</td> <!-- NorNE-nn version -->
   <td>12.9.0</td> <!-- NoReC version -->
   <td>12.9.1</td> <!-- No Sammendrag version -->
   <td>12.9.0</td> <!-- ScaLA-nb version -->
   <td>12.9.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>12.9.1</td> <!-- MMLU-no version -->
   <td>12.9.1</td> <!-- HellaSwag-no version -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>12.9.1</td> <!-- SweDN version -->
   <td>12.9.1</td> <!-- MMLU-sv version -->
   <td>12.9.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.30</td> <!-- Danish rank -->
   <td class="no-rank">3.51</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.28</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da-rank">3.10</td> <!-- Danish rank -->
   <td class="no-rank">3.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.35</td> <!-- Swedish rank -->
   <td class="da ner">38.39 ± 3.57 / 24.87 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">49.44 ± 1.03 / 66.00 ± 0.88</td> <!-- Angry Tweets -->
   <td class="da la">7.50 ± 2.07 / 47.53 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da rc">51.24 ± 1.09 / 57.72 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="da summ">66.09 ± 1.40 / 22.03 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">3.53 ± 1.44 / 24.18 ± 1.19</td> <!-- Danske Talemaader -->
   <td class="da know">12.86 ± 2.99 / 40.23 ± 2.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.29 ± 1.23 / 25.61 ± 0.84</td> <!-- HellaSwag-da -->
   <td class="no ner">38.82 ± 5.36 / 30.48 ± 1.91</td> <!-- NorNE-nb -->
   <td class="no ner">43.28 ± 3.13 / 33.87 ± 3.30</td> <!-- NorNE-nn -->
   <td class="no sent">38.05 ± 1.85 / 47.06 ± 3.97</td> <!-- NoReC -->
   <td class="no summ">64.04 ± 1.06 / 17.41 ± 1.19</td> <!-- No Sammendrag -->
   <td class="no la">8.45 ± 2.47 / 46.75 ± 3.97</td> <!-- ScaLA-nb -->
   <td class="no la">7.50 ± 1.65 / 48.14 ± 4.65</td> <!-- ScaLA-nn -->
   <td class="no rc">40.47 ± 2.77 / 64.21 ± 2.94</td> <!-- NorQuAD -->
   <td class="no know">2.60 ± 1.14 / 25.13 ± 0.64</td> <!-- MMLU-no -->
   <td class="no reason">3.83 ± 0.86 / 26.37 ± 0.88</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.24 ± 3.36 / 24.94 ± 3.21</td> <!-- SUC3 -->
   <td class="sv sent">77.91 ± 1.42 / 76.08 ± 2.54</td> <!-- SweReC -->
   <td class="sv la">5.55 ± 2.55 / 48.57 ± 3.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.41 ± 0.74 / 57.55 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.11 ± 1.02 / 17.57 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">1.49 ± 1.11 / 25.90 ± 0.71</td> <!-- MMLU-sv -->
   <td class="sv reason">3.97 ± 0.92 / 27.45 ± 0.68</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da-rank">3.27</td> <!-- Danish rank -->
   <td class="no-rank">3.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.26</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da-rank">3.15</td> <!-- Danish rank -->
   <td class="no-rank">3.58</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.37</td> <!-- Swedish rank -->
   <td class="da ner">39.83 ± 2.18 / 25.99 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">47.48 ± 2.00 / 63.93 ± 1.86</td> <!-- Angry Tweets -->
   <td class="da la">4.55 ± 2.34 / 42.91 ± 4.05</td> <!-- ScaLA-da -->
   <td class="da rc">49.23 ± 0.63 / 57.45 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="da summ">66.17 ± 1.09 / 21.29 ± 0.90</td> <!-- Nordjylland-News -->
   <td class="da know">10.83 ± 2.01 / 28.99 ± 1.32</td> <!-- Danske Talemaader -->
   <td class="da know">14.66 ± 2.21 / 41.21 ± 0.84</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.71 ± 0.74 / 26.10 ± 0.82</td> <!-- HellaSwag-da -->
   <td class="no ner">46.49 ± 2.30 / 31.87 ± 1.92</td> <!-- NorNE-nb -->
   <td class="no ner">51.46 ± 2.36 / 35.87 ± 2.14</td> <!-- NorNE-nn -->
   <td class="no sent">37.98 ± 1.72 / 43.91 ± 2.51</td> <!-- NoReC -->
   <td class="no summ">64.52 ± 0.50 / 17.03 ± 1.00</td> <!-- No Sammendrag -->
   <td class="no la">7.86 ± 2.74 / 47.20 ± 2.71</td> <!-- ScaLA-nb -->
   <td class="no la">7.23 ± 1.97 / 46.62 ± 3.92</td> <!-- ScaLA-nn -->
   <td class="no rc">33.31 ± 1.03 / 59.27 ± 1.53</td> <!-- NorQuAD -->
   <td class="no know">5.22 ± 0.78 / 25.35 ± 0.57</td> <!-- MMLU-no -->
   <td class="no reason">9.32 ± 1.67 / 29.64 ± 1.49</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.45 ± 3.13 / 26.49 ± 3.00</td> <!-- SUC3 -->
   <td class="sv sent">63.64 ± 3.74 / 65.08 ± 2.46</td> <!-- SweReC -->
   <td class="sv la">5.80 ± 1.74 / 51.04 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.95 ± 1.00 / 57.09 ± 0.92</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.18 ± 0.57 / 16.32 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">4.88 ± 0.59 / 25.13 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">4.63 ± 1.09 / 27.29 ± 1.02</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="da-rank">3.35</td> <!-- Danish rank -->
   <td class="no-rank">3.64</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.14</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="da-rank">3.21</td> <!-- Danish rank -->
   <td class="no-rank">3.74</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.22</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da-rank">3.34</td> <!-- Danish rank -->
   <td class="no-rank">3.56</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.30</td> <!-- Swedish rank -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.23 ± 3.43 / 41.05 ± 4.38</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da rc">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">64.47 ± 1.21 / 18.39 ± 1.63</td> <!-- Nordjylland-News -->
   <td class="da know">11.04 ± 2.43 / 29.26 ± 1.97</td> <!-- Danske Talemaader -->
   <td class="da know">22.71 ± 2.48 / 46.50 ± 1.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.03 ± 1.08 / 26.49 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.50 ± 1.29 / 42.21 ± 1.39</td> <!-- NoReC -->
   <td class="no summ">63.10 ± 1.12 / 16.05 ± 1.50</td> <!-- No Sammendrag -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no rc">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td class="no know">4.51 ± 1.00 / 27.45 ± 0.78</td> <!-- MMLU-no -->
   <td class="no reason">5.27 ± 1.29 / 28.47 ± 1.11</td> <!-- HellaSwag-no -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">79.20 ± 1.03 / 79.87 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.14 ± 0.46 / 18.76 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">3.15 ± 0.80 / 27.43 ± 0.91</td> <!-- MMLU-sv -->
   <td class="sv reason">2.77 ± 1.26 / 26.43 ± 0.84</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>12.10.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- Nordjylland-News version -->
   <td>12.9.0</td> <!-- Danske Talemaader version -->
   <td>12.9.0</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>12.10.0</td> <!-- NoReC version -->
   <td>9.3.1</td> <!-- No Sammendrag version -->
   <td>9.3.1</td> <!-- ScaLA-nb version -->
   <td>9.3.1</td> <!-- ScaLA-nn version -->
   <td>9.3.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>12.10.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da-rank">3.21</td> <!-- Danish rank -->
   <td class="no-rank">3.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.36</td> <!-- Swedish rank -->
   <td class="da ner">16.72 ± 2.23 / 15.96 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">45.89 ± 2.13 / 63.12 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">11.25 ± 2.33 / 51.88 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da rc">53.17 ± 0.79 / 59.30 ± 0.66</td> <!-- ScandiQA-da -->
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
   <td class="no rc">48.31 ± 4.22 / 69.39 ± 4.10</td> <!-- NorQuAD -->
   <td class="no know">3.28 ± 1.19 / 25.97 ± 1.25</td> <!-- MMLU-no -->
   <td class="no reason">1.87 ± 1.03 / 26.44 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.60 ± 1.09 / 18.36 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">3.83 ± 1.03 / 26.46 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">4.40 ± 1.42 / 28.14 ± 1.05</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da-rank">3.20</td> <!-- Danish rank -->
   <td class="no-rank">3.69</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.30</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-33B@1000B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,080 ± 700 / 331 ± 117</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="da-rank">3.28</td> <!-- Danish rank -->
   <td class="no-rank">3.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.39</td> <!-- Swedish rank -->
   <td class="da ner">34.22 ± 2.47 / 22.52 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">45.05 ± 2.49 / 62.23 ± 1.84</td> <!-- Angry Tweets -->
   <td class="da la">9.40 ± 2.63 / 44.83 ± 4.69</td> <!-- ScaLA-da -->
   <td class="da rc">54.92 ± 1.00 / 60.33 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">62.78 ± 0.97 / 15.36 ± 1.96</td> <!-- Nordjylland-News -->
   <td class="da know">0.43 ± 1.04 / 24.15 ± 0.82</td> <!-- Danske Talemaader -->
   <td class="da know">4.81 ± 3.43 / 36.58 ± 2.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.77 ± 0.76 / 26.00 ± 0.65</td> <!-- HellaSwag-da -->
   <td class="no ner">40.40 ± 2.29 / 30.41 ± 2.07</td> <!-- NorNE-nb -->
   <td class="no ner">44.45 ± 3.61 / 34.06 ± 3.27</td> <!-- NorNE-nn -->
   <td class="no sent">40.79 ± 1.70 / 57.84 ± 2.77</td> <!-- NoReC -->
   <td class="no summ">56.55 ± 1.85 / 9.81 ± 1.29</td> <!-- No Sammendrag -->
   <td class="no la">5.91 ± 2.51 / 47.81 ± 3.76</td> <!-- ScaLA-nb -->
   <td class="no la">2.98 ± 2.86 / 45.49 ± 4.59</td> <!-- ScaLA-nn -->
   <td class="no rc">37.75 ± 3.23 / 59.72 ± 3.03</td> <!-- NorQuAD -->
   <td class="no know">1.16 ± 0.75 / 23.71 ± 0.76</td> <!-- MMLU-no -->
   <td class="no reason">-0.29 ± 1.00 / 24.91 ± 0.66</td> <!-- HellaSwag-no -->
   <td class="sv ner">42.35 ± 1.51 / 28.31 ± 3.87</td> <!-- SUC3 -->
   <td class="sv sent">77.68 ± 1.11 / 78.86 ± 0.93</td> <!-- SweReC -->
   <td class="sv la">8.08 ± 1.69 / 50.52 ± 2.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.57 ± 1.25 / 60.34 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.30 ± 1.94 / 14.29 ± 0.83</td> <!-- SweDN -->
   <td class="sv know">1.73 ± 1.04 / 24.98 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.32 ± 1.25 / 25.53 ± 0.82</td> <!-- HellaSwag-sv -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- Nordjylland-News version -->
   <td>12.9.0</td> <!-- Danske Talemaader version -->
   <td>12.9.0</td> <!-- Danish Citizen Tests version -->
   <td>12.9.0</td> <!-- HellaSwag-da version -->
   <td>12.9.0</td> <!-- NorNE-nb version -->
   <td>12.9.0</td> <!-- NorNE-nn version -->
   <td>12.9.0</td> <!-- NoReC version -->
   <td>12.9.0</td> <!-- No Sammendrag version -->
   <td>12.9.0</td> <!-- ScaLA-nb version -->
   <td>12.9.0</td> <!-- ScaLA-nn version -->
   <td>12.9.0</td> <!-- NorQuAD version -->
   <td>12.9.0</td> <!-- MMLU-no version -->
   <td>12.9.0</td> <!-- HellaSwag-no version -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>12.9.0</td> <!-- SweDN version -->
   <td>12.9.0</td> <!-- MMLU-sv version -->
   <td>12.9.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da-rank">3.13</td> <!-- Danish rank -->
   <td class="no-rank">3.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.74</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da-rank">3.37</td> <!-- Danish rank -->
   <td class="no-rank">3.80</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.35</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.56</td> <!-- Danish rank -->
   <td class="no-rank">3.71</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.38</td> <!-- Swedish rank -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da rc">51.22 ± 0.94 / 57.23 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="da summ">65.15 ± 1.16 / 18.96 ± 1.15</td> <!-- Nordjylland-News -->
   <td class="da know">6.34 ± 2.61 / 28.14 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">18.00 ± 3.09 / 45.08 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.57 ± 0.93 / 28.66 ± 0.66</td> <!-- HellaSwag-da -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no summ">61.61 ± 2.04 / 14.34 ± 1.84</td> <!-- No Sammendrag -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no rc">44.62 ± 3.31 / 67.57 ± 3.03</td> <!-- NorQuAD -->
   <td class="no know">3.03 ± 1.30 / 25.60 ± 0.86</td> <!-- MMLU-no -->
   <td class="no reason">5.57 ± 1.19 / 27.61 ± 0.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.57 ± 0.94 / 56.51 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.41 ± 0.85 / 16.45 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">5.23 ± 1.02 / 28.63 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">5.39 ± 0.81 / 28.86 ± 0.60</td> <!-- HellaSwag-sv -->
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
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="da-rank">3.37</td> <!-- Danish rank -->
   <td class="no-rank">3.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.45</td> <!-- Swedish rank -->
   <td class="da ner">37.80 ± 2.75 / 24.74 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">40.51 ± 1.75 / 55.84 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">3.35 ± 1.84 / 44.60 ± 4.67</td> <!-- ScaLA-da -->
   <td class="da rc">49.08 ± 1.74 / 55.58 ± 1.57</td> <!-- ScandiQA-da -->
   <td class="da summ">65.81 ± 1.29 / 21.55 ± 1.19</td> <!-- Nordjylland-News -->
   <td class="da know">-0.90 ± 1.63 / 23.10 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">3.61 ± 2.89 / 35.10 ± 1.82</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.40 ± 1.28 / 25.12 ± 0.72</td> <!-- HellaSwag-da -->
   <td class="no ner">42.29 ± 4.36 / 31.45 ± 1.88</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 3.44 / 35.99 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">27.05 ± 3.33 / 45.30 ± 3.46</td> <!-- NoReC -->
   <td class="no summ">62.81 ± 1.69 / 17.08 ± 1.49</td> <!-- No Sammendrag -->
   <td class="no la">1.63 ± 2.58 / 38.29 ± 4.05</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 40.92 ± 4.00</td> <!-- ScaLA-nn -->
   <td class="no rc">39.18 ± 2.84 / 61.85 ± 3.07</td> <!-- NorQuAD -->
   <td class="no know">1.50 ± 0.72 / 23.00 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">-0.05 ± 1.05 / 25.00 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.78 ± 5.08 / 26.81 ± 3.42</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 1.23 / 74.78 ± 1.97</td> <!-- SweReC -->
   <td class="sv la">2.53 ± 2.80 / 47.37 ± 2.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.93 ± 0.97 / 55.09 ± 0.85</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.49 ± 2.27 / 16.17 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">1.28 ± 1.28 / 23.12 ± 0.63</td> <!-- MMLU-sv -->
   <td class="sv reason">1.27 ± 0.61 / 25.74 ± 0.70</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="da-rank">3.61</td> <!-- Danish rank -->
   <td class="no-rank">3.85</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.36</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="da-rank">3.61</td> <!-- Danish rank -->
   <td class="no-rank">3.66</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.59</td> <!-- Swedish rank -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da rc">50.51 ± 0.90 / 58.22 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 1.07 / 21.48 ± 1.21</td> <!-- Nordjylland-News -->
   <td class="da know">30.90 ± 3.84 / 43.86 ± 4.18</td> <!-- Danske Talemaader -->
   <td class="da know">16.81 ± 3.84 / 42.03 ± 2.42</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.08 ± 1.35 / 32.13 ± 1.04</td> <!-- HellaSwag-da -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no summ">64.07 ± 0.86 / 17.41 ± 0.90</td> <!-- No Sammendrag -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no rc">42.52 ± 2.05 / 68.98 ± 2.23</td> <!-- NorQuAD -->
   <td class="no know">6.89 ± 1.56 / 27.44 ± 1.06</td> <!-- MMLU-no -->
   <td class="no reason">12.81 ± 0.66 / 32.38 ± 0.61</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 0.54 / 57.90 ± 0.53</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.89 ± 0.15 / 18.79 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">6.16 ± 0.81 / 28.35 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">10.90 ± 0.86 / 32.01 ± 0.54</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   <td>9.2.0</td> <!-- NorNE-nb version -->
   <td>9.2.0</td> <!-- NorNE-nn version -->
   <td>9.2.0</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.2.0</td> <!-- ScaLA-nb version -->
   <td>9.2.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.2.0</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da-rank">3.37</td> <!-- Danish rank -->
   <td class="no-rank">4.06</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.49</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="da-rank">3.46</td> <!-- Danish rank -->
   <td class="no-rank">3.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.49</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="da-rank">3.44</td> <!-- Danish rank -->
   <td class="no-rank">4.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.57</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.70</td> <!-- ScandEval rank -->
   <td class="da-rank">3.69</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.52</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-33b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">501 ± 50 / 238 ± 69</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="da-rank">3.47</td> <!-- Danish rank -->
   <td class="no-rank">4.05</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.60</td> <!-- Swedish rank -->
   <td class="da ner">25.35 ± 3.59 / 17.77 ± 2.25</td> <!-- DANSK -->
   <td class="da sent">44.70 ± 1.80 / 60.56 ± 2.77</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.60 / 34.16 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">52.29 ± 0.96 / 58.32 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">62.23 ± 0.78 / 14.60 ± 1.38</td> <!-- Nordjylland-News -->
   <td class="da know">-1.01 ± 1.58 / 23.28 ± 1.25</td> <!-- Danske Talemaader -->
   <td class="da know">1.33 ± 1.98 / 33.83 ± 1.11</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.19 ± 0.99 / 25.04 ± 0.66</td> <!-- HellaSwag-da -->
   <td class="no ner">31.38 ± 5.44 / 24.32 ± 2.75</td> <!-- NorNE-nb -->
   <td class="no ner">37.84 ± 4.65 / 29.35 ± 4.10</td> <!-- NorNE-nn -->
   <td class="no sent">38.88 ± 4.12 / 54.92 ± 4.66</td> <!-- NoReC -->
   <td class="no summ">55.01 ± 1.93 / 8.21 ± 0.98</td> <!-- No Sammendrag -->
   <td class="no la">3.41 ± 2.16 / 35.53 ± 2.75</td> <!-- ScaLA-nb -->
   <td class="no la">3.11 ± 1.55 / 39.80 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no rc">30.39 ± 2.51 / 51.24 ± 2.87</td> <!-- NorQuAD -->
   <td class="no know">-1.56 ± 0.62 / 21.86 ± 0.67</td> <!-- MMLU-no -->
   <td class="no reason">0.51 ± 1.35 / 25.31 ± 0.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">33.61 ± 6.02 / 22.18 ± 4.32</td> <!-- SUC3 -->
   <td class="sv sent">76.75 ± 1.17 / 74.66 ± 1.20</td> <!-- SweReC -->
   <td class="sv la">1.66 ± 1.36 / 33.60 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.68 ± 1.94 / 56.96 ± 1.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.37 ± 1.71 / 12.78 ± 0.63</td> <!-- SweDN -->
   <td class="sv know">-0.31 ± 0.91 / 25.20 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.04 ± 0.62 / 25.05 ± 0.50</td> <!-- HellaSwag-sv -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.10.0</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.0</td> <!-- Danske Talemaader version -->
   <td>12.10.0</td> <!-- Danish Citizen Tests version -->
   <td>12.10.0</td> <!-- HellaSwag-da version -->
   <td>12.9.1</td> <!-- NorNE-nb version -->
   <td>12.10.0</td> <!-- NorNE-nn version -->
   <td>12.9.1</td> <!-- NoReC version -->
   <td>12.10.0</td> <!-- No Sammendrag version -->
   <td>12.10.0</td> <!-- ScaLA-nb version -->
   <td>12.10.0</td> <!-- ScaLA-nn version -->
   <td>12.10.0</td> <!-- NorQuAD version -->
   <td>12.10.0</td> <!-- MMLU-no version -->
   <td>12.10.0</td> <!-- HellaSwag-no version -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.10.0</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="da-rank">3.53</td> <!-- Danish rank -->
   <td class="no-rank">3.90</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.71</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="da-rank">3.56</td> <!-- Danish rank -->
   <td class="no-rank">4.09</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.49</td> <!-- Swedish rank -->
   <td class="da ner">28.45 ± 1.61 / 22.90 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">39.09 ± 1.15 / 45.25 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.26 / 37.98 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da rc">51.67 ± 2.31 / 57.34 ± 2.60</td> <!-- ScandiQA-da -->
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
   <td class="no rc">30.14 ± 2.44 / 50.96 ± 3.46</td> <!-- NorQuAD -->
   <td class="no know">6.67 ± 0.74 / 28.30 ± 0.55</td> <!-- MMLU-no -->
   <td class="no reason">3.50 ± 1.56 / 26.82 ± 1.38</td> <!-- HellaSwag-no -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.63 ± 1.02 / 13.45 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">8.72 ± 0.93 / 30.92 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">3.19 ± 0.62 / 26.88 ± 0.62</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="da-rank">3.71</td> <!-- Danish rank -->
   <td class="no-rank">3.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.63</td> <!-- Swedish rank -->
   <td class="da ner">14.73 ± 1.84 / 14.44 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">27.14 ± 1.93 / 42.34 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">2.65 ± 1.66 / 40.63 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da rc">46.38 ± 0.61 / 54.18 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="da summ">65.48 ± 0.73 / 19.58 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">0.32 ± 0.71 / 23.38 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">7.00 ± 3.44 / 37.91 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.13 ± 0.25 / 25.04 ± 0.54</td> <!-- HellaSwag-da -->
   <td class="no ner">33.08 ± 2.22 / 34.51 ± 2.24</td> <!-- NorNE-nb -->
   <td class="no ner">38.28 ± 2.63 / 40.50 ± 2.72</td> <!-- NorNE-nn -->
   <td class="no sent">35.58 ± 2.13 / 44.49 ± 2.52</td> <!-- NoReC -->
   <td class="no summ">63.11 ± 0.71 / 15.22 ± 1.02</td> <!-- No Sammendrag -->
   <td class="no la">0.82 ± 1.46 / 34.78 ± 1.54</td> <!-- ScaLA-nb -->
   <td class="no la">1.43 ± 1.70 / 34.19 ± 1.10</td> <!-- ScaLA-nn -->
   <td class="no rc">36.06 ± 1.76 / 58.71 ± 1.63</td> <!-- NorQuAD -->
   <td class="no know">-0.68 ± 1.21 / 24.35 ± 0.73</td> <!-- MMLU-no -->
   <td class="no reason">-0.32 ± 0.44 / 24.50 ± 0.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">19.04 ± 2.67 / 19.98 ± 2.64</td> <!-- SUC3 -->
   <td class="sv sent">73.34 ± 1.34 / 68.41 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.90 ± 1.74 / 44.43 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.45 ± 0.58 / 54.69 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.33 ± 0.86 / 17.11 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">0.65 ± 1.12 / 25.94 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.18 ± 0.36 / 24.70 ± 0.60</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="da-rank">3.48</td> <!-- Danish rank -->
   <td class="no-rank">4.15</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.59</td> <!-- Swedish rank -->
   <td class="da ner">24.93 ± 4.36 / 22.23 ± 3.32</td> <!-- DANSK -->
   <td class="da sent">31.65 ± 2.94 / 51.95 ± 2.92</td> <!-- Angry Tweets -->
   <td class="da la">0.06 ± 1.20 / 34.30 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">51.47 ± 1.82 / 57.00 ± 1.94</td> <!-- ScandiQA-da -->
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
   <td class="no rc">26.28 ± 1.51 / 44.62 ± 2.11</td> <!-- NorQuAD -->
   <td class="no know">8.41 ± 1.26 / 29.77 ± 1.22</td> <!-- MMLU-no -->
   <td class="no reason">2.47 ± 1.34 / 26.33 ± 1.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.86 ± 1.75 / 11.38 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">11.71 ± 0.83 / 32.71 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">0.81 ± 0.88 / 25.27 ± 0.59</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,027 ± 503 / 903 ± 296</td> <!-- Model inference speed -->
   <td class="rank">3.76</td> <!-- ScandEval rank -->
   <td class="da-rank">3.61</td> <!-- Danish rank -->
   <td class="no-rank">4.01</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.67</td> <!-- Swedish rank -->
   <td class="da ner">13.78 ± 2.85 / 11.90 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">42.16 ± 0.68 / 45.21 ± 0.45</td> <!-- Angry Tweets -->
   <td class="da la">3.52 ± 1.90 / 39.81 ± 3.18</td> <!-- ScaLA-da -->
   <td class="da rc">20.02 ± 2.31 / 31.67 ± 2.19</td> <!-- ScandiQA-da -->
   <td class="da summ">65.03 ± 0.55 / 18.00 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">40.74 ± 1.91 / 53.17 ± 1.96</td> <!-- Danske Talemaader -->
   <td class="da know">43.43 ± 1.76 / 61.76 ± 1.32</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.50 ± 0.94 / 26.55 ± 0.96</td> <!-- HellaSwag-da -->
   <td class="no ner">27.49 ± 2.13 / 24.26 ± 1.41</td> <!-- NorNE-nb -->
   <td class="no ner">32.33 ± 2.92 / 29.29 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.12 / 64.33 ± 2.80</td> <!-- NoReC -->
   <td class="no summ">62.75 ± 0.25 / 13.28 ± 0.27</td> <!-- No Sammendrag -->
   <td class="no la">3.92 ± 1.56 / 45.78 ± 2.36</td> <!-- ScaLA-nb -->
   <td class="no la">4.27 ± 2.44 / 42.86 ± 3.51</td> <!-- ScaLA-nn -->
   <td class="no rc">2.46 ± 0.73 / 29.01 ± 1.18</td> <!-- NorQuAD -->
   <td class="no know">8.41 ± 0.77 / 32.09 ± 0.44</td> <!-- MMLU-no -->
   <td class="no reason">2.92 ± 1.61 / 25.82 ± 0.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">20.97 ± 2.51 / 16.21 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 0.75 / 67.99 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.35 ± 1.63 / 38.48 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.65 ± 2.11 / 38.84 ± 1.85</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.75 ± 0.70 / 17.94 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">9.17 ± 0.61 / 31.89 ± 0.41</td> <!-- MMLU-sv -->
   <td class="sv reason">3.98 ± 1.37 / 26.35 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
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
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da-rank">3.38</td> <!-- Danish rank -->
   <td class="no-rank">4.26</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.68</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="da-rank">3.60</td> <!-- Danish rank -->
   <td class="no-rank">4.12</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.63</td> <!-- Swedish rank -->
   <td class="da ner">23.98 ± 3.74 / 17.18 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">38.74 ± 2.15 / 49.48 ± 3.14</td> <!-- Angry Tweets -->
   <td class="da la">1.04 ± 1.57 / 33.67 ± 0.22</td> <!-- ScaLA-da -->
   <td class="da rc">50.17 ± 0.92 / 56.29 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">61.96 ± 0.87 / 13.71 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">-0.06 ± 0.90 / 23.97 ± 0.72</td> <!-- Danske Talemaader -->
   <td class="da know">-1.04 ± 2.16 / 34.90 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.73 ± 0.90 / 25.11 ± 0.51</td> <!-- HellaSwag-da -->
   <td class="no ner">22.37 ± 5.96 / 23.75 ± 3.97</td> <!-- NorNE-nb -->
   <td class="no ner">29.90 ± 4.44 / 26.84 ± 3.45</td> <!-- NorNE-nn -->
   <td class="no sent">35.86 ± 3.52 / 52.28 ± 3.76</td> <!-- NoReC -->
   <td class="no summ">53.25 ± 1.69 / 6.87 ± 0.67</td> <!-- No Sammendrag -->
   <td class="no la">1.03 ± 2.07 / 36.12 ± 2.97</td> <!-- ScaLA-nb -->
   <td class="no la">2.92 ± 1.89 / 36.47 ± 2.72</td> <!-- ScaLA-nn -->
   <td class="no rc">34.39 ± 3.15 / 54.65 ± 3.56</td> <!-- NorQuAD -->
   <td class="no know">-1.16 ± 0.91 / 21.94 ± 0.46</td> <!-- MMLU-no -->
   <td class="no reason">-0.55 ± 1.14 / 25.09 ± 0.85</td> <!-- HellaSwag-no -->
   <td class="sv ner">30.64 ± 4.19 / 23.90 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.02 ± 3.18 / 72.36 ± 3.96</td> <!-- SweReC -->
   <td class="sv la">1.08 ± 1.36 / 38.63 ± 3.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.72 ± 1.05 / 54.59 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.93 ± 2.32 / 13.16 ± 1.05</td> <!-- SweDN -->
   <td class="sv know">1.14 ± 0.79 / 22.39 ± 0.53</td> <!-- MMLU-sv -->
   <td class="sv reason">1.13 ± 1.01 / 25.61 ± 0.65</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da-rank">3.66</td> <!-- Danish rank -->
   <td class="no-rank">3.99</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.76</td> <!-- Swedish rank -->
   <td class="da ner">18.23 ± 5.87 / 14.77 ± 3.36</td> <!-- DANSK -->
   <td class="da sent">22.71 ± 5.21 / 35.11 ± 6.59</td> <!-- Angry Tweets -->
   <td class="da la">5.03 ± 2.51 / 49.00 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">49.11 ± 1.16 / 55.56 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="da summ">64.58 ± 1.03 / 18.26 ± 1.00</td> <!-- Nordjylland-News -->
   <td class="da know">1.11 ± 2.19 / 24.85 ± 1.14</td> <!-- Danske Talemaader -->
   <td class="da know">8.76 ± 3.09 / 37.32 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.70 ± 0.84 / 26.17 ± 0.62</td> <!-- HellaSwag-da -->
   <td class="no ner">22.35 ± 7.84 / 23.89 ± 4.74</td> <!-- NorNE-nb -->
   <td class="no ner">21.98 ± 7.52 / 27.22 ± 4.97</td> <!-- NorNE-nn -->
   <td class="no sent">18.23 ± 9.28 / 38.93 ± 6.44</td> <!-- NoReC -->
   <td class="no summ">60.38 ± 1.78 / 12.50 ± 1.62</td> <!-- No Sammendrag -->
   <td class="no la">1.68 ± 1.35 / 39.93 ± 2.78</td> <!-- ScaLA-nb -->
   <td class="no la">2.49 ± 1.88 / 40.26 ± 3.23</td> <!-- ScaLA-nn -->
   <td class="no rc">41.80 ± 3.14 / 64.25 ± 3.13</td> <!-- NorQuAD -->
   <td class="no know">2.13 ± 0.65 / 26.47 ± 0.86</td> <!-- MMLU-no -->
   <td class="no reason">0.98 ± 1.48 / 25.66 ± 1.09</td> <!-- HellaSwag-no -->
   <td class="sv ner">18.83 ± 6.41 / 17.59 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">53.68 ± 10.39 / 58.92 ± 10.87</td> <!-- SweReC -->
   <td class="sv la">3.49 ± 2.20 / 46.13 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.81 ± 0.70 / 55.99 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.05 ± 1.33 / 15.89 ± 0.85</td> <!-- SweDN -->
   <td class="sv know">1.22 ± 0.65 / 26.19 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">0.60 ± 1.34 / 25.62 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>11.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>11.0.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-13b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,520 ± 736 / 823 ± 273</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da-rank">3.52</td> <!-- Danish rank -->
   <td class="no-rank">4.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.64</td> <!-- Swedish rank -->
   <td class="da ner">28.72 ± 2.61 / 20.53 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">37.19 ± 3.92 / 53.63 ± 4.06</td> <!-- Angry Tweets -->
   <td class="da la">2.96 ± 1.73 / 46.67 ± 3.16</td> <!-- ScaLA-da -->
   <td class="da rc">49.53 ± 1.49 / 54.83 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="da summ">61.62 ± 1.05 / 14.33 ± 1.71</td> <!-- Nordjylland-News -->
   <td class="da know">1.17 ± 2.28 / 24.76 ± 1.52</td> <!-- Danske Talemaader -->
   <td class="da know">11.38 ± 3.80 / 38.52 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.16 ± 1.02 / 25.19 ± 0.70</td> <!-- HellaSwag-da -->
   <td class="no ner">28.94 ± 5.63 / 27.01 ± 4.91</td> <!-- NorNE-nb -->
   <td class="no ner">33.83 ± 5.52 / 30.49 ± 4.07</td> <!-- NorNE-nn -->
   <td class="no sent">27.32 ± 3.13 / 38.30 ± 2.19</td> <!-- NoReC -->
   <td class="no summ">54.05 ± 2.19 / 7.52 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">1.46 ± 1.07 / 49.06 ± 1.04</td> <!-- ScaLA-nb -->
   <td class="no la">-0.59 ± 1.36 / 45.94 ± 2.35</td> <!-- ScaLA-nn -->
   <td class="no rc">25.62 ± 4.99 / 40.88 ± 7.54</td> <!-- NorQuAD -->
   <td class="no know">0.32 ± 0.70 / 24.79 ± 0.56</td> <!-- MMLU-no -->
   <td class="no reason">0.92 ± 1.02 / 25.43 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">32.19 ± 4.64 / 24.93 ± 4.09</td> <!-- SUC3 -->
   <td class="sv sent">72.26 ± 6.90 / 72.58 ± 5.87</td> <!-- SweReC -->
   <td class="sv la">2.39 ± 1.29 / 48.49 ± 2.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.92 ± 2.28 / 53.44 ± 2.49</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.46 ± 1.64 / 13.21 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.50 / 25.03 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.50 ± 1.04 / 25.50 ± 0.72</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="da-rank">3.76</td> <!-- Danish rank -->
   <td class="no-rank">4.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.73</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="da-rank">3.64</td> <!-- Danish rank -->
   <td class="no-rank">3.98</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.13</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="da-rank">3.83</td> <!-- Danish rank -->
   <td class="no-rank">4.17</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.79</td> <!-- Swedish rank -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da rc">45.34 ± 0.88 / 51.59 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">62.17 ± 1.12 / 14.96 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">-1.31 ± 1.31 / 24.58 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">3.02 ± 3.77 / 36.58 ± 2.16</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.33 ± 1.17 / 24.65 ± 0.48</td> <!-- HellaSwag-da -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no summ">58.46 ± 2.59 / 11.38 ± 1.45</td> <!-- No Sammendrag -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no rc">34.91 ± 2.65 / 54.30 ± 2.96</td> <!-- NorQuAD -->
   <td class="no know">-0.01 ± 0.86 / 24.32 ± 0.81</td> <!-- MMLU-no -->
   <td class="no reason">0.25 ± 0.94 / 25.10 ± 0.81</td> <!-- HellaSwag-no -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.55 ± 0.85 / 51.69 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.11 ± 1.59 / 15.02 ± 0.84</td> <!-- SweDN -->
   <td class="sv know">2.20 ± 0.88 / 25.62 ± 0.86</td> <!-- MMLU-sv -->
   <td class="sv reason">0.67 ± 1.39 / 25.25 ± 0.51</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
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
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="da-rank">3.63</td> <!-- Danish rank -->
   <td class="no-rank">4.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.01</td> <!-- Swedish rank -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da rc">41.82 ± 2.07 / 48.91 ± 2.47</td> <!-- ScandiQA-da -->
   <td class="da summ">65.27 ± 0.25 / 17.79 ± 0.40</td> <!-- Nordjylland-News -->
   <td class="da know">6.27 ± 1.52 / 27.63 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">6.25 ± 3.25 / 37.75 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.11 ± 1.44 / 26.00 ± 0.86</td> <!-- HellaSwag-da -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no summ">60.01 ± 0.81 / 9.76 ± 0.87</td> <!-- No Sammendrag -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no rc">19.10 ± 2.33 / 38.96 ± 2.78</td> <!-- NorQuAD -->
   <td class="no know">3.21 ± 0.87 / 27.07 ± 0.74</td> <!-- MMLU-no -->
   <td class="no reason">0.18 ± 1.02 / 25.00 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.57 ± 2.45 / 41.66 ± 2.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.79 ± 0.24 / 10.61 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">0.14 ± 1.02 / 24.76 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.83 / 25.53 ± 0.62</td> <!-- HellaSwag-sv -->
   <td>9.1.2</td> <!-- DANSK version -->
   <td>9.1.2</td> <!-- Angry Tweets version -->
   <td>9.1.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   <td>9.1.2</td> <!-- NorNE-nb version -->
   <td>9.1.2</td> <!-- NorNE-nn version -->
   <td>9.1.2</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>9.1.2</td> <!-- ScaLA-nb version -->
   <td>9.1.2</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>9.1.2</td> <!-- MMLU-no version -->
   <td>9.1.2</td> <!-- HellaSwag-no version -->
   <td>9.1.2</td> <!-- SUC3 version -->
   <td>9.1.2</td> <!-- SweReC version -->
   <td>9.1.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.1.2</td> <!-- MMLU-sv version -->
   <td>9.1.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="da-rank">3.85</td> <!-- Danish rank -->
   <td class="no-rank">4.31</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.73</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.97</td> <!-- ScandEval rank -->
   <td class="da-rank">3.79</td> <!-- Danish rank -->
   <td class="no-rank">4.16</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.97</td> <!-- Swedish rank -->
   <td class="da ner">14.88 ± 3.92 / 14.02 ± 2.63</td> <!-- DANSK -->
   <td class="da sent">34.66 ± 1.82 / 46.40 ± 1.53</td> <!-- Angry Tweets -->
   <td class="da la">0.29 ± 1.86 / 41.01 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da rc">42.16 ± 0.88 / 47.49 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="da summ">63.19 ± 1.17 / 17.04 ± 1.07</td> <!-- Nordjylland-News -->
   <td class="da know">0.58 ± 1.06 / 23.87 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">4.60 ± 3.52 / 37.09 ± 1.52</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.34 ± 1.37 / 24.79 ± 0.73</td> <!-- HellaSwag-da -->
   <td class="no ner">14.58 ± 6.07 / 15.44 ± 5.52</td> <!-- NorNE-nb -->
   <td class="no ner">21.06 ± 7.77 / 21.99 ± 7.14</td> <!-- NorNE-nn -->
   <td class="no sent">32.02 ± 1.59 / 36.85 ± 2.01</td> <!-- NoReC -->
   <td class="no summ">60.36 ± 1.93 / 12.69 ± 1.69</td> <!-- No Sammendrag -->
   <td class="no la">1.49 ± 1.40 / 35.35 ± 1.51</td> <!-- ScaLA-nb -->
   <td class="no la">0.98 ± 1.85 / 35.28 ± 2.43</td> <!-- ScaLA-nn -->
   <td class="no rc">22.87 ± 1.85 / 38.93 ± 2.59</td> <!-- NorQuAD -->
   <td class="no know">0.99 ± 0.62 / 24.00 ± 0.70</td> <!-- MMLU-no -->
   <td class="no reason">-0.16 ± 0.90 / 24.84 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">13.79 ± 8.46 / 14.43 ± 7.23</td> <!-- SUC3 -->
   <td class="sv sent">71.59 ± 2.78 / 59.82 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">-0.89 ± 1.22 / 43.82 ± 3.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.33 ± 1.79 / 44.00 ± 1.70</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.77 ± 0.83 / 14.15 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">-0.39 ± 1.21 / 22.30 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.52 ± 1.01 / 25.20 ± 0.85</td> <!-- HellaSwag-sv -->
   <td>10.0.0</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>10.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.0</td> <!-- NorNE-nb version -->
   <td>10.0.0</td> <!-- NorNE-nn version -->
   <td>10.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>10.0.0</td> <!-- ScaLA-nb version -->
   <td>10.0.0</td> <!-- ScaLA-nn version -->
   <td>10.0.0</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.0</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>10.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.98</td> <!-- ScandEval rank -->
   <td class="da-rank">3.84</td> <!-- Danish rank -->
   <td class="no-rank">4.15</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.96</td> <!-- Swedish rank -->
   <td class="da ner">11.28 ± 0.96 / 11.02 ± 0.85</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 3.80 / 49.66 ± 3.96</td> <!-- Angry Tweets -->
   <td class="da la">2.08 ± 1.48 / 45.41 ± 3.83</td> <!-- ScaLA-da -->
   <td class="da rc">36.59 ± 1.41 / 42.03 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="da summ">63.38 ± 0.84 / 15.95 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">-0.09 ± 1.02 / 23.32 ± 0.76</td> <!-- Danske Talemaader -->
   <td class="da know">-0.76 ± 3.27 / 35.04 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.28 ± 0.39 / 25.19 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">24.38 ± 2.13 / 25.79 ± 2.29</td> <!-- NorNE-nb -->
   <td class="no ner">31.28 ± 1.60 / 33.48 ± 1.60</td> <!-- NorNE-nn -->
   <td class="no sent">30.88 ± 2.75 / 46.07 ± 3.07</td> <!-- NoReC -->
   <td class="no summ">60.73 ± 0.70 / 11.71 ± 0.76</td> <!-- No Sammendrag -->
   <td class="no la">-0.30 ± 1.46 / 34.93 ± 1.25</td> <!-- ScaLA-nb -->
   <td class="no la">0.45 ± 0.57 / 33.74 ± 1.25</td> <!-- ScaLA-nn -->
   <td class="no rc">23.99 ± 1.59 / 42.69 ± 1.94</td> <!-- NorQuAD -->
   <td class="no know">-1.01 ± 1.09 / 21.90 ± 0.67</td> <!-- MMLU-no -->
   <td class="no reason">-0.50 ± 0.67 / 25.00 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.84 ± 1.63 / 15.90 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 3.60 / 54.09 ± 1.46</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.21 / 34.76 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.37 ± 1.36 / 40.44 ± 1.53</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.28 ± 0.92 / 14.60 ± 0.79</td> <!-- SweDN -->
   <td class="sv know">0.48 ± 1.07 / 23.44 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">0.33 ± 0.50 / 25.01 ± 0.76</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>12.1.0</td> <!-- ScaLA-nb version -->
   <td>12.1.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>12.1.0</td> <!-- MMLU-no version -->
   <td>12.1.0</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="da-rank">3.88</td> <!-- Danish rank -->
   <td class="no-rank">4.35</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.79</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">4.02</td> <!-- ScandEval rank -->
   <td class="da-rank">3.75</td> <!-- Danish rank -->
   <td class="no-rank">4.50</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.81</td> <!-- Swedish rank -->
   <td class="da ner">21.98 ± 3.33 / 18.42 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">37.77 ± 3.06 / 55.35 ± 4.51</td> <!-- Angry Tweets -->
   <td class="da la">1.26 ± 1.86 / 34.03 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da rc">46.03 ± 1.44 / 52.54 ± 1.95</td> <!-- ScandiQA-da -->
   <td class="da summ">58.21 ± 1.54 / 11.61 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">-0.87 ± 1.27 / 35.70 ± 1.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.00 ± 0.00 / 25.18 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">20.25 ± 6.26 / 20.45 ± 5.54</td> <!-- NorNE-nb -->
   <td class="no ner">28.99 ± 5.03 / 27.50 ± 4.36</td> <!-- NorNE-nn -->
   <td class="no sent">17.44 ± 3.49 / 35.51 ± 4.10</td> <!-- NoReC -->
   <td class="no summ">49.59 ± 1.68 / 5.67 ± 0.54</td> <!-- No Sammendrag -->
   <td class="no la">3.20 ± 1.84 / 34.58 ± 0.97</td> <!-- ScaLA-nb -->
   <td class="no la">2.61 ± 1.80 / 34.49 ± 1.46</td> <!-- ScaLA-nn -->
   <td class="no rc">21.50 ± 2.60 / 40.73 ± 3.86</td> <!-- NorQuAD -->
   <td class="no know">0.86 ± 0.91 / 21.96 ± 0.54</td> <!-- MMLU-no -->
   <td class="no reason">0.00 ± 0.00 / 25.02 ± 0.87</td> <!-- HellaSwag-no -->
   <td class="sv ner">27.07 ± 6.33 / 25.24 ± 4.89</td> <!-- SUC3 -->
   <td class="sv sent">61.96 ± 2.69 / 67.81 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">2.65 ± 1.46 / 40.25 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.16 ± 0.91 / 52.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.11 ± 1.21 / 12.07 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">0.32 ± 0.43 / 21.99 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.00 ± 0.01 / 25.00 ± 0.77</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   <td>12.5.2</td> <!-- NorNE-nb version -->
   <td>12.5.2</td> <!-- NorNE-nn version -->
   <td>12.3.2</td> <!-- NoReC version -->
   <td>12.3.2</td> <!-- No Sammendrag version -->
   <td>12.3.2</td> <!-- ScaLA-nb version -->
   <td>12.3.2</td> <!-- ScaLA-nn version -->
   <td>12.3.2</td> <!-- NorQuAD version -->
   <td>12.3.2</td> <!-- MMLU-no version -->
   <td>12.3.2</td> <!-- HellaSwag-no version -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.05</td> <!-- ScandEval rank -->
   <td class="da-rank">3.95</td> <!-- Danish rank -->
   <td class="no-rank">4.35</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.84</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="da-rank">3.82</td> <!-- Danish rank -->
   <td class="no-rank">4.19</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.19</td> <!-- Swedish rank -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da rc">38.60 ± 0.65 / 47.40 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">63.32 ± 0.32 / 16.03 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">4.49 ± 1.44 / 27.32 ± 0.89</td> <!-- Danske Talemaader -->
   <td class="da know">12.81 ± 4.57 / 37.83 ± 2.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.68 ± 1.31 / 25.00 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">23.82 ± 4.25 / 22.08 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">26.04 ± 6.38 / 24.47 ± 3.69</td> <!-- NorNE-nn -->
   <td class="no sent">32.60 ± 1.84 / 47.47 ± 3.33</td> <!-- NoReC -->
   <td class="no summ">58.08 ± 0.42 / 11.74 ± 0.50</td> <!-- No Sammendrag -->
   <td class="no la">0.34 ± 1.43 / 44.47 ± 2.44</td> <!-- ScaLA-nb -->
   <td class="no la">2.26 ± 2.27 / 45.41 ± 3.25</td> <!-- ScaLA-nn -->
   <td class="no rc">21.33 ± 0.98 / 42.76 ± 1.02</td> <!-- NorQuAD -->
   <td class="no know">2.13 ± 1.32 / 26.30 ± 1.12</td> <!-- MMLU-no -->
   <td class="no reason">1.87 ± 1.34 / 25.87 ± 0.75</td> <!-- HellaSwag-no -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.23 ± 1.07 / 46.83 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">46.68 ± 0.33 / 12.40 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">-0.03 ± 1.31 / 23.73 ± 1.11</td> <!-- MMLU-sv -->
   <td class="sv reason">0.02 ± 0.88 / 25.04 ± 0.61</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>9.3.2</td> <!-- NorNE-nb version -->
   <td>9.3.2</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">4.15</td> <!-- ScandEval rank -->
   <td class="da-rank">4.00</td> <!-- Danish rank -->
   <td class="no-rank">4.21</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.23</td> <!-- Swedish rank -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da rc">34.79 ± 1.52 / 39.67 ± 1.69</td> <!-- ScandiQA-da -->
   <td class="da summ">59.05 ± 1.42 / 12.41 ± 1.13</td> <!-- Nordjylland-News -->
   <td class="da know">1.00 ± 1.72 / 23.91 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">4.85 ± 3.16 / 36.78 ± 1.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.28 ± 0.38 / 25.19 ± 0.78</td> <!-- HellaSwag-da -->
   <td class="no ner">27.37 ± 4.07 / 27.94 ± 4.04</td> <!-- NorNE-nb -->
   <td class="no ner">31.22 ± 3.87 / 31.39 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">34.21 ± 1.63 / 47.17 ± 2.76</td> <!-- NoReC -->
   <td class="no summ">54.28 ± 2.37 / 8.28 ± 0.99</td> <!-- No Sammendrag -->
   <td class="no la">0.92 ± 1.55 / 40.71 ± 2.58</td> <!-- ScaLA-nb -->
   <td class="no la">1.25 ± 2.30 / 43.49 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no rc">18.52 ± 2.78 / 32.10 ± 4.23</td> <!-- NorQuAD -->
   <td class="no know">0.33 ± 1.29 / 22.37 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">0.11 ± 1.10 / 24.94 ± 0.94</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.70 ± 1.46 / 38.82 ± 1.54</td> <!-- ScandiQA-sv -->
   <td class="sv summ">51.36 ± 2.01 / 10.76 ± 0.54</td> <!-- SweDN -->
   <td class="sv know">-0.96 ± 1.08 / 21.85 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.30 ± 0.48 / 25.10 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>9.3.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>9.3.2</td> <!-- ScaLA-nb version -->
   <td>9.3.2</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.2</td> <!-- MMLU-no version -->
   <td>9.3.2</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="da-rank">3.97</td> <!-- Danish rank -->
   <td class="no-rank">4.65</td> <!-- Norwegian rank -->
   <td class="sv-rank">3.95</td> <!-- Swedish rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da rc">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
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
   <td class="no rc">0.12 ± 0.04 / 9.85 ± 0.17</td> <!-- NorQuAD -->
   <td class="no know">2.61 ± 1.38 / 27.69 ± 0.74</td> <!-- MMLU-no -->
   <td class="no reason">0.96 ± 1.02 / 25.05 ± 0.84</td> <!-- HellaSwag-no -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.03 ± 0.33 / 4.86 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.83 ± 1.04 / 25.47 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.62 ± 0.73 / 24.51 ± 0.53</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="da-rank">3.97</td> <!-- Danish rank -->
   <td class="no-rank">4.44</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.26</td> <!-- Swedish rank -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da rc">32.12 ± 1.62 / 38.99 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="da summ">62.61 ± 0.99 / 15.12 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">-2.76 ± 1.71 / 22.41 ± 1.17</td> <!-- Danske Talemaader -->
   <td class="da know">5.08 ± 2.61 / 35.14 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.70 ± 0.94 / 24.83 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">56.77 ± 2.04 / 9.18 ± 1.21</td> <!-- No Sammendrag -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no rc">5.84 ± 1.36 / 16.14 ± 2.48</td> <!-- NorQuAD -->
   <td class="no know">-0.50 ± 1.10 / 23.75 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">0.07 ± 1.21 / 25.26 ± 0.95</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.81 ± 2.73 / 35.67 ± 2.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.68 ± 0.76 / 11.19 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">-0.85 ± 1.05 / 24.38 ± 0.51</td> <!-- MMLU-sv -->
   <td class="sv reason">-1.24 ± 0.90 / 24.30 ± 0.63</td> <!-- HellaSwag-sv -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>0.0.0</td> <!-- HellaSwag-da version -->
   <td>0.0.0</td> <!-- NorNE-nb version -->
   <td>0.0.0</td> <!-- NorNE-nn version -->
   <td>0.0.0</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>0.0.0</td> <!-- ScaLA-nb version -->
   <td>0.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>0.0.0</td> <!-- MMLU-no version -->
   <td>0.0.0</td> <!-- HellaSwag-no version -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>0.0.0</td> <!-- MMLU-sv version -->
   <td>0.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="da-rank">4.38</td> <!-- Danish rank -->
   <td class="no-rank">4.48</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.10</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="da-rank">4.20</td> <!-- Danish rank -->
   <td class="no-rank">4.63</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.17</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="da-rank">4.18</td> <!-- Danish rank -->
   <td class="no-rank">4.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.07</td> <!-- Swedish rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da rc">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
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
   <td class="no rc">0.46 ± 0.07 / 6.96 ± 0.13</td> <!-- NorQuAD -->
   <td class="no know">2.43 ± 1.10 / 24.94 ± 0.98</td> <!-- MMLU-no -->
   <td class="no reason">2.35 ± 0.86 / 26.35 ± 0.78</td> <!-- HellaSwag-no -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">39.53 ± 0.34 / 5.71 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">0.69 ± 0.90 / 24.20 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">0.12 ± 1.51 / 24.97 ± 1.28</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.42</td> <!-- ScandEval rank -->
   <td class="da-rank">4.35</td> <!-- Danish rank -->
   <td class="no-rank">4.54</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.37</td> <!-- Swedish rank -->
   <td class="da ner">13.98 ± 1.54 / 13.46 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">6.37 ± 3.38 / 25.43 ± 4.09</td> <!-- Angry Tweets -->
   <td class="da la">0.41 ± 0.80 / 33.31 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">20.46 ± 2.90 / 24.27 ± 3.23</td> <!-- ScandiQA-da -->
   <td class="da summ">60.87 ± 0.92 / 12.82 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">0.53 ± 1.10 / 24.39 ± 0.85</td> <!-- Danske Talemaader -->
   <td class="da know">4.72 ± 3.89 / 35.76 ± 1.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.07 ± 0.75 / 24.90 ± 0.90</td> <!-- HellaSwag-da -->
   <td class="no ner">27.66 ± 2.00 / 28.61 ± 2.15</td> <!-- NorNE-nb -->
   <td class="no ner">30.88 ± 2.13 / 31.97 ± 2.10</td> <!-- NorNE-nn -->
   <td class="no sent">5.13 ± 3.33 / 20.41 ± 3.12</td> <!-- NoReC -->
   <td class="no summ">58.91 ± 0.95 / 9.74 ± 0.45</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">7.55 ± 1.17 / 15.63 ± 2.64</td> <!-- NorQuAD -->
   <td class="no know">-0.68 ± 1.27 / 22.92 ± 0.65</td> <!-- MMLU-no -->
   <td class="no reason">0.32 ± 0.59 / 25.12 ± 0.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.05 ± 2.31 / 24.35 ± 1.99</td> <!-- SUC3 -->
   <td class="sv sent">12.47 ± 7.10 / 23.03 ± 8.78</td> <!-- SweReC -->
   <td class="sv la">0.08 ± 0.16 / 33.34 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.43 ± 2.69 / 24.25 ± 2.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.80 ± 0.93 / 14.56 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">0.72 ± 0.72 / 23.30 ± 0.96</td> <!-- MMLU-sv -->
   <td class="sv reason">0.11 ± 0.91 / 25.15 ± 0.81</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>11.0.0</td> <!-- NorNE-nb version -->
   <td>11.0.0</td> <!-- NorNE-nn version -->
   <td>9.3.2</td> <!-- NoReC version -->
   <td>12.4.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.4.0</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="da-rank">4.16</td> <!-- Danish rank -->
   <td class="no-rank">5.43</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.22</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da-rank">4.53</td> <!-- Danish rank -->
   <td class="no-rank">4.92</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.43</td> <!-- Swedish rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
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
   <td class="no rc">0.00 ± 0.00 / 3.06 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">0.32 ± 1.03 / 24.22 ± 1.37</td> <!-- MMLU-no -->
   <td class="no reason">0.12 ± 0.91 / 24.92 ± 0.59</td> <!-- HellaSwag-no -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">43.75 ± 0.28 / 4.67 ± 0.12</td> <!-- SweDN -->
   <td class="sv know">-0.22 ± 0.80 / 23.76 ± 0.84</td> <!-- MMLU-sv -->
   <td class="sv reason">0.75 ± 1.00 / 25.27 ± 0.56</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="da-rank">4.51</td> <!-- Danish rank -->
   <td class="no-rank">4.82</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.74</td> <!-- Swedish rank -->
   <td class="da ner">12.82 ± 2.64 / 12.37 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">3.55 ± 3.64 / 22.75 ± 4.02</td> <!-- Angry Tweets -->
   <td class="da la">0.68 ± 1.41 / 35.13 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da rc">19.85 ± 1.75 / 24.31 ± 1.88</td> <!-- ScandiQA-da -->
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
   <td class="no rc">1.85 ± 0.82 / 10.19 ± 1.99</td> <!-- NorQuAD -->
   <td class="no know">-2.42 ± 1.29 / 21.73 ± 0.58</td> <!-- MMLU-no -->
   <td class="no reason">1.23 ± 1.22 / 25.06 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">48.74 ± 1.72 / 10.30 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">-0.62 ± 1.15 / 22.04 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">0.99 ± 1.35 / 25.36 ± 0.92</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="da-rank">4.64</td> <!-- Danish rank -->
   <td class="no-rank">4.89</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.65</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 12.39 ± 1.52</td> <!-- ScandiQA-da -->
   <td class="da summ">61.25 ± 0.17 / 12.03 ± 0.21</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 0.14 / 25.18 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no summ">59.32 ± 0.11 / 9.47 ± 0.12</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 33.45 ± 0.27</td> <!-- NorQuAD -->
   <td class="no know">0.18 ± 0.35 / 21.91 ± 0.52</td> <!-- MMLU-no -->
   <td class="no reason">0.30 ± 0.40 / 25.03 ± 0.88</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 8.92 ± 2.90</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.04 ± 0.07 / 10.84 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.25 ± 0.97 / 21.96 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">0.08 ± 0.78 / 24.93 ± 0.77</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
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
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>9.3.1</td> <!-- MMLU-no version -->
   <td>9.3.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="da-rank">4.61</td> <!-- Danish rank -->
   <td class="no-rank">4.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.77</td> <!-- Swedish rank -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da rc">16.64 ± 3.32 / 19.46 ± 3.63</td> <!-- ScandiQA-da -->
   <td class="da summ">52.34 ± 1.60 / 8.84 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">-0.58 ± 0.97 / 24.00 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">5.18 ± 4.75 / 36.68 ± 2.20</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.28 ± 0.99 / 24.75 ± 0.93</td> <!-- HellaSwag-da -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no summ">51.68 ± 2.20 / 7.39 ± 0.89</td> <!-- No Sammendrag -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no rc">2.32 ± 0.68 / 6.65 ± 1.90</td> <!-- NorQuAD -->
   <td class="no know">0.39 ± 1.28 / 23.22 ± 0.56</td> <!-- MMLU-no -->
   <td class="no reason">-0.80 ± 0.71 / 24.77 ± 0.62</td> <!-- HellaSwag-no -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.40 ± 2.88 / 19.18 ± 3.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">51.48 ± 1.14 / 10.63 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.60 / 22.53 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">1.17 ± 0.86 / 25.54 ± 0.87</td> <!-- HellaSwag-sv -->
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
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.77</td> <!-- ScandEval rank -->
   <td class="da-rank">4.71</td> <!-- Danish rank -->
   <td class="no-rank">4.87</td> <!-- Norwegian rank -->
   <td class="sv-rank">4.73</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.81 ± 2.69 / 19.31 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 30.05 ± 4.99</td> <!-- ScandiQA-da -->
   <td class="da summ">61.06 ± 0.14 / 12.02 ± 0.15</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.15 ± 0.64 / 25.21 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.27 ± 1.21 / 9.77 ± 0.51</td> <!-- NoReC -->
   <td class="no summ">59.10 ± 0.12 / 9.14 ± 0.11</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 32.25 ± 0.29</td> <!-- NorQuAD -->
   <td class="no know">0.83 ± 0.90 / 21.96 ± 0.50</td> <!-- MMLU-no -->
   <td class="no reason">0.09 ± 0.50 / 25.03 ± 0.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.62 ± 12.67 / 35.36 ± 8.35</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 19.59 ± 6.84</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.16 ± 0.07 / 8.81 ± 0.07</td> <!-- SweDN -->
   <td class="sv know">0.47 ± 0.86 / 22.03 ± 0.59</td> <!-- MMLU-sv -->
   <td class="sv reason">0.71 ± 0.64 / 25.02 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="da-rank">4.58</td> <!-- Danish rank -->
   <td class="no-rank">4.88</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.07</td> <!-- Swedish rank -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da rc">6.84 ± 6.83 / 21.33 ± 6.27</td> <!-- ScandiQA-da -->
   <td class="da summ">53.76 ± 0.47 / 11.17 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">-1.83 ± 1.68 / 23.94 ± 1.25</td> <!-- Danske Talemaader -->
   <td class="da know">0.99 ± 3.76 / 34.10 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.48 ± 0.94 / 24.73 ± 0.61</td> <!-- HellaSwag-da -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">20.84 ± 6.06 / 35.78 ± 5.94</td> <!-- NoReC -->
   <td class="no summ">44.23 ± 0.84 / 6.81 ± 0.16</td> <!-- No Sammendrag -->
   <td class="no la">0.45 ± 1.09 / 34.65 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">0.48 ± 0.66 / 32.86 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">2.43 ± 0.61 / 22.78 ± 2.29</td> <!-- NorQuAD -->
   <td class="no know">0.17 ± 1.46 / 24.43 ± 1.54</td> <!-- MMLU-no -->
   <td class="no reason">-0.49 ± 0.65 / 24.19 ± 0.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.82 ± 11.21 / 31.12 ± 8.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">27.09 ± 0.29 / 6.80 ± 0.12</td> <!-- SweDN -->
   <td class="sv know">-0.67 ± 0.81 / 22.55 ± 0.71</td> <!-- MMLU-sv -->
   <td class="sv reason">0.86 ± 0.82 / 25.38 ± 0.51</td> <!-- HellaSwag-sv -->
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
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>11.0.0</td> <!-- ScaLA-nb version -->
   <td>11.0.0</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>11.0.0</td> <!-- MMLU-no version -->
   <td>11.0.0</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">5.01</td> <!-- ScandEval rank -->
   <td class="da-rank">4.80</td> <!-- Danish rank -->
   <td class="no-rank">5.08</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.16</td> <!-- Swedish rank -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da rc">5.15 ± 6.60 / 17.35 ± 5.86</td> <!-- ScandiQA-da -->
   <td class="da summ">51.83 ± 0.77 / 10.14 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">-0.96 ± 1.47 / 23.86 ± 1.33</td> <!-- Danske Talemaader -->
   <td class="da know">3.51 ± 3.46 / 35.41 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.73 ± 1.39 / 25.54 ± 1.00</td> <!-- HellaSwag-da -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">20.64 ± 5.63 / 36.75 ± 3.29</td> <!-- NoReC -->
   <td class="no summ">38.55 ± 0.48 / 5.75 ± 0.20</td> <!-- No Sammendrag -->
   <td class="no la">-0.99 ± 0.88 / 33.37 ± 0.27</td> <!-- ScaLA-nb -->
   <td class="no la">-0.15 ± 0.72 / 32.83 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.53 ± 0.31 / 22.14 ± 2.25</td> <!-- NorQuAD -->
   <td class="no know">0.63 ± 1.48 / 24.41 ± 1.24</td> <!-- MMLU-no -->
   <td class="no reason">-0.09 ± 0.80 / 24.42 ± 0.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">4.79 ± 3.55 / 18.06 ± 2.80</td> <!-- ScandiQA-sv -->
   <td class="sv summ">26.97 ± 0.41 / 6.56 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">-0.11 ± 1.16 / 23.32 ± 0.92</td> <!-- MMLU-sv -->
   <td class="sv reason">0.56 ± 1.22 / 24.79 ± 0.91</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>9.3.1</td> <!-- NorNE-nb version -->
   <td>9.3.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>12.5.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="da-rank">4.87</td> <!-- Danish rank -->
   <td class="no-rank">5.11</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.21</td> <!-- Swedish rank -->
   <td class="da ner">1.13 ± 1.19 / 0.97 ± 1.03</td> <!-- DANSK -->
   <td class="da sent">2.06 ± 2.30 / 20.38 ± 2.71</td> <!-- Angry Tweets -->
   <td class="da la">-0.36 ± 0.97 / 41.52 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da rc">0.32 ± 0.12 / 4.20 ± 0.61</td> <!-- ScandiQA-da -->
   <td class="da summ">54.00 ± 0.80 / 9.08 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">-2.57 ± 2.04 / 23.19 ± 1.37</td> <!-- Danske Talemaader -->
   <td class="da know">3.26 ± 1.64 / 29.55 ± 2.52</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.62 ± 0.87 / 24.55 ± 0.66</td> <!-- HellaSwag-da -->
   <td class="no ner">3.14 ± 2.12 / 2.91 ± 2.02</td> <!-- NorNE-nb -->
   <td class="no ner">3.00 ± 1.58 / 2.65 ± 1.41</td> <!-- NorNE-nn -->
   <td class="no sent">3.41 ± 2.11 / 14.87 ± 2.38</td> <!-- NoReC -->
   <td class="no summ">45.57 ± 1.88 / 4.96 ± 0.39</td> <!-- No Sammendrag -->
   <td class="no la">0.22 ± 0.42 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">0.27 ± 0.79 / 38.20 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 2.27 ± 0.89</td> <!-- NorQuAD -->
   <td class="no know">-0.45 ± 1.48 / 24.16 ± 1.48</td> <!-- MMLU-no -->
   <td class="no reason">-0.27 ± 0.89 / 24.77 ± 0.63</td> <!-- HellaSwag-no -->
   <td class="sv ner">1.47 ± 1.90 / 1.32 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">5.50 ± 4.49 / 28.77 ± 3.76</td> <!-- SweReC -->
   <td class="sv la">-2.19 ± 1.29 / 40.52 ± 3.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.10 ± 0.06 / 4.36 ± 0.44</td> <!-- ScandiQA-sv -->
   <td class="sv summ">37.40 ± 0.61 / 6.53 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">-0.53 ± 1.01 / 24.38 ± 1.08</td> <!-- MMLU-sv -->
   <td class="sv reason">0.25 ± 1.22 / 25.23 ± 0.73</td> <!-- HellaSwag-sv -->
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
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="da-rank">4.99</td> <!-- Danish rank -->
   <td class="no-rank">5.23</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.11</td> <!-- Swedish rank -->
   <td class="da ner">0.64 ± 0.89 / 0.52 ± 0.69</td> <!-- DANSK -->
   <td class="da sent">-0.52 ± 1.72 / 28.55 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">-0.02 ± 1.55 / 36.82 ± 2.52</td> <!-- ScaLA-da -->
   <td class="da rc">0.48 ± 0.27 / 2.89 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="da summ">50.23 ± 0.89 / 6.09 ± 0.27</td> <!-- Nordjylland-News -->
   <td class="da know">0.90 ± 0.92 / 26.20 ± 1.02</td> <!-- Danske Talemaader -->
   <td class="da know">4.10 ± 2.68 / 33.71 ± 1.88</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 1.16 / 25.21 ± 0.48</td> <!-- HellaSwag-da -->
   <td class="no ner">0.29 ± 0.29 / 0.29 ± 0.27</td> <!-- NorNE-nb -->
   <td class="no ner">0.25 ± 0.17 / 0.27 ± 0.21</td> <!-- NorNE-nn -->
   <td class="no sent">-1.43 ± 1.45 / 20.90 ± 4.96</td> <!-- NoReC -->
   <td class="no summ">41.89 ± 1.40 / 3.46 ± 0.33</td> <!-- No Sammendrag -->
   <td class="no la">-0.42 ± 1.10 / 35.77 ± 3.09</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.21 / 39.28 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 3.15 ± 0.55</td> <!-- NorQuAD -->
   <td class="no know">0.69 ± 0.71 / 24.93 ± 0.99</td> <!-- MMLU-no -->
   <td class="no reason">0.55 ± 0.68 / 25.11 ± 0.43</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.26 ± 0.16 / 0.26 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">4.75 ± 2.54 / 27.85 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">-0.60 ± 1.56 / 40.53 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.06 ± 0.09 / 1.07 ± 0.35</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.84 ± 0.24 / 5.74 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.41 ± 1.39 / 24.48 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.81 / 25.32 ± 0.65</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   <td>10.0.1</td> <!-- NorNE-nb version -->
   <td>10.0.1</td> <!-- NorNE-nn version -->
   <td>10.0.1</td> <!-- NoReC version -->
   <td>11.0.0</td> <!-- No Sammendrag version -->
   <td>10.0.1</td> <!-- ScaLA-nb version -->
   <td>10.0.1</td> <!-- ScaLA-nn version -->
   <td>10.0.1</td> <!-- NorQuAD version -->
   <td>10.0.1</td> <!-- MMLU-no version -->
   <td>10.0.1</td> <!-- HellaSwag-no version -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.31</td> <!-- ScandEval rank -->
   <td class="da-rank">5.31</td> <!-- Danish rank -->
   <td class="no-rank">5.35</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.27</td> <!-- Swedish rank -->
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
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">5.35</td> <!-- ScandEval rank -->
   <td class="da-rank">5.44</td> <!-- Danish rank -->
   <td class="no-rank">5.29</td> <!-- Norwegian rank -->
   <td class="sv-rank">5.31</td> <!-- Swedish rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 0.04 ± 0.01</td> <!-- ScandiQA-da -->
   <td class="da summ">37.85 ± 0.55 / 0.76 ± 0.08</td> <!-- Nordjylland-News -->
   <td class="da know">0.26 ± 0.46 / 23.72 ± 0.47</td> <!-- Danske Talemaader -->
   <td class="da know">-0.75 ± 1.90 / 34.96 ± 1.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 0.48 / 24.60 ± 0.50</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no summ">39.58 ± 0.08 / 0.78 ± 0.04</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no rc">0.00 ± 0.00 / 0.47 ± 0.03</td> <!-- NorQuAD -->
   <td class="no know">0.18 ± 0.69 / 22.92 ± 0.50</td> <!-- MMLU-no -->
   <td class="no reason">-0.09 ± 0.53 / 24.70 ± 0.47</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-3.60 ± 3.63 / 20.29 ± 1.99</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- ScandiQA-sv -->
   <td class="sv summ">39.68 ± 0.08 / 1.23 ± 0.02</td> <!-- SweDN -->
   <td class="sv know">-0.20 ± 0.77 / 24.13 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.25 ± 0.67 / 24.68 ± 0.44</td> <!-- HellaSwag-sv -->
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
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Mainland Scandinavian NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-lap8i&quot; src=&quot;https://datawrapper.dwcdn.net/lap8i/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
