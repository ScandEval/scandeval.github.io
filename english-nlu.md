---
layout: leaderboard
title: English NLU
---

<center>Last updated: 07/02/2024 10:05:33 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English question answering - Exact Match / F1-score">SQuAD</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1</td> <!-- Rank -->
   <td>microsoft/deberta-v3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">434</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,521 ± 639 / 440 ± 143</td> <!-- Model inference speed -->
   <td class="score">76.37 ± 1.12</td> <!-- ScandEval score -->
   <td class="en ner">91.88 ± 0.70 / 91.67 ± 0.56</td> <!-- CoNLL-en -->
   <td class="en sent">64.04 ± 1.59 / 67.00 ± 1.56</td> <!-- SST5 -->
   <td class="en la">75.10 ± 1.18 / 87.34 ± 0.67</td> <!-- ScaLA-en -->
   <td class="en qa">74.47 ± 1.03 / 85.54 ± 0.79</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2</td> <!-- Rank -->
   <td>microsoft/deberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">184</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,367 ± 1,408 / 892 ± 292</td> <!-- Model inference speed -->
   <td class="score">72.66 ± 0.91</td> <!-- ScandEval score -->
   <td class="en ner">91.57 ± 0.52 / 91.20 ± 0.41</td> <!-- CoNLL-en -->
   <td class="en sent">61.66 ± 0.85 / 60.80 ± 2.63</td> <!-- SST5 -->
   <td class="en la">68.74 ± 1.72 / 83.85 ± 1.05</td> <!-- ScaLA-en -->
   <td class="en qa">68.69 ± 0.56 / 80.29 ± 0.36</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3</td> <!-- Rank -->
   <td>google/electra-base-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,977 ± 2,342 / 1,855 ± 603</td> <!-- Model inference speed -->
   <td class="score">69.88 ± 1.24</td> <!-- ScandEval score -->
   <td class="en ner">89.83 ± 0.47 / 88.64 ± 0.50</td> <!-- CoNLL-en -->
   <td class="en sent">63.55 ± 1.20 / 60.22 ± 2.49</td> <!-- SST5 -->
   <td class="en la">67.87 ± 1.58 / 83.57 ± 0.86</td> <!-- ScaLA-en -->
   <td class="en qa">58.27 ± 1.71 / 69.68 ± 1.34</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4</td> <!-- Rank -->
   <td>roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,542 ± 1,120 / 845 ± 267</td> <!-- Model inference speed -->
   <td class="score">68.61 ± 4.81</td> <!-- ScandEval score -->
   <td class="en ner">91.53 ± 0.85 / 91.21 ± 0.76</td> <!-- CoNLL-en -->
   <td class="en sent">62.92 ± 1.84 / 62.60 ± 3.18</td> <!-- SST5 -->
   <td class="en la">48.77 ± 15.71 / 71.46 ± 10.95</td> <!-- ScaLA-en -->
   <td class="en qa">71.23 ± 0.84 / 81.98 ± 0.65</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="score">67.64 ± 1.51</td> <!-- ScandEval score -->
   <td class="en ner">91.00 ± 0.40 / 90.70 ± 0.31</td> <!-- CoNLL-en -->
   <td class="en sent">59.54 ± 1.98 / 59.76 ± 3.06</td> <!-- SST5 -->
   <td class="en la">57.29 ± 2.88 / 77.93 ± 1.57</td> <!-- ScaLA-en -->
   <td class="en qa">62.75 ± 0.77 / 73.75 ± 0.74</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="score">67.45 ± 1.13</td> <!-- ScandEval score -->
   <td class="en ner">91.83 ± 0.50 / 91.40 ± 0.43</td> <!-- CoNLL-en -->
   <td class="en sent">53.75 ± 1.47 / 56.40 ± 2.82</td> <!-- SST5 -->
   <td class="en la">62.11 ± 1.53 / 80.67 ± 0.77</td> <!-- ScaLA-en -->
   <td class="en qa">62.10 ± 1.03 / 73.26 ± 0.85</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>bert-large-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">333</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,051 ± 981 / 1,147 ± 372</td> <!-- Model inference speed -->
   <td class="score">66.70 ± 1.16</td> <!-- ScandEval score -->
   <td class="en ner">89.84 ± 0.48 / 89.25 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">58.19 ± 1.32 / 58.14 ± 1.69</td> <!-- SST5 -->
   <td class="en la">63.62 ± 1.90 / 80.92 ± 1.03</td> <!-- ScaLA-en -->
   <td class="en qa">55.17 ± 0.92 / 67.33 ± 0.89</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>bert-large-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,711 ± 1,074 / 933 ± 302</td> <!-- Model inference speed -->
   <td class="score">64.60 ± 1.29</td> <!-- ScandEval score -->
   <td class="en ner">88.80 ± 0.53 / 87.48 ± 0.71</td> <!-- CoNLL-en -->
   <td class="en sent">57.94 ± 1.17 / 58.50 ± 2.31</td> <!-- SST5 -->
   <td class="en la">59.27 ± 2.55 / 79.17 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">52.38 ± 0.93 / 63.79 ± 1.19</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>distilroberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,448 ± 4,387 / 3,147 ± 998</td> <!-- Model inference speed -->
   <td class="score">62.59 ± 1.38</td> <!-- ScandEval score -->
   <td class="en ner">90.04 ± 0.53 / 89.35 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">56.08 ± 1.30 / 57.56 ± 1.96</td> <!-- SST5 -->
   <td class="en la">54.90 ± 2.47 / 76.59 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en qa">49.36 ± 1.22 / 59.73 ± 1.02</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">61.80 ± 2.33</td> <!-- ScandEval score -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8</td> <!-- Rank -->
   <td>google/electra-large-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,700 ± 1,068 / 930 ± 301</td> <!-- Model inference speed -->
   <td class="score">60.52 ± 12.36</td> <!-- ScandEval score -->
   <td class="en ner">67.87 ± 20.05 / 67.30 ± 19.58</td> <!-- CoNLL-en -->
   <td class="en sent">48.08 ± 14.91 / 53.81 ± 10.11</td> <!-- SST5 -->
   <td class="en la">55.46 ± 13.66 / 75.80 ± 8.43</td> <!-- ScaLA-en -->
   <td class="en qa">70.66 ± 0.80 / 81.84 ± 0.57</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9</td> <!-- Rank -->
   <td>bert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,296 ± 2,425 / 1,918 ± 624</td> <!-- Model inference speed -->
   <td class="score">60.24 ± 1.60</td> <!-- ScandEval score -->
   <td class="en ner">87.62 ± 0.60 / 86.68 ± 0.57</td> <!-- CoNLL-en -->
   <td class="en sent">54.01 ± 1.49 / 54.63 ± 2.14</td> <!-- SST5 -->
   <td class="en la">56.97 ± 2.20 / 77.43 ± 1.23</td> <!-- ScaLA-en -->
   <td class="en qa">42.37 ± 2.12 / 53.78 ± 2.04</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10</td> <!-- Rank -->
   <td>xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="score">59.05 ± 9.52</td> <!-- ScandEval score -->
   <td class="en ner">89.81 ± 0.60 / 89.25 ± 0.72</td> <!-- CoNLL-en -->
   <td class="en sent">41.97 ± 17.48 / 50.33 ± 9.16</td> <!-- SST5 -->
   <td class="en la">35.55 ± 18.61 / 63.79 ± 12.17</td> <!-- ScaLA-en -->
   <td class="en qa">68.88 ± 1.40 / 79.18 ± 1.17</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11</td> <!-- Rank -->
   <td>bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="score">56.18 ± 4.12</td> <!-- ScandEval score -->
   <td class="en ner">89.32 ± 0.47 / 88.95 ± 0.35</td> <!-- CoNLL-en -->
   <td class="en sent">41.89 ± 1.50 / 47.23 ± 0.75</td> <!-- SST5 -->
   <td class="en la">38.34 ± 12.84 / 67.51 ± 6.66</td> <!-- ScaLA-en -->
   <td class="en qa">55.19 ± 1.66 / 66.42 ± 1.46</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">55.32 ± 2.71</td> <!-- ScandEval score -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">58.79 ± 1.97 / 69.65 ± 2.00</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">12=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">54.85 ± 2.12</td> <!-- ScandEval score -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.46 ± 1.74 / 81.96 ± 0.56</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>distilbert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">65</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,667 ± 3,904 / 4,323 ± 1,422</td> <!-- Model inference speed -->
   <td class="score">53.52 ± 1.45</td> <!-- ScandEval score -->
   <td class="en ner">84.75 ± 0.61 / 84.65 ± 0.45</td> <!-- CoNLL-en -->
   <td class="en sent">50.94 ± 1.56 / 53.60 ± 2.13</td> <!-- SST5 -->
   <td class="en la">53.47 ± 1.86 / 75.70 ± 1.27</td> <!-- ScaLA-en -->
   <td class="en qa">24.93 ± 1.75 / 35.60 ± 2.05</td> <!-- SQuAD -->
  </tr>
  <tr class="merged-model">
   <td class="rank">13=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">53.52 ± 2.69</td> <!-- ScandEval score -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.35 ± 1.25</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">14</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">53.00 ± 1.47</td> <!-- ScandEval score -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.54 ± 1.41 / 80.82 ± 0.81</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">15</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">49.24 ± 2.31</td> <!-- ScandEval score -->
   <td class="en ner">53.39 ± 2.97 / 47.76 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">65.21 ± 1.35 / 65.73 ± 1.61</td> <!-- SST5 -->
   <td class="en la">12.63 ± 2.60 / 50.10 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en qa">65.74 ± 2.31 / 77.95 ± 1.84</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="score">48.49 ± 1.75</td> <!-- ScandEval score -->
   <td class="en ner">87.70 ± 0.68 / 87.67 ± 0.59</td> <!-- CoNLL-en -->
   <td class="en sent">36.48 ± 3.00 / 45.07 ± 1.32</td> <!-- SST5 -->
   <td class="en la">40.79 ± 2.42 / 68.71 ± 2.04</td> <!-- ScaLA-en -->
   <td class="en qa">29.00 ± 0.89 / 40.37 ± 0.77</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">46.38 ± 2.67</td> <!-- ScandEval score -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">44.64 ± 3.00 / 53.75 ± 3.18</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">16=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">44.96 ± 2.68</td> <!-- ScandEval score -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en qa">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">17</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">19.34 ± 4.37</td> <!-- ScandEval score -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.70 ± 2.02 / 50.85 ± 1.85</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">18=</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">1.77 ± 1.95</td> <!-- ScandEval score -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">-0.28 ± 0.83 / 20.27 ± 0.75</td> <!-- SST5 -->
   <td class="en la">0.25 ± 1.90 / 37.98 ± 2.75</td> <!-- ScaLA-en -->
   <td class="en qa">5.57 ± 3.10 / 11.14 ± 4.67</td> <!-- SQuAD -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">18=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">0.10 ± 0.14</td> <!-- ScandEval score -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en qa">0.00 ± 0.00 / 3.66 ± 0.43</td> <!-- SQuAD -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/english-nlu.csv" target="_blank">Download as CSV</a>
</div>