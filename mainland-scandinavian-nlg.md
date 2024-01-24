---
layout: leaderboard
title: Mainland Scandinavian NLG
---

<center>Last updated: 24/01/2024 12:35:10 CET</center>
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
   <td class="rank">2</td> <!-- Rank -->
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
   <td class="rank">3</td> <!-- Rank -->
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
   <td class="rank">4</td> <!-- Rank -->
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
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/mainland-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>