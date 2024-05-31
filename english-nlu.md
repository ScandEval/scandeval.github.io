---
layout: leaderboard
title: English NLU 🇬🇧
---

<center>Last updated: 31/05/2024 13:54:07 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
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
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,521 ± 639 / 440 ± 143</td> <!-- Model inference speed -->
   <td class="rank">1.09</td> <!-- ScandEval rank -->
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
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,367 ± 1,408 / 892 ± 292</td> <!-- Model inference speed -->
   <td class="rank">1.29</td> <!-- ScandEval rank -->
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
   <td>google/electra-base-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,977 ± 2,342 / 1,855 ± 603</td> <!-- Model inference speed -->
   <td class="rank">1.39</td> <!-- ScandEval rank -->
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
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.44</td> <!-- ScandEval rank -->
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
   <td>FacebookAI/roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,542 ± 1,120 / 845 ± 267</td> <!-- Model inference speed -->
   <td class="rank">1.46</td> <!-- ScandEval rank -->
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
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.49</td> <!-- ScandEval rank -->
   <td class="en ner">91.69 ± 0.67 / 91.29 ± 0.54</td> <!-- CoNLL-en -->
   <td class="en sent">64.37 ± 1.28 / 65.16 ± 2.10</td> <!-- SST5 -->
   <td class="en la">53.58 ± 10.20 / 74.70 ± 7.53</td> <!-- ScaLA-en -->
   <td class="en qa">60.47 ± 1.61 / 73.00 ± 1.37</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
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
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.53</td> <!-- ScandEval rank -->
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
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128126</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.54</td> <!-- ScandEval rank -->
   <td class="en ner">81.79 ± 1.39 / 65.51 ± 4.16</td> <!-- CoNLL-en -->
   <td class="en sent">67.55 ± 2.34 / 74.04 ± 1.80</td> <!-- SST5 -->
   <td class="en la">51.21 ± 4.96 / 75.11 ± 2.42</td> <!-- ScaLA-en -->
   <td class="en qa">66.60 ± 1.45 / 84.48 ± 0.76</td> <!-- SQuAD -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-large-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">333</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,051 ± 981 / 1,147 ± 372</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
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
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.56</td> <!-- ScandEval rank -->
   <td class="en ner">79.06 ± 2.34 / 74.41 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">65.53 ± 2.61 / 68.71 ± 2.08</td> <!-- SST5 -->
   <td class="en la">46.28 ± 4.01 / 72.38 ± 2.33</td> <!-- ScaLA-en -->
   <td class="en qa">75.20 ± 1.68 / 86.90 ± 1.14</td> <!-- SQuAD -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-LaserChat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,387 ± 456 / 717 ± 226</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="en ner">71.91 ± 1.16 / 62.61 ± 2.72</td> <!-- CoNLL-en -->
   <td class="en sent">69.68 ± 0.91 / 69.92 ± 0.73</td> <!-- SST5 -->
   <td class="en la">46.89 ± 2.30 / 72.87 ± 1.01</td> <!-- ScaLA-en -->
   <td class="en qa">76.21 ± 1.03 / 89.02 ± 0.61</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="en ner">90.17 ± 0.50 / 89.85 ± 0.49</td> <!-- CoNLL-en -->
   <td class="en sent">51.74 ± 10.59 / 58.97 ± 6.34</td> <!-- SST5 -->
   <td class="en la">55.55 ± 1.66 / 77.55 ± 0.89</td> <!-- ScaLA-en -->
   <td class="en qa">69.02 ± 1.23 / 81.57 ± 1.05</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
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
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">1.62</td> <!-- ScandEval rank -->
   <td class="en ner">71.81 ± 1.02 / 59.93 ± 2.52</td> <!-- CoNLL-en -->
   <td class="en sent">69.98 ± 1.00 / 69.79 ± 0.76</td> <!-- SST5 -->
   <td class="en la">45.34 ± 2.51 / 72.10 ± 1.10</td> <!-- ScaLA-en -->
   <td class="en qa">72.49 ± 1.57 / 87.51 ± 0.74</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.64</td> <!-- ScandEval rank -->
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
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127999</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.64</td> <!-- ScandEval rank -->
   <td class="en ner">83.48 ± 1.52 / 75.51 ± 2.26</td> <!-- CoNLL-en -->
   <td class="en sent">62.74 ± 2.04 / 71.28 ± 1.46</td> <!-- SST5 -->
   <td class="en la">46.56 ± 3.35 / 71.13 ± 1.97</td> <!-- ScaLA-en -->
   <td class="en qa">65.41 ± 1.96 / 84.78 ± 0.68</td> <!-- SQuAD -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-large-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,711 ± 1,074 / 933 ± 302</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
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
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="en ner">69.50 ± 1.14 / 63.41 ± 0.77</td> <!-- CoNLL-en -->
   <td class="en sent">70.01 ± 0.93 / 59.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">41.35 ± 2.01 / 70.11 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en qa">76.79 ± 0.43 / 89.35 ± 0.19</td> <!-- SQuAD -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/FC-SauerkrautLM-7b-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,160 ± 514 / 668 ± 256</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="en ner">70.15 ± 0.85 / 60.29 ± 2.28</td> <!-- CoNLL-en -->
   <td class="en sent">69.36 ± 0.87 / 67.37 ± 0.89</td> <!-- SST5 -->
   <td class="en la">37.09 ± 2.04 / 68.05 ± 1.30</td> <!-- ScaLA-en -->
   <td class="en qa">77.39 ± 1.14 / 89.74 ± 0.41</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="en ner">89.65 ± 0.52 / 89.71 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">61.46 ± 0.89 / 60.48 ± 2.52</td> <!-- SST5 -->
   <td class="en la">51.32 ± 1.98 / 74.21 ± 1.18</td> <!-- ScaLA-en -->
   <td class="en qa">50.78 ± 1.14 / 63.05 ± 0.89</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="en ner">72.38 ± 1.28 / 66.44 ± 1.74</td> <!-- CoNLL-en -->
   <td class="en sent">60.98 ± 2.19 / 68.64 ± 2.17</td> <!-- SST5 -->
   <td class="en la">43.12 ± 5.21 / 70.12 ± 2.87</td> <!-- ScaLA-en -->
   <td class="en qa">74.50 ± 3.41 / 86.22 ± 1.70</td> <!-- SQuAD -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilroberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,448 ± 4,387 / 3,147 ± 998</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
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
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
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
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="en ner">90.33 ± 0.62 / 90.31 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">52.93 ± 1.41 / 58.98 ± 1.52</td> <!-- SST5 -->
   <td class="en la">50.70 ± 2.70 / 74.17 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">53.77 ± 0.57 / 65.07 ± 0.61</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,296 ± 2,425 / 1,918 ± 624</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
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
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32889</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
   <td class="en ner">71.83 ± 1.48 / 65.37 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.99 ± 3.04 / 69.81 ± 1.86</td> <!-- SST5 -->
   <td class="en la">39.97 ± 3.89 / 69.38 ± 1.87</td> <!-- ScaLA-en -->
   <td class="en qa">64.42 ± 3.17 / 80.97 ± 1.54</td> <!-- SQuAD -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
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
   <td>google/electra-large-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,700 ± 1,068 / 930 ± 301</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
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
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
   <td class="en ner">81.30 ± 1.35 / 76.64 ± 1.77</td> <!-- CoNLL-en -->
   <td class="en sent">66.18 ± 2.04 / 72.85 ± 1.27</td> <!-- SST5 -->
   <td class="en la">38.10 ± 2.32 / 68.58 ± 1.40</td> <!-- ScaLA-en -->
   <td class="en qa">53.31 ± 3.61 / 77.76 ± 1.59</td> <!-- SQuAD -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
   <td>9.1.2</td> <!-- CoNLL-en version -->
   <td>9.1.2</td> <!-- SST5 version -->
   <td>9.1.2</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">61.02 ± 2.70 / 55.57 ± 2.50</td> <!-- CoNLL-en -->
   <td class="en sent">67.10 ± 0.81 / 70.66 ± 0.76</td> <!-- SST5 -->
   <td class="en la">29.82 ± 5.18 / 62.86 ± 4.72</td> <!-- ScaLA-en -->
   <td class="en qa">73.50 ± 1.67 / 84.26 ± 1.30</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">72.80 ± 1.65 / 64.88 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.76 ± 2.53 / 71.14 ± 1.90</td> <!-- SST5 -->
   <td class="en la">28.37 ± 4.76 / 62.85 ± 3.04</td> <!-- ScaLA-en -->
   <td class="en qa">64.70 ± 2.69 / 81.80 ± 1.41</td> <!-- SQuAD -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">75.02 ± 1.31 / 69.47 ± 1.18</td> <!-- CoNLL-en -->
   <td class="en sent">67.64 ± 1.12 / 71.04 ± 1.17</td> <!-- SST5 -->
   <td class="en la">32.29 ± 3.05 / 64.85 ± 2.07</td> <!-- ScaLA-en -->
   <td class="en qa">54.84 ± 2.22 / 79.10 ± 1.10</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat-Sft-Bf16 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,413 ± 463 / 700 ± 220</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">67.52 ± 1.19 / 59.09 ± 2.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.10 ± 1.92 / 70.11 ± 0.80</td> <!-- SST5 -->
   <td class="en la">37.75 ± 2.52 / 67.53 ± 1.75</td> <!-- ScaLA-en -->
   <td class="en qa">64.88 ± 1.60 / 82.23 ± 0.72</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-HerO (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 467 / 744 ± 232</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="en ner">69.26 ± 2.17 / 57.48 ± 2.92</td> <!-- CoNLL-en -->
   <td class="en sent">68.63 ± 2.65 / 73.31 ± 1.74</td> <!-- SST5 -->
   <td class="en la">29.87 ± 3.02 / 63.64 ± 1.60</td> <!-- ScaLA-en -->
   <td class="en qa">60.92 ± 2.44 / 80.40 ± 1.26</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="en ner">66.31 ± 2.09 / 58.68 ± 1.95</td> <!-- CoNLL-en -->
   <td class="en sent">64.30 ± 0.65 / 69.26 ± 0.50</td> <!-- SST5 -->
   <td class="en la">28.18 ± 3.96 / 58.97 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en qa">70.38 ± 3.51 / 82.95 ± 2.38</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.01</td> <!-- ScandEval rank -->
   <td class="en ner">60.90 ± 3.17 / 53.69 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">66.54 ± 1.42 / 69.26 ± 0.83</td> <!-- SST5 -->
   <td class="en la">23.60 ± 3.72 / 57.65 ± 4.08</td> <!-- ScaLA-en -->
   <td class="en qa">75.14 ± 1.51 / 87.25 ± 0.61</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="en ner">59.10 ± 1.87 / 51.31 ± 1.87</td> <!-- CoNLL-en -->
   <td class="en sent">68.41 ± 1.17 / 70.85 ± 0.74</td> <!-- SST5 -->
   <td class="en la">25.43 ± 4.22 / 60.79 ± 3.45</td> <!-- ScaLA-en -->
   <td class="en qa">71.89 ± 2.20 / 82.99 ± 1.78</td> <!-- SQuAD -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en qa">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en qa">75.89 ± 1.84 / 85.86 ± 1.03</td> <!-- SQuAD -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.0</td> <!-- SST5 version -->
   <td>10.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="en ner">66.70 ± 0.99 / 61.08 ± 1.16</td> <!-- CoNLL-en -->
   <td class="en sent">55.62 ± 2.54 / 64.98 ± 2.03</td> <!-- SST5 -->
   <td class="en la">31.36 ± 2.63 / 65.21 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">72.58 ± 0.68 / 84.67 ± 0.91</td> <!-- SQuAD -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.0</td> <!-- SST5 version -->
   <td>12.10.0</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="en ner">56.07 ± 4.01 / 51.66 ± 3.99</td> <!-- CoNLL-en -->
   <td class="en sent">65.29 ± 1.43 / 69.38 ± 0.73</td> <!-- SST5 -->
   <td class="en la">25.78 ± 2.57 / 61.50 ± 2.24</td> <!-- ScaLA-en -->
   <td class="en qa">73.13 ± 4.05 / 83.85 ± 2.69</td> <!-- SQuAD -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
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
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="en ner">70.62 ± 0.90 / 58.92 ± 2.15</td> <!-- CoNLL-en -->
   <td class="en sent">67.78 ± 1.03 / 72.29 ± 0.47</td> <!-- SST5 -->
   <td class="en la">30.99 ± 2.94 / 62.20 ± 2.56</td> <!-- ScaLA-en -->
   <td class="en qa">49.56 ± 2.85 / 76.72 ± 1.15</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="en ner">47.20 ± 3.34 / 41.96 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.88 ± 2.24 / 66.49 ± 0.81</td> <!-- SST5 -->
   <td class="en la">35.75 ± 2.65 / 66.41 ± 2.26</td> <!-- ScaLA-en -->
   <td class="en qa">69.40 ± 4.29 / 82.46 ± 2.86</td> <!-- SQuAD -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.37 ± 1.27</td> <!-- SQuAD -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="en ner">56.38 ± 2.95 / 50.80 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">66.04 ± 1.68 / 65.21 ± 1.48</td> <!-- SST5 -->
   <td class="en la">22.15 ± 3.57 / 57.71 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">71.32 ± 1.41 / 83.70 ± 0.93</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.0</td> <!-- SST5 version -->
   <td>12.5.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="en ner">58.56 ± 1.99 / 54.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en qa">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="en ner">55.45 ± 1.61 / 49.72 ± 1.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en qa">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="en ner">85.88 ± 0.99 / 86.21 ± 0.87</td> <!-- CoNLL-en -->
   <td class="en sent">51.46 ± 1.15 / 51.20 ± 0.50</td> <!-- SST5 -->
   <td class="en la">35.83 ± 11.08 / 65.86 ± 4.95</td> <!-- ScaLA-en -->
   <td class="en qa">43.26 ± 1.61 / 55.52 ± 1.60</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">65</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,667 ± 3,904 / 4,323 ± 1,422</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
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
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="en ner">56.90 ± 3.08 / 51.16 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">562</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="en ner">89.50 ± 0.47 / 89.39 ± 0.41</td> <!-- CoNLL-en -->
   <td class="en sent">45.98 ± 2.97 / 49.81 ± 2.03</td> <!-- SST5 -->
   <td class="en la">30.58 ± 13.07 / 61.93 ± 7.87</td> <!-- ScaLA-en -->
   <td class="en qa">48.44 ± 1.37 / 59.47 ± 1.12</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>cstr/Spaetzle-v8-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,980 ± 1,031 / 1,714 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="en ner">69.40 ± 1.47 / 54.63 ± 3.27</td> <!-- CoNLL-en -->
   <td class="en sent">65.39 ± 2.32 / 73.11 ± 1.62</td> <!-- SST5 -->
   <td class="en la">26.69 ± 3.88 / 62.82 ± 2.19</td> <!-- ScaLA-en -->
   <td class="en qa">49.74 ± 2.61 / 75.27 ± 0.99</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="en ner">69.19 ± 2.03 / 55.64 ± 3.53</td> <!-- CoNLL-en -->
   <td class="en sent">63.77 ± 2.55 / 71.13 ± 1.83</td> <!-- SST5 -->
   <td class="en la">28.43 ± 3.97 / 62.28 ± 1.86</td> <!-- ScaLA-en -->
   <td class="en qa">44.39 ± 2.68 / 71.79 ± 1.25</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
   <td>9.2.0</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.2.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="en ner">64.09 ± 0.96 / 49.92 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">46.77 ± 4.36 / 60.99 ± 2.15</td> <!-- SST5 -->
   <td class="en la">31.62 ± 2.25 / 63.73 ± 1.79</td> <!-- ScaLA-en -->
   <td class="en qa">71.25 ± 0.83 / 85.72 ± 0.57</td> <!-- SQuAD -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="en ner">55.37 ± 2.94 / 51.08 ± 2.87</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en qa">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/phi-2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,472 ± 885 / 728 ± 239</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="en ner">49.16 ± 3.09 / 43.10 ± 2.58</td> <!-- CoNLL-en -->
   <td class="en sent">62.41 ± 1.51 / 67.24 ± 1.18</td> <!-- SST5 -->
   <td class="en la">12.31 ± 2.96 / 48.73 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en qa">75.79 ± 1.88 / 86.40 ± 1.10</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.0.0</td> <!-- ScaLA-en version -->
   <td>12.0.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="en ner">84.05 ± 0.61 / 84.48 ± 0.51</td> <!-- CoNLL-en -->
   <td class="en sent">54.92 ± 1.28 / 52.65 ± 0.58</td> <!-- SST5 -->
   <td class="en la">45.85 ± 1.41 / 71.78 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en qa">4.13 ± 0.19 / 10.53 ± 0.24</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="en ner">82.39 ± 0.62 / 83.07 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">57.35 ± 1.00 / 54.82 ± 0.65</td> <!-- SST5 -->
   <td class="en la">47.29 ± 2.10 / 71.85 ± 1.30</td> <!-- ScaLA-en -->
   <td class="en qa">4.29 ± 0.33 / 10.53 ± 0.29</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
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
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="en ner">87.77 ± 0.51 / 87.83 ± 0.47</td> <!-- CoNLL-en -->
   <td class="en sent">41.09 ± 4.38 / 48.17 ± 3.16</td> <!-- SST5 -->
   <td class="en la">32.26 ± 10.79 / 61.20 ± 5.53</td> <!-- ScaLA-en -->
   <td class="en qa">35.15 ± 1.89 / 44.98 ± 1.93</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="en ner">87.09 ± 0.61 / 87.25 ± 0.49</td> <!-- CoNLL-en -->
   <td class="en sent">55.40 ± 0.56 / 52.86 ± 0.29</td> <!-- SST5 -->
   <td class="en la">39.78 ± 3.59 / 67.21 ± 2.02</td> <!-- ScaLA-en -->
   <td class="en qa">6.20 ± 4.26 / 13.47 ± 5.29</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
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
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="en ner">39.21 ± 1.52 / 34.08 ± 1.88</td> <!-- CoNLL-en -->
   <td class="en sent">65.58 ± 1.59 / 57.86 ± 1.13</td> <!-- SST5 -->
   <td class="en la">7.82 ± 1.43 / 51.19 ± 1.75</td> <!-- ScaLA-en -->
   <td class="en qa">72.25 ± 2.19 / 83.08 ± 1.30</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="en ner">87.08 ± 0.62 / 87.08 ± 0.57</td> <!-- CoNLL-en -->
   <td class="en sent">36.77 ± 1.52 / 45.15 ± 0.60</td> <!-- SST5 -->
   <td class="en la">37.10 ± 1.79 / 67.20 ± 1.15</td> <!-- ScaLA-en -->
   <td class="en qa">26.99 ± 0.77 / 37.98 ± 0.63</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
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
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="en ner">40.89 ± 2.63 / 37.44 ± 2.39</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en qa">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="en ner">38.23 ± 3.10 / 36.38 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">60.70 ± 1.80 / 66.82 ± 1.12</td> <!-- SST5 -->
   <td class="en la">-0.19 ± 2.28 / 38.77 ± 3.32</td> <!-- ScaLA-en -->
   <td class="en qa">61.93 ± 1.98 / 73.71 ± 1.57</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="en ner">19.65 ± 5.96 / 18.64 ± 5.49</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en qa">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,607 ± 565 / 1,212 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="en ner">23.28 ± 6.45 / 21.81 ± 5.61</td> <!-- CoNLL-en -->
   <td class="en sent">61.91 ± 2.08 / 67.80 ± 1.12</td> <!-- SST5 -->
   <td class="en la">6.92 ± 2.36 / 44.29 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en qa">64.68 ± 1.06 / 76.60 ± 0.51</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="en ner">25.36 ± 8.05 / 24.05 ± 7.34</td> <!-- CoNLL-en -->
   <td class="en sent">56.91 ± 2.41 / 66.15 ± 1.54</td> <!-- SST5 -->
   <td class="en la">7.10 ± 2.89 / 49.36 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.60 ± 5.37 / 70.37 ± 4.71</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en qa">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="en ner">88.62 ± 0.53 / 88.44 ± 0.46</td> <!-- CoNLL-en -->
   <td class="en sent">11.09 ± 10.39 / 33.19 ± 4.75</td> <!-- SST5 -->
   <td class="en la">8.46 ± 2.34 / 51.98 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en qa">49.64 ± 1.94 / 62.02 ± 1.77</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,530 ± 748 / 829 ± 277</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="en ner">47.70 ± 2.71 / 44.98 ± 2.69</td> <!-- CoNLL-en -->
   <td class="en sent">51.87 ± 6.35 / 49.40 ± 3.66</td> <!-- SST5 -->
   <td class="en la">0.14 ± 1.67 / 46.80 ± 2.63</td> <!-- ScaLA-en -->
   <td class="en qa">50.83 ± 1.05 / 61.39 ± 1.03</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en qa">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="en ner">81.71 ± 0.66 / 82.33 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">50.69 ± 1.19 / 50.90 ± 0.50</td> <!-- SST5 -->
   <td class="en la">2.16 ± 1.58 / 49.99 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en qa">4.16 ± 0.71 / 11.93 ± 0.61</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="en ner">81.71 ± 0.66 / 82.33 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">50.69 ± 1.19 / 50.90 ± 0.50</td> <!-- SST5 -->
   <td class="en la">2.16 ± 1.58 / 49.99 ± 1.47</td> <!-- ScaLA-en -->
   <td class="en qa">4.19 ± 0.69 / 11.99 ± 0.62</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en qa">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="en ner">77.50 ± 0.54 / 78.82 ± 0.48</td> <!-- CoNLL-en -->
   <td class="en sent">53.10 ± 1.18 / 51.88 ± 0.50</td> <!-- SST5 -->
   <td class="en la">-0.35 ± 1.84 / 48.74 ± 1.43</td> <!-- ScaLA-en -->
   <td class="en qa">3.13 ± 0.27 / 9.98 ± 0.25</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="en ner">71.43 ± 0.88 / 71.51 ± 0.79</td> <!-- CoNLL-en -->
   <td class="en sent">17.53 ± 2.21 / 38.67 ± 1.90</td> <!-- SST5 -->
   <td class="en la">23.93 ± 5.87 / 59.48 ± 3.40</td> <!-- ScaLA-en -->
   <td class="en qa">31.01 ± 0.89 / 42.98 ± 0.49</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="en ner">26.47 ± 6.25 / 28.27 ± 5.35</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en qa">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="en ner">77.64 ± 0.74 / 79.56 ± 0.53</td> <!-- CoNLL-en -->
   <td class="en sent">12.42 ± 9.17 / 33.80 ± 4.31</td> <!-- SST5 -->
   <td class="en la">13.65 ± 6.22 / 53.84 ± 2.20</td> <!-- ScaLA-en -->
   <td class="en qa">33.29 ± 0.96 / 45.71 ± 0.70</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="en ner">71.90 ± 1.49 / 74.21 ± 1.10</td> <!-- CoNLL-en -->
   <td class="en sent">36.22 ± 1.39 / 45.80 ± 1.20</td> <!-- SST5 -->
   <td class="en la">0.47 ± 1.65 / 48.67 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en qa">2.40 ± 0.23 / 8.51 ± 0.21</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="en ner">71.90 ± 1.49 / 74.21 ± 1.10</td> <!-- CoNLL-en -->
   <td class="en sent">36.22 ± 1.39 / 45.80 ± 1.20</td> <!-- SST5 -->
   <td class="en la">0.47 ± 1.65 / 48.67 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en qa">2.44 ± 0.17 / 8.50 ± 0.20</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="en ner">71.33 ± 0.75 / 73.43 ± 0.61</td> <!-- CoNLL-en -->
   <td class="en sent">36.75 ± 1.28 / 47.80 ± 1.46</td> <!-- SST5 -->
   <td class="en la">0.24 ± 1.44 / 47.55 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en qa">1.30 ± 0.31 / 9.37 ± 0.28</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="en ner">65.85 ± 0.80 / 68.72 ± 0.81</td> <!-- CoNLL-en -->
   <td class="en sent">25.85 ± 2.01 / 40.72 ± 0.85</td> <!-- SST5 -->
   <td class="en la">1.21 ± 1.72 / 50.03 ± 0.84</td> <!-- ScaLA-en -->
   <td class="en qa">4.00 ± 0.55 / 11.02 ± 0.40</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.51 ± 2.07 / 50.66 ± 1.90</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="en ner">68.25 ± 2.50 / 70.44 ± 2.50</td> <!-- CoNLL-en -->
   <td class="en sent">1.92 ± 1.68 / 28.84 ± 2.38</td> <!-- SST5 -->
   <td class="en la">1.08 ± 1.34 / 47.42 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en qa">2.79 ± 0.93 / 10.00 ± 0.84</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.34</td> <!-- ScandEval rank -->
   <td class="en ner">34.64 ± 1.25 / 34.41 ± 1.49</td> <!-- CoNLL-en -->
   <td class="en sent">4.00 ± 3.78 / 24.24 ± 3.94</td> <!-- SST5 -->
   <td class="en la">1.33 ± 1.00 / 42.07 ± 4.82</td> <!-- ScaLA-en -->
   <td class="en qa">0.43 ± 0.11 / 6.18 ± 1.24</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">4.41</td> <!-- ScandEval rank -->
   <td class="en ner">30.77 ± 0.92 / 30.14 ± 1.03</td> <!-- CoNLL-en -->
   <td class="en sent">0.58 ± 1.45 / 20.82 ± 1.74</td> <!-- SST5 -->
   <td class="en la">-0.17 ± 0.47 / 37.18 ± 3.93</td> <!-- ScaLA-en -->
   <td class="en qa">0.46 ± 0.14 / 6.16 ± 0.24</td> <!-- SQuAD -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en qa">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>11.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en qa">0.00 ± 0.00 / 3.68 ± 0.43</td> <!-- SQuAD -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/english-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;English NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-kSeuq&quot; src=&quot;https://datawrapper.dwcdn.net/kSeuq/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
