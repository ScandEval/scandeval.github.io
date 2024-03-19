---
layout: leaderboard
title: English NLU
---

<center>Last updated: 19/03/2024 19:07:12 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlu-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English question answering - Exact Match / F1-score">SQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-en">CoNLL-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SST5">SST5 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-en">ScaLA-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD">SQuAD version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>microsoft/deberta-v3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">434</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,521 ± 639 / 440 ± 143</td> <!-- Model inference speed -->
   <td class="rank">1.08</td> <!-- ScandEval rank -->
   <td class="en ner">91.88 ± 0.70 / 91.67 ± 0.56</td> <!-- CoNLL-en -->
   <td class="en sent">64.04 ± 1.59 / 67.00 ± 1.56</td> <!-- SST5 -->
   <td class="en la">75.10 ± 1.18 / 87.34 ± 0.67</td> <!-- ScaLA-en -->
   <td class="en qa">74.47 ± 1.03 / 85.54 ± 0.79</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/deberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">184</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,367 ± 1,408 / 892 ± 292</td> <!-- Model inference speed -->
   <td class="rank">1.28</td> <!-- ScandEval rank -->
   <td class="en ner">91.57 ± 0.52 / 91.20 ± 0.41</td> <!-- CoNLL-en -->
   <td class="en sent">61.66 ± 0.85 / 60.80 ± 2.63</td> <!-- SST5 -->
   <td class="en la">68.74 ± 1.72 / 83.85 ± 1.05</td> <!-- ScaLA-en -->
   <td class="en qa">68.69 ± 0.56 / 80.29 ± 0.36</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,542 ± 1,120 / 845 ± 267</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="en ner">91.53 ± 0.85 / 91.21 ± 0.76</td> <!-- CoNLL-en -->
   <td class="en sent">62.92 ± 1.84 / 62.60 ± 3.18</td> <!-- SST5 -->
   <td class="en la">48.77 ± 15.71 / 71.46 ± 10.95</td> <!-- ScaLA-en -->
   <td class="en qa">71.23 ± 0.84 / 81.98 ± 0.65</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,244 ± 510 / 3,515 ± 848</td> <!-- Model inference speed -->
   <td class="rank">1.40</td> <!-- ScandEval rank -->
   <td class="en ner">78.06 ± 2.73 / 70.76 ± 3.80</td> <!-- CoNLL-en -->
   <td class="en sent">69.06 ± 2.20 / 76.04 ± 1.60</td> <!-- SST5 -->
   <td class="en la">55.76 ± 3.84 / 76.34 ± 1.44</td> <!-- ScaLA-en -->
   <td class="en qa">67.35 ± 1.98 / 85.76 ± 0.77</td> <!-- SQuAD -->
   <td>12.2.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.2.0</td> <!-- ScaLA-en version -->
   <td>12.2.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/electra-base-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,977 ± 2,342 / 1,855 ± 603</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="en ner">89.83 ± 0.47 / 88.64 ± 0.50</td> <!-- CoNLL-en -->
   <td class="en sent">63.55 ± 1.20 / 60.22 ± 2.49</td> <!-- SST5 -->
   <td class="en la">67.87 ± 1.58 / 83.57 ± 0.86</td> <!-- ScaLA-en -->
   <td class="en qa">58.27 ± 1.71 / 69.68 ± 1.34</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="rank">1.54</td> <!-- ScandEval rank -->
   <td class="en ner">91.00 ± 0.40 / 90.70 ± 0.31</td> <!-- CoNLL-en -->
   <td class="en sent">59.54 ± 1.98 / 59.76 ± 3.06</td> <!-- SST5 -->
   <td class="en la">57.29 ± 2.88 / 77.93 ± 1.57</td> <!-- ScaLA-en -->
   <td class="en qa">62.75 ± 0.77 / 73.75 ± 0.74</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="en ner">89.53 ± 0.40 / 89.37 ± 0.30</td> <!-- CoNLL-en -->
   <td class="en sent">53.90 ± 1.96 / 54.63 ± 2.32</td> <!-- SST5 -->
   <td class="en la">55.31 ± 2.36 / 76.38 ± 1.93</td> <!-- ScaLA-en -->
   <td class="en qa">69.89 ± 0.99 / 80.82 ± 0.97</td> <!-- SQuAD -->
   <td>10.0.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>10.0.1</td> <!-- ScaLA-en version -->
   <td>10.0.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,237 ± 1,562 / 2,258 ± 742</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
   <td class="en ner">91.83 ± 0.50 / 91.40 ± 0.43</td> <!-- CoNLL-en -->
   <td class="en sent">53.75 ± 1.47 / 56.40 ± 2.82</td> <!-- SST5 -->
   <td class="en la">62.11 ± 1.53 / 80.67 ± 0.77</td> <!-- ScaLA-en -->
   <td class="en qa">62.10 ± 1.03 / 73.26 ± 0.85</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="en ner">89.48 ± 0.86 / 89.32 ± 0.69</td> <!-- CoNLL-en -->
   <td class="en sent">51.88 ± 6.25 / 56.03 ± 4.61</td> <!-- SST5 -->
   <td class="en la">50.69 ± 4.90 / 73.54 ± 2.97</td> <!-- ScaLA-en -->
   <td class="en qa">69.46 ± 1.02 / 80.82 ± 0.75</td> <!-- SQuAD -->
   <td>10.0.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>10.0.1</td> <!-- ScaLA-en version -->
   <td>10.0.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-large-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">333</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,051 ± 981 / 1,147 ± 372</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="en ner">89.84 ± 0.48 / 89.25 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">58.19 ± 1.32 / 58.14 ± 1.69</td> <!-- SST5 -->
   <td class="en la">63.62 ± 1.90 / 80.92 ± 1.03</td> <!-- ScaLA-en -->
   <td class="en qa">55.17 ± 0.92 / 67.33 ± 0.89</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-large-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,711 ± 1,074 / 933 ± 302</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="en ner">88.80 ± 0.53 / 87.48 ± 0.71</td> <!-- CoNLL-en -->
   <td class="en sent">57.94 ± 1.17 / 58.50 ± 2.31</td> <!-- SST5 -->
   <td class="en la">59.27 ± 2.55 / 79.17 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">52.38 ± 0.93 / 63.79 ± 1.19</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/electra-large-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,700 ± 1,068 / 930 ± 301</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="en ner">67.87 ± 20.05 / 67.30 ± 19.58</td> <!-- CoNLL-en -->
   <td class="en sent">48.08 ± 14.91 / 53.81 ± 10.11</td> <!-- SST5 -->
   <td class="en la">55.46 ± 13.66 / 75.80 ± 8.43</td> <!-- ScaLA-en -->
   <td class="en qa">70.66 ± 0.80 / 81.84 ± 0.57</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en qa">75.83 ± 1.81 / 85.86 ± 1.01</td> <!-- SQuAD -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.0</td> <!-- SST5 version -->
   <td>10.0.0</td> <!-- ScaLA-en version -->
   <td>9.3.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,663 ± 1,248 / 1,619 ± 516</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="en ner">89.81 ± 0.60 / 89.25 ± 0.72</td> <!-- CoNLL-en -->
   <td class="en sent">41.97 ± 17.48 / 50.33 ± 9.16</td> <!-- SST5 -->
   <td class="en la">35.55 ± 18.61 / 63.79 ± 12.17</td> <!-- ScaLA-en -->
   <td class="en qa">68.88 ± 1.40 / 79.18 ± 1.17</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilroberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">17,448 ± 4,387 / 3,147 ± 998</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="en ner">90.04 ± 0.53 / 89.35 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">56.08 ± 1.30 / 57.56 ± 1.96</td> <!-- SST5 -->
   <td class="en la">54.90 ± 2.47 / 76.59 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en qa">49.36 ± 1.22 / 59.73 ± 1.02</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">58.79 ± 1.97 / 69.65 ± 2.00</td> <!-- SQuAD -->
   <td>9.1.2</td> <!-- CoNLL-en version -->
   <td>9.1.2</td> <!-- SST5 version -->
   <td>9.1.2</td> <!-- ScaLA-en version -->
   <td>9.1.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,296 ± 2,425 / 1,918 ± 624</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="en ner">87.62 ± 0.60 / 86.68 ± 0.57</td> <!-- CoNLL-en -->
   <td class="en sent">54.01 ± 1.49 / 54.63 ± 2.14</td> <!-- SST5 -->
   <td class="en la">56.97 ± 2.20 / 77.43 ± 1.23</td> <!-- ScaLA-en -->
   <td class="en qa">42.37 ± 2.12 / 53.78 ± 2.04</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">1.93</td> <!-- ScandEval rank -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.46 ± 1.74 / 81.96 ± 0.56</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en qa">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.35 ± 1.25</td> <!-- SQuAD -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>9.3.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.54 ± 1.41 / 80.82 ± 0.81</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.30 ± 2.09 / 77.85 ± 0.72</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="en ner">53.39 ± 2.97 / 47.76 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">65.21 ± 1.35 / 65.73 ± 1.61</td> <!-- SST5 -->
   <td class="en la">12.63 ± 2.60 / 50.10 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en qa">65.74 ± 2.31 / 77.95 ± 1.84</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="en ner">89.32 ± 0.47 / 88.95 ± 0.35</td> <!-- CoNLL-en -->
   <td class="en sent">41.89 ± 1.50 / 47.23 ± 0.75</td> <!-- SST5 -->
   <td class="en la">38.34 ± 12.84 / 67.51 ± 6.66</td> <!-- ScaLA-en -->
   <td class="en qa">55.19 ± 1.66 / 66.42 ± 1.46</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="en ner">0.54 ± 0.40 / 0.47 ± 0.35</td> <!-- CoNLL-en -->
   <td class="en sent">65.29 ± 1.43 / 69.38 ± 0.73</td> <!-- SST5 -->
   <td class="en la">25.78 ± 2.57 / 61.50 ± 2.24</td> <!-- ScaLA-en -->
   <td class="en qa">73.13 ± 4.05 / 83.85 ± 2.69</td> <!-- SQuAD -->
   <td>12.3.1</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="en ner">0.76 ± 0.29 / 0.70 ± 0.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en qa">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en qa">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="en ner">0.73 ± 0.23 / 0.65 ± 0.20</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en qa">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">65</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">19,667 ± 3,904 / 4,323 ± 1,422</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="en ner">84.75 ± 0.61 / 84.65 ± 0.45</td> <!-- CoNLL-en -->
   <td class="en sent">50.94 ± 1.56 / 53.60 ± 2.13</td> <!-- SST5 -->
   <td class="en la">53.47 ± 1.86 / 75.70 ± 1.27</td> <!-- ScaLA-en -->
   <td class="en qa">24.93 ± 1.75 / 35.60 ± 2.05</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">44.64 ± 3.00 / 53.75 ± 3.18</td> <!-- SQuAD -->
   <td>9.2.0</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.2.0</td> <!-- ScaLA-en version -->
   <td>9.2.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="en ner">0.86 ± 0.22 / 0.77 ± 0.19</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en qa">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/phi-2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,472 ± 885 / 728 ± 239</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="en ner">1.42 ± 0.66 / 1.44 ± 0.58</td> <!-- CoNLL-en -->
   <td class="en sent">62.41 ± 1.51 / 67.24 ± 1.18</td> <!-- SST5 -->
   <td class="en la">12.31 ± 2.96 / 48.73 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en qa">75.79 ± 1.88 / 86.40 ± 1.10</td> <!-- SQuAD -->
   <td>12.0.0</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.0.0</td> <!-- ScaLA-en version -->
   <td>12.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="en ner">1.44 ± 0.73 / 1.29 ± 0.64</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="en ner">1.86 ± 0.96 / 1.64 ± 0.85</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en qa">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="en ner">87.70 ± 0.68 / 87.67 ± 0.59</td> <!-- CoNLL-en -->
   <td class="en sent">36.48 ± 3.00 / 45.07 ± 1.32</td> <!-- SST5 -->
   <td class="en la">40.79 ± 2.42 / 68.71 ± 2.04</td> <!-- ScaLA-en -->
   <td class="en qa">29.00 ± 0.89 / 40.37 ± 0.77</td> <!-- SQuAD -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="en ner">1.07 ± 0.51 / 1.00 ± 0.43</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en qa">60.71 ± 1.51 / 74.26 ± 0.83</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="en ner">0.84 ± 0.34 / 0.76 ± 0.32</td> <!-- CoNLL-en -->
   <td class="en sent">66.54 ± 1.42 / 69.26 ± 0.83</td> <!-- SST5 -->
   <td class="en la">23.60 ± 3.72 / 57.65 ± 4.08</td> <!-- ScaLA-en -->
   <td class="en qa">34.46 ± 2.32 / 64.74 ± 1.66</td> <!-- SQuAD -->
   <td>12.3.1</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="en ner">0.89 ± 0.56 / 0.80 ± 0.50</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">37.83 ± 5.38 / 61.69 ± 3.35</td> <!-- SQuAD -->
   <td>12.3.1</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="en ner">3.37 ± 0.58 / 2.96 ± 0.51</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en qa">63.67 ± 1.45 / 76.52 ± 0.83</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="en ner">6.69 ± 2.64 / 6.63 ± 2.59</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en qa">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="en ner">2.16 ± 1.05 / 1.94 ± 0.90</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en qa">53.27 ± 1.28 / 63.97 ± 1.30</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="en ner">3.67 ± 0.80 / 3.27 ± 0.74</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en qa">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
   <td>12.1.0</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.70 ± 2.02 / 50.85 ± 1.85</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.60</td> <!-- ScandEval rank -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en qa">5.57 ± 3.10 / 11.14 ± 4.67</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>11.0.0</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.76</td> <!-- ScandEval rank -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en qa">0.00 ± 0.00 / 3.66 ± 0.43</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/english-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;English NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-w5LaE&quot; src=&quot;https://datawrapper.dwcdn.net/w5LaE/17/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
