---
layout: leaderboard
title: Mainland Scandinavian NLG
---

<center>Last updated: 02/02/2024 07:43:04 CET</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
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
  <tr>
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
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>RJuro/munin-neuralbeagle-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,499 ± 461 / 783 ± 246</td> <!-- Model inference speed -->
   <td class="score">48.54 ± 1.91</td> <!-- ScandEval score -->
   <td class="da-score">49.02 ± 1.72</td> <!-- Danish score -->
   <td class="no-score">44.99 ± 1.96</td> <!-- Norwegian score -->
   <td class="sv-score">51.62 ± 2.05</td> <!-- Swedish score -->
   <td class="da ner">49.85 ± 1.80 / 35.27 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">50.81 ± 1.92 / 65.66 ± 1.89</td> <!-- Angry Tweets -->
   <td class="da la">24.76 ± 2.82 / 52.04 ± 3.56</td> <!-- ScaLA-da -->
   <td class="da qa">51.43 ± 1.67 / 58.69 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="da summ">68.63 ± 0.28 / 25.10 ± 0.48</td> <!-- Nordjylland-News -->
   <td class="da know">38.87 ± 0.74 / 54.05 ± 0.55</td> <!-- MMLU-da -->
   <td class="da know">64.25 ± 1.30 / 73.24 ± 0.99</td> <!-- ARC-da -->
   <td class="da reason">46.12 ± 2.51 / 59.25 ± 2.06</td> <!-- HellaSwag-da -->
   <td class="no ner">61.90 ± 1.87 / 52.45 ± 3.21</td> <!-- NorNE-nb -->
   <td class="no ner">62.27 ± 1.13 / 51.67 ± 2.50</td> <!-- NorNE-nn -->
   <td class="no sent">54.72 ± 2.28 / 69.86 ± 1.96</td> <!-- NoReC -->
   <td class="no summ">66.24 ± 0.27 / 19.80 ± 0.35</td> <!-- No Sammendrag -->
   <td class="no la">18.90 ± 3.47 / 46.97 ± 4.19</td> <!-- ScaLA-nb -->
   <td class="no la">8.64 ± 2.17 / 43.63 ± 3.75</td> <!-- ScaLA-nn -->
   <td class="no qa">34.91 ± 1.81 / 62.20 ± 2.27</td> <!-- NorQuAD -->
   <td class="no know">32.71 ± 1.14 / 49.33 ± 0.85</td> <!-- MMLU-no -->
   <td class="no know">56.27 ± 1.53 / 67.29 ± 1.16</td> <!-- ARC-no -->
   <td class="no reason">38.69 ± 3.70 / 53.67 ± 3.00</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.18 ± 1.84 / 44.22 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">79.42 ± 0.95 / 79.12 ± 1.07</td> <!-- SweReC -->
   <td class="sv la">19.92 ± 4.12 / 47.58 ± 4.18</td> <!-- ScaLA-sv -->
   <td class="sv qa">50.72 ± 3.41 / 58.38 ± 3.43</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.98 ± 0.19 / 16.85 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">36.57 ± 1.45 / 52.20 ± 1.11</td> <!-- MMLU-sv -->
   <td class="sv know">60.67 ± 1.15 / 70.56 ± 0.84</td> <!-- ARC-sv -->
   <td class="sv reason">39.48 ± 2.52 / 54.20 ± 2.14</td> <!-- HellaSwag-sv -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>timpal0l/BeagleCatMunin (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,450 ± 1,274 / 1,138 ± 360</td> <!-- Model inference speed -->
   <td class="score">47.92 ± 1.85</td> <!-- ScandEval score -->
   <td class="da-score">47.40 ± 1.84</td> <!-- Danish score -->
   <td class="no-score">43.72 ± 2.13</td> <!-- Norwegian score -->
   <td class="sv-score">52.65 ± 1.57</td> <!-- Swedish score -->
   <td class="da ner">48.35 ± 2.25 / 34.01 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.39 ± 1.20 / 67.12 ± 1.13</td> <!-- Angry Tweets -->
   <td class="da la">24.33 ± 4.10 / 49.78 ± 3.94</td> <!-- ScaLA-da -->
   <td class="da qa">58.47 ± 0.79 / 64.49 ± 0.56</td> <!-- ScandiQA-da -->
   <td class="da summ">67.84 ± 0.58 / 23.90 ± 0.69</td> <!-- Nordjylland-News -->
   <td class="da know">37.69 ± 0.80 / 53.04 ± 0.61</td> <!-- MMLU-da -->
   <td class="da know">60.67 ± 1.91 / 70.55 ± 1.45</td> <!-- ARC-da -->
   <td class="da reason">32.22 ± 2.60 / 48.42 ± 2.17</td> <!-- HellaSwag-da -->
   <td class="no ner">57.72 ± 1.71 / 48.96 ± 2.88</td> <!-- NorNE-nb -->
   <td class="no ner">58.02 ± 1.77 / 47.49 ± 3.01</td> <!-- NorNE-nn -->
   <td class="no sent">54.24 ± 2.07 / 68.77 ± 1.77</td> <!-- NoReC -->
   <td class="no summ">65.74 ± 0.42 / 19.27 ± 0.56</td> <!-- No Sammendrag -->
   <td class="no la">13.02 ± 2.31 / 38.70 ± 1.43</td> <!-- ScaLA-nb -->
   <td class="no la">6.65 ± 2.00 / 38.43 ± 2.05</td> <!-- ScaLA-nn -->
   <td class="no qa">44.40 ± 3.16 / 71.75 ± 3.08</td> <!-- NorQuAD -->
   <td class="no know">31.80 ± 1.06 / 48.47 ± 0.83</td> <!-- MMLU-no -->
   <td class="no know">53.64 ± 1.47 / 65.30 ± 1.11</td> <!-- ARC-no -->
   <td class="no reason">31.22 ± 4.09 / 47.90 ± 3.24</td> <!-- HellaSwag-no -->
   <td class="sv ner">50.72 ± 2.14 / 37.15 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">80.72 ± 0.73 / 80.40 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">25.63 ± 2.86 / 48.40 ± 2.95</td> <!-- ScaLA-sv -->
   <td class="sv qa">58.16 ± 0.81 / 64.55 ± 0.70</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.62 ± 0.30 / 19.68 ± 0.41</td> <!-- SweDN -->
   <td class="sv know">36.79 ± 1.20 / 52.23 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv know">61.81 ± 1.01 / 71.37 ± 0.75</td> <!-- ARC-sv -->
   <td class="sv reason">38.39 ± 3.03 / 53.33 ± 2.53</td> <!-- HellaSwag-sv -->
  </tr>
  <tr>
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
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,065 ± 472 / 1,055 ± 321</td> <!-- Model inference speed -->
   <td class="score">46.79 ± 1.72</td> <!-- ScandEval score -->
   <td class="da-score">46.72 ± 1.47</td> <!-- Danish score -->
   <td class="no-score">43.07 ± 1.81</td> <!-- Norwegian score -->
   <td class="sv-score">50.57 ± 1.89</td> <!-- Swedish score -->
   <td class="da ner">51.47 ± 1.90 / 34.70 ± 2.73</td> <!-- DANSK -->
   <td class="da sent">50.02 ± 1.28 / 66.53 ± 1.04</td> <!-- Angry Tweets -->
   <td class="da la">21.10 ± 2.04 / 56.07 ± 2.28</td> <!-- ScaLA-da -->
   <td class="da qa">47.41 ± 1.64 / 57.80 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="da summ">68.14 ± 0.35 / 23.67 ± 0.51</td> <!-- Nordjylland-News -->
   <td class="da know">34.74 ± 0.85 / 50.80 ± 0.62</td> <!-- MMLU-da -->
   <td class="da know">58.06 ± 1.16 / 68.60 ± 0.89</td> <!-- ARC-da -->
   <td class="da reason">42.49 ± 2.07 / 56.26 ± 1.87</td> <!-- HellaSwag-da -->
   <td class="no ner">62.31 ± 2.15 / 54.43 ± 2.27</td> <!-- NorNE-nb -->
   <td class="no ner">62.81 ± 1.13 / 53.57 ± 2.55</td> <!-- NorNE-nn -->
   <td class="no sent">53.12 ± 2.72 / 67.77 ± 2.14</td> <!-- NoReC -->
   <td class="no summ">66.01 ± 0.20 / 19.31 ± 0.35</td> <!-- No Sammendrag -->
   <td class="no la">14.66 ± 2.60 / 48.02 ± 3.36</td> <!-- ScaLA-nb -->
   <td class="no la">10.88 ± 1.17 / 48.34 ± 2.45</td> <!-- ScaLA-nn -->
   <td class="no qa">30.20 ± 1.60 / 62.49 ± 1.70</td> <!-- NorQuAD -->
   <td class="no know">27.92 ± 1.29 / 45.57 ± 0.98</td> <!-- MMLU-no -->
   <td class="no know">50.88 ± 1.46 / 63.21 ± 1.10</td> <!-- ARC-no -->
   <td class="no reason">37.46 ± 3.26 / 52.09 ± 3.13</td> <!-- HellaSwag-no -->
   <td class="sv ner">58.85 ± 1.71 / 44.79 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">76.52 ± 0.71 / 77.39 ± 0.70</td> <!-- SweReC -->
   <td class="sv la">18.63 ± 3.14 / 49.89 ± 3.46</td> <!-- ScaLA-sv -->
   <td class="sv qa">47.63 ± 2.16 / 58.70 ± 0.80</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.26 ± 0.20 / 20.15 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">33.36 ± 0.95 / 49.78 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv know">57.37 ± 1.67 / 68.02 ± 1.26</td> <!-- ARC-sv -->
   <td class="sv reason">40.75 ± 4.01 / 54.93 ± 3.44</td> <!-- HellaSwag-sv -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>birgermoell/NeuralBeagle-Flashback-dare-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,910 ± 413 / 1,148 ± 347</td> <!-- Model inference speed -->
   <td class="score">44.72 ± 3.27</td> <!-- ScandEval score -->
   <td class="da-score">44.67 ± 3.27</td> <!-- Danish score -->
   <td class="no-score">42.52 ± 3.15</td> <!-- Norwegian score -->
   <td class="sv-score">46.97 ± 3.40</td> <!-- Swedish score -->
   <td class="da ner">46.44 ± 3.21 / 34.44 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">45.16 ± 3.24 / 54.44 ± 4.21</td> <!-- Angry Tweets -->
   <td class="da la">19.43 ± 7.34 / 49.91 ± 6.48</td> <!-- ScaLA-da -->
   <td class="da qa">58.11 ± 1.95 / 63.66 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="da summ">66.16 ± 0.74 / 18.53 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">36.00 ± 2.22 / 51.48 ± 1.71</td> <!-- MMLU-da -->
   <td class="da know">56.25 ± 3.82 / 67.19 ± 2.87</td> <!-- ARC-da -->
   <td class="da reason">31.30 ± 3.38 / 47.89 ± 2.62</td> <!-- HellaSwag-da -->
   <td class="no ner">52.25 ± 3.21 / 46.46 ± 3.91</td> <!-- NorNE-nb -->
   <td class="no ner">63.39 ± 3.82 / 50.92 ± 3.97</td> <!-- NorNE-nn -->
   <td class="no sent">58.77 ± 3.95 / 71.71 ± 3.35</td> <!-- NoReC -->
   <td class="no summ">65.31 ± 0.48 / 18.19 ± 0.58</td> <!-- No Sammendrag -->
   <td class="no la">-2.15 ± 7.59 / 36.87 ± 1.67</td> <!-- ScaLA-nb -->
   <td class="no la">-0.04 ± 3.26 / 35.46 ± 1.38</td> <!-- ScaLA-nn -->
   <td class="no qa">42.89 ± 2.80 / 68.70 ± 2.22</td> <!-- NorQuAD -->
   <td class="no know">27.85 ± 2.14 / 45.90 ± 1.57</td> <!-- MMLU-no -->
   <td class="no know">51.55 ± 3.87 / 63.75 ± 2.78</td> <!-- ARC-no -->
   <td class="no reason">34.26 ± 2.90 / 49.92 ± 2.55</td> <!-- HellaSwag-no -->
   <td class="sv ner">54.02 ± 4.44 / 38.95 ± 5.80</td> <!-- SUC3 -->
   <td class="sv sent">39.03 ± 5.07 / 55.76 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">21.18 ± 5.71 / 48.56 ± 5.00</td> <!-- ScaLA-sv -->
   <td class="sv qa">60.61 ± 1.46 / 65.64 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.68 ± 0.55 / 24.01 ± 1.02</td> <!-- SweDN -->
   <td class="sv know">31.58 ± 3.86 / 48.79 ± 2.87</td> <!-- MMLU-sv -->
   <td class="sv know">60.34 ± 2.53 / 70.27 ± 1.85</td> <!-- ARC-sv -->
   <td class="sv reason">40.32 ± 3.39 / 54.96 ± 2.45</td> <!-- HellaSwag-sv -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">6</td> <!-- Rank -->
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
  <tr>
   <td class="rank">7=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">7=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">8=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">8=</td> <!-- Rank -->
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
  <tr>
   <td class="rank">9</td> <!-- Rank -->
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
  <tr>
   <td class="rank">10</td> <!-- Rank -->
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
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>