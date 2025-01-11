---
layout: leaderboard
title: Faroese NLU 🇫🇴
---

<center>Last updated: 11/01/2025 11:03:36 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="faroese-nlu" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">FoSent</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese reading comprehension - Exact Match / F1-score">FoQA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoNE">FoNE version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoSent">FoSent version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-fo">ScaLA-fo version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on FoQA">FoQA version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="fo ner">86.51 ± 2.01 / 85.01 ± 2.45</td> <!-- FoNE -->
   <td class="fo sent">38.22 ± 8.49 / 52.33 ± 6.78</td> <!-- FoSent -->
   <td class="fo la">35.09 ± 5.70 / 65.72 ± 3.27</td> <!-- ScaLA-fo -->
   <td class="fo rc">58.65 ± 3.25 / 81.93 ± 2.20</td> <!-- FoQA -->
   <td>12.5.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.5.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/FoBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,623 ± 2,828 / 3,737 ± 1,191</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="fo ner">91.31 ± 0.69 / 91.79 ± 0.47</td> <!-- FoNE -->
   <td class="fo sent">10.69 ± 5.70 / 26.65 ± 6.61</td> <!-- FoSent -->
   <td class="fo la">64.39 ± 1.55 / 81.38 ± 1.04</td> <!-- ScaLA-fo -->
   <td class="fo rc">27.09 ± 1.55 / 36.68 ± 1.88</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-405B-Instruct-FP8 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">405869</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">799 ± 246 / 112 ± 38</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="fo ner">81.95 ± 1.35 / 81.71 ± 1.81</td> <!-- FoNE -->
   <td class="fo sent">53.25 ± 1.76 / 50.18 ± 1.09</td> <!-- FoSent -->
   <td class="fo la">14.29 ± 2.45 / 40.76 ± 1.85</td> <!-- ScaLA-fo -->
   <td class="fo rc">60.41 ± 1.26 / 79.84 ± 0.96</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen2.5-72B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">72706</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,219 ± 412 / 158 ± 53</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="fo ner">76.56 ± 1.09 / 58.59 ± 3.63</td> <!-- FoNE -->
   <td class="fo sent">46.61 ± 1.58 / 47.25 ± 1.29</td> <!-- FoSent -->
   <td class="fo la">23.45 ± 2.41 / 59.84 ± 1.99</td> <!-- ScaLA-fo -->
   <td class="fo rc">55.28 ± 2.18 / 77.14 ± 1.37</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-70B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,409 ± 457 / 186 ± 63</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="fo ner">79.04 ± 1.57 / 69.20 ± 3.32</td> <!-- FoNE -->
   <td class="fo sent">52.33 ± 2.11 / 49.69 ± 1.21</td> <!-- FoSent -->
   <td class="fo la">15.72 ± 2.73 / 53.70 ± 3.15</td> <!-- ScaLA-fo -->
   <td class="fo rc">59.08 ± 1.71 / 79.21 ± 1.19</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="fo ner">81.30 ± 1.24 / 73.31 ± 3.51</td> <!-- FoNE -->
   <td class="fo sent">60.99 ± 2.59 / 72.95 ± 1.68</td> <!-- FoSent -->
   <td class="fo la">12.49 ± 3.30 / 49.82 ± 2.65</td> <!-- ScaLA-fo -->
   <td class="fo rc">48.47 ± 1.72 / 70.99 ± 1.42</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.3-70B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,353 ± 443 / 180 ± 61</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="fo ner">78.46 ± 1.42 / 66.11 ± 4.28</td> <!-- FoNE -->
   <td class="fo sent">51.60 ± 1.99 / 49.29 ± 1.20</td> <!-- FoSent -->
   <td class="fo la">17.25 ± 3.90 / 53.45 ± 4.72</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.98 ± 1.67 / 72.58 ± 1.07</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandi-1e4</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,074 ± 2,990 / 3,347 ± 1,080</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="fo ner">90.52 ± 0.47 / 90.83 ± 0.40</td> <!-- FoNE -->
   <td class="fo sent">11.53 ± 8.77 / 32.97 ± 9.54</td> <!-- FoSent -->
   <td class="fo la">44.99 ± 11.76 / 71.54 ± 5.83</td> <!-- ScaLA-fo -->
   <td class="fo rc">25.14 ± 1.72 / 34.64 ± 1.98</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">637 ± 306 / 92 ± 31</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="fo ner">68.00 ± 1.08 / 37.75 ± 1.09</td> <!-- FoNE -->
   <td class="fo sent">27.30 ± 4.69 / 30.12 ± 3.11</td> <!-- FoSent -->
   <td class="fo la">28.09 ± 3.31 / 54.91 ± 2.24</td> <!-- ScaLA-fo -->
   <td class="fo rc">58.59 ± 1.88 / 77.38 ± 1.63</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/c4ai-command-r-08-2024 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">32296</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,909 ± 646 / 248 ± 84</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="fo ner">73.26 ± 1.78 / 63.41 ± 3.03</td> <!-- FoNE -->
   <td class="fo sent">47.71 ± 2.52 / 64.44 ± 1.96</td> <!-- FoSent -->
   <td class="fo la">10.41 ± 2.22 / 54.04 ± 1.47</td> <!-- ScaLA-fo -->
   <td class="fo rc">57.08 ± 1.61 / 73.87 ± 1.31</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/QwQ-32B-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">32764</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,258 ± 1,221 / 198 ± 67</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="fo ner">77.19 ± 1.09 / 72.79 ± 2.09</td> <!-- FoNE -->
   <td class="fo sent">45.55 ± 2.05 / 46.59 ± 1.05</td> <!-- FoSent -->
   <td class="fo la">16.92 ± 1.77 / 55.66 ± 2.98</td> <!-- ScaLA-fo -->
   <td class="fo rc">47.51 ± 2.79 / 69.45 ± 2.43</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/Llama-3.1-Nemotron-70B-Instruct-HF (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,208 ± 412 / 156 ± 53</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="fo ner">64.88 ± 1.71 / 37.91 ± 1.50</td> <!-- FoNE -->
   <td class="fo sent">52.56 ± 2.14 / 49.94 ± 1.21</td> <!-- FoSent -->
   <td class="fo la">14.28 ± 1.04 / 45.93 ± 2.64</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.11 ± 1.82 / 74.50 ± 0.82</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,231 ± 8,171 / 4,863 ± 1,598</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="fo ner">88.81 ± 0.65 / 89.12 ± 0.56</td> <!-- FoNE -->
   <td class="fo sent">15.45 ± 3.96 / 40.77 ± 4.75</td> <!-- FoSent -->
   <td class="fo la">30.92 ± 8.65 / 63.05 ± 4.66</td> <!-- ScaLA-fo -->
   <td class="fo rc">25.48 ± 2.79 / 37.21 ± 3.83</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="fo ner">88.60 ± 0.60 / 89.37 ± 0.54</td> <!-- FoNE -->
   <td class="fo sent">6.70 ± 4.85 / 25.36 ± 7.25</td> <!-- FoSent -->
   <td class="fo la">46.81 ± 2.12 / 72.76 ± 1.40</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.96 ± 1.19 / 30.59 ± 1.61</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">908 ± 303 / 96 ± 36</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="fo ner">53.92 ± 1.55 / 28.59 ± 1.28</td> <!-- FoNE -->
   <td class="fo sent">35.05 ± 3.84 / 34.41 ± 2.93</td> <!-- FoSent -->
   <td class="fo la">23.12 ± 4.18 / 60.20 ± 2.01</td> <!-- ScaLA-fo -->
   <td class="fo rc">54.99 ± 2.45 / 76.60 ± 1.29</td> <!-- FoQA -->
   <td>14.0.1</td> <!-- FoNE version -->
   <td>14.0.1</td> <!-- FoSent version -->
   <td>14.0.1</td> <!-- ScaLA-fo version -->
   <td>14.0.1</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-sonnet-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">193 ± 87 / 55 ± 19</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="fo ner">72.52 ± 0.65 / 60.99 ± 0.78</td> <!-- FoNE -->
   <td class="fo sent">8.17 ± 5.22 / 27.16 ± 4.39</td> <!-- FoSent -->
   <td class="fo la">32.38 ± 4.28 / 56.38 ± 2.60</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.34 ± 1.90 / 69.24 ± 1.30</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 377 / 287 ± 97</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="fo ner">70.61 ± 1.12 / 68.27 ± 1.76</td> <!-- FoNE -->
   <td class="fo sent">45.78 ± 2.05 / 47.72 ± 1.15</td> <!-- FoSent -->
   <td class="fo la">4.58 ± 2.43 / 36.78 ± 1.86</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.67 ± 1.56 / 72.73 ± 1.11</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">470</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="fo ner">89.16 ± 0.66 / 89.62 ± 0.62</td> <!-- FoNE -->
   <td class="fo sent">21.57 ± 4.96 / 45.40 ± 4.23</td> <!-- FoSent -->
   <td class="fo la">22.76 ± 10.57 / 60.04 ± 5.76</td> <!-- ScaLA-fo -->
   <td class="fo rc">30.55 ± 1.05 / 41.85 ± 1.13</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">784 ± 310 / 95 ± 28</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="fo ner">73.80 ± 2.44 / 63.06 ± 3.84</td> <!-- FoNE -->
   <td class="fo sent">39.45 ± 8.53 / 62.38 ± 6.69</td> <!-- FoSent -->
   <td class="fo la">34.78 ± 4.81 / 63.14 ± 2.83</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.87 ± 1.17 / 19.37 ± 1.52</td> <!-- FoQA -->
   <td>14.0.0</td> <!-- FoNE version -->
   <td>14.0.0</td> <!-- FoSent version -->
   <td>14.0.0</td> <!-- ScaLA-fo version -->
   <td>14.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">436 ± 152 / 57 ± 21</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="fo ner">57.52 ± 2.17 / 36.36 ± 1.53</td> <!-- FoNE -->
   <td class="fo sent">13.18 ± 5.13 / 19.41 ± 3.41</td> <!-- FoSent -->
   <td class="fo la">28.03 ± 3.90 / 62.26 ± 2.03</td> <!-- ScaLA-fo -->
   <td class="fo rc">59.06 ± 2.40 / 76.65 ± 1.98</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.3</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,473 ± 377 / 283 ± 96</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="fo ner">67.67 ± 1.31 / 59.86 ± 2.12</td> <!-- FoNE -->
   <td class="fo sent">48.54 ± 2.43 / 49.17 ± 1.48</td> <!-- FoSent -->
   <td class="fo la">3.89 ± 2.71 / 36.33 ± 1.50</td> <!-- ScaLA-fo -->
   <td class="fo rc">47.07 ± 2.63 / 69.50 ± 1.68</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mixtral-8x7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46703</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,363 ± 794 / 311 ± 105</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="fo ner">67.97 ± 1.73 / 65.91 ± 2.05</td> <!-- FoNE -->
   <td class="fo sent">45.19 ± 3.93 / 59.61 ± 3.28</td> <!-- FoSent -->
   <td class="fo la">5.21 ± 3.44 / 47.34 ± 4.27</td> <!-- ScaLA-fo -->
   <td class="fo rc">43.26 ± 1.74 / 60.83 ± 1.76</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="fo ner">81.86 ± 2.08 / 67.98 ± 3.64</td> <!-- FoNE -->
   <td class="fo sent">27.30 ± 11.60 / 55.31 ± 9.21</td> <!-- FoSent -->
   <td class="fo la">-0.97 ± 2.82 / 33.64 ± 0.85</td> <!-- ScaLA-fo -->
   <td class="fo rc">56.45 ± 2.88 / 78.76 ± 1.86</td> <!-- FoQA -->
   <td>12.10.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.10.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/mistral-nemo-minitron-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8414</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,470 ± 836 / 326 ± 111</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="fo ner">66.18 ± 1.87 / 62.76 ± 2.46</td> <!-- FoNE -->
   <td class="fo sent">39.48 ± 3.86 / 56.83 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">5.78 ± 1.69 / 47.83 ± 3.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">44.81 ± 2.15 / 63.16 ± 2.38</td> <!-- FoQA -->
   <td>14.1.1</td> <!-- FoNE version -->
   <td>14.1.1</td> <!-- FoSent version -->
   <td>14.1.1</td> <!-- ScaLA-fo version -->
   <td>14.1.1</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>pere/roberta-base-exp-32</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,081 ± 2,950 / 3,365 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="fo ner">90.60 ± 0.45 / 90.78 ± 0.45</td> <!-- FoNE -->
   <td class="fo sent">11.28 ± 5.45 / 28.12 ± 6.89</td> <!-- FoSent -->
   <td class="fo la">22.86 ± 13.14 / 59.92 ± 6.74</td> <!-- ScaLA-fo -->
   <td class="fo rc">24.90 ± 1.52 / 33.83 ± 1.68</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mgoin/Nemotron-4-340B-Instruct-hf-FP8 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">341029</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,904 ± 475 / 361 ± 121</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="fo ner">55.31 ± 9.55 / 44.19 ± 6.59</td> <!-- FoNE -->
   <td class="fo sent">51.62 ± 10.21 / 62.71 ± 10.54</td> <!-- FoSent -->
   <td class="fo la">15.07 ± 1.77 / 54.46 ± 2.11</td> <!-- ScaLA-fo -->
   <td class="fo rc">18.22 ± 3.26 / 36.19 ± 4.86</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/ScandiBERT-no-faroese</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,436 ± 2,820 / 3,704 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="fo ner">88.14 ± 0.58 / 88.89 ± 0.52</td> <!-- FoNE -->
   <td class="fo sent">6.88 ± 5.56 / 24.40 ± 8.37</td> <!-- FoSent -->
   <td class="fo la">27.71 ± 9.67 / 61.60 ± 5.69</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.47 ± 2.44 / 29.37 ± 3.28</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mixtral-8x7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46703</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,535 ± 1,837 / 760 ± 256</td> <!-- Model inference speed -->
   <td class="rank">3.29</td> <!-- ScandEval rank -->
   <td class="fo ner">63.43 ± 0.93 / 41.57 ± 2.20</td> <!-- FoNE -->
   <td class="fo sent">43.99 ± 2.94 / 59.58 ± 2.00</td> <!-- FoSent -->
   <td class="fo la">9.38 ± 2.05 / 51.75 ± 1.36</td> <!-- ScaLA-fo -->
   <td class="fo rc">25.35 ± 3.98 / 49.54 ± 4.57</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/c4ai-command-r-v01 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">34981</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,919 ± 645 / 248 ± 83</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="fo ner">64.53 ± 1.51 / 50.53 ± 3.29</td> <!-- FoNE -->
   <td class="fo sent">44.01 ± 1.86 / 55.97 ± 2.61</td> <!-- FoSent -->
   <td class="fo la">2.39 ± 1.56 / 38.90 ± 2.09</td> <!-- ScaLA-fo -->
   <td class="fo rc">34.84 ± 3.88 / 58.25 ± 3.25</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mixtral-8x7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46998</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,015 ± 2,966 / 1,121 ± 510</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="fo ner">58.62 ± 3.34 / 53.80 ± 3.15</td> <!-- FoNE -->
   <td class="fo sent">40.74 ± 5.37 / 57.33 ± 4.26</td> <!-- FoSent -->
   <td class="fo la">5.58 ± 2.68 / 45.68 ± 4.79</td> <!-- ScaLA-fo -->
   <td class="fo rc">28.04 ± 7.49 / 52.48 ± 5.80</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-xlmr-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,004 ± 2,244 / 2,324 ± 761</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="fo ner">87.79 ± 0.40 / 88.46 ± 0.31</td> <!-- FoNE -->
   <td class="fo sent">7.80 ± 5.19 / 24.52 ± 6.96</td> <!-- FoSent -->
   <td class="fo la">22.51 ± 10.65 / 55.58 ± 8.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">11.16 ± 3.59 / 16.82 ± 5.50</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="fo ner">87.35 ± 0.94 / 87.65 ± 0.94</td> <!-- FoNE -->
   <td class="fo sent">0.04 ± 3.09 / 17.28 ± 2.02</td> <!-- FoSent -->
   <td class="fo la">14.65 ± 11.12 / 46.36 ± 10.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">36.10 ± 1.91 / 48.41 ± 2.09</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="fo ner">88.64 ± 0.34 / 89.11 ± 0.29</td> <!-- FoNE -->
   <td class="fo sent">23.63 ± 6.26 / 44.37 ± 7.53</td> <!-- FoSent -->
   <td class="fo la">2.05 ± 2.30 / 47.88 ± 2.17</td> <!-- ScaLA-fo -->
   <td class="fo rc">24.09 ± 4.66 / 37.60 ± 4.39</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,302 ± 323 / 253 ± 86</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="fo ner">65.55 ± 1.39 / 51.57 ± 3.35</td> <!-- FoNE -->
   <td class="fo sent">29.49 ± 2.40 / 47.06 ± 2.82</td> <!-- FoSent -->
   <td class="fo la">2.05 ± 1.58 / 35.92 ± 2.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">47.72 ± 2.10 / 65.78 ± 1.43</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mixtral-8x7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46998</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,368 ± 793 / 317 ± 108</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="fo ner">62.60 ± 3.09 / 54.91 ± 2.40</td> <!-- FoNE -->
   <td class="fo sent">31.36 ± 5.40 / 50.13 ± 5.67</td> <!-- FoSent -->
   <td class="fo la">5.21 ± 3.15 / 46.32 ± 4.42</td> <!-- ScaLA-fo -->
   <td class="fo rc">34.26 ± 2.20 / 51.27 ± 2.30</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>jonfd/electra-small-nordic</td> <!-- Model ID -->
   <td class="num_model_parameters">22</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">96</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,989 ± 120 / 3,809 ± 1,230</td> <!-- Model inference speed -->
   <td class="rank">3.52</td> <!-- ScandEval rank -->
   <td class="fo ner">85.80 ± 0.25 / 86.58 ± 0.26</td> <!-- FoNE -->
   <td class="fo sent">-0.16 ± 3.99 / 22.65 ± 3.79</td> <!-- FoSent -->
   <td class="fo la">30.88 ± 2.36 / 63.79 ± 1.33</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">3.53</td> <!-- ScandEval rank -->
   <td class="fo ner">88.39 ± 0.86 / 88.75 ± 0.75</td> <!-- FoNE -->
   <td class="fo sent">18.28 ± 3.38 / 39.08 ± 2.62</td> <!-- FoSent -->
   <td class="fo la">2.85 ± 1.32 / 48.43 ± 2.29</td> <!-- ScaLA-fo -->
   <td class="fo rc">31.03 ± 1.94 / 43.72 ± 2.89</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,686 ± 685 / 491 ± 164</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="fo ner">64.72 ± 1.73 / 47.25 ± 4.90</td> <!-- FoNE -->
   <td class="fo sent">28.57 ± 4.08 / 50.22 ± 2.92</td> <!-- FoSent -->
   <td class="fo la">5.12 ± 1.16 / 51.09 ± 0.89</td> <!-- ScaLA-fo -->
   <td class="fo rc">38.83 ± 3.81 / 56.89 ± 3.51</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,986 ± 823 / 276 ± 94</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="fo ner">65.65 ± 3.31 / 63.81 ± 2.72</td> <!-- FoNE -->
   <td class="fo sent">24.30 ± 7.03 / 35.85 ± 7.35</td> <!-- FoSent -->
   <td class="fo la">0.61 ± 1.75 / 35.51 ± 2.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.01 ± 1.79 / 65.74 ± 1.54</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,446 ± 354 / 295 ± 100</td> <!-- Model inference speed -->
   <td class="rank">3.55</td> <!-- ScandEval rank -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo sent">25.57 ± 6.07 / 44.34 ± 6.18</td> <!-- FoSent -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td class="fo rc">44.06 ± 1.93 / 60.40 ± 2.37</td> <!-- FoQA -->
   <td>9.1.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>9.1.2</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="fo ner">58.24 ± 3.73 / 47.44 ± 4.83</td> <!-- FoNE -->
   <td class="fo sent">32.79 ± 2.01 / 41.82 ± 1.09</td> <!-- FoSent -->
   <td class="fo la">1.77 ± 2.13 / 45.44 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.13 ± 1.12 / 64.71 ± 0.74</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,364 ± 343 / 266 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="fo ner">61.32 ± 4.26 / 59.28 ± 4.43</td> <!-- FoNE -->
   <td class="fo sent">26.73 ± 4.70 / 45.03 ± 5.25</td> <!-- FoSent -->
   <td class="fo la">1.30 ± 1.64 / 45.10 ± 3.27</td> <!-- ScaLA-fo -->
   <td class="fo rc">44.98 ± 1.62 / 62.38 ± 1.68</td> <!-- FoQA -->
   <td>12.10.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.10.4</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,419 ± 349 / 286 ± 97</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="fo ner">63.40 ± 2.78 / 59.96 ± 2.91</td> <!-- FoNE -->
   <td class="fo sent">26.90 ± 4.62 / 39.87 ± 5.82</td> <!-- FoSent -->
   <td class="fo la">2.16 ± 2.25 / 39.38 ± 4.12</td> <!-- ScaLA-fo -->
   <td class="fo rc">40.73 ± 1.32 / 57.50 ± 1.39</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,370 ± 416 / 711 ± 242</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo sent">32.07 ± 3.55 / 51.69 ± 3.46</td> <!-- FoSent -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.00 ± 1.21 / 59.78 ± 1.14</td> <!-- FoQA -->
   <td>9.2.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">3.59</td> <!-- ScandEval rank -->
   <td class="fo ner">54.79 ± 2.33 / 46.30 ± 4.57</td> <!-- FoNE -->
   <td class="fo sent">35.84 ± 8.64 / 48.22 ± 7.58</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.54</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.94 ± 2.59 / 62.06 ± 2.17</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 625 / 476 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="fo ner">61.47 ± 1.57 / 58.60 ± 2.31</td> <!-- FoNE -->
   <td class="fo sent">24.35 ± 6.38 / 30.32 ± 5.04</td> <!-- FoSent -->
   <td class="fo la">1.44 ± 1.85 / 34.71 ± 1.84</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.54 ± 1.49 / 58.90 ± 1.24</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,477 ± 376 / 285 ± 97</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="fo ner">61.11 ± 4.21 / 58.55 ± 4.19</td> <!-- FoNE -->
   <td class="fo sent">19.40 ± 8.13 / 32.14 ± 7.75</td> <!-- FoSent -->
   <td class="fo la">2.02 ± 1.68 / 39.88 ± 3.56</td> <!-- ScaLA-fo -->
   <td class="fo rc">50.34 ± 1.74 / 71.74 ± 1.27</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">151</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,908 ± 3,201 / 2,700 ± 872</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="fo ner">86.09 ± 1.03 / 86.85 ± 1.02</td> <!-- FoNE -->
   <td class="fo sent">5.17 ± 4.32 / 26.72 ± 6.11</td> <!-- FoSent -->
   <td class="fo la">15.24 ± 6.84 / 50.54 ± 4.85</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.82 ± 1.50 / 22.99 ± 1.63</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-sbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,757 ± 3,883 / 3,864 ± 1,237</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="fo ner">86.20 ± 0.50 / 86.91 ± 0.46</td> <!-- FoNE -->
   <td class="fo sent">19.12 ± 2.94 / 41.88 ± 2.47</td> <!-- FoSent -->
   <td class="fo la">11.80 ± 7.52 / 53.06 ± 5.04</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.47 ± 1.01 / 11.22 ± 1.50</td> <!-- FoQA -->
   <td>12.10.5</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.10.5</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="fo ner">59.96 ± 2.42 / 58.61 ± 2.57</td> <!-- FoNE -->
   <td class="fo sent">28.33 ± 7.70 / 49.72 ± 6.84</td> <!-- FoSent -->
   <td class="fo la">2.24 ± 1.78 / 41.32 ± 3.70</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.52 ± 1.83 / 57.16 ± 2.10</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="fo ner">88.24 ± 0.58 / 88.48 ± 0.54</td> <!-- FoNE -->
   <td class="fo sent">6.42 ± 5.53 / 24.34 ± 7.55</td> <!-- FoSent -->
   <td class="fo la">1.73 ± 1.70 / 42.32 ± 5.16</td> <!-- ScaLA-fo -->
   <td class="fo rc">35.08 ± 2.58 / 47.03 ± 3.42</td> <!-- FoQA -->
   <td>10.0.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>10.0.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,405 ± 1,970 / 2,856 ± 917</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="fo ner">86.94 ± 0.47 / 87.58 ± 0.46</td> <!-- FoNE -->
   <td class="fo sent">1.08 ± 4.61 / 24.02 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">12.35 ± 8.96 / 53.00 ± 5.17</td> <!-- ScaLA-fo -->
   <td class="fo rc">24.57 ± 2.18 / 34.06 ± 2.82</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,151 ± 294 / 227 ± 76</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="fo ner">61.81 ± 2.69 / 59.37 ± 2.94</td> <!-- FoNE -->
   <td class="fo sent">24.67 ± 6.35 / 43.87 ± 6.36</td> <!-- FoSent -->
   <td class="fo la">1.32 ± 1.90 / 40.36 ± 4.18</td> <!-- ScaLA-fo -->
   <td class="fo rc">35.62 ± 1.71 / 51.48 ± 2.47</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/mistral-nemo-minitron-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8414</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,161 ± 676 / 1,247 ± 481</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="fo ner">67.72 ± 1.04 / 51.81 ± 3.32</td> <!-- FoNE -->
   <td class="fo sent">42.98 ± 3.22 / 60.44 ± 2.81</td> <!-- FoSent -->
   <td class="fo la">6.40 ± 1.61 / 51.02 ± 1.86</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.07 ± 0.10 / 29.23 ± 1.59</td> <!-- FoQA -->
   <td>14.1.1</td> <!-- FoNE version -->
   <td>14.1.1</td> <!-- FoSent version -->
   <td>14.1.1</td> <!-- ScaLA-fo version -->
   <td>14.1.1</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="fo ner">87.44 ± 0.35 / 88.01 ± 0.28</td> <!-- FoNE -->
   <td class="fo sent">10.97 ± 3.84 / 30.74 ± 5.68</td> <!-- FoSent -->
   <td class="fo la">7.38 ± 6.28 / 47.69 ± 4.51</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.80 ± 3.56 / 22.12 ± 5.23</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-large</td> <!-- Model ID -->
   <td class="num_model_parameters">406</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,677 ± 719 / 1,886 ± 604</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="fo ner">86.84 ± 0.77 / 87.51 ± 0.72</td> <!-- FoNE -->
   <td class="fo sent">2.92 ± 3.57 / 25.10 ± 5.74</td> <!-- FoSent -->
   <td class="fo la">9.82 ± 3.95 / 50.49 ± 3.45</td> <!-- ScaLA-fo -->
   <td class="fo rc">21.19 ± 2.49 / 30.11 ± 2.76</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-70B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,220 ± 411 / 158 ± 53</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="fo ner">65.06 ± 2.04 / 64.49 ± 1.85</td> <!-- FoNE -->
   <td class="fo sent">48.44 ± 4.16 / 54.28 ± 3.55</td> <!-- FoSent -->
   <td class="fo la">3.30 ± 1.95 / 34.38 ± 1.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 20.32 ± 0.61</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="fo ner">66.82 ± 2.36 / 65.84 ± 2.35</td> <!-- FoNE -->
   <td class="fo sent">21.19 ± 5.19 / 32.96 ± 5.05</td> <!-- FoSent -->
   <td class="fo la">-0.36 ± 1.67 / 37.57 ± 3.35</td> <!-- ScaLA-fo -->
   <td class="fo rc">36.47 ± 0.96 / 51.89 ± 1.05</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-ic3</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,119 ± 1,576 / 3,812 ± 1,242</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="fo ner">87.22 ± 0.68 / 87.92 ± 0.59</td> <!-- FoNE -->
   <td class="fo sent">15.94 ± 5.79 / 37.27 ± 7.66</td> <!-- FoSent -->
   <td class="fo la">6.23 ± 6.96 / 48.55 ± 4.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.98 ± 1.75 / 4.35 ± 2.54</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,697 ± 2,113 / 5,432 ± 1,749</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="fo ner">86.50 ± 0.96 / 87.11 ± 0.90</td> <!-- FoNE -->
   <td class="fo sent">8.64 ± 5.25 / 29.80 ± 8.39</td> <!-- FoSent -->
   <td class="fo la">10.13 ± 8.55 / 47.31 ± 7.04</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.35 ± 3.50 / 8.28 ± 5.36</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/XLMR-ENIS</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,711 ± 2,333 / 2,141 ± 689</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="fo ner">87.09 ± 0.76 / 87.71 ± 0.73</td> <!-- FoNE -->
   <td class="fo sent">15.11 ± 7.40 / 38.19 ± 7.66</td> <!-- FoSent -->
   <td class="fo la">3.09 ± 1.98 / 39.41 ± 4.45</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.75 ± 2.66 / 8.73 ± 4.07</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">559</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="fo ner">87.85 ± 0.95 / 88.21 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">5.14 ± 5.42 / 22.03 ± 5.69</td> <!-- FoSent -->
   <td class="fo la">1.17 ± 2.11 / 40.94 ± 5.07</td> <!-- ScaLA-fo -->
   <td class="fo rc">27.72 ± 1.48 / 39.88 ± 2.04</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="fo ner">84.14 ± 0.67 / 84.82 ± 0.64</td> <!-- FoNE -->
   <td class="fo sent">21.20 ± 3.85 / 43.97 ± 3.72</td> <!-- FoSent -->
   <td class="fo la">1.33 ± 2.18 / 48.85 ± 1.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.20 ± 1.78 / 22.95 ± 2.71</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,707 ± 688 / 497 ± 166</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="fo ner">62.22 ± 2.10 / 58.79 ± 2.20</td> <!-- FoNE -->
   <td class="fo sent">17.34 ± 5.56 / 37.16 ± 5.28</td> <!-- FoSent -->
   <td class="fo la">0.01 ± 2.43 / 37.74 ± 4.20</td> <!-- ScaLA-fo -->
   <td class="fo rc">38.70 ± 1.22 / 54.70 ± 0.93</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,136 ± 1,282 / 668 ± 326</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="fo ner">62.20 ± 1.42 / 45.92 ± 2.03</td> <!-- FoNE -->
   <td class="fo sent">26.68 ± 6.93 / 47.94 ± 8.20</td> <!-- FoSent -->
   <td class="fo la">7.07 ± 2.30 / 44.94 ± 2.71</td> <!-- ScaLA-fo -->
   <td class="fo rc">11.97 ± 3.61 / 31.80 ± 3.65</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KennethEnevoldsen/dfm-sentence-encoder-medium</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,998 ± 2,549 / 3,833 ± 1,223</td> <!-- Model inference speed -->
   <td class="rank">3.87</td> <!-- ScandEval rank -->
   <td class="fo ner">84.92 ± 0.70 / 85.65 ± 0.67</td> <!-- FoNE -->
   <td class="fo sent">10.17 ± 4.54 / 30.26 ± 5.80</td> <!-- FoSent -->
   <td class="fo la">2.96 ± 2.66 / 45.42 ± 4.03</td> <!-- ScaLA-fo -->
   <td class="fo rc">14.00 ± 2.44 / 20.08 ± 3.54</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="fo ner">60.37 ± 3.60 / 59.38 ± 3.85</td> <!-- FoNE -->
   <td class="fo sent">8.21 ± 5.06 / 27.79 ± 5.76</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">43.69 ± 2.03 / 60.55 ± 1.76</td> <!-- FoQA -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,051 ± 3,289 / 2,704 ± 897</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="fo ner">86.10 ± 0.64 / 86.75 ± 0.57</td> <!-- FoNE -->
   <td class="fo sent">4.80 ± 5.07 / 21.63 ± 2.01</td> <!-- FoSent -->
   <td class="fo la">6.28 ± 2.41 / 49.62 ± 2.08</td> <!-- ScaLA-fo -->
   <td class="fo rc">9.89 ± 2.08 / 14.41 ± 3.08</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="fo ner">60.46 ± 2.53 / 58.29 ± 2.53</td> <!-- FoNE -->
   <td class="fo sent">21.59 ± 6.94 / 40.68 ± 5.50</td> <!-- FoSent -->
   <td class="fo la">0.51 ± 0.78 / 36.20 ± 2.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">33.54 ± 1.00 / 49.02 ± 0.91</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="fo ner">85.86 ± 0.51 / 86.55 ± 0.49</td> <!-- FoNE -->
   <td class="fo sent">16.49 ± 2.83 / 34.48 ± 3.01</td> <!-- FoSent -->
   <td class="fo la">0.80 ± 2.32 / 42.37 ± 4.42</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.17 ± 2.62 / 2.93 ± 3.66</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo sent">15.85 ± 6.84 / 36.28 ± 7.13</td> <!-- FoSent -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">33.54 ± 1.29 / 50.80 ± 1.31</td> <!-- FoQA -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-125k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,763 ± 2,523 / 4,238 ± 1,370</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="fo ner">80.61 ± 0.91 / 81.31 ± 0.89</td> <!-- FoNE -->
   <td class="fo sent">2.87 ± 3.48 / 19.80 ± 4.75</td> <!-- FoSent -->
   <td class="fo la">9.60 ± 3.82 / 52.30 ± 1.73</td> <!-- ScaLA-fo -->
   <td class="fo rc">11.57 ± 0.86 / 17.37 ± 1.12</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="fo ner">58.67 ± 3.95 / 58.47 ± 3.96</td> <!-- FoNE -->
   <td class="fo sent">10.39 ± 7.55 / 30.73 ± 6.92</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">40.95 ± 1.80 / 55.82 ± 1.95</td> <!-- FoQA -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.1.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Nordics/bert-large-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">334</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,199 ± 1,139 / 2,051 ± 651</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="fo ner">83.22 ± 0.71 / 83.91 ± 0.66</td> <!-- FoNE -->
   <td class="fo sent">2.93 ± 3.78 / 22.30 ± 4.06</td> <!-- FoSent -->
   <td class="fo la">6.78 ± 3.31 / 51.53 ± 2.36</td> <!-- ScaLA-fo -->
   <td class="fo rc">15.94 ± 1.67 / 22.00 ± 2.12</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-165k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,138 ± 1,111 / 2,067 ± 660</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="fo ner">82.76 ± 0.95 / 83.43 ± 0.88</td> <!-- FoNE -->
   <td class="fo sent">1.22 ± 4.49 / 25.53 ± 4.87</td> <!-- FoSent -->
   <td class="fo la">7.58 ± 3.56 / 52.05 ± 1.14</td> <!-- ScaLA-fo -->
   <td class="fo rc">16.13 ± 1.68 / 23.78 ± 2.02</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="fo ner">53.38 ± 3.96 / 53.04 ± 3.85</td> <!-- FoNE -->
   <td class="fo sent">21.11 ± 6.06 / 41.25 ± 6.85</td> <!-- FoSent -->
   <td class="fo la">0.46 ± 2.01 / 44.83 ± 3.28</td> <!-- ScaLA-fo -->
   <td class="fo rc">35.99 ± 1.01 / 51.25 ± 1.12</td> <!-- FoQA -->
   <td>12.5.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.3.2</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/IceBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,360 ± 1,611 / 3,858 ± 1,246</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="fo ner">87.13 ± 0.58 / 87.70 ± 0.45</td> <!-- FoNE -->
   <td class="fo sent">8.64 ± 5.25 / 29.80 ± 8.39</td> <!-- FoSent -->
   <td class="fo la">3.66 ± 3.33 / 40.81 ± 4.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.07 ± 3.59 / 8.05 ± 5.61</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">3.98</td> <!-- ScandEval rank -->
   <td class="fo ner">58.96 ± 2.05 / 52.20 ± 2.50</td> <!-- FoNE -->
   <td class="fo sent">8.97 ± 6.97 / 27.85 ± 5.18</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">39.20 ± 1.10 / 54.89 ± 1.25</td> <!-- FoQA -->
   <td>12.5.3</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>12.5.3</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-igc</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,551 ± 1,656 / 3,918 ± 1,274</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="fo ner">83.82 ± 0.98 / 84.34 ± 0.88</td> <!-- FoNE -->
   <td class="fo sent">12.12 ± 5.60 / 32.60 ± 6.48</td> <!-- FoSent -->
   <td class="fo la">4.93 ± 3.16 / 45.85 ± 3.66</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.17 ± 2.95 / 7.88 ± 4.65</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>mideind/IceBERT-mC4-is</td> <!-- Model ID -->
   <td class="num_model_parameters">163</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,308 ± 1,614 / 3,851 ± 1,254</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="fo ner">88.44 ± 0.35 / 89.11 ± 0.38</td> <!-- FoNE -->
   <td class="fo sent">1.73 ± 3.39 / 17.03 ± 2.53</td> <!-- FoSent -->
   <td class="fo la">11.83 ± 4.90 / 48.95 ± 6.81</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">103</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">23</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,432 ± 2,838 / 3,642 ± 1,189</td> <!-- Model inference speed -->
   <td class="rank">4.00</td> <!-- ScandEval rank -->
   <td class="fo ner">86.62 ± 0.43 / 87.31 ± 0.44</td> <!-- FoNE -->
   <td class="fo sent">2.99 ± 2.41 / 22.15 ± 2.57</td> <!-- FoSent -->
   <td class="fo la">3.64 ± 3.82 / 49.77 ± 2.26</td> <!-- ScaLA-fo -->
   <td class="fo rc">13.84 ± 1.99 / 21.44 ± 2.62</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">4.00</td> <!-- ScandEval rank -->
   <td class="fo ner">82.97 ± 0.83 / 83.62 ± 0.81</td> <!-- FoNE -->
   <td class="fo sent">18.07 ± 4.85 / 39.76 ± 3.32</td> <!-- FoSent -->
   <td class="fo la">2.93 ± 1.96 / 46.51 ± 4.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-base-swedish-cased-600k</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,726 ± 2,508 / 4,234 ± 1,365</td> <!-- Model inference speed -->
   <td class="rank">4.02</td> <!-- ScandEval rank -->
   <td class="fo ner">81.02 ± 0.75 / 81.74 ± 0.75</td> <!-- FoNE -->
   <td class="fo sent">7.39 ± 3.22 / 27.62 ± 2.64</td> <!-- FoSent -->
   <td class="fo la">4.00 ± 2.04 / 50.51 ± 1.11</td> <!-- ScaLA-fo -->
   <td class="fo rc">12.98 ± 1.18 / 20.39 ± 1.75</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo sent">13.24 ± 5.37 / 38.49 ± 4.97</td> <!-- FoSent -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td class="fo rc">31.87 ± 2.20 / 46.21 ± 1.15</td> <!-- FoQA -->
   <td>9.3.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>9.3.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased-new</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,933 ± 2,541 / 4,289 ± 1,376</td> <!-- Model inference speed -->
   <td class="rank">4.05</td> <!-- ScandEval rank -->
   <td class="fo ner">84.02 ± 0.86 / 84.66 ± 0.82</td> <!-- FoNE -->
   <td class="fo sent">0.92 ± 4.36 / 23.25 ± 4.15</td> <!-- FoSent -->
   <td class="fo la">5.65 ± 3.07 / 49.17 ± 3.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.14 ± 2.31 / 10.87 ± 3.52</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/megatron-bert-large-swedish-cased-110k</td> <!-- Model ID -->
   <td class="num_model_parameters">369</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,075 ± 1,093 / 2,057 ± 661</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="fo ner">82.36 ± 0.91 / 82.94 ± 0.90</td> <!-- FoNE -->
   <td class="fo sent">6.99 ± 2.15 / 31.03 ± 3.17</td> <!-- FoSent -->
   <td class="fo la">5.20 ± 2.67 / 50.88 ± 1.55</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.65 ± 1.46 / 4.33 ± 2.24</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="fo ner">40.18 ± 3.60 / 39.95 ± 3.38</td> <!-- FoNE -->
   <td class="fo sent">14.19 ± 8.12 / 28.15 ± 8.15</td> <!-- FoSent -->
   <td class="fo la">0.31 ± 1.71 / 41.35 ± 4.05</td> <!-- ScaLA-fo -->
   <td class="fo rc">41.60 ± 2.49 / 60.78 ± 2.12</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="fo ner">67.42 ± 2.21 / 60.87 ± 3.22</td> <!-- FoNE -->
   <td class="fo sent">20.01 ± 4.67 / 38.23 ± 3.04</td> <!-- FoSent -->
   <td class="fo la">7.02 ± 1.56 / 49.32 ± 2.91</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.65 ± 0.17 / 7.03 ± 0.26</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,227 ± 2,650 / 4,252 ± 1,393</td> <!-- Model inference speed -->
   <td class="rank">4.10</td> <!-- ScandEval rank -->
   <td class="fo ner">82.64 ± 0.63 / 83.27 ± 0.65</td> <!-- FoNE -->
   <td class="fo sent">5.78 ± 2.10 / 24.21 ± 4.42</td> <!-- FoSent -->
   <td class="fo la">8.03 ± 2.01 / 51.96 ± 1.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">9.77 ± 3.39 / 32.64 ± 2.55</td> <!-- FoSent -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">4.13</td> <!-- ScandEval rank -->
   <td class="fo ner">82.91 ± 0.89 / 83.43 ± 0.87</td> <!-- FoNE -->
   <td class="fo sent">9.77 ± 3.39 / 32.64 ± 2.55</td> <!-- FoSent -->
   <td class="fo la">1.67 ± 2.22 / 46.20 ± 3.31</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">167</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">4.14</td> <!-- ScandEval rank -->
   <td class="fo ner">73.06 ± 1.51 / 72.61 ± 1.40</td> <!-- FoNE -->
   <td class="fo sent">2.33 ± 1.48 / 20.95 ± 2.83</td> <!-- FoSent -->
   <td class="fo la">5.48 ± 2.42 / 49.18 ± 3.63</td> <!-- ScaLA-fo -->
   <td class="fo rc">11.29 ± 2.19 / 18.32 ± 2.98</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="fo ner">75.63 ± 1.41 / 76.23 ± 1.36</td> <!-- FoNE -->
   <td class="fo sent">9.82 ± 2.60 / 36.40 ± 2.64</td> <!-- FoSent -->
   <td class="fo la">3.65 ± 1.93 / 48.34 ± 1.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="fo ner">77.00 ± 1.08 / 77.85 ± 1.05</td> <!-- FoNE -->
   <td class="fo sent">9.59 ± 3.69 / 32.95 ± 3.64</td> <!-- FoSent -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="fo ner">77.16 ± 0.93 / 78.00 ± 0.91</td> <!-- FoNE -->
   <td class="fo sent">10.41 ± 3.80 / 34.36 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">4.09 ± 2.27 / 47.26 ± 3.09</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="fo ner">80.92 ± 0.59 / 81.63 ± 0.56</td> <!-- FoNE -->
   <td class="fo sent">12.97 ± 2.96 / 31.99 ± 2.53</td> <!-- FoSent -->
   <td class="fo la">1.19 ± 2.37 / 43.13 ± 4.70</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">69</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,597 ± 6,036 / 5,271 ± 1,697</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="fo ner">82.05 ± 0.46 / 82.67 ± 0.43</td> <!-- FoNE -->
   <td class="fo sent">4.40 ± 3.12 / 25.01 ± 4.58</td> <!-- FoSent -->
   <td class="fo la">3.98 ± 2.94 / 50.53 ± 1.83</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.97 ± 1.01 / 1.92 ± 1.82</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>patrickvonplaten/norwegian-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,698 ± 2,699 / 3,891 ± 1,278</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="fo ner">82.57 ± 0.93 / 83.35 ± 0.91</td> <!-- FoNE -->
   <td class="fo sent">1.68 ± 4.03 / 18.08 ± 3.73</td> <!-- FoSent -->
   <td class="fo la">5.74 ± 3.53 / 48.75 ± 3.22</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-haiku-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">277 ± 77 / 70 ± 25</td> <!-- Model inference speed -->
   <td class="rank">4.18</td> <!-- ScandEval rank -->
   <td class="fo ner">51.06 ± 1.45 / 30.27 ± 1.00</td> <!-- FoNE -->
   <td class="fo sent">-3.58 ± 4.03 / 14.94 ± 2.38</td> <!-- FoSent -->
   <td class="fo la">4.10 ± 4.03 / 37.28 ± 1.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">45.29 ± 1.54 / 72.97 ± 1.19</td> <!-- FoQA -->
   <td>14.0.3</td> <!-- FoNE version -->
   <td>14.0.2</td> <!-- FoSent version -->
   <td>14.0.3</td> <!-- ScaLA-fo version -->
   <td>14.0.3</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="fo ner">83.21 ± 0.53 / 83.81 ± 0.45</td> <!-- FoNE -->
   <td class="fo sent">3.90 ± 4.05 / 25.25 ± 5.25</td> <!-- FoSent -->
   <td class="fo la">2.37 ± 4.63 / 48.46 ± 3.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">1.35 ± 1.03 / 2.54 ± 1.88</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,437 ± 2,628 / 3,834 ± 1,252</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="fo ner">80.52 ± 0.76 / 81.35 ± 0.69</td> <!-- FoNE -->
   <td class="fo sent">2.89 ± 3.05 / 27.56 ± 2.96</td> <!-- FoSent -->
   <td class="fo la">6.51 ± 3.60 / 51.81 ± 1.95</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="fo ner">81.70 ± 0.58 / 82.18 ± 0.53</td> <!-- FoNE -->
   <td class="fo sent">12.82 ± 3.51 / 33.99 ± 2.71</td> <!-- FoSent -->
   <td class="fo la">0.25 ± 2.87 / 44.81 ± 2.90</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>vesteinn/DanskBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,749 ± 2,665 / 4,014 ± 1,281</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="fo ner">85.04 ± 0.57 / 85.72 ± 0.50</td> <!-- FoNE -->
   <td class="fo sent">2.02 ± 4.21 / 21.25 ± 5.15</td> <!-- FoSent -->
   <td class="fo la">4.48 ± 1.63 / 44.45 ± 4.77</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.15 ± 0.29 / 0.21 ± 0.39</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-danish</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,004 ± 2,964 / 3,290 ± 1,092</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="fo ner">80.21 ± 0.95 / 80.80 ± 0.97</td> <!-- FoNE -->
   <td class="fo sent">2.88 ± 4.40 / 23.61 ± 4.78</td> <!-- FoSent -->
   <td class="fo la">1.10 ± 2.44 / 48.16 ± 1.47</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.95 ± 1.36 / 11.84 ± 1.76</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="fo ner">83.96 ± 0.80 / 84.63 ± 0.76</td> <!-- FoNE -->
   <td class="fo sent">5.16 ± 3.25 / 23.12 ± 4.48</td> <!-- FoSent -->
   <td class="fo la">1.05 ± 1.66 / 41.31 ± 4.91</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>DeepPavlov/rubert-base-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,785 ± 2,658 / 3,983 ± 1,289</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="fo ner">83.15 ± 0.73 / 83.90 ± 0.74</td> <!-- FoNE -->
   <td class="fo sent">0.56 ± 4.44 / 29.23 ± 3.77</td> <!-- FoSent -->
   <td class="fo la">3.21 ± 2.89 / 47.97 ± 3.56</td> <!-- ScaLA-fo -->
   <td class="fo rc">1.53 ± 1.23 / 2.95 ± 2.23</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,181 ± 2,451 / 4,620 ± 1,507</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="fo ner">82.76 ± 1.26 / 83.50 ± 1.20</td> <!-- FoNE -->
   <td class="fo sent">3.46 ± 2.02 / 20.63 ± 3.68</td> <!-- FoSent -->
   <td class="fo la">3.98 ± 2.70 / 47.46 ± 2.35</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.01 ± 0.02</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="fo ner">84.73 ± 1.49 / 85.19 ± 1.59</td> <!-- FoNE -->
   <td class="fo sent">-0.64 ± 3.87 / 22.47 ± 3.96</td> <!-- FoSent -->
   <td class="fo la">1.37 ± 2.46 / 39.78 ± 3.24</td> <!-- ScaLA-fo -->
   <td class="fo rc">4.15 ± 4.39 / 5.74 ± 6.06</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="fo ner">46.64 ± 1.91 / 35.58 ± 2.47</td> <!-- FoNE -->
   <td class="fo sent">16.72 ± 4.87 / 41.68 ± 4.39</td> <!-- FoSent -->
   <td class="fo la">-1.54 ± 2.60 / 36.21 ± 2.51</td> <!-- ScaLA-fo -->
   <td class="fo rc">18.69 ± 5.12 / 38.94 ± 4.72</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="fo ner">82.24 ± 0.85 / 82.84 ± 0.78</td> <!-- FoNE -->
   <td class="fo sent">6.35 ± 5.07 / 29.58 ± 4.89</td> <!-- FoSent -->
   <td class="fo la">2.84 ± 1.41 / 50.47 ± 1.13</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">4.26</td> <!-- ScandEval rank -->
   <td class="fo ner">84.00 ± 1.30 / 84.83 ± 1.28</td> <!-- FoNE -->
   <td class="fo sent">3.05 ± 3.68 / 27.70 ± 4.19</td> <!-- FoSent -->
   <td class="fo la">1.94 ± 2.58 / 46.27 ± 2.74</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.02 ± 0.05 / 0.02 ± 0.05</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">37,268 ± 6,577 / 8,719 ± 2,865</td> <!-- Model inference speed -->
   <td class="rank">4.27</td> <!-- ScandEval rank -->
   <td class="fo ner">80.48 ± 0.91 / 81.17 ± 0.85</td> <!-- FoNE -->
   <td class="fo sent">3.50 ± 3.59 / 26.43 ± 3.38</td> <!-- FoSent -->
   <td class="fo la">0.60 ± 2.08 / 45.78 ± 2.54</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.63 ± 1.57 / 4.63 ± 2.53</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,354 ± 3,334 / 2,451 ± 777</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="fo ner">81.78 ± 0.95 / 82.55 ± 0.90</td> <!-- FoNE -->
   <td class="fo sent">4.85 ± 5.63 / 24.28 ± 7.08</td> <!-- FoSent -->
   <td class="fo la">-1.18 ± 2.36 / 37.68 ± 3.64</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.69 ± 0.78 / 1.03 ± 1.15</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">4.29</td> <!-- ScandEval rank -->
   <td class="fo ner">85.97 ± 1.12 / 86.52 ± 1.08</td> <!-- FoNE -->
   <td class="fo sent">2.54 ± 4.09 / 19.42 ± 4.54</td> <!-- FoSent -->
   <td class="fo la">0.02 ± 1.38 / 44.65 ± 2.65</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.72 ± 0.93 / 1.00 ± 1.31</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/bert-base-swedish-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,164 ± 2,392 / 4,574 ± 1,478</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="fo ner">79.99 ± 1.13 / 80.76 ± 1.10</td> <!-- FoNE -->
   <td class="fo sent">3.46 ± 2.02 / 20.63 ± 3.68</td> <!-- FoSent -->
   <td class="fo la">1.32 ± 2.66 / 49.75 ± 1.50</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.10 ± 0.15 / 0.13 ± 0.19</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="fo ner">80.45 ± 1.48 / 81.32 ± 1.42</td> <!-- FoNE -->
   <td class="fo sent">0.90 ± 2.61 / 26.49 ± 2.31</td> <!-- FoSent -->
   <td class="fo la">2.52 ± 1.88 / 47.78 ± 1.67</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.58 ± 0.81 / 1.12 ± 1.62</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="fo ner">80.58 ± 0.45 / 81.29 ± 0.46</td> <!-- FoNE -->
   <td class="fo sent">3.06 ± 2.93 / 25.95 ± 1.54</td> <!-- FoSent -->
   <td class="fo la">1.58 ± 2.34 / 49.16 ± 2.33</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">4.33</td> <!-- ScandEval rank -->
   <td class="fo ner">39.78 ± 1.79 / 31.09 ± 2.58</td> <!-- FoNE -->
   <td class="fo sent">16.03 ± 6.81 / 39.68 ± 7.16</td> <!-- FoSent -->
   <td class="fo la">-0.48 ± 1.85 / 33.39 ± 0.49</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.04 ± 4.63 / 38.93 ± 4.09</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.0.4</td> <!-- FoSent version -->
   <td>14.0.4</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,735 ± 7,558 / 6,846 ± 2,312</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="fo ner">85.58 ± 1.04 / 86.23 ± 1.03</td> <!-- FoNE -->
   <td class="fo sent">0.37 ± 2.84 / 16.66 ± 1.24</td> <!-- FoSent -->
   <td class="fo la">0.35 ± 2.36 / 43.55 ± 4.58</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,995 ± 135 / 3,839 ± 1,247</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="fo ner">62.07 ± 1.18 / 61.72 ± 1.18</td> <!-- FoNE -->
   <td class="fo sent">8.70 ± 3.64 / 31.07 ± 4.78</td> <!-- FoSent -->
   <td class="fo la">5.11 ± 3.80 / 47.64 ± 4.52</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="fo ner">45.56 ± 1.92 / 42.78 ± 1.78</td> <!-- FoNE -->
   <td class="fo sent">7.44 ± 3.71 / 28.90 ± 5.97</td> <!-- FoSent -->
   <td class="fo la">0.92 ± 2.19 / 40.29 ± 3.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">20.82 ± 1.22 / 31.49 ± 1.49</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>DDSC/roberta-base-scandinavian</td> <!-- Model ID -->
   <td class="num_model_parameters">124</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,491 ± 2,800 / 3,182 ± 1,026</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="fo ner">63.86 ± 20.89 / 64.42 ± 21.07</td> <!-- FoNE -->
   <td class="fo sent">2.04 ± 2.65 / 20.52 ± 2.77</td> <!-- FoSent -->
   <td class="fo la">0.73 ± 2.11 / 49.36 ± 1.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">10.57 ± 1.30 / 15.52 ± 1.88</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="fo ner">60.88 ± 2.03 / 60.02 ± 1.84</td> <!-- FoNE -->
   <td class="fo sent">0.16 ± 0.32 / 14.73 ± 2.24</td> <!-- FoSent -->
   <td class="fo la">-0.35 ± 1.18 / 34.50 ± 1.25</td> <!-- ScaLA-fo -->
   <td class="fo rc">18.54 ± 1.93 / 29.79 ± 1.35</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>pdelobelle/robbert-v2-dutch-base</td> <!-- Model ID -->
   <td class="num_model_parameters">116</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">40</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,481 ± 2,820 / 3,708 ± 1,186</td> <!-- Model inference speed -->
   <td class="rank">4.40</td> <!-- ScandEval rank -->
   <td class="fo ner">78.59 ± 1.16 / 79.35 ± 1.08</td> <!-- FoNE -->
   <td class="fo sent">3.32 ± 3.17 / 22.45 ± 6.10</td> <!-- FoSent -->
   <td class="fo la">0.65 ± 2.63 / 47.40 ± 3.23</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">4.41</td> <!-- ScandEval rank -->
   <td class="fo ner">73.34 ± 1.57 / 74.24 ± 1.56</td> <!-- FoNE -->
   <td class="fo sent">1.49 ± 2.48 / 20.15 ± 3.56</td> <!-- FoSent -->
   <td class="fo la">0.97 ± 2.25 / 44.25 ± 3.12</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.01 ± 0.02</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>KBLab/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,925 ± 2,281 / 4,780 ± 1,554</td> <!-- Model inference speed -->
   <td class="rank">4.41</td> <!-- ScandEval rank -->
   <td class="fo ner">73.80 ± 0.98 / 74.58 ± 0.92</td> <!-- FoNE -->
   <td class="fo sent">1.09 ± 3.08 / 22.88 ± 1.59</td> <!-- FoSent -->
   <td class="fo la">0.81 ± 2.90 / 48.11 ± 2.18</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">4.42</td> <!-- ScandEval rank -->
   <td class="fo ner">56.88 ± 2.51 / 57.68 ± 2.14</td> <!-- FoNE -->
   <td class="fo sent">3.80 ± 5.87 / 28.41 ± 4.70</td> <!-- FoSent -->
   <td class="fo la">-0.21 ± 2.20 / 34.20 ± 1.19</td> <!-- ScaLA-fo -->
   <td class="fo rc">13.72 ± 2.56 / 24.11 ± 2.40</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ltg/norbert2</td> <!-- Model ID -->
   <td class="num_model_parameters">125</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,523 ± 2,863 / 3,690 ± 1,195</td> <!-- Model inference speed -->
   <td class="rank">4.43</td> <!-- ScandEval rank -->
   <td class="fo ner">60.57 ± 0.86 / 60.42 ± 0.90</td> <!-- FoNE -->
   <td class="fo sent">2.58 ± 3.12 / 27.61 ± 2.89</td> <!-- FoSent -->
   <td class="fo la">4.16 ± 2.63 / 47.13 ± 3.43</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.84 ± 0.99 / 14.80 ± 1.25</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">4.46</td> <!-- ScandEval rank -->
   <td class="fo ner">59.50 ± 1.56 / 58.98 ± 1.55</td> <!-- FoNE -->
   <td class="fo sent">0.94 ± 4.40 / 23.64 ± 4.57</td> <!-- FoSent -->
   <td class="fo la">3.25 ± 2.04 / 49.77 ± 1.40</td> <!-- ScaLA-fo -->
   <td class="fo rc">5.56 ± 1.52 / 10.14 ± 2.41</td> <!-- FoQA -->
   <td>12.6.1</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.6.1</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">4.47</td> <!-- ScandEval rank -->
   <td class="fo ner">72.08 ± 1.25 / 72.93 ± 1.20</td> <!-- FoNE -->
   <td class="fo sent">-1.81 ± 2.47 / 15.54 ± 0.87</td> <!-- FoSent -->
   <td class="fo la">2.65 ± 2.40 / 48.48 ± 1.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>Maltehb/aelaectra-danish-electra-small-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">14</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,593 ± 114 / 3,034 ± 973</td> <!-- Model inference speed -->
   <td class="rank">4.53</td> <!-- ScandEval rank -->
   <td class="fo ner">58.52 ± 3.91 / 59.67 ± 3.83</td> <!-- FoNE -->
   <td class="fo sent">3.76 ± 3.09 / 23.86 ± 4.50</td> <!-- FoSent -->
   <td class="fo la">1.09 ± 2.20 / 33.70 ± 0.56</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>12.7.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>12.7.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,273 ± 2,312 / 3,555 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">4.54</td> <!-- ScandEval rank -->
   <td class="fo ner">58.50 ± 0.63 / 58.33 ± 0.70</td> <!-- FoNE -->
   <td class="fo sent">-0.24 ± 2.78 / 20.55 ± 2.59</td> <!-- FoSent -->
   <td class="fo la">5.96 ± 2.04 / 51.99 ± 1.53</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">4.56</td> <!-- ScandEval rank -->
   <td class="fo ner">41.27 ± 4.31 / 40.85 ± 4.31</td> <!-- FoNE -->
   <td class="fo sent">5.40 ± 3.00 / 17.90 ± 2.95</td> <!-- FoSent -->
   <td class="fo la">-0.20 ± 2.17 / 43.01 ± 3.39</td> <!-- ScaLA-fo -->
   <td class="fo rc">19.69 ± 2.66 / 29.77 ± 2.80</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">24</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">29</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,821 ± 2,209 / 3,547 ± 1,184</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="fo ner">59.66 ± 0.63 / 59.39 ± 0.60</td> <!-- FoNE -->
   <td class="fo sent">-1.39 ± 3.48 / 23.17 ± 3.58</td> <!-- FoSent -->
   <td class="fo la">4.58 ± 3.90 / 50.83 ± 2.59</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="fo ner">40.28 ± 3.29 / 42.15 ± 2.85</td> <!-- FoNE -->
   <td class="fo sent">3.94 ± 3.10 / 30.51 ± 3.43</td> <!-- FoSent -->
   <td class="fo la">-0.26 ± 1.92 / 38.29 ± 4.03</td> <!-- ScaLA-fo -->
   <td class="fo rc">10.68 ± 1.75 / 17.52 ± 1.85</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.75</td> <!-- ScandEval rank -->
   <td class="fo ner">48.70 ± 1.57 / 48.51 ± 1.57</td> <!-- FoNE -->
   <td class="fo sent">1.07 ± 2.10 / 17.71 ± 4.10</td> <!-- FoSent -->
   <td class="fo la">2.37 ± 2.06 / 37.68 ± 3.25</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>0.0.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>0.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">4.80</td> <!-- ScandEval rank -->
   <td class="fo ner">33.53 ± 3.87 / 35.41 ± 3.77</td> <!-- FoNE -->
   <td class="fo sent">4.25 ± 5.04 / 26.21 ± 4.24</td> <!-- FoSent -->
   <td class="fo la">-2.32 ± 2.11 / 45.19 ± 2.78</td> <!-- ScaLA-fo -->
   <td class="fo rc">15.41 ± 2.05 / 25.07 ± 1.98</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">4.86</td> <!-- ScandEval rank -->
   <td class="fo ner">27.91 ± 4.97 / 30.98 ± 4.28</td> <!-- FoNE -->
   <td class="fo sent">0.77 ± 4.14 / 23.56 ± 3.58</td> <!-- FoSent -->
   <td class="fo la">-0.48 ± 0.89 / 33.97 ± 1.00</td> <!-- ScaLA-fo -->
   <td class="fo rc">16.56 ± 1.66 / 26.11 ± 1.42</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">4.87</td> <!-- ScandEval rank -->
   <td class="fo ner">38.91 ± 4.57 / 39.53 ± 3.74</td> <!-- FoNE -->
   <td class="fo sent">-1.72 ± 2.43 / 16.58 ± 3.29</td> <!-- FoSent -->
   <td class="fo la">0.66 ± 0.95 / 33.60 ± 0.66</td> <!-- ScaLA-fo -->
   <td class="fo rc">4.82 ± 3.70 / 7.41 ± 5.58</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">5.03</td> <!-- ScandEval rank -->
   <td class="fo ner">26.85 ± 3.99 / 27.35 ± 3.60</td> <!-- FoNE -->
   <td class="fo sent">3.07 ± 2.88 / 28.68 ± 2.63</td> <!-- FoSent -->
   <td class="fo la">-0.12 ± 1.62 / 45.84 ± 3.59</td> <!-- ScaLA-fo -->
   <td class="fo rc">1.39 ± 0.54 / 4.02 ± 0.64</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">5.03</td> <!-- ScandEval rank -->
   <td class="fo ner">31.99 ± 3.53 / 32.31 ± 3.75</td> <!-- FoNE -->
   <td class="fo sent">0.00 ± 0.00 / 13.57 ± 0.43</td> <!-- FoSent -->
   <td class="fo la">0.48 ± 1.60 / 37.69 ± 4.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.29 ± 0.29 / 0.89 ± 0.74</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="fo ner">23.22 ± 3.22 / 24.30 ± 2.81</td> <!-- FoNE -->
   <td class="fo sent">3.78 ± 2.95 / 27.36 ± 2.62</td> <!-- FoSent -->
   <td class="fo la">0.41 ± 2.39 / 39.64 ± 3.47</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.54 ± 0.33 / 3.34 ± 0.61</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>13.3.0</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="fo ner">20.76 ± 6.32 / 22.79 ± 5.85</td> <!-- FoNE -->
   <td class="fo sent">-1.78 ± 2.38 / 16.36 ± 2.94</td> <!-- FoSent -->
   <td class="fo la">0.87 ± 1.94 / 34.86 ± 1.71</td> <!-- ScaLA-fo -->
   <td class="fo rc">3.58 ± 2.75 / 6.25 ± 4.69</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">5.08</td> <!-- ScandEval rank -->
   <td class="fo ner">28.14 ± 2.42 / 28.12 ± 2.55</td> <!-- FoNE -->
   <td class="fo sent">-0.56 ± 5.13 / 23.83 ± 3.35</td> <!-- FoSent -->
   <td class="fo la">-0.06 ± 0.67 / 33.85 ± 0.68</td> <!-- ScaLA-fo -->
   <td class="fo rc">2.43 ± 0.73 / 6.05 ± 0.59</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.08</td> <!-- ScandEval rank -->
   <td class="fo ner">22.75 ± 5.63 / 23.52 ± 4.86</td> <!-- FoNE -->
   <td class="fo sent">-0.03 ± 6.54 / 23.66 ± 3.61</td> <!-- FoSent -->
   <td class="fo la">-0.78 ± 1.59 / 33.93 ± 0.87</td> <!-- ScaLA-fo -->
   <td class="fo rc">7.75 ± 1.53 / 12.38 ± 1.36</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">5.10</td> <!-- ScandEval rank -->
   <td class="fo ner">25.51 ± 2.40 / 26.43 ± 1.77</td> <!-- FoNE -->
   <td class="fo sent">-0.24 ± 2.92 / 26.18 ± 4.52</td> <!-- FoSent -->
   <td class="fo la">0.46 ± 1.43 / 36.19 ± 3.30</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.15 ± 0.20 / 3.01 ± 0.44</td> <!-- FoQA -->
   <td>13.1.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.1.0</td> <!-- ScaLA-fo version -->
   <td>13.1.0</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>tiiuae/Falcon3-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1669</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,270 ± 2,690 / 1,434 ± 437</td> <!-- Model inference speed -->
   <td class="rank">5.10</td> <!-- ScandEval rank -->
   <td class="fo ner">14.18 ± 3.48 / 13.89 ± 3.46</td> <!-- FoNE -->
   <td class="fo sent">2.36 ± 2.76 / 17.70 ± 4.11</td> <!-- FoSent -->
   <td class="fo la">2.29 ± 2.66 / 48.34 ± 3.37</td> <!-- ScaLA-fo -->
   <td class="fo rc">6.35 ± 1.25 / 12.91 ± 1.66</td> <!-- FoQA -->
   <td>14.1.2</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.1.2</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">5.11</td> <!-- ScandEval rank -->
   <td class="fo ner">22.55 ± 5.84 / 22.62 ± 6.04</td> <!-- FoNE -->
   <td class="fo sent">0.67 ± 1.52 / 13.76 ± 0.51</td> <!-- FoSent -->
   <td class="fo la">0.87 ± 1.83 / 38.38 ± 4.75</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.27 ± 0.26 / 0.91 ± 0.72</td> <!-- FoQA -->
   <td>14.0.4</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>14.1.2</td> <!-- ScaLA-fo version -->
   <td>14.0.4</td> <!-- FoQA version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.49</td> <!-- ScandEval rank -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo sent">0.74 ± 1.78 / 13.97 ± 0.80</td> <!-- FoSent -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="fo rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoQA -->
   <td>13.0.0</td> <!-- FoNE version -->
   <td>14.1.2</td> <!-- FoSent version -->
   <td>13.0.0</td> <!-- ScaLA-fo version -->
   <td>13.0.0</td> <!-- FoQA version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/faroese-nlu.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
