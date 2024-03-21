---
layout: leaderboard
title: German NLU
---

<center>Last updated: 21/03/2024 14:59:49 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="german-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermEval">GermEval version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SB10k">SB10k version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-de">ScaLA-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermanQuAD">GermanQuAD version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>deepset/gbert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,463 ± 874 / 1,491 ± 486</td> <!-- Model inference speed -->
   <td class="rank">1.04</td> <!-- ScandEval rank -->
   <td class="de ner">82.15 ± 1.14 / 80.99 ± 1.18</td> <!-- GermEval -->
   <td class="de sent">66.16 ± 2.01 / 77.19 ± 1.42</td> <!-- SB10k -->
   <td class="de la">77.48 ± 1.86 / 88.36 ± 1.08</td> <!-- ScaLA-de -->
   <td class="de qa">32.63 ± 0.86 / 59.31 ± 0.92</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,355 ± 475 / 1,002 ± 312</td> <!-- Model inference speed -->
   <td class="rank">1.18</td> <!-- ScandEval rank -->
   <td class="de ner">79.32 ± 1.76 / 77.85 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">59.69 ± 2.32 / 72.69 ± 1.52</td> <!-- SB10k -->
   <td class="de la">72.25 ± 1.53 / 86.00 ± 0.81</td> <!-- ScaLA-de -->
   <td class="de qa">34.48 ± 1.79 / 54.55 ± 3.16</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">1.26</td> <!-- ScandEval rank -->
   <td class="de ner">80.27 ± 1.34 / 79.20 ± 1.29</td> <!-- GermEval -->
   <td class="de sent">58.44 ± 7.27 / 71.84 ± 5.22</td> <!-- SB10k -->
   <td class="de la">62.12 ± 9.02 / 80.04 ± 5.30</td> <!-- ScaLA-de -->
   <td class="de qa">32.23 ± 1.48 / 56.36 ± 1.54</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="de ner">81.05 ± 0.86 / 80.30 ± 0.79</td> <!-- GermEval -->
   <td class="de sent">59.50 ± 1.98 / 72.44 ± 1.63</td> <!-- SB10k -->
   <td class="de la">71.84 ± 2.71 / 85.57 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de qa">26.25 ± 0.97 / 48.90 ± 1.73</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,305 ± 3,306 / 2,414 ± 780</td> <!-- Model inference speed -->
   <td class="rank">1.40</td> <!-- ScandEval rank -->
   <td class="de ner">78.99 ± 0.87 / 78.42 ± 0.82</td> <!-- GermEval -->
   <td class="de sent">59.17 ± 1.96 / 72.66 ± 1.28</td> <!-- SB10k -->
   <td class="de la">61.58 ± 2.02 / 78.93 ± 1.45</td> <!-- ScaLA-de -->
   <td class="de qa">30.42 ± 1.43 / 55.28 ± 1.63</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">16,043 ± 2,590 / 4,268 ± 1,377</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="de ner">81.33 ± 0.53 / 80.25 ± 0.48</td> <!-- GermEval -->
   <td class="de sent">57.77 ± 3.03 / 71.70 ± 1.94</td> <!-- SB10k -->
   <td class="de la">66.13 ± 2.07 / 81.96 ± 1.14</td> <!-- ScaLA-de -->
   <td class="de qa">16.68 ± 1.05 / 35.77 ± 1.07</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,386 ± 3,349 / 2,435 ± 787</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="de ner">78.94 ± 0.98 / 77.93 ± 0.97</td> <!-- GermEval -->
   <td class="de sent">58.20 ± 2.20 / 71.95 ± 1.45</td> <!-- SB10k -->
   <td class="de la">53.53 ± 2.56 / 75.10 ± 1.39</td> <!-- ScaLA-de -->
   <td class="de qa">23.55 ± 0.57 / 45.91 ± 0.73</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-german-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,844 ± 1,972 / 3,014 ± 986</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="de ner">80.90 ± 0.56 / 79.02 ± 0.65</td> <!-- GermEval -->
   <td class="de sent">53.44 ± 1.89 / 68.72 ± 1.27</td> <!-- SB10k -->
   <td class="de la">67.08 ± 3.43 / 82.95 ± 1.78</td> <!-- ScaLA-de -->
   <td class="de qa">14.49 ± 2.19 / 32.64 ± 3.32</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-german-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,438 ± 1,997 / 2,779 ± 908</td> <!-- Model inference speed -->
   <td class="rank">1.74</td> <!-- ScandEval rank -->
   <td class="de ner">79.93 ± 0.97 / 78.08 ± 1.11</td> <!-- GermEval -->
   <td class="de sent">56.26 ± 1.78 / 70.64 ± 1.23</td> <!-- SB10k -->
   <td class="de la">68.22 ± 3.07 / 83.39 ± 1.69</td> <!-- ScaLA-de -->
   <td class="de qa">13.87 ± 1.26 / 31.18 ± 1.97</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,471 ± 2,152 / 2,194 ± 723</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="de ner">76.70 ± 1.42 / 75.98 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">57.27 ± 1.97 / 71.21 ± 1.33</td> <!-- SB10k -->
   <td class="de la">52.46 ± 11.58 / 74.00 ± 7.44</td> <!-- ScaLA-de -->
   <td class="de qa">18.24 ± 2.41 / 38.20 ± 2.88</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="rank">1.89</td> <!-- ScandEval rank -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,135 ± 3,232 / 2,442 ± 778</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="de ner">73.96 ± 2.57 / 74.43 ± 2.14</td> <!-- GermEval -->
   <td class="de sent">57.43 ± 1.86 / 71.30 ± 1.43</td> <!-- SB10k -->
   <td class="de la">35.00 ± 18.42 / 61.88 ± 13.13</td> <!-- ScaLA-de -->
   <td class="de qa">20.81 ± 1.19 / 41.69 ± 1.19</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de qa">25.22 ± 3.76 / 60.93 ± 2.96</td> <!-- GermanQuAD -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>9.3.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,918 ± 2,938 / 3,330 ± 1,088</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="de ner">79.97 ± 0.60 / 79.61 ± 0.72</td> <!-- GermEval -->
   <td class="de sent">58.30 ± 3.04 / 72.07 ± 2.02</td> <!-- SB10k -->
   <td class="de la">11.85 ± 7.35 / 51.92 ± 5.15</td> <!-- ScaLA-de -->
   <td class="de qa">19.63 ± 5.99 / 37.77 ± 9.50</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="de ner">48.11 ± 2.01 / 39.66 ± 3.29</td> <!-- GermEval -->
   <td class="de sent">54.96 ± 2.69 / 69.64 ± 2.09</td> <!-- SB10k -->
   <td class="de la">21.57 ± 4.18 / 55.63 ± 4.56</td> <!-- ScaLA-de -->
   <td class="de qa">31.49 ± 3.11 / 61.33 ± 3.41</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,837 ± 2,928 / 3,264 ± 1,046</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="de ner">75.55 ± 0.87 / 74.67 ± 1.09</td> <!-- GermEval -->
   <td class="de sent">63.32 ± 2.32 / 75.28 ± 1.65</td> <!-- SB10k -->
   <td class="de la">49.39 ± 3.11 / 73.04 ± 1.87</td> <!-- ScaLA-de -->
   <td class="de qa">1.43 ± 0.24 / 6.26 ± 1.14</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,299 ± 910 / 1,415 ± 451</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="de ner">74.80 ± 1.48 / 74.00 ± 1.42</td> <!-- GermEval -->
   <td class="de sent">55.04 ± 3.06 / 69.65 ± 2.21</td> <!-- SB10k -->
   <td class="de la">29.15 ± 14.43 / 61.13 ± 9.16</td> <!-- ScaLA-de -->
   <td class="de qa">11.93 ± 3.95 / 22.32 ± 7.19</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="de ner">79.38 ± 0.80 / 79.33 ± 0.74</td> <!-- GermEval -->
   <td class="de sent">58.58 ± 2.31 / 72.09 ± 1.64</td> <!-- SB10k -->
   <td class="de la">15.34 ± 5.24 / 52.99 ± 1.90</td> <!-- ScaLA-de -->
   <td class="de qa">16.58 ± 6.50 / 32.33 ± 11.35</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="de ner">72.25 ± 1.06 / 71.08 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">62.00 ± 2.11 / 74.40 ± 1.38</td> <!-- SB10k -->
   <td class="de la">48.10 ± 4.34 / 71.95 ± 3.29</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">22.94 ± 3.05 / 47.19 ± 4.45</td> <!-- GermanQuAD -->
   <td>9.1.2</td> <!-- GermEval version -->
   <td>9.1.2</td> <!-- SB10k version -->
   <td>9.1.2</td> <!-- ScaLA-de version -->
   <td>9.1.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="de ner">47.74 ± 1.95 / 41.60 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de qa">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="de ner">56.71 ± 1.34 / 47.69 ± 2.04</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.03 / 62.42 ± 3.31</td> <!-- SB10k -->
   <td class="de la">19.92 ± 3.22 / 52.83 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de qa">27.87 ± 2.01 / 57.64 ± 2.05</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="de ner">51.79 ± 0.92 / 36.09 ± 1.73</td> <!-- GermEval -->
   <td class="de sent">47.27 ± 3.06 / 63.50 ± 2.88</td> <!-- SB10k -->
   <td class="de la">22.15 ± 1.83 / 56.64 ± 4.04</td> <!-- ScaLA-de -->
   <td class="de qa">24.30 ± 3.79 / 54.51 ± 4.48</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="de ner">76.68 ± 0.91 / 76.46 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">59.51 ± 1.54 / 72.84 ± 1.06</td> <!-- SB10k -->
   <td class="de la">32.54 ± 11.48 / 60.57 ± 7.28</td> <!-- ScaLA-de -->
   <td class="de qa">1.53 ± 0.96 / 2.39 ± 1.52</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="de ner">55.15 ± 1.17 / 41.83 ± 1.49</td> <!-- GermEval -->
   <td class="de sent">47.85 ± 2.29 / 65.02 ± 1.69</td> <!-- SB10k -->
   <td class="de la">24.29 ± 2.18 / 60.90 ± 1.65</td> <!-- ScaLA-de -->
   <td class="de qa">23.98 ± 2.16 / 57.70 ± 1.94</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.2.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM_German_7b_v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,972 ± 315 / 689 ± 204</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="de ner">42.48 ± 2.68 / 32.20 ± 1.31</td> <!-- GermEval -->
   <td class="de sent">48.67 ± 3.85 / 59.21 ± 4.18</td> <!-- SB10k -->
   <td class="de la">8.72 ± 2.15 / 43.37 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">34.07 ± 3.77 / 65.17 ± 3.27</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,994 ± 2,975 / 3,374 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="de ner">71.80 ± 1.12 / 70.17 ± 0.91</td> <!-- GermEval -->
   <td class="de sent">57.71 ± 2.22 / 71.63 ± 1.60</td> <!-- SB10k -->
   <td class="de la">38.75 ± 6.45 / 66.42 ± 4.26</td> <!-- ScaLA-de -->
   <td class="de qa">0.30 ± 0.24 / 2.03 ± 1.51</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mayflowergmbh/Wiedervereinigung-7b-dpo (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,374 ± 432 / 744 ± 230</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="de ner">53.57 ± 3.49 / 40.72 ± 3.06</td> <!-- GermEval -->
   <td class="de sent">51.92 ± 3.19 / 67.12 ± 2.11</td> <!-- SB10k -->
   <td class="de la">29.06 ± 5.04 / 62.77 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de qa">15.01 ± 2.99 / 50.63 ± 3.70</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="de ner">44.97 ± 1.75 / 35.79 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">53.14 ± 2.67 / 67.89 ± 2.15</td> <!-- SB10k -->
   <td class="de la">7.64 ± 2.47 / 37.95 ± 2.67</td> <!-- ScaLA-de -->
   <td class="de qa">30.12 ± 1.55 / 57.17 ± 2.38</td> <!-- GermanQuAD -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>10.0.0</td> <!-- SB10k version -->
   <td>10.0.0</td> <!-- ScaLA-de version -->
   <td>9.3.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,165 ± 3,028 / 3,385 ± 1,115</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="de ner">67.24 ± 1.36 / 64.92 ± 0.93</td> <!-- GermEval -->
   <td class="de sent">41.36 ± 2.28 / 60.16 ± 2.09</td> <!-- SB10k -->
   <td class="de la">48.21 ± 2.81 / 71.63 ± 1.82</td> <!-- ScaLA-de -->
   <td class="de qa">7.75 ± 0.77 / 20.77 ± 1.40</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="de ner">50.00 ± 1.33 / 38.45 ± 1.68</td> <!-- GermEval -->
   <td class="de sent">46.54 ± 2.92 / 63.66 ± 2.14</td> <!-- SB10k -->
   <td class="de la">15.30 ± 1.79 / 55.12 ± 1.92</td> <!-- ScaLA-de -->
   <td class="de qa">25.57 ± 3.57 / 56.05 ± 3.74</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="de ner">69.40 ± 0.61 / 68.22 ± 0.64</td> <!-- GermEval -->
   <td class="de sent">52.68 ± 2.03 / 68.31 ± 1.34</td> <!-- SB10k -->
   <td class="de la">34.44 ± 9.47 / 64.23 ± 5.35</td> <!-- ScaLA-de -->
   <td class="de qa">0.73 ± 0.17 / 4.35 ± 1.32</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,428 ± 3,628 / 3,529 ± 1,171</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="de ner">65.62 ± 0.89 / 64.02 ± 0.68</td> <!-- GermEval -->
   <td class="de sent">55.60 ± 2.05 / 70.33 ± 1.38</td> <!-- SB10k -->
   <td class="de la">32.22 ± 1.30 / 63.81 ± 0.85</td> <!-- ScaLA-de -->
   <td class="de qa">0.64 ± 0.22 / 3.98 ± 1.45</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="de ner">39.09 ± 2.92 / 31.71 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">47.83 ± 2.81 / 60.24 ± 3.30</td> <!-- SB10k -->
   <td class="de la">10.31 ± 2.60 / 46.65 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">26.13 ± 3.79 / 53.13 ± 4.50</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="de ner">68.39 ± 0.98 / 67.24 ± 1.10</td> <!-- GermEval -->
   <td class="de sent">45.91 ± 3.76 / 62.57 ± 3.33</td> <!-- SB10k -->
   <td class="de la">2.79 ± 2.11 / 39.08 ± 4.38</td> <!-- ScaLA-de -->
   <td class="de qa">18.83 ± 1.45 / 35.01 ± 2.44</td> <!-- GermanQuAD -->
   <td>10.0.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>10.0.1</td> <!-- ScaLA-de version -->
   <td>10.0.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="de ner">67.24 ± 1.51 / 66.01 ± 1.32</td> <!-- GermEval -->
   <td class="de sent">45.84 ± 2.11 / 63.35 ± 1.48</td> <!-- SB10k -->
   <td class="de la">2.28 ± 1.62 / 35.18 ± 2.11</td> <!-- ScaLA-de -->
   <td class="de qa">18.17 ± 1.85 / 33.37 ± 2.80</td> <!-- GermanQuAD -->
   <td>10.0.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>10.0.1</td> <!-- ScaLA-de version -->
   <td>10.0.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="de ner">31.51 ± 8.45 / 28.51 ± 7.54</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de qa">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="de ner">55.47 ± 0.33 / 41.46 ± 3.01</td> <!-- GermEval -->
   <td class="de sent">55.91 ± 2.49 / 70.31 ± 1.76</td> <!-- SB10k -->
   <td class="de la">22.47 ± 3.37 / 56.77 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">3.85 ± 1.44 / 42.38 ± 3.92</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="de ner">41.88 ± 1.87 / 31.88 ± 1.77</td> <!-- GermEval -->
   <td class="de sent">50.17 ± 2.52 / 65.78 ± 1.89</td> <!-- SB10k -->
   <td class="de la">15.82 ± 2.45 / 53.27 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">18.35 ± 2.70 / 39.71 ± 4.79</td> <!-- GermanQuAD -->
   <td>9.2.0</td> <!-- GermEval version -->
   <td>9.2.0</td> <!-- SB10k version -->
   <td>9.2.0</td> <!-- ScaLA-de version -->
   <td>9.2.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="de ner">50.46 ± 2.44 / 41.15 ± 3.05</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de qa">7.23 ± 2.21 / 44.27 ± 2.77</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.2.0</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,151 ± 5,903 / 5,196 ± 1,675</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="de ner">66.75 ± 0.70 / 64.45 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">49.61 ± 1.79 / 66.07 ± 1.24</td> <!-- SB10k -->
   <td class="de la">17.60 ± 7.17 / 57.72 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de qa">0.36 ± 0.20 / 3.58 ± 1.30</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,344 ± 5,907 / 5,202 ± 1,679</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="de ner">53.77 ± 1.34 / 52.79 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">53.53 ± 1.69 / 68.92 ± 1.15</td> <!-- SB10k -->
   <td class="de la">20.15 ± 3.91 / 55.76 ± 4.83</td> <!-- ScaLA-de -->
   <td class="de qa">0.58 ± 0.14 / 6.68 ± 1.42</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,807 ± 4,171 / 3,323 ± 1,083</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="de ner">53.13 ± 0.87 / 52.41 ± 0.88</td> <!-- GermEval -->
   <td class="de sent">51.94 ± 1.46 / 67.85 ± 0.93</td> <!-- SB10k -->
   <td class="de la">17.74 ± 5.98 / 55.36 ± 4.55</td> <!-- ScaLA-de -->
   <td class="de qa">0.06 ± 0.06 / 0.82 ± 0.70</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="de ner">21.52 ± 6.77 / 20.73 ± 6.40</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de qa">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="de ner">35.78 ± 2.37 / 26.98 ± 1.75</td> <!-- GermEval -->
   <td class="de sent">34.13 ± 7.00 / 46.96 ± 8.23</td> <!-- SB10k -->
   <td class="de la">2.18 ± 1.60 / 38.27 ± 3.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.99 ± 4.02 / 38.26 ± 5.37</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="de ner">34.53 ± 1.35 / 26.72 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de qa">23.48 ± 0.97 / 51.64 ± 1.00</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="de ner">14.07 ± 3.23 / 13.30 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.54 ± 5.12 / 49.63 ± 5.78</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.40 ± 3.28 / 45.47 ± 3.32</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="de ner">26.77 ± 2.51 / 22.36 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de qa">16.36 ± 3.23 / 41.95 ± 4.35</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.44</td> <!-- ScandEval rank -->
   <td class="de ner">6.64 ± 2.06 / 9.38 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de qa">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">15,177 ± 2,980 / 3,410 ± 1,076</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="de ner">34.18 ± 3.33 / 33.53 ± 3.44</td> <!-- GermEval -->
   <td class="de sent">34.81 ± 3.19 / 55.72 ± 2.24</td> <!-- SB10k -->
   <td class="de la">1.25 ± 1.54 / 48.35 ± 1.50</td> <!-- ScaLA-de -->
   <td class="de qa">0.46 ± 0.37 / 3.29 ± 2.33</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="de ner">25.84 ± 2.87 / 24.60 ± 2.60</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de qa">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.82</td> <!-- ScandEval rank -->
   <td class="de ner">21.01 ± 1.58 / 20.34 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de qa">13.61 ± 1.64 / 29.08 ± 1.96</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="de ner">21.18 ± 1.20 / 20.51 ± 1.37</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de qa">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,219 ± 712 / 3,276 ± 803</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="de ner">9.42 ± 0.82 / 9.75 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">9.76 ± 8.55 / 28.33 ± 9.75</td> <!-- SB10k -->
   <td class="de la">-0.18 ± 0.64 / 33.67 ± 0.62</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 14.60 ± 0.67</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.55</td> <!-- ScandEval rank -->
   <td class="de ner">0.30 ± 0.60 / 0.26 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">0.29 ± 1.28 / 17.22 ± 1.25</td> <!-- SB10k -->
   <td class="de la">-0.11 ± 1.16 / 36.65 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.54 ± 0.12</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>11.0.0</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;German NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-I9boM&quot; src=&quot;https://datawrapper.dwcdn.net/I9boM/29/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
