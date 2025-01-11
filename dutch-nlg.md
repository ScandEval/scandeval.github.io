---
layout: leaderboard
title: Dutch NLG 🇳🇱
---

<center>Last updated: 11/01/2025 17:22:56 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="dutch-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch reading comprehension - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch summarization - BERTScore / ROUGE-L">Wiki-Lingua-NL</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-nl">CoNLL-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Dutch Social">Dutch Social version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nl">ScaLA-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD-nl">SQuAD-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Wiki-Lingua-NL">Wiki-Lingua-NL version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-nl">MMLU-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-nl">HellaSwag-nl version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8316</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.22</td> <!-- ScandEval rank -->
   <td class="nl ner">73.35 ± 2.61 / 56.00 ± 2.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.92 ± 2.78 / 40.80 ± 2.43</td> <!-- Dutch Social -->
   <td class="nl la">76.70 ± 2.39 / 88.16 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.03 ± 1.96 / 76.47 ± 1.22</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.97 ± 0.41 / 22.66 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.71 ± 2.96 / 78.12 ± 2.24</td> <!-- MMLU-nl -->
   <td class="nl reason">90.07 ± 1.29 / 92.54 ± 0.98</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.40</td> <!-- ScandEval rank -->
   <td class="nl ner">72.91 ± 3.24 / 68.06 ± 4.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">19.08 ± 3.37 / 42.04 ± 2.31</td> <!-- Dutch Social -->
   <td class="nl la">54.33 ± 3.49 / 75.54 ± 2.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.99 ± 2.07 / 77.63 ± 1.16</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.41 ± 0.97 / 25.41 ± 1.66</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.33 ± 1.92 / 73.98 ± 1.56</td> <!-- MMLU-nl -->
   <td class="nl reason">71.06 ± 2.82 / 78.16 ± 2.22</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.53</td> <!-- ScandEval rank -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.22 ± 3.26 / 33.41 ± 3.24</td> <!-- Dutch Social -->
   <td class="nl la">72.30 ± 2.26 / 85.96 ± 1.13</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.13 ± 0.50 / 17.61 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.04 ± 1.91 / 77.58 ± 1.42</td> <!-- MMLU-nl -->
   <td class="nl reason">88.29 ± 2.26 / 91.17 ± 1.70</td> <!-- HellaSwag-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.3.2</td> <!-- SQuAD-nl version -->
   <td>12.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
   <td class="nl ner">74.64 ± 3.67 / 71.84 ± 4.01</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.90 ± 2.04 / 41.93 ± 1.60</td> <!-- Dutch Social -->
   <td class="nl la">49.54 ± 4.22 / 74.03 ± 2.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">44.77 ± 1.67 / 71.44 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.28 ± 0.65 / 22.72 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.80 ± 3.16 / 74.38 ± 2.37</td> <!-- MMLU-nl -->
   <td class="nl reason">76.21 ± 1.36 / 82.15 ± 1.01</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-405B-Instruct-FP8 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">405869</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">799 ± 246 / 112 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="nl ner">69.12 ± 2.03 / 64.39 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.23 ± 1.27 / 20.82 ± 0.81</td> <!-- Dutch Social -->
   <td class="nl la">68.74 ± 0.69 / 83.97 ± 0.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.25 ± 3.26 / 73.34 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.51 ± 1.10 / 24.87 ± 1.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">74.89 ± 1.06 / 81.14 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">80.93 ± 1.07 / 85.65 ± 0.81</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="nl ner">76.75 ± 3.44 / 61.13 ± 4.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 2.24 / 32.52 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">56.26 ± 4.51 / 73.83 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.55 ± 2.54 / 76.28 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.86 ± 0.46 / 16.93 ± 0.91</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">73.11 ± 1.87 / 79.69 ± 1.46</td> <!-- MMLU-nl -->
   <td class="nl reason">92.69 ± 1.46 / 94.53 ± 1.09</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32889</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="nl ner">67.00 ± 3.69 / 56.41 ± 4.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.33 ± 4.14 / 36.14 ± 2.91</td> <!-- Dutch Social -->
   <td class="nl la">55.48 ± 4.37 / 77.55 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.02 ± 1.67 / 76.87 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.95 ± 0.75 / 21.31 ± 1.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">54.36 ± 1.61 / 65.70 ± 1.26</td> <!-- MMLU-nl -->
   <td class="nl reason">70.26 ± 3.64 / 77.62 ± 2.82</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-70B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,409 ± 457 / 186 ± 63</td> <!-- Model inference speed -->
   <td class="rank">1.80</td> <!-- ScandEval rank -->
   <td class="nl ner">68.82 ± 1.86 / 53.75 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.41 ± 1.33 / 21.26 ± 0.89</td> <!-- Dutch Social -->
   <td class="nl la">61.66 ± 1.04 / 80.70 ± 0.54</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.43 ± 1.71 / 74.07 ± 0.54</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.51 ± 0.76 / 23.39 ± 1.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">68.61 ± 1.24 / 76.39 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">69.72 ± 1.33 / 76.77 ± 1.11</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/QwQ-32B-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">32764</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,258 ± 1,221 / 198 ± 67</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="nl ner">71.32 ± 1.36 / 57.50 ± 3.60</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.12 ± 1.28 / 21.29 ± 0.75</td> <!-- Dutch Social -->
   <td class="nl la">63.96 ± 1.27 / 81.82 ± 0.72</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.36 ± 1.16 / 73.62 ± 0.47</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.59 ± 0.44 / 16.89 ± 0.53</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">67.82 ± 0.94 / 75.79 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">78.26 ± 1.44 / 83.32 ± 1.15</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="nl ner">65.20 ± 1.76 / 53.16 ± 2.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.80 ± 0.93 / 36.86 ± 1.08</td> <!-- Dutch Social -->
   <td class="nl la">59.02 ± 1.53 / 79.44 ± 0.78</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.60 ± 1.51 / 74.99 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.03 ± 1.25 / 20.76 ± 1.31</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">59.71 ± 0.83 / 69.70 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">70.70 ± 1.31 / 77.81 ± 0.99</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">637 ± 306 / 92 ± 31</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="nl ner">69.12 ± 2.60 / 41.51 ± 2.79</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.36 ± 2.16 / 19.95 ± 1.34</td> <!-- Dutch Social -->
   <td class="nl la">58.88 ± 2.34 / 79.01 ± 1.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.88 ± 1.32 / 70.93 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.09 / 13.15 ± 0.11</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.81 ± 1.85 / 78.12 ± 1.39</td> <!-- MMLU-nl -->
   <td class="nl reason">84.34 ± 2.59 / 88.20 ± 1.98</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.3-70B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,353 ± 443 / 180 ± 61</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="nl ner">70.37 ± 1.97 / 56.00 ± 2.79</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.87 ± 1.05 / 19.75 ± 0.82</td> <!-- Dutch Social -->
   <td class="nl la">62.87 ± 1.48 / 81.12 ± 0.82</td> <!-- ScaLA-nl -->
   <td class="nl rc">44.30 ± 1.09 / 68.76 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.36 ± 0.65 / 22.77 ± 1.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">68.82 ± 1.12 / 76.61 ± 0.84</td> <!-- MMLU-nl -->
   <td class="nl reason">74.72 ± 0.75 / 80.76 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen2.5-72B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">72706</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,219 ± 412 / 158 ± 53</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="nl ner">67.16 ± 1.61 / 44.06 ± 2.06</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.84 ± 1.35 / 19.81 ± 0.75</td> <!-- Dutch Social -->
   <td class="nl la">66.06 ± 1.20 / 82.87 ± 0.67</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.91 ± 2.59 / 71.45 ± 0.89</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.83 ± 0.23 / 15.04 ± 0.29</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">73.09 ± 0.79 / 79.74 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">79.00 ± 0.83 / 84.13 ± 0.64</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">784 ± 310 / 95 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="nl ner">68.71 ± 3.85 / 53.19 ± 4.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">20.33 ± 2.51 / 40.68 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">49.52 ± 5.39 / 72.59 ± 3.64</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.06 ± 3.24 / 61.15 ± 2.69</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.13 ± 0.23 / 15.64 ± 0.32</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">62.12 ± 2.67 / 71.76 ± 1.95</td> <!-- MMLU-nl -->
   <td class="nl reason">65.74 ± 3.66 / 73.59 ± 2.89</td> <!-- HellaSwag-nl -->
   <td>14.0.0</td> <!-- CoNLL-nl version -->
   <td>14.0.0</td> <!-- Dutch Social version -->
   <td>14.0.0</td> <!-- ScaLA-nl version -->
   <td>14.0.0</td> <!-- SQuAD-nl version -->
   <td>14.0.1</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.1</td> <!-- MMLU-nl version -->
   <td>14.0.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">436 ± 152 / 57 ± 21</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="nl ner">55.72 ± 3.68 / 40.53 ± 2.95</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.13 ± 1.98 / 18.38 ± 1.21</td> <!-- Dutch Social -->
   <td class="nl la">67.28 ± 2.42 / 83.06 ± 1.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 2.18 / 72.73 ± 1.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.09 ± 0.08 / 12.91 ± 0.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">67.45 ± 1.74 / 75.66 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl reason">72.71 ± 2.29 / 79.49 ± 1.72</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/c4ai-command-r-08-2024 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">32296</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,909 ± 646 / 248 ± 84</td> <!-- Model inference speed -->
   <td class="rank">2.01</td> <!-- ScandEval rank -->
   <td class="nl ner">68.58 ± 1.76 / 44.49 ± 2.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.41 ± 1.69 / 35.58 ± 1.84</td> <!-- Dutch Social -->
   <td class="nl la">55.01 ± 1.21 / 77.17 ± 0.63</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.63 ± 0.55 / 72.85 ± 0.32</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.69 ± 0.95 / 16.39 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">50.48 ± 0.92 / 62.55 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">49.08 ± 1.51 / 60.63 ± 1.34</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="nl ner">57.13 ± 2.73 / 36.21 ± 1.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.43 ± 2.17 / 40.83 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">31.39 ± 5.53 / 56.70 ± 5.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.33 ± 1.35 / 73.56 ± 0.52</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.59 ± 1.21 / 21.08 ± 1.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.71 ± 0.86 / 65.15 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">53.26 ± 3.38 / 63.65 ± 2.84</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">908 ± 303 / 96 ± 36</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="nl ner">64.15 ± 2.49 / 38.77 ± 2.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.67 ± 2.02 / 18.63 ± 1.37</td> <!-- Dutch Social -->
   <td class="nl la">62.44 ± 3.24 / 80.58 ± 1.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.65 ± 1.56 / 70.43 ± 1.29</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.26 ± 0.11 / 13.64 ± 0.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">56.45 ± 2.36 / 67.46 ± 1.73</td> <!-- MMLU-nl -->
   <td class="nl reason">62.09 ± 2.86 / 71.09 ± 2.06</td> <!-- HellaSwag-nl -->
   <td>14.0.1</td> <!-- CoNLL-nl version -->
   <td>14.0.1</td> <!-- Dutch Social version -->
   <td>14.0.1</td> <!-- ScaLA-nl version -->
   <td>14.0.1</td> <!-- SQuAD-nl version -->
   <td>14.0.1</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="nl ner">65.37 ± 1.61 / 46.10 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.93 ± 1.80 / 34.67 ± 2.84</td> <!-- Dutch Social -->
   <td class="nl la">41.67 ± 1.53 / 69.81 ± 1.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">67.75 ± 0.62 / 78.01 ± 0.45</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.83 ± 0.35 / 26.12 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.18 ± 0.57 / 55.06 ± 0.44</td> <!-- MMLU-nl -->
   <td class="nl reason">65.34 ± 1.05 / 73.48 ± 0.83</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="nl ner">68.17 ± 1.75 / 51.61 ± 2.73</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.56 ± 1.04 / 19.29 ± 0.63</td> <!-- Dutch Social -->
   <td class="nl la">56.89 ± 0.82 / 78.31 ± 0.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.05 ± 2.18 / 71.82 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.01 ± 0.23 / 15.23 ± 0.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">58.74 ± 0.88 / 68.94 ± 0.65</td> <!-- MMLU-nl -->
   <td class="nl reason">65.18 ± 0.73 / 73.34 ± 0.53</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="nl ner">52.62 ± 2.15 / 39.41 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.78 ± 1.31 / 32.80 ± 0.87</td> <!-- Dutch Social -->
   <td class="nl la">59.23 ± 1.58 / 79.42 ± 0.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.78 ± 0.87 / 72.71 ± 0.70</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.39 ± 0.71 / 20.04 ± 1.05</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.99 ± 0.77 / 65.31 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">65.58 ± 1.18 / 73.75 ± 0.94</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.13 ± 0.41 / 21.32 ± 0.75</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.28 ± 2.88 / 56.45 ± 2.26</td> <!-- MMLU-nl -->
   <td class="nl reason">61.52 ± 2.69 / 70.62 ± 2.20</td> <!-- HellaSwag-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>0.0.0</td> <!-- MMLU-nl version -->
   <td>0.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="nl ner">66.50 ± 3.72 / 57.66 ± 3.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.82 ± 4.30 / 34.91 ± 2.53</td> <!-- Dutch Social -->
   <td class="nl la">49.55 ± 4.95 / 73.43 ± 3.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">65.26 ± 1.55 / 77.36 ± 1.41</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.28 ± 1.07 / 21.33 ± 1.39</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">49.41 ± 2.21 / 61.91 ± 1.74</td> <!-- MMLU-nl -->
   <td class="nl reason">54.50 ± 4.84 / 65.70 ± 3.64</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="nl ner">64.00 ± 3.52 / 48.94 ± 3.83</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.30 ± 3.75 / 30.50 ± 2.48</td> <!-- Dutch Social -->
   <td class="nl la">30.88 ± 4.62 / 59.62 ± 4.50</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.14 ± 1.55 / 70.96 ± 1.01</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.71 ± 0.70 / 19.82 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">45.47 ± 2.07 / 59.14 ± 1.69</td> <!-- MMLU-nl -->
   <td class="nl reason">42.91 ± 3.26 / 57.30 ± 2.39</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="nl ner">66.57 ± 1.86 / 48.40 ± 2.67</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.10 ± 1.55 / 33.62 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">40.31 ± 2.25 / 69.53 ± 1.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.99 ± 0.95 / 74.24 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.68 / 20.75 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.50 ± 0.84 / 56.53 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">48.51 ± 1.44 / 60.59 ± 1.34</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/Llama-3.1-Nemotron-70B-Instruct-HF (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,208 ± 412 / 156 ± 53</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="nl ner">55.08 ± 2.19 / 30.07 ± 1.17</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 1.40 / 20.34 ± 0.88</td> <!-- Dutch Social -->
   <td class="nl la">61.31 ± 1.10 / 80.58 ± 0.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.80 ± 1.58 / 70.37 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.72 ± 0.51 / 9.05 ± 0.31</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">68.15 ± 1.32 / 76.04 ± 1.01</td> <!-- MMLU-nl -->
   <td class="nl reason">72.50 ± 0.80 / 79.13 ± 0.64</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,686 ± 685 / 491 ± 164</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="nl ner">53.02 ± 1.86 / 30.09 ± 1.16</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.68 ± 1.32 / 34.87 ± 0.67</td> <!-- Dutch Social -->
   <td class="nl la">29.97 ± 2.13 / 64.01 ± 1.12</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.40 ± 1.34 / 69.31 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">73.93 ± 0.30 / 30.81 ± 0.43</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.81 ± 1.13 / 53.87 ± 0.90</td> <!-- MMLU-nl -->
   <td class="nl reason">40.95 ± 1.72 / 55.25 ± 1.38</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.1.2</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.2</td> <!-- MMLU-nl version -->
   <td>14.1.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="nl ner">64.25 ± 2.23 / 46.52 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.66 ± 1.99 / 39.45 ± 1.52</td> <!-- Dutch Social -->
   <td class="nl la">28.59 ± 1.48 / 61.24 ± 1.46</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.64 ± 0.86 / 68.04 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.57 / 19.51 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.37 ± 1.30 / 51.43 ± 0.96</td> <!-- MMLU-nl -->
   <td class="nl reason">47.50 ± 1.75 / 60.41 ± 1.32</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mixtral-8x7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46703</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,535 ± 1,837 / 760 ± 256</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="nl ner">58.80 ± 3.37 / 37.95 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.50 ± 1.74 / 33.57 ± 1.09</td> <!-- Dutch Social -->
   <td class="nl la">45.22 ± 1.65 / 71.80 ± 1.10</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.03 ± 2.34 / 67.41 ± 1.00</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.95 ± 0.32 / 15.67 ± 0.51</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">43.41 ± 1.10 / 57.51 ± 0.81</td> <!-- MMLU-nl -->
   <td class="nl reason">43.33 ± 1.37 / 57.03 ± 1.09</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.94 ± 1.12 / 70.12 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="nl summ">71.20 ± 0.46 / 23.47 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.23 ± 2.86 / 54.77 ± 2.16</td> <!-- MMLU-nl -->
   <td class="nl reason">47.87 ± 2.49 / 60.78 ± 1.85</td> <!-- HellaSwag-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,986 ± 823 / 276 ± 94</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="nl ner">64.79 ± 1.96 / 45.48 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.83 / 37.12 ± 2.19</td> <!-- Dutch Social -->
   <td class="nl la">32.97 ± 2.68 / 58.52 ± 2.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.89 ± 1.06 / 74.73 ± 1.02</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.29 ± 1.29 / 20.14 ± 1.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.44 ± 1.33 / 53.68 ± 1.01</td> <!-- MMLU-nl -->
   <td class="nl reason">30.88 ± 2.27 / 47.18 ± 1.81</td> <!-- HellaSwag-nl -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,707 ± 688 / 497 ± 166</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="nl ner">60.81 ± 1.94 / 46.59 ± 3.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.63 / 24.82 ± 0.95</td> <!-- Dutch Social -->
   <td class="nl la">31.12 ± 2.35 / 64.29 ± 1.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.00 ± 1.23 / 74.60 ± 0.67</td> <!-- SQuAD-nl -->
   <td class="nl summ">72.90 ± 0.24 / 30.63 ± 0.42</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.37 ± 1.09 / 48.63 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">53.32 ± 1.89 / 64.30 ± 1.72</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="nl ner">43.06 ± 1.89 / 30.50 ± 1.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.25 / 33.40 ± 1.41</td> <!-- Dutch Social -->
   <td class="nl la">40.85 ± 3.31 / 68.94 ± 2.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.42 ± 0.63 / 74.62 ± 0.52</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.33 ± 0.60 / 23.01 ± 1.18</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">41.90 ± 1.02 / 56.09 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">36.69 ± 1.64 / 50.85 ± 1.65</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 377 / 287 ± 97</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="nl ner">68.72 ± 1.81 / 54.89 ± 2.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.67 ± 2.51 / 41.36 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">32.91 ± 2.56 / 64.93 ± 1.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.36 ± 1.31 / 67.50 ± 0.69</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.82 / 18.19 ± 1.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.18 ± 1.31 / 51.68 ± 1.05</td> <!-- MMLU-nl -->
   <td class="nl reason">33.91 ± 1.71 / 48.01 ± 1.47</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mixtral-8x7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46703</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,363 ± 794 / 311 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="nl ner">64.81 ± 2.75 / 50.00 ± 2.43</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.99 ± 2.90 / 35.40 ± 3.35</td> <!-- Dutch Social -->
   <td class="nl la">39.38 ± 1.67 / 69.22 ± 0.96</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.08 ± 2.09 / 59.88 ± 2.00</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.41 ± 0.70 / 20.80 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">45.60 ± 1.16 / 59.03 ± 0.83</td> <!-- MMLU-nl -->
   <td class="nl reason">24.71 ± 2.75 / 41.41 ± 2.20</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,136 ± 1,282 / 668 ± 326</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="nl ner">63.01 ± 2.00 / 33.76 ± 1.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.13 ± 1.83 / 40.18 ± 1.61</td> <!-- Dutch Social -->
   <td class="nl la">39.20 ± 1.25 / 68.05 ± 1.27</td> <!-- ScaLA-nl -->
   <td class="nl rc">36.46 ± 2.79 / 59.21 ± 2.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.42 ± 0.66 / 14.56 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.99 ± 1.03 / 49.58 ± 0.77</td> <!-- MMLU-nl -->
   <td class="nl reason">42.56 ± 1.31 / 56.00 ± 0.93</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt-mixtral (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="nl ner">62.16 ± 1.09 / 45.76 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.92 ± 1.08 / 24.28 ± 0.76</td> <!-- Dutch Social -->
   <td class="nl la">32.76 ± 2.94 / 65.17 ± 2.79</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.87 ± 0.92 / 72.57 ± 0.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.39 ± 0.73 / 20.83 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">46.17 ± 0.64 / 59.57 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">33.31 ± 1.83 / 49.12 ± 1.64</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,302 ± 323 / 253 ± 86</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="nl ner">63.30 ± 2.36 / 39.20 ± 2.16</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.82 ± 1.07 / 34.18 ± 1.11</td> <!-- Dutch Social -->
   <td class="nl la">32.20 ± 0.77 / 65.67 ± 0.69</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.45 ± 0.89 / 71.13 ± 0.60</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.60 ± 0.14 / 15.53 ± 0.18</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.02 ± 0.79 / 49.45 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">44.88 ± 2.56 / 57.56 ± 2.18</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.1.2</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.2</td> <!-- MMLU-nl version -->
   <td>14.1.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="nl ner">64.71 ± 5.15 / 53.58 ± 3.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.14 ± 3.37 / 38.64 ± 2.36</td> <!-- Dutch Social -->
   <td class="nl la">25.22 ± 5.45 / 61.28 ± 2.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">46.34 ± 1.07 / 66.56 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.71 ± 0.59 / 17.76 ± 0.71</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.49 ± 2.59 / 53.52 ± 2.03</td> <!-- MMLU-nl -->
   <td class="nl reason">47.66 ± 2.91 / 60.31 ± 2.30</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>yhavinga/Boreas-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,913 ± 459 / 1,129 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="nl ner">60.22 ± 1.55 / 38.72 ± 1.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.97 ± 1.80 / 35.17 ± 3.03</td> <!-- Dutch Social -->
   <td class="nl la">30.94 ± 4.81 / 62.66 ± 3.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.19 ± 1.96 / 67.52 ± 1.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.60 ± 1.93 / 20.00 ± 1.35</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.34 ± 1.32 / 51.45 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">31.47 ± 2.90 / 47.64 ± 2.52</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/c4ai-command-r-v01 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">34981</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,919 ± 645 / 248 ± 83</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="nl ner">61.21 ± 2.15 / 41.76 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.03 ± 1.38 / 29.15 ± 1.45</td> <!-- Dutch Social -->
   <td class="nl la">38.15 ± 2.37 / 65.60 ± 2.16</td> <!-- ScaLA-nl -->
   <td class="nl rc">44.91 ± 3.07 / 63.57 ± 1.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.58 ± 0.17 / 18.69 ± 0.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">41.03 ± 0.96 / 55.56 ± 0.74</td> <!-- MMLU-nl -->
   <td class="nl reason">44.57 ± 1.60 / 58.17 ± 1.22</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.1.1</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.1</td> <!-- MMLU-nl version -->
   <td>14.1.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,477 ± 376 / 285 ± 97</td> <!-- Model inference speed -->
   <td class="rank">2.54</td> <!-- ScandEval rank -->
   <td class="nl ner">62.26 ± 2.20 / 42.41 ± 2.02</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.45 ± 2.69 / 33.45 ± 1.99</td> <!-- Dutch Social -->
   <td class="nl la">30.30 ± 3.94 / 62.28 ± 2.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.99 ± 1.00 / 73.73 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.17 ± 1.24 / 18.63 ± 1.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.38 ± 0.86 / 52.08 ± 0.66</td> <!-- MMLU-nl -->
   <td class="nl reason">28.33 ± 2.31 / 45.29 ± 1.78</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-sonnet-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">193 ± 87 / 55 ± 19</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="nl ner">62.41 ± 2.92 / 52.27 ± 2.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.64 ± 2.16 / 33.98 ± 1.59</td> <!-- Dutch Social -->
   <td class="nl la">74.06 ± 2.21 / 86.59 ± 1.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">35.77 ± 1.20 / 68.02 ± 1.47</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.25 ± 0.09 / 13.47 ± 0.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.77 ± 1.44 / 40.51 ± 0.91</td> <!-- MMLU-nl -->
   <td class="nl reason">14.21 ± 1.94 / 33.83 ± 1.57</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.3</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/mistral-nemo-minitron-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8414</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,470 ± 836 / 326 ± 111</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="nl ner">66.29 ± 2.06 / 47.69 ± 2.04</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.71 ± 2.10 / 37.65 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">31.39 ± 1.27 / 63.48 ± 1.67</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.33 ± 1.71 / 58.63 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.10 ± 0.62 / 17.65 ± 0.69</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">37.55 ± 1.03 / 52.98 ± 0.83</td> <!-- MMLU-nl -->
   <td class="nl reason">29.69 ± 2.55 / 44.05 ± 2.51</td> <!-- HellaSwag-nl -->
   <td>14.1.1</td> <!-- CoNLL-nl version -->
   <td>14.1.1</td> <!-- Dutch Social version -->
   <td>14.1.1</td> <!-- ScaLA-nl version -->
   <td>14.1.1</td> <!-- SQuAD-nl version -->
   <td>14.1.1</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.1</td> <!-- MMLU-nl version -->
   <td>14.1.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat-Sft-Bf16 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,413 ± 463 / 700 ± 220</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="nl ner">56.83 ± 2.31 / 46.81 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.79 ± 1.96 / 41.48 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">23.58 ± 2.69 / 50.85 ± 3.74</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.90 ± 1.80 / 70.07 ± 0.77</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.06 ± 1.20 / 18.45 ± 1.09</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.73 ± 0.75 / 50.05 ± 0.57</td> <!-- MMLU-nl -->
   <td class="nl reason">29.29 ± 1.83 / 45.90 ± 1.77</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Reynaerde-7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,562 ± 487 / 782 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="nl ner">59.16 ± 2.29 / 42.33 ± 2.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.39 ± 1.44 / 28.74 ± 1.05</td> <!-- Dutch Social -->
   <td class="nl la">19.50 ± 1.96 / 55.52 ± 3.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.96 ± 1.24 / 72.79 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.19 ± 0.63 / 20.85 ± 0.78</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.93 ± 0.63 / 49.37 ± 0.55</td> <!-- MMLU-nl -->
   <td class="nl reason">28.04 ± 1.54 / 45.48 ± 1.35</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,686 ± 1,131 / 996 ± 326</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="nl ner">57.81 ± 2.68 / 47.15 ± 2.77</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.62 ± 2.25 / 41.08 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">25.34 ± 2.37 / 54.46 ± 3.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.81 ± 1.44 / 70.49 ± 0.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.51 ± 2.40 / 15.62 ± 1.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.78 ± 0.80 / 50.83 ± 0.58</td> <!-- MMLU-nl -->
   <td class="nl reason">30.29 ± 1.78 / 46.74 ± 1.68</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Reynaerde-7B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,554 ± 483 / 781 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="nl ner">56.22 ± 2.46 / 38.04 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.22 ± 1.85 / 30.99 ± 1.36</td> <!-- Dutch Social -->
   <td class="nl la">20.04 ± 1.67 / 55.38 ± 3.62</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.15 ± 1.01 / 72.89 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.28 ± 0.61 / 20.97 ± 0.82</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.44 ± 0.61 / 49.05 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">31.24 ± 1.92 / 47.72 ± 1.69</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mgoin/Nemotron-4-340B-Instruct-hf-FP8 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">341029</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,904 ± 475 / 361 ± 121</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="nl ner">47.60 ± 2.59 / 29.38 ± 1.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.62 ± 2.33 / 34.10 ± 2.72</td> <!-- Dutch Social -->
   <td class="nl la">61.64 ± 9.03 / 78.16 ± 6.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">24.02 ± 6.42 / 38.65 ± 10.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.51 ± 2.27 / 8.49 ± 1.49</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">50.32 ± 11.27 / 61.39 ± 9.56</td> <!-- MMLU-nl -->
   <td class="nl reason">64.62 ± 6.94 / 71.43 ± 6.37</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="nl ner">53.62 ± 2.29 / 40.51 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.37 ± 1.25 / 36.94 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">23.47 ± 1.79 / 60.17 ± 1.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.20 ± 1.02 / 72.98 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.34 ± 3.24 / 18.49 ± 1.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.69 ± 0.59 / 50.59 ± 0.56</td> <!-- MMLU-nl -->
   <td class="nl reason">31.36 ± 1.90 / 46.78 ± 1.51</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Llama-3-8B-dutch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,800 ± 1,275 / 566 ± 194</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="nl ner">60.14 ± 2.00 / 44.91 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.07 ± 1.98 / 34.77 ± 1.31</td> <!-- Dutch Social -->
   <td class="nl la">15.67 ± 3.75 / 40.14 ± 2.65</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.93 ± 1.17 / 71.20 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.49 ± 1.40 / 18.40 ± 1.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.13 ± 1.24 / 51.76 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">28.25 ± 2.23 / 44.23 ± 2.03</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 625 / 476 ± 159</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="nl ner">52.32 ± 1.98 / 41.98 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.46 ± 1.09 / 21.30 ± 0.67</td> <!-- Dutch Social -->
   <td class="nl la">42.42 ± 3.42 / 68.81 ± 2.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.12 ± 1.81 / 63.79 ± 1.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.00 ± 0.61 / 18.47 ± 0.79</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.34 ± 0.87 / 50.51 ± 0.72</td> <!-- MMLU-nl -->
   <td class="nl reason">26.46 ± 3.88 / 43.33 ± 3.00</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.1.2</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.2</td> <!-- MMLU-nl version -->
   <td>14.1.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,473 ± 377 / 283 ± 96</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="nl ner">61.68 ± 1.94 / 42.64 ± 1.85</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.97 ± 1.44 / 20.07 ± 0.82</td> <!-- Dutch Social -->
   <td class="nl la">36.57 ± 1.77 / 65.25 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">33.88 ± 1.83 / 62.17 ± 0.91</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.80 ± 0.38 / 16.87 ± 0.29</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">37.45 ± 0.61 / 53.03 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">42.45 ± 1.72 / 56.78 ± 1.31</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.1.2</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.2</td> <!-- MMLU-nl version -->
   <td>14.1.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/Mistral-7B-v0.1-chat-nl (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,907 ± 1,028 / 1,695 ± 549</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="nl ner">56.73 ± 1.95 / 38.97 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.08 ± 1.46 / 32.20 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">19.41 ± 2.55 / 57.17 ± 2.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.91 ± 0.92 / 71.22 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.05 ± 0.39 / 21.26 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">31.39 ± 0.86 / 48.09 ± 0.72</td> <!-- MMLU-nl -->
   <td class="nl reason">16.49 ± 2.14 / 36.67 ± 1.72</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mixtral-8x7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46998</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,015 ± 2,966 / 1,121 ± 510</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="nl ner">62.81 ± 3.06 / 43.07 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.28 ± 2.13 / 32.44 ± 3.18</td> <!-- Dutch Social -->
   <td class="nl la">28.57 ± 2.14 / 60.59 ± 2.37</td> <!-- ScaLA-nl -->
   <td class="nl rc">38.75 ± 5.65 / 58.21 ± 3.41</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.35 ± 0.98 / 18.66 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">39.53 ± 0.99 / 54.24 ± 0.73</td> <!-- MMLU-nl -->
   <td class="nl reason">26.71 ± 3.11 / 44.58 ± 2.46</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="nl ner">47.75 ± 2.33 / 35.64 ± 1.89</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.68 ± 0.61 / 26.25 ± 1.18</td> <!-- Dutch Social -->
   <td class="nl la">28.28 ± 2.48 / 62.81 ± 1.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.49 ± 1.15 / 73.19 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.60 ± 1.18 / 19.95 ± 1.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.19 ± 0.97 / 55.52 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">31.45 ± 2.79 / 44.15 ± 3.09</td> <!-- HellaSwag-nl -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.9.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.9.1</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,370 ± 416 / 711 ± 242</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.99 ± 0.49 / 19.54 ± 0.55</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.86 ± 1.89 / 41.71 ± 1.45</td> <!-- MMLU-nl -->
   <td class="nl reason">24.80 ± 1.77 / 42.93 ± 1.38</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="nl ner">52.52 ± 1.62 / 44.69 ± 2.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.85 ± 1.90 / 36.43 ± 2.11</td> <!-- Dutch Social -->
   <td class="nl la">17.72 ± 1.86 / 57.31 ± 1.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.50 ± 1.16 / 67.02 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.23 ± 0.48 / 18.18 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.62 ± 0.65 / 43.32 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">15.79 ± 1.37 / 35.56 ± 1.11</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,446 ± 354 / 295 ± 100</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.24 ± 0.91 / 17.54 ± 1.10</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.49 ± 0.57 / 51.51 ± 0.42</td> <!-- MMLU-nl -->
   <td class="nl reason">19.88 ± 1.80 / 39.13 ± 1.56</td> <!-- HellaSwag-nl -->
   <td>9.1.2</td> <!-- CoNLL-nl version -->
   <td>9.1.2</td> <!-- Dutch Social version -->
   <td>9.1.2</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="nl ner">47.28 ± 1.57 / 36.12 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.12 ± 1.92 / 35.44 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">12.74 ± 2.68 / 52.69 ± 2.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.36 ± 1.36 / 71.20 ± 0.77</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.26 ± 0.75 / 16.55 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.88 ± 0.86 / 44.76 ± 0.70</td> <!-- MMLU-nl -->
   <td class="nl reason">34.05 ± 1.57 / 50.08 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mixtral-8x7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">46998</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,368 ± 793 / 317 ± 108</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="nl ner">62.76 ± 3.54 / 40.29 ± 1.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.83 ± 1.32 / 37.70 ± 1.94</td> <!-- Dutch Social -->
   <td class="nl la">24.44 ± 2.86 / 58.02 ± 2.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.17 ± 2.88 / 37.61 ± 2.20</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.34 ± 0.59 / 18.36 ± 0.69</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.50 ± 0.76 / 52.93 ± 0.49</td> <!-- MMLU-nl -->
   <td class="nl reason">20.26 ± 3.39 / 38.63 ± 3.03</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="nl ner">56.76 ± 1.52 / 42.03 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.11 ± 1.17 / 26.36 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">23.55 ± 2.76 / 59.14 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.89 ± 1.10 / 72.41 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.33 ± 0.72 / 17.66 ± 0.87</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.92 ± 1.07 / 51.02 ± 0.85</td> <!-- MMLU-nl -->
   <td class="nl reason">23.87 ± 1.80 / 42.03 ± 1.58</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/GEITje-7B-ultra (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,475 ± 460 / 765 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="nl ner">42.20 ± 2.20 / 27.85 ± 1.11</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.78 ± 2.52 / 42.17 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">18.23 ± 1.91 / 50.04 ± 2.54</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.41 ± 1.11 / 66.45 ± 0.46</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.30 ± 0.40 / 20.79 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.92 ± 1.09 / 44.44 ± 0.85</td> <!-- MMLU-nl -->
   <td class="nl reason">25.72 ± 1.01 / 43.74 ± 0.69</td> <!-- HellaSwag-nl -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>10.0.1</td> <!-- MMLU-nl version -->
   <td>10.0.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,364 ± 343 / 266 ± 90</td> <!-- Model inference speed -->
   <td class="rank">2.85</td> <!-- ScandEval rank -->
   <td class="nl ner">56.52 ± 1.42 / 41.84 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.02 ± 1.21 / 26.40 ± 2.96</td> <!-- Dutch Social -->
   <td class="nl la">23.41 ± 2.91 / 59.14 ± 3.11</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.90 ± 1.07 / 72.49 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.74 / 17.69 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.93 ± 1.11 / 51.02 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">23.73 ± 1.97 / 41.93 ± 1.68</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,681 ± 1,650 / 2,177 ± 717</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="nl ner">50.31 ± 1.94 / 41.54 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.58 ± 1.62 / 36.56 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">14.72 ± 1.84 / 50.23 ± 3.10</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.19 ± 0.80 / 66.72 ± 0.92</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.40 ± 0.77 / 17.47 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.31 ± 0.70 / 46.18 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">21.25 ± 1.25 / 40.78 ± 1.02</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.5</td> <!-- MMLU-nl version -->
   <td>12.10.5</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>neuralmagic/Sparse-Llama-3.1-8B-2of4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,996 ± 817 / 284 ± 96</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="nl ner">34.21 ± 3.16 / 33.46 ± 2.25</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.94 ± 2.89 / 34.06 ± 1.51</td> <!-- Dutch Social -->
   <td class="nl la">6.18 ± 3.30 / 37.82 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.44 ± 0.63 / 71.27 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.48 ± 0.77 / 20.21 ± 0.93</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.76 ± 0.98 / 46.99 ± 0.77</td> <!-- MMLU-nl -->
   <td class="nl reason">38.79 ± 3.59 / 51.86 ± 3.32</td> <!-- HellaSwag-nl -->
   <td>13.2.0</td> <!-- CoNLL-nl version -->
   <td>13.2.0</td> <!-- Dutch Social version -->
   <td>13.2.0</td> <!-- ScaLA-nl version -->
   <td>13.2.0</td> <!-- SQuAD-nl version -->
   <td>13.2.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.2.0</td> <!-- MMLU-nl version -->
   <td>13.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="nl ner">57.80 ± 1.53 / 39.43 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 1.27 / 29.84 ± 2.35</td> <!-- Dutch Social -->
   <td class="nl la">17.40 ± 1.54 / 57.26 ± 1.96</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.35 ± 0.85 / 69.69 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.11 ± 0.58 / 18.31 ± 0.61</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.15 ± 1.09 / 44.95 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">19.18 ± 1.46 / 38.84 ± 1.26</td> <!-- HellaSwag-nl -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="nl ner">43.66 ± 2.01 / 40.23 ± 1.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.87 ± 1.32 / 37.23 ± 1.55</td> <!-- Dutch Social -->
   <td class="nl la">17.94 ± 3.48 / 55.88 ± 3.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.77 ± 1.82 / 64.44 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.74 ± 1.00 / 18.33 ± 1.28</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.80 ± 0.84 / 50.30 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">21.02 ± 1.29 / 40.27 ± 1.09</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B-chat-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,908 ± 1,022 / 1,694 ± 551</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="nl ner">42.12 ± 4.00 / 31.12 ± 1.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.06 ± 2.30 / 40.32 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">19.71 ± 3.65 / 49.65 ± 4.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.19 ± 0.91 / 70.06 ± 0.82</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.55 ± 0.49 / 19.18 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.71 ± 0.91 / 45.01 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">18.03 ± 1.77 / 36.82 ± 1.76</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="nl ner">57.66 ± 1.29 / 43.77 ± 2.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.41 ± 1.47 / 25.59 ± 1.30</td> <!-- Dutch Social -->
   <td class="nl la">16.93 ± 2.60 / 55.72 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.29 ± 1.11 / 68.94 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.22 ± 0.50 / 19.03 ± 0.51</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.70 ± 1.05 / 44.15 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">17.92 ± 1.69 / 37.64 ± 1.43</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="nl ner">40.58 ± 2.08 / 28.95 ± 1.56</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.17 ± 1.32 / 32.96 ± 1.96</td> <!-- Dutch Social -->
   <td class="nl la">19.63 ± 2.61 / 52.65 ± 2.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.30 ± 1.25 / 67.27 ± 0.73</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.83 ± 0.86 / 19.21 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.30 ± 1.02 / 46.88 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">31.43 ± 1.42 / 47.87 ± 1.30</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="nl ner">63.29 ± 2.51 / 52.18 ± 4.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.81 ± 1.66 / 36.99 ± 2.58</td> <!-- Dutch Social -->
   <td class="nl la">8.16 ± 1.97 / 44.29 ± 4.25</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.64 ± 0.68 / 66.29 ± 0.71</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.08 ± 0.90 / 15.69 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">16.86 ± 1.16 / 37.54 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">6.24 ± 0.78 / 29.25 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-haiku-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">277 ± 77 / 70 ± 25</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="nl ner">61.15 ± 3.04 / 43.60 ± 2.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.71 ± 2.21 / 30.22 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">35.26 ± 2.46 / 59.55 ± 1.69</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.27 ± 1.25 / 68.96 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.93 ± 0.11 / 13.88 ± 0.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">8.55 ± 2.28 / 28.32 ± 1.08</td> <!-- MMLU-nl -->
   <td class="nl reason">10.69 ± 1.69 / 31.29 ± 1.47</td> <!-- HellaSwag-nl -->
   <td>14.0.3</td> <!-- CoNLL-nl version -->
   <td>14.0.2</td> <!-- Dutch Social version -->
   <td>14.0.3</td> <!-- ScaLA-nl version -->
   <td>14.0.3</td> <!-- SQuAD-nl version -->
   <td>14.0.3</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.3</td> <!-- MMLU-nl version -->
   <td>14.0.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="nl ner">44.27 ± 2.14 / 34.47 ± 2.48</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.84 ± 1.82 / 36.64 ± 1.13</td> <!-- Dutch Social -->
   <td class="nl la">10.44 ± 1.58 / 48.93 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.40 ± 1.14 / 68.02 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.60 ± 0.62 / 15.63 ± 0.45</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.63 ± 0.84 / 46.39 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">22.58 ± 0.97 / 41.78 ± 0.71</td> <!-- HellaSwag-nl -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="nl ner">53.78 ± 1.86 / 41.29 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.46 ± 0.67 / 19.49 ± 0.92</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.37 ± 0.99 / 45.81 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">15.25 ± 1.71 / 35.83 ± 1.42</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.2.0</td> <!-- Dutch Social version -->
   <td>12.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.3.1</td> <!-- MMLU-nl version -->
   <td>12.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2775</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,710 ± 1,040 / 1,188 ± 383</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="nl ner">36.50 ± 2.72 / 28.73 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.70 ± 2.29 / 40.77 ± 1.77</td> <!-- Dutch Social -->
   <td class="nl la">4.81 ± 2.20 / 43.19 ± 1.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.63 ± 0.62 / 71.62 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.01 ± 0.42 / 17.97 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.76 ± 1.00 / 44.94 ± 0.74</td> <!-- MMLU-nl -->
   <td class="nl reason">12.93 ± 1.54 / 34.12 ± 1.22</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="nl ner">53.93 ± 2.71 / 47.48 ± 2.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.83 ± 2.37 / 34.00 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">6.58 ± 3.36 / 48.51 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.45 ± 2.52 / 67.47 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.89 ± 0.38 / 17.99 ± 0.46</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">19.58 ± 1.24 / 38.76 ± 1.06</td> <!-- MMLU-nl -->
   <td class="nl reason">13.68 ± 1.08 / 32.30 ± 0.99</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,920 ± 1,028 / 1,696 ± 550</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="nl ner">50.69 ± 1.67 / 35.96 ± 2.63</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.16 ± 1.68 / 27.37 ± 1.95</td> <!-- Dutch Social -->
   <td class="nl la">20.45 ± 2.12 / 59.00 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.48 ± 0.86 / 66.71 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.92 ± 0.50 / 20.19 ± 0.69</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.89 ± 1.55 / 42.34 ± 1.14</td> <!-- MMLU-nl -->
   <td class="nl reason">9.84 ± 1.87 / 30.90 ± 1.58</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2775</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,704 ± 1,015 / 1,185 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="nl ner">39.57 ± 2.74 / 31.81 ± 1.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.25 ± 2.12 / 39.92 ± 1.66</td> <!-- Dutch Social -->
   <td class="nl la">9.31 ± 1.92 / 50.99 ± 2.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.26 ± 0.62 / 71.03 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.37 ± 0.53 / 17.63 ± 0.74</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.63 ± 1.33 / 44.86 ± 1.00</td> <!-- MMLU-nl -->
   <td class="nl reason">11.62 ± 1.28 / 32.71 ± 1.00</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-70B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,220 ± 411 / 158 ± 53</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="nl ner">69.37 ± 2.25 / 59.14 ± 2.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.35 ± 1.64 / 31.18 ± 2.02</td> <!-- Dutch Social -->
   <td class="nl la">29.13 ± 3.95 / 58.71 ± 5.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.34 ± 0.14 / 15.25 ± 0.86</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.69 ± 0.52 / 10.85 ± 0.37</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">50.90 ± 1.94 / 63.00 ± 1.48</td> <!-- MMLU-nl -->
   <td class="nl reason">34.78 ± 2.85 / 49.76 ± 2.31</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="nl ner">42.52 ± 2.25 / 37.46 ± 3.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.75 ± 0.84 / 14.83 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.25 ± 1.22 / 43.08 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">16.21 ± 1.51 / 37.11 ± 1.16</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="nl ner">52.55 ± 1.64 / 43.32 ± 1.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.26 ± 2.09 / 28.32 ± 2.68</td> <!-- Dutch Social -->
   <td class="nl la">24.57 ± 3.54 / 54.94 ± 5.33</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.99 ± 0.95 / 72.74 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.02 ± 0.84 / 16.97 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.73 ± 0.90 / 45.62 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">19.43 ± 1.53 / 38.57 ± 1.39</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="nl ner">47.53 ± 1.90 / 32.42 ± 1.99</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.36 ± 2.96 / 28.11 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">30.67 ± 4.45 / 63.78 ± 2.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.55 ± 0.70 / 67.56 ± 0.60</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.58 ± 0.85 / 22.14 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.12 ± 0.98 / 44.50 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">11.70 ± 2.42 / 32.05 ± 1.90</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>nvidia/mistral-nemo-minitron-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8414</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,161 ± 676 / 1,247 ± 481</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="nl ner">60.11 ± 1.96 / 37.17 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.12 ± 1.15 / 29.33 ± 1.27</td> <!-- Dutch Social -->
   <td class="nl la">32.68 ± 1.80 / 64.15 ± 1.14</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 17.43 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.01 ± 0.11 / 11.65 ± 0.13</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">41.00 ± 1.29 / 55.62 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">39.20 ± 2.23 / 53.01 ± 1.79</td> <!-- HellaSwag-nl -->
   <td>14.1.1</td> <!-- CoNLL-nl version -->
   <td>14.1.1</td> <!-- Dutch Social version -->
   <td>14.1.1</td> <!-- ScaLA-nl version -->
   <td>14.1.1</td> <!-- SQuAD-nl version -->
   <td>14.1.1</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.1</td> <!-- MMLU-nl version -->
   <td>14.1.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="nl ner">49.25 ± 2.57 / 36.48 ± 2.14</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.45 ± 1.76 / 39.66 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">11.87 ± 2.68 / 47.32 ± 3.85</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 1.44 / 67.04 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.96 / 16.74 ± 0.86</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">21.52 ± 1.18 / 40.76 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">22.32 ± 2.02 / 39.89 ± 1.82</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.59 ± 0.56 / 18.45 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.19 ± 1.26 / 39.24 ± 1.03</td> <!-- MMLU-nl -->
   <td class="nl reason">11.42 ± 1.29 / 32.50 ± 1.10</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="nl ner">51.31 ± 2.32 / 42.95 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.66 ± 0.74 / 18.22 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.12 ± 0.86 / 44.36 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">13.99 ± 2.04 / 34.45 ± 1.89</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.2.0</td> <!-- MMLU-nl version -->
   <td>12.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="nl ner">60.72 ± 2.14 / 45.52 ± 2.46</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.38 ± 1.62 / 29.91 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">10.96 ± 1.47 / 47.97 ± 3.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.20 ± 0.91 / 61.75 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.23 ± 0.96 / 16.22 ± 0.74</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">15.26 ± 0.67 / 35.76 ± 0.34</td> <!-- MMLU-nl -->
   <td class="nl reason">4.03 ± 0.90 / 27.17 ± 0.73</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.97 / 16.55 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.06 ± 0.77 / 44.08 ± 0.51</td> <!-- MMLU-nl -->
   <td class="nl reason">14.26 ± 1.48 / 35.14 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,804 ± 1,045 / 1,220 ± 392</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="nl ner">33.92 ± 3.43 / 28.63 ± 2.42</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.39 ± 1.64 / 41.03 ± 1.87</td> <!-- Dutch Social -->
   <td class="nl la">6.75 ± 2.55 / 41.28 ± 2.37</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.57 ± 1.03 / 69.39 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.49 ± 0.90 / 16.13 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.66 ± 0.67 / 42.68 ± 0.55</td> <!-- MMLU-nl -->
   <td class="nl reason">4.78 ± 1.80 / 27.19 ± 1.20</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="nl ner">51.18 ± 1.62 / 35.45 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.23 ± 2.84 / 19.38 ± 4.37</td> <!-- Dutch Social -->
   <td class="nl la">1.99 ± 2.56 / 34.69 ± 1.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.66 ± 1.25 / 65.31 ± 1.06</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.81 ± 1.16 / 15.41 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.03 ± 1.02 / 45.90 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">23.64 ± 1.21 / 42.59 ± 0.96</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/GEITje-7B-ultra-sft (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,979 ± 1,044 / 1,724 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="nl ner">39.41 ± 2.93 / 30.59 ± 1.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.00 ± 3.04 / 35.01 ± 3.72</td> <!-- Dutch Social -->
   <td class="nl la">16.10 ± 2.34 / 52.05 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.02 ± 0.97 / 65.63 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.74 ± 0.43 / 20.32 ± 0.57</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.80 ± 0.75 / 42.85 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">12.49 ± 2.15 / 33.04 ± 2.08</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="nl ner">54.56 ± 2.96 / 37.86 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.43 ± 1.27 / 24.23 ± 0.94</td> <!-- Dutch Social -->
   <td class="nl la">10.99 ± 2.55 / 50.46 ± 4.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.91 ± 1.08 / 66.78 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.88 ± 1.41 / 12.36 ± 1.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.12 ± 1.17 / 43.50 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">10.65 ± 1.55 / 31.51 ± 1.52</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="nl ner">42.52 ± 3.31 / 33.08 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.91 ± 1.71 / 35.24 ± 2.62</td> <!-- Dutch Social -->
   <td class="nl la">0.69 ± 2.82 / 36.10 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.95 ± 1.18 / 66.87 ± 1.37</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.71 ± 0.60 / 17.04 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.93 ± 1.42 / 40.35 ± 1.23</td> <!-- MMLU-nl -->
   <td class="nl reason">24.42 ± 1.73 / 42.26 ± 1.49</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.24</td> <!-- ScandEval rank -->
   <td class="nl ner">47.40 ± 3.29 / 33.11 ± 2.04</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.98 / 30.71 ± 1.89</td> <!-- Dutch Social -->
   <td class="nl la">3.10 ± 1.93 / 34.24 ± 0.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.53 ± 1.48 / 68.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.27 ± 2.04 / 16.54 ± 1.58</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.18 ± 0.87 / 46.04 ± 0.54</td> <!-- MMLU-nl -->
   <td class="nl reason">10.34 ± 1.08 / 32.08 ± 1.06</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.92 ± 0.61 / 70.24 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.58 ± 1.13 / 16.33 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.36 ± 1.12 / 37.44 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">6.68 ± 1.82 / 29.30 ± 1.02</td> <!-- HellaSwag-nl -->
   <td>9.2.0</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.2.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="nl ner">35.74 ± 3.22 / 31.74 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.90 ± 1.59 / 14.17 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.20 ± 1.53 / 41.49 ± 1.08</td> <!-- MMLU-nl -->
   <td class="nl reason">13.11 ± 1.85 / 33.86 ± 1.69</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.30</td> <!-- ScandEval rank -->
   <td class="nl ner">48.24 ± 2.28 / 40.24 ± 1.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.37 ± 1.34 / 33.54 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">10.73 ± 1.76 / 48.26 ± 4.65</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.83 ± 1.16 / 65.28 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.32 ± 0.90 / 18.12 ± 1.06</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.72 ± 1.25 / 24.90 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.47 ± 0.87 / 24.28 ± 0.68</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="nl ner">35.30 ± 3.76 / 33.68 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.67 ± 2.21 / 31.30 ± 4.51</td> <!-- Dutch Social -->
   <td class="nl la">1.76 ± 2.37 / 47.60 ± 1.68</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.05 ± 1.68 / 55.38 ± 1.66</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.15 ± 1.54 / 14.60 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">6.24 ± 1.54 / 29.02 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl reason">0.47 ± 1.20 / 24.89 ± 0.59</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="nl ner">46.95 ± 2.32 / 36.13 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.34 ± 2.10 / 19.37 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">3.46 ± 1.91 / 41.32 ± 3.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.07 ± 0.89 / 68.14 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.31 ± 0.64 / 17.24 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">18.21 ± 0.70 / 37.51 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">9.03 ± 1.04 / 29.35 ± 0.77</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="nl ner">48.53 ± 3.89 / 38.20 ± 2.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.15 ± 1.55 / 22.01 ± 1.44</td> <!-- Dutch Social -->
   <td class="nl la">4.88 ± 2.27 / 38.78 ± 3.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.38 ± 0.93 / 56.09 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.56 ± 1.09 / 15.20 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.38 ± 1.06 / 29.60 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">2.69 ± 0.56 / 25.85 ± 0.33</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="nl ner">39.24 ± 2.43 / 24.25 ± 1.34</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.25 ± 1.28 / 18.15 ± 3.08</td> <!-- Dutch Social -->
   <td class="nl la">11.48 ± 1.02 / 52.86 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.18 ± 0.98 / 65.58 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.55 ± 0.28 / 15.78 ± 0.39</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.37 ± 0.76 / 32.35 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">9.13 ± 1.17 / 27.27 ± 0.70</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="nl ner">50.88 ± 3.41 / 39.51 ± 3.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.39 ± 1.50 / 30.05 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">3.31 ± 1.19 / 37.97 ± 4.40</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.44 ± 1.06 / 58.85 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.50 ± 2.95 / 10.11 ± 2.12</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">9.22 ± 0.79 / 31.06 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">4.45 ± 1.38 / 28.26 ± 1.08</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="nl ner">24.44 ± 1.62 / 25.02 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.40 ± 2.14 / 40.21 ± 2.51</td> <!-- Dutch Social -->
   <td class="nl la">4.85 ± 2.01 / 49.10 ± 2.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">39.83 ± 1.08 / 52.69 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.89 ± 1.27 / 13.01 ± 0.47</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">4.38 ± 1.45 / 27.07 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl reason">1.95 ± 0.83 / 24.88 ± 0.71</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="nl ner">22.63 ± 4.98 / 22.71 ± 2.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.11 ± 1.55 / 28.07 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">8.04 ± 1.79 / 48.95 ± 2.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.39 ± 2.14 / 65.22 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.90 ± 1.04 / 17.09 ± 0.93</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.76 ± 0.76 / 41.67 ± 0.80</td> <!-- MMLU-nl -->
   <td class="nl reason">8.50 ± 1.32 / 30.16 ± 1.11</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="nl ner">36.61 ± 3.37 / 31.91 ± 2.20</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.77 ± 1.80 / 25.31 ± 1.42</td> <!-- Dutch Social -->
   <td class="nl la">3.52 ± 2.07 / 35.34 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.51 ± 0.97 / 70.33 ± 0.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.50 ± 5.78 / 15.01 ± 1.59</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.90 ± 1.44 / 35.20 ± 1.09</td> <!-- MMLU-nl -->
   <td class="nl reason">7.26 ± 1.56 / 29.91 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,136 ± 558 / 942 ± 290</td> <!-- Model inference speed -->
   <td class="rank">3.53</td> <!-- ScandEval rank -->
   <td class="nl ner">33.73 ± 2.02 / 30.41 ± 1.57</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.45 ± 1.77 / 22.28 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">3.78 ± 2.04 / 50.30 ± 1.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">43.60 ± 1.46 / 58.94 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.44 / 16.25 ± 0.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.67 ± 1.39 / 34.95 ± 1.02</td> <!-- MMLU-nl -->
   <td class="nl reason">11.51 ± 0.68 / 33.35 ± 0.60</td> <!-- HellaSwag-nl -->
   <td>13.2.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.2.0</td> <!-- ScaLA-nl version -->
   <td>13.2.0</td> <!-- SQuAD-nl version -->
   <td>13.2.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.2.0</td> <!-- MMLU-nl version -->
   <td>13.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="nl ner">42.01 ± 2.06 / 37.16 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.15 ± 1.70 / 32.55 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">1.11 ± 2.15 / 36.71 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.04 ± 1.61 / 53.75 ± 1.10</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.72 ± 1.05 / 12.47 ± 0.62</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.71 ± 0.69 / 38.01 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.98 ± 1.11 / 28.05 ± 1.00</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="nl ner">37.39 ± 3.37 / 32.77 ± 1.97</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.51 ± 1.57 / 19.22 ± 1.72</td> <!-- Dutch Social -->
   <td class="nl la">3.11 ± 0.88 / 50.54 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.60 ± 1.28 / 61.06 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.63 ± 1.86 / 12.27 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.52 ± 1.25 / 35.34 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">6.60 ± 1.13 / 29.30 ± 0.97</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.49 ± 1.37 / 47.34 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.24 ± 0.86 / 15.62 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.41 ± 1.15 / 27.75 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">0.15 ± 0.98 / 25.59 ± 0.57</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="nl ner">42.35 ± 2.49 / 29.29 ± 1.66</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.78 ± 0.93 / 8.63 ± 0.29</td> <!-- Dutch Social -->
   <td class="nl la">-0.02 ± 1.29 / 38.46 ± 1.55</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.61 ± 1.96 / 59.25 ± 1.42</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.32 ± 0.26 / 16.11 ± 0.29</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.59 ± 0.65 / 34.74 ± 0.52</td> <!-- MMLU-nl -->
   <td class="nl reason">11.78 ± 1.60 / 32.91 ± 0.98</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.0.4</td> <!-- Dutch Social version -->
   <td>14.0.4</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,964 ± 2,255 / 1,299 ± 433</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="nl ner">30.60 ± 2.69 / 26.10 ± 1.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.26 ± 1.54 / 37.96 ± 2.44</td> <!-- Dutch Social -->
   <td class="nl la">1.04 ± 1.52 / 45.97 ± 3.20</td> <!-- ScaLA-nl -->
   <td class="nl rc">39.69 ± 1.18 / 50.12 ± 0.89</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.20 ± 1.00 / 13.03 ± 0.49</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.10 ± 1.04 / 26.02 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.52 ± 0.72 / 23.98 ± 0.59</td> <!-- HellaSwag-nl -->
   <td>13.2.0</td> <!-- CoNLL-nl version -->
   <td>13.2.0</td> <!-- Dutch Social version -->
   <td>13.2.0</td> <!-- ScaLA-nl version -->
   <td>13.2.0</td> <!-- SQuAD-nl version -->
   <td>13.2.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.2.0</td> <!-- MMLU-nl version -->
   <td>13.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="nl ner">32.45 ± 2.17 / 30.83 ± 2.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.03 ± 2.08 / 34.16 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">5.58 ± 1.32 / 44.79 ± 3.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.18 ± 1.19 / 61.82 ± 1.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.96 ± 0.80 / 14.66 ± 0.48</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.53 ± 1.10 / 25.95 ± 1.10</td> <!-- MMLU-nl -->
   <td class="nl reason">1.04 ± 0.74 / 25.13 ± 0.68</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="nl ner">38.85 ± 3.77 / 32.18 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.99 ± 8.25 / 12.75 ± 2.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.97 ± 0.92 / 32.28 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">1.45 ± 1.15 / 24.79 ± 0.52</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.70</td> <!-- ScandEval rank -->
   <td class="nl ner">36.58 ± 3.88 / 33.82 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.32 ± 1.30 / 24.04 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">4.01 ± 2.01 / 36.03 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.81 ± 0.81 / 63.87 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.24 ± 1.79 / 10.76 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.24 ± 1.06 / 31.02 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">6.75 ± 0.83 / 28.50 ± 0.84</td> <!-- HellaSwag-nl -->
   <td>12.10.8</td> <!-- CoNLL-nl version -->
   <td>12.10.8</td> <!-- Dutch Social version -->
   <td>12.10.8</td> <!-- ScaLA-nl version -->
   <td>12.10.8</td> <!-- SQuAD-nl version -->
   <td>12.10.8</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="nl ner">16.90 ± 4.91 / 17.38 ± 4.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.61 ± 2.22 / 13.67 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.94 ± 0.50 / 31.87 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">3.29 ± 0.95 / 26.85 ± 0.49</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="nl ner">24.15 ± 5.73 / 26.49 ± 4.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.31 ± 1.56 / 20.06 ± 1.06</td> <!-- Dutch Social -->
   <td class="nl la">1.60 ± 1.71 / 41.51 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.08 ± 1.76 / 49.32 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.43 ± 1.17 / 14.57 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.04 ± 1.28 / 26.56 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">3.70 ± 1.54 / 26.98 ± 1.26</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="nl ner">23.44 ± 5.09 / 25.00 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.91 ± 0.99 / 12.65 ± 0.41</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">12.11 ± 0.90 / 33.62 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.41 ± 1.13 / 29.73 ± 0.82</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Tweeties/tweety-7b-dutch-v24a (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7391</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,971 ± 423 / 1,351 ± 410</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="nl ner">35.83 ± 3.06 / 29.15 ± 2.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.47 ± 2.51 / 40.41 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">16.81 ± 3.31 / 53.38 ± 5.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 14.18 ± 0.38</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.61 ± 0.65 / 9.48 ± 0.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.21 ± 1.63 / 37.93 ± 1.39</td> <!-- MMLU-nl -->
   <td class="nl reason">5.94 ± 1.54 / 28.98 ± 0.98</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="nl ner">31.84 ± 3.39 / 28.66 ± 1.77</td> <!-- CoNLL-nl -->
   <td class="nl sent">1.56 ± 3.25 / 28.78 ± 2.60</td> <!-- Dutch Social -->
   <td class="nl la">5.05 ± 1.34 / 43.99 ± 4.14</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.55 ± 0.77 / 48.56 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.35 ± 1.16 / 13.63 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.39 ± 0.96 / 34.55 ± 0.65</td> <!-- MMLU-nl -->
   <td class="nl reason">4.57 ± 0.96 / 27.42 ± 0.73</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">3.86</td> <!-- ScandEval rank -->
   <td class="nl ner">22.84 ± 5.42 / 25.11 ± 3.52</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.60 ± 2.12 / 29.94 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">2.55 ± 1.41 / 40.88 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.33 ± 1.19 / 48.35 ± 1.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.31 ± 1.50 / 13.08 ± 0.51</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.32 ± 0.71 / 35.65 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">3.87 ± 1.02 / 27.14 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="nl ner">18.66 ± 4.43 / 17.56 ± 4.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.36 ± 0.81 / 11.72 ± 0.73</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.09 ± 1.13 / 25.90 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">1.44 ± 1.12 / 26.50 ± 0.68</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="nl ner">36.74 ± 3.36 / 32.36 ± 1.39</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 2.44 / 34.17 ± 2.59</td> <!-- Dutch Social -->
   <td class="nl la">3.01 ± 1.94 / 46.03 ± 4.19</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.32 ± 1.55 / 40.73 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.76 ± 1.36 / 10.67 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.67 ± 1.15 / 24.89 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.30 ± 1.01 / 23.52 ± 0.38</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="nl ner">31.13 ± 3.71 / 29.34 ± 2.26</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.24 ± 2.08 / 29.45 ± 4.63</td> <!-- Dutch Social -->
   <td class="nl la">1.23 ± 1.73 / 44.71 ± 3.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.13 ± 0.85 / 39.28 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="nl summ">56.85 ± 0.66 / 11.52 ± 0.17</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.79 ± 1.11 / 26.12 ± 0.72</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.63 ± 1.13 / 23.93 ± 0.71</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1385</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,808 ± 2,183 / 1,289 ± 428</td> <!-- Model inference speed -->
   <td class="rank">3.98</td> <!-- ScandEval rank -->
   <td class="nl ner">12.76 ± 7.37 / 14.65 ± 5.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.35 ± 1.70 / 31.57 ± 6.23</td> <!-- Dutch Social -->
   <td class="nl la">0.69 ± 1.52 / 44.03 ± 3.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.71 ± 0.79 / 47.08 ± 1.12</td> <!-- SQuAD-nl -->
   <td class="nl summ">56.45 ± 1.86 / 12.01 ± 0.44</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.05 ± 0.51 / 24.48 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.85 ± 0.88 / 23.82 ± 0.73</td> <!-- HellaSwag-nl -->
   <td>13.2.0</td> <!-- CoNLL-nl version -->
   <td>13.2.0</td> <!-- Dutch Social version -->
   <td>13.2.0</td> <!-- ScaLA-nl version -->
   <td>13.2.0</td> <!-- SQuAD-nl version -->
   <td>13.2.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.2.0</td> <!-- MMLU-nl version -->
   <td>13.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.03</td> <!-- ScandEval rank -->
   <td class="nl ner">11.66 ± 6.46 / 15.15 ± 4.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">55.00 ± 1.73 / 11.21 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.56 ± 0.64 / 34.17 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">5.89 ± 0.82 / 29.17 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="nl ner">28.30 ± 3.90 / 28.67 ± 3.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.40 ± 2.03 / 10.34 ± 0.54</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.44 ± 0.51 / 29.86 ± 0.35</td> <!-- MMLU-nl -->
   <td class="nl reason">1.70 ± 1.42 / 26.04 ± 0.91</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="nl ner">37.37 ± 2.22 / 30.45 ± 2.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.55 ± 1.82 / 23.90 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">0.05 ± 1.35 / 35.78 ± 2.30</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.81 ± 1.54 / 46.37 ± 1.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.22 ± 0.39 / 8.61 ± 0.17</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.92 ± 1.04 / 27.22 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">0.16 ± 0.55 / 25.29 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="nl ner">22.03 ± 4.43 / 19.22 ± 3.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.25 ± 2.95 / 26.57 ± 3.31</td> <!-- Dutch Social -->
   <td class="nl la">1.46 ± 1.83 / 42.29 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.76 ± 1.92 / 52.60 ± 1.99</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.56 ± 1.45 / 10.34 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.46 ± 1.05 / 28.09 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.58 ± 0.81 / 23.58 ± 0.50</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="nl ner">23.58 ± 4.08 / 26.01 ± 4.43</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 3.56 / 33.04 ± 3.49</td> <!-- Dutch Social -->
   <td class="nl la">1.79 ± 1.38 / 40.53 ± 3.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.11 ± 2.05 / 35.07 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">53.77 ± 3.32 / 10.12 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.41 ± 0.68 / 24.81 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.45 ± 0.84 / 25.39 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">4.12</td> <!-- ScandEval rank -->
   <td class="nl ner">38.22 ± 3.45 / 35.62 ± 3.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.99 ± 3.86 / 29.17 ± 2.70</td> <!-- Dutch Social -->
   <td class="nl la">1.85 ± 1.45 / 40.34 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">27.77 ± 1.34 / 36.19 ± 1.60</td> <!-- SQuAD-nl -->
   <td class="nl summ">49.31 ± 4.05 / 8.77 ± 1.00</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-1.45 ± 0.89 / 24.35 ± 0.73</td> <!-- MMLU-nl -->
   <td class="nl reason">0.83 ± 0.92 / 26.03 ± 0.51</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>tiiuae/Falcon3-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1669</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,270 ± 2,690 / 1,434 ± 437</td> <!-- Model inference speed -->
   <td class="rank">4.15</td> <!-- ScandEval rank -->
   <td class="nl ner">28.25 ± 3.03 / 25.24 ± 2.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.73 ± 1.83 / 15.20 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">0.76 ± 1.10 / 33.57 ± 0.34</td> <!-- ScaLA-nl -->
   <td class="nl rc">19.08 ± 2.27 / 28.16 ± 2.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.20 ± 1.38 / 10.23 ± 0.61</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.45 ± 0.96 / 28.87 ± 0.86</td> <!-- MMLU-nl -->
   <td class="nl reason">2.34 ± 1.16 / 26.19 ± 0.80</td> <!-- HellaSwag-nl -->
   <td>14.1.2</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.1.2</td> <!-- SQuAD-nl version -->
   <td>14.1.2</td> <!-- Wiki-Lingua-NL version -->
   <td>14.1.2</td> <!-- MMLU-nl version -->
   <td>14.1.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="nl ner">22.50 ± 2.27 / 24.09 ± 2.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.04 ± 1.51 / 18.08 ± 2.09</td> <!-- Dutch Social -->
   <td class="nl la">-0.61 ± 1.30 / 46.51 ± 2.55</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.96 ± 1.55 / 35.73 ± 1.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">56.55 ± 3.05 / 13.22 ± 1.01</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.27 ± 1.29 / 24.94 ± 0.91</td> <!-- MMLU-nl -->
   <td class="nl reason">1.47 ± 0.79 / 25.75 ± 0.39</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="nl ner">20.95 ± 2.02 / 25.63 ± 1.96</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.84 ± 1.76 / 27.74 ± 5.49</td> <!-- Dutch Social -->
   <td class="nl la">-1.50 ± 1.30 / 34.07 ± 0.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.67 ± 1.77 / 30.14 ± 1.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">53.89 ± 2.61 / 10.53 ± 0.37</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.45 ± 1.59 / 24.24 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.31 ± 1.39 / 23.58 ± 0.40</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="nl ner">15.68 ± 5.54 / 22.21 ± 5.42</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.73 ± 2.20 / 27.67 ± 4.00</td> <!-- Dutch Social -->
   <td class="nl la">0.63 ± 1.05 / 43.48 ± 2.98</td> <!-- ScaLA-nl -->
   <td class="nl rc">19.73 ± 1.42 / 27.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.53 ± 2.03 / 9.14 ± 0.47</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.30 ± 0.75 / 24.43 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.36 ± 0.85 / 24.09 ± 0.49</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32896</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="nl ner">22.95 ± 1.99 / 23.05 ± 1.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.40 ± 1.70 / 22.89 ± 4.81</td> <!-- Dutch Social -->
   <td class="nl la">3.12 ± 1.51 / 45.58 ± 4.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.40 ± 1.73 / 32.09 ± 1.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.36 ± 2.03 / 9.96 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.48 ± 0.81 / 24.57 ± 0.67</td> <!-- MMLU-nl -->
   <td class="nl reason">1.28 ± 1.03 / 26.62 ± 0.80</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="nl ner">18.70 ± 5.76 / 19.58 ± 4.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.70 ± 1.69 / 17.91 ± 1.48</td> <!-- Dutch Social -->
   <td class="nl la">2.19 ± 2.08 / 45.43 ± 3.44</td> <!-- ScaLA-nl -->
   <td class="nl rc">38.08 ± 1.07 / 48.44 ± 1.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.79 ± 0.51 / 7.59 ± 0.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.65 ± 1.39 / 25.05 ± 1.02</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.02 ± 0.92 / 24.75 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="nl ner">21.32 ± 2.14 / 22.20 ± 2.65</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.37 ± 2.16 / 18.06 ± 2.83</td> <!-- Dutch Social -->
   <td class="nl la">-0.19 ± 1.24 / 41.66 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">9.38 ± 1.20 / 15.78 ± 1.26</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.94 ± 2.76 / 7.92 ± 0.87</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.33 ± 1.58 / 24.74 ± 1.23</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.81 ± 0.69 / 24.22 ± 0.67</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="nl ner">22.58 ± 5.05 / 26.82 ± 3.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.92 ± 2.71 / 19.51 ± 4.22</td> <!-- Dutch Social -->
   <td class="nl la">-1.27 ± 1.85 / 41.38 ± 3.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">6.64 ± 1.96 / 11.74 ± 1.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.43 ± 0.37 / 7.83 ± 0.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.56 ± 1.27 / 24.38 ± 0.98</td> <!-- MMLU-nl -->
   <td class="nl reason">0.29 ± 1.06 / 25.10 ± 0.83</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="nl ner">24.47 ± 2.03 / 26.64 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.57 ± 2.03 / 16.42 ± 3.18</td> <!-- Dutch Social -->
   <td class="nl la">-2.03 ± 1.35 / 39.46 ± 4.09</td> <!-- ScaLA-nl -->
   <td class="nl rc">10.18 ± 1.78 / 17.17 ± 2.17</td> <!-- SQuAD-nl -->
   <td class="nl summ">44.43 ± 2.69 / 7.67 ± 0.47</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.11 ± 1.20 / 24.70 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.01 ± 1.24 / 24.56 ± 0.75</td> <!-- HellaSwag-nl -->
   <td>14.0.4</td> <!-- CoNLL-nl version -->
   <td>14.1.2</td> <!-- Dutch Social version -->
   <td>14.1.2</td> <!-- ScaLA-nl version -->
   <td>14.0.4</td> <!-- SQuAD-nl version -->
   <td>14.0.4</td> <!-- Wiki-Lingua-NL version -->
   <td>14.0.4</td> <!-- MMLU-nl version -->
   <td>14.0.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.64</td> <!-- ScandEval rank -->
   <td class="nl ner">15.82 ± 3.13 / 16.46 ± 2.61</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.62 ± 1.55 / 16.18 ± 1.88</td> <!-- Dutch Social -->
   <td class="nl la">1.16 ± 1.38 / 34.30 ± 1.27</td> <!-- ScaLA-nl -->
   <td class="nl rc">3.25 ± 1.17 / 5.89 ± 0.97</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.82 ± 3.44 / 9.74 ± 0.58</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.36 ± 1.10 / 25.96 ± 0.81</td> <!-- MMLU-nl -->
   <td class="nl reason">0.34 ± 1.33 / 25.40 ± 0.83</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.66</td> <!-- ScandEval rank -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.95 ± 1.17 / 9.87 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 5.43 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.14 ± 0.15 / 10.07 ± 0.16</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.11 ± 0.64 / 24.32 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.13 ± 0.82 / 23.60 ± 0.33</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="nl ner">17.49 ± 2.94 / 18.59 ± 2.66</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.01 ± 1.88 / 15.88 ± 1.32</td> <!-- Dutch Social -->
   <td class="nl la">-0.02 ± 0.15 / 34.86 ± 2.12</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.53 ± 0.36 / 3.23 ± 0.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.46 ± 1.93 / 9.47 ± 0.33</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.33 ± 0.71 / 25.12 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.10 ± 0.85 / 24.87 ± 0.65</td> <!-- HellaSwag-nl -->
   <td>13.1.0</td> <!-- CoNLL-nl version -->
   <td>13.1.0</td> <!-- Dutch Social version -->
   <td>13.1.0</td> <!-- ScaLA-nl version -->
   <td>13.1.0</td> <!-- SQuAD-nl version -->
   <td>13.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.1.0</td> <!-- MMLU-nl version -->
   <td>13.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.95</td> <!-- ScandEval rank -->
   <td class="nl ner">3.80 ± 1.23 / 4.24 ± 1.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.97 ± 1.50 / 13.00 ± 2.52</td> <!-- Dutch Social -->
   <td class="nl la">-0.37 ± 0.55 / 33.40 ± 0.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.40 ± 0.25 / 2.98 ± 0.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.25 ± 4.22 / 6.15 ± 1.03</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.98 ± 0.91 / 24.82 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.05 ± 1.07 / 24.51 ± 0.88</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.02</td> <!-- ScandEval rank -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 8.62 ± 0.30</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 0.01 ± 0.00</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.74 ± 0.57 / 0.22 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.32 ± 0.67 / 24.79 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">1.73 ± 1.07 / 26.61 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.33</td> <!-- ScandEval rank -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">30.20 ± 0.68 / 2.14 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.45 ± 0.84 / 24.91 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.56 ± 0.80 / 23.53 ± 0.49</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>11.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>12.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>11.0.0</td> <!-- MMLU-nl version -->
   <td>11.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/dutch-nlg.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
