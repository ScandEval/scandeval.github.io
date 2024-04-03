---
layout: leaderboard
title: Dutch NLU
---

<center>Last updated: 03/04/2024 11:35:53 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="dutch-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch question answering - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-nl">CoNLL-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Dutch Social">Dutch Social version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nl">ScaLA-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD-nl">SQuAD-nl version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="nl ner">82.31 ± 2.14 / 86.91 ± 1.34</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.64 ± 2.91 / 49.90 ± 3.42</td> <!-- Dutch Social -->
   <td class="nl la">58.51 ± 4.12 / 78.17 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.32 ± 1.91 / 57.53 ± 1.78</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="nl ner">82.02 ± 1.04 / 84.71 ± 0.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">33.99 ± 4.05 / 50.69 ± 4.23</td> <!-- Dutch Social -->
   <td class="nl la">60.77 ± 1.53 / 79.80 ± 0.87</td> <!-- ScaLA-nl -->
   <td class="nl qa">41.55 ± 1.08 / 51.73 ± 1.18</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4 ± 0 / 3 ± 0</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.05 ± 1.85 / 35.62 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">74.01 ± 1.29 / 86.71 ± 0.78</td> <!-- ScaLA-nl -->
   <td class="nl qa">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.3.2</td> <!-- Dutch Social version -->
   <td>12.3.2</td> <!-- ScaLA-nl version -->
   <td>12.3.2</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbert-2022-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">43</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,307 ± 2,134 / 2,580 ± 834</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="nl ner">79.84 ± 1.41 / 84.42 ± 1.03</td> <!-- CoNLL-nl -->
   <td class="nl sent">24.58 ± 5.35 / 42.93 ± 4.78</td> <!-- Dutch Social -->
   <td class="nl la">68.76 ± 1.47 / 83.77 ± 0.93</td> <!-- ScaLA-nl -->
   <td class="nl qa">27.63 ± 1.32 / 36.98 ± 1.39</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="nl ner">78.30 ± 1.97 / 83.07 ± 1.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">26.68 ± 2.90 / 44.41 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">63.83 ± 3.09 / 80.68 ± 2.18</td> <!-- ScaLA-nl -->
   <td class="nl qa">28.34 ± 1.30 / 37.79 ± 1.37</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,471 ± 2,152 / 2,194 ± 723</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="nl ner">78.45 ± 1.88 / 83.50 ± 0.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">22.67 ± 7.22 / 44.07 ± 6.51</td> <!-- Dutch Social -->
   <td class="nl la">54.92 ± 9.62 / 76.14 ± 5.00</td> <!-- ScaLA-nl -->
   <td class="nl qa">31.82 ± 2.84 / 40.85 ± 3.02</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">1.81</td> <!-- ScandEval rank -->
   <td class="nl ner">79.12 ± 1.90 / 83.05 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">27.67 ± 2.85 / 44.90 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">39.28 ± 12.28 / 67.90 ± 5.94</td> <!-- ScaLA-nl -->
   <td class="nl qa">35.71 ± 1.70 / 46.63 ± 1.40</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="nl ner">83.49 ± 1.51 / 86.12 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.82 ± 7.93 / 30.82 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">64.80 ± 8.79 / 80.93 ± 6.29</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.72 ± 1.20 / 61.66 ± 1.16</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbertje-1-gb-non-shuffled</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">21,007 ± 3,892 / 4,922 ± 1,588</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="nl ner">74.50 ± 1.61 / 81.38 ± 0.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.23 ± 1.76 / 50.11 ± 2.55</td> <!-- Dutch Social -->
   <td class="nl la">54.57 ± 1.72 / 75.82 ± 1.07</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.31 ± 0.28 / 11.55 ± 0.22</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbert-2023-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,230 ± 1,939 / 2,750 ± 897</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="nl ner">82.22 ± 1.28 / 86.32 ± 0.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">28.20 ± 3.75 / 44.38 ± 3.44</td> <!-- Dutch Social -->
   <td class="nl la">55.12 ± 11.67 / 76.12 ± 7.45</td> <!-- ScaLA-nl -->
   <td class="nl qa">9.74 ± 0.34 / 44.34 ± 0.99</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="nl ner">84.47 ± 1.84 / 87.98 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.16 ± 5.21 / 27.85 ± 3.29</td> <!-- Dutch Social -->
   <td class="nl la">71.23 ± 1.62 / 85.45 ± 0.83</td> <!-- ScaLA-nl -->
   <td class="nl qa">46.43 ± 0.72 / 57.80 ± 0.84</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbertje-1-gb-merged</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">21,027 ± 3,902 / 4,932 ± 1,591</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="nl ner">72.51 ± 0.97 / 80.14 ± 0.74</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.26 ± 2.51 / 47.44 ± 2.78</td> <!-- Dutch Social -->
   <td class="nl la">50.00 ± 2.09 / 73.38 ± 1.43</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.97 ± 0.44 / 11.08 ± 0.47</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="nl ner">78.74 ± 1.42 / 84.14 ± 0.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">22.58 ± 5.79 / 41.55 ± 4.55</td> <!-- Dutch Social -->
   <td class="nl la">55.39 ± 2.71 / 76.38 ± 2.03</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.95 ± 3.06 / 7.23 ± 3.67</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbertje-1-gb-shuffled</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,616 ± 3,755 / 4,819 ± 1,542</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="nl ner">73.55 ± 2.27 / 80.69 ± 1.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">26.02 ± 3.29 / 42.90 ± 2.60</td> <!-- Dutch Social -->
   <td class="nl la">57.03 ± 1.80 / 77.24 ± 1.09</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.64 ± 0.36 / 12.04 ± 0.28</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbert-2023-dutch-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,444 ± 911 / 1,413 ± 457</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="nl ner">81.05 ± 2.44 / 85.20 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">16.35 ± 6.39 / 36.89 ± 5.03</td> <!-- Dutch Social -->
   <td class="nl la">65.18 ± 1.83 / 82.29 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl qa">11.44 ± 0.50 / 52.98 ± 1.31</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="nl ner">77.15 ± 1.38 / 81.92 ± 1.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.78 ± 6.76 / 37.09 ± 4.14</td> <!-- Dutch Social -->
   <td class="nl la">56.72 ± 3.83 / 77.53 ± 2.17</td> <!-- ScaLA-nl -->
   <td class="nl qa">14.61 ± 4.26 / 20.91 ± 5.21</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="nl ner">70.59 ± 1.60 / 78.25 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">21.37 ± 8.79 / 40.62 ± 7.64</td> <!-- Dutch Social -->
   <td class="nl la">45.86 ± 2.06 / 71.32 ± 1.40</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.20 ± 0.30 / 10.40 ± 0.38</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="nl ner">78.85 ± 2.48 / 83.35 ± 2.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.80 ± 7.64 / 33.49 ± 6.73</td> <!-- Dutch Social -->
   <td class="nl la">14.56 ± 8.02 / 53.64 ± 5.14</td> <!-- ScaLA-nl -->
   <td class="nl qa">42.08 ± 7.94 / 51.94 ± 9.08</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>DTAI-KULeuven/robbertje-1-gb-bort</td> <!-- Model ID -->
   <td class="num_model_parameters">45</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">31,087 ± 5,833 / 7,147 ± 2,339</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="nl ner">66.74 ± 1.53 / 75.07 ± 0.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">24.93 ± 6.85 / 41.47 ± 4.05</td> <!-- Dutch Social -->
   <td class="nl la">37.19 ± 6.22 / 66.68 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.23 ± 0.43 / 10.67 ± 0.44</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.88 ± 1.15 / 70.09 ± 0.97</td> <!-- SQuAD-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>9.3.2</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl qa">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td>9.1.2</td> <!-- CoNLL-nl version -->
   <td>9.1.2</td> <!-- Dutch Social version -->
   <td>9.1.2</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/GEITje-7B-ultra (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,475 ± 460 / 765 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="nl ner">42.25 ± 2.12 / 27.85 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.78 ± 2.52 / 42.17 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">18.23 ± 1.91 / 50.04 ± 2.54</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.41 ± 1.11 / 66.45 ± 0.46</td> <!-- SQuAD-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="nl ner">67.89 ± 1.61 / 74.48 ± 1.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">23.25 ± 6.95 / 44.88 ± 6.27</td> <!-- Dutch Social -->
   <td class="nl la">21.36 ± 7.80 / 59.50 ± 3.54</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.50 ± 0.39 / 9.94 ± 0.33</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">108</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="nl ner">75.02 ± 1.48 / 81.57 ± 0.76</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.45 ± 2.99 / 29.70 ± 1.94</td> <!-- Dutch Social -->
   <td class="nl la">45.28 ± 0.55 / 71.89 ± 0.59</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.18 ± 1.26 / 27.86 ± 1.48</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="nl ner">57.66 ± 1.29 / 43.77 ± 2.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.41 ± 1.47 / 25.59 ± 1.30</td> <!-- Dutch Social -->
   <td class="nl la">16.93 ± 2.60 / 55.72 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl qa">56.29 ± 1.11 / 68.94 ± 0.81</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="nl ner">48.14 ± 6.28 / 43.67 ± 4.37</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl qa">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.2.0</td> <!-- Dutch Social version -->
   <td>12.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="nl ner">47.53 ± 1.90 / 32.42 ± 1.99</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.36 ± 2.96 / 28.11 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">30.67 ± 4.45 / 63.78 ± 2.80</td> <!-- ScaLA-nl -->
   <td class="nl qa">56.55 ± 0.70 / 67.56 ± 0.60</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="nl ner">74.03 ± 3.05 / 80.59 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.53 ± 5.28 / 32.06 ± 4.17</td> <!-- Dutch Social -->
   <td class="nl la">39.12 ± 12.90 / 68.36 ± 6.85</td> <!-- ScaLA-nl -->
   <td class="nl qa">7.71 ± 0.42 / 12.90 ± 0.39</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl qa">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">93</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="nl ner">49.54 ± 1.42 / 50.44 ± 1.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.86 ± 3.09 / 35.33 ± 1.77</td> <!-- Dutch Social -->
   <td class="nl la">27.90 ± 5.58 / 62.47 ± 3.34</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.65 ± 1.02 / 29.40 ± 1.29</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="nl ner">42.51 ± 6.54 / 40.38 ± 3.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl qa">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="nl ner">77.35 ± 2.80 / 82.50 ± 1.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.55 ± 5.33 / 28.68 ± 3.64</td> <!-- Dutch Social -->
   <td class="nl la">18.25 ± 8.41 / 54.00 ± 5.57</td> <!-- ScaLA-nl -->
   <td class="nl qa">28.37 ± 4.84 / 36.84 ± 5.92</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="nl ner">73.03 ± 2.07 / 79.97 ± 1.63</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.65 ± 4.19 / 26.89 ± 2.64</td> <!-- Dutch Social -->
   <td class="nl la">2.00 ± 2.03 / 39.53 ± 4.47</td> <!-- ScaLA-nl -->
   <td class="nl qa">42.85 ± 0.98 / 53.68 ± 0.89</td> <!-- SQuAD-nl -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>10.0.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="nl ner">35.30 ± 3.76 / 33.68 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.67 ± 2.21 / 31.30 ± 4.51</td> <!-- Dutch Social -->
   <td class="nl la">1.76 ± 2.37 / 47.60 ± 1.68</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.05 ± 1.68 / 55.38 ± 1.66</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="nl ner">22.82 ± 6.74 / 26.58 ± 6.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="nl ner">24.85 ± 6.27 / 22.96 ± 5.14</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="nl ner">46.34 ± 2.00 / 33.30 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.96 ± 1.44 / 18.10 ± 2.39</td> <!-- Dutch Social -->
   <td class="nl la">0.88 ± 1.23 / 33.53 ± 0.48</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.33 ± 1.28 / 66.50 ± 0.94</td> <!-- SQuAD-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.0</td> <!-- Dutch Social version -->
   <td>10.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="nl ner">70.92 ± 1.61 / 78.52 ± 1.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.50 ± 3.15 / 27.25 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">2.06 ± 1.79 / 41.06 ± 5.11</td> <!-- ScaLA-nl -->
   <td class="nl qa">41.40 ± 1.92 / 51.93 ± 2.09</td> <!-- SQuAD-nl -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>10.0.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.51 ± 2.13 / 44.59 ± 2.68</td> <!-- SQuAD-nl -->
   <td>9.2.0</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.2.0</td> <!-- ScaLA-nl version -->
   <td>9.2.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="nl ner">58.67 ± 1.07 / 68.27 ± 0.94</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.82 ± 4.47 / 37.11 ± 2.75</td> <!-- Dutch Social -->
   <td class="nl la">9.27 ± 4.66 / 52.04 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl qa">2.17 ± 0.34 / 8.02 ± 0.41</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.56 ± 1.37 / 47.43 ± 1.50</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="nl ner">56.98 ± 1.37 / 66.91 ± 1.60</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.66 ± 4.65 / 31.17 ± 3.34</td> <!-- Dutch Social -->
   <td class="nl la">19.37 ± 4.34 / 56.74 ± 3.13</td> <!-- ScaLA-nl -->
   <td class="nl qa">3.11 ± 0.37 / 7.91 ± 0.25</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="nl ner">29.22 ± 2.84 / 30.53 ± 1.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="nl ner">17.12 ± 3.08 / 12.52 ± 2.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>jpostma/DagoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,241 ± 2,115 / 2,565 ± 830</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="nl ner">42.28 ± 1.41 / 47.68 ± 1.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.01 ± 2.88 / 31.60 ± 2.41</td> <!-- Dutch Social -->
   <td class="nl la">31.21 ± 1.62 / 64.82 ± 0.69</td> <!-- ScaLA-nl -->
   <td class="nl qa">3.65 ± 0.33 / 9.49 ± 0.31</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="nl ner">23.79 ± 2.23 / 23.73 ± 1.94</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl qa">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="nl ner">17.85 ± 4.84 / 16.04 ± 3.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl qa">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="nl ner">44.46 ± 2.24 / 60.04 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.39 ± 4.20 / 30.69 ± 2.83</td> <!-- Dutch Social -->
   <td class="nl la">2.07 ± 1.34 / 48.42 ± 1.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.30 ± 1.26 / 9.24 ± 1.13</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="nl ner">41.38 ± 2.82 / 56.29 ± 1.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.45 ± 2.80 / 29.85 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.55 ± 1.97 / 49.24 ± 1.16</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.40 ± 0.22 / 6.62 ± 0.38</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="nl ner">22.60 ± 2.46 / 25.50 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="nl ner">8.34 ± 3.09 / 10.76 ± 3.46</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl qa">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.89</td> <!-- ScandEval rank -->
   <td class="nl ner">19.25 ± 3.64 / 23.18 ± 2.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.92 ± 2.71 / 19.51 ± 4.22</td> <!-- Dutch Social -->
   <td class="nl la">-1.27 ± 1.85 / 41.38 ± 3.59</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.64 ± 1.96 / 11.74 ± 1.62</td> <!-- SQuAD-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,319 ± 94 / 656 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="nl ner">13.09 ± 1.68 / 16.25 ± 2.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.92 ± 2.11 / 25.39 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.93 ± 1.37 / 40.76 ± 4.83</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.26 ± 0.09 / 2.70 ± 1.10</td> <!-- SQuAD-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.26</td> <!-- ScandEval rank -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.95 ± 1.17 / 9.87 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.00 ± 0.00 / 5.43 ± 0.58</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>11.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/dutch-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Dutch NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-rkwMq&quot; src=&quot;https://datawrapper.dwcdn.net/rkwMq/857/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
