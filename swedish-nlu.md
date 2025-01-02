---
layout: leaderboard
title: Swedish NLU 🇸🇪
---

<center>Last updated: 02/01/2025 10:48:43 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="swedish-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SweReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish reading comprehension - Exact Match / F1-score">ScandiQA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SUC3">SUC3 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweReC">SweReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-sv">ScaLA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-sv">ScandiQA-sv version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,314 ± 1,202 / 776 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.07</td> <!-- ScandEval rank -->
   <td class="sv ner">88.78 ± 1.05 / 85.30 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">81.73 ± 0.71 / 80.87 ± 0.96</td> <!-- SweReC -->
   <td class="sv la">75.83 ± 0.49 / 87.67 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.35 ± 0.70 / 65.90 ± 0.55</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.28</td> <!-- ScandEval rank -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/lynx-micro (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,162 ± 2,661 / 1,878 ± 623</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="sv ner">83.64 ± 1.90 / 81.69 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">78.57 ± 0.78 / 78.35 ± 0.90</td> <!-- SweReC -->
   <td class="sv la">66.83 ± 0.98 / 83.20 ± 0.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.84 ± 0.54 / 62.97 ± 0.52</td> <!-- ScandiQA-sv -->
   <td>12.10.2</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">1.33</td> <!-- ScandEval rank -->
   <td class="sv ner">82.65 ± 1.04 / 80.43 ± 0.93</td> <!-- SUC3 -->
   <td class="sv sent">77.25 ± 1.20 / 73.96 ± 2.59</td> <!-- SweReC -->
   <td class="sv la">77.90 ± 1.45 / 88.63 ± 0.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.64 ± 1.11 / 55.64 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.35</td> <!-- ScandEval rank -->
   <td class="sv ner">82.97 ± 0.98 / 81.14 ± 1.14</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 1.25 / 73.57 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">73.81 ± 4.60 / 86.33 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.50 ± 1.32 / 55.34 ± 1.33</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="sv ner">81.05 ± 1.34 / 76.08 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">78.00 ± 0.89 / 75.01 ± 2.18</td> <!-- SweReC -->
   <td class="sv la">76.79 ± 1.70 / 87.59 ± 1.06</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.71 ± 1.09 / 51.70 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">370</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">1.44</td> <!-- ScandEval rank -->
   <td class="sv ner">80.39 ± 1.34 / 74.83 ± 1.44</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 0.79 / 77.12 ± 0.86</td> <!-- SweReC -->
   <td class="sv la">76.28 ± 1.86 / 87.37 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.56 ± 0.52 / 50.85 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">1.49</td> <!-- ScandEval rank -->
   <td class="sv ner">81.95 ± 1.55 / 76.66 ± 1.60</td> <!-- SUC3 -->
   <td class="sv sent">75.58 ± 1.17 / 73.35 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">78.86 ± 0.83 / 89.07 ± 0.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/bert-large-nordic-pile-1M-steps</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,571 ± 1,331 / 1,493 ± 479</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="sv ner">80.65 ± 2.12 / 78.69 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">77.43 ± 1.07 / 75.95 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">76.56 ± 1.06 / 87.86 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv rc">41.54 ± 1.50 / 46.79 ± 1.60</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-large</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,048 ± 824 / 1,354 ± 429</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="sv ner">79.01 ± 1.13 / 73.76 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">75.32 ± 1.55 / 69.39 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">69.11 ± 1.50 / 84.32 ± 0.70</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.88 ± 0.87 / 54.15 ± 0.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">576</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
   <td class="sv ner">78.23 ± 1.53 / 72.58 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">75.99 ± 1.15 / 71.01 ± 4.17</td> <!-- SweReC -->
   <td class="sv la">72.17 ± 0.94 / 85.94 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.00 ± 2.13 / 51.05 ± 2.40</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
   <td class="sv ner">80.36 ± 1.12 / 78.57 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">79.65 ± 1.05 / 78.90 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">63.15 ± 1.65 / 81.06 ± 0.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.99 ± 1.18 / 53.49 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="sv ner">78.61 ± 1.45 / 72.84 ± 1.51</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 0.80 / 75.77 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">72.87 ± 2.36 / 85.57 ± 1.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.11 ± 0.99 / 49.29 ± 1.05</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="sv ner">81.23 ± 1.58 / 75.95 ± 1.72</td> <!-- SUC3 -->
   <td class="sv sent">75.73 ± 0.72 / 73.61 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">78.60 ± 0.98 / 88.95 ± 0.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.56 ± 1.53 / 43.79 ± 1.43</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="sv ner">78.84 ± 2.19 / 72.86 ± 2.04</td> <!-- SUC3 -->
   <td class="sv sent">75.24 ± 0.99 / 72.06 ± 2.67</td> <!-- SweReC -->
   <td class="sv la">72.30 ± 1.04 / 85.77 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.74 ± 1.04 / 50.62 ± 0.85</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="sv ner">62.59 ± 2.04 / 45.11 ± 4.50</td> <!-- SUC3 -->
   <td class="sv sent">80.73 ± 0.52 / 81.25 ± 0.57</td> <!-- SweReC -->
   <td class="sv la">61.37 ± 2.06 / 79.34 ± 1.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.76 ± 1.03 / 66.73 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="sv ner">78.91 ± 1.24 / 72.93 ± 1.08</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 0.81 / 72.74 ± 2.11</td> <!-- SweReC -->
   <td class="sv la">70.08 ± 2.11 / 83.40 ± 1.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">41.14 ± 1.18 / 47.18 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">837 ± 294 / 126 ± 43</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="sv ner">71.43 ± 1.58 / 58.93 ± 3.29</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 1.54 / 76.51 ± 1.63</td> <!-- SweReC -->
   <td class="sv la">55.99 ± 2.64 / 75.08 ± 2.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.46 ± 0.90 / 64.95 ± 0.64</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,231 ± 8,171 / 4,863 ± 1,598</td> <!-- Model inference speed -->
   <td class="rank">1.62</td> <!-- ScandEval rank -->
   <td class="sv ner">80.05 ± 1.13 / 74.21 ± 1.26</td> <!-- SUC3 -->
   <td class="sv sent">75.09 ± 1.30 / 72.93 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">61.83 ± 1.28 / 79.96 ± 0.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.69 ± 1.11 / 51.07 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="sv ner">62.91 ± 1.46 / 47.13 ± 3.48</td> <!-- SUC3 -->
   <td class="sv sent">79.51 ± 0.63 / 79.57 ± 0.65</td> <!-- SweReC -->
   <td class="sv la">60.28 ± 1.19 / 79.99 ± 0.66</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.44 ± 0.92 / 64.81 ± 0.62</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-large-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,671 ± 1,380 / 1,497 ± 482</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="sv ner">74.18 ± 2.01 / 68.89 ± 2.46</td> <!-- SUC3 -->
   <td class="sv sent">75.11 ± 1.19 / 74.74 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">64.11 ± 3.27 / 81.63 ± 1.66</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.79 ± 1.61 / 52.40 ± 1.77</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="sv ner">79.50 ± 0.96 / 77.37 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">79.48 ± 0.87 / 77.47 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">53.01 ± 15.20 / 75.97 ± 7.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.68 ± 1.62 / 53.19 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="sv ner">79.29 ± 0.94 / 73.18 ± 0.95</td> <!-- SUC3 -->
   <td class="sv sent">75.85 ± 0.54 / 70.58 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">70.43 ± 1.03 / 83.85 ± 0.65</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.56 ± 0.64 / 44.01 ± 0.43</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,079 ± 2,948 / 3,359 ± 1,091</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="sv ner">80.02 ± 1.62 / 74.04 ± 1.75</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 1.60 / 73.41 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">71.92 ± 1.07 / 85.01 ± 0.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.80 ± 0.78 / 38.58 ± 0.70</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="sv ner">79.08 ± 2.32 / 73.06 ± 2.01</td> <!-- SUC3 -->
   <td class="sv sent">72.53 ± 0.98 / 67.74 ± 3.02</td> <!-- SweReC -->
   <td class="sv la">73.01 ± 1.43 / 85.98 ± 0.81</td> <!-- ScaLA-sv -->
   <td class="sv rc">36.92 ± 2.25 / 41.99 ± 2.38</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="sv ner">80.33 ± 2.50 / 75.03 ± 3.79</td> <!-- SUC3 -->
   <td class="sv sent">76.63 ± 0.98 / 74.25 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">49.72 ± 19.88 / 69.94 ± 13.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.64 ± 1.42 / 52.21 ± 1.45</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv rc">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="sv ner">79.99 ± 1.32 / 74.07 ± 1.54</td> <!-- SUC3 -->
   <td class="sv sent">76.04 ± 0.97 / 72.61 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">73.52 ± 2.31 / 85.57 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.60 ± 1.30 / 35.83 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="sv ner">79.90 ± 1.41 / 73.80 ± 1.53</td> <!-- SUC3 -->
   <td class="sv sent">76.20 ± 1.16 / 74.01 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">73.62 ± 1.17 / 86.19 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.38 ± 1.23 / 37.12 ± 1.20</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-1</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,245 ± 1,260 / 1,416 ± 453</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="sv ner">71.65 ± 1.55 / 69.08 ± 1.45</td> <!-- SUC3 -->
   <td class="sv sent">74.92 ± 0.98 / 72.01 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">63.43 ± 2.30 / 81.00 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.20 ± 1.03 / 51.94 ± 0.92</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-large-2</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,569 ± 1,320 / 1,492 ± 476</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="sv ner">71.86 ± 1.73 / 69.05 ± 1.65</td> <!-- SUC3 -->
   <td class="sv sent">74.67 ± 1.43 / 71.15 ± 3.57</td> <!-- SweReC -->
   <td class="sv la">62.77 ± 3.14 / 80.75 ± 1.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.77 ± 3.06 / 50.58 ± 2.94</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">1.74</td> <!-- ScandEval rank -->
   <td class="sv ner">77.78 ± 1.69 / 72.08 ± 1.81</td> <!-- SUC3 -->
   <td class="sv sent">73.58 ± 1.37 / 70.43 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">60.36 ± 2.98 / 79.72 ± 1.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">41.71 ± 1.08 / 47.07 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="sv ner">52.50 ± 1.02 / 37.38 ± 2.57</td> <!-- SUC3 -->
   <td class="sv sent">78.51 ± 0.93 / 76.24 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">61.28 ± 1.63 / 80.07 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.22 ± 1.03 / 64.60 ± 0.52</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="sv ner">78.58 ± 1.52 / 72.45 ± 1.57</td> <!-- SUC3 -->
   <td class="sv sent">73.41 ± 0.98 / 68.72 ± 3.80</td> <!-- SweReC -->
   <td class="sv la">71.14 ± 1.62 / 84.55 ± 0.97</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.62 ± 1.35 / 36.20 ± 1.16</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium-3</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,278 / 2,749 ± 894</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="sv ner">81.35 ± 1.26 / 79.18 ± 1.23</td> <!-- SUC3 -->
   <td class="sv sent">71.16 ± 1.21 / 69.78 ± 3.24</td> <!-- SweReC -->
   <td class="sv la">63.89 ± 1.18 / 81.45 ± 0.75</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.18 ± 2.04 / 42.09 ± 2.23</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="sv ner">50.43 ± 3.97 / 27.20 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">80.55 ± 1.46 / 77.22 ± 3.78</td> <!-- SweReC -->
   <td class="sv la">50.86 ± 3.91 / 72.14 ± 3.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.35 ± 1.16 / 65.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,050 ± 3,222 / 2,727 ± 886</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="sv ner">80.38 ± 0.99 / 75.35 ± 0.88</td> <!-- SUC3 -->
   <td class="sv sent">71.21 ± 1.11 / 67.49 ± 2.90</td> <!-- SweReC -->
   <td class="sv la">64.03 ± 1.94 / 81.39 ± 1.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.33 ± 2.25 / 39.61 ± 2.31</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-sbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,757 ± 3,883 / 3,864 ± 1,237</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="sv ner">80.26 ± 1.10 / 77.87 ± 1.03</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 0.75 / 69.24 ± 2.39</td> <!-- SweReC -->
   <td class="sv la">62.49 ± 2.06 / 80.42 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.80 ± 1.33 / 38.28 ± 1.45</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="sv ner">79.02 ± 0.74 / 77.59 ± 0.76</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.89 / 69.85 ± 3.16</td> <!-- SweReC -->
   <td class="sv la">50.19 ± 1.23 / 74.23 ± 0.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.65 ± 1.29 / 46.62 ± 1.30</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="sv ner">78.21 ± 0.92 / 72.63 ± 0.98</td> <!-- SUC3 -->
   <td class="sv sent">71.05 ± 1.70 / 70.72 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">56.02 ± 2.92 / 77.31 ± 1.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.52 ± 1.02 / 47.31 ± 0.99</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,954 / 3,356 ± 1,090</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="sv ner">74.48 ± 2.35 / 67.89 ± 2.16</td> <!-- SUC3 -->
   <td class="sv sent">74.58 ± 1.29 / 70.97 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">69.07 ± 2.22 / 83.17 ± 1.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.66 ± 1.18 / 37.05 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="sv ner">75.40 ± 1.45 / 70.45 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">76.22 ± 0.78 / 75.25 ± 1.16</td> <!-- SweReC -->
   <td class="sv la">65.73 ± 1.73 / 81.50 ± 1.14</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.34 ± 1.44 / 34.01 ± 1.50</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-debug-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,958 ± 2,903 / 3,331 ± 1,077</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="sv ner">72.25 ± 2.16 / 65.94 ± 2.04</td> <!-- SUC3 -->
   <td class="sv sent">75.04 ± 1.08 / 72.35 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">70.16 ± 1.47 / 84.29 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.89 ± 0.99 / 36.93 ± 0.90</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,610 ± 751 / 176 ± 66</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.49 / 44.62 ± 4.10</td> <!-- SUC3 -->
   <td class="sv sent">79.96 ± 0.93 / 75.75 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">31.70 ± 4.07 / 59.28 ± 5.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.33 ± 0.88 / 65.24 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Llama-3-8B-flashback-v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,807 ± 1,152 / 979 ± 319</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="sv ner">59.03 ± 2.04 / 41.99 ± 4.35</td> <!-- SUC3 -->
   <td class="sv sent">81.13 ± 0.94 / 80.80 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">33.06 ± 3.65 / 61.21 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.21 ± 0.67 / 64.01 ± 0.68</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">1.89</td> <!-- ScandEval rank -->
   <td class="sv ner">62.86 ± 1.95 / 36.42 ± 3.49</td> <!-- SUC3 -->
   <td class="sv sent">70.54 ± 6.38 / 73.39 ± 6.37</td> <!-- SweReC -->
   <td class="sv la">37.50 ± 2.48 / 66.32 ± 1.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.00 ± 0.85 / 65.98 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">1.89</td> <!-- ScandEval rank -->
   <td class="sv ner">79.75 ± 0.94 / 73.45 ± 0.86</td> <!-- SUC3 -->
   <td class="sv sent">74.73 ± 1.15 / 70.83 ± 3.72</td> <!-- SweReC -->
   <td class="sv la">53.55 ± 16.68 / 75.79 ± 8.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.20 ± 0.86 / 36.88 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/orpo-llama-3-swe (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,974 ± 1,208 / 1,032 ± 342</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="sv ner">60.93 ± 2.85 / 38.87 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.68 / 75.13 ± 1.85</td> <!-- SweReC -->
   <td class="sv la">26.02 ± 4.38 / 52.19 ± 5.44</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.84 ± 0.92 / 65.92 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-8</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,112 ± 2,969 / 3,347 ± 1,093</td> <!-- Model inference speed -->
   <td class="rank">1.93</td> <!-- ScandEval rank -->
   <td class="sv ner">73.44 ± 2.81 / 67.31 ± 3.11</td> <!-- SUC3 -->
   <td class="sv sent">73.63 ± 1.53 / 68.42 ± 4.24</td> <!-- SweReC -->
   <td class="sv la">58.91 ± 17.49 / 77.13 ± 10.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.39 ± 1.02 / 37.33 ± 0.86</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/dolphin-2.9-llama3-8b-flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,018 ± 1,216 / 996 ± 324</td> <!-- Model inference speed -->
   <td class="rank">1.93</td> <!-- ScandEval rank -->
   <td class="sv ner">65.33 ± 2.38 / 46.88 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">74.99 ± 3.45 / 76.76 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">32.65 ± 5.08 / 61.25 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.71 ± 1.34 / 64.54 ± 1.00</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">912 ± 238 / 179 ± 70</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="sv ner">67.49 ± 2.20 / 51.10 ± 4.76</td> <!-- SUC3 -->
   <td class="sv sent">76.74 ± 1.27 / 75.66 ± 1.17</td> <!-- SweReC -->
   <td class="sv la">22.37 ± 3.11 / 54.47 ± 4.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.15 ± 0.72 / 64.47 ± 0.58</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt-mixtral (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="sv ner">54.14 ± 2.49 / 37.43 ± 3.05</td> <!-- SUC3 -->
   <td class="sv sent">78.27 ± 1.32 / 77.65 ± 1.28</td> <!-- SweReC -->
   <td class="sv la">32.49 ± 1.94 / 64.28 ± 2.18</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.95 ± 0.96 / 66.56 ± 0.62</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,629 ± 573 / 262 ± 149</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/sol (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,701 ± 876 / 771 ± 247</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="sv ner">57.51 ± 2.30 / 37.74 ± 3.15</td> <!-- SUC3 -->
   <td class="sv sent">77.31 ± 1.01 / 70.55 ± 2.26</td> <!-- SweReC -->
   <td class="sv la">25.06 ± 5.02 / 49.04 ± 4.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.77 / 67.43 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="sv ner">72.49 ± 1.68 / 67.03 ± 1.55</td> <!-- SUC3 -->
   <td class="sv sent">70.69 ± 1.08 / 67.03 ± 3.40</td> <!-- SweReC -->
   <td class="sv la">56.60 ± 3.25 / 76.70 ± 2.48</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.89 ± 1.88 / 37.63 ± 1.86</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="sv ner">46.57 ± 3.34 / 33.94 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.53 ± 2.55 / 77.96 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">33.43 ± 3.89 / 61.87 ± 4.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.87 ± 1.52 / 64.53 ± 1.41</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="sv ner">47.28 ± 3.05 / 34.01 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.62 ± 2.52 / 78.04 ± 2.98</td> <!-- SweReC -->
   <td class="sv la">33.23 ± 4.72 / 61.29 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.00 ± 1.69 / 64.62 ± 1.44</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/kbbert-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">82</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,698 ± 4,287 / 8,677 ± 2,776</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">80.12 ± 1.41 / 73.78 ± 1.37</td> <!-- SUC3 -->
   <td class="sv sent">71.28 ± 1.09 / 69.73 ± 2.94</td> <!-- SweReC -->
   <td class="sv la">51.58 ± 2.89 / 73.82 ± 2.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.16 ± 0.76 / 33.47 ± 0.62</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,396 ± 6,394 / 4,534 ± 1,421</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">68.39 ± 7.26 / 63.66 ± 6.41</td> <!-- SUC3 -->
   <td class="sv sent">73.43 ± 0.91 / 61.29 ± 1.81</td> <!-- SweReC -->
   <td class="sv la">45.09 ± 15.90 / 68.48 ± 11.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.04 ± 2.09 / 43.73 ± 1.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">178</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">76.29 ± 1.28 / 70.33 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">61.78 ± 1.21 / 60.94 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">47.74 ± 7.69 / 72.98 ± 4.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">41.17 ± 1.01 / 46.07 ± 1.12</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32B</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,103 ± 2,982 / 3,357 ± 1,081</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">77.97 ± 0.82 / 72.10 ± 0.94</td> <!-- SUC3 -->
   <td class="sv sent">73.27 ± 0.75 / 71.87 ± 1.30</td> <!-- SweReC -->
   <td class="sv la">47.19 ± 16.37 / 72.10 ± 8.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.07 ± 0.93 / 36.17 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.98 ± 1.65 / 65.44 ± 1.38</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="sv ner">46.61 ± 3.11 / 34.10 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 2.01 / 78.30 ± 2.42</td> <!-- SweReC -->
   <td class="sv la">34.16 ± 4.39 / 60.06 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.77 ± 1.76 / 63.50 ± 1.47</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,005 ± 330 / 196 ± 74</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="sv ner">71.52 ± 1.43 / 59.28 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">80.46 ± 0.83 / 78.67 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">12.29 ± 3.59 / 40.53 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.54 ± 1.52 / 62.08 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,696 ± 1,260 / 1,630 ± 515</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="sv ner">79.53 ± 2.77 / 74.53 ± 2.70</td> <!-- SUC3 -->
   <td class="sv sent">75.42 ± 1.08 / 72.68 ± 3.19</td> <!-- SweReC -->
   <td class="sv la">18.44 ± 10.88 / 53.57 ± 7.20</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.19 ± 1.10 / 53.67 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.43 ± 1.59 / 65.06 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,431 ± 1,267 / 1,139 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="sv ner">48.19 ± 2.55 / 37.50 ± 3.62</td> <!-- SUC3 -->
   <td class="sv sent">79.95 ± 0.87 / 81.24 ± 0.64</td> <!-- SweReC -->
   <td class="sv la">32.85 ± 2.28 / 61.74 ± 3.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.52 / 63.58 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 2.00 / 64.06 ± 1.76</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8067</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="sv ner">67.38 ± 1.52 / 52.86 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 4.81 / 67.01 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">29.41 ± 10.34 / 52.38 ± 8.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.67 ± 0.89 / 66.26 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="sv ner">56.21 ± 2.49 / 44.78 ± 4.19</td> <!-- SUC3 -->
   <td class="sv sent">78.30 ± 1.71 / 79.80 ± 2.03</td> <!-- SweReC -->
   <td class="sv la">14.35 ± 5.65 / 48.69 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.08 ± 1.47 / 65.72 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="sv ner">75.49 ± 1.09 / 74.57 ± 0.60</td> <!-- SUC3 -->
   <td class="sv sent">71.12 ± 0.90 / 60.88 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">36.69 ± 15.58 / 65.77 ± 8.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.55 ± 2.07 / 38.90 ± 2.21</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.42 ± 1.64 / 63.83 ± 1.18</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="sv ner">70.85 ± 1.56 / 65.50 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">63.30 ± 0.93 / 59.96 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">48.97 ± 1.14 / 73.78 ± 0.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.00 ± 1.52 / 42.69 ± 1.62</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="sv ner">75.62 ± 1.56 / 70.17 ± 1.46</td> <!-- SUC3 -->
   <td class="sv sent">62.50 ± 1.10 / 60.57 ± 2.75</td> <!-- SweReC -->
   <td class="sv la">38.18 ± 7.03 / 66.99 ± 4.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.96 ± 1.11 / 45.91 ± 1.20</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.75 ± 1.13 / 64.72 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,385 ± 2,815 / 3,578 ± 1,177</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="sv ner">68.55 ± 3.16 / 62.00 ± 2.58</td> <!-- SUC3 -->
   <td class="sv sent">69.96 ± 1.75 / 68.67 ± 3.21</td> <!-- SweReC -->
   <td class="sv la">52.88 ± 14.23 / 75.25 ± 7.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">27.99 ± 1.23 / 32.49 ± 1.27</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.67 ± 0.96 / 64.58 ± 0.78</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.92 ± 1.64 / 64.87 ± 1.47</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="sv ner">47.10 ± 2.60 / 35.06 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">73.05 ± 5.27 / 74.56 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">30.29 ± 2.63 / 61.40 ± 3.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.38 / 63.51 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="sv ner">45.12 ± 2.72 / 30.73 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">78.74 ± 2.13 / 80.11 ± 2.64</td> <!-- SweReC -->
   <td class="sv la">19.74 ± 6.09 / 46.97 ± 5.83</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.15 ± 1.71 / 65.22 ± 1.28</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="sv ner">48.36 ± 3.07 / 34.48 ± 5.22</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 2.19 / 78.11 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">20.94 ± 5.55 / 44.72 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.07 ± 1.90 / 63.87 ± 1.46</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="sv ner">40.59 ± 1.98 / 28.19 ± 1.47</td> <!-- SUC3 -->
   <td class="sv sent">76.02 ± 2.40 / 77.86 ± 1.70</td> <!-- SweReC -->
   <td class="sv la">33.98 ± 5.90 / 57.44 ± 6.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.98 ± 0.58 / 63.97 ± 0.66</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,062 ± 3,216 / 2,733 ± 885</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="sv ner">74.88 ± 1.45 / 69.57 ± 1.83</td> <!-- SUC3 -->
   <td class="sv sent">61.89 ± 0.90 / 60.17 ± 3.06</td> <!-- SweReC -->
   <td class="sv la">40.22 ± 2.03 / 68.89 ± 2.06</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.95 ± 0.82 / 44.78 ± 0.99</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,973 ± 3,205 / 2,725 ± 884</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="sv ner">76.55 ± 1.28 / 70.38 ± 1.01</td> <!-- SUC3 -->
   <td class="sv sent">61.60 ± 1.38 / 62.28 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">37.44 ± 6.65 / 66.67 ± 4.88</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.32 ± 1.25 / 43.87 ± 1.29</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,081 ± 3,231 / 2,748 ± 891</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="sv ner">75.33 ± 0.99 / 69.89 ± 0.52</td> <!-- SUC3 -->
   <td class="sv sent">61.80 ± 1.76 / 58.93 ± 3.28</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 5.98 / 66.91 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.95 ± 1.95 / 44.71 ± 1.99</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.75 ± 1.46 / 65.08 ± 1.15</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="sv ner">48.43 ± 2.75 / 35.31 ± 2.80</td> <!-- SUC3 -->
   <td class="sv sent">79.43 ± 0.85 / 78.21 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">17.37 ± 2.57 / 52.91 ± 4.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.05 ± 1.22 / 62.72 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="sv ner">70.17 ± 0.99 / 64.19 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">66.62 ± 1.71 / 61.90 ± 2.61</td> <!-- SweReC -->
   <td class="sv la">46.72 ± 3.65 / 72.15 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.38 ± 1.36 / 35.79 ± 1.33</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="sv ner">72.90 ± 1.37 / 66.93 ± 1.30</td> <!-- SUC3 -->
   <td class="sv sent">61.11 ± 1.28 / 58.97 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">55.05 ± 1.64 / 76.76 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.04 ± 1.16 / 33.60 ± 1.06</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,141 ± 994 / 905 ± 299</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="sv ner">36.45 ± 2.44 / 27.24 ± 2.29</td> <!-- SUC3 -->
   <td class="sv sent">81.12 ± 1.02 / 77.04 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">26.80 ± 2.07 / 59.15 ± 2.72</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.16 ± 0.82 / 64.72 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,121 ± 288 / 205 ± 68</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="sv ner">60.04 ± 1.22 / 43.93 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 0.85 / 67.87 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">7.54 ± 2.52 / 35.42 ± 1.33</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.60 ± 0.59 / 63.65 ± 0.30</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,018 ± 326 / 189 ± 73</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="sv ner">57.38 ± 1.93 / 29.69 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">78.43 ± 0.93 / 74.54 ± 2.40</td> <!-- SweReC -->
   <td class="sv la">14.52 ± 2.43 / 45.18 ± 4.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.14 ± 1.81 / 63.00 ± 0.50</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="sv ner">54.37 ± 3.04 / 42.16 ± 4.00</td> <!-- SUC3 -->
   <td class="sv sent">75.98 ± 1.15 / 74.44 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">17.98 ± 1.97 / 56.01 ± 2.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.07 ± 0.74 / 64.24 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>12.0.0</td> <!-- SUC3 version -->
   <td>12.0.0</td> <!-- SweReC version -->
   <td>12.0.0</td> <!-- ScaLA-sv version -->
   <td>12.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.1</td> <!-- SweReC version -->
   <td>12.5.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">973 ± 251 / 174 ± 59</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="sv ner">44.80 ± 2.36 / 34.91 ± 2.67</td> <!-- SUC3 -->
   <td class="sv sent">75.92 ± 2.44 / 75.77 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">24.84 ± 2.78 / 59.88 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.71 ± 1.65 / 62.01 ± 1.64</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,007 ± 316 / 162 ± 45</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">104</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="sv ner">74.13 ± 1.17 / 68.93 ± 1.36</td> <!-- SUC3 -->
   <td class="sv sent">62.18 ± 1.26 / 59.44 ± 2.35</td> <!-- SweReC -->
   <td class="sv la">36.93 ± 6.47 / 65.97 ± 6.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.59 ± 1.99 / 41.94 ± 2.23</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama3-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,695 ± 1,277 / 532 ± 183</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="sv ner">63.19 ± 2.83 / 51.22 ± 3.61</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.64 / 61.59 ± 0.77</td> <!-- SweReC -->
   <td class="sv la">5.34 ± 1.42 / 34.32 ± 0.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.70 ± 0.87 / 66.00 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,151 ± 294 / 227 ± 76</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="sv ner">53.00 ± 2.53 / 39.09 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">79.70 ± 0.65 / 79.45 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">4.32 ± 2.19 / 34.43 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.03 ± 1.03 / 64.74 ± 0.84</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="sv ner">71.07 ± 1.59 / 65.46 ± 1.28</td> <!-- SUC3 -->
   <td class="sv sent">66.42 ± 0.72 / 57.57 ± 1.23</td> <!-- SweReC -->
   <td class="sv la">69.19 ± 0.66 / 84.26 ± 0.36</td> <!-- ScaLA-sv -->
   <td class="sv rc">11.85 ± 4.94 / 13.02 ± 5.55</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="sv ner">52.34 ± 3.07 / 39.14 ± 4.60</td> <!-- SUC3 -->
   <td class="sv sent">77.66 ± 2.09 / 78.59 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.00 ± 4.15 / 36.34 ± 2.20</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.81 / 64.12 ± 1.59</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.1</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="sv ner">71.34 ± 0.91 / 65.04 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">70.91 ± 1.23 / 67.12 ± 3.79</td> <!-- SweReC -->
   <td class="sv la">53.52 ± 1.22 / 76.15 ± 0.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.41 ± 4.10 / 18.47 ± 4.44</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.31 ± 0.92 / 63.73 ± 1.04</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="sv ner">49.90 ± 2.28 / 35.48 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 2.05 / 79.13 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">14.67 ± 2.27 / 53.90 ± 2.24</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.12 ± 0.70 / 63.72 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="sv ner">42.23 ± 2.44 / 30.30 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">78.80 ± 0.93 / 75.28 ± 1.78</td> <!-- SweReC -->
   <td class="sv la">15.47 ± 1.79 / 54.26 ± 3.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.75 ± 1.15 / 62.43 ± 0.95</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="sv ner">44.94 ± 2.91 / 35.67 ± 3.53</td> <!-- SUC3 -->
   <td class="sv sent">76.78 ± 1.63 / 78.27 ± 1.22</td> <!-- SweReC -->
   <td class="sv la">16.96 ± 2.77 / 55.03 ± 3.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.83 ± 1.02 / 63.13 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-small</td> <!-- Model ID -->
   <td class="num_model_parameters">41</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,515 ± 2,514 / 3,042 ± 1,004</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="sv ner">74.22 ± 1.37 / 68.68 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">63.80 ± 1.56 / 57.65 ± 2.24</td> <!-- SweReC -->
   <td class="sv la">37.77 ± 5.16 / 65.87 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.45 ± 0.94 / 35.81 ± 0.94</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.16 ± 1.23 / 65.78 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="sv ner">72.33 ± 0.82 / 67.15 ± 0.85</td> <!-- SUC3 -->
   <td class="sv sent">67.77 ± 1.19 / 62.98 ± 2.57</td> <!-- SweReC -->
   <td class="sv la">33.79 ± 7.61 / 64.01 ± 6.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.71 ± 0.77 / 37.46 ± 0.64</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="sv ner">46.74 ± 4.30 / 33.57 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">77.06 ± 1.82 / 79.02 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">14.00 ± 1.59 / 53.89 ± 3.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.74 ± 0.52 / 63.45 ± 0.49</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="sv ner">51.06 ± 2.85 / 31.63 ± 3.67</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 1.09 / 67.88 ± 3.15</td> <!-- SweReC -->
   <td class="sv la">5.88 ± 3.89 / 38.51 ± 4.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.43 ± 1.04 / 62.93 ± 0.94</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="sv ner">78.60 ± 1.91 / 73.04 ± 2.25</td> <!-- SUC3 -->
   <td class="sv sent">73.67 ± 1.48 / 68.61 ± 3.14</td> <!-- SweReC -->
   <td class="sv la">15.41 ± 4.59 / 53.29 ± 3.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.41 ± 3.14 / 37.13 ± 3.07</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="sv ner">58.84 ± 13.92 / 53.63 ± 12.63</td> <!-- SUC3 -->
   <td class="sv sent">72.28 ± 0.79 / 71.62 ± 1.38</td> <!-- SweReC -->
   <td class="sv la">37.61 ± 17.89 / 66.93 ± 9.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.59 ± 0.68 / 35.43 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="sv ner">50.85 ± 2.44 / 39.65 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">74.17 ± 2.12 / 76.62 ± 1.83</td> <!-- SweReC -->
   <td class="sv la">7.51 ± 1.94 / 37.81 ± 1.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.32 ± 0.63 / 63.28 ± 0.71</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-13B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 645 / 709 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="sv ner">49.26 ± 2.31 / 36.92 ± 4.05</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 0.80 / 77.87 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">0.22 ± 0.43 / 33.38 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.78 ± 1.02 / 63.61 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="sv ner">68.94 ± 1.53 / 62.54 ± 1.20</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 0.89 / 68.13 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">40.21 ± 2.53 / 67.11 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.09 ± 1.31 / 25.99 ± 1.19</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,735 ± 7,558 / 6,846 ± 2,312</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="sv ner">79.43 ± 1.07 / 74.17 ± 1.10</td> <!-- SUC3 -->
   <td class="sv sent">71.48 ± 2.63 / 65.72 ± 4.78</td> <!-- SweReC -->
   <td class="sv la">7.26 ± 2.18 / 45.42 ± 4.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.72 ± 1.71 / 38.23 ± 1.57</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="sv ner">59.77 ± 3.55 / 45.71 ± 4.91</td> <!-- SUC3 -->
   <td class="sv sent">74.45 ± 1.19 / 72.26 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">3.97 ± 1.50 / 34.79 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 1.05 / 56.07 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="sv ner">43.74 ± 2.58 / 34.37 ± 2.59</td> <!-- SUC3 -->
   <td class="sv sent">76.98 ± 1.31 / 71.38 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">16.01 ± 2.24 / 51.83 ± 3.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.38 ± 1.78 / 57.83 ± 0.99</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>distilbert/distilbert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,355 ± 5,946 / 5,266 ± 1,714</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="sv ner">70.08 ± 1.38 / 64.46 ± 1.31</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.22 / 56.16 ± 2.13</td> <!-- SweReC -->
   <td class="sv la">33.71 ± 1.12 / 65.32 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.48 ± 1.85 / 36.44 ± 1.87</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="sv ner">70.22 ± 1.49 / 63.97 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">71.33 ± 1.20 / 65.44 ± 3.64</td> <!-- SweReC -->
   <td class="sv la">39.60 ± 5.87 / 66.60 ± 3.19</td> <!-- ScaLA-sv -->
   <td class="sv rc">18.65 ± 1.15 / 24.75 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-33B@1000B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,080 ± 700 / 331 ± 117</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="sv ner">42.35 ± 1.51 / 28.31 ± 3.87</td> <!-- SUC3 -->
   <td class="sv sent">77.68 ± 1.11 / 78.86 ± 0.93</td> <!-- SweReC -->
   <td class="sv la">8.08 ± 1.69 / 50.52 ± 2.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.57 ± 1.25 / 60.34 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="sv ner">74.26 ± 1.65 / 68.20 ± 1.70</td> <!-- SUC3 -->
   <td class="sv sent">63.35 ± 5.43 / 60.33 ± 5.50</td> <!-- SweReC -->
   <td class="sv la">16.07 ± 10.73 / 52.48 ± 7.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">36.77 ± 3.78 / 41.72 ± 3.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="sv ner">76.31 ± 1.29 / 70.91 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">73.32 ± 1.13 / 70.21 ± 3.74</td> <!-- SweReC -->
   <td class="sv la">32.29 ± 10.98 / 62.21 ± 5.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.12 ± 5.80 / 19.52 ± 6.73</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.2.0</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="sv ner">52.85 ± 2.76 / 35.11 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">73.93 ± 1.58 / 73.97 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">8.27 ± 2.90 / 43.29 ± 4.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.49 ± 0.77 / 54.50 ± 0.73</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="sv ner">65.14 ± 1.57 / 59.82 ± 1.39</td> <!-- SUC3 -->
   <td class="sv sent">73.47 ± 0.84 / 70.20 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">36.62 ± 6.55 / 66.09 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">18.65 ± 0.91 / 25.00 ± 0.87</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="sv ner">70.56 ± 1.36 / 64.49 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">60.69 ± 0.46 / 56.69 ± 1.35</td> <!-- SweReC -->
   <td class="sv la">30.83 ± 1.47 / 63.39 ± 1.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.41 ± 1.05 / 36.45 ± 1.05</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="sv ner">47.24 ± 3.36 / 24.94 ± 3.21</td> <!-- SUC3 -->
   <td class="sv sent">77.91 ± 1.42 / 76.08 ± 2.54</td> <!-- SweReC -->
   <td class="sv la">5.55 ± 2.55 / 48.57 ± 3.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.41 ± 0.74 / 57.55 ± 0.69</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>neuralmagic/Sparse-Llama-3.1-8B-2of4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,841 ± 509 / 865 ± 263</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="sv ner">33.21 ± 2.39 / 32.18 ± 2.40</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 0.92 / 76.28 ± 1.76</td> <!-- SweReC -->
   <td class="sv la">10.51 ± 3.79 / 49.04 ± 4.63</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.15 ± 1.06 / 63.06 ± 0.85</td> <!-- ScandiQA-sv -->
   <td>13.2.0</td> <!-- SUC3 version -->
   <td>13.2.0</td> <!-- SweReC version -->
   <td>13.2.0</td> <!-- ScaLA-sv version -->
   <td>13.2.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="sv ner">42.87 ± 3.17 / 40.34 ± 2.52</td> <!-- SUC3 -->
   <td class="sv sent">79.18 ± 0.46 / 76.66 ± 1.44</td> <!-- SweReC -->
   <td class="sv la">8.65 ± 1.60 / 46.95 ± 3.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.56 ± 0.79 / 57.58 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="sv ner">45.23 ± 3.64 / 37.99 ± 4.03</td> <!-- SUC3 -->
   <td class="sv sent">72.76 ± 2.25 / 72.65 ± 2.38</td> <!-- SweReC -->
   <td class="sv la">11.25 ± 2.04 / 51.22 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.22 ± 0.70 / 59.36 ± 0.78</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">76</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">42</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,081 ± 5,875 / 5,209 ± 1,692</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="sv ner">69.94 ± 1.11 / 63.93 ± 1.47</td> <!-- SUC3 -->
   <td class="sv sent">59.83 ± 1.11 / 55.15 ± 0.99</td> <!-- SweReC -->
   <td class="sv la">29.82 ± 1.23 / 63.32 ± 1.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.13 ± 1.15 / 36.20 ± 1.22</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-40b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">39927</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">409 ± 53 / 182 ± 54</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="sv ner">32.00 ± 3.27 / 17.02 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">80.44 ± 0.54 / 77.81 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">10.73 ± 2.53 / 51.37 ± 4.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.80 ± 0.86 / 60.53 ± 0.78</td> <!-- ScandiQA-sv -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">79.20 ± 1.03 / 79.87 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>12.10.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">61</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">28,950 ± 5,114 / 7,010 ± 2,267</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">69.25 ± 1.37 / 63.90 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">58.47 ± 1.30 / 56.03 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">29.80 ± 1.57 / 63.53 ± 0.90</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.61 ± 1.31 / 35.37 ± 1.52</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,196 ± 5,956 / 5,220 ± 1,691</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">69.62 ± 0.88 / 63.51 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">59.42 ± 1.21 / 55.74 ± 1.26</td> <!-- SweReC -->
   <td class="sv la">29.01 ± 2.06 / 62.65 ± 1.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">31.82 ± 1.07 / 36.82 ± 1.14</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">41.49 ± 2.82 / 38.09 ± 2.86</td> <!-- SUC3 -->
   <td class="sv sent">75.64 ± 1.51 / 76.06 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">0.66 ± 1.97 / 33.73 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.48 ± 0.54 / 63.85 ± 0.46</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.22 ± 0.88 / 61.85 ± 0.63</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="sv ner">69.28 ± 1.15 / 63.61 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">59.53 ± 1.69 / 57.93 ± 2.20</td> <!-- SweReC -->
   <td class="sv la">29.36 ± 1.50 / 63.60 ± 0.89</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.42 ± 1.54 / 35.34 ± 1.63</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="sv ner">68.83 ± 1.00 / 63.29 ± 1.48</td> <!-- SUC3 -->
   <td class="sv sent">64.25 ± 1.66 / 63.62 ± 2.92</td> <!-- SweReC -->
   <td class="sv la">28.62 ± 9.43 / 59.33 ± 5.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.78 ± 2.01 / 34.26 ± 2.03</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="sv ner">45.55 ± 2.18 / 26.78 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">70.71 ± 1.99 / 71.19 ± 1.14</td> <!-- SweReC -->
   <td class="sv la">4.83 ± 3.48 / 36.64 ± 2.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.25 ± 1.21 / 61.21 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="sv ner">35.61 ± 2.19 / 26.05 ± 2.45</td> <!-- SUC3 -->
   <td class="sv sent">75.84 ± 1.41 / 77.22 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">15.62 ± 1.67 / 51.30 ± 3.09</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.76 ± 0.92 / 58.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="sv ner">48.78 ± 5.08 / 26.81 ± 3.42</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 1.23 / 74.78 ± 1.97</td> <!-- SweReC -->
   <td class="sv la">2.53 ± 2.80 / 47.37 ± 2.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.93 ± 0.97 / 55.09 ± 0.85</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="sv ner">32.37 ± 3.05 / 24.60 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">75.33 ± 2.41 / 77.99 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">12.73 ± 6.32 / 45.51 ± 7.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.05 ± 1.83 / 58.32 ± 1.46</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Addedk/mbert-swedish-distilled-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,091 ± 5,835 / 5,209 ± 1,690</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="sv ner">73.41 ± 1.54 / 66.98 ± 1.68</td> <!-- SUC3 -->
   <td class="sv sent">62.10 ± 1.18 / 60.27 ± 2.82</td> <!-- SweReC -->
   <td class="sv la">34.86 ± 1.29 / 66.98 ± 0.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">18.10 ± 2.67 / 21.09 ± 3.18</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Phi-3-mini-4k-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,360 ± 179 / 566 ± 190</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">47.81 ± 2.60 / 27.94 ± 5.79</td> <!-- SUC3 -->
   <td class="sv sent">68.43 ± 2.12 / 68.82 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">3.63 ± 1.46 / 43.69 ± 4.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.03 ± 0.62 / 58.80 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">30.45 ± 3.49 / 23.98 ± 3.18</td> <!-- SUC3 -->
   <td class="sv sent">76.36 ± 1.10 / 65.98 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">6.06 ± 2.07 / 49.80 ± 2.71</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.19 ± 0.71 / 60.59 ± 0.61</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">51.76 ± 4.53 / 41.73 ± 6.65</td> <!-- SUC3 -->
   <td class="sv sent">70.61 ± 1.12 / 60.47 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">6.24 ± 3.11 / 46.34 ± 5.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.67 ± 1.34 / 50.56 ± 1.33</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,004 ± 2,244 / 2,324 ± 761</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="sv ner">70.57 ± 1.07 / 70.41 ± 0.93</td> <!-- SUC3 -->
   <td class="sv sent">66.01 ± 1.43 / 57.28 ± 0.85</td> <!-- SweReC -->
   <td class="sv la">10.20 ± 5.38 / 50.80 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.71 ± 0.94 / 36.08 ± 0.92</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="sv ner">53.95 ± 1.89 / 42.16 ± 4.59</td> <!-- SUC3 -->
   <td class="sv sent">60.91 ± 2.35 / 59.47 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">0.32 ± 0.62 / 33.39 ± 0.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.28 ± 0.62 / 63.41 ± 0.55</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,194 ± 687 / 650 ± 216</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="sv ner">66.50 ± 1.49 / 59.99 ± 1.40</td> <!-- SUC3 -->
   <td class="sv sent">72.19 ± 0.71 / 67.88 ± 2.34</td> <!-- SweReC -->
   <td class="sv la">28.75 ± 5.58 / 63.30 ± 2.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">15.91 ± 0.87 / 23.08 ± 0.95</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td>12.10.8</td> <!-- SUC3 version -->
   <td>12.10.8</td> <!-- SweReC version -->
   <td>12.10.8</td> <!-- ScaLA-sv version -->
   <td>12.10.8</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">3969</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="sv ner">51.45 ± 3.13 / 26.49 ± 3.00</td> <!-- SUC3 -->
   <td class="sv sent">63.64 ± 3.74 / 65.08 ± 2.46</td> <!-- SweReC -->
   <td class="sv la">5.80 ± 1.74 / 51.04 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.95 ± 1.00 / 57.09 ± 0.92</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.57 ± 0.94 / 56.51 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="sv ner">40.68 ± 2.32 / 24.33 ± 2.43</td> <!-- SUC3 -->
   <td class="sv sent">68.96 ± 2.04 / 72.76 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">4.77 ± 1.97 / 43.64 ± 5.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.73 ± 0.76 / 56.63 ± 0.69</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="sv ner">66.11 ± 1.24 / 61.03 ± 1.08</td> <!-- SUC3 -->
   <td class="sv sent">59.66 ± 1.84 / 55.24 ± 1.32</td> <!-- SweReC -->
   <td class="sv la">26.28 ± 8.44 / 59.64 ± 5.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">24.36 ± 0.92 / 30.54 ± 0.96</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="sv ner">36.54 ± 2.70 / 28.79 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">68.85 ± 5.19 / 70.02 ± 3.95</td> <!-- SweReC -->
   <td class="sv la">2.60 ± 2.58 / 40.21 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.58 ± 0.89 / 59.78 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-33b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">501 ± 50 / 238 ± 69</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="sv ner">33.61 ± 6.02 / 22.18 ± 4.32</td> <!-- SUC3 -->
   <td class="sv sent">76.75 ± 1.17 / 74.66 ± 1.20</td> <!-- SweReC -->
   <td class="sv la">1.66 ± 1.36 / 33.60 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.68 ± 1.94 / 56.96 ± 1.73</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.10.0</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="sv ner">50.10 ± 4.30 / 42.80 ± 5.47</td> <!-- SUC3 -->
   <td class="sv sent">65.67 ± 3.92 / 64.00 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">4.55 ± 2.18 / 45.11 ± 4.32</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.83 ± 1.02 / 49.35 ± 1.09</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="sv ner">41.60 ± 2.74 / 37.22 ± 3.26</td> <!-- SUC3 -->
   <td class="sv sent">71.86 ± 2.01 / 71.15 ± 2.16</td> <!-- SweReC -->
   <td class="sv la">3.72 ± 1.40 / 48.04 ± 1.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.57 ± 1.35 / 52.90 ± 1.42</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-13b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,520 ± 736 / 823 ± 273</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="sv ner">32.19 ± 4.64 / 24.93 ± 4.09</td> <!-- SUC3 -->
   <td class="sv sent">72.26 ± 6.90 / 72.58 ± 5.87</td> <!-- SweReC -->
   <td class="sv la">2.39 ± 1.29 / 48.49 ± 2.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.92 ± 2.28 / 53.44 ± 2.49</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.33 ± 1.03 / 64.03 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="sv ner">65.50 ± 1.20 / 59.72 ± 1.22</td> <!-- SUC3 -->
   <td class="sv sent">68.36 ± 1.18 / 63.94 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">14.81 ± 6.63 / 55.50 ± 4.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.11 ± 1.18 / 22.88 ± 1.34</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="sv ner">30.64 ± 4.19 / 23.90 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.02 ± 3.18 / 72.36 ± 3.96</td> <!-- SweReC -->
   <td class="sv la">1.08 ± 1.36 / 38.63 ± 3.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.72 ± 1.05 / 54.59 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="sv ner">29.89 ± 7.13 / 27.65 ± 6.45</td> <!-- SUC3 -->
   <td class="sv sent">74.33 ± 1.07 / 73.73 ± 1.77</td> <!-- SweReC -->
   <td class="sv la">1.06 ± 1.79 / 43.95 ± 3.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.89 ± 2.72 / 52.70 ± 3.39</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="sv ner">27.41 ± 2.70 / 24.45 ± 3.82</td> <!-- SUC3 -->
   <td class="sv sent">72.24 ± 0.82 / 68.89 ± 2.63</td> <!-- SweReC -->
   <td class="sv la">0.13 ± 1.85 / 36.22 ± 3.14</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.77 ± 0.63 / 56.59 ± 0.54</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="sv ner">65.95 ± 1.70 / 60.53 ± 1.38</td> <!-- SUC3 -->
   <td class="sv sent">64.02 ± 2.78 / 62.27 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">0.80 ± 0.78 / 47.24 ± 3.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.46 ± 0.90 / 33.13 ± 0.88</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="sv ner">37.37 ± 1.87 / 26.31 ± 3.34</td> <!-- SUC3 -->
   <td class="sv sent">64.46 ± 3.06 / 69.83 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">4.49 ± 1.96 / 46.63 ± 4.39</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.92 ± 1.06 / 49.57 ± 1.17</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="sv ner">35.96 ± 3.50 / 26.41 ± 4.11</td> <!-- SUC3 -->
   <td class="sv sent">68.31 ± 1.43 / 72.51 ± 1.03</td> <!-- SweReC -->
   <td class="sv la">3.61 ± 1.79 / 49.47 ± 1.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.26 ± 1.85 / 49.32 ± 1.97</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="sv ner">15.70 ± 1.54 / 14.65 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">68.23 ± 3.81 / 71.17 ± 3.07</td> <!-- SweReC -->
   <td class="sv la">12.39 ± 1.39 / 50.99 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.04 ± 0.97 / 60.86 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,297 ± 338 / 245 ± 83</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="sv ner">53.65 ± 2.53 / 39.64 ± 3.15</td> <!-- SUC3 -->
   <td class="sv sent">79.91 ± 0.83 / 75.33 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">14.15 ± 4.12 / 41.21 ± 4.42</td> <!-- ScaLA-sv -->
   <td class="sv rc">10.43 ± 3.47 / 27.86 ± 4.03</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-xs</td> <!-- Model ID -->
   <td class="num_model_parameters">15</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">508</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,208 ± 2,713 / 3,059 ± 1,002</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="sv ner">67.53 ± 1.66 / 62.96 ± 1.62</td> <!-- SUC3 -->
   <td class="sv sent">59.27 ± 2.14 / 55.26 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.83 ± 2.01 / 49.25 ± 1.48</td> <!-- ScaLA-sv -->
   <td class="sv rc">24.11 ± 2.76 / 27.79 ± 2.63</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">130947</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="sv ner">36.01 ± 3.07 / 24.61 ± 4.22</td> <!-- SUC3 -->
   <td class="sv sent">57.18 ± 5.33 / 62.72 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 2.14 / 38.30 ± 3.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.04 ± 0.95 / 56.97 ± 0.96</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="sv ner">35.02 ± 2.08 / 17.87 ± 0.89</td> <!-- SUC3 -->
   <td class="sv sent">51.80 ± 4.28 / 57.15 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">6.15 ± 0.86 / 36.62 ± 0.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.85 ± 0.74 / 60.00 ± 0.48</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="sv ner">58.01 ± 1.23 / 53.87 ± 1.25</td> <!-- SUC3 -->
   <td class="sv sent">57.67 ± 1.61 / 53.64 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">13.40 ± 4.31 / 55.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">24.92 ± 0.80 / 30.11 ± 0.83</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="sv ner">19.04 ± 2.67 / 19.98 ± 2.64</td> <!-- SUC3 -->
   <td class="sv sent">73.34 ± 1.34 / 68.41 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.90 ± 1.74 / 44.43 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.45 ± 0.58 / 54.69 ± 0.56</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="sv ner">47.19 ± 9.01 / 44.34 ± 8.27</td> <!-- SUC3 -->
   <td class="sv sent">56.57 ± 1.41 / 53.47 ± 0.84</td> <!-- SweReC -->
   <td class="sv la">20.92 ± 4.12 / 59.05 ± 1.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">23.86 ± 1.25 / 30.47 ± 1.51</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,136 ± 558 / 942 ± 290</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="sv ner">29.08 ± 2.82 / 25.68 ± 3.52</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 1.71 / 69.73 ± 1.24</td> <!-- SweReC -->
   <td class="sv la">0.50 ± 1.34 / 45.71 ± 2.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.52 ± 0.88 / 54.03 ± 0.77</td> <!-- ScandiQA-sv -->
   <td>13.2.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.2.0</td> <!-- ScaLA-sv version -->
   <td>13.2.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="sv ner">27.07 ± 6.33 / 25.24 ± 4.89</td> <!-- SUC3 -->
   <td class="sv sent">61.96 ± 2.69 / 67.81 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">2.65 ± 1.46 / 40.25 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.16 ± 0.91 / 52.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,340 ± 3,185 / 5,178 ± 1,700</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="sv ner">52.79 ± 1.21 / 48.47 ± 0.71</td> <!-- SUC3 -->
   <td class="sv sent">57.93 ± 1.56 / 53.71 ± 0.61</td> <!-- SweReC -->
   <td class="sv la">14.72 ± 2.01 / 55.92 ± 1.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.54 ± 0.97 / 26.37 ± 0.75</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="sv ner">23.25 ± 1.99 / 20.55 ± 2.20</td> <!-- SUC3 -->
   <td class="sv sent">71.70 ± 1.09 / 71.01 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">-0.82 ± 2.23 / 40.80 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.48 ± 1.52 / 46.93 ± 1.61</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 0.54 / 57.90 ± 0.53</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.55 ± 0.85 / 51.69 ± 0.79</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="sv ner">55.06 ± 0.96 / 51.37 ± 1.03</td> <!-- SUC3 -->
   <td class="sv sent">53.70 ± 1.46 / 51.98 ± 0.58</td> <!-- SweReC -->
   <td class="sv la">12.38 ± 3.23 / 55.18 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">22.53 ± 0.86 / 27.59 ± 0.94</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,091 ± 2,427 / 4,575 ± 1,485</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="sv ner">50.29 ± 1.22 / 47.15 ± 1.18</td> <!-- SUC3 -->
   <td class="sv sent">57.42 ± 1.88 / 56.53 ± 1.66</td> <!-- SweReC -->
   <td class="sv la">4.94 ± 1.62 / 51.57 ± 1.19</td> <!-- ScaLA-sv -->
   <td class="sv rc">24.16 ± 1.28 / 30.28 ± 1.18</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/encoder-medium-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,130 ± 2,433 / 4,566 ± 1,473</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="sv ner">49.62 ± 2.01 / 46.05 ± 2.11</td> <!-- SUC3 -->
   <td class="sv sent">58.70 ± 2.54 / 58.15 ± 3.35</td> <!-- SweReC -->
   <td class="sv la">2.23 ± 2.12 / 46.43 ± 4.85</td> <!-- ScaLA-sv -->
   <td class="sv rc">25.45 ± 0.75 / 30.80 ± 0.81</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">3969</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,027 ± 503 / 903 ± 296</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="sv ner">20.97 ± 2.51 / 16.21 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 0.75 / 67.99 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.35 ± 1.63 / 38.48 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.65 ± 2.11 / 38.84 ± 1.85</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="sv ner">38.36 ± 1.60 / 37.63 ± 1.73</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 1.72 / 56.25 ± 1.72</td> <!-- SweReC -->
   <td class="sv la">19.40 ± 5.65 / 58.63 ± 3.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">19.23 ± 0.59 / 26.64 ± 0.90</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="sv ner">18.83 ± 6.41 / 17.59 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">53.68 ± 10.39 / 58.92 ± 10.87</td> <!-- SweReC -->
   <td class="sv la">3.49 ± 2.20 / 46.13 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.81 ± 0.70 / 55.99 ± 0.69</td> <!-- ScandiQA-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,964 ± 2,255 / 1,299 ± 433</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="sv ner">33.80 ± 1.96 / 21.70 ± 3.21</td> <!-- SUC3 -->
   <td class="sv sent">58.78 ± 1.36 / 60.51 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">0.72 ± 1.17 / 45.33 ± 3.14</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.45 ± 1.87 / 42.40 ± 2.14</td> <!-- ScandiQA-sv -->
   <td>13.2.0</td> <!-- SUC3 version -->
   <td>13.2.0</td> <!-- SweReC version -->
   <td>13.2.0</td> <!-- ScaLA-sv version -->
   <td>13.2.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannesg/bertsson</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,314 ± 2,786 / 3,666 ± 1,201</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="sv ner">51.13 ± 2.13 / 46.67 ± 1.98</td> <!-- SUC3 -->
   <td class="sv sent">61.67 ± 1.40 / 59.12 ± 2.44</td> <!-- SweReC -->
   <td class="sv la">2.87 ± 1.53 / 48.92 ± 2.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.24 ± 1.13 / 25.10 ± 1.06</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jannikskytt/MeDa-Bert</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">511</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,114 ± 2,429 / 4,566 ± 1,482</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="sv ner">48.32 ± 1.62 / 45.04 ± 1.50</td> <!-- SUC3 -->
   <td class="sv sent">53.98 ± 2.05 / 52.94 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">3.33 ± 2.12 / 51.06 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">23.15 ± 2.61 / 29.17 ± 2.19</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="sv ner">49.86 ± 1.85 / 44.53 ± 1.58</td> <!-- SUC3 -->
   <td class="sv sent">60.06 ± 1.30 / 55.65 ± 1.34</td> <!-- SweReC -->
   <td class="sv la">3.18 ± 1.63 / 48.38 ± 1.42</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.08 ± 2.60 / 23.46 ± 3.10</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,296 ± 335 / 246 ± 84</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="sv ner">32.54 ± 4.81 / 26.20 ± 4.00</td> <!-- SUC3 -->
   <td class="sv sent">43.55 ± 16.01 / 46.98 ± 12.54</td> <!-- SweReC -->
   <td class="sv la">1.93 ± 1.31 / 42.44 ± 4.14</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.80 ± 1.75 / 51.57 ± 1.61</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">62.71 ± 0.81 / 57.24 ± 1.73</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.76 ± 1.03 / 17.62 ± 1.24</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="sv ner">51.67 ± 1.46 / 53.62 ± 1.02</td> <!-- SUC3 -->
   <td class="sv sent">63.04 ± 0.70 / 56.50 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">2.32 ± 1.83 / 48.77 ± 1.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.93 ± 1.00 / 17.75 ± 1.16</td> <!-- ScandiQA-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">3.23</td> <!-- ScandEval rank -->
   <td class="sv ner">57.82 ± 1.40 / 54.55 ± 1.33</td> <!-- SUC3 -->
   <td class="sv sent">55.68 ± 1.09 / 52.81 ± 0.44</td> <!-- SweReC -->
   <td class="sv la">19.26 ± 1.80 / 58.62 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="sv ner">50.07 ± 4.14 / 47.04 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">56.10 ± 1.85 / 52.92 ± 0.76</td> <!-- SweReC -->
   <td class="sv la">5.05 ± 2.27 / 51.08 ± 1.44</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.49 ± 1.13 / 22.34 ± 1.16</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.57 ± 2.45 / 41.66 ± 2.41</td> <!-- ScandiQA-sv -->
   <td>9.1.2</td> <!-- SUC3 version -->
   <td>9.1.2</td> <!-- SweReC version -->
   <td>9.1.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.29</td> <!-- ScandEval rank -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.23 ± 1.07 / 46.83 ± 0.82</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1385</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,808 ± 2,183 / 1,289 ± 428</td> <!-- Model inference speed -->
   <td class="rank">3.29</td> <!-- ScandEval rank -->
   <td class="sv ner">23.26 ± 5.42 / 20.21 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">55.06 ± 5.28 / 50.38 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">1.81 ± 2.14 / 40.07 ± 4.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.49 ± 2.28 / 39.42 ± 2.19</td> <!-- ScandiQA-sv -->
   <td>13.2.0</td> <!-- SUC3 version -->
   <td>13.2.0</td> <!-- SweReC version -->
   <td>13.2.0</td> <!-- ScaLA-sv version -->
   <td>13.2.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="sv ner">36.29 ± 4.00 / 31.64 ± 3.95</td> <!-- SUC3 -->
   <td class="sv sent">43.31 ± 11.42 / 47.97 ± 7.92</td> <!-- SweReC -->
   <td class="sv la">1.76 ± 1.39 / 36.32 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.64 ± 1.84 / 38.42 ± 1.95</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="sv ner">14.84 ± 1.63 / 15.90 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 3.60 / 54.09 ± 1.46</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.21 / 34.76 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.37 ± 1.36 / 40.44 ± 1.53</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>jjzha/dajobbert-base-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,243 ± 2,428 / 4,593 ± 1,484</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="sv ner">42.99 ± 1.57 / 39.98 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">55.49 ± 1.28 / 55.99 ± 2.15</td> <!-- SweReC -->
   <td class="sv la">4.69 ± 2.28 / 51.01 ± 1.58</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.22 ± 1.90 / 20.83 ± 1.46</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="sv ner">21.42 ± 6.21 / 20.27 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">52.35 ± 5.28 / 53.31 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.58 / 41.75 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.71 ± 2.02 / 37.44 ± 2.20</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="sv ner">37.17 ± 2.59 / 25.25 ± 1.61</td> <!-- SUC3 -->
   <td class="sv sent">20.20 ± 4.93 / 21.73 ± 5.47</td> <!-- SweReC -->
   <td class="sv la">6.13 ± 1.52 / 39.55 ± 1.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.66 ± 1.19 / 56.90 ± 1.10</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="sv ner">39.17 ± 4.06 / 36.74 ± 3.78</td> <!-- SUC3 -->
   <td class="sv sent">57.71 ± 1.40 / 53.54 ± 0.59</td> <!-- SweReC -->
   <td class="sv la">17.10 ± 2.57 / 57.41 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.11 ± 0.11 / 0.13 ± 0.12</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,424 ± 1,080 / 464 ± 158</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="sv ner">4.49 ± 3.07 / 4.08 ± 2.82</td> <!-- SUC3 -->
   <td class="sv sent">66.82 ± 3.87 / 65.85 ± 3.21</td> <!-- SweReC -->
   <td class="sv la">3.07 ± 2.81 / 41.18 ± 4.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">22.14 ± 3.47 / 29.52 ± 4.26</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.70 ± 1.46 / 38.82 ± 1.54</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="sv ner">42.78 ± 3.26 / 40.46 ± 3.04</td> <!-- SUC3 -->
   <td class="sv sent">44.95 ± 2.30 / 48.17 ± 1.06</td> <!-- SweReC -->
   <td class="sv la">1.43 ± 1.34 / 48.66 ± 2.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">8.71 ± 2.58 / 16.77 ± 2.50</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.81 ± 2.73 / 35.67 ± 2.95</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="sv ner">26.87 ± 2.26 / 25.42 ± 2.14</td> <!-- SUC3 -->
   <td class="sv sent">57.41 ± 1.89 / 53.50 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">-1.06 ± 1.33 / 48.72 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv rc">5.54 ± 1.44 / 10.83 ± 2.62</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,880 ± 556 / 280 ± 95</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="sv ner">1.37 ± 0.87 / 1.26 ± 0.79</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.49 / 63.33 ± 2.32</td> <!-- SweReC -->
   <td class="sv la">6.19 ± 4.39 / 41.49 ± 6.70</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.45 ± 0.33 / 8.27 ± 1.38</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="sv ner">14.09 ± 5.11 / 15.95 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">32.88 ± 12.10 / 40.51 ± 7.40</td> <!-- SweReC -->
   <td class="sv la">0.55 ± 0.60 / 33.45 ± 0.32</td> <!-- ScaLA-sv -->
   <td class="sv rc">32.00 ± 1.48 / 37.80 ± 1.63</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="sv ner">22.09 ± 2.91 / 21.86 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">33.63 ± 11.18 / 41.43 ± 7.35</td> <!-- SweReC -->
   <td class="sv la">0.59 ± 0.94 / 37.25 ± 4.09</td> <!-- ScaLA-sv -->
   <td class="sv rc">21.60 ± 1.52 / 26.25 ± 1.48</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RabotaRu/HRBert-mini</td> <!-- Model ID -->
   <td class="num_model_parameters">80</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">54,951 ± 11,500 / 11,401 ± 3,819</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="sv ner">24.61 ± 1.58 / 23.05 ± 1.43</td> <!-- SUC3 -->
   <td class="sv sent">52.31 ± 1.22 / 51.51 ± 0.49</td> <!-- SweReC -->
   <td class="sv la">1.32 ± 1.87 / 46.80 ± 4.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">2.86 ± 0.73 / 8.44 ± 2.01</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">83</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">52</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,013 ± 4,309 / 8,840 ± 2,859</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="sv ner">22.47 ± 1.55 / 20.74 ± 1.42</td> <!-- SUC3 -->
   <td class="sv sent">53.88 ± 1.97 / 52.30 ± 1.04</td> <!-- SweReC -->
   <td class="sv la">1.55 ± 1.62 / 44.06 ± 3.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">1.12 ± 0.85 / 3.07 ± 1.91</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="sv ner">16.28 ± 4.73 / 16.34 ± 4.84</td> <!-- SUC3 -->
   <td class="sv sent">26.98 ± 10.16 / 37.60 ± 6.58</td> <!-- SweReC -->
   <td class="sv la">0.60 ± 1.43 / 38.74 ± 4.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.78 ± 2.45 / 22.13 ± 2.29</td> <!-- ScandiQA-sv -->
   <td>14.0.4</td> <!-- SUC3 version -->
   <td>14.0.4</td> <!-- SweReC version -->
   <td>14.0.4</td> <!-- ScaLA-sv version -->
   <td>14.0.4</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="sv ner">11.91 ± 3.04 / 11.31 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.11 ± 5.32 / 50.09 ± 3.33</td> <!-- SweReC -->
   <td class="sv la">0.86 ± 0.82 / 39.16 ± 3.63</td> <!-- ScaLA-sv -->
   <td class="sv rc">2.00 ± 0.63 / 7.20 ± 1.68</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="sv ner">10.54 ± 1.12 / 9.71 ± 1.00</td> <!-- SUC3 -->
   <td class="sv sent">55.54 ± 2.75 / 52.75 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">-0.15 ± 0.52 / 35.33 ± 3.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.02 ± 0.03 / 0.04 ± 0.05</td> <!-- ScandiQA-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>0.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="sv ner">18.22 ± 1.75 / 17.97 ± 2.10</td> <!-- SUC3 -->
   <td class="sv sent">11.52 ± 7.20 / 29.30 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.72 ± 1.21 / 34.96 ± 1.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">27.27 ± 3.03 / 31.25 ± 3.24</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.09</td> <!-- ScandEval rank -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.82 ± 11.21 / 31.12 ± 8.39</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.10</td> <!-- ScandEval rank -->
   <td class="sv ner">13.64 ± 5.84 / 16.38 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">9.34 ± 6.26 / 26.00 ± 3.56</td> <!-- SweReC -->
   <td class="sv la">2.20 ± 1.59 / 41.62 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">26.06 ± 2.35 / 30.05 ± 2.29</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="sv ner">23.05 ± 2.31 / 24.35 ± 1.99</td> <!-- SUC3 -->
   <td class="sv sent">12.47 ± 7.10 / 23.03 ± 8.78</td> <!-- SweReC -->
   <td class="sv la">0.08 ± 0.16 / 33.34 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.43 ± 2.69 / 24.25 ± 2.67</td> <!-- ScandiQA-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">3969</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.27</td> <!-- ScandEval rank -->
   <td class="sv ner">17.09 ± 2.33 / 18.78 ± 2.11</td> <!-- SUC3 -->
   <td class="sv sent">7.41 ± 9.32 / 28.42 ± 3.18</td> <!-- SweReC -->
   <td class="sv la">0.47 ± 1.48 / 38.19 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">11.73 ± 3.22 / 13.94 ± 3.48</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">4.79 ± 3.55 / 18.06 ± 2.80</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 8.92 ± 2.90</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.62 ± 12.67 / 35.36 ± 8.35</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 19.59 ± 6.84</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.40 ± 2.88 / 19.18 ± 3.18</td> <!-- ScandiQA-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="sv ner">19.15 ± 1.75 / 20.52 ± 1.77</td> <!-- SUC3 -->
   <td class="sv sent">-3.03 ± 7.40 / 24.39 ± 3.87</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.12 / 36.05 ± 2.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.18 ± 3.82 / 16.55 ± 4.25</td> <!-- ScandiQA-sv -->
   <td>13.1.0</td> <!-- SUC3 version -->
   <td>13.1.0</td> <!-- SweReC version -->
   <td>13.1.0</td> <!-- ScaLA-sv version -->
   <td>13.1.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">4.68</td> <!-- ScandEval rank -->
   <td class="sv ner">1.47 ± 1.90 / 1.32 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">5.50 ± 4.49 / 28.77 ± 3.76</td> <!-- SweReC -->
   <td class="sv la">-2.19 ± 1.29 / 40.52 ± 3.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.10 ± 0.06 / 4.36 ± 0.44</td> <!-- ScandiQA-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.76</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.78</td> <!-- ScandEval rank -->
   <td class="sv ner">0.26 ± 0.16 / 0.26 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">4.75 ± 2.54 / 27.85 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">-0.60 ± 1.56 / 40.53 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.06 ± 0.09 / 1.07 ± 0.35</td> <!-- ScandiQA-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/qa-icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">44,889 ± 6,944 / 13,506 ± 4,256</td> <!-- Model inference speed -->
   <td class="rank">4.85</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-0.10 ± 1.04 / 22.69 ± 0.52</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.02 ± 0.01</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">4.85</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.16 ± 0.14</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- ScandiQA-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">4.90</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-3.60 ± 3.63 / 20.29 ± 1.99</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- ScandiQA-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/swedish-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
