---
layout: leaderboard
title: English NLG 🇬🇧
---

<center>Last updated: 06/01/2025 11:01:15 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlg" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English reading comprehension - Exact Match / F1-score">SQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English summarization - BERTScore / ROUGE-L">CNN-DailyMail</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English knowledge - Matthews Correlation Coefficient / Accuracy">MMLU</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-en">CoNLL-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SST5">SST5 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-en">ScaLA-en version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD">SQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CNN-DailyMail">CNN-DailyMail version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU">MMLU version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag">HellaSwag version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128254</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.20</td> <!-- ScandEval rank -->
   <td class="en ner">81.79 ± 1.39 / 65.51 ± 4.16</td> <!-- CoNLL-en -->
   <td class="en sent">67.55 ± 2.34 / 74.04 ± 1.80</td> <!-- SST5 -->
   <td class="en la">51.21 ± 4.96 / 75.11 ± 2.42</td> <!-- ScaLA-en -->
   <td class="en rc">66.60 ± 1.45 / 84.48 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">68.80 ± 0.43 / 21.84 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">81.71 ± 1.12 / 86.29 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">89.91 ± 1.81 / 92.38 ± 1.34</td> <!-- HellaSwag -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.2</td> <!-- MMLU version -->
   <td>12.10.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.21</td> <!-- ScandEval rank -->
   <td class="en ner">78.06 ± 2.73 / 70.76 ± 3.80</td> <!-- CoNLL-en -->
   <td class="en sent">69.06 ± 2.20 / 76.04 ± 1.60</td> <!-- SST5 -->
   <td class="en la">55.76 ± 3.84 / 76.34 ± 1.44</td> <!-- ScaLA-en -->
   <td class="en rc">67.35 ± 1.98 / 85.76 ± 0.77</td> <!-- SQuAD -->
   <td class="en summ">70.54 ± 0.24 / 26.98 ± 0.49</td> <!-- CNN-DailyMail -->
   <td class="en know">72.27 ± 2.36 / 78.75 ± 1.88</td> <!-- MMLU -->
   <td class="en reason">91.51 ± 2.15 / 93.59 ± 1.62</td> <!-- HellaSwag -->
   <td>12.2.0</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.2.0</td> <!-- ScaLA-en version -->
   <td>12.2.0</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128127</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="en ner">83.48 ± 1.52 / 75.51 ± 2.26</td> <!-- CoNLL-en -->
   <td class="en sent">62.74 ± 2.04 / 71.28 ± 1.46</td> <!-- SST5 -->
   <td class="en la">46.56 ± 3.35 / 71.13 ± 1.97</td> <!-- ScaLA-en -->
   <td class="en rc">65.41 ± 1.96 / 84.78 ± 0.68</td> <!-- SQuAD -->
   <td class="en summ">67.64 ± 0.97 / 20.90 ± 0.92</td> <!-- CNN-DailyMail -->
   <td class="en know">78.55 ± 1.82 / 83.91 ± 1.34</td> <!-- MMLU -->
   <td class="en reason">91.34 ± 1.66 / 93.48 ± 1.27</td> <!-- HellaSwag -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.2</td> <!-- SST5 version -->
   <td>12.10.2</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.2</td> <!-- MMLU version -->
   <td>12.10.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.31</td> <!-- ScandEval rank -->
   <td class="en ner">79.06 ± 2.34 / 74.41 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">65.53 ± 2.61 / 68.71 ± 2.08</td> <!-- SST5 -->
   <td class="en la">46.28 ± 4.01 / 72.38 ± 2.33</td> <!-- ScaLA-en -->
   <td class="en rc">75.20 ± 1.68 / 86.90 ± 1.14</td> <!-- SQuAD -->
   <td class="en summ">69.10 ± 0.33 / 21.34 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">72.64 ± 1.98 / 79.49 ± 1.48</td> <!-- MMLU -->
   <td class="en reason">77.49 ± 4.78 / 82.50 ± 3.93</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">637 ± 306 / 92 ± 31</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="en ner">81.23 ± 1.31 / 72.72 ± 1.69</td> <!-- CoNLL-en -->
   <td class="en sent">63.46 ± 1.00 / 69.35 ± 1.28</td> <!-- SST5 -->
   <td class="en la">46.45 ± 4.58 / 72.89 ± 2.30</td> <!-- ScaLA-en -->
   <td class="en rc">57.64 ± 1.26 / 81.53 ± 0.66</td> <!-- SQuAD -->
   <td class="en summ">68.71 ± 0.14 / 20.56 ± 0.22</td> <!-- CNN-DailyMail -->
   <td class="en know">80.09 ± 2.42 / 85.12 ± 1.78</td> <!-- MMLU -->
   <td class="en reason">86.91 ± 1.20 / 90.04 ± 0.92</td> <!-- HellaSwag -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   <td>14.0.3</td> <!-- CNN-DailyMail version -->
   <td>14.0.3</td> <!-- MMLU version -->
   <td>14.0.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8448</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="en ner">62.40 ± 1.15 / 59.91 ± 1.66</td> <!-- CoNLL-en -->
   <td class="en sent">68.68 ± 0.87 / 73.25 ± 0.48</td> <!-- SST5 -->
   <td class="en la">54.17 ± 2.59 / 76.02 ± 1.67</td> <!-- ScaLA-en -->
   <td class="en rc">66.96 ± 1.51 / 84.76 ± 0.92</td> <!-- SQuAD -->
   <td class="en summ">69.79 ± 0.37 / 26.34 ± 0.54</td> <!-- CNN-DailyMail -->
   <td class="en know">68.71 ± 0.72 / 76.45 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">81.25 ± 1.38 / 85.84 ± 1.05</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="en ner">69.50 ± 1.14 / 63.41 ± 0.77</td> <!-- CoNLL-en -->
   <td class="en sent">70.01 ± 0.93 / 59.77 ± 0.59</td> <!-- SST5 -->
   <td class="en la">41.35 ± 2.01 / 70.11 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">76.79 ± 0.43 / 89.35 ± 0.19</td> <!-- SQuAD -->
   <td class="en summ">71.16 ± 0.12 / 29.84 ± 0.23</td> <!-- CNN-DailyMail -->
   <td class="en know">51.95 ± 0.84 / 63.78 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">90.94 ± 0.54 / 93.17 ± 0.41</td> <!-- HellaSwag -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   <td>12.5.3</td> <!-- CNN-DailyMail version -->
   <td>12.5.3</td> <!-- MMLU version -->
   <td>12.5.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/gemma-2-27b-it-FP8-Dynamic (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">28411</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,633 ± 1,236 / 777 ± 220</td> <!-- Model inference speed -->
   <td class="rank">1.44</td> <!-- ScandEval rank -->
   <td class="en ner">81.06 ± 0.87 / 75.22 ± 1.31</td> <!-- CoNLL-en -->
   <td class="en sent">68.92 ± 1.04 / 72.90 ± 0.74</td> <!-- SST5 -->
   <td class="en la">49.06 ± 1.46 / 72.52 ± 0.82</td> <!-- ScaLA-en -->
   <td class="en rc">61.27 ± 1.63 / 81.48 ± 0.86</td> <!-- SQuAD -->
   <td class="en summ">68.00 ± 0.09 / 22.45 ± 0.14</td> <!-- CNN-DailyMail -->
   <td class="en know">67.84 ± 0.73 / 75.85 ± 0.56</td> <!-- MMLU -->
   <td class="en reason">78.26 ± 0.99 / 83.56 ± 0.79</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-LaserChat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,915 ± 502 / 301 ± 157</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="en ner">72.31 ± 0.95 / 58.34 ± 1.84</td> <!-- CoNLL-en -->
   <td class="en sent">69.64 ± 0.81 / 74.44 ± 0.54</td> <!-- SST5 -->
   <td class="en la">46.08 ± 1.45 / 71.39 ± 0.74</td> <!-- ScaLA-en -->
   <td class="en rc">72.23 ± 1.24 / 86.80 ± 0.57</td> <!-- SQuAD -->
   <td class="en summ">70.23 ± 0.09 / 26.49 ± 0.30</td> <!-- CNN-DailyMail -->
   <td class="en know">48.37 ± 1.21 / 61.11 ± 0.87</td> <!-- MMLU -->
   <td class="en reason">76.87 ± 0.79 / 82.49 ± 0.62</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4349</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="en ner">72.38 ± 1.28 / 66.44 ± 1.74</td> <!-- CoNLL-en -->
   <td class="en sent">60.98 ± 2.19 / 68.64 ± 2.17</td> <!-- SST5 -->
   <td class="en la">43.12 ± 5.21 / 70.12 ± 2.87</td> <!-- ScaLA-en -->
   <td class="en rc">74.50 ± 3.41 / 86.22 ± 1.70</td> <!-- SQuAD -->
   <td class="en summ">71.63 ± 0.35 / 26.83 ± 0.78</td> <!-- CNN-DailyMail -->
   <td class="en know">54.29 ± 1.91 / 65.78 ± 1.33</td> <!-- MMLU -->
   <td class="en reason">74.35 ± 4.59 / 80.47 ± 3.64</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.52</td> <!-- ScandEval rank -->
   <td class="en ner">81.30 ± 1.35 / 76.64 ± 1.77</td> <!-- CoNLL-en -->
   <td class="en sent">66.18 ± 2.04 / 72.85 ± 1.27</td> <!-- SST5 -->
   <td class="en la">38.10 ± 2.32 / 68.58 ± 1.40</td> <!-- ScaLA-en -->
   <td class="en rc">53.31 ± 3.61 / 77.76 ± 1.59</td> <!-- SQuAD -->
   <td class="en summ">70.35 ± 0.46 / 26.71 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">72.39 ± 1.41 / 79.30 ± 1.05</td> <!-- MMLU -->
   <td class="en reason">83.86 ± 2.24 / 87.81 ± 1.71</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">33017</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="en ner">71.83 ± 1.48 / 65.37 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.99 ± 3.04 / 69.81 ± 1.86</td> <!-- SST5 -->
   <td class="en la">39.97 ± 3.89 / 69.38 ± 1.87</td> <!-- ScaLA-en -->
   <td class="en rc">64.42 ± 3.17 / 80.97 ± 1.54</td> <!-- SQuAD -->
   <td class="en summ">71.27 ± 0.50 / 25.32 ± 0.64</td> <!-- CNN-DailyMail -->
   <td class="en know">64.27 ± 3.04 / 73.20 ± 2.27</td> <!-- MMLU -->
   <td class="en reason">77.60 ± 4.02 / 82.85 ± 3.10</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">784 ± 310 / 95 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="en ner">77.38 ± 1.61 / 66.97 ± 2.42</td> <!-- CoNLL-en -->
   <td class="en sent">66.75 ± 2.50 / 73.93 ± 1.51</td> <!-- SST5 -->
   <td class="en la">52.43 ± 3.69 / 74.46 ± 2.17</td> <!-- ScaLA-en -->
   <td class="en rc">41.03 ± 6.90 / 67.96 ± 4.99</td> <!-- SQuAD -->
   <td class="en summ">68.73 ± 0.21 / 20.97 ± 0.36</td> <!-- CNN-DailyMail -->
   <td class="en know">66.63 ± 2.82 / 74.92 ± 2.08</td> <!-- MMLU -->
   <td class="en reason">79.95 ± 1.44 / 84.69 ± 1.09</td> <!-- HellaSwag -->
   <td>14.0.0</td> <!-- CoNLL-en version -->
   <td>14.0.0</td> <!-- SST5 version -->
   <td>14.0.0</td> <!-- ScaLA-en version -->
   <td>14.0.0</td> <!-- SQuAD version -->
   <td>14.0.1</td> <!-- CNN-DailyMail version -->
   <td>14.0.1</td> <!-- MMLU version -->
   <td>14.0.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/FC-SauerkrautLM-7b-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,160 ± 514 / 668 ± 256</td> <!-- Model inference speed -->
   <td class="rank">1.56</td> <!-- ScandEval rank -->
   <td class="en ner">70.15 ± 0.85 / 60.29 ± 2.28</td> <!-- CoNLL-en -->
   <td class="en sent">69.36 ± 0.87 / 67.37 ± 0.89</td> <!-- SST5 -->
   <td class="en la">37.09 ± 2.04 / 68.05 ± 1.30</td> <!-- ScaLA-en -->
   <td class="en rc">77.39 ± 1.14 / 89.74 ± 0.41</td> <!-- SQuAD -->
   <td class="en summ">69.72 ± 0.17 / 25.82 ± 0.35</td> <!-- CNN-DailyMail -->
   <td class="en know">50.10 ± 1.05 / 62.63 ± 0.79</td> <!-- MMLU -->
   <td class="en reason">77.27 ± 0.64 / 82.91 ± 0.49</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8448</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.56</td> <!-- ScandEval rank -->
   <td class="en ner">58.07 ± 2.46 / 51.39 ± 2.35</td> <!-- CoNLL-en -->
   <td class="en sent">68.40 ± 1.17 / 71.79 ± 0.65</td> <!-- SST5 -->
   <td class="en la">51.58 ± 2.03 / 74.57 ± 1.48</td> <!-- ScaLA-en -->
   <td class="en rc">62.03 ± 1.62 / 81.91 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">69.72 ± 0.42 / 25.66 ± 0.38</td> <!-- CNN-DailyMail -->
   <td class="en know">63.99 ± 0.76 / 72.84 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">75.87 ± 1.74 / 81.61 ± 1.30</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024256</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="en ner">75.24 ± 0.84 / 67.78 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">63.05 ± 1.41 / 70.34 ± 0.52</td> <!-- SST5 -->
   <td class="en la">44.75 ± 2.73 / 71.43 ± 1.71</td> <!-- ScaLA-en -->
   <td class="en rc">67.70 ± 1.57 / 83.88 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">70.56 ± 0.58 / 25.57 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">57.55 ± 1.00 / 68.02 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">67.97 ± 1.89 / 75.51 ± 1.48</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">908 ± 303 / 96 ± 36</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
   <td class="en ner">75.80 ± 0.83 / 52.95 ± 1.04</td> <!-- CoNLL-en -->
   <td class="en sent">61.65 ± 2.17 / 71.46 ± 1.72</td> <!-- SST5 -->
   <td class="en la">47.74 ± 4.29 / 73.28 ± 2.23</td> <!-- ScaLA-en -->
   <td class="en rc">56.98 ± 1.46 / 79.90 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">68.60 ± 0.16 / 20.57 ± 0.28</td> <!-- CNN-DailyMail -->
   <td class="en know">63.18 ± 2.47 / 72.23 ± 1.82</td> <!-- MMLU -->
   <td class="en reason">77.31 ± 1.71 / 82.54 ± 1.37</td> <!-- HellaSwag -->
   <td>14.0.1</td> <!-- CoNLL-en version -->
   <td>14.0.1</td> <!-- SST5 version -->
   <td>14.0.1</td> <!-- ScaLA-en version -->
   <td>14.0.1</td> <!-- SQuAD version -->
   <td>14.0.3</td> <!-- CNN-DailyMail version -->
   <td>14.0.3</td> <!-- MMLU version -->
   <td>14.0.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,629 ± 573 / 262 ± 149</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="en ner">72.77 ± 1.02 / 57.29 ± 1.58</td> <!-- CoNLL-en -->
   <td class="en sent">70.12 ± 0.78 / 74.54 ± 0.50</td> <!-- SST5 -->
   <td class="en la">44.68 ± 0.97 / 71.05 ± 0.52</td> <!-- ScaLA-en -->
   <td class="en rc">57.17 ± 2.60 / 80.36 ± 1.40</td> <!-- SQuAD -->
   <td class="en summ">69.32 ± 0.08 / 23.63 ± 0.24</td> <!-- CNN-DailyMail -->
   <td class="en know">47.17 ± 1.25 / 60.21 ± 0.92</td> <!-- MMLU -->
   <td class="en reason">77.25 ± 0.73 / 82.76 ± 0.56</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">436 ± 152 / 57 ± 21</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="en ner">42.40 ± 2.22 / 34.09 ± 2.02</td> <!-- CoNLL-en -->
   <td class="en sent">65.24 ± 2.14 / 72.51 ± 1.77</td> <!-- SST5 -->
   <td class="en la">44.59 ± 4.02 / 71.93 ± 2.06</td> <!-- ScaLA-en -->
   <td class="en rc">62.94 ± 1.37 / 82.84 ± 0.53</td> <!-- SQuAD -->
   <td class="en summ">68.33 ± 0.17 / 20.27 ± 0.29</td> <!-- CNN-DailyMail -->
   <td class="en know">78.80 ± 2.08 / 84.14 ± 1.57</td> <!-- MMLU -->
   <td class="en reason">82.60 ± 1.54 / 86.60 ± 1.25</td> <!-- HellaSwag -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   <td>14.0.3</td> <!-- CNN-DailyMail version -->
   <td>14.0.3</td> <!-- MMLU version -->
   <td>14.0.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt-mixtral (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="en ner">67.43 ± 0.90 / 60.40 ± 1.08</td> <!-- CoNLL-en -->
   <td class="en sent">68.55 ± 1.35 / 69.63 ± 0.98</td> <!-- SST5 -->
   <td class="en la">39.75 ± 2.28 / 69.19 ± 1.17</td> <!-- ScaLA-en -->
   <td class="en rc">65.93 ± 2.77 / 82.86 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">70.90 ± 0.34 / 25.88 ± 0.75</td> <!-- CNN-DailyMail -->
   <td class="en know">59.14 ± 1.02 / 69.28 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">57.88 ± 2.80 / 67.75 ± 2.34</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en rc">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.18 / 24.41 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">43.69 ± 3.59 / 57.38 ± 3.06</td> <!-- MMLU -->
   <td class="en reason">75.60 ± 3.04 / 81.48 ± 2.31</td> <!-- HellaSwag -->
   <td>0.0.0</td> <!-- CoNLL-en version -->
   <td>0.0.0</td> <!-- SST5 version -->
   <td>0.0.0</td> <!-- ScaLA-en version -->
   <td>0.0.0</td> <!-- SQuAD version -->
   <td>0.0.0</td> <!-- CNN-DailyMail version -->
   <td>0.0.0</td> <!-- MMLU version -->
   <td>0.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">912 ± 238 / 179 ± 70</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="en ner">72.40 ± 0.80 / 65.83 ± 1.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.46 ± 2.10 / 69.49 ± 1.15</td> <!-- SST5 -->
   <td class="en la">35.86 ± 7.94 / 65.20 ± 6.98</td> <!-- ScaLA-en -->
   <td class="en rc">68.42 ± 1.21 / 83.97 ± 0.74</td> <!-- SQuAD -->
   <td class="en summ">69.38 ± 0.48 / 24.96 ± 0.47</td> <!-- CNN-DailyMail -->
   <td class="en know">53.42 ± 0.91 / 64.98 ± 0.74</td> <!-- MMLU -->
   <td class="en reason">78.36 ± 2.31 / 83.62 ± 1.78</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8448</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="en ner">50.90 ± 2.39 / 44.74 ± 1.46</td> <!-- CoNLL-en -->
   <td class="en sent">68.91 ± 0.89 / 70.46 ± 1.23</td> <!-- SST5 -->
   <td class="en la">43.79 ± 3.15 / 71.10 ± 1.74</td> <!-- ScaLA-en -->
   <td class="en rc">69.17 ± 1.55 / 84.25 ± 1.13</td> <!-- SQuAD -->
   <td class="en summ">69.67 ± 0.46 / 25.26 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">61.34 ± 0.86 / 70.95 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">62.23 ± 3.55 / 70.69 ± 3.11</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,118 ± 302 / 184 ± 63</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="en ner">66.17 ± 1.74 / 57.76 ± 1.30</td> <!-- CoNLL-en -->
   <td class="en sent">68.03 ± 0.81 / 69.65 ± 1.18</td> <!-- SST5 -->
   <td class="en la">39.76 ± 2.51 / 69.54 ± 1.18</td> <!-- ScaLA-en -->
   <td class="en rc">71.21 ± 1.53 / 84.07 ± 0.91</td> <!-- SQuAD -->
   <td class="en summ">69.30 ± 0.10 / 23.68 ± 0.29</td> <!-- CNN-DailyMail -->
   <td class="en know">49.99 ± 0.60 / 62.20 ± 0.47</td> <!-- MMLU -->
   <td class="en reason">52.45 ± 1.74 / 61.79 ± 1.58</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,018 ± 326 / 189 ± 73</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="en ner">67.33 ± 1.57 / 53.00 ± 0.88</td> <!-- CoNLL-en -->
   <td class="en sent">68.67 ± 0.74 / 66.23 ± 0.49</td> <!-- SST5 -->
   <td class="en la">31.18 ± 1.63 / 65.23 ± 0.69</td> <!-- ScaLA-en -->
   <td class="en rc">68.33 ± 2.04 / 84.26 ± 1.04</td> <!-- SQuAD -->
   <td class="en summ">72.23 ± 0.14 / 30.67 ± 0.16</td> <!-- CNN-DailyMail -->
   <td class="en know">49.41 ± 1.09 / 62.03 ± 0.82</td> <!-- MMLU -->
   <td class="en reason">58.93 ± 1.50 / 68.81 ± 1.21</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,005 ± 330 / 196 ± 74</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="en ner">76.95 ± 0.95 / 72.47 ± 0.82</td> <!-- CoNLL-en -->
   <td class="en sent">68.12 ± 0.92 / 72.48 ± 0.53</td> <!-- SST5 -->
   <td class="en la">34.34 ± 3.37 / 65.84 ± 1.59</td> <!-- ScaLA-en -->
   <td class="en rc">47.88 ± 3.37 / 76.21 ± 1.69</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.25 / 26.30 ± 0.35</td> <!-- CNN-DailyMail -->
   <td class="en know">56.62 ± 0.49 / 67.29 ± 0.39</td> <!-- MMLU -->
   <td class="en reason">69.03 ± 1.19 / 76.69 ± 0.89</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4352</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="en ner">55.51 ± 1.48 / 50.61 ± 1.37</td> <!-- CoNLL-en -->
   <td class="en sent">68.74 ± 0.81 / 58.25 ± 0.31</td> <!-- SST5 -->
   <td class="en la">40.81 ± 3.66 / 69.94 ± 1.98</td> <!-- ScaLA-en -->
   <td class="en rc">72.33 ± 2.68 / 84.50 ± 1.61</td> <!-- SQuAD -->
   <td class="en summ">67.71 ± 0.08 / 23.57 ± 0.14</td> <!-- CNN-DailyMail -->
   <td class="en know">48.36 ± 0.95 / 61.21 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">68.50 ± 0.63 / 76.04 ± 0.47</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-HerO (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 467 / 744 ± 232</td> <!-- Model inference speed -->
   <td class="rank">1.78</td> <!-- ScandEval rank -->
   <td class="en ner">69.26 ± 2.17 / 57.48 ± 2.92</td> <!-- CoNLL-en -->
   <td class="en sent">68.63 ± 2.65 / 73.31 ± 1.74</td> <!-- SST5 -->
   <td class="en la">29.87 ± 3.02 / 63.64 ± 1.60</td> <!-- ScaLA-en -->
   <td class="en rc">60.92 ± 2.44 / 80.40 ± 1.26</td> <!-- SQuAD -->
   <td class="en summ">70.20 ± 0.33 / 26.15 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">49.51 ± 2.34 / 61.84 ± 1.70</td> <!-- MMLU -->
   <td class="en reason">71.47 ± 2.32 / 78.36 ± 1.73</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,007 ± 316 / 162 ± 45</td> <!-- Model inference speed -->
   <td class="rank">1.81</td> <!-- ScandEval rank -->
   <td class="en ner">75.02 ± 1.31 / 69.47 ± 1.18</td> <!-- CoNLL-en -->
   <td class="en sent">67.64 ± 1.12 / 71.04 ± 1.17</td> <!-- SST5 -->
   <td class="en la">32.29 ± 3.05 / 64.85 ± 2.07</td> <!-- ScaLA-en -->
   <td class="en rc">54.84 ± 2.22 / 79.10 ± 1.10</td> <!-- SQuAD -->
   <td class="en summ">69.28 ± 0.17 / 25.48 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">53.77 ± 1.03 / 64.91 ± 0.80</td> <!-- MMLU -->
   <td class="en reason">57.64 ± 1.55 / 67.29 ± 1.30</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="en ner">72.80 ± 1.65 / 64.88 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.76 ± 2.53 / 71.14 ± 1.90</td> <!-- SST5 -->
   <td class="en la">28.37 ± 4.76 / 62.85 ± 3.04</td> <!-- ScaLA-en -->
   <td class="en rc">64.70 ± 2.69 / 81.80 ± 1.41</td> <!-- SQuAD -->
   <td class="en summ">71.04 ± 0.42 / 25.68 ± 0.52</td> <!-- CNN-DailyMail -->
   <td class="en know">47.00 ± 2.21 / 60.12 ± 1.58</td> <!-- MMLU -->
   <td class="en reason">61.56 ± 2.97 / 70.27 ± 2.27</td> <!-- HellaSwag -->
   <td>12.7.0</td> <!-- CoNLL-en version -->
   <td>12.7.0</td> <!-- SST5 version -->
   <td>12.7.0</td> <!-- ScaLA-en version -->
   <td>12.7.0</td> <!-- SQuAD version -->
   <td>12.7.0</td> <!-- CNN-DailyMail version -->
   <td>12.7.0</td> <!-- MMLU version -->
   <td>12.7.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat-Sft-Bf16 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,413 ± 463 / 700 ± 220</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="en ner">67.52 ± 1.19 / 59.09 ± 2.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.10 ± 1.92 / 70.11 ± 0.80</td> <!-- SST5 -->
   <td class="en la">37.75 ± 2.52 / 67.53 ± 1.75</td> <!-- ScaLA-en -->
   <td class="en rc">64.88 ± 1.60 / 82.23 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">68.45 ± 0.22 / 21.67 ± 0.52</td> <!-- CNN-DailyMail -->
   <td class="en know">47.66 ± 0.96 / 60.75 ± 0.72</td> <!-- MMLU -->
   <td class="en reason">63.35 ± 1.62 / 72.16 ± 1.31</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,610 ± 751 / 176 ± 66</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="en ner">69.86 ± 2.10 / 62.68 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">66.76 ± 0.72 / 68.58 ± 0.72</td> <!-- SST5 -->
   <td class="en la">30.96 ± 2.46 / 61.29 ± 3.61</td> <!-- ScaLA-en -->
   <td class="en rc">71.39 ± 2.20 / 84.24 ± 1.55</td> <!-- SQuAD -->
   <td class="en summ">67.93 ± 0.44 / 22.00 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">52.47 ± 0.85 / 64.25 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">43.95 ± 3.26 / 57.04 ± 2.74</td> <!-- HellaSwag -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.11.0</td> <!-- SST5 version -->
   <td>12.11.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en rc">52.69 ± 2.21 / 76.37 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">70.55 ± 0.73 / 26.32 ± 0.97</td> <!-- CNN-DailyMail -->
   <td class="en know">51.74 ± 1.82 / 63.44 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">71.96 ± 2.38 / 78.87 ± 1.66</td> <!-- HellaSwag -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>9.3.2</td> <!-- CNN-DailyMail version -->
   <td>9.3.2</td> <!-- MMLU version -->
   <td>9.3.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>neuralmagic/Sparse-Llama-3.1-8B-2of4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,996 ± 817 / 284 ± 96</td> <!-- Model inference speed -->
   <td class="rank">1.89</td> <!-- ScandEval rank -->
   <td class="en ner">59.28 ± 0.97 / 55.81 ± 1.40</td> <!-- CoNLL-en -->
   <td class="en sent">68.49 ± 0.77 / 58.77 ± 0.44</td> <!-- SST5 -->
   <td class="en la">21.95 ± 3.10 / 49.75 ± 3.85</td> <!-- ScaLA-en -->
   <td class="en rc">78.16 ± 2.12 / 87.44 ± 1.32</td> <!-- SQuAD -->
   <td class="en summ">69.54 ± 0.30 / 26.96 ± 0.56</td> <!-- CNN-DailyMail -->
   <td class="en know">46.35 ± 0.95 / 59.11 ± 0.72</td> <!-- MMLU -->
   <td class="en reason">60.61 ± 4.03 / 67.80 ± 3.65</td> <!-- HellaSwag -->
   <td>13.2.0</td> <!-- CoNLL-en version -->
   <td>13.2.0</td> <!-- SST5 version -->
   <td>13.2.0</td> <!-- ScaLA-en version -->
   <td>13.2.0</td> <!-- SQuAD version -->
   <td>13.2.0</td> <!-- CNN-DailyMail version -->
   <td>13.2.0</td> <!-- MMLU version -->
   <td>13.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">1.89</td> <!-- ScandEval rank -->
   <td class="en ner">70.62 ± 0.90 / 58.92 ± 2.15</td> <!-- CoNLL-en -->
   <td class="en sent">67.78 ± 1.03 / 72.29 ± 0.47</td> <!-- SST5 -->
   <td class="en la">30.99 ± 2.94 / 62.20 ± 2.56</td> <!-- ScaLA-en -->
   <td class="en rc">49.56 ± 2.85 / 76.72 ± 1.15</td> <!-- SQuAD -->
   <td class="en summ">70.76 ± 0.56 / 24.95 ± 1.03</td> <!-- CNN-DailyMail -->
   <td class="en know">44.11 ± 4.39 / 57.76 ± 3.36</td> <!-- MMLU -->
   <td class="en reason">69.20 ± 2.71 / 76.75 ± 2.06</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="en ner">64.09 ± 0.96 / 49.92 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">46.77 ± 4.36 / 60.99 ± 2.15</td> <!-- SST5 -->
   <td class="en la">31.62 ± 2.25 / 63.73 ± 1.79</td> <!-- ScaLA-en -->
   <td class="en rc">71.25 ± 0.83 / 85.72 ± 0.57</td> <!-- SQuAD -->
   <td class="en summ">69.54 ± 0.57 / 24.79 ± 0.89</td> <!-- CNN-DailyMail -->
   <td class="en know">57.66 ± 1.17 / 68.22 ± 0.88</td> <!-- MMLU -->
   <td class="en reason">72.26 ± 0.86 / 79.10 ± 0.64</td> <!-- HellaSwag -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.0</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>cstr/Spaetzle-v8-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,980 ± 1,031 / 1,714 ± 552</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="en ner">69.40 ± 1.47 / 54.63 ± 3.27</td> <!-- CoNLL-en -->
   <td class="en sent">65.39 ± 2.32 / 73.11 ± 1.62</td> <!-- SST5 -->
   <td class="en la">26.69 ± 3.88 / 62.82 ± 2.19</td> <!-- ScaLA-en -->
   <td class="en rc">49.74 ± 2.61 / 75.27 ± 0.99</td> <!-- SQuAD -->
   <td class="en summ">71.02 ± 0.71 / 25.90 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">52.23 ± 1.23 / 63.71 ± 0.98</td> <!-- MMLU -->
   <td class="en reason">74.61 ± 2.55 / 80.66 ± 1.88</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,446 ± 354 / 295 ± 100</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en rc">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
   <td class="en summ">69.11 ± 0.31 / 23.70 ± 0.53</td> <!-- CNN-DailyMail -->
   <td class="en know">47.74 ± 1.26 / 60.63 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">34.96 ± 4.19 / 49.62 ± 3.28</td> <!-- HellaSwag -->
   <td>9.1.2</td> <!-- CoNLL-en version -->
   <td>9.1.2</td> <!-- SST5 version -->
   <td>9.1.2</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>11.0.0</td> <!-- CNN-DailyMail version -->
   <td>9.2.0</td> <!-- MMLU version -->
   <td>9.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,335 ± 338 / 260 ± 88</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="en ner">66.31 ± 2.09 / 58.68 ± 1.95</td> <!-- CoNLL-en -->
   <td class="en sent">64.30 ± 0.65 / 69.26 ± 0.50</td> <!-- SST5 -->
   <td class="en la">28.18 ± 3.96 / 58.97 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en rc">70.38 ± 3.51 / 82.95 ± 2.38</td> <!-- SQuAD -->
   <td class="en summ">67.90 ± 0.49 / 21.54 ± 0.57</td> <!-- CNN-DailyMail -->
   <td class="en know">52.54 ± 0.88 / 64.26 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">41.19 ± 4.40 / 54.78 ± 3.62</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
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
   <td class="en rc">73.50 ± 1.67 / 84.26 ± 1.30</td> <!-- SQuAD -->
   <td class="en summ">69.02 ± 0.55 / 23.87 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">47.13 ± 1.24 / 60.08 ± 0.92</td> <!-- MMLU -->
   <td class="en reason">35.88 ± 4.42 / 49.95 ± 3.87</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,364 ± 343 / 266 ± 90</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">61.02 ± 2.74 / 55.65 ± 2.55</td> <!-- CoNLL-en -->
   <td class="en sent">67.29 ± 0.80 / 70.81 ± 0.84</td> <!-- SST5 -->
   <td class="en la">30.10 ± 5.12 / 62.99 ± 4.71</td> <!-- ScaLA-en -->
   <td class="en rc">73.59 ± 1.75 / 84.31 ± 1.35</td> <!-- SQuAD -->
   <td class="en summ">69.04 ± 0.56 / 23.86 ± 0.77</td> <!-- CNN-DailyMail -->
   <td class="en know">47.63 ± 1.17 / 60.45 ± 0.88</td> <!-- MMLU -->
   <td class="en reason">35.63 ± 4.21 / 49.72 ± 3.73</td> <!-- HellaSwag -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4352</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="en ner">57.78 ± 1.91 / 50.30 ± 2.29</td> <!-- CoNLL-en -->
   <td class="en sent">67.81 ± 1.00 / 61.89 ± 1.51</td> <!-- SST5 -->
   <td class="en la">22.81 ± 2.71 / 60.07 ± 2.49</td> <!-- ScaLA-en -->
   <td class="en rc">72.90 ± 1.16 / 83.67 ± 0.66</td> <!-- SQuAD -->
   <td class="en summ">67.33 ± 0.41 / 22.76 ± 0.60</td> <!-- CNN-DailyMail -->
   <td class="en know">37.80 ± 0.99 / 53.52 ± 0.78</td> <!-- MMLU -->
   <td class="en reason">67.23 ± 0.96 / 75.34 ± 0.74</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="en ner">69.19 ± 2.03 / 55.64 ± 3.53</td> <!-- CoNLL-en -->
   <td class="en sent">63.77 ± 2.55 / 71.13 ± 1.83</td> <!-- SST5 -->
   <td class="en la">28.43 ± 3.97 / 62.28 ± 1.86</td> <!-- ScaLA-en -->
   <td class="en rc">44.39 ± 2.68 / 71.79 ± 1.25</td> <!-- SQuAD -->
   <td class="en summ">69.77 ± 0.76 / 24.60 ± 1.13</td> <!-- CNN-DailyMail -->
   <td class="en know">46.53 ± 2.54 / 59.53 ± 1.87</td> <!-- MMLU -->
   <td class="en reason">71.36 ± 3.95 / 78.36 ± 2.91</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,121 ± 288 / 205 ± 68</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="en ner">56.16 ± 3.59 / 51.12 ± 2.58</td> <!-- CoNLL-en -->
   <td class="en sent">68.27 ± 0.53 / 60.37 ± 0.57</td> <!-- SST5 -->
   <td class="en la">23.88 ± 2.16 / 60.87 ± 1.62</td> <!-- ScaLA-en -->
   <td class="en rc">74.23 ± 1.31 / 85.11 ± 0.73</td> <!-- SQuAD -->
   <td class="en summ">72.14 ± 0.13 / 29.83 ± 0.23</td> <!-- CNN-DailyMail -->
   <td class="en know">33.04 ± 1.30 / 49.51 ± 0.98</td> <!-- MMLU -->
   <td class="en reason">55.10 ± 1.39 / 64.78 ± 1.34</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">973 ± 251 / 174 ± 59</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="en ner">55.76 ± 2.15 / 52.69 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">66.89 ± 1.09 / 69.50 ± 0.96</td> <!-- SST5 -->
   <td class="en la">36.47 ± 2.07 / 67.43 ± 1.29</td> <!-- ScaLA-en -->
   <td class="en rc">67.55 ± 1.46 / 80.25 ± 1.22</td> <!-- SQuAD -->
   <td class="en summ">66.51 ± 0.93 / 21.81 ± 1.31</td> <!-- CNN-DailyMail -->
   <td class="en know">46.22 ± 1.20 / 59.52 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">52.23 ± 2.04 / 61.87 ± 1.91</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4352</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="en ner">61.97 ± 1.74 / 54.58 ± 1.53</td> <!-- CoNLL-en -->
   <td class="en sent">67.54 ± 1.33 / 66.16 ± 1.54</td> <!-- SST5 -->
   <td class="en la">31.70 ± 2.00 / 65.43 ± 1.09</td> <!-- ScaLA-en -->
   <td class="en rc">59.78 ± 1.66 / 78.74 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">68.61 ± 0.41 / 24.36 ± 0.58</td> <!-- CNN-DailyMail -->
   <td class="en know">39.82 ± 0.91 / 54.59 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">57.51 ± 0.92 / 67.67 ± 0.71</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="en ner">60.90 ± 3.17 / 53.69 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">66.54 ± 1.42 / 69.26 ± 0.83</td> <!-- SST5 -->
   <td class="en la">23.60 ± 3.72 / 57.65 ± 4.08</td> <!-- ScaLA-en -->
   <td class="en rc">75.14 ± 1.51 / 87.25 ± 0.61</td> <!-- SQuAD -->
   <td class="en summ">68.96 ± 0.53 / 25.60 ± 0.80</td> <!-- CNN-DailyMail -->
   <td class="en know">42.53 ± 0.85 / 56.25 ± 0.72</td> <!-- MMLU -->
   <td class="en reason">41.79 ± 3.18 / 54.82 ± 2.83</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.3.1</td> <!-- MMLU version -->
   <td>12.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="en ner">47.20 ± 3.34 / 41.96 ± 3.12</td> <!-- CoNLL-en -->
   <td class="en sent">63.88 ± 2.24 / 66.49 ± 0.81</td> <!-- SST5 -->
   <td class="en la">35.75 ± 2.65 / 66.41 ± 2.26</td> <!-- ScaLA-en -->
   <td class="en rc">69.40 ± 4.29 / 82.46 ± 2.86</td> <!-- SQuAD -->
   <td class="en summ">69.25 ± 0.80 / 24.32 ± 0.95</td> <!-- CNN-DailyMail -->
   <td class="en know">50.57 ± 1.00 / 61.48 ± 0.80</td> <!-- MMLU -->
   <td class="en reason">35.79 ± 4.89 / 46.37 ± 3.67</td> <!-- HellaSwag -->
   <td>12.9.1</td> <!-- CoNLL-en version -->
   <td>12.9.1</td> <!-- SST5 version -->
   <td>12.9.1</td> <!-- ScaLA-en version -->
   <td>12.9.1</td> <!-- SQuAD version -->
   <td>12.9.1</td> <!-- CNN-DailyMail version -->
   <td>12.9.1</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="en ner">68.44 ± 1.14 / 56.80 ± 2.31</td> <!-- CoNLL-en -->
   <td class="en sent">66.00 ± 1.41 / 70.47 ± 1.02</td> <!-- SST5 -->
   <td class="en la">32.04 ± 3.44 / 65.62 ± 1.88</td> <!-- ScaLA-en -->
   <td class="en rc">49.54 ± 3.13 / 75.26 ± 1.64</td> <!-- SQuAD -->
   <td class="en summ">69.23 ± 0.19 / 24.84 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">45.50 ± 0.74 / 58.96 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">46.50 ± 1.78 / 59.43 ± 1.44</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="en ner">55.45 ± 1.61 / 49.72 ± 1.27</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en rc">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
   <td class="en summ">68.67 ± 0.11 / 21.65 ± 0.21</td> <!-- CNN-DailyMail -->
   <td class="en know">39.82 ± 0.76 / 54.62 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">51.82 ± 1.03 / 63.79 ± 0.79</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-sonnet-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">193 ± 87 / 55 ± 19</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="en ner">82.11 ± 1.42 / 79.77 ± 1.03</td> <!-- CoNLL-en -->
   <td class="en sent">67.01 ± 2.34 / 71.49 ± 1.89</td> <!-- SST5 -->
   <td class="en la">51.09 ± 5.20 / 74.48 ± 2.70</td> <!-- ScaLA-en -->
   <td class="en rc">52.41 ± 1.56 / 77.79 ± 1.01</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.14 / 18.28 ± 0.26</td> <!-- CNN-DailyMail -->
   <td class="en know">26.14 ± 2.01 / 35.16 ± 1.54</td> <!-- MMLU -->
   <td class="en reason">13.56 ± 3.11 / 26.48 ± 1.71</td> <!-- HellaSwag -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.3</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   <td>14.0.3</td> <!-- CNN-DailyMail version -->
   <td>14.0.3</td> <!-- MMLU version -->
   <td>14.0.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="en ner">59.10 ± 1.87 / 51.31 ± 1.87</td> <!-- CoNLL-en -->
   <td class="en sent">68.41 ± 1.17 / 70.85 ± 0.74</td> <!-- SST5 -->
   <td class="en la">25.43 ± 4.22 / 60.79 ± 3.45</td> <!-- ScaLA-en -->
   <td class="en rc">71.89 ± 2.20 / 82.99 ± 1.78</td> <!-- SQuAD -->
   <td class="en summ">67.99 ± 0.41 / 22.12 ± 0.52</td> <!-- CNN-DailyMail -->
   <td class="en know">44.09 ± 1.21 / 56.37 ± 0.96</td> <!-- MMLU -->
   <td class="en reason">32.29 ± 4.57 / 45.16 ± 4.28</td> <!-- HellaSwag -->
   <td>12.5.3</td> <!-- CoNLL-en version -->
   <td>12.5.3</td> <!-- SST5 version -->
   <td>12.5.3</td> <!-- ScaLA-en version -->
   <td>12.5.3</td> <!-- SQuAD version -->
   <td>12.5.3</td> <!-- CNN-DailyMail version -->
   <td>12.5.3</td> <!-- MMLU version -->
   <td>12.5.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en rc">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
   <td class="en summ">69.62 ± 0.31 / 24.65 ± 0.44</td> <!-- CNN-DailyMail -->
   <td class="en know">38.40 ± 0.98 / 53.43 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">35.72 ± 1.56 / 49.69 ± 1.42</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,483 ± 321 / 379 ± 158</td> <!-- Model inference speed -->
   <td class="rank">2.10</td> <!-- ScandEval rank -->
   <td class="en ner">44.81 ± 2.07 / 39.51 ± 1.62</td> <!-- CoNLL-en -->
   <td class="en sent">62.54 ± 2.18 / 68.78 ± 1.18</td> <!-- SST5 -->
   <td class="en la">28.10 ± 4.55 / 62.46 ± 4.36</td> <!-- ScaLA-en -->
   <td class="en rc">71.71 ± 2.21 / 84.31 ± 1.69</td> <!-- SQuAD -->
   <td class="en summ">69.27 ± 0.77 / 25.38 ± 1.10</td> <!-- CNN-DailyMail -->
   <td class="en know">45.95 ± 0.80 / 59.04 ± 0.60</td> <!-- MMLU -->
   <td class="en reason">43.97 ± 1.97 / 56.43 ± 1.61</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en rc">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
   <td class="en summ">68.84 ± 0.52 / 24.99 ± 0.80</td> <!-- CNN-DailyMail -->
   <td class="en know">36.49 ± 0.82 / 52.02 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">38.09 ± 2.61 / 52.60 ± 2.19</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="en ner">58.56 ± 1.99 / 54.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en rc">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">67.27 ± 0.39 / 19.77 ± 0.31</td> <!-- CNN-DailyMail -->
   <td class="en know">38.68 ± 1.02 / 53.45 ± 0.74</td> <!-- MMLU -->
   <td class="en reason">47.47 ± 1.28 / 60.44 ± 1.02</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="en ner">68.75 ± 1.54 / 60.01 ± 1.57</td> <!-- CoNLL-en -->
   <td class="en sent">62.37 ± 1.68 / 67.79 ± 1.51</td> <!-- SST5 -->
   <td class="en la">25.07 ± 3.20 / 61.02 ± 2.86</td> <!-- ScaLA-en -->
   <td class="en rc">61.56 ± 1.18 / 80.11 ± 0.70</td> <!-- SQuAD -->
   <td class="en summ">69.40 ± 0.49 / 24.79 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">38.00 ± 0.83 / 52.95 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">42.14 ± 2.47 / 55.96 ± 1.93</td> <!-- HellaSwag -->
   <td>12.11.0</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.11.0</td> <!-- SQuAD version -->
   <td>12.11.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="en ner">56.07 ± 4.01 / 51.66 ± 3.99</td> <!-- CoNLL-en -->
   <td class="en sent">65.29 ± 1.43 / 69.38 ± 0.73</td> <!-- SST5 -->
   <td class="en la">25.78 ± 2.57 / 61.50 ± 2.24</td> <!-- ScaLA-en -->
   <td class="en rc">73.13 ± 4.05 / 83.85 ± 2.69</td> <!-- SQuAD -->
   <td class="en summ">68.76 ± 0.54 / 23.14 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">41.47 ± 0.94 / 55.81 ± 0.77</td> <!-- MMLU -->
   <td class="en reason">32.75 ± 3.47 / 48.17 ± 2.83</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>12.3.1</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.3.1</td> <!-- SQuAD version -->
   <td>12.3.1</td> <!-- CNN-DailyMail version -->
   <td>12.3.1</td> <!-- MMLU version -->
   <td>12.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="en ner">63.75 ± 2.50 / 59.28 ± 2.20</td> <!-- CoNLL-en -->
   <td class="en sent">61.85 ± 1.70 / 69.02 ± 0.76</td> <!-- SST5 -->
   <td class="en la">26.41 ± 4.93 / 59.67 ± 4.84</td> <!-- ScaLA-en -->
   <td class="en rc">73.48 ± 2.06 / 85.27 ± 1.15</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.58 / 22.39 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">38.04 ± 1.30 / 53.30 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">28.16 ± 3.07 / 44.80 ± 2.46</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2047</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,194 ± 687 / 650 ± 216</td> <!-- Model inference speed -->
   <td class="rank">2.17</td> <!-- ScandEval rank -->
   <td class="en ner">68.69 ± 1.08 / 58.53 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">66.77 ± 0.54 / 70.41 ± 0.88</td> <!-- SST5 -->
   <td class="en la">42.14 ± 2.29 / 70.53 ± 0.99</td> <!-- ScaLA-en -->
   <td class="en rc">63.71 ± 1.70 / 81.26 ± 1.09</td> <!-- SQuAD -->
   <td class="en summ">45.05 ± 10.76 / 15.91 ± 3.64</td> <!-- CNN-DailyMail -->
   <td class="en know">56.92 ± 0.88 / 67.56 ± 0.66</td> <!-- MMLU -->
   <td class="en reason">55.78 ± 0.98 / 65.88 ± 0.81</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8445</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="en ner">66.70 ± 0.99 / 61.08 ± 1.16</td> <!-- CoNLL-en -->
   <td class="en sent">55.62 ± 2.54 / 64.98 ± 2.03</td> <!-- SST5 -->
   <td class="en la">31.36 ± 2.63 / 65.21 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">72.58 ± 0.68 / 84.67 ± 0.91</td> <!-- SQuAD -->
   <td class="en summ">67.24 ± 0.71 / 21.99 ± 0.99</td> <!-- CNN-DailyMail -->
   <td class="en know">35.27 ± 1.22 / 50.12 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">32.54 ± 1.77 / 46.58 ± 1.66</td> <!-- HellaSwag -->
   <td>12.10.0</td> <!-- CoNLL-en version -->
   <td>12.10.0</td> <!-- SST5 version -->
   <td>12.10.0</td> <!-- ScaLA-en version -->
   <td>12.10.0</td> <!-- SQuAD version -->
   <td>12.10.0</td> <!-- CNN-DailyMail version -->
   <td>12.10.0</td> <!-- MMLU version -->
   <td>12.10.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,370 ± 416 / 711 ± 242</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en rc">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
   <td class="en summ">69.75 ± 0.63 / 24.71 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">34.93 ± 1.35 / 50.71 ± 1.00</td> <!-- MMLU -->
   <td class="en reason">44.91 ± 2.44 / 58.07 ± 1.93</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.2</td> <!-- MMLU version -->
   <td>9.3.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="en ner">56.90 ± 3.08 / 51.16 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en rc">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.63 ± 0.46 / 25.61 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">38.48 ± 1.10 / 53.32 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">27.67 ± 2.08 / 43.61 ± 2.08</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.3.1</td> <!-- MMLU version -->
   <td>12.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8448</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="en ner">44.36 ± 1.46 / 38.51 ± 1.53</td> <!-- CoNLL-en -->
   <td class="en sent">66.37 ± 1.35 / 67.64 ± 1.35</td> <!-- SST5 -->
   <td class="en la">34.69 ± 2.50 / 67.16 ± 1.29</td> <!-- ScaLA-en -->
   <td class="en rc">55.07 ± 1.73 / 78.88 ± 0.80</td> <!-- SQuAD -->
   <td class="en summ">68.09 ± 0.20 / 23.58 ± 0.33</td> <!-- CNN-DailyMail -->
   <td class="en know">42.89 ± 1.25 / 57.03 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">45.52 ± 0.68 / 58.39 ± 0.55</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="en ner">56.38 ± 2.95 / 50.80 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">66.04 ± 1.68 / 65.21 ± 1.48</td> <!-- SST5 -->
   <td class="en la">22.15 ± 3.57 / 57.71 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en rc">71.32 ± 1.41 / 83.70 ± 0.93</td> <!-- SQuAD -->
   <td class="en summ">68.13 ± 0.68 / 23.08 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">35.47 ± 1.23 / 50.47 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">29.25 ± 3.05 / 44.01 ± 2.75</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.0</td> <!-- SST5 version -->
   <td>12.5.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.5.0</td> <!-- MMLU version -->
   <td>12.5.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en rc">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
   <td class="en summ">69.95 ± 0.32 / 25.22 ± 0.33</td> <!-- CNN-DailyMail -->
   <td class="en know">30.47 ± 0.70 / 46.82 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">30.18 ± 1.87 / 45.85 ± 1.98</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="en ner">55.37 ± 2.94 / 51.08 ± 2.87</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en rc">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
   <td class="en summ">68.61 ± 0.55 / 23.48 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">37.04 ± 1.33 / 52.33 ± 1.02</td> <!-- MMLU -->
   <td class="en reason">23.54 ± 2.08 / 40.78 ± 1.59</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.2.0</td> <!-- MMLU version -->
   <td>12.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="en ner">52.79 ± 4.09 / 43.45 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">65.92 ± 1.02 / 70.47 ± 0.75</td> <!-- SST5 -->
   <td class="en la">16.74 ± 2.67 / 55.45 ± 3.35</td> <!-- ScaLA-en -->
   <td class="en rc">64.92 ± 2.84 / 80.88 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">65.50 ± 0.97 / 21.90 ± 0.40</td> <!-- CNN-DailyMail -->
   <td class="en know">33.84 ± 0.87 / 50.07 ± 0.67</td> <!-- MMLU -->
   <td class="en reason">49.84 ± 1.22 / 61.87 ± 1.03</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="en ner">72.76 ± 0.57 / 67.49 ± 0.90</td> <!-- CoNLL-en -->
   <td class="en sent">62.35 ± 1.68 / 67.34 ± 0.77</td> <!-- SST5 -->
   <td class="en la">21.57 ± 2.22 / 59.22 ± 1.69</td> <!-- ScaLA-en -->
   <td class="en rc">69.80 ± 3.60 / 81.37 ± 2.26</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.60 / 23.48 ± 0.91</td> <!-- CNN-DailyMail -->
   <td class="en know">25.63 ± 0.81 / 44.26 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">16.44 ± 1.84 / 36.73 ± 1.54</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4351</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,002 ± 95 / 416 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="en ner">72.64 ± 0.61 / 67.38 ± 0.91</td> <!-- CoNLL-en -->
   <td class="en sent">62.31 ± 1.79 / 67.31 ± 0.86</td> <!-- SST5 -->
   <td class="en la">22.38 ± 2.05 / 59.67 ± 1.50</td> <!-- ScaLA-en -->
   <td class="en rc">69.84 ± 3.57 / 81.40 ± 2.25</td> <!-- SQuAD -->
   <td class="en summ">67.71 ± 0.62 / 23.43 ± 0.95</td> <!-- CNN-DailyMail -->
   <td class="en know">25.41 ± 0.75 / 44.10 ± 0.58</td> <!-- MMLU -->
   <td class="en reason">16.50 ± 1.79 / 36.76 ± 1.44</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.5</td> <!-- MMLU version -->
   <td>12.10.5</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,136 ± 558 / 942 ± 290</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="en ner">53.21 ± 1.85 / 45.68 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">65.98 ± 1.15 / 64.68 ± 2.08</td> <!-- SST5 -->
   <td class="en la">7.26 ± 2.04 / 52.39 ± 1.92</td> <!-- ScaLA-en -->
   <td class="en rc">64.71 ± 1.95 / 79.37 ± 1.16</td> <!-- SQuAD -->
   <td class="en summ">68.81 ± 0.21 / 24.11 ± 0.23</td> <!-- CNN-DailyMail -->
   <td class="en know">36.50 ± 1.02 / 52.05 ± 0.77</td> <!-- MMLU -->
   <td class="en reason">46.95 ± 1.41 / 59.90 ± 1.18</td> <!-- HellaSwag -->
   <td>13.2.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.2.0</td> <!-- ScaLA-en version -->
   <td>13.2.0</td> <!-- SQuAD version -->
   <td>13.2.0</td> <!-- CNN-DailyMail version -->
   <td>13.2.0</td> <!-- MMLU version -->
   <td>13.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="en ner">49.44 ± 3.68 / 39.69 ± 2.34</td> <!-- CoNLL-en -->
   <td class="en sent">66.65 ± 1.04 / 65.72 ± 1.32</td> <!-- SST5 -->
   <td class="en la">12.56 ± 2.15 / 54.20 ± 3.42</td> <!-- ScaLA-en -->
   <td class="en rc">63.29 ± 4.61 / 75.62 ± 3.79</td> <!-- SQuAD -->
   <td class="en summ">66.38 ± 0.28 / 21.17 ± 0.41</td> <!-- CNN-DailyMail -->
   <td class="en know">32.06 ± 0.87 / 49.12 ± 0.61</td> <!-- MMLU -->
   <td class="en reason">58.21 ± 0.98 / 68.63 ± 0.74</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="en ner">59.09 ± 1.44 / 52.03 ± 1.96</td> <!-- CoNLL-en -->
   <td class="en sent">63.29 ± 1.29 / 67.82 ± 0.74</td> <!-- SST5 -->
   <td class="en la">13.50 ± 4.14 / 50.33 ± 5.61</td> <!-- ScaLA-en -->
   <td class="en rc">68.15 ± 2.21 / 81.12 ± 1.18</td> <!-- SQuAD -->
   <td class="en summ">67.73 ± 0.51 / 22.02 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">40.10 ± 0.68 / 54.53 ± 0.48</td> <!-- MMLU -->
   <td class="en reason">20.88 ± 2.25 / 39.75 ± 1.62</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="en ner">47.50 ± 1.70 / 41.85 ± 1.68</td> <!-- CoNLL-en -->
   <td class="en sent">64.69 ± 1.33 / 57.60 ± 0.63</td> <!-- SST5 -->
   <td class="en la">8.01 ± 1.97 / 51.78 ± 1.65</td> <!-- ScaLA-en -->
   <td class="en rc">71.81 ± 1.05 / 80.90 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.71 ± 0.11 / 27.72 ± 0.26</td> <!-- CNN-DailyMail -->
   <td class="en know">18.92 ± 0.73 / 38.74 ± 0.53</td> <!-- MMLU -->
   <td class="en reason">54.53 ± 0.89 / 65.79 ± 0.65</td> <!-- HellaSwag -->
   <td>12.10.8</td> <!-- CoNLL-en version -->
   <td>12.10.8</td> <!-- SST5 version -->
   <td>12.10.8</td> <!-- ScaLA-en version -->
   <td>12.10.8</td> <!-- SQuAD version -->
   <td>12.10.8</td> <!-- CNN-DailyMail version -->
   <td>12.10.8</td> <!-- MMLU version -->
   <td>12.10.8</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="en ner">72.59 ± 0.91 / 65.83 ± 1.30</td> <!-- CoNLL-en -->
   <td class="en sent">61.61 ± 1.45 / 67.09 ± 1.38</td> <!-- SST5 -->
   <td class="en la">18.37 ± 2.07 / 56.26 ± 2.62</td> <!-- ScaLA-en -->
   <td class="en rc">66.68 ± 3.56 / 78.95 ± 2.38</td> <!-- SQuAD -->
   <td class="en summ">68.41 ± 0.33 / 24.66 ± 0.47</td> <!-- CNN-DailyMail -->
   <td class="en know">24.14 ± 0.58 / 42.17 ± 0.33</td> <!-- MMLU -->
   <td class="en reason">14.42 ± 2.00 / 34.50 ± 1.81</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en rc">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
   <td class="en summ">68.82 ± 0.54 / 23.58 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">25.98 ± 0.90 / 42.52 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">11.77 ± 1.81 / 31.25 ± 1.99</td> <!-- HellaSwag -->
   <td>9.2.0</td> <!-- CoNLL-en version -->
   <td>9.2.0</td> <!-- SST5 version -->
   <td>9.2.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>9.2.0</td> <!-- MMLU version -->
   <td>9.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/phi-2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,472 ± 885 / 728 ± 239</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="en ner">49.16 ± 3.09 / 43.10 ± 2.58</td> <!-- CoNLL-en -->
   <td class="en sent">62.41 ± 1.51 / 67.24 ± 1.18</td> <!-- SST5 -->
   <td class="en la">12.31 ± 2.96 / 48.73 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en rc">75.79 ± 1.88 / 86.40 ± 1.10</td> <!-- SQuAD -->
   <td class="en summ">67.79 ± 0.51 / 23.29 ± 0.89</td> <!-- CNN-DailyMail -->
   <td class="en know">40.15 ± 1.11 / 54.65 ± 0.86</td> <!-- MMLU -->
   <td class="en reason">23.21 ± 2.87 / 39.96 ± 2.45</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.0.0</td> <!-- ScaLA-en version -->
   <td>12.0.0</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>12.0.0</td> <!-- MMLU version -->
   <td>12.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="en ner">41.02 ± 3.86 / 40.03 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">66.43 ± 0.78 / 57.25 ± 0.33</td> <!-- SST5 -->
   <td class="en la">5.17 ± 1.55 / 37.03 ± 2.40</td> <!-- ScaLA-en -->
   <td class="en rc">76.04 ± 0.97 / 85.31 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">70.28 ± 0.06 / 28.85 ± 0.17</td> <!-- CNN-DailyMail -->
   <td class="en know">34.92 ± 0.75 / 50.82 ± 0.73</td> <!-- MMLU -->
   <td class="en reason">18.73 ± 1.32 / 34.76 ± 0.91</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="en ner">53.39 ± 2.97 / 47.76 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">65.21 ± 1.35 / 65.73 ± 1.61</td> <!-- SST5 -->
   <td class="en la">12.63 ± 2.60 / 50.10 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en rc">65.74 ± 2.31 / 77.95 ± 1.84</td> <!-- SQuAD -->
   <td class="en summ">68.05 ± 0.54 / 24.11 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">31.65 ± 1.00 / 47.19 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">17.69 ± 2.71 / 35.94 ± 2.08</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="en ner">47.58 ± 2.41 / 39.52 ± 1.41</td> <!-- CoNLL-en -->
   <td class="en sent">66.78 ± 0.76 / 61.52 ± 0.99</td> <!-- SST5 -->
   <td class="en la">20.53 ± 3.83 / 58.47 ± 2.90</td> <!-- ScaLA-en -->
   <td class="en rc">58.07 ± 2.23 / 69.96 ± 1.63</td> <!-- SQuAD -->
   <td class="en summ">62.45 ± 5.62 / 19.60 ± 1.85</td> <!-- CNN-DailyMail -->
   <td class="en know">32.90 ± 0.96 / 49.16 ± 0.95</td> <!-- MMLU -->
   <td class="en reason">25.32 ± 2.12 / 42.50 ± 2.39</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="en ner">47.76 ± 2.72 / 44.84 ± 2.71</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 0.85 / 65.96 ± 2.20</td> <!-- SST5 -->
   <td class="en la">5.76 ± 1.50 / 50.36 ± 2.34</td> <!-- ScaLA-en -->
   <td class="en rc">70.34 ± 1.81 / 81.54 ± 1.06</td> <!-- SQuAD -->
   <td class="en summ">65.88 ± 1.55 / 19.75 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">29.83 ± 1.09 / 47.45 ± 0.69</td> <!-- MMLU -->
   <td class="en reason">18.44 ± 2.21 / 36.96 ± 2.10</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.8</td> <!-- CNN-DailyMail version -->
   <td>12.10.8</td> <!-- MMLU version -->
   <td>12.10.8</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="en ner">47.20 ± 3.39 / 44.00 ± 3.43</td> <!-- CoNLL-en -->
   <td class="en sent">64.82 ± 1.13 / 67.11 ± 1.41</td> <!-- SST5 -->
   <td class="en la">7.57 ± 2.31 / 45.83 ± 3.97</td> <!-- ScaLA-en -->
   <td class="en rc">73.88 ± 1.02 / 83.56 ± 0.75</td> <!-- SQuAD -->
   <td class="en summ">67.34 ± 0.38 / 21.61 ± 0.61</td> <!-- CNN-DailyMail -->
   <td class="en know">16.59 ± 1.01 / 35.35 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">11.97 ± 1.35 / 32.72 ± 0.94</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en rc">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
   <td class="en summ">68.15 ± 0.13 / 22.11 ± 0.19</td> <!-- CNN-DailyMail -->
   <td class="en know">27.24 ± 1.14 / 44.95 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">22.84 ± 1.16 / 41.75 ± 0.99</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>claude-3-5-haiku-20241022 (zero-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">unknown</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">200000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">277 ± 77 / 70 ± 25</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="en ner">74.35 ± 1.24 / 63.12 ± 1.09</td> <!-- CoNLL-en -->
   <td class="en sent">31.19 ± 2.30 / 44.96 ± 1.92</td> <!-- SST5 -->
   <td class="en la">21.76 ± 3.56 / 59.95 ± 1.92</td> <!-- ScaLA-en -->
   <td class="en rc">45.70 ± 1.03 / 74.84 ± 0.76</td> <!-- SQuAD -->
   <td class="en summ">67.96 ± 0.14 / 18.65 ± 0.23</td> <!-- CNN-DailyMail -->
   <td class="en know">28.80 ± 2.50 / 39.84 ± 1.87</td> <!-- MMLU -->
   <td class="en reason">42.52 ± 3.28 / 53.63 ± 2.58</td> <!-- HellaSwag -->
   <td>14.0.3</td> <!-- CoNLL-en version -->
   <td>14.0.2</td> <!-- SST5 version -->
   <td>14.0.3</td> <!-- ScaLA-en version -->
   <td>14.0.3</td> <!-- SQuAD version -->
   <td>14.0.3</td> <!-- CNN-DailyMail version -->
   <td>14.0.3</td> <!-- MMLU version -->
   <td>14.0.3</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="en ner">58.30 ± 2.16 / 53.45 ± 1.98</td> <!-- CoNLL-en -->
   <td class="en sent">59.01 ± 2.14 / 62.37 ± 1.73</td> <!-- SST5 -->
   <td class="en la">10.33 ± 3.06 / 53.28 ± 2.21</td> <!-- ScaLA-en -->
   <td class="en rc">65.04 ± 2.20 / 75.93 ± 1.50</td> <!-- SQuAD -->
   <td class="en summ">67.46 ± 0.31 / 23.04 ± 0.42</td> <!-- CNN-DailyMail -->
   <td class="en know">14.10 ± 0.93 / 34.24 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">10.67 ± 0.81 / 32.66 ± 0.64</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="en ner">41.57 ± 4.29 / 37.51 ± 3.05</td> <!-- CoNLL-en -->
   <td class="en sent">62.32 ± 1.12 / 67.09 ± 0.96</td> <!-- SST5 -->
   <td class="en la">8.04 ± 3.17 / 48.16 ± 5.38</td> <!-- ScaLA-en -->
   <td class="en rc">56.01 ± 3.10 / 67.43 ± 2.41</td> <!-- SQuAD -->
   <td class="en summ">65.06 ± 0.87 / 20.12 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">34.02 ± 0.87 / 50.12 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">22.81 ± 1.86 / 41.37 ± 1.41</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,297 ± 338 / 245 ± 83</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="en ner">62.90 ± 2.49 / 56.12 ± 1.92</td> <!-- CoNLL-en -->
   <td class="en sent">62.39 ± 1.67 / 66.36 ± 0.89</td> <!-- SST5 -->
   <td class="en la">19.96 ± 4.17 / 51.63 ± 5.43</td> <!-- ScaLA-en -->
   <td class="en rc">25.93 ± 4.95 / 47.47 ± 4.90</td> <!-- SQuAD -->
   <td class="en summ">63.31 ± 0.93 / 15.85 ± 0.47</td> <!-- CNN-DailyMail -->
   <td class="en know">40.90 ± 1.22 / 55.74 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">16.59 ± 3.39 / 36.28 ± 2.78</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8448</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="en ner">30.82 ± 4.46 / 27.49 ± 3.87</td> <!-- CoNLL-en -->
   <td class="en sent">66.28 ± 0.84 / 65.60 ± 1.23</td> <!-- SST5 -->
   <td class="en la">10.09 ± 2.52 / 48.92 ± 3.34</td> <!-- ScaLA-en -->
   <td class="en rc">64.96 ± 3.77 / 78.21 ± 2.16</td> <!-- SQuAD -->
   <td class="en summ">67.13 ± 0.54 / 21.94 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">35.14 ± 1.07 / 51.22 ± 0.84</td> <!-- MMLU -->
   <td class="en reason">11.26 ± 1.35 / 31.40 ± 1.40</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="en ner">40.89 ± 2.63 / 37.44 ± 2.39</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en rc">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">67.23 ± 0.14 / 18.87 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">26.84 ± 0.41 / 44.86 ± 0.31</td> <!-- MMLU -->
   <td class="en reason">23.89 ± 1.20 / 42.78 ± 0.95</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="en ner">56.41 ± 1.79 / 52.05 ± 1.57</td> <!-- CoNLL-en -->
   <td class="en sent">59.46 ± 1.16 / 65.61 ± 1.08</td> <!-- SST5 -->
   <td class="en la">8.36 ± 0.71 / 49.50 ± 2.90</td> <!-- ScaLA-en -->
   <td class="en rc">47.26 ± 3.09 / 67.95 ± 2.10</td> <!-- SQuAD -->
   <td class="en summ">66.61 ± 0.54 / 21.06 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">25.59 ± 0.93 / 43.75 ± 0.65</td> <!-- MMLU -->
   <td class="en reason">18.56 ± 1.15 / 38.13 ± 0.88</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">2.76</td> <!-- ScandEval rank -->
   <td class="en ner">39.21 ± 1.52 / 34.08 ± 1.88</td> <!-- CoNLL-en -->
   <td class="en sent">65.58 ± 1.59 / 57.86 ± 1.13</td> <!-- SST5 -->
   <td class="en la">7.82 ± 1.43 / 51.19 ± 1.75</td> <!-- ScaLA-en -->
   <td class="en rc">72.25 ± 2.19 / 83.08 ± 1.30</td> <!-- SQuAD -->
   <td class="en summ">64.07 ± 0.60 / 19.27 ± 0.54</td> <!-- CNN-DailyMail -->
   <td class="en know">14.98 ± 0.77 / 36.11 ± 0.75</td> <!-- MMLU -->
   <td class="en reason">13.55 ± 1.51 / 34.03 ± 1.55</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="en ner">60.64 ± 2.11 / 55.14 ± 2.01</td> <!-- CoNLL-en -->
   <td class="en sent">61.20 ± 1.16 / 61.92 ± 1.68</td> <!-- SST5 -->
   <td class="en la">7.63 ± 2.79 / 46.39 ± 3.79</td> <!-- ScaLA-en -->
   <td class="en rc">69.83 ± 2.12 / 80.15 ± 1.27</td> <!-- SQuAD -->
   <td class="en summ">56.62 ± 3.70 / 13.80 ± 2.77</td> <!-- CNN-DailyMail -->
   <td class="en know">16.29 ± 0.76 / 36.25 ± 0.61</td> <!-- MMLU -->
   <td class="en reason">10.37 ± 1.17 / 32.60 ± 0.89</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,964 ± 2,255 / 1,299 ± 433</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="en ner">46.26 ± 3.26 / 40.49 ± 2.54</td> <!-- CoNLL-en -->
   <td class="en sent">63.47 ± 0.73 / 60.77 ± 1.39</td> <!-- SST5 -->
   <td class="en la">13.17 ± 1.60 / 54.31 ± 1.93</td> <!-- ScaLA-en -->
   <td class="en rc">59.32 ± 1.48 / 72.97 ± 0.96</td> <!-- SQuAD -->
   <td class="en summ">66.43 ± 0.60 / 20.68 ± 0.92</td> <!-- CNN-DailyMail -->
   <td class="en know">9.68 ± 1.07 / 31.43 ± 0.85</td> <!-- MMLU -->
   <td class="en reason">4.99 ± 0.71 / 26.87 ± 0.63</td> <!-- HellaSwag -->
   <td>13.2.0</td> <!-- CoNLL-en version -->
   <td>13.2.0</td> <!-- SST5 version -->
   <td>13.2.0</td> <!-- ScaLA-en version -->
   <td>13.2.0</td> <!-- SQuAD version -->
   <td>13.2.0</td> <!-- CNN-DailyMail version -->
   <td>13.2.0</td> <!-- MMLU version -->
   <td>13.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="en ner">45.89 ± 2.63 / 42.96 ± 2.56</td> <!-- CoNLL-en -->
   <td class="en sent">59.29 ± 1.35 / 65.59 ± 1.02</td> <!-- SST5 -->
   <td class="en la">9.11 ± 2.36 / 52.02 ± 2.16</td> <!-- ScaLA-en -->
   <td class="en rc">66.74 ± 1.21 / 77.75 ± 1.09</td> <!-- SQuAD -->
   <td class="en summ">68.17 ± 0.69 / 22.50 ± 0.73</td> <!-- CNN-DailyMail -->
   <td class="en know">0.92 ± 1.20 / 23.00 ± 0.81</td> <!-- MMLU -->
   <td class="en reason">0.61 ± 1.04 / 25.00 ± 0.60</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="en ner">19.65 ± 5.96 / 18.64 ± 5.49</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en rc">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
   <td class="en summ">66.51 ± 0.85 / 21.76 ± 0.84</td> <!-- CNN-DailyMail -->
   <td class="en know">20.38 ± 0.82 / 38.44 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">7.41 ± 1.01 / 29.08 ± 0.61</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,607 ± 565 / 1,212 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="en ner">23.28 ± 6.45 / 21.81 ± 5.61</td> <!-- CoNLL-en -->
   <td class="en sent">61.91 ± 2.08 / 67.80 ± 1.12</td> <!-- SST5 -->
   <td class="en la">6.92 ± 2.36 / 44.29 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en rc">64.68 ± 1.06 / 76.60 ± 0.51</td> <!-- SQuAD -->
   <td class="en summ">65.15 ± 0.86 / 20.15 ± 0.50</td> <!-- CNN-DailyMail -->
   <td class="en know">22.65 ± 0.87 / 41.40 ± 0.67</td> <!-- MMLU -->
   <td class="en reason">14.54 ± 1.87 / 34.39 ± 1.49</td> <!-- HellaSwag -->
   <td>12.6.1</td> <!-- CoNLL-en version -->
   <td>12.6.1</td> <!-- SST5 version -->
   <td>12.6.1</td> <!-- ScaLA-en version -->
   <td>12.6.1</td> <!-- SQuAD version -->
   <td>12.6.1</td> <!-- CNN-DailyMail version -->
   <td>12.6.1</td> <!-- MMLU version -->
   <td>12.6.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en rc">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
   <td class="en summ">67.28 ± 0.27 / 22.84 ± 0.41</td> <!-- CNN-DailyMail -->
   <td class="en know">18.21 ± 0.70 / 37.61 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">10.84 ± 1.23 / 31.84 ± 1.00</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1657</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,009 ± 4,072 / 2,702 ± 878</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="en ner">37.47 ± 1.64 / 32.39 ± 2.53</td> <!-- CoNLL-en -->
   <td class="en sent">58.61 ± 2.46 / 62.78 ± 1.22</td> <!-- SST5 -->
   <td class="en la">5.30 ± 1.43 / 46.95 ± 3.51</td> <!-- ScaLA-en -->
   <td class="en rc">63.26 ± 0.73 / 74.41 ± 0.65</td> <!-- SQuAD -->
   <td class="en summ">67.24 ± 0.36 / 21.22 ± 0.36</td> <!-- CNN-DailyMail -->
   <td class="en know">3.93 ± 0.84 / 28.88 ± 0.73</td> <!-- MMLU -->
   <td class="en reason">1.26 ± 1.14 / 25.56 ± 0.82</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4352</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="en ner">42.78 ± 4.24 / 40.64 ± 2.84</td> <!-- CoNLL-en -->
   <td class="en sent">59.90 ± 4.98 / 54.05 ± 2.70</td> <!-- SST5 -->
   <td class="en la">5.68 ± 1.91 / 50.82 ± 2.18</td> <!-- ScaLA-en -->
   <td class="en rc">58.52 ± 1.88 / 68.97 ± 1.86</td> <!-- SQuAD -->
   <td class="en summ">64.83 ± 0.95 / 18.37 ± 0.46</td> <!-- CNN-DailyMail -->
   <td class="en know">1.63 ± 0.89 / 23.51 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">0.54 ± 1.01 / 24.93 ± 0.46</td> <!-- HellaSwag -->
   <td>12.10.5</td> <!-- CoNLL-en version -->
   <td>12.10.5</td> <!-- SST5 version -->
   <td>12.10.5</td> <!-- ScaLA-en version -->
   <td>12.10.5</td> <!-- SQuAD version -->
   <td>12.10.5</td> <!-- CNN-DailyMail version -->
   <td>12.10.5</td> <!-- MMLU version -->
   <td>12.10.5</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-research-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,254 ± 328 / 243 ± 83</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="en ner">50.73 ± 2.64 / 38.64 ± 1.60</td> <!-- CoNLL-en -->
   <td class="en sent">27.52 ± 3.38 / 31.81 ± 3.98</td> <!-- SST5 -->
   <td class="en la">2.96 ± 2.64 / 35.23 ± 1.82</td> <!-- ScaLA-en -->
   <td class="en rc">63.42 ± 1.34 / 76.38 ± 1.18</td> <!-- SQuAD -->
   <td class="en summ">68.74 ± 0.08 / 21.51 ± 0.20</td> <!-- CNN-DailyMail -->
   <td class="en know">16.65 ± 0.64 / 35.86 ± 0.47</td> <!-- MMLU -->
   <td class="en reason">10.69 ± 1.12 / 29.62 ± 0.77</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en rc">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
   <td class="en summ">65.22 ± 0.29 / 19.22 ± 0.18</td> <!-- CNN-DailyMail -->
   <td class="en know">18.24 ± 1.14 / 37.15 ± 0.82</td> <!-- MMLU -->
   <td class="en reason">10.89 ± 1.01 / 32.65 ± 0.85</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="en ner">38.51 ± 3.33 / 38.08 ± 2.64</td> <!-- CoNLL-en -->
   <td class="en sent">63.60 ± 2.87 / 58.50 ± 1.25</td> <!-- SST5 -->
   <td class="en la">2.23 ± 1.32 / 34.15 ± 0.60</td> <!-- ScaLA-en -->
   <td class="en rc">45.44 ± 3.61 / 59.52 ± 2.98</td> <!-- SQuAD -->
   <td class="en summ">67.11 ± 0.90 / 21.77 ± 0.72</td> <!-- CNN-DailyMail -->
   <td class="en know">5.02 ± 1.22 / 25.76 ± 1.01</td> <!-- MMLU -->
   <td class="en reason">2.08 ± 0.75 / 25.95 ± 0.35</td> <!-- HellaSwag -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,296 ± 335 / 246 ± 84</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="en ner">40.91 ± 6.01 / 37.55 ± 4.86</td> <!-- CoNLL-en -->
   <td class="en sent">47.12 ± 10.26 / 54.09 ± 8.04</td> <!-- SST5 -->
   <td class="en la">6.03 ± 1.71 / 49.55 ± 3.61</td> <!-- ScaLA-en -->
   <td class="en rc">51.34 ± 2.37 / 65.28 ± 2.29</td> <!-- SQuAD -->
   <td class="en summ">66.65 ± 1.14 / 20.92 ± 1.64</td> <!-- CNN-DailyMail -->
   <td class="en know">4.91 ± 2.84 / 25.92 ± 1.81</td> <!-- MMLU -->
   <td class="en reason">1.21 ± 1.04 / 25.67 ± 0.89</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en rc">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
   <td class="en summ">65.81 ± 1.90 / 20.88 ± 0.66</td> <!-- CNN-DailyMail -->
   <td class="en know">11.66 ± 1.13 / 32.84 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">5.22 ± 1.17 / 27.95 ± 1.10</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1385</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,808 ± 2,183 / 1,289 ± 428</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="en ner">29.84 ± 4.45 / 28.13 ± 3.61</td> <!-- CoNLL-en -->
   <td class="en sent">64.13 ± 1.51 / 56.76 ± 0.96</td> <!-- SST5 -->
   <td class="en la">3.99 ± 1.63 / 43.68 ± 3.91</td> <!-- ScaLA-en -->
   <td class="en rc">55.74 ± 1.72 / 65.95 ± 1.64</td> <!-- SQuAD -->
   <td class="en summ">64.55 ± 0.62 / 19.04 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">1.42 ± 1.20 / 26.10 ± 0.80</td> <!-- MMLU -->
   <td class="en reason">1.42 ± 0.61 / 25.58 ± 0.70</td> <!-- HellaSwag -->
   <td>13.2.0</td> <!-- CoNLL-en version -->
   <td>13.2.0</td> <!-- SST5 version -->
   <td>13.2.0</td> <!-- ScaLA-en version -->
   <td>13.2.0</td> <!-- SQuAD version -->
   <td>13.2.0</td> <!-- CNN-DailyMail version -->
   <td>13.2.0</td> <!-- MMLU version -->
   <td>13.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>openGPT-X/Teuken-7B-instruct-commercial-v0.4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7453</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,438 ± 410 / 233 ± 79</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="en ner">44.48 ± 3.17 / 36.31 ± 2.23</td> <!-- CoNLL-en -->
   <td class="en sent">23.69 ± 3.36 / 25.98 ± 3.59</td> <!-- SST5 -->
   <td class="en la">8.52 ± 2.60 / 51.57 ± 2.62</td> <!-- ScaLA-en -->
   <td class="en rc">56.97 ± 1.53 / 71.38 ± 1.28</td> <!-- SQuAD -->
   <td class="en summ">68.81 ± 0.06 / 22.48 ± 0.20</td> <!-- CNN-DailyMail -->
   <td class="en know">15.31 ± 1.45 / 35.07 ± 1.13</td> <!-- MMLU -->
   <td class="en reason">9.35 ± 1.36 / 29.47 ± 1.09</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131328</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="en ner">35.08 ± 5.88 / 32.44 ± 4.89</td> <!-- CoNLL-en -->
   <td class="en sent">54.40 ± 2.92 / 64.38 ± 2.10</td> <!-- SST5 -->
   <td class="en la">2.97 ± 0.84 / 45.05 ± 4.18</td> <!-- ScaLA-en -->
   <td class="en rc">58.30 ± 2.84 / 71.04 ± 1.83</td> <!-- SQuAD -->
   <td class="en summ">62.19 ± 1.70 / 16.53 ± 1.13</td> <!-- CNN-DailyMail -->
   <td class="en know">7.91 ± 0.72 / 29.30 ± 0.46</td> <!-- MMLU -->
   <td class="en reason">1.60 ± 1.21 / 26.25 ± 0.85</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="en ner">35.84 ± 5.12 / 35.76 ± 4.29</td> <!-- CoNLL-en -->
   <td class="en sent">56.87 ± 8.16 / 59.62 ± 5.61</td> <!-- SST5 -->
   <td class="en la">3.08 ± 2.98 / 40.66 ± 4.63</td> <!-- ScaLA-en -->
   <td class="en rc">52.77 ± 1.53 / 66.64 ± 1.58</td> <!-- SQuAD -->
   <td class="en summ">63.96 ± 1.61 / 19.20 ± 1.54</td> <!-- CNN-DailyMail -->
   <td class="en know">7.42 ± 1.60 / 28.95 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">2.24 ± 1.08 / 25.72 ± 0.82</td> <!-- HellaSwag -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en rc">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
   <td class="en summ">43.45 ± 7.12 / 15.14 ± 2.47</td> <!-- CNN-DailyMail -->
   <td class="en know">9.10 ± 1.33 / 30.31 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">8.35 ± 0.79 / 29.79 ± 0.76</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>9.3.1</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2304</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="en ner">38.23 ± 3.10 / 36.38 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">60.70 ± 1.80 / 66.82 ± 1.12</td> <!-- SST5 -->
   <td class="en la">-0.19 ± 2.28 / 38.77 ± 3.32</td> <!-- ScaLA-en -->
   <td class="en rc">61.93 ± 1.98 / 73.71 ± 1.57</td> <!-- SQuAD -->
   <td class="en summ">51.32 ± 0.91 / 11.96 ± 0.57</td> <!-- CNN-DailyMail -->
   <td class="en know">5.00 ± 1.53 / 27.59 ± 1.14</td> <!-- MMLU -->
   <td class="en reason">1.10 ± 1.02 / 25.71 ± 0.66</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="en ner">30.73 ± 4.30 / 29.47 ± 4.10</td> <!-- CoNLL-en -->
   <td class="en sent">59.51 ± 3.73 / 54.82 ± 2.43</td> <!-- SST5 -->
   <td class="en la">1.55 ± 1.90 / 43.18 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en rc">49.03 ± 1.47 / 60.00 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">57.73 ± 4.93 / 15.68 ± 1.21</td> <!-- CNN-DailyMail -->
   <td class="en know">0.11 ± 1.23 / 23.20 ± 0.56</td> <!-- MMLU -->
   <td class="en reason">-0.06 ± 0.39 / 24.60 ± 0.44</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">33024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="en ner">28.63 ± 4.74 / 27.07 ± 4.13</td> <!-- CoNLL-en -->
   <td class="en sent">66.55 ± 0.72 / 58.18 ± 0.62</td> <!-- SST5 -->
   <td class="en la">1.47 ± 1.57 / 45.89 ± 2.92</td> <!-- ScaLA-en -->
   <td class="en rc">35.00 ± 2.01 / 47.83 ± 2.25</td> <!-- SQuAD -->
   <td class="en summ">62.05 ± 1.63 / 16.80 ± 1.01</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.41 ± 1.21 / 23.76 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">-0.04 ± 0.77 / 25.03 ± 0.52</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="en ner">31.14 ± 1.79 / 28.54 ± 0.86</td> <!-- CoNLL-en -->
   <td class="en sent">43.97 ± 5.28 / 55.08 ± 4.26</td> <!-- SST5 -->
   <td class="en la">3.49 ± 2.49 / 46.52 ± 4.13</td> <!-- ScaLA-en -->
   <td class="en rc">47.91 ± 4.97 / 60.41 ± 3.91</td> <!-- SQuAD -->
   <td class="en summ">62.20 ± 1.04 / 17.61 ± 0.50</td> <!-- CNN-DailyMail -->
   <td class="en know">0.12 ± 1.55 / 23.00 ± 0.82</td> <!-- MMLU -->
   <td class="en reason">0.13 ± 1.34 / 24.53 ± 0.49</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2304</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="en ner">25.36 ± 8.05 / 24.05 ± 7.34</td> <!-- CoNLL-en -->
   <td class="en sent">56.91 ± 2.41 / 66.15 ± 1.54</td> <!-- SST5 -->
   <td class="en la">7.10 ± 2.89 / 49.36 ± 4.03</td> <!-- ScaLA-en -->
   <td class="en rc">58.60 ± 5.37 / 70.37 ± 4.71</td> <!-- SQuAD -->
   <td class="en summ">46.16 ± 1.28 / 11.33 ± 0.70</td> <!-- CNN-DailyMail -->
   <td class="en know">0.71 ± 0.85 / 24.97 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">0.82 ± 1.01 / 25.62 ± 0.74</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.5.2</td> <!-- SST5 version -->
   <td>12.5.2</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>12.5.2</td> <!-- CNN-DailyMail version -->
   <td>12.5.2</td> <!-- MMLU version -->
   <td>12.5.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2304</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="en ner">26.47 ± 6.25 / 28.27 ± 5.35</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en rc">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
   <td class="en summ">46.18 ± 1.20 / 10.06 ± 0.67</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.87 ± 0.99 / 23.08 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">0.20 ± 1.12 / 24.94 ± 0.86</td> <!-- HellaSwag -->
   <td>12.5.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-1.2b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,756 ± 3,589 / 1,157 ± 670</td> <!-- Model inference speed -->
   <td class="rank">3.76</td> <!-- ScandEval rank -->
   <td class="en ner">40.45 ± 3.27 / 37.90 ± 2.99</td> <!-- CoNLL-en -->
   <td class="en sent">47.72 ± 3.58 / 56.94 ± 1.93</td> <!-- SST5 -->
   <td class="en la">-1.04 ± 1.90 / 39.17 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en rc">26.77 ± 5.45 / 35.60 ± 6.25</td> <!-- SQuAD -->
   <td class="en summ">50.31 ± 7.81 / 13.58 ± 2.12</td> <!-- CNN-DailyMail -->
   <td class="en know">1.03 ± 0.82 / 26.95 ± 0.56</td> <!-- MMLU -->
   <td class="en reason">-0.30 ± 1.30 / 24.99 ± 1.10</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en rc">36.51 ± 2.07 / 50.66 ± 1.90</td> <!-- SQuAD -->
   <td class="en summ">60.11 ± 1.39 / 16.29 ± 0.69</td> <!-- CNN-DailyMail -->
   <td class="en know">3.71 ± 0.75 / 28.35 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">0.62 ± 0.99 / 24.68 ± 0.55</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.2</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Nano (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1195</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,519 ± 841 / 323 ± 104</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="en ner">21.60 ± 4.23 / 23.22 ± 3.33</td> <!-- CoNLL-en -->
   <td class="en sent">45.04 ± 5.17 / 50.76 ± 4.28</td> <!-- SST5 -->
   <td class="en la">-0.60 ± 0.87 / 34.57 ± 1.70</td> <!-- ScaLA-en -->
   <td class="en rc">33.46 ± 2.84 / 44.25 ± 3.38</td> <!-- SQuAD -->
   <td class="en summ">49.12 ± 7.39 / 12.74 ± 2.01</td> <!-- CNN-DailyMail -->
   <td class="en know">2.37 ± 0.75 / 27.67 ± 0.77</td> <!-- MMLU -->
   <td class="en reason">-0.33 ± 1.21 / 25.00 ± 1.15</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-3b-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3212</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,513 ± 1,241 / 1,282 ± 644</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="en ner">27.37 ± 4.57 / 26.50 ± 4.52</td> <!-- CoNLL-en -->
   <td class="en sent">36.14 ± 7.74 / 45.63 ± 7.84</td> <!-- SST5 -->
   <td class="en la">-1.97 ± 1.83 / 43.64 ± 2.89</td> <!-- ScaLA-en -->
   <td class="en rc">7.42 ± 2.13 / 16.44 ± 2.71</td> <!-- SQuAD -->
   <td class="en summ">60.89 ± 0.87 / 17.36 ± 0.62</td> <!-- CNN-DailyMail -->
   <td class="en know">2.21 ± 1.17 / 26.40 ± 1.12</td> <!-- MMLU -->
   <td class="en reason">-0.90 ± 0.79 / 24.52 ± 0.70</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.05</td> <!-- ScandEval rank -->
   <td class="en ner">31.26 ± 3.84 / 30.44 ± 3.28</td> <!-- CoNLL-en -->
   <td class="en sent">26.69 ± 10.82 / 34.46 ± 8.00</td> <!-- SST5 -->
   <td class="en la">1.78 ± 1.67 / 43.50 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">13.88 ± 1.36 / 22.49 ± 2.14</td> <!-- SQuAD -->
   <td class="en summ">52.05 ± 1.59 / 12.74 ± 1.04</td> <!-- CNN-DailyMail -->
   <td class="en know">1.51 ± 0.81 / 25.05 ± 0.75</td> <!-- MMLU -->
   <td class="en reason">-0.76 ± 0.97 / 24.52 ± 0.59</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.06</td> <!-- ScandEval rank -->
   <td class="en ner">29.96 ± 3.19 / 28.98 ± 3.29</td> <!-- CoNLL-en -->
   <td class="en sent">18.64 ± 8.52 / 28.83 ± 5.86</td> <!-- SST5 -->
   <td class="en la">1.85 ± 1.20 / 44.03 ± 3.98</td> <!-- ScaLA-en -->
   <td class="en rc">26.90 ± 1.56 / 36.91 ± 1.53</td> <!-- SQuAD -->
   <td class="en summ">52.96 ± 1.38 / 14.23 ± 0.78</td> <!-- CNN-DailyMail -->
   <td class="en know">1.34 ± 0.74 / 25.67 ± 1.03</td> <!-- MMLU -->
   <td class="en reason">0.10 ± 1.29 / 24.71 ± 0.69</td> <!-- HellaSwag -->
   <td>13.1.0</td> <!-- CoNLL-en version -->
   <td>13.1.0</td> <!-- SST5 version -->
   <td>13.1.0</td> <!-- ScaLA-en version -->
   <td>13.1.0</td> <!-- SQuAD version -->
   <td>13.1.0</td> <!-- CNN-DailyMail version -->
   <td>13.1.0</td> <!-- MMLU version -->
   <td>13.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,880 ± 556 / 280 ± 95</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="en ner">0.02 ± 0.03 / 0.01 ± 0.03</td> <!-- CoNLL-en -->
   <td class="en sent">60.98 ± 1.60 / 58.19 ± 1.01</td> <!-- SST5 -->
   <td class="en la">2.26 ± 3.46 / 36.14 ± 4.01</td> <!-- ScaLA-en -->
   <td class="en rc">9.94 ± 1.53 / 26.50 ± 2.35</td> <!-- SQuAD -->
   <td class="en summ">41.10 ± 2.34 / 6.64 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">12.17 ± 1.07 / 31.75 ± 1.03</td> <!-- MMLU -->
   <td class="en reason">0.62 ± 1.44 / 25.00 ± 0.88</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,424 ± 1,080 / 464 ± 158</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="en ner">3.98 ± 3.16 / 3.68 ± 2.99</td> <!-- CoNLL-en -->
   <td class="en sent">39.56 ± 6.39 / 48.56 ± 7.74</td> <!-- SST5 -->
   <td class="en la">5.15 ± 1.53 / 46.63 ± 3.93</td> <!-- ScaLA-en -->
   <td class="en rc">26.96 ± 2.30 / 42.51 ± 3.06</td> <!-- SQuAD -->
   <td class="en summ">43.27 ± 1.15 / 7.42 ± 0.80</td> <!-- CNN-DailyMail -->
   <td class="en know">2.45 ± 1.06 / 28.00 ± 0.77</td> <!-- MMLU -->
   <td class="en reason">-0.84 ± 1.17 / 24.50 ± 0.79</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-Pico (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,331 ± 787 / 301 ± 97</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="en ner">27.45 ± 4.13 / 27.11 ± 3.47</td> <!-- CoNLL-en -->
   <td class="en sent">27.24 ± 8.04 / 39.08 ± 6.46</td> <!-- SST5 -->
   <td class="en la">0.32 ± 0.85 / 43.07 ± 3.37</td> <!-- ScaLA-en -->
   <td class="en rc">15.62 ± 2.29 / 26.76 ± 1.43</td> <!-- SQuAD -->
   <td class="en summ">43.83 ± 6.89 / 8.96 ± 1.14</td> <!-- CNN-DailyMail -->
   <td class="en know">0.65 ± 0.70 / 24.30 ± 0.79</td> <!-- MMLU -->
   <td class="en reason">-0.44 ± 1.22 / 24.71 ± 0.98</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>PleIAs/Pleias-350m-Preview (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">353</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,242 ± 3,432 / 1,335 ± 484</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="en ner">31.79 ± 3.88 / 31.32 ± 2.81</td> <!-- CoNLL-en -->
   <td class="en sent">18.45 ± 9.77 / 33.15 ± 6.93</td> <!-- SST5 -->
   <td class="en la">-0.28 ± 1.49 / 40.66 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">12.35 ± 1.80 / 21.93 ± 1.63</td> <!-- SQuAD -->
   <td class="en summ">46.13 ± 6.88 / 11.20 ± 1.59</td> <!-- CNN-DailyMail -->
   <td class="en know">-1.20 ± 0.68 / 23.43 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">0.47 ± 1.47 / 25.42 ± 1.15</td> <!-- HellaSwag -->
   <td>14.0.4</td> <!-- CoNLL-en version -->
   <td>14.0.4</td> <!-- SST5 version -->
   <td>14.0.4</td> <!-- ScaLA-en version -->
   <td>14.0.4</td> <!-- SQuAD version -->
   <td>14.0.4</td> <!-- CNN-DailyMail version -->
   <td>14.0.4</td> <!-- MMLU version -->
   <td>14.0.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.53</td> <!-- ScandEval rank -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en rc">0.00 ± 0.00 / 3.68 ± 0.43</td> <!-- SQuAD -->
   <td class="en summ">61.26 ± 0.09 / 6.73 ± 0.06</td> <!-- CNN-DailyMail -->
   <td class="en know">0.00 ± 0.00 / 22.69 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">0.36 ± 0.47 / 24.60 ± 0.43</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.67</td> <!-- ScandEval rank -->
   <td class="en ner">12.34 ± 2.70 / 12.41 ± 2.54</td> <!-- CoNLL-en -->
   <td class="en sent">-1.48 ± 3.09 / 21.17 ± 2.22</td> <!-- SST5 -->
   <td class="en la">-0.48 ± 1.52 / 42.45 ± 3.99</td> <!-- ScaLA-en -->
   <td class="en rc">0.72 ± 0.25 / 6.31 ± 0.51</td> <!-- SQuAD -->
   <td class="en summ">49.61 ± 1.17 / 9.59 ± 0.65</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.12 ± 0.65 / 22.69 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">-0.01 ± 0.01 / 24.59 ± 0.43</td> <!-- HellaSwag -->
   <td>12.10.4</td> <!-- CoNLL-en version -->
   <td>12.10.4</td> <!-- SST5 version -->
   <td>12.10.4</td> <!-- ScaLA-en version -->
   <td>12.10.4</td> <!-- SQuAD version -->
   <td>12.10.4</td> <!-- CNN-DailyMail version -->
   <td>12.10.4</td> <!-- MMLU version -->
   <td>12.10.4</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">4.82</td> <!-- ScandEval rank -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">2.48 ± 1.94 / 34.52 ± 0.85</td> <!-- ScaLA-en -->
   <td class="en rc">0.01 ± 0.02 / 0.03 ± 0.02</td> <!-- SQuAD -->
   <td class="en summ">44.80 ± 0.36 / 0.32 ± 0.04</td> <!-- CNN-DailyMail -->
   <td class="en know">-0.69 ± 0.77 / 22.76 ± 0.40</td> <!-- MMLU -->
   <td class="en reason">0.37 ± 0.95 / 24.71 ± 0.44</td> <!-- HellaSwag -->
   <td>13.0.0</td> <!-- CoNLL-en version -->
   <td>13.0.0</td> <!-- SST5 version -->
   <td>13.0.0</td> <!-- ScaLA-en version -->
   <td>13.0.0</td> <!-- SQuAD version -->
   <td>13.0.0</td> <!-- CNN-DailyMail version -->
   <td>13.0.0</td> <!-- MMLU version -->
   <td>13.0.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.91</td> <!-- ScandEval rank -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en rc">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
   <td class="en summ">34.62 ± 0.17 / 2.18 ± 0.04</td> <!-- CNN-DailyMail -->
   <td class="en know">0.37 ± 0.93 / 24.18 ± 0.90</td> <!-- MMLU -->
   <td class="en reason">-0.17 ± 0.50 / 24.82 ± 0.41</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>11.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>11.0.0</td> <!-- MMLU version -->
   <td>11.0.0</td> <!-- HellaSwag version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/english-nlg.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
</div>
