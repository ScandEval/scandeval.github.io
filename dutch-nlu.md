---
layout: leaderboard
title: Dutch NLU
---

<center>Last updated: 05/02/2024 10:58:26 CET</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="dutch-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch question answering - Exact Match / F1-score">SQuAD-nl</span></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="score">54.70 ± 2.77</td> <!-- ScandEval score -->
   <td class="nl ner">82.31 ± 2.14 / 86.91 ± 1.34</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.64 ± 2.91 / 49.90 ± 3.42</td> <!-- Dutch Social -->
   <td class="nl la">58.51 ± 4.12 / 78.17 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.32 ± 1.91 / 57.53 ± 1.78</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="score">54.58 ± 1.93</td> <!-- ScandEval score -->
   <td class="nl ner">82.02 ± 1.04 / 84.71 ± 0.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">33.99 ± 4.05 / 50.69 ± 4.23</td> <!-- Dutch Social -->
   <td class="nl la">60.77 ± 1.53 / 79.80 ± 0.87</td> <!-- ScaLA-nl -->
   <td class="nl qa">41.55 ± 1.08 / 51.73 ± 1.18</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="score">51.96 ± 4.86</td> <!-- ScandEval score -->
   <td class="nl ner">83.49 ± 1.51 / 86.12 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.82 ± 7.93 / 30.82 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">64.80 ± 8.79 / 80.93 ± 6.29</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.72 ± 1.20 / 61.66 ± 1.16</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score">51.82 ± 2.35</td> <!-- ScandEval score -->
   <td class="nl ner">84.47 ± 1.84 / 87.98 ± 1.21</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.16 ± 5.21 / 27.85 ± 3.29</td> <!-- Dutch Social -->
   <td class="nl la">71.23 ± 1.62 / 85.45 ± 0.83</td> <!-- ScaLA-nl -->
   <td class="nl qa">46.43 ± 0.72 / 57.80 ± 0.84</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbert-2022-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">43</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,307 ± 2,134 / 2,580 ± 834</td> <!-- Model inference speed -->
   <td class="score">50.20 ± 2.39</td> <!-- ScandEval score -->
   <td class="nl ner">79.84 ± 1.41 / 84.42 ± 1.03</td> <!-- CoNLL-nl -->
   <td class="nl sent">24.58 ± 5.35 / 42.93 ± 4.78</td> <!-- Dutch Social -->
   <td class="nl la">68.76 ± 1.47 / 83.77 ± 0.93</td> <!-- ScaLA-nl -->
   <td class="nl qa">27.63 ± 1.32 / 36.98 ± 1.39</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="score">49.29 ± 2.31</td> <!-- ScandEval score -->
   <td class="nl ner">78.30 ± 1.97 / 83.07 ± 1.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">26.68 ± 2.90 / 44.41 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">63.83 ± 3.09 / 80.68 ± 2.18</td> <!-- ScaLA-nl -->
   <td class="nl qa">28.34 ± 1.30 / 37.79 ± 1.37</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">48.07 ± 3.48</td> <!-- ScandEval score -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,471 ± 2,152 / 2,194 ± 723</td> <!-- Model inference speed -->
   <td class="score">46.97 ± 5.39</td> <!-- ScandEval score -->
   <td class="nl ner">78.45 ± 1.88 / 83.50 ± 0.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">22.67 ± 7.22 / 44.07 ± 6.51</td> <!-- Dutch Social -->
   <td class="nl la">54.92 ± 9.62 / 76.14 ± 5.00</td> <!-- ScaLA-nl -->
   <td class="nl qa">31.82 ± 2.84 / 40.85 ± 3.02</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">2=</td> <!-- Rank -->
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="score">45.45 ± 4.68</td> <!-- ScandEval score -->
   <td class="nl ner">79.12 ± 1.90 / 83.05 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">27.67 ± 2.85 / 44.90 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">39.28 ± 12.28 / 67.90 ± 5.94</td> <!-- ScaLA-nl -->
   <td class="nl qa">35.71 ± 1.70 / 46.63 ± 1.40</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbert-2023-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,230 ± 1,939 / 2,750 ± 897</td> <!-- Model inference speed -->
   <td class="score">43.82 ± 4.26</td> <!-- ScandEval score -->
   <td class="nl ner">82.22 ± 1.28 / 86.32 ± 0.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">28.20 ± 3.75 / 44.38 ± 3.44</td> <!-- Dutch Social -->
   <td class="nl la">55.12 ± 11.67 / 76.12 ± 7.45</td> <!-- ScaLA-nl -->
   <td class="nl qa">9.74 ± 0.34 / 44.34 ± 0.99</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbert-2023-dutch-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,444 ± 911 / 1,413 ± 457</td> <!-- Model inference speed -->
   <td class="score">43.51 ± 2.79</td> <!-- ScandEval score -->
   <td class="nl ner">81.05 ± 2.44 / 85.20 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">16.35 ± 6.39 / 36.89 ± 5.03</td> <!-- Dutch Social -->
   <td class="nl la">65.18 ± 1.83 / 82.29 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl qa">11.44 ± 0.50 / 52.98 ± 1.31</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbertje-1-gb-non-shuffled</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">21,007 ± 3,892 / 4,922 ± 1,588</td> <!-- Model inference speed -->
   <td class="score">41.90 ± 1.34</td> <!-- ScandEval score -->
   <td class="nl ner">74.50 ± 1.61 / 81.38 ± 0.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.23 ± 1.76 / 50.11 ± 2.55</td> <!-- Dutch Social -->
   <td class="nl la">54.57 ± 1.72 / 75.82 ± 1.07</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.31 ± 0.28 / 11.55 ± 0.22</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="score">41.81 ± 4.06</td> <!-- ScandEval score -->
   <td class="nl ner">77.15 ± 1.38 / 81.92 ± 1.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.78 ± 6.76 / 37.09 ± 4.14</td> <!-- Dutch Social -->
   <td class="nl la">56.72 ± 3.83 / 77.53 ± 2.17</td> <!-- ScaLA-nl -->
   <td class="nl qa">14.61 ± 4.26 / 20.91 ± 5.21</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbertje-1-gb-shuffled</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,616 ± 3,755 / 4,819 ± 1,542</td> <!-- Model inference speed -->
   <td class="score">40.81 ± 1.93</td> <!-- ScandEval score -->
   <td class="nl ner">73.55 ± 2.27 / 80.69 ± 1.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">26.02 ± 3.29 / 42.90 ± 2.60</td> <!-- Dutch Social -->
   <td class="nl la">57.03 ± 1.80 / 77.24 ± 1.09</td> <!-- ScaLA-nl -->
   <td class="nl qa">6.64 ± 0.36 / 12.04 ± 0.28</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="score">40.66 ± 3.25</td> <!-- ScandEval score -->
   <td class="nl ner">78.74 ± 1.42 / 84.14 ± 0.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">22.58 ± 5.79 / 41.55 ± 4.55</td> <!-- Dutch Social -->
   <td class="nl la">55.39 ± 2.71 / 76.38 ± 2.03</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.95 ± 3.06 / 7.23 ± 3.67</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">4=</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbertje-1-gb-merged</td> <!-- Model ID -->
   <td class="num_model_parameters">74</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">21,027 ± 3,902 / 4,932 ± 1,591</td> <!-- Model inference speed -->
   <td class="score">40.19 ± 1.50</td> <!-- ScandEval score -->
   <td class="nl ner">72.51 ± 0.97 / 80.14 ± 0.74</td> <!-- CoNLL-nl -->
   <td class="nl sent">32.26 ± 2.51 / 47.44 ± 2.78</td> <!-- Dutch Social -->
   <td class="nl la">50.00 ± 2.09 / 73.38 ± 1.43</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.97 ± 0.44 / 11.08 ± 0.47</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,065 ± 472 / 1,055 ± 321</td> <!-- Model inference speed -->
   <td class="score">38.04 ± 1.71</td> <!-- ScandEval score -->
   <td class="nl ner">64.63 ± 1.54 / 49.98 ± 1.68</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.29 ± 2.22 / 40.71 ± 1.44</td> <!-- Dutch Social -->
   <td class="nl la">29.04 ± 1.85 / 63.14 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.20 ± 1.23 / 63.77 ± 0.82</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">108</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="score">36.98 ± 1.57</td> <!-- ScandEval score -->
   <td class="nl ner">75.02 ± 1.48 / 81.57 ± 0.76</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.45 ± 2.99 / 29.70 ± 1.94</td> <!-- Dutch Social -->
   <td class="nl la">45.28 ± 0.55 / 71.89 ± 0.59</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.18 ± 1.26 / 27.86 ± 1.48</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="score">36.82 ± 6.52</td> <!-- ScandEval score -->
   <td class="nl ner">78.85 ± 2.48 / 83.35 ± 2.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.80 ± 7.64 / 33.49 ± 6.73</td> <!-- Dutch Social -->
   <td class="nl la">14.56 ± 8.02 / 53.64 ± 5.14</td> <!-- ScaLA-nl -->
   <td class="nl qa">42.08 ± 7.94 / 51.94 ± 9.08</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">6</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="score">35.75 ± 3.19</td> <!-- ScandEval score -->
   <td class="nl ner">70.59 ± 1.60 / 78.25 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">21.37 ± 8.79 / 40.62 ± 7.64</td> <!-- Dutch Social -->
   <td class="nl la">45.86 ± 2.06 / 71.32 ± 1.40</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.20 ± 0.30 / 10.40 ± 0.38</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">7</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">35.41 ± 2.12</td> <!-- ScandEval score -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.14 ± 2.64 / 59.42 ± 3.10</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">8</td> <!-- Rank -->
   <td>DTAI-KULeuven/robbertje-1-gb-bort</td> <!-- Model ID -->
   <td class="num_model_parameters">45</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">31,087 ± 5,833 / 7,147 ± 2,339</td> <!-- Model inference speed -->
   <td class="score">33.52 ± 3.76</td> <!-- ScandEval score -->
   <td class="nl ner">66.74 ± 1.53 / 75.07 ± 0.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">24.93 ± 6.85 / 41.47 ± 4.05</td> <!-- Dutch Social -->
   <td class="nl la">37.19 ± 6.22 / 66.68 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl qa">5.23 ± 0.43 / 10.67 ± 0.44</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">9=</td> <!-- Rank -->
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="score">32.63 ± 5.34</td> <!-- ScandEval score -->
   <td class="nl ner">77.35 ± 2.80 / 82.50 ± 1.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.55 ± 5.33 / 28.68 ± 3.64</td> <!-- Dutch Social -->
   <td class="nl la">18.25 ± 8.41 / 54.00 ± 5.57</td> <!-- ScaLA-nl -->
   <td class="nl qa">28.37 ± 4.84 / 36.84 ± 5.92</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">9=</td> <!-- Rank -->
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="score">32.60 ± 5.41</td> <!-- ScandEval score -->
   <td class="nl ner">74.03 ± 3.05 / 80.59 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.53 ± 5.28 / 32.06 ± 4.17</td> <!-- Dutch Social -->
   <td class="nl la">39.12 ± 12.90 / 68.36 ± 6.85</td> <!-- ScaLA-nl -->
   <td class="nl qa">7.71 ± 0.42 / 12.90 ± 0.39</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">9=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">32.11 ± 1.65</td> <!-- ScandEval score -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.41 ± 0.79 / 66.24 ± 0.81</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">10</td> <!-- Rank -->
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="score">29.25 ± 4.19</td> <!-- ScandEval score -->
   <td class="nl ner">67.89 ± 1.61 / 74.48 ± 1.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">23.25 ± 6.95 / 44.88 ± 6.27</td> <!-- Dutch Social -->
   <td class="nl la">21.36 ± 7.80 / 59.50 ± 3.54</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.50 ± 0.39 / 9.94 ± 0.33</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">11=</td> <!-- Rank -->
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">93</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="score">28.24 ± 2.78</td> <!-- ScandEval score -->
   <td class="nl ner">49.54 ± 1.42 / 50.44 ± 1.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.86 ± 3.09 / 35.33 ± 1.77</td> <!-- Dutch Social -->
   <td class="nl la">27.90 ± 5.58 / 62.47 ± 3.34</td> <!-- ScaLA-nl -->
   <td class="nl qa">20.65 ± 1.02 / 29.40 ± 1.29</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">11=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">25.94 ± 2.67</td> <!-- ScandEval score -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.51 ± 2.13 / 44.59 ± 2.68</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">12=</td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="score">22.28 ± 2.68</td> <!-- ScandEval score -->
   <td class="nl ner">56.98 ± 1.37 / 66.91 ± 1.60</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.66 ± 4.65 / 31.17 ± 3.34</td> <!-- Dutch Social -->
   <td class="nl la">19.37 ± 4.34 / 56.74 ± 3.13</td> <!-- ScaLA-nl -->
   <td class="nl qa">3.11 ± 0.37 / 7.91 ± 0.25</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">12=</td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="score">21.98 ± 2.63</td> <!-- ScandEval score -->
   <td class="nl ner">58.67 ± 1.07 / 68.27 ± 0.94</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.82 ± 4.47 / 37.11 ± 2.75</td> <!-- Dutch Social -->
   <td class="nl la">9.27 ± 4.66 / 52.04 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl qa">2.17 ± 0.34 / 8.02 ± 0.41</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">13</td> <!-- Rank -->
   <td>jpostma/DagoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,241 ± 2,115 / 2,565 ± 830</td> <!-- Model inference speed -->
   <td class="score">21.29 ± 1.56</td> <!-- ScandEval score -->
   <td class="nl ner">42.28 ± 1.41 / 47.68 ± 1.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.01 ± 2.88 / 31.60 ± 2.41</td> <!-- Dutch Social -->
   <td class="nl la">31.21 ± 1.62 / 64.82 ± 0.69</td> <!-- ScaLA-nl -->
   <td class="nl qa">3.65 ± 0.33 / 9.49 ± 0.31</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">14=</td> <!-- Rank -->
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="score">14.80 ± 2.26</td> <!-- ScandEval score -->
   <td class="nl ner">44.46 ± 2.24 / 60.04 ± 1.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.39 ± 4.20 / 30.69 ± 2.83</td> <!-- Dutch Social -->
   <td class="nl la">2.07 ± 1.34 / 48.42 ± 1.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.30 ± 1.26 / 9.24 ± 1.13</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">14=</td> <!-- Rank -->
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="score">13.94 ± 1.95</td> <!-- ScandEval score -->
   <td class="nl ner">41.38 ± 2.82 / 56.29 ± 1.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.45 ± 2.80 / 29.85 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.55 ± 1.97 / 49.24 ± 1.16</td> <!-- ScaLA-nl -->
   <td class="nl qa">4.40 ± 0.22 / 6.62 ± 0.38</td> <!-- SQuAD-nl -->
  </tr>
  <tr>
   <td class="rank">15</td> <!-- Rank -->
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,319 ± 94 / 656 ± 172</td> <!-- Model inference speed -->
   <td class="score">4.05 ± 1.31</td> <!-- ScandEval score -->
   <td class="nl ner">13.09 ± 1.68 / 16.25 ± 2.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.92 ± 2.11 / 25.39 ± 1.86</td> <!-- Dutch Social -->
   <td class="nl la">1.93 ± 1.37 / 40.76 ± 4.83</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.26 ± 0.09 / 2.70 ± 1.10</td> <!-- SQuAD-nl -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/dutch-nlu.csv" target="_blank">Download as CSV</a>
</div>