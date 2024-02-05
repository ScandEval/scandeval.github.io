---
layout: leaderboard
title: Mainland Scandinavian NLG
---

<center>Last updated: 05/02/2024 20:30:50 CET</center>

<div class="table-wrapper centered">

<input type="checkbox" id="merged-models-checkbox">
<label for="merged-models-checkbox">Include merged models</label>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">ARC-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian summarization - BERTScore / ROUGE-L">No Sammendrag</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact Match / F1-score">NorQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian knowledge - Matthews Correlation Coefficient / Accuracy">ARC-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-no</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact Match / F1-score">ScandiQA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish summarization - BERTScore / ROUGE-L">SweDN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish knowledge - Matthews Correlation Coefficient / Accuracy">ARC-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-sv</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">58.52 ± 2.42</td> <!-- ScandEval score -->
   <td class="da-score">56.72 ± 2.44</td> <!-- Danish score -->
   <td class="no-score">57.31 ± 2.37</td> <!-- Norwegian score -->
   <td class="sv-score">61.54 ± 2.46</td> <!-- Swedish score -->
   <td class="da ner">59.61 ± 2.65 / 47.73 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">50.54 ± 3.00 / 66.79 ± 1.87</td> <!-- Angry Tweets -->
   <td class="da la">57.57 ± 3.30 / 77.07 ± 1.91</td> <!-- ScaLA-da -->
   <td class="da qa">51.09 ± 1.97 / 59.01 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 0.29 / 18.43 ± 0.41</td> <!-- Nordjylland-News -->
   <td class="da know">39.74 ± 2.47 / 54.53 ± 1.94</td> <!-- MMLU-da -->
   <td class="da know">65.24 ± 2.71 / 73.59 ± 2.09</td> <!-- ARC-da -->
   <td class="da reason">59.36 ± 3.26 / 69.18 ± 2.51</td> <!-- HellaSwag-da -->
   <td class="no ner">77.70 ± 2.64 / 68.71 ± 2.97</td> <!-- NorNE-nb -->
   <td class="no ner">73.92 ± 2.53 / 67.96 ± 2.67</td> <!-- NorNE-nn -->
   <td class="no sent">58.88 ± 3.23 / 71.00 ± 2.87</td> <!-- NoReC -->
   <td class="no summ">64.35 ± 0.24 / 15.05 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">54.29 ± 4.27 / 73.02 ± 3.26</td> <!-- ScaLA-nb -->
   <td class="no la">32.82 ± 3.43 / 56.05 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">46.44 ± 1.55 / 72.64 ± 1.26</td> <!-- NorQuAD -->
   <td class="no know">40.26 ± 5.24 / 54.88 ± 3.85</td> <!-- MMLU-no -->
   <td class="no know">65.97 ± 1.75 / 74.38 ± 1.32</td> <!-- ARC-no -->
   <td class="no reason">59.02 ± 1.63 / 68.63 ± 1.34</td> <!-- HellaSwag-no -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv qa">57.59 ± 2.08 / 65.53 ± 1.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.66 ± 0.17 / 19.69 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">40.73 ± 3.36 / 55.16 ± 2.75</td> <!-- MMLU-sv -->
   <td class="sv know">63.58 ± 3.48 / 72.58 ± 2.64</td> <!-- ARC-sv -->
   <td class="sv reason">50.51 ± 2.33 / 62.07 ± 1.95</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="score">48.55 ± 2.60</td> <!-- ScandEval score -->
   <td class="da-score">47.78 ± 2.57</td> <!-- Danish score -->
   <td class="no-score">46.39 ± 2.65</td> <!-- Norwegian score -->
   <td class="sv-score">51.47 ± 2.59</td> <!-- Swedish score -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da qa">58.28 ± 2.00 / 64.34 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="da summ">68.44 ± 0.43 / 24.68 ± 0.67</td> <!-- Nordjylland-News -->
   <td class="da know">37.34 ± 1.71 / 52.50 ± 1.35</td> <!-- MMLU-da -->
   <td class="da know">66.59 ± 3.42 / 74.84 ± 2.52</td> <!-- ARC-da -->
   <td class="da reason">42.21 ± 3.40 / 56.48 ± 2.62</td> <!-- HellaSwag-da -->
   <td class="no ner">61.17 ± 3.56 / 54.24 ± 3.45</td> <!-- NorNE-nb -->
   <td class="no ner">65.44 ± 2.83 / 54.34 ± 3.95</td> <!-- NorNE-nn -->
   <td class="no sent">58.69 ± 3.28 / 70.83 ± 2.49</td> <!-- NoReC -->
   <td class="no summ">66.08 ± 0.32 / 20.15 ± 0.64</td> <!-- No Sammendrag -->
   <td class="no la">15.03 ± 2.70 / 40.22 ± 1.66</td> <!-- ScaLA-nb -->
   <td class="no la">5.95 ± 4.55 / 39.18 ± 2.91</td> <!-- ScaLA-nn -->
   <td class="no qa">42.42 ± 2.92 / 69.55 ± 3.18</td> <!-- NorQuAD -->
   <td class="no know">27.31 ± 2.26 / 45.04 ± 1.66</td> <!-- MMLU-no -->
   <td class="no know">56.92 ± 2.43 / 67.66 ± 1.81</td> <!-- ARC-no -->
   <td class="no reason">41.63 ± 2.84 / 56.02 ± 2.19</td> <!-- HellaSwag-no -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.69 ± 1.54 / 65.02 ± 1.14</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.06 ± 0.31 / 23.91 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">33.71 ± 2.28 / 50.08 ± 1.68</td> <!-- MMLU-sv -->
   <td class="sv know">67.71 ± 3.09 / 75.66 ± 2.33</td> <!-- ARC-sv -->
   <td class="sv reason">41.45 ± 3.36 / 55.51 ± 2.69</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="score">48.00 ± 2.51</td> <!-- ScandEval score -->
   <td class="da-score">45.13 ± 2.71</td> <!-- Danish score -->
   <td class="no-score">48.40 ± 2.70</td> <!-- Norwegian score -->
   <td class="sv-score">50.49 ± 2.11</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">68.14 ± 0.43 / 23.78 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">36.17 ± 1.86 / 51.60 ± 1.40</td> <!-- MMLU-da -->
   <td class="da know">66.24 ± 3.19 / 74.65 ± 2.40</td> <!-- ARC-da -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no know">58.53 ± 1.92 / 68.95 ± 1.42</td> <!-- ARC-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv know">63.97 ± 2.61 / 72.85 ± 2.01</td> <!-- ARC-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="score">48.00 ± 2.51</td> <!-- ScandEval score -->
   <td class="da-score">45.13 ± 2.71</td> <!-- Danish score -->
   <td class="no-score">48.40 ± 2.70</td> <!-- Norwegian score -->
   <td class="sv-score">50.49 ± 2.11</td> <!-- Swedish score -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da qa">57.38 ± 2.21 / 63.91 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">68.14 ± 0.43 / 23.78 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">36.17 ± 1.86 / 51.60 ± 1.40</td> <!-- MMLU-da -->
   <td class="da know">66.24 ± 3.19 / 74.65 ± 2.40</td> <!-- ARC-da -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td class="no ner">63.33 ± 2.69 / 53.24 ± 3.41</td> <!-- NorNE-nb -->
   <td class="no ner">68.84 ± 1.87 / 53.85 ± 3.78</td> <!-- NorNE-nn -->
   <td class="no sent">58.28 ± 3.11 / 69.79 ± 2.39</td> <!-- NoReC -->
   <td class="no summ">65.94 ± 0.22 / 19.92 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">18.65 ± 3.84 / 45.34 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">10.72 ± 5.52 / 43.91 ± 3.48</td> <!-- ScaLA-nn -->
   <td class="no qa">44.57 ± 4.08 / 70.85 ± 3.15</td> <!-- NorQuAD -->
   <td class="no know">26.61 ± 3.10 / 44.80 ± 2.38</td> <!-- MMLU-no -->
   <td class="no know">58.53 ± 1.92 / 68.95 ± 1.42</td> <!-- ARC-no -->
   <td class="no reason">46.64 ± 2.03 / 59.84 ± 1.50</td> <!-- HellaSwag-no -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.98 ± 1.47 / 66.15 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv know">63.97 ± 2.61 / 72.85 ± 2.01</td> <!-- ARC-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="score">47.28 ± 1.20</td> <!-- ScandEval score -->
   <td class="da-score">43.66 ± 0.83</td> <!-- Danish score -->
   <td class="no-score">48.48 ± 1.75</td> <!-- Norwegian score -->
   <td class="sv-score">49.71 ± 1.01</td> <!-- Swedish score -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">57.24 ± 0.74 / 63.79 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">67.61 ± 0.21 / 22.14 ± 0.48</td> <!-- Nordjylland-News -->
   <td class="da know">34.79 ± 0.90 / 50.86 ± 0.65</td> <!-- MMLU-da -->
   <td class="da know">57.52 ± 1.90 / 68.09 ± 1.47</td> <!-- ARC-da -->
   <td class="da reason">43.42 ± 1.05 / 57.50 ± 0.80</td> <!-- HellaSwag-da -->
   <td class="no ner">63.28 ± 1.99 / 47.72 ± 3.74</td> <!-- NorNE-nb -->
   <td class="no ner">61.25 ± 1.05 / 45.04 ± 2.92</td> <!-- NorNE-nn -->
   <td class="no sent">56.90 ± 1.49 / 70.81 ± 1.30</td> <!-- NoReC -->
   <td class="no summ">66.20 ± 0.24 / 20.14 ± 0.31</td> <!-- No Sammendrag -->
   <td class="no la">13.86 ± 1.95 / 44.84 ± 2.31</td> <!-- ScaLA-nb -->
   <td class="no la">10.17 ± 1.89 / 46.48 ± 2.46</td> <!-- ScaLA-nn -->
   <td class="no qa">49.06 ± 4.30 / 74.35 ± 3.96</td> <!-- NorQuAD -->
   <td class="no know">32.37 ± 1.15 / 49.00 ± 0.91</td> <!-- MMLU-no -->
   <td class="no know">58.24 ± 1.22 / 68.62 ± 0.90</td> <!-- ARC-no -->
   <td class="no reason">47.62 ± 1.62 / 60.59 ± 1.18</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.13 ± 1.18 / 65.74 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.33 ± 0.16 / 18.83 ± 0.21</td> <!-- SweDN -->
   <td class="sv know">35.01 ± 0.99 / 51.07 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv know">59.22 ± 1.30 / 69.23 ± 0.93</td> <!-- ARC-sv -->
   <td class="sv reason">43.72 ± 0.69 / 57.66 ± 0.50</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="score">47.05 ± 2.69</td> <!-- ScandEval score -->
   <td class="da-score">47.32 ± 2.44</td> <!-- Danish score -->
   <td class="no-score">43.21 ± 2.99</td> <!-- Norwegian score -->
   <td class="sv-score">50.62 ± 2.66</td> <!-- Swedish score -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da qa">58.23 ± 1.78 / 63.89 ± 1.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.78 ± 0.60 / 20.69 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">37.14 ± 2.25 / 52.19 ± 1.76</td> <!-- MMLU-da -->
   <td class="da know">59.96 ± 3.38 / 69.88 ± 2.51</td> <!-- ARC-da -->
   <td class="da reason">33.70 ± 2.78 / 50.16 ± 2.01</td> <!-- HellaSwag-da -->
   <td class="no ner">53.96 ± 3.37 / 49.84 ± 3.30</td> <!-- NorNE-nb -->
   <td class="no ner">63.45 ± 2.27 / 53.13 ± 3.43</td> <!-- NorNE-nn -->
   <td class="no sent">52.70 ± 4.58 / 66.82 ± 3.41</td> <!-- NoReC -->
   <td class="no summ">65.23 ± 0.55 / 18.64 ± 0.86</td> <!-- No Sammendrag -->
   <td class="no la">14.87 ± 3.37 / 40.83 ± 1.91</td> <!-- ScaLA-nb -->
   <td class="no la">2.48 ± 3.31 / 35.61 ± 1.83</td> <!-- ScaLA-nn -->
   <td class="no qa">41.56 ± 3.29 / 67.34 ± 2.82</td> <!-- NorQuAD -->
   <td class="no know">27.42 ± 2.13 / 45.20 ± 1.58</td> <!-- MMLU-no -->
   <td class="no know">51.66 ± 2.63 / 63.83 ± 1.93</td> <!-- ARC-no -->
   <td class="no reason">36.05 ± 3.95 / 51.68 ± 2.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.10 ± 1.61 / 65.00 ± 1.34</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.62 ± 0.42 / 23.90 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">27.95 ± 2.57 / 45.86 ± 1.85</td> <!-- MMLU-sv -->
   <td class="sv know">64.70 ± 3.13 / 73.44 ± 2.38</td> <!-- ARC-sv -->
   <td class="sv reason">36.11 ± 3.54 / 51.60 ± 2.44</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="score">46.39 ± 2.62</td> <!-- ScandEval score -->
   <td class="da-score">44.79 ± 2.65</td> <!-- Danish score -->
   <td class="no-score">42.71 ± 2.76</td> <!-- Norwegian score -->
   <td class="sv-score">51.67 ± 2.45</td> <!-- Swedish score -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da qa">58.27 ± 1.08 / 63.53 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">66.17 ± 0.63 / 18.50 ± 0.60</td> <!-- Nordjylland-News -->
   <td class="da know">32.41 ± 1.28 / 48.75 ± 0.85</td> <!-- MMLU-da -->
   <td class="da know">58.14 ± 3.36 / 68.67 ± 2.51</td> <!-- ARC-da -->
   <td class="da reason">28.33 ± 2.11 / 45.86 ± 1.72</td> <!-- HellaSwag-da -->
   <td class="no ner">56.44 ± 3.14 / 50.10 ± 4.61</td> <!-- NorNE-nb -->
   <td class="no ner">66.56 ± 2.40 / 54.48 ± 4.93</td> <!-- NorNE-nn -->
   <td class="no sent">53.24 ± 4.75 / 67.94 ± 3.75</td> <!-- NoReC -->
   <td class="no summ">64.96 ± 0.56 / 17.92 ± 0.82</td> <!-- No Sammendrag -->
   <td class="no la">11.96 ± 2.46 / 37.26 ± 1.15</td> <!-- ScaLA-nb -->
   <td class="no la">2.50 ± 4.21 / 35.26 ± 1.79</td> <!-- ScaLA-nn -->
   <td class="no qa">42.02 ± 2.82 / 66.99 ± 2.53</td> <!-- NorQuAD -->
   <td class="no know">26.64 ± 1.95 / 44.88 ± 1.41</td> <!-- MMLU-no -->
   <td class="no know">51.17 ± 2.94 / 63.36 ± 2.17</td> <!-- ARC-no -->
   <td class="no reason">31.14 ± 2.64 / 48.01 ± 2.14</td> <!-- HellaSwag-no -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.18 ± 1.37 / 64.78 ± 1.14</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.54 ± 0.48 / 23.67 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 2.34 / 46.95 ± 1.75</td> <!-- MMLU-sv -->
   <td class="sv know">59.54 ± 3.47 / 69.65 ± 2.57</td> <!-- ARC-sv -->
   <td class="sv reason">37.45 ± 3.61 / 52.85 ± 2.76</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="score">42.14 ± 3.13</td> <!-- ScandEval score -->
   <td class="da-score">42.70 ± 2.76</td> <!-- Danish score -->
   <td class="no-score">41.05 ± 3.47</td> <!-- Norwegian score -->
   <td class="sv-score">42.67 ± 3.15</td> <!-- Swedish score -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da qa">58.16 ± 1.29 / 63.63 ± 0.95</td> <!-- ScandiQA-da -->
   <td class="da summ">66.22 ± 0.72 / 18.95 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">23.49 ± 4.09 / 42.30 ± 3.02</td> <!-- MMLU-da -->
   <td class="da know">44.00 ± 3.07 / 57.89 ± 2.19</td> <!-- ARC-da -->
   <td class="da reason">25.54 ± 2.80 / 43.01 ± 1.95</td> <!-- HellaSwag-da -->
   <td class="no ner">51.78 ± 2.90 / 47.69 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">61.22 ± 3.73 / 50.00 ± 4.37</td> <!-- NorNE-nn -->
   <td class="no sent">53.06 ± 4.92 / 67.05 ± 4.22</td> <!-- NoReC -->
   <td class="no summ">65.11 ± 0.51 / 18.04 ± 0.81</td> <!-- No Sammendrag -->
   <td class="no la">10.27 ± 5.84 / 43.06 ± 3.15</td> <!-- ScaLA-nb -->
   <td class="no la">8.06 ± 3.56 / 41.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">41.18 ± 3.00 / 66.43 ± 2.76</td> <!-- NorQuAD -->
   <td class="no know">25.61 ± 2.74 / 44.49 ± 2.07</td> <!-- MMLU-no -->
   <td class="no know">43.76 ± 3.80 / 57.89 ± 2.76</td> <!-- ARC-no -->
   <td class="no reason">27.67 ± 4.55 / 44.18 ± 3.63</td> <!-- HellaSwag-no -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv qa">59.03 ± 1.52 / 64.13 ± 1.23</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.55 ± 0.53 / 23.64 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">23.10 ± 2.38 / 42.58 ± 1.74</td> <!-- MMLU-sv -->
   <td class="sv know">48.12 ± 1.81 / 60.94 ± 1.36</td> <!-- ARC-sv -->
   <td class="sv reason">29.31 ± 5.03 / 47.11 ± 3.62</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,505 ± 465 / 774 ± 242</td> <!-- Model inference speed -->
   <td class="score">42.00 ± 1.91</td> <!-- ScandEval score -->
   <td class="da-score">39.68 ± 1.89</td> <!-- Danish score -->
   <td class="no-score">36.79 ± 2.02</td> <!-- Norwegian score -->
   <td class="sv-score">49.52 ± 1.82</td> <!-- Swedish score -->
   <td class="da ner">41.66 ± 3.23 / 28.72 ± 2.20</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 2.03 / 62.67 ± 2.20</td> <!-- Angry Tweets -->
   <td class="da la">17.36 ± 2.43 / 53.55 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da qa">51.28 ± 1.14 / 56.19 ± 0.93</td> <!-- ScandiQA-da -->
   <td class="da summ">66.48 ± 0.60 / 21.83 ± 0.82</td> <!-- Nordjylland-News -->
   <td class="da know">31.12 ± 1.25 / 48.06 ± 0.93</td> <!-- MMLU-da -->
   <td class="da know">47.36 ± 1.56 / 60.46 ± 1.25</td> <!-- ARC-da -->
   <td class="da reason">14.21 ± 2.42 / 34.62 ± 2.04</td> <!-- HellaSwag-da -->
   <td class="no ner">48.28 ± 2.45 / 37.94 ± 2.62</td> <!-- NorNE-nb -->
   <td class="no ner">50.51 ± 2.81 / 38.77 ± 3.26</td> <!-- NorNE-nn -->
   <td class="no sent">49.76 ± 2.62 / 64.69 ± 2.26</td> <!-- NoReC -->
   <td class="no summ">64.48 ± 0.81 / 17.66 ± 1.07</td> <!-- No Sammendrag -->
   <td class="no la">14.54 ± 2.23 / 47.43 ± 4.29</td> <!-- ScaLA-nb -->
   <td class="no la">9.16 ± 1.52 / 48.30 ± 3.84</td> <!-- ScaLA-nn -->
   <td class="no qa">32.04 ± 1.57 / 53.75 ± 1.86</td> <!-- NorQuAD -->
   <td class="no know">25.52 ± 1.42 / 43.62 ± 1.11</td> <!-- MMLU-no -->
   <td class="no know">44.40 ± 1.24 / 58.26 ± 0.97</td> <!-- ARC-no -->
   <td class="no reason">15.04 ± 3.34 / 35.35 ± 2.33</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.16 ± 2.57 / 29.58 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">80.29 ± 1.06 / 80.37 ± 0.72</td> <!-- SweReC -->
   <td class="sv la">34.80 ± 2.22 / 65.44 ± 2.16</td> <!-- ScaLA-sv -->
   <td class="sv qa">51.82 ± 3.03 / 57.01 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.96 ± 0.31 / 19.25 ± 0.59</td> <!-- SweDN -->
   <td class="sv know">33.42 ± 0.70 / 49.88 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv know">57.37 ± 1.67 / 68.02 ± 1.25</td> <!-- ARC-sv -->
   <td class="sv reason">25.20 ± 2.35 / 43.09 ± 2.17</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">40.30 ± 2.15</td> <!-- ScandEval score -->
   <td class="da-score">39.60 ± 1.94</td> <!-- Danish score -->
   <td class="no-score">35.98 ± 2.54</td> <!-- Norwegian score -->
   <td class="sv-score">45.31 ± 1.96</td> <!-- Swedish score -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da qa">48.51 ± 2.11 / 53.66 ± 2.06</td> <!-- ScandiQA-da -->
   <td class="da summ">67.52 ± 0.29 / 23.53 ± 0.51</td> <!-- Nordjylland-News -->
   <td class="da know">34.76 ± 1.14 / 50.97 ± 0.84</td> <!-- MMLU-da -->
   <td class="da know">55.75 ± 1.61 / 66.87 ± 1.23</td> <!-- ARC-da -->
   <td class="da reason">18.53 ± 2.03 / 37.79 ± 1.68</td> <!-- HellaSwag-da -->
   <td class="no ner">52.00 ± 1.91 / 43.55 ± 2.21</td> <!-- NorNE-nb -->
   <td class="no ner">55.12 ± 3.14 / 45.34 ± 4.15</td> <!-- NorNE-nn -->
   <td class="no sent">47.25 ± 4.11 / 64.53 ± 3.71</td> <!-- NoReC -->
   <td class="no summ">65.05 ± 0.62 / 18.64 ± 0.80</td> <!-- No Sammendrag -->
   <td class="no la">8.66 ± 4.12 / 38.87 ± 3.40</td> <!-- ScaLA-nb -->
   <td class="no la">6.80 ± 1.59 / 39.72 ± 2.50</td> <!-- ScaLA-nn -->
   <td class="no qa">29.44 ± 2.86 / 50.68 ± 3.91</td> <!-- NorQuAD -->
   <td class="no know">27.78 ± 1.08 / 45.76 ± 0.79</td> <!-- MMLU-no -->
   <td class="no know">48.07 ± 1.30 / 61.18 ± 0.99</td> <!-- ARC-no -->
   <td class="no reason">10.88 ± 3.63 / 32.43 ± 2.67</td> <!-- HellaSwag-no -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.43 ± 4.69 / 54.33 ± 4.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.82 ± 0.29 / 19.41 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">35.52 ± 1.01 / 51.52 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv know">57.11 ± 1.04 / 67.79 ± 0.75</td> <!-- ARC-sv -->
   <td class="sv reason">19.67 ± 2.31 / 38.98 ± 1.98</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">38.06 ± 1.73</td> <!-- ScandEval score -->
   <td class="da-score">37.19 ± 1.87</td> <!-- Danish score -->
   <td class="no-score">35.28 ± 1.71</td> <!-- Norwegian score -->
   <td class="sv-score">41.72 ± 1.62</td> <!-- Swedish score -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da qa">51.42 ± 2.35 / 58.76 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="da summ">66.59 ± 0.34 / 21.45 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">24.65 ± 0.72 / 42.86 ± 0.55</td> <!-- MMLU-da -->
   <td class="da know">37.27 ± 1.32 / 52.46 ± 1.00</td> <!-- ARC-da -->
   <td class="da reason">14.85 ± 1.19 / 35.26 ± 1.24</td> <!-- HellaSwag-da -->
   <td class="no ner">50.08 ± 1.54 / 34.52 ± 1.17</td> <!-- NorNE-nb -->
   <td class="no ner">51.27 ± 1.52 / 33.37 ± 2.37</td> <!-- NorNE-nn -->
   <td class="no sent">43.65 ± 1.98 / 60.88 ± 1.36</td> <!-- NoReC -->
   <td class="no summ">63.31 ± 0.56 / 15.33 ± 0.67</td> <!-- No Sammendrag -->
   <td class="no la">14.09 ± 2.85 / 44.91 ± 3.95</td> <!-- ScaLA-nb -->
   <td class="no la">8.28 ± 1.82 / 47.22 ± 3.72</td> <!-- ScaLA-nn -->
   <td class="no qa">37.31 ± 3.13 / 63.71 ± 2.98</td> <!-- NorQuAD -->
   <td class="no know">20.44 ± 1.03 / 39.51 ± 0.72</td> <!-- MMLU-no -->
   <td class="no know">29.49 ± 1.32 / 46.31 ± 0.91</td> <!-- ARC-no -->
   <td class="no reason">15.87 ± 1.29 / 35.89 ± 1.06</td> <!-- HellaSwag-no -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.05 ± 1.44 / 59.27 ± 1.12</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.91 ± 0.43 / 18.85 ± 0.26</td> <!-- SweDN -->
   <td class="sv know">24.03 ± 1.09 / 42.32 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv know">37.48 ± 1.32 / 52.64 ± 1.12</td> <!-- ARC-sv -->
   <td class="sv reason">15.37 ± 0.71 / 35.78 ± 0.69</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="score">37.71 ± 1.69</td> <!-- ScandEval score -->
   <td class="da-score">38.76 ± 1.68</td> <!-- Danish score -->
   <td class="no-score">33.57 ± 1.67</td> <!-- Norwegian score -->
   <td class="sv-score">40.80 ± 1.72</td> <!-- Swedish score -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da qa">46.93 ± 1.12 / 55.22 ± 1.34</td> <!-- ScandiQA-da -->
   <td class="da summ">66.66 ± 0.32 / 20.59 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">24.43 ± 1.89 / 42.90 ± 1.34</td> <!-- MMLU-da -->
   <td class="da know">43.68 ± 1.64 / 57.64 ± 1.22</td> <!-- ARC-da -->
   <td class="da reason">11.59 ± 1.75 / 32.81 ± 1.55</td> <!-- HellaSwag-da -->
   <td class="no ner">57.01 ± 1.93 / 44.65 ± 2.87</td> <!-- NorNE-nb -->
   <td class="no ner">56.77 ± 0.98 / 41.67 ± 3.53</td> <!-- NorNE-nn -->
   <td class="no sent">38.81 ± 2.67 / 56.39 ± 3.13</td> <!-- NoReC -->
   <td class="no summ">63.93 ± 0.31 / 15.55 ± 0.57</td> <!-- No Sammendrag -->
   <td class="no la">14.16 ± 2.24 / 54.43 ± 2.61</td> <!-- ScaLA-nb -->
   <td class="no la">9.29 ± 2.65 / 50.59 ± 3.99</td> <!-- ScaLA-nn -->
   <td class="no qa">25.79 ± 1.43 / 50.84 ± 1.80</td> <!-- NorQuAD -->
   <td class="no know">17.08 ± 1.29 / 37.00 ± 1.04</td> <!-- MMLU-no -->
   <td class="no know">37.58 ± 0.93 / 53.10 ± 0.67</td> <!-- ARC-no -->
   <td class="no reason">10.52 ± 2.25 / 31.85 ± 1.79</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">48.44 ± 1.45 / 57.11 ± 1.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.03 ± 0.09 / 18.17 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">22.36 ± 1.17 / 41.14 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv know">44.29 ± 1.80 / 58.11 ± 1.38</td> <!-- ARC-sv -->
   <td class="sv reason">12.52 ± 1.41 / 33.90 ± 1.11</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5</td> <!-- Rank -->
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,019 ± 480 / 1,048 ± 317</td> <!-- Model inference speed -->
   <td class="score">37.50 ± 2.49</td> <!-- ScandEval score -->
   <td class="da-score">39.56 ± 2.70</td> <!-- Danish score -->
   <td class="no-score">30.82 ± 2.69</td> <!-- Norwegian score -->
   <td class="sv-score">42.13 ± 2.07</td> <!-- Swedish score -->
   <td class="da ner">38.31 ± 2.59 / 27.23 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">37.13 ± 2.26 / 44.00 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">26.46 ± 5.28 / 53.12 ± 6.51</td> <!-- ScaLA-da -->
   <td class="da qa">39.77 ± 4.66 / 44.54 ± 5.00</td> <!-- ScandiQA-da -->
   <td class="da summ">62.96 ± 0.57 / 16.35 ± 0.33</td> <!-- Nordjylland-News -->
   <td class="da know">35.57 ± 0.85 / 51.37 ± 0.66</td> <!-- MMLU-da -->
   <td class="da know">58.95 ± 1.18 / 69.25 ± 0.89</td> <!-- ARC-da -->
   <td class="da reason">25.06 ± 2.56 / 42.93 ± 2.25</td> <!-- HellaSwag-da -->
   <td class="no ner">46.32 ± 3.74 / 34.02 ± 2.70</td> <!-- NorNE-nb -->
   <td class="no ner">48.20 ± 1.59 / 35.05 ± 2.05</td> <!-- NorNE-nn -->
   <td class="no sent">20.46 ± 5.98 / 36.24 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">58.74 ± 0.83 / 11.67 ± 0.51</td> <!-- No Sammendrag -->
   <td class="no la">4.50 ± 4.17 / 35.29 ± 2.89</td> <!-- ScaLA-nb -->
   <td class="no la">1.10 ± 1.47 / 34.51 ± 1.24</td> <!-- ScaLA-nn -->
   <td class="no qa">31.16 ± 1.83 / 52.35 ± 2.34</td> <!-- NorQuAD -->
   <td class="no know">28.98 ± 1.16 / 46.10 ± 0.95</td> <!-- MMLU-no -->
   <td class="no know">50.48 ± 1.10 / 62.90 ± 0.86</td> <!-- ARC-no -->
   <td class="no reason">15.62 ± 3.56 / 35.78 ± 2.81</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.55 ± 2.39 / 27.89 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">78.79 ± 0.91 / 75.25 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">15.77 ± 1.64 / 54.44 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv qa">39.62 ± 4.78 / 45.18 ± 4.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.17 ± 0.81 / 16.98 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">30.96 ± 1.12 / 47.90 ± 0.94</td> <!-- MMLU-sv -->
   <td class="sv know">51.42 ± 1.34 / 63.57 ± 1.00</td> <!-- ARC-sv -->
   <td class="sv reason">18.79 ± 2.75 / 38.32 ± 2.26</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">34.79 ± 1.52</td> <!-- ScandEval score -->
   <td class="da-score">34.70 ± 1.28</td> <!-- Danish score -->
   <td class="no-score">31.57 ± 1.78</td> <!-- Norwegian score -->
   <td class="sv-score">38.10 ± 1.50</td> <!-- Swedish score -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da qa">55.00 ± 0.79 / 61.31 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">66.86 ± 0.31 / 20.92 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">17.57 ± 0.87 / 37.52 ± 0.69</td> <!-- MMLU-da -->
   <td class="da know">21.78 ± 1.24 / 41.20 ± 0.86</td> <!-- ARC-da -->
   <td class="da reason">11.32 ± 0.41 / 32.24 ± 0.79</td> <!-- HellaSwag-da -->
   <td class="no ner">44.99 ± 2.49 / 38.59 ± 2.84</td> <!-- NorNE-nb -->
   <td class="no ner">49.09 ± 1.90 / 39.09 ± 4.02</td> <!-- NorNE-nn -->
   <td class="no sent">41.56 ± 3.37 / 57.09 ± 3.80</td> <!-- NoReC -->
   <td class="no summ">64.39 ± 0.40 / 16.25 ± 0.69</td> <!-- No Sammendrag -->
   <td class="no la">3.04 ± 2.84 / 36.81 ± 2.42</td> <!-- ScaLA-nb -->
   <td class="no la">4.03 ± 2.49 / 40.55 ± 4.14</td> <!-- ScaLA-nn -->
   <td class="no qa">33.76 ± 2.07 / 61.97 ± 2.31</td> <!-- NorQuAD -->
   <td class="no know">14.81 ± 0.79 / 34.79 ± 0.63</td> <!-- MMLU-no -->
   <td class="no know">21.17 ± 1.19 / 40.79 ± 0.85</td> <!-- ARC-no -->
   <td class="no reason">12.69 ± 0.77 / 31.84 ± 1.05</td> <!-- HellaSwag-no -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">54.07 ± 0.84 / 60.93 ± 0.80</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.64 ± 0.07 / 18.92 ± 0.15</td> <!-- SweDN -->
   <td class="sv know">17.73 ± 0.98 / 37.55 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv know">25.20 ± 0.88 / 43.68 ± 0.70</td> <!-- ARC-sv -->
   <td class="sv reason">12.85 ± 0.93 / 33.37 ± 0.90</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">32.01 ± 1.80</td> <!-- ScandEval score -->
   <td class="da-score">30.68 ± 1.53</td> <!-- Danish score -->
   <td class="no-score">27.35 ± 1.66</td> <!-- Norwegian score -->
   <td class="sv-score">38.01 ± 2.20</td> <!-- Swedish score -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">45.42 ± 1.92 / 51.05 ± 2.05</td> <!-- ScandiQA-da -->
   <td class="da summ">66.53 ± 0.26 / 21.74 ± 0.32</td> <!-- Nordjylland-News -->
   <td class="da know">16.18 ± 0.85 / 36.87 ± 0.58</td> <!-- MMLU-da -->
   <td class="da know">21.61 ± 1.58 / 40.86 ± 1.31</td> <!-- ARC-da -->
   <td class="da reason">7.93 ± 1.49 / 29.76 ± 0.92</td> <!-- HellaSwag-da -->
   <td class="no ner">42.13 ± 3.82 / 37.17 ± 3.44</td> <!-- NorNE-nb -->
   <td class="no ner">43.80 ± 2.85 / 37.48 ± 4.00</td> <!-- NorNE-nn -->
   <td class="no sent">41.74 ± 2.25 / 57.91 ± 2.82</td> <!-- NoReC -->
   <td class="no summ">64.71 ± 0.87 / 18.26 ± 1.15</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.02 ± 0.04 / 33.88 ± 0.35</td> <!-- ScaLA-nn -->
   <td class="no qa">18.67 ± 2.60 / 36.99 ± 2.72</td> <!-- NorQuAD -->
   <td class="no know">14.48 ± 1.33 / 35.35 ± 0.94</td> <!-- MMLU-no -->
   <td class="no know">19.20 ± 0.91 / 38.93 ± 0.69</td> <!-- ARC-no -->
   <td class="no reason">6.49 ± 1.39 / 28.64 ± 0.96</td> <!-- HellaSwag-no -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv qa">43.42 ± 4.19 / 49.62 ± 4.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.31 ± 0.31 / 18.96 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">15.65 ± 0.55 / 36.32 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv know">22.60 ± 1.53 / 41.41 ± 1.12</td> <!-- ARC-sv -->
   <td class="sv reason">8.74 ± 1.34 / 29.87 ± 1.40</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">30.44 ± 2.01</td> <!-- ScandEval score -->
   <td class="da-score">27.68 ± 1.98</td> <!-- Danish score -->
   <td class="no-score">28.42 ± 2.26</td> <!-- Norwegian score -->
   <td class="sv-score">35.22 ± 1.79</td> <!-- Swedish score -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.24 ± 3.46 / 41.07 ± 4.41</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da qa">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">64.47 ± 1.21 / 18.39 ± 1.63</td> <!-- Nordjylland-News -->
   <td class="da know">5.03 ± 0.87 / 28.35 ± 0.92</td> <!-- MMLU-da -->
   <td class="da know">3.95 ± 1.51 / 28.39 ± 0.91</td> <!-- ARC-da -->
   <td class="da reason">3.03 ± 1.08 / 26.49 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">30.82 ± 5.81 / 25.27 ± 3.92</td> <!-- NorNE-nb -->
   <td class="no ner">39.56 ± 4.73 / 32.12 ± 4.06</td> <!-- NorNE-nn -->
   <td class="no sent">34.51 ± 1.27 / 42.18 ± 1.39</td> <!-- NoReC -->
   <td class="no summ">63.10 ± 1.12 / 16.05 ± 1.50</td> <!-- No Sammendrag -->
   <td class="no la">15.17 ± 1.41 / 49.46 ± 2.90</td> <!-- ScaLA-nb -->
   <td class="no la">12.46 ± 3.29 / 48.89 ± 5.19</td> <!-- ScaLA-nn -->
   <td class="no qa">42.81 ± 3.10 / 66.15 ± 3.21</td> <!-- NorQuAD -->
   <td class="no know">4.51 ± 1.00 / 27.45 ± 0.78</td> <!-- MMLU-no -->
   <td class="no know">3.98 ± 1.90 / 29.17 ± 0.95</td> <!-- ARC-no -->
   <td class="no reason">5.27 ± 1.29 / 28.47 ± 1.11</td> <!-- HellaSwag-no -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">78.88 ± 1.58 / 79.56 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv qa">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.14 ± 0.46 / 18.76 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">3.15 ± 0.80 / 27.43 ± 0.91</td> <!-- MMLU-sv -->
   <td class="sv know">2.99 ± 1.66 / 27.55 ± 0.92</td> <!-- ARC-sv -->
   <td class="sv reason">2.77 ± 1.26 / 26.43 ± 0.84</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">29.80 ± 1.55</td> <!-- ScandEval score -->
   <td class="da-score">27.80 ± 1.41</td> <!-- Danish score -->
   <td class="no-score">25.73 ± 1.91</td> <!-- Norwegian score -->
   <td class="sv-score">35.88 ± 1.33</td> <!-- Swedish score -->
   <td class="da ner">33.41 ± 3.32 / 25.37 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">26.08 ± 2.58 / 36.10 ± 3.61</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 0.43 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da qa">51.90 ± 1.44 / 56.87 ± 1.30</td> <!-- ScandiQA-da -->
   <td class="da summ">65.25 ± 0.37 / 19.49 ± 0.46</td> <!-- Nordjylland-News -->
   <td class="da know">12.68 ± 1.17 / 32.38 ± 1.00</td> <!-- MMLU-da -->
   <td class="da know">15.27 ± 1.57 / 35.82 ± 1.15</td> <!-- ARC-da -->
   <td class="da reason">4.19 ± 0.36 / 27.25 ± 0.65</td> <!-- HellaSwag-da -->
   <td class="no ner">41.44 ± 4.22 / 32.73 ± 3.13</td> <!-- NorNE-nb -->
   <td class="no ner">45.09 ± 3.73 / 35.29 ± 4.71</td> <!-- NorNE-nn -->
   <td class="no sent">34.51 ± 3.16 / 54.99 ± 2.47</td> <!-- NoReC -->
   <td class="no summ">62.38 ± 0.40 / 14.30 ± 0.44</td> <!-- No Sammendrag -->
   <td class="no la">0.00 ± 0.00 / 33.41 ± 0.30</td> <!-- ScaLA-nb -->
   <td class="no la">0.56 ± 1.10 / 33.93 ± 0.37</td> <!-- ScaLA-nn -->
   <td class="no qa">24.53 ± 3.16 / 41.00 ± 4.65</td> <!-- NorQuAD -->
   <td class="no know">8.98 ± 0.79 / 28.94 ± 0.83</td> <!-- MMLU-no -->
   <td class="no know">12.43 ± 1.23 / 34.25 ± 0.94</td> <!-- ARC-no -->
   <td class="no reason">4.46 ± 1.14 / 27.19 ± 1.10</td> <!-- HellaSwag-no -->
   <td class="sv ner">41.08 ± 3.32 / 29.46 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 0.82 / 75.25 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">-0.21 ± 0.42 / 33.36 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv qa">52.58 ± 1.46 / 57.71 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.36 ± 0.83 / 16.19 ± 1.12</td> <!-- SweDN -->
   <td class="sv know">13.09 ± 1.18 / 32.28 ± 1.12</td> <!-- MMLU-sv -->
   <td class="sv know">17.64 ± 1.48 / 36.86 ± 1.39</td> <!-- ARC-sv -->
   <td class="sv reason">3.59 ± 1.12 / 26.82 ± 1.13</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="score">26.67 ± 2.30</td> <!-- ScandEval score -->
   <td class="da-score">23.65 ± 2.02</td> <!-- Danish score -->
   <td class="no-score">24.28 ± 2.74</td> <!-- Norwegian score -->
   <td class="sv-score">32.08 ± 2.13</td> <!-- Swedish score -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da qa">39.18 ± 3.52 / 44.53 ± 3.79</td> <!-- ScandiQA-da -->
   <td class="da summ">66.28 ± 0.55 / 20.87 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">4.93 ± 0.91 / 28.06 ± 0.72</td> <!-- MMLU-da -->
   <td class="da know">5.23 ± 0.98 / 29.21 ± 0.88</td> <!-- ARC-da -->
   <td class="da reason">5.57 ± 0.93 / 28.66 ± 0.66</td> <!-- HellaSwag-da -->
   <td class="no ner">29.62 ± 4.17 / 24.40 ± 2.42</td> <!-- NorNE-nb -->
   <td class="no ner">32.30 ± 5.27 / 29.23 ± 3.22</td> <!-- NorNE-nn -->
   <td class="no sent">34.67 ± 5.23 / 54.62 ± 5.71</td> <!-- NoReC -->
   <td class="no summ">63.58 ± 1.06 / 16.52 ± 1.39</td> <!-- No Sammendrag -->
   <td class="no la">8.37 ± 1.71 / 48.94 ± 2.72</td> <!-- ScaLA-nb -->
   <td class="no la">7.76 ± 2.86 / 46.16 ± 4.77</td> <!-- ScaLA-nn -->
   <td class="no qa">24.67 ± 2.82 / 43.02 ± 4.03</td> <!-- NorQuAD -->
   <td class="no know">3.03 ± 1.30 / 25.60 ± 0.86</td> <!-- MMLU-no -->
   <td class="no know">1.92 ± 2.47 / 27.75 ± 1.43</td> <!-- ARC-no -->
   <td class="no reason">5.57 ± 1.19 / 27.61 ± 0.93</td> <!-- HellaSwag-no -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv qa">35.78 ± 4.94 / 41.08 ± 5.23</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.08 ± 0.64 / 17.89 ± 0.48</td> <!-- SweDN -->
   <td class="sv know">5.23 ± 1.02 / 28.63 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv know">5.49 ± 2.01 / 29.43 ± 1.25</td> <!-- ARC-sv -->
   <td class="sv reason">5.39 ± 0.81 / 28.86 ± 0.60</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="score">26.36 ± 1.77</td> <!-- ScandEval score -->
   <td class="da-score">23.06 ± 1.54</td> <!-- Danish score -->
   <td class="no-score">26.09 ± 2.13</td> <!-- Norwegian score -->
   <td class="sv-score">29.94 ± 1.64</td> <!-- Swedish score -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da qa">44.04 ± 2.07 / 51.91 ± 2.08</td> <!-- ScandiQA-da -->
   <td class="da summ">67.12 ± 0.48 / 22.61 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">8.25 ± 0.88 / 28.79 ± 0.69</td> <!-- MMLU-da -->
   <td class="da know">11.72 ± 2.02 / 32.99 ± 1.77</td> <!-- ARC-da -->
   <td class="da reason">11.08 ± 1.35 / 32.13 ± 1.04</td> <!-- HellaSwag-da -->
   <td class="no ner">24.67 ± 1.69 / 24.58 ± 1.95</td> <!-- NorNE-nb -->
   <td class="no ner">29.03 ± 2.12 / 29.83 ± 2.15</td> <!-- NorNE-nn -->
   <td class="no sent">34.39 ± 5.34 / 50.45 ± 6.08</td> <!-- NoReC -->
   <td class="no summ">64.83 ± 0.60 / 18.37 ± 0.66</td> <!-- No Sammendrag -->
   <td class="no la">2.42 ± 1.83 / 35.49 ± 2.63</td> <!-- ScaLA-nb -->
   <td class="no la">5.11 ± 2.68 / 38.37 ± 3.31</td> <!-- ScaLA-nn -->
   <td class="no qa">31.39 ± 2.33 / 52.78 ± 3.03</td> <!-- NorQuAD -->
   <td class="no know">6.89 ± 1.56 / 27.44 ± 1.06</td> <!-- MMLU-no -->
   <td class="no know">10.30 ± 2.10 / 32.06 ± 1.70</td> <!-- ARC-no -->
   <td class="no reason">12.81 ± 0.66 / 32.38 ± 0.61</td> <!-- HellaSwag-no -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv qa">42.72 ± 2.66 / 50.17 ± 3.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.86 ± 0.15 / 19.08 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">6.16 ± 0.81 / 28.35 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv know">11.86 ± 1.84 / 33.18 ± 1.24</td> <!-- ARC-sv -->
   <td class="sv reason">10.90 ± 0.86 / 32.01 ± 0.54</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="score">22.63 ± 2.26</td> <!-- ScandEval score -->
   <td class="da-score">21.19 ± 2.10</td> <!-- Danish score -->
   <td class="no-score">20.07 ± 2.80</td> <!-- Norwegian score -->
   <td class="sv-score">26.64 ± 1.89</td> <!-- Swedish score -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da qa">45.31 ± 0.88 / 51.56 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">63.77 ± 1.09 / 17.31 ± 1.38</td> <!-- Nordjylland-News -->
   <td class="da know">-1.05 ± 1.43 / 23.83 ± 0.92</td> <!-- MMLU-da -->
   <td class="da know">-0.38 ± 1.35 / 23.96 ± 0.89</td> <!-- ARC-da -->
   <td class="da reason">-0.33 ± 1.17 / 24.65 ± 0.48</td> <!-- HellaSwag-da -->
   <td class="no ner">13.49 ± 7.98 / 14.80 ± 7.68</td> <!-- NorNE-nb -->
   <td class="no ner">14.74 ± 8.45 / 15.09 ± 7.85</td> <!-- NorNE-nn -->
   <td class="no sent">27.28 ± 4.39 / 49.18 ± 4.23</td> <!-- NoReC -->
   <td class="no summ">61.24 ± 0.98 / 13.30 ± 0.99</td> <!-- No Sammendrag -->
   <td class="no la">3.09 ± 0.79 / 42.87 ± 3.49</td> <!-- ScaLA-nb -->
   <td class="no la">1.86 ± 1.90 / 38.18 ± 1.44</td> <!-- ScaLA-nn -->
   <td class="no qa">34.90 ± 2.66 / 54.29 ± 2.94</td> <!-- NorQuAD -->
   <td class="no know">-0.01 ± 0.86 / 24.32 ± 0.81</td> <!-- MMLU-no -->
   <td class="no know">0.45 ± 1.24 / 24.77 ± 1.24</td> <!-- ARC-no -->
   <td class="no reason">0.25 ± 0.94 / 25.10 ± 0.81</td> <!-- HellaSwag-no -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv qa">45.53 ± 0.83 / 51.66 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.90 ± 1.33 / 16.54 ± 0.71</td> <!-- SweDN -->
   <td class="sv know">2.20 ± 0.88 / 25.62 ± 0.86</td> <!-- MMLU-sv -->
   <td class="sv know">-0.76 ± 1.29 / 25.22 ± 1.02</td> <!-- ARC-sv -->
   <td class="sv reason">0.67 ± 1.39 / 25.25 ± 0.51</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9=</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="score">19.73 ± 2.39</td> <!-- ScandEval score -->
   <td class="da-score">20.51 ± 1.85</td> <!-- Danish score -->
   <td class="no-score">17.79 ± 1.80</td> <!-- Norwegian score -->
   <td class="sv-score">20.88 ± 3.52</td> <!-- Swedish score -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da qa">18.78 ± 3.89 / 24.10 ± 4.26</td> <!-- ScandiQA-da -->
   <td class="da summ">65.74 ± 0.29 / 19.05 ± 0.64</td> <!-- Nordjylland-News -->
   <td class="da know">1.73 ± 0.94 / 26.18 ± 0.63</td> <!-- MMLU-da -->
   <td class="da know">-1.91 ± 1.70 / 24.70 ± 0.92</td> <!-- ARC-da -->
   <td class="da reason">2.11 ± 1.44 / 26.00 ± 0.86</td> <!-- HellaSwag-da -->
   <td class="no ner">28.74 ± 4.18 / 28.29 ± 4.37</td> <!-- NorNE-nb -->
   <td class="no ner">30.34 ± 6.08 / 30.02 ± 6.42</td> <!-- NorNE-nn -->
   <td class="no sent">27.49 ± 3.13 / 48.00 ± 3.89</td> <!-- NoReC -->
   <td class="no summ">60.72 ± 0.76 / 10.83 ± 0.72</td> <!-- No Sammendrag -->
   <td class="no la">-2.17 ± 1.06 / 33.52 ± 0.37</td> <!-- ScaLA-nb -->
   <td class="no la">0.26 ± 1.08 / 34.12 ± 0.45</td> <!-- ScaLA-nn -->
   <td class="no qa">5.35 ± 0.33 / 17.89 ± 1.64</td> <!-- NorQuAD -->
   <td class="no know">3.21 ± 0.87 / 27.07 ± 0.74</td> <!-- MMLU-no -->
   <td class="no know">1.26 ± 1.45 / 25.80 ± 0.88</td> <!-- ARC-no -->
   <td class="no reason">0.18 ± 1.02 / 25.00 ± 0.86</td> <!-- HellaSwag-no -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv qa">15.08 ± 3.85 / 19.72 ± 4.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.65 ± 0.26 / 11.86 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">0.14 ± 1.02 / 24.76 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv know">-0.84 ± 0.99 / 25.06 ± 0.82</td> <!-- ARC-sv -->
   <td class="sv reason">0.52 ± 0.83 / 25.53 ± 0.62</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">18.06 ± 2.08</td> <!-- ScandEval score -->
   <td class="da-score">15.11 ± 1.92</td> <!-- Danish score -->
   <td class="no-score">16.81 ± 1.51</td> <!-- Norwegian score -->
   <td class="sv-score">22.28 ± 2.81</td> <!-- Swedish score -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da qa">26.21 ± 3.93 / 29.03 ± 4.17</td> <!-- ScandiQA-da -->
   <td class="da summ">60.03 ± 0.65 / 12.94 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">0.76 ± 0.91 / 25.67 ± 0.80</td> <!-- MMLU-da -->
   <td class="da know">-0.23 ± 2.17 / 24.31 ± 1.91</td> <!-- ARC-da -->
   <td class="da reason">-0.88 ± 1.17 / 24.43 ± 0.74</td> <!-- HellaSwag-da -->
   <td class="no ner">21.04 ± 2.63 / 20.44 ± 2.47</td> <!-- NorNE-nb -->
   <td class="no ner">18.71 ± 2.67 / 19.91 ± 2.89</td> <!-- NorNE-nn -->
   <td class="no sent">12.22 ± 1.17 / 23.50 ± 3.03</td> <!-- NoReC -->
   <td class="no summ">60.08 ± 1.33 / 12.33 ± 0.95</td> <!-- No Sammendrag -->
   <td class="no la">-1.18 ± 1.40 / 35.70 ± 2.67</td> <!-- ScaLA-nb -->
   <td class="no la">0.36 ± 1.28 / 37.66 ± 4.07</td> <!-- ScaLA-nn -->
   <td class="no qa">26.79 ± 1.65 / 50.19 ± 1.83</td> <!-- NorQuAD -->
   <td class="no know">0.21 ± 0.83 / 26.88 ± 1.44</td> <!-- MMLU-no -->
   <td class="no know">-1.42 ± 1.74 / 23.64 ± 1.79</td> <!-- ARC-no -->
   <td class="no reason">-0.30 ± 1.13 / 24.48 ± 0.70</td> <!-- HellaSwag-no -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv qa">44.37 ± 1.37 / 50.18 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.49 ± 0.54 / 14.60 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">1.12 ± 0.42 / 25.27 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv know">-0.28 ± 1.45 / 25.37 ± 1.01</td> <!-- ARC-sv -->
   <td class="sv reason">-0.91 ± 0.96 / 24.26 ± 0.64</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10=</td> <!-- Rank -->
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="score">16.87 ± 3.05</td> <!-- ScandEval score -->
   <td class="da-score">16.66 ± 2.18</td> <!-- Danish score -->
   <td class="no-score">15.16 ± 2.64</td> <!-- Norwegian score -->
   <td class="sv-score">18.80 ± 4.35</td> <!-- Swedish score -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da qa">14.16 ± 1.82 / 19.24 ± 1.85</td> <!-- ScandiQA-da -->
   <td class="da summ">63.76 ± 0.90 / 17.20 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">-1.11 ± 1.35 / 23.90 ± 1.06</td> <!-- MMLU-da -->
   <td class="da know">0.05 ± 1.21 / 24.68 ± 0.96</td> <!-- ARC-da -->
   <td class="da reason">-0.70 ± 0.94 / 24.83 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">27.37 ± 6.89 / 27.19 ± 7.19</td> <!-- NorNE-nb -->
   <td class="no ner">27.59 ± 6.34 / 28.03 ± 6.94</td> <!-- NorNE-nn -->
   <td class="no sent">18.09 ± 6.14 / 31.83 ± 6.77</td> <!-- NoReC -->
   <td class="no summ">58.73 ± 1.67 / 10.49 ± 1.17</td> <!-- No Sammendrag -->
   <td class="no la">-0.19 ± 1.93 / 41.38 ± 3.18</td> <!-- ScaLA-nb -->
   <td class="no la">-0.80 ± 0.89 / 40.66 ± 3.78</td> <!-- ScaLA-nn -->
   <td class="no qa">2.15 ± 0.46 / 10.01 ± 1.47</td> <!-- NorQuAD -->
   <td class="no know">-0.50 ± 1.10 / 23.75 ± 0.96</td> <!-- MMLU-no -->
   <td class="no know">0.76 ± 0.88 / 25.14 ± 0.65</td> <!-- ARC-no -->
   <td class="no reason">0.07 ± 1.21 / 25.26 ± 0.95</td> <!-- HellaSwag-no -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv qa">21.56 ± 3.80 / 26.32 ± 4.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.33 ± 0.73 / 13.25 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">-0.85 ± 1.05 / 24.38 ± 0.51</td> <!-- MMLU-sv -->
   <td class="sv know">0.17 ± 1.99 / 25.19 ± 1.57</td> <!-- ARC-sv -->
   <td class="sv reason">-1.24 ± 0.90 / 24.30 ± 0.63</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="score">10.65 ± 2.26</td> <!-- ScandEval score -->
   <td class="da-score">10.88 ± 1.84</td> <!-- Danish score -->
   <td class="no-score">10.30 ± 2.09</td> <!-- Norwegian score -->
   <td class="sv-score">10.76 ± 2.84</td> <!-- Swedish score -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da qa">7.70 ± 0.67 / 10.40 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">57.45 ± 1.32 / 12.05 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">-0.37 ± 1.31 / 23.87 ± 1.03</td> <!-- MMLU-da -->
   <td class="da know">0.23 ± 1.54 / 23.34 ± 1.01</td> <!-- ARC-da -->
   <td class="da reason">-1.28 ± 0.99 / 24.75 ± 0.93</td> <!-- HellaSwag-da -->
   <td class="no ner">13.55 ± 6.73 / 15.90 ± 5.66</td> <!-- NorNE-nb -->
   <td class="no ner">9.38 ± 4.88 / 11.18 ± 4.52</td> <!-- NorNE-nn -->
   <td class="no sent">7.78 ± 3.76 / 21.70 ± 5.02</td> <!-- NoReC -->
   <td class="no summ">55.00 ± 1.43 / 9.00 ± 0.65</td> <!-- No Sammendrag -->
   <td class="no la">-1.46 ± 1.07 / 43.30 ± 2.30</td> <!-- ScaLA-nb -->
   <td class="no la">-2.97 ± 1.29 / 44.41 ± 3.18</td> <!-- ScaLA-nn -->
   <td class="no qa">0.90 ± 0.23 / 4.99 ± 1.08</td> <!-- NorQuAD -->
   <td class="no know">0.39 ± 1.28 / 23.22 ± 0.56</td> <!-- MMLU-no -->
   <td class="no know">-0.51 ± 1.77 / 23.07 ± 1.64</td> <!-- ARC-no -->
   <td class="no reason">-0.80 ± 0.71 / 24.77 ± 0.62</td> <!-- HellaSwag-no -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv qa">7.64 ± 2.58 / 9.62 ± 3.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.07 ± 1.04 / 13.34 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.60 / 22.53 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv know">-0.66 ± 1.95 / 23.78 ± 1.42</td> <!-- ARC-sv -->
   <td class="sv reason">1.17 ± 0.86 / 25.54 ± 0.87</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="score">8.25 ± 1.46</td> <!-- ScandEval score -->
   <td class="da-score">9.52 ± 1.30</td> <!-- Danish score -->
   <td class="no-score">8.24 ± 1.14</td> <!-- Norwegian score -->
   <td class="sv-score">6.98 ± 1.95</td> <!-- Swedish score -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.92 ± 0.79 / 35.76 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da qa">6.82 ± 6.80 / 21.29 ± 6.25</td> <!-- ScandiQA-da -->
   <td class="da summ">58.94 ± 0.40 / 15.76 ± 0.66</td> <!-- Nordjylland-News -->
   <td class="da know">-0.18 ± 0.36 / 23.41 ± 0.62</td> <!-- MMLU-da -->
   <td class="da know">0.00 ± 0.00 / 21.79 ± 0.76</td> <!-- ARC-da -->
   <td class="da reason">-0.18 ± 0.65 / 25.00 ± 0.59</td> <!-- HellaSwag-da -->
   <td class="no ner">5.29 ± 4.68 / 4.93 ± 4.38</td> <!-- NorNE-nb -->
   <td class="no ner">6.77 ± 6.18 / 6.78 ± 5.66</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no summ">49.57 ± 0.81 / 9.47 ± 0.48</td> <!-- No Sammendrag -->
   <td class="no la">0.20 ± 1.19 / 38.14 ± 4.59</td> <!-- ScaLA-nb -->
   <td class="no la">-0.90 ± 1.07 / 37.78 ± 5.01</td> <!-- ScaLA-nn -->
   <td class="no qa">2.45 ± 0.61 / 22.80 ± 2.27</td> <!-- NorQuAD -->
   <td class="no know">0.00 ± 0.00 / 21.90 ± 0.51</td> <!-- MMLU-no -->
   <td class="no know">0.00 ± 0.00 / 22.44 ± 1.03</td> <!-- ARC-no -->
   <td class="no reason">0.00 ± 0.00 / 25.02 ± 0.87</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">0.33 ± 0.66 / 19.45 ± 0.34</td> <!-- SweReC -->
   <td class="sv la">0.41 ± 0.81 / 33.36 ± 0.28</td> <!-- ScaLA-sv -->
   <td class="sv qa">17.79 ± 11.20 / 31.10 ± 8.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">29.95 ± 0.23 / 8.33 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">0.17 ± 0.34 / 21.97 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv know">0.00 ± 0.00 / 22.42 ± 0.88</td> <!-- ARC-sv -->
   <td class="sv reason">-0.01 ± 0.01 / 25.00 ± 0.77</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="score">7.18 ± 1.04</td> <!-- ScandEval score -->
   <td class="da-score">8.78 ± 1.51</td> <!-- Danish score -->
   <td class="no-score">6.59 ± 0.44</td> <!-- Norwegian score -->
   <td class="sv-score">6.17 ± 1.15</td> <!-- Swedish score -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">-1.00 ± 0.82 / 27.41 ± 0.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.75 ± 1.00 / 33.28 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da qa">5.16 ± 6.60 / 17.34 ± 5.84</td> <!-- ScandiQA-da -->
   <td class="da summ">57.26 ± 0.88 / 14.33 ± 0.65</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 23.42 ± 0.62</td> <!-- MMLU-da -->
   <td class="da know">0.24 ± 0.47 / 21.80 ± 0.76</td> <!-- ARC-da -->
   <td class="da reason">0.33 ± 0.65 / 25.05 ± 0.60</td> <!-- HellaSwag-da -->
   <td class="no ner">0.22 ± 0.21 / 1.66 ± 1.38</td> <!-- NorNE-nb -->
   <td class="no ner">0.24 ± 0.40 / 1.43 ± 1.97</td> <!-- NorNE-nn -->
   <td class="no sent">0.00 ± 0.00 / 9.59 ± 0.29</td> <!-- NoReC -->
   <td class="no summ">44.80 ± 1.54 / 8.15 ± 0.74</td> <!-- No Sammendrag -->
   <td class="no la">0.75 ± 0.82 / 35.63 ± 3.45</td> <!-- ScaLA-nb -->
   <td class="no la">0.42 ± 0.95 / 35.89 ± 3.60</td> <!-- ScaLA-nn -->
   <td class="no qa">0.55 ± 0.32 / 22.10 ± 2.28</td> <!-- NorQuAD -->
   <td class="no know">-0.01 ± 0.02 / 21.90 ± 0.51</td> <!-- MMLU-no -->
   <td class="no know">-0.03 ± 0.05 / 22.44 ± 1.03</td> <!-- ARC-no -->
   <td class="no reason">0.00 ± 0.01 / 25.02 ± 0.87</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">7.45 ± 3.03 / 24.92 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv qa">4.82 ± 3.58 / 18.08 ± 2.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">30.78 ± 0.33 / 8.47 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">0.29 ± 0.37 / 21.98 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv know">0.32 ± 1.01 / 22.45 ± 0.87</td> <!-- ARC-sv -->
   <td class="sv reason">-0.15 ± 0.43 / 24.96 ± 0.81</td> <!-- HellaSwag-sv -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">13</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">5.14 ± 0.82</td> <!-- ScandEval score -->
   <td class="da-score">4.88 ± 0.85</td> <!-- Danish score -->
   <td class="no-score">4.57 ± 0.69</td> <!-- Norwegian score -->
   <td class="sv-score">5.96 ± 0.93</td> <!-- Swedish score -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">0.41 ± 0.55 / 18.36 ± 0.51</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 0.33 / 33.45 ± 0.33</td> <!-- ScaLA-da -->
   <td class="da qa">2.00 ± 1.70 / 2.69 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="da summ">31.24 ± 1.02 / 1.76 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">0.58 ± 0.71 / 23.92 ± 0.63</td> <!-- MMLU-da -->
   <td class="da know">0.17 ± 0.79 / 22.90 ± 0.72</td> <!-- ARC-da -->
   <td class="da reason">-0.41 ± 0.90 / 24.83 ± 0.82</td> <!-- HellaSwag-da -->
   <td class="no ner">0.08 ± 0.16 / 0.07 ± 0.14</td> <!-- NorNE-nb -->
   <td class="no ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- NorNE-nn -->
   <td class="no sent">-0.73 ± 1.44 / 11.42 ± 1.46</td> <!-- NoReC -->
   <td class="no summ">33.33 ± 0.19 / 1.15 ± 0.06</td> <!-- No Sammendrag -->
   <td class="no la">-0.23 ± 0.95 / 33.80 ± 1.10</td> <!-- ScaLA-nb -->
   <td class="no la">0.88 ± 1.03 / 33.92 ± 2.21</td> <!-- ScaLA-nn -->
   <td class="no qa">0.00 ± 0.00 / 0.73 ± 0.05</td> <!-- NorQuAD -->
   <td class="no know">-0.40 ± 0.97 / 22.35 ± 0.43</td> <!-- MMLU-no -->
   <td class="no know">0.32 ± 1.12 / 23.20 ± 0.70</td> <!-- ARC-no -->
   <td class="no reason">-0.94 ± 1.10 / 24.74 ± 0.85</td> <!-- HellaSwag-no -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">1.38 ± 1.38 / 39.60 ± 4.21</td> <!-- ScaLA-sv -->
   <td class="sv qa">6.24 ± 3.13 / 7.86 ± 3.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">34.81 ± 0.08 / 3.13 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.16 ± 0.48 / 22.57 ± 0.38</td> <!-- MMLU-sv -->
   <td class="sv know">-0.83 ± 1.37 / 22.97 ± 0.76</td> <!-- ARC-sv -->
   <td class="sv reason">-0.19 ± 0.97 / 24.75 ± 0.67</td> <!-- HellaSwag-sv -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>