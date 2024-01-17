---
layout: leaderboard
title: German NLU
---

<center>Last updated: 17/01/2024 12:56:40</center>
<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="german-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>deepset/gbert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">336</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,463 ± 874 / 1,491 ± 486</td> <!-- Model inference speed -->
   <td class="score">64.31 ± 1.48</td> <!-- ScandEval score -->
   <td class="de ner">80.99 ± 1.18 / 82.15 ± 1.14</td> <!-- GermEval -->
   <td class="de sent">66.16 ± 2.01 / 77.19 ± 1.42</td> <!-- SB10k -->
   <td class="de la">77.48 ± 1.86 / 88.36 ± 1.08</td> <!-- ScaLA-de -->
   <td class="de qa">32.63 ± 0.86 / 59.31 ± 0.92</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">1=</td> <!-- Rank -->
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="score">61.07 ± 1.89</td> <!-- ScandEval score -->
   <td class="de ner">77.85 ± 1.92 / 79.32 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">59.69 ± 2.32 / 72.69 ± 1.52</td> <!-- SB10k -->
   <td class="de la">72.25 ± 1.53 / 86.00 ± 0.81</td> <!-- ScaLA-de -->
   <td class="de qa">34.48 ± 1.79 / 54.55 ± 3.16</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">2</td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score">59.47 ± 1.61</td> <!-- ScandEval score -->
   <td class="de ner">80.30 ± 0.79 / 81.05 ± 0.86</td> <!-- GermEval -->
   <td class="de sent">59.50 ± 1.98 / 72.44 ± 1.63</td> <!-- SB10k -->
   <td class="de la">71.84 ± 2.71 / 85.57 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de qa">26.25 ± 0.97 / 48.90 ± 1.73</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,744 ± 947 / 1,059 ± 347</td> <!-- Model inference speed -->
   <td class="score">58.00 ± 4.76</td> <!-- ScandEval score -->
   <td class="de ner">79.20 ± 1.29 / 80.27 ± 1.34</td> <!-- GermEval -->
   <td class="de sent">58.44 ± 7.27 / 71.84 ± 5.22</td> <!-- SB10k -->
   <td class="de la">62.12 ± 9.02 / 80.04 ± 5.30</td> <!-- ScaLA-de -->
   <td class="de qa">32.23 ± 1.48 / 56.36 ± 1.54</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">3=</td> <!-- Rank -->
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="score">57.40 ± 1.56</td> <!-- ScandEval score -->
   <td class="de ner">78.42 ± 0.82 / 78.99 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">59.17 ± 1.96 / 72.66 ± 1.28</td> <!-- SB10k -->
   <td class="de la">61.58 ± 2.02 / 78.93 ± 1.45</td> <!-- ScaLA-de -->
   <td class="de qa">30.42 ± 1.43 / 55.28 ± 1.63</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">4</td> <!-- Rank -->
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,570 ± 1,759 / 2,635 ± 894</td> <!-- Model inference speed -->
   <td class="score">55.21 ± 1.66</td> <!-- ScandEval score -->
   <td class="de ner">80.25 ± 0.48 / 81.33 ± 0.53</td> <!-- GermEval -->
   <td class="de sent">57.77 ± 3.03 / 71.70 ± 1.94</td> <!-- SB10k -->
   <td class="de la">66.13 ± 2.07 / 81.96 ± 1.14</td> <!-- ScaLA-de -->
   <td class="de qa">16.68 ± 1.05 / 35.77 ± 1.07</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
   <td>dbmdz/bert-base-german-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,438 ± 1,997 / 2,779 ± 908</td> <!-- Model inference speed -->
   <td class="score">54.11 ± 1.80</td> <!-- ScandEval score -->
   <td class="de ner">78.08 ± 1.11 / 79.93 ± 0.97</td> <!-- GermEval -->
   <td class="de sent">56.26 ± 1.78 / 70.64 ± 1.23</td> <!-- SB10k -->
   <td class="de la">68.22 ± 3.07 / 83.39 ± 1.69</td> <!-- ScaLA-de -->
   <td class="de qa">13.87 ± 1.26 / 31.18 ± 1.97</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">5=</td> <!-- Rank -->
   <td>dbmdz/bert-base-german-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,844 ± 1,972 / 3,014 ± 986</td> <!-- Model inference speed -->
   <td class="score">53.51 ± 2.04</td> <!-- ScandEval score -->
   <td class="de ner">79.02 ± 0.65 / 80.90 ± 0.56</td> <!-- GermEval -->
   <td class="de sent">53.44 ± 1.89 / 68.72 ± 1.27</td> <!-- SB10k -->
   <td class="de la">67.08 ± 3.43 / 82.95 ± 1.78</td> <!-- ScaLA-de -->
   <td class="de qa">14.49 ± 2.19 / 32.64 ± 3.32</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">6</td> <!-- Rank -->
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="score">53.30 ± 1.58</td> <!-- ScandEval score -->
   <td class="de ner">77.93 ± 0.97 / 78.94 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">58.20 ± 2.20 / 71.95 ± 1.45</td> <!-- SB10k -->
   <td class="de la">53.53 ± 2.56 / 75.10 ± 1.39</td> <!-- ScaLA-de -->
   <td class="de qa">23.55 ± 0.57 / 45.91 ± 0.73</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">7</td> <!-- Rank -->
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,471 ± 2,152 / 2,194 ± 723</td> <!-- Model inference speed -->
   <td class="score">50.99 ± 4.25</td> <!-- ScandEval score -->
   <td class="de ner">75.98 ± 1.05 / 76.70 ± 1.42</td> <!-- GermEval -->
   <td class="de sent">57.27 ± 1.97 / 71.21 ± 1.33</td> <!-- SB10k -->
   <td class="de la">52.46 ± 11.58 / 74.00 ± 7.44</td> <!-- ScaLA-de -->
   <td class="de qa">18.24 ± 2.41 / 38.20 ± 2.88</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">8</td> <!-- Rank -->
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,116 ± 2,084 / 2,119 ± 696</td> <!-- Model inference speed -->
   <td class="score">47.20 ± 1.69</td> <!-- ScandEval score -->
   <td class="de ner">74.67 ± 1.09 / 75.55 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">63.32 ± 2.32 / 75.28 ± 1.65</td> <!-- SB10k -->
   <td class="de la">49.39 ± 3.11 / 73.04 ± 1.87</td> <!-- ScaLA-de -->
   <td class="de qa">1.43 ± 0.24 / 6.26 ± 1.14</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">9</td> <!-- Rank -->
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="score">46.92 ± 5.90</td> <!-- ScandEval score -->
   <td class="de ner">74.43 ± 2.14 / 73.96 ± 2.57</td> <!-- GermEval -->
   <td class="de sent">57.43 ± 1.86 / 71.30 ± 1.43</td> <!-- SB10k -->
   <td class="de la">35.00 ± 18.42 / 61.88 ± 13.13</td> <!-- ScaLA-de -->
   <td class="de qa">20.81 ± 1.19 / 41.69 ± 1.19</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">10</td> <!-- Rank -->
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="score">45.29 ± 1.90</td> <!-- ScandEval score -->
   <td class="de ner">71.08 ± 1.17 / 72.25 ± 1.06</td> <!-- GermEval -->
   <td class="de sent">62.00 ± 2.11 / 74.40 ± 1.38</td> <!-- SB10k -->
   <td class="de la">48.10 ± 4.34 / 71.95 ± 3.29</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">11</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">42.72 ± 2.99</td> <!-- ScandEval score -->
   <td class="de ner">46.22 ± 3.41 / 61.50 ± 2.96</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">12</td> <!-- Rank -->
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="score">42.53 ± 5.71</td> <!-- ScandEval score -->
   <td class="de ner">74.00 ± 1.42 / 74.80 ± 1.48</td> <!-- GermEval -->
   <td class="de sent">55.04 ± 3.06 / 69.65 ± 2.21</td> <!-- SB10k -->
   <td class="de la">29.15 ± 14.43 / 61.13 ± 9.16</td> <!-- ScaLA-de -->
   <td class="de qa">11.93 ± 3.95 / 22.32 ± 7.19</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">13</td> <!-- Rank -->
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="score">42.51 ± 3.74</td> <!-- ScandEval score -->
   <td class="de ner">76.46 ± 0.98 / 76.68 ± 0.91</td> <!-- GermEval -->
   <td class="de sent">59.51 ± 1.54 / 72.84 ± 1.06</td> <!-- SB10k -->
   <td class="de la">32.54 ± 11.48 / 60.57 ± 7.28</td> <!-- ScaLA-de -->
   <td class="de qa">1.53 ± 0.96 / 2.39 ± 1.52</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">14=</td> <!-- Rank -->
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,943 ± 2,072 / 2,074 ± 707</td> <!-- Model inference speed -->
   <td class="score">42.46 ± 3.70</td> <!-- ScandEval score -->
   <td class="de ner">79.33 ± 0.74 / 79.38 ± 0.80</td> <!-- GermEval -->
   <td class="de sent">58.58 ± 2.31 / 72.09 ± 1.64</td> <!-- SB10k -->
   <td class="de la">15.34 ± 5.24 / 52.99 ± 1.90</td> <!-- ScaLA-de -->
   <td class="de qa">16.58 ± 6.50 / 32.33 ± 11.35</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">14=</td> <!-- Rank -->
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,814 ± 2,015 / 2,093 ± 695</td> <!-- Model inference speed -->
   <td class="score">42.35 ± 4.28</td> <!-- ScandEval score -->
   <td class="de ner">79.61 ± 0.72 / 79.97 ± 0.60</td> <!-- GermEval -->
   <td class="de sent">58.30 ± 3.04 / 72.07 ± 2.02</td> <!-- SB10k -->
   <td class="de la">11.85 ± 7.35 / 51.92 ± 5.15</td> <!-- ScaLA-de -->
   <td class="de qa">19.63 ± 5.99 / 37.77 ± 9.50</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">15</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="score">41.73 ± 2.46</td> <!-- ScandEval score -->
   <td class="de ner">70.17 ± 0.91 / 71.80 ± 1.12</td> <!-- GermEval -->
   <td class="de sent">57.71 ± 2.22 / 71.63 ± 1.60</td> <!-- SB10k -->
   <td class="de la">38.75 ± 6.45 / 66.42 ± 4.26</td> <!-- ScaLA-de -->
   <td class="de qa">0.30 ± 0.24 / 2.03 ± 1.51</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">16</td> <!-- Rank -->
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="score">40.56 ± 1.70</td> <!-- ScandEval score -->
   <td class="de ner">64.92 ± 0.93 / 67.24 ± 1.36</td> <!-- GermEval -->
   <td class="de sent">41.36 ± 2.28 / 60.16 ± 2.09</td> <!-- SB10k -->
   <td class="de la">48.21 ± 2.81 / 71.63 ± 1.82</td> <!-- ScaLA-de -->
   <td class="de qa">7.75 ± 0.77 / 20.77 ± 1.40</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">17=</td> <!-- Rank -->
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="score">39.02 ± 3.08</td> <!-- ScandEval score -->
   <td class="de ner">68.22 ± 0.64 / 69.40 ± 0.61</td> <!-- GermEval -->
   <td class="de sent">52.68 ± 2.03 / 68.31 ± 1.34</td> <!-- SB10k -->
   <td class="de la">34.44 ± 9.47 / 64.23 ± 5.35</td> <!-- ScaLA-de -->
   <td class="de qa">0.73 ± 0.17 / 4.35 ± 1.32</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">17=</td> <!-- Rank -->
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="score">38.12 ± 1.06</td> <!-- ScandEval score -->
   <td class="de ner">64.02 ± 0.68 / 65.62 ± 0.89</td> <!-- GermEval -->
   <td class="de sent">55.60 ± 2.05 / 70.33 ± 1.38</td> <!-- SB10k -->
   <td class="de la">32.22 ± 1.30 / 63.81 ± 0.85</td> <!-- ScaLA-de -->
   <td class="de qa">0.64 ± 0.22 / 3.98 ± 1.45</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">18</td> <!-- Rank -->
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="score">33.01 ± 2.47</td> <!-- ScandEval score -->
   <td class="de ner">64.45 ± 0.73 / 66.75 ± 0.70</td> <!-- GermEval -->
   <td class="de sent">49.61 ± 1.79 / 66.07 ± 1.24</td> <!-- SB10k -->
   <td class="de la">17.60 ± 7.17 / 57.72 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de qa">0.36 ± 0.20 / 3.58 ± 1.30</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">19</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,451 ± 466 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="score">31.91 ± 2.37</td> <!-- ScandEval score -->
   <td class="de ner">33.50 ± 1.22 / 40.91 ± 1.26</td> <!-- GermEval -->
   <td class="de sent">54.31 ± 1.72 / 68.17 ± 1.17</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.08 / 57.80 ± 3.73</td> <!-- ScaLA-de -->
   <td class="de qa">16.71 ± 2.45 / 38.80 ± 3.65</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">20</td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="score">31.76 ± 1.70</td> <!-- ScandEval score -->
   <td class="de ner">52.79 ± 1.05 / 53.77 ± 1.34</td> <!-- GermEval -->
   <td class="de sent">53.53 ± 1.69 / 68.92 ± 1.15</td> <!-- SB10k -->
   <td class="de la">20.15 ± 3.91 / 55.76 ± 4.83</td> <!-- ScaLA-de -->
   <td class="de qa">0.58 ± 0.14 / 6.68 ± 1.42</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">21=</td> <!-- Rank -->
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,807 ± 4,171 / 3,323 ± 1,083</td> <!-- Model inference speed -->
   <td class="score">30.54 ± 2.10</td> <!-- ScandEval score -->
   <td class="de ner">52.41 ± 0.88 / 53.13 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">51.94 ± 1.46 / 67.85 ± 0.93</td> <!-- SB10k -->
   <td class="de la">17.74 ± 5.98 / 55.36 ± 4.55</td> <!-- ScaLA-de -->
   <td class="de qa">0.06 ± 0.06 / 0.82 ± 0.70</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">21=</td> <!-- Rank -->
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="score">17.51 ± 2.13</td> <!-- ScandEval score -->
   <td class="de ner">33.53 ± 3.44 / 34.18 ± 3.33</td> <!-- GermEval -->
   <td class="de sent">34.81 ± 3.19 / 55.72 ± 2.24</td> <!-- SB10k -->
   <td class="de la">1.25 ± 1.54 / 48.35 ± 1.50</td> <!-- ScaLA-de -->
   <td class="de qa">0.46 ± 0.37 / 3.29 ± 2.33</td> <!-- GermanQuAD -->
  </tr>
  <tr>
   <td class="rank">22</td> <!-- Rank -->
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,237 ± 120 / 1,441 ± 325</td> <!-- Model inference speed -->
   <td class="score">4.83 ± 2.52</td> <!-- ScandEval score -->
   <td class="de ner">9.75 ± 0.87 / 9.42 ± 0.82</td> <!-- GermEval -->
   <td class="de sent">9.76 ± 8.55 / 28.33 ± 9.75</td> <!-- SB10k -->
   <td class="de la">-0.18 ± 0.64 / 33.67 ± 0.62</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlu.csv" target="_blank">Download as CSV</a>
</div>