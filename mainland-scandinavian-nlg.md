---
layout: leaderboard
title: Mainland Scandinavian NLG
---

<center>Last updated: 19/02/2024 10:14:38 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="mainland-scandinavian-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score">SV</span></th>

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
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1</td> <!-- Rank -->
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,244 ± 510 / 3,515 ± 848</td> <!-- Model inference speed -->
   <td class="score">71.46 ± 1.96</td> <!-- ScandEval score -->
   <td class="da-score">69.97 ± 1.79</td> <!-- Danish score -->
   <td class="no-score">70.19 ± 2.42</td> <!-- Norwegian score -->
   <td class="sv-score">74.22 ± 1.68</td> <!-- Swedish score -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da qa">49.82 ± 1.79 / 60.78 ± 1.18</td> <!-- ScandiQA-da -->
   <td class="da summ">67.38 ± 0.26 / 20.59 ± 0.61</td> <!-- Nordjylland-News -->
   <td class="da know">94.93 ± 1.03 / 96.21 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">93.98 ± 2.15 / 95.94 ± 1.44</td> <!-- Danish Citizen Tests -->
   <td class="da reason">81.64 ± 1.80 / 86.17 ± 1.34</td> <!-- HellaSwag-da -->
   <td class="no ner">81.16 ± 2.46 / 63.39 ± 4.07</td> <!-- NorNE-nb -->
   <td class="no ner">75.75 ± 4.49 / 60.44 ± 5.46</td> <!-- NorNE-nn -->
   <td class="no sent">72.72 ± 3.20 / 81.35 ± 2.22</td> <!-- NoReC -->
   <td class="no summ">65.92 ± 0.28 / 19.24 ± 0.59</td> <!-- No Sammendrag -->
   <td class="no la">77.30 ± 2.97 / 88.39 ± 1.60</td> <!-- ScaLA-nb -->
   <td class="no la">57.18 ± 3.91 / 76.40 ± 2.66</td> <!-- ScaLA-nn -->
   <td class="no qa">49.93 ± 3.13 / 77.72 ± 1.70</td> <!-- NorQuAD -->
   <td class="no know">68.77 ± 2.09 / 76.56 ± 1.57</td> <!-- MMLU-no -->
   <td class="no reason">88.30 ± 1.32 / 91.13 ± 0.98</td> <!-- HellaSwag-no -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">56.50 ± 1.74 / 67.22 ± 1.24</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.83 ± 0.15 / 22.67 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">72.53 ± 1.82 / 79.26 ± 1.44</td> <!-- MMLU-sv -->
   <td class="sv reason">85.67 ± 2.59 / 89.14 ± 2.05</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">58.67 ± 2.50</td> <!-- ScandEval score -->
   <td class="da-score">60.62 ± 2.44</td> <!-- Danish score -->
   <td class="no-score">55.47 ± 2.62</td> <!-- Norwegian score -->
   <td class="sv-score">59.91 ± 2.45</td> <!-- Swedish score -->
   <td class="da ner">59.61 ± 2.65 / 47.73 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">50.54 ± 3.00 / 66.79 ± 1.87</td> <!-- Angry Tweets -->
   <td class="da la">57.57 ± 3.30 / 77.07 ± 1.91</td> <!-- ScaLA-da -->
   <td class="da qa">51.09 ± 1.97 / 59.01 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 0.29 / 18.43 ± 0.41</td> <!-- Nordjylland-News -->
   <td class="da know">81.95 ± 2.61 / 86.33 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">77.66 ± 2.57 / 85.08 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">59.36 ± 3.26 / 69.18 ± 2.51</td> <!-- HellaSwag-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no summ">64.35 ± 0.24 / 15.05 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">46.44 ± 1.55 / 72.64 ± 1.26</td> <!-- NorQuAD -->
   <td class="no know">40.26 ± 5.24 / 54.88 ± 3.85</td> <!-- MMLU-no -->
   <td class="no reason">59.02 ± 1.63 / 68.63 ± 1.34</td> <!-- HellaSwag-no -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.59 ± 2.08 / 65.53 ± 1.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.66 ± 0.17 / 19.69 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">40.73 ± 3.36 / 55.16 ± 2.75</td> <!-- MMLU-sv -->
   <td class="sv reason">50.51 ± 2.33 / 62.07 ± 1.95</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="score">48.96 ± 2.89</td> <!-- ScandEval score -->
   <td class="da-score">52.66 ± 2.55</td> <!-- Danish score -->
   <td class="no-score">44.31 ± 3.20</td> <!-- Norwegian score -->
   <td class="sv-score">49.90 ± 2.91</td> <!-- Swedish score -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">56.70 ± 1.80 / 64.12 ± 1.15</td> <!-- ScandiQA-da -->
   <td class="da summ">68.75 ± 0.47 / 24.84 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">74.24 ± 2.14 / 80.62 ± 1.61</td> <!-- Danske Talemaader -->
   <td class="da know">70.86 ± 3.58 / 80.31 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">41.49 ± 2.88 / 55.86 ± 2.17</td> <!-- HellaSwag-da -->
   <td class="no ner">61.18 ± 2.76 / 56.36 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">65.16 ± 3.97 / 55.74 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">55.61 ± 4.02 / 68.27 ± 3.49</td> <!-- NoReC -->
   <td class="no summ">65.99 ± 0.31 / 19.46 ± 0.47</td> <!-- No Sammendrag -->
   <td class="no la">20.84 ± 5.41 / 49.36 ± 4.98</td> <!-- ScaLA-nb -->
   <td class="no la">9.12 ± 3.51 / 43.06 ± 3.74</td> <!-- ScaLA-nn -->
   <td class="no qa">42.98 ± 3.04 / 69.12 ± 2.82</td> <!-- NorQuAD -->
   <td class="no know">27.77 ± 2.86 / 45.43 ± 2.04</td> <!-- MMLU-no -->
   <td class="no reason">39.67 ± 4.37 / 54.26 ± 3.37</td> <!-- HellaSwag-no -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.43 ± 1.62 / 65.06 ± 1.24</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.58 ± 0.22 / 22.52 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">32.54 ± 2.61 / 49.30 ± 1.93</td> <!-- MMLU-sv -->
   <td class="sv reason">34.94 ± 3.79 / 50.39 ± 3.23</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="score">47.75 ± 2.64</td> <!-- ScandEval score -->
   <td class="da-score">49.94 ± 2.75</td> <!-- Danish score -->
   <td class="no-score">44.27 ± 2.63</td> <!-- Norwegian score -->
   <td class="sv-score">49.04 ± 2.53</td> <!-- Swedish score -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 2.00 / 64.34 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="da summ">68.44 ± 0.43 / 24.68 ± 0.67</td> <!-- Nordjylland-News -->
   <td class="da know">67.37 ± 4.12 / 75.55 ± 3.01</td> <!-- Danske Talemaader -->
   <td class="da know">66.75 ± 3.42 / 77.34 ± 2.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.21 ± 3.40 / 56.48 ± 2.62</td> <!-- HellaSwag-da -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no summ">66.08 ± 0.32 / 20.15 ± 0.64</td> <!-- No Sammendrag -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no qa">42.42 ± 2.92 / 69.55 ± 3.18</td> <!-- NorQuAD -->
   <td class="no know">27.31 ± 2.26 / 45.04 ± 1.66</td> <!-- MMLU-no -->
   <td class="no reason">41.63 ± 2.84 / 56.02 ± 2.19</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.69 ± 1.54 / 65.02 ± 1.14</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.06 ± 0.31 / 23.91 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">33.71 ± 2.28 / 50.08 ± 1.68</td> <!-- MMLU-sv -->
   <td class="sv reason">41.45 ± 3.36 / 55.51 ± 2.69</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="score">47.13 ± 2.56</td> <!-- ScandEval score -->
   <td class="da-score">47.38 ± 2.81</td> <!-- Danish score -->
   <td class="no-score">46.12 ± 2.79</td> <!-- Norwegian score -->
   <td class="sv-score">47.90 ± 2.09</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">68.14 ± 0.43 / 23.78 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="score">47.13 ± 2.56</td> <!-- ScandEval score -->
   <td class="da-score">47.38 ± 2.81</td> <!-- Danish score -->
   <td class="no-score">46.12 ± 2.79</td> <!-- Norwegian score -->
   <td class="sv-score">47.90 ± 2.09</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">68.14 ± 0.43 / 23.78 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">47.06 ± 2.75</td> <!-- ScandEval score -->
   <td class="da-score">49.58 ± 2.72</td> <!-- Danish score -->
   <td class="no-score">42.47 ± 2.53</td> <!-- Norwegian score -->
   <td class="sv-score">49.14 ± 3.02</td> <!-- Swedish score -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da qa">51.75 ± 2.23 / 61.31 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="da summ">68.15 ± 0.54 / 23.56 ± 0.64</td> <!-- Nordjylland-News -->
   <td class="da know">65.38 ± 2.59 / 73.95 ± 1.84</td> <!-- Danske Talemaader -->
   <td class="da know">62.78 ± 4.04 / 74.61 ± 2.90</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.07 ± 2.57 / 53.83 ± 2.06</td> <!-- HellaSwag-da -->
   <td class="no ner">62.47 ± 2.56 / 57.71 ± 3.02</td> <!-- NorNE-nb -->
   <td class="no ner">66.69 ± 2.91 / 58.83 ± 3.70</td> <!-- NorNE-nn -->
   <td class="no sent">54.04 ± 2.91 / 66.46 ± 2.59</td> <!-- NoReC -->
   <td class="no summ">65.74 ± 0.37 / 19.13 ± 0.54</td> <!-- No Sammendrag -->
   <td class="no la">16.75 ± 4.54 / 49.11 ± 4.45</td> <!-- ScaLA-nb -->
   <td class="no la">13.00 ± 4.46 / 49.33 ± 2.69</td> <!-- ScaLA-nn -->
   <td class="no qa">34.48 ± 2.13 / 65.45 ± 2.05</td> <!-- NorQuAD -->
   <td class="no know">28.39 ± 1.76 / 45.59 ± 1.28</td> <!-- MMLU-no -->
   <td class="no reason">35.19 ± 3.28 / 50.12 ± 3.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.96 ± 2.34 / 60.01 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.35 ± 0.32 / 24.05 ± 0.66</td> <!-- SweDN -->
   <td class="sv know">32.30 ± 2.48 / 48.98 ± 1.96</td> <!-- MMLU-sv -->
   <td class="sv reason">38.78 ± 5.70 / 52.89 ± 4.91</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="score">46.92 ± 2.81</td> <!-- ScandEval score -->
   <td class="da-score">48.75 ± 2.80</td> <!-- Danish score -->
   <td class="no-score">41.28 ± 2.75</td> <!-- Norwegian score -->
   <td class="sv-score">50.71 ± 2.88</td> <!-- Swedish score -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da qa">57.39 ± 1.73 / 63.66 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="da summ">67.78 ± 0.78 / 23.48 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">66.49 ± 2.90 / 74.84 ± 2.12</td> <!-- Danske Talemaader -->
   <td class="da know">60.41 ± 1.95 / 72.97 ± 1.45</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.51 ± 3.95 / 45.74 ± 3.03</td> <!-- HellaSwag-da -->
   <td class="no ner">54.04 ± 2.86 / 48.50 ± 2.85</td> <!-- NorNE-nb -->
   <td class="no ner">62.21 ± 3.31 / 50.38 ± 4.32</td> <!-- NorNE-nn -->
   <td class="no sent">54.74 ± 3.71 / 67.81 ± 2.80</td> <!-- NoReC -->
   <td class="no summ">65.60 ± 0.49 / 19.07 ± 0.70</td> <!-- No Sammendrag -->
   <td class="no la">14.51 ± 1.97 / 40.94 ± 1.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.38 ± 4.69 / 37.62 ± 2.92</td> <!-- ScaLA-nn -->
   <td class="no qa">42.71 ± 3.21 / 69.11 ± 2.46</td> <!-- NorQuAD -->
   <td class="no know">25.82 ± 1.66 / 43.75 ± 1.18</td> <!-- MMLU-no -->
   <td class="no reason">32.01 ± 3.74 / 48.40 ± 2.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.92 ± 1.60 / 65.40 ± 1.37</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.89 ± 0.44 / 23.94 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">34.80 ± 2.79 / 50.82 ± 2.10</td> <!-- MMLU-sv -->
   <td class="sv reason">36.65 ± 5.07 / 51.56 ± 4.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="score">46.82 ± 2.70</td> <!-- ScandEval score -->
   <td class="da-score">50.12 ± 2.63</td> <!-- Danish score -->
   <td class="no-score">41.43 ± 2.40</td> <!-- Norwegian score -->
   <td class="sv-score">48.91 ± 3.07</td> <!-- Swedish score -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da qa">57.88 ± 2.44 / 64.46 ± 1.86</td> <!-- ScandiQA-da -->
   <td class="da summ">67.84 ± 0.47 / 23.04 ± 0.67</td> <!-- Nordjylland-News -->
   <td class="da know">72.92 ± 2.52 / 79.69 ± 1.88</td> <!-- Danske Talemaader -->
   <td class="da know">68.11 ± 3.00 / 78.52 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">40.62 ± 3.23 / 55.12 ± 2.44</td> <!-- HellaSwag-da -->
   <td class="no ner">53.68 ± 2.01 / 49.22 ± 2.67</td> <!-- NorNE-nb -->
   <td class="no ner">61.92 ± 4.06 / 49.03 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">47.78 ± 3.19 / 57.76 ± 2.55</td> <!-- NoReC -->
   <td class="no summ">64.23 ± 0.75 / 16.90 ± 0.94</td> <!-- No Sammendrag -->
   <td class="no la">0.91 ± 1.78 / 33.51 ± 0.85</td> <!-- ScaLA-nb -->
   <td class="no la">1.24 ± 1.66 / 33.71 ± 0.94</td> <!-- ScaLA-nn -->
   <td class="no qa">47.95 ± 2.91 / 71.02 ± 2.28</td> <!-- NorQuAD -->
   <td class="no know">28.59 ± 2.31 / 46.48 ± 1.80</td> <!-- MMLU-no -->
   <td class="no reason">42.57 ± 2.86 / 56.64 ± 2.17</td> <!-- HellaSwag-no -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.03 ± 1.95 / 64.06 ± 1.75</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.13 ± 0.34 / 19.26 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">29.81 ± 2.25 / 47.46 ± 1.72</td> <!-- MMLU-sv -->
   <td class="sv reason">35.59 ± 3.75 / 51.76 ± 2.63</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="score">46.69 ± 1.22</td> <!-- ScandEval score -->
   <td class="da-score">45.46 ± 0.94</td> <!-- Danish score -->
   <td class="no-score">46.63 ± 1.75</td> <!-- Norwegian score -->
   <td class="sv-score">47.98 ± 0.99</td> <!-- Swedish score -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">57.24 ± 0.74 / 63.79 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">67.61 ± 0.21 / 22.14 ± 0.48</td> <!-- Nordjylland-News -->
   <td class="da know">64.32 ± 1.99 / 73.00 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">53.18 ± 2.37 / 67.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">43.42 ± 1.05 / 57.50 ± 0.80</td> <!-- HellaSwag-da -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no summ">66.20 ± 0.24 / 20.14 ± 0.31</td> <!-- No Sammendrag -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no qa">49.06 ± 4.30 / 74.35 ± 3.96</td> <!-- NorQuAD -->
   <td class="no know">32.37 ± 1.15 / 49.00 ± 0.91</td> <!-- MMLU-no -->
   <td class="no reason">47.62 ± 1.62 / 60.59 ± 1.18</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.13 ± 1.18 / 65.74 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.33 ± 0.16 / 18.83 ± 0.21</td> <!-- SweDN -->
   <td class="sv know">35.01 ± 0.99 / 51.07 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">43.72 ± 0.69 / 57.66 ± 0.50</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="score">46.39 ± 2.69</td> <!-- ScandEval score -->
   <td class="da-score">49.68 ± 2.50</td> <!-- Danish score -->
   <td class="no-score">41.48 ± 2.95</td> <!-- Norwegian score -->
   <td class="sv-score">48.00 ± 2.62</td> <!-- Swedish score -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">58.23 ± 1.78 / 63.89 ± 1.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.78 ± 0.60 / 20.69 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">65.32 ± 3.33 / 73.95 ± 2.50</td> <!-- Danske Talemaader -->
   <td class="da know">64.76 ± 3.24 / 75.94 ± 2.37</td> <!-- Danish Citizen Tests -->
   <td class="da reason">33.70 ± 2.78 / 50.16 ± 2.01</td> <!-- HellaSwag-da -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no summ">65.23 ± 0.55 / 18.64 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no qa">41.56 ± 3.29 / 67.34 ± 2.82</td> <!-- NorQuAD -->
   <td class="no know">27.42 ± 2.13 / 45.20 ± 1.58</td> <!-- MMLU-no -->
   <td class="no reason">36.05 ± 3.95 / 51.68 ± 2.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.10 ± 1.61 / 65.00 ± 1.34</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.62 ± 0.42 / 23.90 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">27.95 ± 2.57 / 45.86 ± 1.85</td> <!-- MMLU-sv -->
   <td class="sv reason">36.11 ± 3.54 / 51.60 ± 2.44</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="score">45.84 ± 2.93</td> <!-- ScandEval score -->
   <td class="da-score">48.80 ± 2.89</td> <!-- Danish score -->
   <td class="no-score">39.44 ± 3.37</td> <!-- Norwegian score -->
   <td class="sv-score">49.27 ± 2.55</td> <!-- Swedish score -->
   <td class="da ner">46.06 ± 3.28 / 35.43 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 4.23 / 61.68 ± 4.43</td> <!-- Angry Tweets -->
   <td class="da la">27.68 ± 4.25 / 57.59 ± 5.15</td> <!-- ScaLA-da -->
   <td class="da qa">57.78 ± 1.43 / 62.26 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="da summ">67.22 ± 0.84 / 22.14 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">68.64 ± 3.34 / 76.45 ± 2.52</td> <!-- Danske Talemaader -->
   <td class="da know">66.17 ± 3.73 / 76.72 ± 2.55</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.95 ± 2.64 / 42.19 ± 2.42</td> <!-- HellaSwag-da -->
   <td class="no ner">49.69 ± 2.90 / 43.57 ± 2.90</td> <!-- NorNE-nb -->
   <td class="no ner">61.78 ± 2.03 / 49.91 ± 4.24</td> <!-- NorNE-nn -->
   <td class="no sent">55.87 ± 5.21 / 68.97 ± 3.95</td> <!-- NoReC -->
   <td class="no summ">64.94 ± 0.66 / 18.09 ± 1.08</td> <!-- No Sammendrag -->
   <td class="no la">2.99 ± 3.04 / 34.16 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.62 ± 4.06 / 68.17 ± 3.48</td> <!-- NorQuAD -->
   <td class="no know">28.26 ± 2.85 / 45.78 ± 2.14</td> <!-- MMLU-no -->
   <td class="no reason">25.83 ± 5.55 / 43.63 ± 4.29</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.28 ± 3.05 / 34.01 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.62 ± 2.52 / 78.04 ± 2.98</td> <!-- SweReC -->
   <td class="sv la">33.23 ± 4.72 / 61.29 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.00 ± 1.69 / 64.62 ± 1.44</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.68 ± 0.43 / 21.83 ± 0.75</td> <!-- SweDN -->
   <td class="sv know">29.95 ± 1.74 / 47.23 ± 1.24</td> <!-- MMLU-sv -->
   <td class="sv reason">31.12 ± 3.68 / 47.85 ± 2.80</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="score">45.83 ± 2.58</td> <!-- ScandEval score -->
   <td class="da-score">47.00 ± 2.67</td> <!-- Danish score -->
   <td class="no-score">40.96 ± 2.69</td> <!-- Norwegian score -->
   <td class="sv-score">49.52 ± 2.37</td> <!-- Swedish score -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da qa">58.27 ± 1.08 / 63.53 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">66.17 ± 0.63 / 18.50 ± 0.60</td> <!-- Nordjylland-News -->
   <td class="da know">61.29 ± 2.33 / 70.82 ± 1.78</td> <!-- Danske Talemaader -->
   <td class="da know">60.29 ± 2.58 / 72.97 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.33 ± 2.11 / 45.86 ± 1.72</td> <!-- HellaSwag-da -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no summ">64.96 ± 0.56 / 17.92 ± 0.82</td> <!-- No Sammendrag -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">42.02 ± 2.82 / 66.99 ± 2.53</td> <!-- NorQuAD -->
   <td class="no know">26.64 ± 1.95 / 44.88 ± 1.41</td> <!-- MMLU-no -->
   <td class="no reason">31.14 ± 2.64 / 48.01 ± 2.14</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.18 ± 1.37 / 64.78 ± 1.14</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.54 ± 0.48 / 23.67 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 2.34 / 46.95 ± 1.75</td> <!-- MMLU-sv -->
   <td class="sv reason">37.45 ± 3.61 / 52.85 ± 2.76</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="score">45.82 ± 2.85</td> <!-- ScandEval score -->
   <td class="da-score">48.92 ± 2.82</td> <!-- Danish score -->
   <td class="no-score">40.78 ± 3.10</td> <!-- Norwegian score -->
   <td class="sv-score">47.75 ± 2.64</td> <!-- Swedish score -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da qa">56.81 ± 1.68 / 62.39 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="da summ">66.05 ± 0.78 / 17.88 ± 0.99</td> <!-- Nordjylland-News -->
   <td class="da know">67.48 ± 3.13 / 75.62 ± 2.33</td> <!-- Danske Talemaader -->
   <td class="da know">63.69 ± 2.43 / 75.31 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">32.11 ± 3.47 / 48.55 ± 2.67</td> <!-- HellaSwag-da -->
   <td class="no ner">55.93 ± 2.70 / 50.51 ± 3.15</td> <!-- NorNE-nb -->
   <td class="no ner">63.85 ± 2.45 / 53.11 ± 4.11</td> <!-- NorNE-nn -->
   <td class="no sent">50.41 ± 5.49 / 64.49 ± 4.37</td> <!-- NoReC -->
   <td class="no summ">65.10 ± 0.51 / 18.12 ± 0.74</td> <!-- No Sammendrag -->
   <td class="no la">15.74 ± 4.15 / 41.16 ± 2.21</td> <!-- ScaLA-nb -->
   <td class="no la">2.23 ± 4.69 / 34.70 ± 1.39</td> <!-- ScaLA-nn -->
   <td class="no qa">39.87 ± 2.87 / 65.67 ± 2.58</td> <!-- NorQuAD -->
   <td class="no know">26.34 ± 1.48 / 44.69 ± 1.13</td> <!-- MMLU-no -->
   <td class="no reason">34.85 ± 4.33 / 50.23 ± 3.39</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.81 ± 1.16 / 64.81 ± 1.01</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.48 / 23.65 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">27.24 ± 2.07 / 45.51 ± 1.53</td> <!-- MMLU-sv -->
   <td class="sv reason">32.04 ± 4.21 / 48.67 ± 3.11</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="score">45.72 ± 2.82</td> <!-- ScandEval score -->
   <td class="da-score">48.72 ± 2.88</td> <!-- Danish score -->
   <td class="no-score">39.53 ± 3.20</td> <!-- Norwegian score -->
   <td class="sv-score">48.92 ± 2.39</td> <!-- Swedish score -->
   <td class="da ner">45.94 ± 3.62 / 35.68 ± 3.35</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 4.52 / 62.28 ± 4.29</td> <!-- Angry Tweets -->
   <td class="da la">28.04 ± 3.83 / 58.31 ± 5.00</td> <!-- ScaLA-da -->
   <td class="da qa">57.65 ± 1.66 / 62.03 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">67.21 ± 0.84 / 22.21 ± 1.05</td> <!-- Nordjylland-News -->
   <td class="da know">68.88 ± 2.98 / 76.64 ± 2.22</td> <!-- Danske Talemaader -->
   <td class="da know">64.81 ± 3.96 / 75.78 ± 2.64</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.63 ± 2.25 / 42.03 ± 2.02</td> <!-- HellaSwag-da -->
   <td class="no ner">49.67 ± 3.12 / 43.26 ± 3.03</td> <!-- NorNE-nb -->
   <td class="no ner">61.11 ± 1.93 / 50.15 ± 4.14</td> <!-- NorNE-nn -->
   <td class="no sent">56.07 ± 5.22 / 68.93 ± 4.07</td> <!-- NoReC -->
   <td class="no summ">64.97 ± 0.59 / 18.14 ± 1.03</td> <!-- No Sammendrag -->
   <td class="no la">3.81 ± 3.09 / 34.47 ± 1.22</td> <!-- ScaLA-nb -->
   <td class="no la">-1.29 ± 2.53 / 33.32 ± 0.91</td> <!-- ScaLA-nn -->
   <td class="no qa">44.98 ± 4.12 / 68.18 ± 3.39</td> <!-- NorQuAD -->
   <td class="no know">28.63 ± 2.26 / 45.94 ± 1.79</td> <!-- MMLU-no -->
   <td class="no reason">25.43 ± 4.85 / 43.48 ± 3.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.57 ± 3.34 / 33.94 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.53 ± 2.55 / 77.96 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">33.43 ± 3.89 / 61.87 ± 4.02</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.87 ± 1.52 / 64.53 ± 1.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.76 ± 0.41 / 21.92 ± 0.79</td> <!-- SweDN -->
   <td class="sv know">28.89 ± 2.22 / 46.41 ± 1.55</td> <!-- MMLU-sv -->
   <td class="sv reason">30.36 ± 2.80 / 47.15 ± 2.26</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="score">45.57 ± 1.56</td> <!-- ScandEval score -->
   <td class="da-score">48.54 ± 1.58</td> <!-- Danish score -->
   <td class="no-score">41.41 ± 1.74</td> <!-- Norwegian score -->
   <td class="sv-score">46.78 ± 1.37</td> <!-- Swedish score -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da qa">59.82 ± 0.84 / 65.44 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="da summ">68.23 ± 0.18 / 24.43 ± 0.30</td> <!-- Nordjylland-News -->
   <td class="da know">66.61 ± 0.93 / 74.86 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">64.80 ± 1.46 / 76.46 ± 1.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.18 ± 0.99 / 46.64 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">61.41 ± 1.71 / 52.32 ± 2.63</td> <!-- NorNE-nb -->
   <td class="no ner">59.49 ± 1.26 / 49.45 ± 3.31</td> <!-- NorNE-nn -->
   <td class="no sent">49.19 ± 1.64 / 63.36 ± 1.52</td> <!-- NoReC -->
   <td class="no summ">64.87 ± 0.42 / 17.67 ± 0.63</td> <!-- No Sammendrag -->
   <td class="no la">15.17 ± 2.64 / 50.25 ± 4.51</td> <!-- ScaLA-nb -->
   <td class="no la">10.78 ± 1.99 / 50.08 ± 4.20</td> <!-- ScaLA-nn -->
   <td class="no qa">48.98 ± 3.05 / 73.08 ± 2.30</td> <!-- NorQuAD -->
   <td class="no know">27.64 ± 1.39 / 45.78 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">25.74 ± 1.87 / 43.95 ± 1.58</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.60 ± 1.00 / 64.53 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.20 ± 0.21 / 18.38 ± 0.34</td> <!-- SweDN -->
   <td class="sv know">31.04 ± 1.08 / 48.29 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">23.57 ± 1.68 / 42.37 ± 1.34</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="score">44.38 ± 2.59</td> <!-- ScandEval score -->
   <td class="da-score">45.07 ± 2.65</td> <!-- Danish score -->
   <td class="no-score">39.80 ± 2.59</td> <!-- Norwegian score -->
   <td class="sv-score">48.26 ± 2.53</td> <!-- Swedish score -->
   <td class="da ner">45.61 ± 3.06 / 35.04 ± 2.94</td> <!-- DANSK -->
   <td class="da sent">53.73 ± 3.06 / 67.51 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">17.08 ± 5.36 / 52.62 ± 5.62</td> <!-- ScaLA-da -->
   <td class="da qa">56.67 ± 1.19 / 61.18 ± 1.07</td> <!-- ScandiQA-da -->
   <td class="da summ">66.73 ± 0.84 / 21.67 ± 1.21</td> <!-- Nordjylland-News -->
   <td class="da know">60.58 ± 2.62 / 69.80 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">57.89 ± 3.66 / 70.00 ± 2.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.45 ± 1.87 / 35.47 ± 1.77</td> <!-- HellaSwag-da -->
   <td class="no ner">48.24 ± 3.18 / 42.53 ± 3.52</td> <!-- NorNE-nb -->
   <td class="no ner">61.50 ± 1.54 / 50.90 ± 4.58</td> <!-- NorNE-nn -->
   <td class="no sent">49.40 ± 3.40 / 60.71 ± 3.33</td> <!-- NoReC -->
   <td class="no summ">64.56 ± 0.80 / 17.62 ± 1.06</td> <!-- No Sammendrag -->
   <td class="no la">24.12 ± 3.24 / 59.38 ± 2.25</td> <!-- ScaLA-nb -->
   <td class="no la">13.20 ± 3.16 / 54.42 ± 3.04</td> <!-- ScaLA-nn -->
   <td class="no qa">47.93 ± 3.46 / 69.52 ± 3.06</td> <!-- NorQuAD -->
   <td class="no know">26.21 ± 2.32 / 42.54 ± 1.71</td> <!-- MMLU-no -->
   <td class="no reason">17.00 ± 2.59 / 33.52 ± 2.18</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.61 ± 3.11 / 34.10 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 2.01 / 78.30 ± 2.42</td> <!-- SweReC -->
   <td class="sv la">34.16 ± 4.39 / 60.06 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.77 ± 1.76 / 63.50 ± 1.47</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.77 ± 0.46 / 22.42 ± 0.84</td> <!-- SweDN -->
   <td class="sv know">29.77 ± 2.44 / 46.25 ± 1.64</td> <!-- MMLU-sv -->
   <td class="sv reason">25.38 ± 3.56 / 39.34 ± 3.89</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="score">43.44 ± 1.49</td> <!-- ScandEval score -->
   <td class="da-score">47.55 ± 1.73</td> <!-- Danish score -->
   <td class="no-score">38.28 ± 1.48</td> <!-- Norwegian score -->
   <td class="sv-score">44.50 ± 1.26</td> <!-- Swedish score -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da qa">58.35 ± 0.73 / 64.83 ± 0.45</td> <!-- ScandiQA-da -->
   <td class="da summ">67.89 ± 0.78 / 24.45 ± 0.45</td> <!-- Nordjylland-News -->
   <td class="da know">78.71 ± 1.22 / 83.82 ± 0.94</td> <!-- Danske Talemaader -->
   <td class="da know">63.74 ± 2.06 / 74.88 ± 1.46</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.58 ± 0.96 / 45.97 ± 0.76</td> <!-- HellaSwag-da -->
   <td class="no ner">51.99 ± 1.85 / 37.40 ± 2.95</td> <!-- NorNE-nb -->
   <td class="no ner">52.74 ± 1.13 / 36.83 ± 1.95</td> <!-- NorNE-nn -->
   <td class="no sent">50.39 ± 1.38 / 66.42 ± 1.20</td> <!-- NoReC -->
   <td class="no summ">64.22 ± 0.42 / 16.29 ± 0.56</td> <!-- No Sammendrag -->
   <td class="no la">0.99 ± 1.03 / 33.56 ± 0.25</td> <!-- ScaLA-nb -->
   <td class="no la">1.27 ± 1.30 / 34.04 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">47.77 ± 3.16 / 72.52 ± 2.51</td> <!-- NorQuAD -->
   <td class="no know">25.74 ± 0.98 / 43.89 ± 0.69</td> <!-- MMLU-no -->
   <td class="no reason">26.36 ± 1.73 / 44.31 ± 1.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.33 ± 0.94 / 63.73 ± 1.05</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.23 ± 0.34 / 15.41 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">28.15 ± 0.90 / 45.69 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">23.58 ± 1.41 / 42.30 ± 1.04</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="score">43.23 ± 2.77</td> <!-- ScandEval score -->
   <td class="da-score">44.02 ± 2.84</td> <!-- Danish score -->
   <td class="no-score">38.68 ± 2.81</td> <!-- Norwegian score -->
   <td class="sv-score">47.00 ± 2.65</td> <!-- Swedish score -->
   <td class="da ner">45.39 ± 2.46 / 34.45 ± 2.56</td> <!-- DANSK -->
   <td class="da sent">51.95 ± 2.65 / 65.69 ± 2.11</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 6.27 / 45.66 ± 5.58</td> <!-- ScaLA-da -->
   <td class="da qa">58.51 ± 1.35 / 62.73 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="da summ">66.84 ± 0.89 / 21.74 ± 1.24</td> <!-- Nordjylland-News -->
   <td class="da know">57.16 ± 3.03 / 66.99 ± 2.44</td> <!-- Danske Talemaader -->
   <td class="da know">60.06 ± 3.26 / 71.17 ± 2.36</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.62 ± 3.14 / 33.40 ± 2.67</td> <!-- HellaSwag-da -->
   <td class="no ner">47.61 ± 2.50 / 42.16 ± 2.82</td> <!-- NorNE-nb -->
   <td class="no ner">60.57 ± 2.02 / 48.89 ± 4.48</td> <!-- NorNE-nn -->
   <td class="no sent">44.46 ± 4.10 / 52.31 ± 4.53</td> <!-- NoReC -->
   <td class="no summ">64.59 ± 0.86 / 17.61 ± 1.09</td> <!-- No Sammendrag -->
   <td class="no la">23.99 ± 5.54 / 60.60 ± 2.74</td> <!-- ScaLA-nb -->
   <td class="no la">11.60 ± 3.18 / 53.40 ± 2.75</td> <!-- ScaLA-nn -->
   <td class="no qa">47.02 ± 3.37 / 69.07 ± 2.64</td> <!-- NorQuAD -->
   <td class="no know">27.13 ± 1.80 / 42.23 ± 1.12</td> <!-- MMLU-no -->
   <td class="no reason">15.65 ± 2.90 / 31.76 ± 2.07</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.36 ± 3.07 / 34.48 ± 5.22</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 2.19 / 78.11 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">20.94 ± 5.55 / 44.72 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.07 ± 1.90 / 63.87 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.59 ± 0.50 / 22.19 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">31.44 ± 1.94 / 47.30 ± 1.54</td> <!-- MMLU-sv -->
   <td class="sv reason">26.04 ± 3.42 / 38.83 ± 4.24</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="score">42.59 ± 2.83</td> <!-- ScandEval score -->
   <td class="da-score">43.99 ± 2.83</td> <!-- Danish score -->
   <td class="no-score">37.54 ± 2.86</td> <!-- Norwegian score -->
   <td class="sv-score">46.24 ± 2.80</td> <!-- Swedish score -->
   <td class="da ner">46.03 ± 3.93 / 34.23 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">49.59 ± 3.26 / 63.45 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">12.72 ± 3.51 / 46.56 ± 5.33</td> <!-- ScaLA-da -->
   <td class="da qa">57.03 ± 1.13 / 61.58 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="da summ">65.98 ± 0.98 / 20.16 ± 1.27</td> <!-- Nordjylland-News -->
   <td class="da know">59.88 ± 2.64 / 69.41 ± 2.10</td> <!-- Danske Talemaader -->
   <td class="da know">59.51 ± 3.33 / 71.02 ± 2.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.86 ± 4.05 / 34.77 ± 3.07</td> <!-- HellaSwag-da -->
   <td class="no ner">47.26 ± 3.76 / 40.22 ± 3.43</td> <!-- NorNE-nb -->
   <td class="no ner">59.35 ± 2.82 / 45.26 ± 3.91</td> <!-- NorNE-nn -->
   <td class="no sent">54.93 ± 3.49 / 68.45 ± 2.61</td> <!-- NoReC -->
   <td class="no summ">64.25 ± 0.86 / 16.92 ± 1.27</td> <!-- No Sammendrag -->
   <td class="no la">9.00 ± 2.87 / 37.53 ± 2.91</td> <!-- ScaLA-nb -->
   <td class="no la">5.26 ± 3.15 / 39.01 ± 3.54</td> <!-- ScaLA-nn -->
   <td class="no qa">45.95 ± 3.12 / 68.00 ± 3.07</td> <!-- NorQuAD -->
   <td class="no know">21.89 ± 2.60 / 39.61 ± 2.11</td> <!-- MMLU-no -->
   <td class="no reason">15.32 ± 3.65 / 34.57 ± 2.40</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.12 ± 2.72 / 30.73 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">78.74 ± 2.13 / 80.11 ± 2.64</td> <!-- SweReC -->
   <td class="sv la">19.74 ± 6.09 / 46.97 ± 5.83</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.15 ± 1.71 / 65.22 ± 1.28</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.41 ± 0.46 / 21.90 ± 0.70</td> <!-- SweDN -->
   <td class="sv know">31.24 ± 3.01 / 47.77 ± 2.19</td> <!-- MMLU-sv -->
   <td class="sv reason">22.30 ± 3.50 / 39.45 ± 2.60</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="score">42.47 ± 3.06</td> <!-- ScandEval score -->
   <td class="da-score">46.77 ± 2.58</td> <!-- Danish score -->
   <td class="no-score">39.76 ± 3.39</td> <!-- Norwegian score -->
   <td class="sv-score">40.89 ± 3.19</td> <!-- Swedish score -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da qa">58.16 ± 1.29 / 63.63 ± 0.95</td> <!-- ScandiQA-da -->
   <td class="da summ">66.22 ± 0.72 / 18.95 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">62.80 ± 2.47 / 72.15 ± 1.80</td> <!-- Danske Talemaader -->
   <td class="da know">61.54 ± 2.29 / 73.98 ± 1.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.54 ± 2.80 / 43.01 ± 1.95</td> <!-- HellaSwag-da -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no summ">65.11 ± 0.51 / 18.04 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">41.18 ± 3.00 / 66.43 ± 2.76</td> <!-- NorQuAD -->
   <td class="no know">25.61 ± 2.74 / 44.49 ± 2.07</td> <!-- MMLU-no -->
   <td class="no reason">27.67 ± 4.55 / 44.18 ± 3.63</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.03 ± 1.52 / 64.13 ± 1.23</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.55 ± 0.53 / 23.64 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">23.10 ± 2.38 / 42.58 ± 1.74</td> <!-- MMLU-sv -->
   <td class="sv reason">29.31 ± 5.03 / 47.11 ± 3.62</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,505 ± 465 / 774 ± 242</td> <!-- Model inference speed -->
   <td class="score">41.53 ± 1.89</td> <!-- ScandEval score -->
   <td class="da-score">41.35 ± 1.88</td> <!-- Danish score -->
   <td class="no-score">35.44 ± 2.04</td> <!-- Norwegian score -->
   <td class="sv-score">47.81 ± 1.75</td> <!-- Swedish score -->
   <td class="da ner">41.66 ± 3.23 / 28.72 ± 2.20</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 2.03 / 62.67 ± 2.20</td> <!-- Angry Tweets -->
   <td class="da la">17.36 ± 2.43 / 53.55 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">51.28 ± 1.14 / 56.19 ± 0.93</td> <!-- ScandiQA-da -->
   <td class="da summ">66.48 ± 0.60 / 21.83 ± 0.82</td> <!-- Nordjylland-News -->
   <td class="da know">50.80 ± 1.80 / 62.70 ± 1.46</td> <!-- Danske Talemaader -->
   <td class="da know">51.07 ± 0.83 / 66.84 ± 0.61</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.21 ± 2.42 / 34.62 ± 2.04</td> <!-- HellaSwag-da -->
   <td class="no ner">48.28 ± 2.45 / 37.94 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">50.51 ± 2.81 / 38.77 ± 3.26</td> <!-- NorNE-nn -->
   <td class="no sent">49.76 ± 2.62 / 64.69 ± 2.26</td> <!-- NoReC -->
   <td class="no summ">64.48 ± 0.81 / 17.66 ± 1.07</td> <!-- No Sammendrag -->
   <td class="no la">14.54 ± 2.23 / 47.43 ± 4.29</td> <!-- ScaLA-nb -->
   <td class="no la">9.16 ± 1.52 / 48.30 ± 3.84</td> <!-- ScaLA-nn -->
   <td class="no qa">32.04 ± 1.57 / 53.75 ± 1.86</td> <!-- NorQuAD -->
   <td class="no know">25.52 ± 1.42 / 43.62 ± 1.11</td> <!-- MMLU-no -->
   <td class="no reason">15.04 ± 3.34 / 35.35 ± 2.33</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.16 ± 2.57 / 29.58 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">80.29 ± 1.06 / 80.37 ± 0.72</td> <!-- SweReC -->
   <td class="sv la">34.80 ± 2.22 / 65.44 ± 2.16</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.82 ± 3.03 / 57.01 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.96 ± 0.31 / 19.25 ± 0.59</td> <!-- SweDN -->
   <td class="sv know">33.42 ± 0.70 / 49.88 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">25.20 ± 2.35 / 43.09 ± 2.17</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="score">40.13 ± 1.60</td> <!-- ScandEval score -->
   <td class="da-score">42.45 ± 1.56</td> <!-- Danish score -->
   <td class="no-score">35.58 ± 1.75</td> <!-- Norwegian score -->
   <td class="sv-score">42.37 ± 1.51</td> <!-- Swedish score -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da qa">51.49 ± 1.17 / 60.76 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">67.67 ± 0.34 / 22.71 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">51.60 ± 1.33 / 63.50 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.85 ± 2.68 / 52.62 ± 2.08</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.21 ± 1.60 / 40.78 ± 1.32</td> <!-- HellaSwag-da -->
   <td class="no ner">53.42 ± 2.48 / 42.63 ± 1.66</td> <!-- NorNE-nb -->
   <td class="no ner">54.34 ± 1.93 / 41.06 ± 2.40</td> <!-- NorNE-nn -->
   <td class="no sent">38.79 ± 2.56 / 53.72 ± 3.01</td> <!-- NoReC -->
   <td class="no summ">65.14 ± 0.32 / 17.79 ± 0.57</td> <!-- No Sammendrag -->
   <td class="no la">17.06 ± 1.53 / 56.51 ± 2.06</td> <!-- ScaLA-nb -->
   <td class="no la">11.00 ± 1.00 / 53.26 ± 2.32</td> <!-- ScaLA-nn -->
   <td class="no qa">35.68 ± 2.46 / 64.20 ± 2.43</td> <!-- NorQuAD -->
   <td class="no know">20.37 ± 1.34 / 39.32 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">21.16 ± 2.07 / 39.85 ± 1.73</td> <!-- HellaSwag-no -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.50 ± 0.34 / 61.43 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.94 ± 0.15 / 19.70 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">25.60 ± 1.10 / 43.53 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">21.75 ± 1.61 / 40.57 ± 1.45</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">39.80 ± 2.19</td> <!-- ScandEval score -->
   <td class="da-score">41.10 ± 2.07</td> <!-- Danish score -->
   <td class="no-score">34.53 ± 2.53</td> <!-- Norwegian score -->
   <td class="sv-score">43.77 ± 1.96</td> <!-- Swedish score -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">48.51 ± 2.11 / 53.66 ± 2.06</td> <!-- ScandiQA-da -->
   <td class="da summ">67.52 ± 0.29 / 23.53 ± 0.51</td> <!-- Nordjylland-News -->
   <td class="da know">53.26 ± 1.94 / 64.50 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">58.26 ± 2.62 / 71.56 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.53 ± 2.03 / 37.79 ± 1.68</td> <!-- HellaSwag-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no summ">65.05 ± 0.62 / 18.64 ± 0.80</td> <!-- No Sammendrag -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">29.44 ± 2.86 / 50.68 ± 3.91</td> <!-- NorQuAD -->
   <td class="no know">27.78 ± 1.08 / 45.76 ± 0.79</td> <!-- MMLU-no -->
   <td class="no reason">10.88 ± 3.63 / 32.43 ± 2.67</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.43 ± 4.69 / 54.33 ± 4.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.82 ± 0.29 / 19.41 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">35.52 ± 1.01 / 51.52 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">19.67 ± 2.31 / 38.98 ± 1.98</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6=</td> <!-- Rank -->
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,161 ± 1,201 / 1,151 ± 376</td> <!-- Model inference speed -->
   <td class="score">39.52 ± 1.94</td> <!-- ScandEval score -->
   <td class="da-score">42.83 ± 1.96</td> <!-- Danish score -->
   <td class="no-score">32.60 ± 2.58</td> <!-- Norwegian score -->
   <td class="sv-score">43.12 ± 1.29</td> <!-- Swedish score -->
   <td class="da ner">46.30 ± 2.54 / 30.32 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">45.44 ± 1.76 / 59.21 ± 2.03</td> <!-- Angry Tweets -->
   <td class="da la">8.46 ± 4.07 / 37.89 ± 2.91</td> <!-- ScaLA-da -->
   <td class="da qa">58.33 ± 0.82 / 63.88 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="da summ">67.34 ± 0.39 / 23.12 ± 0.42</td> <!-- Nordjylland-News -->
   <td class="da know">60.78 ± 1.64 / 69.96 ± 1.28</td> <!-- Danske Talemaader -->
   <td class="da know">61.29 ± 2.78 / 73.50 ± 1.95</td> <!-- Danish Citizen Tests -->
   <td class="da reason">12.88 ± 1.95 / 32.12 ± 2.40</td> <!-- HellaSwag-da -->
   <td class="no ner">54.34 ± 2.57 / 43.19 ± 2.92</td> <!-- NorNE-nb -->
   <td class="no ner">55.98 ± 2.46 / 43.36 ± 2.98</td> <!-- NorNE-nn -->
   <td class="no sent">45.04 ± 3.29 / 62.68 ± 2.97</td> <!-- NoReC -->
   <td class="no summ">63.69 ± 0.78 / 16.38 ± 1.00</td> <!-- No Sammendrag -->
   <td class="no la">2.22 ± 1.46 / 34.78 ± 0.95</td> <!-- ScaLA-nb -->
   <td class="no la">2.52 ± 2.47 / 35.88 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">30.90 ± 4.69 / 59.06 ± 4.25</td> <!-- NorQuAD -->
   <td class="no know">25.07 ± 1.40 / 43.36 ± 1.08</td> <!-- MMLU-no -->
   <td class="no reason">5.95 ± 3.42 / 28.33 ± 2.16</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.45 ± 2.98 / 39.71 ± 4.87</td> <!-- SUC3 -->
   <td class="sv sent">80.20 ± 0.57 / 80.03 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">3.78 ± 1.59 / 34.07 ± 0.58</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.21 ± 0.90 / 64.03 ± 0.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.73 ± 0.31 / 18.27 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">30.93 ± 0.91 / 47.69 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">10.56 ± 1.77 / 30.48 ± 1.46</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">37.97 ± 1.76</td> <!-- ScandEval score -->
   <td class="da-score">38.51 ± 1.98</td> <!-- Danish score -->
   <td class="no-score">34.63 ± 1.69</td> <!-- Norwegian score -->
   <td class="sv-score">40.76 ± 1.60</td> <!-- Swedish score -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.42 ± 2.35 / 58.76 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="da summ">66.59 ± 0.34 / 21.45 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">45.07 ± 1.34 / 58.18 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.36 ± 2.19 / 55.82 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.85 ± 1.19 / 35.26 ± 1.24</td> <!-- HellaSwag-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no summ">63.31 ± 0.56 / 15.33 ± 0.67</td> <!-- No Sammendrag -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.31 ± 3.13 / 63.71 ± 2.98</td> <!-- NorQuAD -->
   <td class="no know">20.44 ± 1.03 / 39.51 ± 0.72</td> <!-- MMLU-no -->
   <td class="no reason">15.87 ± 1.29 / 35.89 ± 1.06</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.05 ± 1.44 / 59.27 ± 1.12</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.91 ± 0.43 / 18.85 ± 0.26</td> <!-- SweDN -->
   <td class="sv know">24.03 ± 1.09 / 42.32 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">15.37 ± 0.71 / 35.78 ± 0.69</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,019 ± 480 / 1,048 ± 317</td> <!-- Model inference speed -->
   <td class="score">37.72 ± 2.50</td> <!-- ScandEval score -->
   <td class="da-score">43.20 ± 2.75</td> <!-- Danish score -->
   <td class="no-score">29.29 ± 2.69</td> <!-- Norwegian score -->
   <td class="sv-score">40.66 ± 2.06</td> <!-- Swedish score -->
   <td class="da ner">38.31 ± 2.59 / 27.23 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">37.13 ± 2.26 / 44.00 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">26.46 ± 5.28 / 53.12 ± 6.51</td> <!-- ScaLA-da -->
   <td class="da qa">39.77 ± 4.66 / 44.54 ± 5.00</td> <!-- ScandiQA-da -->
   <td class="da summ">62.96 ± 0.57 / 16.35 ± 0.33</td> <!-- Nordjylland-News -->
   <td class="da know">77.60 ± 1.36 / 82.98 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">67.85 ± 1.25 / 77.93 ± 0.90</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.06 ± 2.56 / 42.93 ± 2.25</td> <!-- HellaSwag-da -->
   <td class="no ner">46.32 ± 3.74 / 34.02 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">48.20 ± 1.59 / 35.05 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">20.46 ± 5.98 / 36.24 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">58.74 ± 0.83 / 11.67 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">4.50 ± 4.17 / 35.29 ± 2.89</td> <!-- ScaLA-nb -->
   <td class="no la">1.10 ± 1.47 / 34.51 ± 1.24</td> <!-- ScaLA-nn -->
   <td class="no qa">31.16 ± 1.83 / 52.35 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">28.98 ± 1.16 / 46.10 ± 0.95</td> <!-- MMLU-no -->
   <td class="no reason">15.62 ± 3.56 / 35.78 ± 2.81</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.55 ± 2.39 / 27.89 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">78.79 ± 0.91 / 75.25 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">15.77 ± 1.64 / 54.44 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.62 ± 4.78 / 45.18 ± 4.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.17 ± 0.81 / 16.98 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">30.96 ± 1.12 / 47.90 ± 0.94</td> <!-- MMLU-sv -->
   <td class="sv reason">18.79 ± 2.75 / 38.32 ± 2.26</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="score">36.93 ± 1.69</td> <!-- ScandEval score -->
   <td class="da-score">39.44 ± 1.71</td> <!-- Danish score -->
   <td class="no-score">32.11 ± 1.69</td> <!-- Norwegian score -->
   <td class="sv-score">39.23 ± 1.67</td> <!-- Swedish score -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">46.93 ± 1.12 / 55.22 ± 1.34</td> <!-- ScandiQA-da -->
   <td class="da summ">66.66 ± 0.32 / 20.59 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">41.77 ± 1.71 / 55.65 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">35.86 ± 2.28 / 52.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.59 ± 1.75 / 32.81 ± 1.55</td> <!-- HellaSwag-da -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no summ">63.93 ± 0.31 / 15.55 ± 0.57</td> <!-- No Sammendrag -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">25.79 ± 1.43 / 50.84 ± 1.80</td> <!-- NorQuAD -->
   <td class="no know">17.08 ± 1.29 / 37.00 ± 1.04</td> <!-- MMLU-no -->
   <td class="no reason">10.52 ± 2.25 / 31.85 ± 1.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.44 ± 1.45 / 57.11 ± 1.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.03 ± 0.09 / 18.17 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">22.36 ± 1.17 / 41.14 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">12.52 ± 1.41 / 33.90 ± 1.11</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">35.14 ± 1.58</td> <!-- ScandEval score -->
   <td class="da-score">36.74 ± 1.47</td> <!-- Danish score -->
   <td class="no-score">31.11 ± 1.75</td> <!-- Norwegian score -->
   <td class="sv-score">37.56 ± 1.51</td> <!-- Swedish score -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.00 ± 0.79 / 61.31 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">66.86 ± 0.31 / 20.92 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">32.17 ± 2.28 / 46.67 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">35.74 ± 2.46 / 55.18 ± 1.81</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.32 ± 0.41 / 32.24 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no summ">64.39 ± 0.40 / 16.25 ± 0.69</td> <!-- No Sammendrag -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.76 ± 2.07 / 61.97 ± 2.31</td> <!-- NorQuAD -->
   <td class="no know">14.81 ± 0.79 / 34.79 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">12.69 ± 0.77 / 31.84 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.07 ± 0.84 / 60.93 ± 0.80</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.64 ± 0.07 / 18.92 ± 0.15</td> <!-- SweDN -->
   <td class="sv know">17.73 ± 0.98 / 37.55 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">12.85 ± 0.93 / 33.37 ± 0.90</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="score">34.57 ± 1.66</td> <!-- ScandEval score -->
   <td class="da-score">30.05 ± 1.73</td> <!-- Danish score -->
   <td class="no-score">32.59 ± 1.88</td> <!-- Norwegian score -->
   <td class="sv-score">41.07 ± 1.37</td> <!-- Swedish score -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da qa">55.00 ± 0.85 / 60.83 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">65.05 ± 0.64 / 19.91 ± 0.90</td> <!-- Nordjylland-News -->
   <td class="da know">34.07 ± 2.13 / 50.17 ± 1.60</td> <!-- Danske Talemaader -->
   <td class="da know">33.75 ± 2.28 / 54.22 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.61 ± 1.51 / 34.38 ± 1.20</td> <!-- HellaSwag-da -->
   <td class="no ner">43.44 ± 1.89 / 33.41 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">46.33 ± 3.12 / 34.05 ± 2.27</td> <!-- NorNE-nn -->
   <td class="no sent">38.96 ± 2.34 / 56.27 ± 3.65</td> <!-- NoReC -->
   <td class="no summ">63.40 ± 0.66 / 15.77 ± 0.82</td> <!-- No Sammendrag -->
   <td class="no la">0.75 ± 1.07 / 33.42 ± 0.29</td> <!-- ScaLA-nb -->
   <td class="no la">1.04 ± 1.93 / 33.14 ± 0.66</td> <!-- ScaLA-nn -->
   <td class="no qa">40.33 ± 3.57 / 62.91 ± 3.37</td> <!-- NorQuAD -->
   <td class="no know">23.14 ± 0.98 / 41.88 ± 0.80</td> <!-- MMLU-no -->
   <td class="no reason">16.50 ± 1.60 / 36.98 ± 1.27</td> <!-- HellaSwag-no -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv qa">55.05 ± 0.85 / 60.85 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.95 ± 0.62 / 17.89 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">25.28 ± 0.72 / 43.71 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">19.20 ± 1.18 / 38.76 ± 0.96</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="score">33.99 ± 2.83</td> <!-- ScandEval score -->
   <td class="da-score">35.52 ± 2.87</td> <!-- Danish score -->
   <td class="no-score">28.78 ± 2.92</td> <!-- Norwegian score -->
   <td class="sv-score">37.66 ± 2.69</td> <!-- Swedish score -->
   <td class="da ner">30.16 ± 4.47 / 25.03 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">48.49 ± 2.41 / 63.06 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">5.52 ± 4.66 / 38.81 ± 4.27</td> <!-- ScaLA-da -->
   <td class="da qa">52.44 ± 1.32 / 57.22 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="da summ">65.67 ± 0.65 / 19.75 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">43.57 ± 3.32 / 56.56 ± 2.69</td> <!-- Danske Talemaader -->
   <td class="da know">35.60 ± 4.28 / 50.86 ± 3.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.76 ± 2.77 / 28.91 ± 2.38</td> <!-- HellaSwag-da -->
   <td class="no ner">35.98 ± 3.79 / 27.51 ± 2.13</td> <!-- NorNE-nb -->
   <td class="no ner">47.39 ± 2.31 / 36.42 ± 2.87</td> <!-- NorNE-nn -->
   <td class="no sent">38.98 ± 5.51 / 58.23 ± 4.01</td> <!-- NoReC -->
   <td class="no summ">61.99 ± 0.85 / 14.07 ± 0.75</td> <!-- No Sammendrag -->
   <td class="no la">11.54 ± 5.04 / 49.91 ± 3.96</td> <!-- ScaLA-nb -->
   <td class="no la">5.20 ± 3.47 / 46.19 ± 5.23</td> <!-- ScaLA-nn -->
   <td class="no qa">37.54 ± 3.00 / 56.56 ± 2.96</td> <!-- NorQuAD -->
   <td class="no know">10.40 ± 2.03 / 29.84 ± 1.34</td> <!-- MMLU-no -->
   <td class="no reason">2.52 ± 1.76 / 24.84 ± 1.48</td> <!-- HellaSwag-no -->
   <td class="sv ner">32.37 ± 3.05 / 24.60 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">75.33 ± 2.41 / 77.99 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">12.73 ± 6.32 / 45.51 ± 7.43</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.05 ± 1.83 / 58.32 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.74 ± 0.74 / 19.59 ± 0.87</td> <!-- SweDN -->
   <td class="sv know">15.60 ± 1.96 / 33.16 ± 1.77</td> <!-- MMLU-sv -->
   <td class="sv reason">9.81 ± 2.55 / 28.12 ± 2.70</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">32.17 ± 1.82</td> <!-- ScandEval score -->
   <td class="da-score">31.97 ± 1.65</td> <!-- Danish score -->
   <td class="no-score">27.01 ± 1.69</td> <!-- Norwegian score -->
   <td class="sv-score">37.52 ± 2.13</td> <!-- Swedish score -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">45.42 ± 1.92 / 51.05 ± 2.05</td> <!-- ScandiQA-da -->
   <td class="da summ">66.53 ± 0.26 / 21.74 ± 0.32</td> <!-- Nordjylland-News -->
   <td class="da know">20.18 ± 1.80 / 38.69 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">35.69 ± 2.31 / 57.05 ± 1.60</td> <!-- Danish Citizen Tests -->
   <td class="da reason">7.93 ± 1.49 / 29.76 ± 0.92</td> <!-- HellaSwag-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no summ">64.71 ± 0.87 / 18.26 ± 1.15</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">18.67 ± 2.60 / 36.99 ± 2.72</td> <!-- NorQuAD -->
   <td class="no know">14.48 ± 1.33 / 35.35 ± 0.94</td> <!-- MMLU-no -->
   <td class="no reason">6.49 ± 1.39 / 28.64 ± 0.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.42 ± 4.19 / 49.62 ± 4.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.31 ± 0.31 / 18.96 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">15.65 ± 0.55 / 36.32 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">8.74 ± 1.34 / 29.87 ± 1.40</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10=</td> <!-- Rank -->
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="score">29.12 ± 2.04</td> <!-- ScandEval score -->
   <td class="da-score">28.33 ± 1.84</td> <!-- Danish score -->
   <td class="no-score">25.27 ± 2.24</td> <!-- Norwegian score -->
   <td class="sv-score">33.77 ± 2.03</td> <!-- Swedish score -->
   <td class="da ner">37.80 ± 2.75 / 24.74 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">40.51 ± 1.75 / 55.84 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">3.35 ± 1.84 / 44.60 ± 4.67</td> <!-- ScaLA-da -->
   <td class="da qa">49.08 ± 1.74 / 55.58 ± 1.57</td> <!-- ScandiQA-da -->
   <td class="da summ">65.80 ± 1.29 / 21.65 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">-0.90 ± 1.63 / 23.10 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">3.61 ± 2.89 / 35.10 ± 1.82</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.40 ± 1.28 / 25.12 ± 0.72</td> <!-- HellaSwag-da -->
   <td class="no ner">42.29 ± 4.36 / 31.45 ± 1.88</td> <!-- NorNE-nb -->
   <td class="no ner">46.29 ± 3.44 / 35.99 ± 4.20</td> <!-- NorNE-nn -->
   <td class="no sent">27.05 ± 3.33 / 45.30 ± 3.46</td> <!-- NoReC -->
   <td class="no summ">62.81 ± 1.69 / 17.08 ± 1.49</td> <!-- No Sammendrag -->
   <td class="no la">1.63 ± 2.58 / 38.29 ± 4.05</td> <!-- ScaLA-nb -->
   <td class="no la">2.57 ± 1.78 / 40.92 ± 4.00</td> <!-- ScaLA-nn -->
   <td class="no qa">39.18 ± 2.84 / 61.85 ± 3.07</td> <!-- NorQuAD -->
   <td class="no know">1.50 ± 0.72 / 23.00 ± 0.61</td> <!-- MMLU-no -->
   <td class="no reason">-0.05 ± 1.05 / 25.00 ± 0.83</td> <!-- HellaSwag-no -->
   <td class="sv ner">48.78 ± 5.08 / 26.81 ± 3.42</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 1.23 / 74.78 ± 1.97</td> <!-- SweReC -->
   <td class="sv la">2.53 ± 2.80 / 47.37 ± 2.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.93 ± 0.97 / 55.09 ± 0.85</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.49 ± 2.27 / 16.17 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">1.28 ± 1.28 / 23.12 ± 0.63</td> <!-- MMLU-sv -->
   <td class="sv reason">1.27 ± 0.61 / 25.74 ± 0.70</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="score">27.03 ± 2.34</td> <!-- ScandEval score -->
   <td class="da-score">24.66 ± 2.29</td> <!-- Danish score -->
   <td class="no-score">24.36 ± 2.66</td> <!-- Norwegian score -->
   <td class="sv-score">32.07 ± 2.06</td> <!-- Swedish score -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da qa">39.18 ± 3.52 / 44.53 ± 3.79</td> <!-- ScandiQA-da -->
   <td class="da summ">66.28 ± 0.55 / 20.87 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">6.34 ± 2.61 / 28.14 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">18.00 ± 3.09 / 45.08 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.57 ± 0.93 / 28.66 ± 0.66</td> <!-- HellaSwag-da -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no summ">63.58 ± 1.06 / 16.52 ± 1.39</td> <!-- No Sammendrag -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no qa">24.67 ± 2.82 / 43.02 ± 4.03</td> <!-- NorQuAD -->
   <td class="no know">3.03 ± 1.30 / 25.60 ± 0.86</td> <!-- MMLU-no -->
   <td class="no reason">5.57 ± 1.19 / 27.61 ± 0.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.78 ± 4.94 / 41.08 ± 5.23</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.08 ± 0.64 / 17.89 ± 0.48</td> <!-- SweDN -->
   <td class="sv know">5.23 ± 1.02 / 28.63 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">5.39 ± 0.81 / 28.86 ± 0.60</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="score">26.81 ± 1.85</td> <!-- ScandEval score -->
   <td class="da-score">25.04 ± 1.88</td> <!-- Danish score -->
   <td class="no-score">25.85 ± 2.09</td> <!-- Norwegian score -->
   <td class="sv-score">29.53 ± 1.57</td> <!-- Swedish score -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da qa">44.04 ± 2.07 / 51.91 ± 2.08</td> <!-- ScandiQA-da -->
   <td class="da summ">67.12 ± 0.48 / 22.61 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">30.90 ± 3.84 / 43.86 ± 4.18</td> <!-- Danske Talemaader -->
   <td class="da know">16.81 ± 3.84 / 42.03 ± 2.42</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.08 ± 1.35 / 32.13 ± 1.04</td> <!-- HellaSwag-da -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no summ">64.83 ± 0.60 / 18.37 ± 0.66</td> <!-- No Sammendrag -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">31.39 ± 2.33 / 52.78 ± 3.03</td> <!-- NorQuAD -->
   <td class="no know">6.89 ± 1.56 / 27.44 ± 1.06</td> <!-- MMLU-no -->
   <td class="no reason">12.81 ± 0.66 / 32.38 ± 0.61</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.72 ± 2.66 / 50.17 ± 3.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.86 ± 0.15 / 19.08 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">6.16 ± 0.81 / 28.35 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">10.90 ± 0.86 / 32.01 ± 0.54</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="score">22.77 ± 2.30</td> <!-- ScandEval score -->
   <td class="da-score">21.41 ± 2.26</td> <!-- Danish score -->
   <td class="no-score">20.04 ± 2.77</td> <!-- Norwegian score -->
   <td class="sv-score">26.85 ± 1.86</td> <!-- Swedish score -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da qa">45.31 ± 0.88 / 51.56 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">63.77 ± 1.09 / 17.31 ± 1.38</td> <!-- Nordjylland-News -->
   <td class="da know">-1.31 ± 1.31 / 24.58 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">3.02 ± 3.77 / 36.58 ± 2.16</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.33 ± 1.17 / 24.65 ± 0.48</td> <!-- HellaSwag-da -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no summ">61.24 ± 0.98 / 13.30 ± 0.99</td> <!-- No Sammendrag -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">34.90 ± 2.66 / 54.29 ± 2.94</td> <!-- NorQuAD -->
   <td class="no know">-0.01 ± 0.86 / 24.32 ± 0.81</td> <!-- MMLU-no -->
   <td class="no reason">0.25 ± 0.94 / 25.10 ± 0.81</td> <!-- HellaSwag-no -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.53 ± 0.83 / 51.66 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.90 ± 1.33 / 16.54 ± 0.71</td> <!-- SweDN -->
   <td class="sv know">2.20 ± 0.88 / 25.62 ± 0.86</td> <!-- MMLU-sv -->
   <td class="sv reason">0.67 ± 1.39 / 25.25 ± 0.51</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11=</td> <!-- Rank -->
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="score">22.63 ± 2.15</td> <!-- ScandEval score -->
   <td class="da-score">22.62 ± 1.89</td> <!-- Danish score -->
   <td class="no-score">19.48 ± 2.14</td> <!-- Norwegian score -->
   <td class="sv-score">25.78 ± 2.44</td> <!-- Swedish score -->
   <td class="da ner">14.88 ± 3.92 / 14.02 ± 2.63</td> <!-- DANSK -->
   <td class="da sent">34.66 ± 1.82 / 46.40 ± 1.53</td> <!-- Angry Tweets -->
   <td class="da la">0.29 ± 1.86 / 41.01 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da qa">42.16 ± 0.88 / 47.49 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="da summ">64.09 ± 1.10 / 18.29 ± 1.30</td> <!-- Nordjylland-News -->
   <td class="da know">0.58 ± 1.06 / 23.87 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">4.60 ± 3.52 / 37.09 ± 1.52</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.34 ± 1.37 / 24.79 ± 0.73</td> <!-- HellaSwag-da -->
   <td class="no ner">14.58 ± 6.07 / 15.44 ± 5.52</td> <!-- NorNE-nb -->
   <td class="no ner">21.06 ± 7.77 / 21.99 ± 7.14</td> <!-- NorNE-nn -->
   <td class="no sent">32.02 ± 1.59 / 36.85 ± 2.01</td> <!-- NoReC -->
   <td class="no summ">61.58 ± 1.46 / 13.96 ± 1.66</td> <!-- No Sammendrag -->
   <td class="no la">1.49 ± 1.40 / 35.35 ± 1.51</td> <!-- ScaLA-nb -->
   <td class="no la">0.98 ± 1.85 / 35.28 ± 2.43</td> <!-- ScaLA-nn -->
   <td class="no qa">22.87 ± 1.85 / 38.93 ± 2.59</td> <!-- NorQuAD -->
   <td class="no know">0.99 ± 0.62 / 24.00 ± 0.70</td> <!-- MMLU-no -->
   <td class="no reason">-0.16 ± 0.90 / 24.84 ± 0.71</td> <!-- HellaSwag-no -->
   <td class="sv ner">13.79 ± 8.46 / 14.43 ± 7.23</td> <!-- SUC3 -->
   <td class="sv sent">71.59 ± 2.78 / 59.82 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">-0.89 ± 1.22 / 43.82 ± 3.45</td> <!-- ScaLA-sv -->
   <td class="sv qa">38.33 ± 1.79 / 44.00 ± 1.70</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.54 ± 0.58 / 15.68 ± 0.49</td> <!-- SweDN -->
   <td class="sv know">-0.39 ± 1.21 / 22.30 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.52 ± 1.01 / 25.20 ± 0.85</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="score">21.69 ± 2.21</td> <!-- ScandEval score -->
   <td class="da-score">21.85 ± 2.12</td> <!-- Danish score -->
   <td class="no-score">20.42 ± 1.90</td> <!-- Norwegian score -->
   <td class="sv-score">22.81 ± 2.61</td> <!-- Swedish score -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da qa">38.57 ± 0.65 / 47.40 ± 0.63</td> <!-- ScandiQA-da -->
   <td class="da summ">64.15 ± 0.49 / 17.81 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">4.49 ± 1.44 / 27.32 ± 0.89</td> <!-- Danske Talemaader -->
   <td class="da know">12.81 ± 4.57 / 37.83 ± 2.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.68 ± 1.31 / 25.00 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">23.82 ± 4.25 / 22.08 ± 2.50</td> <!-- NorNE-nb -->
   <td class="no ner">26.04 ± 6.38 / 24.47 ± 3.69</td> <!-- NorNE-nn -->
   <td class="no sent">32.60 ± 1.84 / 47.47 ± 3.33</td> <!-- NoReC -->
   <td class="no summ">58.76 ± 0.62 / 12.29 ± 0.77</td> <!-- No Sammendrag -->
   <td class="no la">0.34 ± 1.43 / 44.47 ± 2.44</td> <!-- ScaLA-nb -->
   <td class="no la">2.26 ± 2.27 / 45.41 ± 3.25</td> <!-- ScaLA-nn -->
   <td class="no qa">21.34 ± 0.98 / 42.76 ± 1.06</td> <!-- NorQuAD -->
   <td class="no know">2.13 ± 1.32 / 26.30 ± 1.12</td> <!-- MMLU-no -->
   <td class="no reason">1.87 ± 1.34 / 25.87 ± 0.75</td> <!-- HellaSwag-no -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv qa">37.22 ± 1.08 / 46.81 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">47.50 ± 0.37 / 13.19 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">-0.03 ± 1.31 / 23.73 ± 1.11</td> <!-- MMLU-sv -->
   <td class="sv reason">0.02 ± 0.88 / 25.04 ± 0.61</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="score">20.60 ± 2.38</td> <!-- ScandEval score -->
   <td class="da-score">20.61 ± 2.08</td> <!-- Danish score -->
   <td class="no-score">20.16 ± 1.95</td> <!-- Norwegian score -->
   <td class="sv-score">21.02 ± 3.11</td> <!-- Swedish score -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da qa">34.81 ± 1.50 / 39.69 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="da summ">60.53 ± 1.84 / 14.21 ± 1.66</td> <!-- Nordjylland-News -->
   <td class="da know">1.00 ± 1.72 / 23.91 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">4.85 ± 3.16 / 36.78 ± 1.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.28 ± 0.38 / 25.19 ± 0.78</td> <!-- HellaSwag-da -->
   <td class="no ner">27.37 ± 4.07 / 27.94 ± 4.04</td> <!-- NorNE-nb -->
   <td class="no ner">31.22 ± 3.87 / 31.39 ± 3.99</td> <!-- NorNE-nn -->
   <td class="no sent">34.21 ± 1.63 / 47.17 ± 2.76</td> <!-- NoReC -->
   <td class="no summ">57.57 ± 0.95 / 10.19 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">0.92 ± 1.55 / 40.71 ± 2.58</td> <!-- ScaLA-nb -->
   <td class="no la">1.25 ± 2.30 / 43.49 ± 3.20</td> <!-- ScaLA-nn -->
   <td class="no qa">18.54 ± 2.77 / 32.10 ± 4.22</td> <!-- NorQuAD -->
   <td class="no know">0.33 ± 1.29 / 22.37 ± 1.03</td> <!-- MMLU-no -->
   <td class="no reason">0.11 ± 1.10 / 24.94 ± 0.94</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">33.71 ± 1.47 / 38.82 ± 1.55</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.46 ± 1.68 / 13.65 ± 0.53</td> <!-- SweDN -->
   <td class="sv know">-0.96 ± 1.08 / 21.85 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.30 ± 0.48 / 25.10 ± 0.69</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="score">20.10 ± 2.43</td> <!-- ScandEval score -->
   <td class="da-score">21.42 ± 2.00</td> <!-- Danish score -->
   <td class="no-score">17.93 ± 1.76</td> <!-- Norwegian score -->
   <td class="sv-score">20.95 ± 3.52</td> <!-- Swedish score -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da qa">18.78 ± 3.89 / 24.10 ± 4.26</td> <!-- ScandiQA-da -->
   <td class="da summ">65.74 ± 0.29 / 19.05 ± 0.64</td> <!-- Nordjylland-News -->
   <td class="da know">6.27 ± 1.52 / 27.63 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">6.25 ± 3.25 / 37.75 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.11 ± 1.44 / 26.00 ± 0.86</td> <!-- HellaSwag-da -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no summ">60.72 ± 0.76 / 10.83 ± 0.72</td> <!-- No Sammendrag -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 0.33 / 17.89 ± 1.64</td> <!-- NorQuAD -->
   <td class="no know">3.21 ± 0.87 / 27.07 ± 0.74</td> <!-- MMLU-no -->
   <td class="no reason">0.18 ± 1.02 / 25.00 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">15.08 ± 3.85 / 19.72 ± 4.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.65 ± 0.26 / 11.86 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">0.14 ± 1.02 / 24.76 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.83 / 25.53 ± 0.62</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">18.23 ± 2.13</td> <!-- ScandEval score -->
   <td class="da-score">15.38 ± 2.22</td> <!-- Danish score -->
   <td class="no-score">16.92 ± 1.44</td> <!-- Norwegian score -->
   <td class="sv-score">22.38 ± 2.73</td> <!-- Swedish score -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.21 ± 3.93 / 29.03 ± 4.17</td> <!-- ScandiQA-da -->
   <td class="da summ">60.03 ± 0.65 / 12.94 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">0.10 ± 1.50 / 26.50 ± 1.00</td> <!-- Danske Talemaader -->
   <td class="da know">4.29 ± 5.87 / 35.00 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 1.17 / 24.43 ± 0.74</td> <!-- HellaSwag-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no summ">60.08 ± 1.33 / 12.33 ± 0.95</td> <!-- No Sammendrag -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.79 ± 1.65 / 50.19 ± 1.83</td> <!-- NorQuAD -->
   <td class="no know">0.21 ± 0.83 / 26.88 ± 1.44</td> <!-- MMLU-no -->
   <td class="no reason">-0.30 ± 1.13 / 24.48 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.37 ± 1.37 / 50.18 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.49 ± 0.54 / 14.60 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">1.12 ± 0.42 / 25.27 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.91 ± 0.96 / 24.26 ± 0.64</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">13</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="score">16.90 ± 3.08</td> <!-- ScandEval score -->
   <td class="da-score">16.90 ± 2.30</td> <!-- Danish score -->
   <td class="no-score">15.07 ± 2.66</td> <!-- Norwegian score -->
   <td class="sv-score">18.73 ± 4.28</td> <!-- Swedish score -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">14.16 ± 1.82 / 19.24 ± 1.85</td> <!-- ScandiQA-da -->
   <td class="da summ">63.76 ± 0.90 / 17.20 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">-2.76 ± 1.71 / 22.41 ± 1.17</td> <!-- Danske Talemaader -->
   <td class="da know">5.08 ± 2.61 / 35.14 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.70 ± 0.94 / 24.83 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">58.73 ± 1.67 / 10.49 ± 1.17</td> <!-- No Sammendrag -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no qa">2.15 ± 0.46 / 10.01 ± 1.47</td> <!-- NorQuAD -->
   <td class="no know">-0.50 ± 1.10 / 23.75 ± 0.96</td> <!-- MMLU-no -->
   <td class="no reason">0.07 ± 1.21 / 25.26 ± 0.95</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">21.56 ± 3.80 / 26.32 ± 4.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.33 ± 0.73 / 13.25 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">-0.85 ± 1.05 / 24.38 ± 0.51</td> <!-- MMLU-sv -->
   <td class="sv reason">-1.24 ± 0.90 / 24.30 ± 0.63</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">14</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="score">11.82 ± 2.89</td> <!-- ScandEval score -->
   <td class="da-score">13.35 ± 2.57</td> <!-- Danish score -->
   <td class="no-score">11.29 ± 2.27</td> <!-- Norwegian score -->
   <td class="sv-score">10.82 ± 3.83</td> <!-- Swedish score -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da qa">6.82 ± 6.80 / 21.29 ± 6.25</td> <!-- ScandiQA-da -->
   <td class="da summ">58.94 ± 0.40 / 15.76 ± 0.66</td> <!-- Nordjylland-News -->
   <td class="da know">-1.83 ± 1.68 / 23.94 ± 1.25</td> <!-- Danske Talemaader -->
   <td class="da know">0.99 ± 3.76 / 34.10 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.48 ± 0.94 / 24.73 ± 0.61</td> <!-- HellaSwag-da -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">20.84 ± 6.06 / 35.78 ± 5.94</td> <!-- NoReC -->
   <td class="no summ">49.57 ± 0.81 / 9.47 ± 0.48</td> <!-- No Sammendrag -->
   <td class="no la">0.45 ± 1.09 / 34.65 ± 1.93</td> <!-- ScaLA-nb -->
   <td class="no la">0.48 ± 0.66 / 32.86 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">2.45 ± 0.61 / 22.80 ± 2.27</td> <!-- NorQuAD -->
   <td class="no know">0.17 ± 1.46 / 24.43 ± 1.54</td> <!-- MMLU-no -->
   <td class="no reason">-0.49 ± 0.65 / 24.19 ± 0.56</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.79 ± 11.20 / 31.10 ± 8.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">29.95 ± 0.23 / 8.33 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">-0.67 ± 0.81 / 22.55 ± 0.71</td> <!-- MMLU-sv -->
   <td class="sv reason">0.86 ± 0.82 / 25.38 ± 0.51</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">15=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">11.03 ± 0.85</td> <!-- ScandEval score -->
   <td class="da-score">10.76 ± 0.65</td> <!-- Danish score -->
   <td class="no-score">8.79 ± 0.25</td> <!-- Norwegian score -->
   <td class="sv-score">13.54 ± 1.64</td> <!-- Swedish score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 12.40 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">62.29 ± 0.25 / 14.50 ± 0.42</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 0.14 / 25.18 ± 0.77</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">0.95 ± 0.80 / 9.68 ± 0.28</td> <!-- NoReC -->
   <td class="no summ">60.13 ± 0.23 / 11.12 ± 0.20</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 33.55 ± 0.25</td> <!-- NorQuAD -->
   <td class="no know">0.18 ± 0.35 / 21.91 ± 0.52</td> <!-- MMLU-no -->
   <td class="no reason">0.30 ± 0.40 / 25.03 ± 0.88</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 8.95 ± 2.92</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.30 ± 0.04 / 12.23 ± 0.07</td> <!-- SweDN -->
   <td class="sv know">-0.25 ± 0.97 / 21.96 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">0.08 ± 0.78 / 24.93 ± 0.77</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">15=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="score">10.78 ± 2.28</td> <!-- ScandEval score -->
   <td class="da-score">11.22 ± 2.04</td> <!-- Danish score -->
   <td class="no-score">10.36 ± 2.06</td> <!-- Norwegian score -->
   <td class="sv-score">10.77 ± 2.75</td> <!-- Swedish score -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da qa">7.70 ± 0.67 / 10.40 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">57.45 ± 1.32 / 12.05 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">-0.58 ± 0.97 / 24.00 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">5.18 ± 4.75 / 36.68 ± 2.20</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.28 ± 0.99 / 24.75 ± 0.93</td> <!-- HellaSwag-da -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no summ">55.00 ± 1.43 / 9.00 ± 0.65</td> <!-- No Sammendrag -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no qa">0.90 ± 0.23 / 4.99 ± 1.08</td> <!-- NorQuAD -->
   <td class="no know">0.39 ± 1.28 / 23.22 ± 0.56</td> <!-- MMLU-no -->
   <td class="no reason">-0.80 ± 0.71 / 24.77 ± 0.62</td> <!-- HellaSwag-no -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">7.64 ± 2.58 / 9.62 ± 3.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.07 ± 1.04 / 13.34 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.60 / 22.53 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">1.17 ± 0.86 / 25.54 ± 0.87</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">15=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="score">10.28 ± 0.98</td> <!-- ScandEval score -->
   <td class="da-score">9.53 ± 0.52</td> <!-- Danish score -->
   <td class="no-score">8.76 ± 0.39</td> <!-- Norwegian score -->
   <td class="sv-score">12.57 ± 2.03</td> <!-- Swedish score -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.81 ± 2.69 / 19.31 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">0.00 ± 0.00 / 30.05 ± 4.99</td> <!-- ScandiQA-da -->
   <td class="da summ">61.75 ± 0.28 / 13.92 ± 0.40</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.15 ± 0.64 / 25.21 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">1.27 ± 1.21 / 9.77 ± 0.51</td> <!-- NoReC -->
   <td class="no summ">59.10 ± 0.13 / 9.14 ± 0.12</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.25 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.00 ± 0.00 / 32.79 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 32.25 ± 0.29</td> <!-- NorQuAD -->
   <td class="no know">0.83 ± 0.90 / 21.96 ± 0.50</td> <!-- MMLU-no -->
   <td class="no reason">0.09 ± 0.50 / 25.03 ± 0.89</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.62 ± 12.67 / 35.36 ± 8.35</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.00 ± 0.00 / 19.59 ± 6.84</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.16 ± 0.06 / 8.83 ± 0.07</td> <!-- SweDN -->
   <td class="sv know">0.47 ± 0.86 / 22.03 ± 0.59</td> <!-- MMLU-sv -->
   <td class="sv reason">0.71 ± 0.64 / 25.02 ± 0.72</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="score">10.07 ± 2.42</td> <!-- ScandEval score -->
   <td class="da-score">10.81 ± 2.85</td> <!-- Danish score -->
   <td class="no-score">9.46 ± 1.55</td> <!-- Norwegian score -->
   <td class="sv-score">9.93 ± 2.86</td> <!-- Swedish score -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da qa">5.16 ± 6.60 / 17.34 ± 5.84</td> <!-- ScandiQA-da -->
   <td class="da summ">57.26 ± 0.88 / 14.33 ± 0.65</td> <!-- Nordjylland-News -->
   <td class="da know">-0.96 ± 1.47 / 23.86 ± 1.33</td> <!-- Danske Talemaader -->
   <td class="da know">3.51 ± 3.46 / 35.41 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.73 ± 1.39 / 25.54 ± 1.00</td> <!-- HellaSwag-da -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">20.64 ± 5.63 / 36.75 ± 3.29</td> <!-- NoReC -->
   <td class="no summ">44.80 ± 1.54 / 8.15 ± 0.74</td> <!-- No Sammendrag -->
   <td class="no la">-0.99 ± 0.88 / 33.37 ± 0.27</td> <!-- ScaLA-nb -->
   <td class="no la">-0.15 ± 0.72 / 32.83 ± 0.34</td> <!-- ScaLA-nn -->
   <td class="no qa">0.55 ± 0.32 / 22.10 ± 2.28</td> <!-- NorQuAD -->
   <td class="no know">0.63 ± 1.48 / 24.41 ± 1.24</td> <!-- MMLU-no -->
   <td class="no reason">-0.09 ± 0.80 / 24.42 ± 0.74</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv qa">4.82 ± 3.58 / 18.08 ± 2.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">30.78 ± 0.33 / 8.47 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">-0.11 ± 1.16 / 23.32 ± 0.92</td> <!-- MMLU-sv -->
   <td class="sv reason">0.56 ± 1.22 / 24.79 ± 0.91</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">17=</td> <!-- Rank -->
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="score">7.35 ± 1.01</td> <!-- ScandEval score -->
   <td class="da-score">8.08 ± 1.14</td> <!-- Danish score -->
   <td class="no-score">6.79 ± 0.91</td> <!-- Norwegian score -->
   <td class="sv-score">7.19 ± 0.99</td> <!-- Swedish score -->
   <td class="da ner">0.64 ± 0.89 / 0.52 ± 0.69</td> <!-- DANSK -->
   <td class="da sent">-0.52 ± 1.72 / 28.55 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">-0.02 ± 1.55 / 36.82 ± 2.52</td> <!-- ScaLA-da -->
   <td class="da qa">0.48 ± 0.27 / 2.89 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="da summ">53.42 ± 0.61 / 8.22 ± 0.19</td> <!-- Nordjylland-News -->
   <td class="da know">0.90 ± 0.92 / 26.20 ± 1.02</td> <!-- Danske Talemaader -->
   <td class="da know">4.10 ± 2.68 / 33.71 ± 1.88</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 1.16 / 25.21 ± 0.48</td> <!-- HellaSwag-da -->
   <td class="no ner">0.29 ± 0.29 / 0.29 ± 0.27</td> <!-- NorNE-nb -->
   <td class="no ner">0.25 ± 0.17 / 0.27 ± 0.21</td> <!-- NorNE-nn -->
   <td class="no sent">-1.43 ± 1.45 / 20.90 ± 4.96</td> <!-- NoReC -->
   <td class="no summ">47.11 ± 1.65 / 5.29 ± 0.39</td> <!-- No Sammendrag -->
   <td class="no la">-0.42 ± 1.10 / 35.77 ± 3.09</td> <!-- ScaLA-nb -->
   <td class="no la">1.11 ± 2.21 / 39.28 ± 4.12</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 3.15 ± 0.55</td> <!-- NorQuAD -->
   <td class="no know">0.69 ± 0.71 / 24.93 ± 0.99</td> <!-- MMLU-no -->
   <td class="no reason">0.55 ± 0.68 / 25.11 ± 0.43</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.26 ± 0.16 / 0.26 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">4.75 ± 2.54 / 27.85 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">-0.60 ± 1.56 / 40.53 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv qa">0.06 ± 0.09 / 1.07 ± 0.35</td> <!-- ScandiQA-sv -->
   <td class="sv summ">45.76 ± 0.36 / 8.16 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">-0.41 ± 1.39 / 24.48 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.81 / 25.32 ± 0.65</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">17=</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">5.61 ± 1.10</td> <!-- ScandEval score -->
   <td class="da-score">5.40 ± 1.55</td> <!-- Danish score -->
   <td class="no-score">5.51 ± 0.84</td> <!-- Norwegian score -->
   <td class="sv-score">5.93 ± 0.92</td> <!-- Swedish score -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da qa">2.00 ± 1.70 / 2.69 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="da summ">31.24 ± 1.02 / 1.76 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">-0.61 ± 0.54 / 24.71 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">6.94 ± 3.67 / 38.18 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.12 ± 0.87 / 24.71 ± 0.88</td> <!-- HellaSwag-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">4.76 ± 1.84 / 16.95 ± 5.07</td> <!-- NoReC -->
   <td class="no summ">33.33 ± 0.19 / 1.15 ± 0.06</td> <!-- No Sammendrag -->
   <td class="no la">0.67 ± 1.94 / 40.42 ± 4.43</td> <!-- ScaLA-nb -->
   <td class="no la">-0.88 ± 1.89 / 40.70 ± 4.30</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.73 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">0.72 ± 0.81 / 22.86 ± 0.63</td> <!-- MMLU-no -->
   <td class="no reason">-0.20 ± 1.06 / 24.94 ± 0.69</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv qa">6.24 ± 3.13 / 7.86 ± 3.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">34.81 ± 0.08 / 3.13 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.37 ± 1.08 / 22.43 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">0.36 ± 0.83 / 25.08 ± 0.77</td> <!-- HellaSwag-sv -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>