---
layout: leaderboard
title: Swedish NLG 🇸🇪
---

<center>Last updated: 31/10/2024 16:22:42 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="swedish-nlg-test" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish summarization - BERTScore / ROUGE-L">SweDN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SUC3">SUC3 version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweReC">SweReC version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-sv">ScaLA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-sv">ScandiQA-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SweDN">SweDN version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-sv">MMLU-sv version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-sv">HellaSwag-sv version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8191</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.20</td> <!-- ScandEval rank -->
   <td class="sv ner">76.86 ± 1.89 / 54.97 ± 4.44</td> <!-- SUC3 -->
   <td class="sv sent">79.19 ± 1.87 / 80.56 ± 1.82</td> <!-- SweReC -->
   <td class="sv la">80.93 ± 1.67 / 89.90 ± 0.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.81 ± 1.28 / 65.15 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.83 ± 0.15 / 22.67 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">72.53 ± 1.82 / 79.26 ± 1.44</td> <!-- MMLU-sv -->
   <td class="sv reason">85.67 ± 2.59 / 89.14 ± 2.05</td> <!-- HellaSwag-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.28</td> <!-- ScandEval rank -->
   <td class="sv ner">76.66 ± 2.11 / 60.34 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">77.16 ± 2.65 / 79.22 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">68.99 ± 4.33 / 83.37 ± 2.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 1.35 / 67.71 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.00 ± 0.29 / 16.97 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">70.70 ± 1.32 / 77.97 ± 0.99</td> <!-- MMLU-sv -->
   <td class="sv reason">86.30 ± 2.23 / 89.65 ± 1.68</td> <!-- HellaSwag-sv -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.2</td> <!-- MMLU-sv version -->
   <td>12.10.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.29</td> <!-- ScandEval rank -->
   <td class="sv ner">74.45 ± 3.09 / 49.97 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">77.59 ± 1.38 / 78.78 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">71.35 ± 3.10 / 83.98 ± 2.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.56 ± 1.39 / 66.76 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.08 ± 0.14 / 17.19 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">71.32 ± 1.56 / 78.48 ± 1.15</td> <!-- MMLU-sv -->
   <td class="sv reason">84.09 ± 2.99 / 88.01 ± 2.26</td> <!-- HellaSwag-sv -->
   <td>12.10.0</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.2</td> <!-- MMLU-sv version -->
   <td>12.10.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,314 ± 1,202 / 776 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.42</td> <!-- ScandEval rank -->
   <td class="sv ner">88.78 ± 1.05 / 85.30 ± 1.16</td> <!-- SUC3 -->
   <td class="sv sent">81.73 ± 0.71 / 80.87 ± 0.96</td> <!-- SweReC -->
   <td class="sv la">75.83 ± 0.49 / 87.67 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.35 ± 0.70 / 65.90 ± 0.55</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.96 ± 0.09 / 23.17 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">41.07 ± 0.83 / 55.49 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">75.73 ± 0.72 / 81.68 ± 0.55</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.48</td> <!-- ScandEval rank -->
   <td class="sv ner">74.61 ± 2.99 / 56.50 ± 6.30</td> <!-- SUC3 -->
   <td class="sv sent">78.61 ± 1.40 / 78.64 ± 1.53</td> <!-- SweReC -->
   <td class="sv la">63.20 ± 3.34 / 80.61 ± 2.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.98 ± 1.65 / 66.85 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.41 / 22.47 ± 0.82</td> <!-- SweDN -->
   <td class="sv know">61.55 ± 1.68 / 71.02 ± 1.21</td> <!-- MMLU-sv -->
   <td class="sv reason">66.21 ± 3.22 / 73.40 ± 2.77</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="sv ner">62.59 ± 2.04 / 45.11 ± 4.50</td> <!-- SUC3 -->
   <td class="sv sent">80.73 ± 0.52 / 81.25 ± 0.57</td> <!-- SweReC -->
   <td class="sv la">61.37 ± 2.06 / 79.34 ± 1.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.76 ± 1.03 / 66.73 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.54 ± 0.91 / 19.89 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">58.15 ± 1.11 / 68.33 ± 0.83</td> <!-- MMLU-sv -->
   <td class="sv reason">68.94 ± 1.51 / 76.41 ± 1.17</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="sv ner">52.50 ± 1.02 / 37.38 ± 2.57</td> <!-- SUC3 -->
   <td class="sv sent">78.51 ± 0.93 / 76.24 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">61.28 ± 1.63 / 80.07 ± 1.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.22 ± 1.03 / 64.60 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.30 ± 0.12 / 19.72 ± 0.19</td> <!-- SweDN -->
   <td class="sv know">51.58 ± 0.83 / 63.27 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">66.61 ± 1.12 / 74.72 ± 0.93</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
   <td class="sv ner">62.96 ± 3.44 / 52.14 ± 4.04</td> <!-- SUC3 -->
   <td class="sv sent">75.25 ± 2.41 / 78.80 ± 1.96</td> <!-- SweReC -->
   <td class="sv la">53.28 ± 3.33 / 75.37 ± 1.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.42 ± 1.65 / 65.04 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.60 ± 0.30 / 21.60 ± 0.76</td> <!-- SweDN -->
   <td class="sv know">53.56 ± 2.20 / 64.88 ± 1.66</td> <!-- MMLU-sv -->
   <td class="sv reason">59.70 ± 4.69 / 69.38 ± 3.70</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="sv ner">77.06 ± 2.72 / 67.75 ± 5.69</td> <!-- SUC3 -->
   <td class="sv sent">53.56 ± 7.15 / 67.07 ± 3.93</td> <!-- SweReC -->
   <td class="sv la">47.50 ± 3.37 / 71.31 ± 2.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.86 ± 1.77 / 60.96 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.25 ± 0.18 / 22.84 ± 0.44</td> <!-- SweDN -->
   <td class="sv know">61.31 ± 2.07 / 70.78 ± 1.60</td> <!-- MMLU-sv -->
   <td class="sv reason">66.73 ± 2.34 / 74.65 ± 1.78</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.93</td> <!-- ScandEval rank -->
   <td class="sv ner">64.76 ± 3.91 / 61.08 ± 5.41</td> <!-- SUC3 -->
   <td class="sv sent">75.46 ± 1.99 / 74.35 ± 3.70</td> <!-- SweReC -->
   <td class="sv la">43.27 ± 5.03 / 65.62 ± 4.94</td> <!-- ScaLA-sv -->
   <td class="sv rc">63.04 ± 1.52 / 66.95 ± 1.31</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.43 ± 0.33 / 24.92 ± 0.74</td> <!-- SweDN -->
   <td class="sv know">46.16 ± 2.67 / 59.53 ± 2.04</td> <!-- MMLU-sv -->
   <td class="sv reason">50.41 ± 5.18 / 62.34 ± 3.86</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.94</td> <!-- ScandEval rank -->
   <td class="sv ner">73.04 ± 2.74 / 61.64 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">72.77 ± 2.64 / 72.56 ± 2.45</td> <!-- SweReC -->
   <td class="sv la">58.06 ± 3.84 / 76.06 ± 2.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.02 ± 2.11 / 66.84 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.92 ± 0.16 / 19.00 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">40.73 ± 3.36 / 55.16 ± 2.75</td> <!-- MMLU-sv -->
   <td class="sv reason">50.51 ± 2.33 / 62.07 ± 1.95</td> <!-- HellaSwag-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>0.0.0</td> <!-- MMLU-sv version -->
   <td>0.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/lynx-micro (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,162 ± 2,661 / 1,878 ± 623</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="sv ner">83.64 ± 1.90 / 81.69 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">78.57 ± 0.78 / 78.35 ± 0.90</td> <!-- SweReC -->
   <td class="sv la">66.83 ± 0.98 / 83.20 ± 0.51</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.84 ± 0.54 / 62.97 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.40 ± 0.05 / 18.09 ± 0.11</td> <!-- SweDN -->
   <td class="sv know">20.47 ± 0.72 / 40.39 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">49.92 ± 0.92 / 62.45 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>12.10.2</td> <!-- SUC3 version -->
   <td>12.10.2</td> <!-- SweReC version -->
   <td>12.10.2</td> <!-- ScaLA-sv version -->
   <td>12.10.2</td> <!-- ScandiQA-sv version -->
   <td>12.10.2</td> <!-- SweDN version -->
   <td>12.10.2</td> <!-- MMLU-sv version -->
   <td>12.10.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="sv ner">50.43 ± 3.97 / 27.20 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">80.55 ± 1.46 / 77.22 ± 3.78</td> <!-- SweReC -->
   <td class="sv la">50.86 ± 3.91 / 72.14 ± 3.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.35 ± 1.16 / 65.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.63 ± 0.26 / 19.75 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">52.06 ± 0.97 / 63.92 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">49.80 ± 3.86 / 60.88 ± 3.42</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="sv ner">67.38 ± 1.52 / 52.86 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">65.51 ± 4.81 / 67.01 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">29.41 ± 10.34 / 52.38 ± 8.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.67 ± 0.89 / 66.26 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.70 ± 0.71 / 16.98 ± 0.75</td> <!-- SweDN -->
   <td class="sv know">50.06 ± 2.65 / 61.33 ± 2.36</td> <!-- MMLU-sv -->
   <td class="sv reason">64.58 ± 2.48 / 72.57 ± 2.06</td> <!-- HellaSwag-sv -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   <td>12.11.0</td> <!-- SweDN version -->
   <td>12.11.0</td> <!-- MMLU-sv version -->
   <td>12.11.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/sol (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,701 ± 876 / 771 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="sv ner">57.51 ± 2.30 / 37.74 ± 3.15</td> <!-- SUC3 -->
   <td class="sv sent">77.31 ± 1.01 / 70.55 ± 2.26</td> <!-- SweReC -->
   <td class="sv la">25.06 ± 5.02 / 49.04 ± 4.68</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.77 / 67.43 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.22 ± 0.19 / 18.86 ± 0.30</td> <!-- SweDN -->
   <td class="sv know">39.52 ± 0.58 / 54.47 ± 0.38</td> <!-- MMLU-sv -->
   <td class="sv reason">70.93 ± 1.29 / 78.03 ± 1.01</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="sv ner">59.65 ± 2.22 / 39.33 ± 3.33</td> <!-- SUC3 -->
   <td class="sv sent">77.48 ± 1.23 / 70.13 ± 2.81</td> <!-- SweReC -->
   <td class="sv la">16.94 ± 2.36 / 40.98 ± 1.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">62.65 ± 0.56 / 68.15 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.19 ± 0.36 / 19.09 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">39.82 ± 0.69 / 54.84 ± 0.53</td> <!-- MMLU-sv -->
   <td class="sv reason">68.87 ± 1.35 / 76.46 ± 1.04</td> <!-- HellaSwag-sv -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   <td>12.5.3</td> <!-- SweDN version -->
   <td>12.5.3</td> <!-- MMLU-sv version -->
   <td>12.5.3</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="sv ner">67.49 ± 2.20 / 51.10 ± 4.76</td> <!-- SUC3 -->
   <td class="sv sent">76.74 ± 1.27 / 75.66 ± 1.17</td> <!-- SweReC -->
   <td class="sv la">22.37 ± 3.11 / 54.47 ± 4.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.15 ± 0.72 / 64.47 ± 0.58</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.37 ± 0.39 / 19.85 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">37.50 ± 0.73 / 52.72 ± 0.63</td> <!-- MMLU-sv -->
   <td class="sv reason">55.01 ± 2.40 / 65.64 ± 2.12</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="sv ner">62.86 ± 1.95 / 36.42 ± 3.49</td> <!-- SUC3 -->
   <td class="sv sent">70.54 ± 6.38 / 73.39 ± 6.37</td> <!-- SweReC -->
   <td class="sv la">37.50 ± 2.48 / 66.32 ± 1.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.00 ± 0.85 / 65.98 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.93 ± 0.19 / 19.24 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">40.58 ± 1.17 / 55.16 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">42.99 ± 2.04 / 56.16 ± 1.93</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="sv ner">60.38 ± 1.60 / 36.17 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">77.49 ± 0.98 / 72.07 ± 1.56</td> <!-- SweReC -->
   <td class="sv la">29.32 ± 2.34 / 54.43 ± 2.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.79 ± 0.83 / 65.84 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.75 ± 0.16 / 20.23 ± 0.23</td> <!-- SweDN -->
   <td class="sv know">36.05 ± 1.10 / 51.86 ± 0.87</td> <!-- MMLU-sv -->
   <td class="sv reason">51.15 ± 1.71 / 63.20 ± 1.32</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.49 / 44.62 ± 4.10</td> <!-- SUC3 -->
   <td class="sv sent">79.96 ± 0.93 / 75.75 ± 2.22</td> <!-- SweReC -->
   <td class="sv la">31.70 ± 4.07 / 59.28 ± 5.00</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.33 ± 0.88 / 65.24 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.07 ± 0.28 / 18.94 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">37.48 ± 0.64 / 52.46 ± 0.52</td> <!-- MMLU-sv -->
   <td class="sv reason">31.27 ± 1.39 / 47.97 ± 1.30</td> <!-- HellaSwag-sv -->
   <td>12.11.0</td> <!-- SUC3 version -->
   <td>12.11.0</td> <!-- SweReC version -->
   <td>12.11.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="sv ner">54.14 ± 2.49 / 37.43 ± 3.05</td> <!-- SUC3 -->
   <td class="sv sent">78.27 ± 1.32 / 77.65 ± 1.28</td> <!-- SweReC -->
   <td class="sv la">32.49 ± 1.94 / 64.28 ± 2.18</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.95 ± 0.96 / 66.56 ± 0.62</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.86 ± 0.29 / 19.67 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">43.62 ± 0.82 / 57.61 ± 0.65</td> <!-- MMLU-sv -->
   <td class="sv reason">28.84 ± 2.65 / 45.75 ± 2.13</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/dolphin-2.9-llama3-8b-flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,018 ± 1,216 / 996 ± 324</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="sv ner">65.33 ± 2.38 / 46.88 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">74.99 ± 3.45 / 76.76 ± 1.80</td> <!-- SweReC -->
   <td class="sv la">32.65 ± 5.08 / 61.25 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.71 ± 1.34 / 64.54 ± 1.00</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.53 ± 0.29 / 19.24 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">33.16 ± 2.11 / 49.26 ± 1.55</td> <!-- MMLU-sv -->
   <td class="sv reason">32.51 ± 2.97 / 48.24 ± 2.10</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="sv ner">71.52 ± 1.43 / 59.28 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">80.46 ± 0.83 / 78.67 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">12.29 ± 3.59 / 40.53 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.54 ± 1.52 / 62.08 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.27 ± 0.15 / 19.05 ± 0.30</td> <!-- SweDN -->
   <td class="sv know">39.40 ± 1.44 / 53.87 ± 1.19</td> <!-- MMLU-sv -->
   <td class="sv reason">38.88 ± 1.25 / 53.72 ± 0.91</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="sv ner">50.53 ± 3.30 / 37.77 ± 4.38</td> <!-- SUC3 -->
   <td class="sv sent">77.37 ± 2.25 / 78.66 ± 2.43</td> <!-- SweReC -->
   <td class="sv la">27.84 ± 4.72 / 49.46 ± 4.52</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.98 ± 1.65 / 65.44 ± 1.38</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.89 ± 0.44 / 23.94 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">34.80 ± 2.79 / 50.82 ± 2.10</td> <!-- MMLU-sv -->
   <td class="sv reason">36.65 ± 5.07 / 51.56 ± 4.13</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/orpo-llama-3-swe (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,974 ± 1,208 / 1,032 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="sv ner">60.93 ± 2.85 / 38.87 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.68 / 75.13 ± 1.85</td> <!-- SweReC -->
   <td class="sv la">26.02 ± 4.38 / 52.19 ± 5.44</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.84 ± 0.92 / 65.92 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.99 ± 0.26 / 18.65 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">36.35 ± 1.03 / 51.91 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">27.22 ± 2.24 / 45.02 ± 1.74</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Llama-3-8B-flashback-v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,807 ± 1,152 / 979 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="sv ner">59.03 ± 2.04 / 41.99 ± 4.35</td> <!-- SUC3 -->
   <td class="sv sent">81.13 ± 0.94 / 80.80 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">33.06 ± 3.65 / 61.21 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.21 ± 0.67 / 64.01 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.69 / 18.01 ± 0.55</td> <!-- SweDN -->
   <td class="sv know">35.24 ± 0.83 / 50.70 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">25.14 ± 2.02 / 42.54 ± 1.99</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="sv ner">60.36 ± 2.84 / 39.37 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">79.74 ± 0.75 / 75.11 ± 1.91</td> <!-- SweReC -->
   <td class="sv la">28.24 ± 4.19 / 55.29 ± 5.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.73 ± 1.13 / 65.72 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.81 ± 0.24 / 18.56 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">35.86 ± 0.90 / 51.39 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">26.49 ± 1.89 / 44.41 ± 1.56</td> <!-- HellaSwag-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="sv ner">62.96 ± 2.62 / 51.99 ± 5.66</td> <!-- SUC3 -->
   <td class="sv sent">77.13 ± 2.43 / 78.36 ± 1.88</td> <!-- SweReC -->
   <td class="sv la">15.73 ± 7.07 / 47.41 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.43 ± 1.59 / 65.06 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.58 ± 0.22 / 22.52 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">32.54 ± 2.61 / 49.30 ± 1.93</td> <!-- MMLU-sv -->
   <td class="sv reason">34.94 ± 3.79 / 50.39 ± 3.23</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="sv ner">60.87 ± 3.71 / 47.40 ± 5.32</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.20 / 67.79 ± 2.37</td> <!-- SweReC -->
   <td class="sv la">6.78 ± 4.34 / 35.90 ± 2.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.75 ± 1.46 / 65.08 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.06 ± 0.31 / 23.91 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">33.71 ± 2.28 / 50.08 ± 1.68</td> <!-- MMLU-sv -->
   <td class="sv reason">41.45 ± 3.36 / 55.51 ± 2.69</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">43.68 ± 3.65 / 29.40 ± 3.10</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 4.50 / 77.58 ± 4.13</td> <!-- SweReC -->
   <td class="sv la">36.25 ± 2.66 / 65.08 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.62 ± 0.98 / 64.23 ± 0.88</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.44 ± 0.29 / 18.70 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">39.94 ± 1.17 / 53.25 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">25.96 ± 3.94 / 40.33 ± 3.17</td> <!-- HellaSwag-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   <td>12.9.1</td> <!-- SweDN version -->
   <td>12.9.1</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">3843</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="sv ner">55.91 ± 3.25 / 39.73 ± 4.94</td> <!-- SUC3 -->
   <td class="sv sent">64.52 ± 3.15 / 70.51 ± 2.49</td> <!-- SweReC -->
   <td class="sv la">23.85 ± 7.34 / 56.89 ± 6.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.88 ± 1.51 / 65.82 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.24 / 21.77 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">37.60 ± 3.30 / 52.46 ± 2.31</td> <!-- MMLU-sv -->
   <td class="sv reason">31.78 ± 2.98 / 47.11 ± 2.71</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="sv ner">46.57 ± 3.34 / 33.94 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.53 ± 2.55 / 77.96 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">33.43 ± 3.89 / 61.87 ± 4.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.87 ± 1.52 / 64.53 ± 1.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.76 ± 0.41 / 21.92 ± 0.79</td> <!-- SweDN -->
   <td class="sv know">28.89 ± 2.22 / 46.41 ± 1.55</td> <!-- MMLU-sv -->
   <td class="sv reason">30.36 ± 2.80 / 47.15 ± 2.26</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="sv ner">47.28 ± 3.05 / 34.01 ± 3.73</td> <!-- SUC3 -->
   <td class="sv sent">76.62 ± 2.52 / 78.04 ± 2.98</td> <!-- SweReC -->
   <td class="sv la">33.23 ± 4.72 / 61.29 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.00 ± 1.69 / 64.62 ± 1.44</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.68 ± 0.43 / 21.83 ± 0.75</td> <!-- SweDN -->
   <td class="sv know">29.95 ± 1.74 / 47.23 ± 1.24</td> <!-- MMLU-sv -->
   <td class="sv reason">31.12 ± 3.68 / 47.85 ± 2.80</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="sv ner">55.29 ± 3.95 / 41.59 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">78.29 ± 1.83 / 78.77 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">18.45 ± 3.00 / 46.38 ± 2.81</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.42 ± 1.64 / 63.83 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.54 ± 0.48 / 23.67 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 2.34 / 46.95 ± 1.75</td> <!-- MMLU-sv -->
   <td class="sv reason">37.45 ± 3.61 / 52.85 ± 2.76</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="sv ner">61.25 ± 3.35 / 50.76 ± 5.94</td> <!-- SUC3 -->
   <td class="sv sent">76.03 ± 2.11 / 78.25 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">16.28 ± 4.81 / 49.04 ± 3.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.96 ± 2.34 / 60.05 ± 1.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.35 ± 0.32 / 24.05 ± 0.66</td> <!-- SweDN -->
   <td class="sv know">32.30 ± 2.48 / 48.98 ± 1.96</td> <!-- MMLU-sv -->
   <td class="sv reason">38.78 ± 5.70 / 52.89 ± 4.91</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.51</td> <!-- ScandEval rank -->
   <td class="sv ner">59.36 ± 2.75 / 47.08 ± 4.17</td> <!-- SUC3 -->
   <td class="sv sent">72.04 ± 3.27 / 63.83 ± 2.07</td> <!-- SweReC -->
   <td class="sv la">22.38 ± 7.17 / 54.70 ± 5.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.96 ± 2.00 / 64.06 ± 1.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.13 ± 0.34 / 19.26 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">29.81 ± 2.25 / 47.46 ± 1.72</td> <!-- MMLU-sv -->
   <td class="sv reason">35.59 ± 3.75 / 51.76 ± 2.63</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="sv ner">56.21 ± 2.49 / 44.78 ± 4.19</td> <!-- SUC3 -->
   <td class="sv sent">78.30 ± 1.71 / 79.80 ± 2.03</td> <!-- SweReC -->
   <td class="sv la">14.35 ± 5.65 / 48.69 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">61.08 ± 1.47 / 65.72 ± 1.07</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.96 ± 0.40 / 24.14 ± 0.74</td> <!-- SweDN -->
   <td class="sv know">31.74 ± 2.48 / 48.52 ± 1.88</td> <!-- MMLU-sv -->
   <td class="sv reason">30.12 ± 2.07 / 47.58 ± 1.29</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama3-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,695 ± 1,277 / 532 ± 183</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="sv ner">63.19 ± 2.83 / 51.22 ± 3.61</td> <!-- SUC3 -->
   <td class="sv sent">76.06 ± 0.64 / 61.59 ± 0.77</td> <!-- SweReC -->
   <td class="sv la">5.34 ± 1.42 / 34.32 ± 0.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.70 ± 0.87 / 66.00 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.25 ± 0.16 / 20.28 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">36.23 ± 0.91 / 51.68 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">43.60 ± 1.33 / 56.86 ± 1.15</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">57.38 ± 1.93 / 29.69 ± 4.23</td> <!-- SUC3 -->
   <td class="sv sent">78.43 ± 0.93 / 74.54 ± 2.40</td> <!-- SweReC -->
   <td class="sv la">14.52 ± 2.43 / 45.18 ± 4.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.14 ± 1.81 / 63.00 ± 0.50</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.69 ± 0.22 / 19.95 ± 0.16</td> <!-- SweDN -->
   <td class="sv know">37.32 ± 0.70 / 52.95 ± 0.50</td> <!-- MMLU-sv -->
   <td class="sv reason">38.28 ± 1.31 / 53.70 ± 0.97</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">69.67 ± 1.30 / 52.94 ± 4.01</td> <!-- SUC3 -->
   <td class="sv sent">59.93 ± 4.70 / 67.54 ± 3.04</td> <!-- SweReC -->
   <td class="sv la">27.63 ± 3.19 / 60.85 ± 3.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.84 ± 1.61 / 60.85 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.60 ± 0.07 / 19.13 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">33.54 ± 1.40 / 49.20 ± 1.13</td> <!-- MMLU-sv -->
   <td class="sv reason">30.32 ± 2.27 / 45.96 ± 1.87</td> <!-- HellaSwag-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.55</td> <!-- ScandEval rank -->
   <td class="sv ner">44.14 ± 2.40 / 29.77 ± 4.06</td> <!-- SUC3 -->
   <td class="sv sent">80.14 ± 1.11 / 80.19 ± 0.78</td> <!-- SweReC -->
   <td class="sv la">34.23 ± 2.23 / 65.29 ± 2.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.07 ± 1.56 / 62.52 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.15 ± 0.31 / 18.72 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">33.24 ± 0.85 / 49.69 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">25.50 ± 2.25 / 43.44 ± 2.03</td> <!-- HellaSwag-sv -->
   <td>12.5.3</td> <!-- SUC3 version -->
   <td>12.5.3</td> <!-- SweReC version -->
   <td>12.5.3</td> <!-- ScaLA-sv version -->
   <td>12.5.3</td> <!-- ScandiQA-sv version -->
   <td>12.5.3</td> <!-- SweDN version -->
   <td>12.5.3</td> <!-- MMLU-sv version -->
   <td>12.5.3</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="sv ner">46.61 ± 3.11 / 34.10 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">76.38 ± 2.01 / 78.30 ± 2.42</td> <!-- SweReC -->
   <td class="sv la">34.16 ± 4.39 / 60.06 ± 4.67</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.77 ± 1.76 / 63.50 ± 1.47</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.77 ± 0.46 / 22.42 ± 0.84</td> <!-- SweDN -->
   <td class="sv know">29.77 ± 2.44 / 46.25 ± 1.64</td> <!-- MMLU-sv -->
   <td class="sv reason">25.38 ± 3.56 / 39.34 ± 3.89</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="sv ner">52.96 ± 3.45 / 41.51 ± 4.30</td> <!-- SUC3 -->
   <td class="sv sent">76.99 ± 2.37 / 76.84 ± 2.99</td> <!-- SweReC -->
   <td class="sv la">14.27 ± 4.36 / 40.60 ± 3.04</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.92 ± 1.64 / 64.87 ± 1.47</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.62 ± 0.42 / 23.90 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">27.95 ± 2.57 / 45.86 ± 1.85</td> <!-- MMLU-sv -->
   <td class="sv reason">36.11 ± 3.54 / 51.60 ± 2.44</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="sv ner">53.66 ± 3.57 / 41.97 ± 4.83</td> <!-- SUC3 -->
   <td class="sv sent">77.72 ± 2.51 / 78.40 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">16.22 ± 4.46 / 43.17 ± 3.88</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.75 ± 1.13 / 64.72 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.57 ± 0.48 / 23.65 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">27.24 ± 2.07 / 45.51 ± 1.53</td> <!-- MMLU-sv -->
   <td class="sv reason">32.04 ± 4.21 / 48.67 ± 3.11</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.2</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="sv ner">63.85 ± 2.67 / 47.77 ± 4.72</td> <!-- SUC3 -->
   <td class="sv sent">73.72 ± 2.98 / 62.83 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">-0.56 ± 2.24 / 33.54 ± 1.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.10 ± 1.48 / 66.26 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">68.11 ± 0.21 / 23.63 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">27.79 ± 2.32 / 45.82 ± 1.61</td> <!-- MMLU-sv -->
   <td class="sv reason">42.43 ± 2.76 / 56.52 ± 2.13</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="sv ner">48.36 ± 3.07 / 34.48 ± 5.22</td> <!-- SUC3 -->
   <td class="sv sent">76.57 ± 2.19 / 78.11 ± 2.73</td> <!-- SweReC -->
   <td class="sv la">20.94 ± 5.55 / 44.72 ± 4.06</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.07 ± 1.90 / 63.87 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.59 ± 0.50 / 22.19 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">31.44 ± 1.94 / 47.30 ± 1.54</td> <!-- MMLU-sv -->
   <td class="sv reason">26.04 ± 3.42 / 38.83 ± 4.24</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="sv ner">54.37 ± 3.04 / 42.16 ± 4.00</td> <!-- SUC3 -->
   <td class="sv sent">75.98 ± 1.15 / 74.44 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">17.98 ± 1.97 / 56.01 ± 2.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.07 ± 0.74 / 64.24 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.09 / 14.42 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">32.81 ± 0.91 / 49.28 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">36.24 ± 1.44 / 51.96 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.0.0</td> <!-- SUC3 version -->
   <td>12.0.0</td> <!-- SweReC version -->
   <td>12.0.0</td> <!-- ScaLA-sv version -->
   <td>12.0.0</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>12.0.0</td> <!-- MMLU-sv version -->
   <td>12.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="sv ner">58.90 ± 1.34 / 42.48 ± 3.97</td> <!-- SUC3 -->
   <td class="sv sent">67.74 ± 2.79 / 71.89 ± 1.89</td> <!-- SweReC -->
   <td class="sv la">16.52 ± 2.55 / 46.30 ± 2.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.41 ± 1.21 / 59.91 ± 0.48</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.09 ± 0.17 / 19.64 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">31.76 ± 0.89 / 48.64 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">45.84 ± 1.47 / 59.27 ± 1.16</td> <!-- HellaSwag-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="sv ner">58.40 ± 2.62 / 40.55 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">74.30 ± 1.26 / 60.35 ± 0.41</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.37 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.16 ± 1.23 / 65.78 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.36 ± 0.14 / 18.81 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">35.01 ± 0.99 / 51.07 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">43.72 ± 0.69 / 57.66 ± 0.50</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="sv ner">45.12 ± 2.72 / 30.73 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">78.74 ± 2.13 / 80.11 ± 2.64</td> <!-- SweReC -->
   <td class="sv la">19.74 ± 6.09 / 46.97 ± 5.83</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.15 ± 1.71 / 65.22 ± 1.28</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.41 ± 0.46 / 21.90 ± 0.70</td> <!-- SweDN -->
   <td class="sv know">31.24 ± 3.01 / 47.77 ± 2.19</td> <!-- MMLU-sv -->
   <td class="sv reason">22.30 ± 3.50 / 39.45 ± 2.60</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,431 ± 1,267 / 1,139 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="sv ner">48.19 ± 2.55 / 37.50 ± 3.62</td> <!-- SUC3 -->
   <td class="sv sent">79.95 ± 0.87 / 81.24 ± 0.64</td> <!-- SweReC -->
   <td class="sv la">32.85 ± 2.28 / 61.74 ± 3.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.52 / 63.58 ± 1.19</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.95 ± 0.25 / 20.56 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">25.32 ± 0.99 / 42.09 ± 1.04</td> <!-- MMLU-sv -->
   <td class="sv reason">14.55 ± 2.32 / 31.99 ± 2.16</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="sv ner">55.06 ± 2.38 / 41.39 ± 4.31</td> <!-- SUC3 -->
   <td class="sv sent">77.50 ± 0.90 / 73.87 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">17.47 ± 2.33 / 47.73 ± 3.35</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.67 ± 0.96 / 64.58 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.18 ± 0.24 / 18.13 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">31.04 ± 1.08 / 48.29 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">23.57 ± 1.68 / 42.37 ± 1.34</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="sv ner">60.53 ± 3.06 / 48.45 ± 5.19</td> <!-- SUC3 -->
   <td class="sv sent">67.03 ± 3.61 / 70.77 ± 1.95</td> <!-- SweReC -->
   <td class="sv la">15.10 ± 4.60 / 48.57 ± 2.91</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.46 ± 1.63 / 53.50 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.94 ± 0.21 / 22.99 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">27.51 ± 3.08 / 45.43 ± 2.37</td> <!-- MMLU-sv -->
   <td class="sv reason">42.29 ± 5.08 / 55.43 ± 4.50</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="sv ner">44.80 ± 2.36 / 34.91 ± 2.67</td> <!-- SUC3 -->
   <td class="sv sent">75.92 ± 2.44 / 75.77 ± 2.08</td> <!-- SweReC -->
   <td class="sv la">24.84 ± 2.78 / 59.88 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.71 ± 1.65 / 62.01 ± 1.64</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.65 ± 0.52 / 18.25 ± 0.41</td> <!-- SweDN -->
   <td class="sv know">26.71 ± 1.53 / 44.61 ± 1.21</td> <!-- MMLU-sv -->
   <td class="sv reason">30.43 ± 0.92 / 47.06 ± 0.83</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="sv ner">47.10 ± 2.60 / 35.06 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">73.05 ± 5.27 / 74.56 ± 4.19</td> <!-- SweReC -->
   <td class="sv la">30.29 ± 2.63 / 61.40 ± 3.22</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.39 ± 1.38 / 63.51 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.69 ± 0.53 / 19.03 ± 0.41</td> <!-- SweDN -->
   <td class="sv know">27.40 ± 0.76 / 44.17 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">21.08 ± 3.28 / 38.46 ± 2.96</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.4.0</td> <!-- MMLU-sv version -->
   <td>12.4.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="sv ner">54.52 ± 3.33 / 44.11 ± 5.29</td> <!-- SUC3 -->
   <td class="sv sent">78.45 ± 1.21 / 79.73 ± 0.97</td> <!-- SweReC -->
   <td class="sv la">21.55 ± 3.74 / 49.54 ± 4.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.71 ± 0.68 / 65.01 ± 0.64</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.59 ± 0.34 / 18.56 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">25.51 ± 0.81 / 43.68 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">14.97 ± 1.73 / 34.85 ± 1.34</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="sv ner">48.96 ± 2.72 / 39.25 ± 3.69</td> <!-- SUC3 -->
   <td class="sv sent">78.90 ± 0.95 / 78.62 ± 1.08</td> <!-- SweReC -->
   <td class="sv la">10.82 ± 3.46 / 38.95 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.91 ± 1.02 / 64.72 ± 0.76</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.33 / 19.24 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.52 ± 1.19 / 50.47 ± 0.93</td> <!-- MMLU-sv -->
   <td class="sv reason">20.96 ± 1.96 / 39.95 ± 1.66</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.1</td> <!-- SweReC version -->
   <td>12.5.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.5.1</td> <!-- SweDN version -->
   <td>12.5.1</td> <!-- MMLU-sv version -->
   <td>12.5.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="sv ner">53.00 ± 2.53 / 39.09 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">79.70 ± 0.65 / 79.45 ± 0.68</td> <!-- SweReC -->
   <td class="sv la">4.32 ± 2.19 / 34.43 ± 0.87</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.03 ± 1.03 / 64.74 ± 0.84</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.89 ± 0.28 / 19.31 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">35.48 ± 0.99 / 51.54 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">20.54 ± 2.14 / 39.66 ± 1.80</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="sv ner">53.34 ± 2.55 / 40.48 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">80.00 ± 0.70 / 79.80 ± 0.66</td> <!-- SweReC -->
   <td class="sv la">4.61 ± 2.18 / 34.51 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.99 ± 1.05 / 64.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.87 ± 0.31 / 19.30 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">35.52 ± 1.01 / 51.52 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">19.67 ± 2.31 / 38.98 ± 1.98</td> <!-- HellaSwag-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.1.2</td> <!-- MMLU-sv version -->
   <td>9.1.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="sv ner">49.18 ± 2.71 / 39.25 ± 3.60</td> <!-- SUC3 -->
   <td class="sv sent">79.08 ± 0.77 / 78.81 ± 0.94</td> <!-- SweReC -->
   <td class="sv la">11.06 ± 3.55 / 38.96 ± 3.77</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 1.04 / 64.79 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.79 ± 0.32 / 19.30 ± 0.42</td> <!-- SweDN -->
   <td class="sv know">34.51 ± 1.13 / 50.46 ± 0.88</td> <!-- MMLU-sv -->
   <td class="sv reason">20.84 ± 2.19 / 39.88 ± 1.85</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="sv ner">52.34 ± 3.07 / 39.14 ± 4.60</td> <!-- SUC3 -->
   <td class="sv sent">77.66 ± 2.09 / 78.59 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.00 ± 4.15 / 36.34 ± 2.20</td> <!-- ScaLA-sv -->
   <td class="sv rc">60.16 ± 1.81 / 64.12 ± 1.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.54 ± 0.49 / 19.31 ± 0.71</td> <!-- SweDN -->
   <td class="sv know">31.83 ± 2.27 / 48.55 ± 1.67</td> <!-- MMLU-sv -->
   <td class="sv reason">20.55 ± 3.93 / 38.95 ± 3.23</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.1</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,141 ± 994 / 905 ± 299</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="sv ner">36.45 ± 2.44 / 27.24 ± 2.29</td> <!-- SUC3 -->
   <td class="sv sent">81.12 ± 1.02 / 77.04 ± 2.74</td> <!-- SweReC -->
   <td class="sv la">26.80 ± 2.07 / 59.15 ± 2.72</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.16 ± 0.82 / 64.72 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.09 ± 0.31 / 20.48 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">29.01 ± 0.68 / 45.32 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">15.92 ± 1.74 / 35.28 ± 1.24</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="sv ner">48.43 ± 2.75 / 35.31 ± 2.80</td> <!-- SUC3 -->
   <td class="sv sent">79.43 ± 0.85 / 78.21 ± 1.69</td> <!-- SweReC -->
   <td class="sv la">17.37 ± 2.57 / 52.91 ± 4.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.05 ± 1.22 / 62.72 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.81 ± 0.34 / 18.13 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">31.72 ± 0.55 / 48.70 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">15.69 ± 2.43 / 35.96 ± 2.03</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="sv ner">44.94 ± 2.91 / 35.67 ± 3.53</td> <!-- SUC3 -->
   <td class="sv sent">76.78 ± 1.63 / 78.27 ± 1.22</td> <!-- SweReC -->
   <td class="sv la">16.96 ± 2.77 / 55.03 ± 3.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.83 ± 1.02 / 63.13 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.09 ± 0.37 / 19.37 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">26.57 ± 1.18 / 44.19 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">24.62 ± 2.11 / 42.11 ± 1.50</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="sv ner">49.90 ± 2.28 / 35.48 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">77.19 ± 2.05 / 79.13 ± 1.43</td> <!-- SweReC -->
   <td class="sv la">14.67 ± 2.27 / 53.90 ± 2.24</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.12 ± 0.70 / 63.72 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.25 ± 0.10 / 19.64 ± 0.19</td> <!-- SweDN -->
   <td class="sv know">24.40 ± 1.20 / 42.73 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">19.30 ± 1.27 / 38.75 ± 1.05</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.11.0</td> <!-- ScandiQA-sv version -->
   <td>12.11.0</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="sv ner">44.64 ± 1.66 / 31.30 ± 2.96</td> <!-- SUC3 -->
   <td class="sv sent">77.98 ± 1.01 / 72.79 ± 2.47</td> <!-- SweReC -->
   <td class="sv la">16.57 ± 2.58 / 51.86 ± 3.69</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.31 ± 0.92 / 63.73 ± 1.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.23 ± 0.35 / 15.35 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">28.15 ± 0.90 / 45.69 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">23.58 ± 1.41 / 42.30 ± 1.04</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="sv ner">42.23 ± 2.44 / 30.30 ± 4.71</td> <!-- SUC3 -->
   <td class="sv sent">78.80 ± 0.93 / 75.28 ± 1.78</td> <!-- SweReC -->
   <td class="sv la">15.47 ± 1.79 / 54.26 ± 3.41</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.75 ± 1.15 / 62.43 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.78 ± 0.76 / 16.74 ± 0.45</td> <!-- SweDN -->
   <td class="sv know">30.86 ± 1.12 / 47.83 ± 0.93</td> <!-- MMLU-sv -->
   <td class="sv reason">19.11 ± 2.74 / 38.55 ± 2.29</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.4.0</td> <!-- SweReC version -->
   <td>12.4.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.4.0</td> <!-- MMLU-sv version -->
   <td>12.4.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="sv ner">60.04 ± 1.22 / 43.93 ± 3.63</td> <!-- SUC3 -->
   <td class="sv sent">76.21 ± 0.85 / 67.87 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">7.54 ± 2.52 / 35.42 ± 1.33</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.60 ± 0.59 / 63.65 ± 0.30</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.00 ± 0.55 / 18.11 ± 0.35</td> <!-- SweDN -->
   <td class="sv know">20.97 ± 0.82 / 39.72 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">28.96 ± 2.18 / 46.32 ± 1.64</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-13B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 645 / 709 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="sv ner">49.26 ± 2.31 / 36.92 ± 4.05</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 0.80 / 77.87 ± 2.06</td> <!-- SweReC -->
   <td class="sv la">0.22 ± 0.43 / 33.38 ± 0.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.78 ± 1.02 / 63.61 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.99 ± 0.07 / 19.57 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">25.56 ± 0.86 / 43.67 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">28.26 ± 1.97 / 45.89 ± 1.42</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="sv ner">43.74 ± 2.58 / 34.37 ± 2.59</td> <!-- SUC3 -->
   <td class="sv sent">76.98 ± 1.31 / 71.38 ± 3.20</td> <!-- SweReC -->
   <td class="sv la">16.01 ± 2.24 / 51.83 ± 3.50</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.38 ± 1.78 / 57.83 ± 0.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.98 ± 0.47 / 17.53 ± 0.50</td> <!-- SweDN -->
   <td class="sv know">29.44 ± 0.61 / 47.21 ± 0.47</td> <!-- MMLU-sv -->
   <td class="sv reason">22.42 ± 1.89 / 41.45 ± 1.49</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="sv ner">47.92 ± 2.66 / 33.00 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">62.90 ± 2.44 / 70.61 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">19.95 ± 2.24 / 56.49 ± 2.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.51 ± 0.36 / 61.42 ± 0.52</td> <!-- ScandiQA-sv -->
   <td class="sv summ">66.11 ± 0.18 / 19.64 ± 0.28</td> <!-- SweDN -->
   <td class="sv know">25.60 ± 1.10 / 43.53 ± 0.90</td> <!-- MMLU-sv -->
   <td class="sv reason">21.75 ± 1.61 / 40.57 ± 1.45</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="sv ner">46.74 ± 4.30 / 33.57 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">77.06 ± 1.82 / 79.02 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">14.00 ± 1.59 / 53.89 ± 3.10</td> <!-- ScaLA-sv -->
   <td class="sv rc">56.74 ± 0.52 / 63.45 ± 0.49</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.56 ± 0.85 / 15.85 ± 0.34</td> <!-- SweDN -->
   <td class="sv know">30.87 ± 1.35 / 47.77 ± 1.01</td> <!-- MMLU-sv -->
   <td class="sv reason">15.79 ± 1.57 / 35.66 ± 0.84</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="sv ner">51.73 ± 4.51 / 40.50 ± 6.05</td> <!-- SUC3 -->
   <td class="sv sent">36.06 ± 3.31 / 53.46 ± 1.79</td> <!-- SweReC -->
   <td class="sv la">19.42 ± 5.08 / 46.92 ± 5.36</td> <!-- ScaLA-sv -->
   <td class="sv rc">59.26 ± 1.66 / 64.40 ± 1.35</td> <!-- ScandiQA-sv -->
   <td class="sv summ">67.55 ± 0.53 / 23.64 ± 0.72</td> <!-- SweDN -->
   <td class="sv know">23.10 ± 2.38 / 42.58 ± 1.74</td> <!-- MMLU-sv -->
   <td class="sv reason">29.31 ± 5.03 / 47.11 ± 3.62</td> <!-- HellaSwag-sv -->
   <td>9.3.0</td> <!-- SUC3 version -->
   <td>9.3.0</td> <!-- SweReC version -->
   <td>9.3.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>9.3.0</td> <!-- SweDN version -->
   <td>9.3.0</td> <!-- MMLU-sv version -->
   <td>9.3.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="sv ner">35.61 ± 2.19 / 26.05 ± 2.45</td> <!-- SUC3 -->
   <td class="sv sent">75.84 ± 1.41 / 77.22 ± 1.09</td> <!-- SweReC -->
   <td class="sv la">15.62 ± 1.67 / 51.30 ± 3.09</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.76 ± 0.92 / 58.65 ± 0.83</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.16 ± 0.13 / 18.88 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">27.00 ± 0.89 / 44.95 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">31.43 ± 1.21 / 47.99 ± 0.85</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="sv ner">50.85 ± 2.44 / 39.65 ± 3.83</td> <!-- SUC3 -->
   <td class="sv sent">74.17 ± 2.12 / 76.62 ± 1.83</td> <!-- SweReC -->
   <td class="sv la">7.51 ± 1.94 / 37.81 ± 1.76</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.32 ± 0.63 / 63.28 ± 0.71</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.20 ± 0.45 / 19.06 ± 0.15</td> <!-- SweDN -->
   <td class="sv know">23.92 ± 0.88 / 42.25 ± 0.73</td> <!-- MMLU-sv -->
   <td class="sv reason">17.67 ± 1.53 / 37.32 ± 1.20</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="sv ner">51.06 ± 2.85 / 31.63 ± 3.67</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 1.09 / 67.88 ± 3.15</td> <!-- SweReC -->
   <td class="sv la">5.88 ± 3.89 / 38.51 ± 4.84</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.43 ± 1.04 / 62.93 ± 0.94</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.73 ± 0.74 / 17.61 ± 0.49</td> <!-- SweDN -->
   <td class="sv know">27.05 ± 1.14 / 44.68 ± 0.87</td> <!-- MMLU-sv -->
   <td class="sv reason">13.30 ± 1.20 / 33.89 ± 1.04</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="sv ner">47.67 ± 2.81 / 36.91 ± 3.50</td> <!-- SUC3 -->
   <td class="sv sent">71.73 ± 2.40 / 74.97 ± 1.84</td> <!-- SweReC -->
   <td class="sv la">7.90 ± 3.20 / 41.24 ± 4.78</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.78 ± 0.79 / 64.48 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.07 ± 0.34 / 19.59 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">25.52 ± 1.30 / 43.68 ± 1.03</td> <!-- MMLU-sv -->
   <td class="sv reason">14.06 ± 1.68 / 35.12 ± 1.47</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.2.0</td> <!-- SweReC version -->
   <td>12.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.1</td> <!-- MMLU-sv version -->
   <td>12.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="sv ner">45.55 ± 2.18 / 26.78 ± 3.65</td> <!-- SUC3 -->
   <td class="sv sent">70.71 ± 1.99 / 71.19 ± 1.14</td> <!-- SweReC -->
   <td class="sv la">4.83 ± 3.48 / 36.64 ± 2.95</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.25 ± 1.21 / 61.21 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.18 ± 0.45 / 17.62 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">26.05 ± 0.80 / 44.56 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">27.09 ± 1.66 / 44.95 ± 1.30</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="sv ner">49.02 ± 3.23 / 41.69 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">76.56 ± 1.52 / 78.16 ± 1.12</td> <!-- SweReC -->
   <td class="sv la">2.18 ± 2.34 / 36.26 ± 3.89</td> <!-- ScaLA-sv -->
   <td class="sv rc">58.98 ± 0.95 / 63.65 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.42 ± 0.45 / 18.79 ± 0.47</td> <!-- SweDN -->
   <td class="sv know">23.68 ± 1.41 / 42.15 ± 1.14</td> <!-- MMLU-sv -->
   <td class="sv reason">14.05 ± 1.60 / 34.81 ± 1.58</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="sv ner">46.69 ± 2.39 / 32.97 ± 4.57</td> <!-- SUC3 -->
   <td class="sv sent">75.39 ± 1.06 / 71.95 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">2.91 ± 2.80 / 35.26 ± 2.12</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.95 ± 0.86 / 60.77 ± 0.75</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.70 ± 0.76 / 17.52 ± 0.40</td> <!-- SweDN -->
   <td class="sv know">25.28 ± 0.72 / 43.71 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">19.20 ± 1.18 / 38.76 ± 0.96</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="sv ner">45.01 ± 2.11 / 27.59 ± 3.35</td> <!-- SUC3 -->
   <td class="sv sent">73.33 ± 1.98 / 76.19 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">11.59 ± 3.45 / 40.89 ± 4.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.12 ± 1.42 / 59.29 ± 1.17</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.10 ± 0.60 / 18.05 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">24.03 ± 1.09 / 42.32 ± 0.70</td> <!-- MMLU-sv -->
   <td class="sv reason">15.37 ± 0.71 / 35.78 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="sv ner">54.38 ± 2.92 / 39.66 ± 5.20</td> <!-- SUC3 -->
   <td class="sv sent">55.84 ± 2.51 / 66.96 ± 1.37</td> <!-- SweReC -->
   <td class="sv la">16.05 ± 2.15 / 54.22 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.22 ± 0.88 / 61.85 ± 0.63</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.90 ± 0.14 / 16.99 ± 0.20</td> <!-- SweDN -->
   <td class="sv know">22.36 ± 1.17 / 41.14 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">12.52 ± 1.41 / 33.90 ± 1.11</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="sv ner">44.11 ± 4.26 / 31.64 ± 4.48</td> <!-- SUC3 -->
   <td class="sv sent">79.05 ± 1.08 / 75.52 ± 2.66</td> <!-- SweReC -->
   <td class="sv la">7.34 ± 3.19 / 43.83 ± 5.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.49 ± 0.95 / 63.16 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.63 ± 0.39 / 18.68 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">15.65 ± 0.55 / 36.32 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">8.74 ± 1.34 / 29.87 ± 1.40</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="sv ner">53.95 ± 1.89 / 42.16 ± 4.59</td> <!-- SUC3 -->
   <td class="sv sent">60.91 ± 2.35 / 59.47 ± 1.21</td> <!-- SweReC -->
   <td class="sv la">0.32 ± 0.62 / 33.39 ± 0.28</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.28 ± 0.62 / 63.41 ± 0.55</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.73 ± 0.18 / 15.64 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">20.96 ± 0.77 / 40.70 ± 0.59</td> <!-- MMLU-sv -->
   <td class="sv reason">25.76 ± 1.39 / 43.71 ± 1.09</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="sv ner">41.25 ± 2.07 / 32.87 ± 2.49</td> <!-- SUC3 -->
   <td class="sv sent">76.60 ± 0.98 / 64.63 ± 2.41</td> <!-- SweReC -->
   <td class="sv la">6.37 ± 2.08 / 49.55 ± 3.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.87 ± 0.64 / 61.35 ± 0.68</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.90 ± 0.52 / 17.15 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">16.18 ± 0.78 / 34.88 ± 0.66</td> <!-- MMLU-sv -->
   <td class="sv reason">8.52 ± 1.90 / 29.96 ± 1.75</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="sv ner">59.77 ± 3.55 / 45.71 ± 4.91</td> <!-- SUC3 -->
   <td class="sv sent">74.45 ± 1.19 / 72.26 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">3.97 ± 1.50 / 34.79 ± 0.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 1.05 / 56.07 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.61 ± 0.55 / 17.92 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">14.34 ± 0.73 / 35.93 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">7.40 ± 1.39 / 30.20 ± 1.23</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="sv ner">39.72 ± 2.82 / 29.85 ± 2.99</td> <!-- SUC3 -->
   <td class="sv sent">66.18 ± 3.25 / 72.00 ± 1.75</td> <!-- SweReC -->
   <td class="sv la">6.74 ± 1.66 / 45.55 ± 4.31</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.05 ± 0.84 / 60.90 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.92 ± 0.05 / 18.51 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">17.73 ± 0.98 / 37.55 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">12.85 ± 0.93 / 33.37 ± 0.90</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">3.15</td> <!-- ScandEval rank -->
   <td class="sv ner">32.37 ± 3.05 / 24.60 ± 3.81</td> <!-- SUC3 -->
   <td class="sv sent">75.33 ± 2.41 / 77.99 ± 2.58</td> <!-- SweReC -->
   <td class="sv la">12.73 ± 6.32 / 45.51 ± 7.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.05 ± 1.83 / 58.32 ± 1.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.74 ± 0.74 / 19.59 ± 0.87</td> <!-- SweDN -->
   <td class="sv know">15.60 ± 1.96 / 33.16 ± 1.77</td> <!-- MMLU-sv -->
   <td class="sv reason">9.81 ± 2.55 / 28.12 ± 2.70</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>10.0.1</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="sv ner">45.23 ± 3.64 / 37.99 ± 4.03</td> <!-- SUC3 -->
   <td class="sv sent">72.76 ± 2.25 / 72.65 ± 2.38</td> <!-- SweReC -->
   <td class="sv la">11.25 ± 2.04 / 51.22 ± 3.26</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.22 ± 0.70 / 59.36 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.56 ± 0.78 / 17.51 ± 0.44</td> <!-- SweDN -->
   <td class="sv know">18.14 ± 1.00 / 38.28 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">6.77 ± 1.16 / 28.93 ± 0.94</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="sv ner">46.15 ± 2.77 / 24.28 ± 3.74</td> <!-- SUC3 -->
   <td class="sv sent">67.17 ± 1.93 / 70.99 ± 1.64</td> <!-- SweReC -->
   <td class="sv la">5.30 ± 1.62 / 47.01 ± 3.23</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.12 ± 1.02 / 57.49 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.20 ± 0.99 / 15.57 ± 0.62</td> <!-- SweDN -->
   <td class="sv know">21.33 ± 1.03 / 41.04 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">16.12 ± 1.15 / 36.99 ± 0.85</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="sv ner">40.19 ± 2.97 / 31.88 ± 4.51</td> <!-- SUC3 -->
   <td class="sv sent">64.08 ± 2.44 / 69.62 ± 1.29</td> <!-- SweReC -->
   <td class="sv la">5.43 ± 2.02 / 38.32 ± 2.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.21 ± 1.08 / 59.57 ± 0.97</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.90 ± 0.87 / 17.34 ± 0.52</td> <!-- SweDN -->
   <td class="sv know">20.95 ± 0.97 / 40.87 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">16.59 ± 1.45 / 36.76 ± 1.20</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="sv ner">52.85 ± 2.76 / 35.11 ± 3.66</td> <!-- SUC3 -->
   <td class="sv sent">73.93 ± 1.58 / 73.97 ± 1.19</td> <!-- SweReC -->
   <td class="sv la">8.27 ± 2.90 / 43.29 ± 4.82</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.49 ± 0.77 / 54.50 ± 0.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.98 ± 0.80 / 16.18 ± 0.48</td> <!-- SweDN -->
   <td class="sv know">13.69 ± 0.86 / 33.34 ± 0.46</td> <!-- MMLU-sv -->
   <td class="sv reason">5.68 ± 1.13 / 27.99 ± 1.11</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="sv ner">30.45 ± 3.49 / 23.98 ± 3.18</td> <!-- SUC3 -->
   <td class="sv sent">76.36 ± 1.10 / 65.98 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">6.06 ± 2.07 / 49.80 ± 2.71</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.19 ± 0.71 / 60.59 ± 0.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.12 ± 0.69 / 17.92 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">20.80 ± 0.90 / 40.36 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">6.24 ± 1.13 / 28.87 ± 1.03</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-40b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">39927</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1795</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">409 ± 53 / 182 ± 54</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="sv ner">32.00 ± 3.27 / 17.02 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">80.44 ± 0.54 / 77.81 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">10.73 ± 2.53 / 51.37 ± 4.05</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.80 ± 0.86 / 60.53 ± 0.78</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.16 ± 0.50 / 19.50 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">8.35 ± 0.95 / 30.38 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">5.74 ± 1.30 / 28.98 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>12.9.1</td> <!-- SweDN version -->
   <td>12.9.1</td> <!-- MMLU-sv version -->
   <td>12.9.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Phi-3-mini-4k-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,360 ± 179 / 566 ± 190</td> <!-- Model inference speed -->
   <td class="rank">3.22</td> <!-- ScandEval rank -->
   <td class="sv ner">47.81 ± 2.60 / 27.94 ± 5.79</td> <!-- SUC3 -->
   <td class="sv sent">68.43 ± 2.12 / 68.82 ± 2.65</td> <!-- SweReC -->
   <td class="sv la">3.63 ± 1.46 / 43.69 ± 4.56</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.03 ± 0.62 / 58.80 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.14 ± 0.47 / 11.16 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">23.29 ± 1.03 / 42.63 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">12.06 ± 1.23 / 33.77 ± 0.99</td> <!-- HellaSwag-sv -->
   <td>12.10.4</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.4</td> <!-- ScaLA-sv version -->
   <td>12.10.4</td> <!-- ScandiQA-sv version -->
   <td>12.10.4</td> <!-- SweDN version -->
   <td>12.10.4</td> <!-- MMLU-sv version -->
   <td>12.10.4</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4065</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="sv ner">23.88 ± 7.28 / 17.99 ± 3.56</td> <!-- SUC3 -->
   <td class="sv sent">80.26 ± 0.89 / 77.89 ± 0.89</td> <!-- SweReC -->
   <td class="sv la">13.50 ± 2.27 / 52.55 ± 2.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">55.02 ± 0.96 / 60.74 ± 0.89</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.78 ± 0.63 / 18.68 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">6.62 ± 0.88 / 27.61 ± 0.74</td> <!-- MMLU-sv -->
   <td class="sv reason">2.66 ± 1.04 / 26.32 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="sv ner">36.54 ± 2.70 / 28.79 ± 3.85</td> <!-- SUC3 -->
   <td class="sv sent">68.85 ± 5.19 / 70.02 ± 3.95</td> <!-- SweReC -->
   <td class="sv la">2.60 ± 2.58 / 40.21 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.58 ± 0.89 / 59.78 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.77 ± 1.85 / 17.01 ± 0.69</td> <!-- SweDN -->
   <td class="sv know">16.19 ± 1.01 / 37.23 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">14.06 ± 1.52 / 34.80 ± 1.35</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">130819</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.27</td> <!-- ScandEval rank -->
   <td class="sv ner">42.36 ± 1.67 / 21.33 ± 2.90</td> <!-- SUC3 -->
   <td class="sv sent">51.53 ± 6.32 / 62.14 ± 3.43</td> <!-- SweReC -->
   <td class="sv la">3.11 ± 1.60 / 47.93 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.11 ± 0.96 / 57.21 ± 0.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.28 ± 0.86 / 15.52 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">22.99 ± 1.08 / 42.27 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">20.19 ± 0.99 / 40.11 ± 0.71</td> <!-- HellaSwag-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.9.1</td> <!-- ScaLA-sv version -->
   <td>12.9.1</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="sv ner">31.86 ± 5.09 / 21.95 ± 3.90</td> <!-- SUC3 -->
   <td class="sv sent">79.20 ± 1.03 / 79.87 ± 1.11</td> <!-- SweReC -->
   <td class="sv la">12.26 ± 1.97 / 46.90 ± 4.11</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.58 ± 0.97 / 60.28 ± 0.81</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.14 ± 0.46 / 18.76 ± 0.39</td> <!-- SweDN -->
   <td class="sv know">3.15 ± 0.80 / 27.43 ± 0.91</td> <!-- MMLU-sv -->
   <td class="sv reason">2.77 ± 1.26 / 26.43 ± 0.84</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>12.10.0</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="sv ner">42.87 ± 3.17 / 40.34 ± 2.52</td> <!-- SUC3 -->
   <td class="sv sent">79.18 ± 0.46 / 76.66 ± 1.44</td> <!-- SweReC -->
   <td class="sv la">8.65 ± 1.60 / 46.95 ± 3.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.56 ± 0.79 / 57.58 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.66 ± 0.41 / 18.04 ± 0.38</td> <!-- SweDN -->
   <td class="sv know">2.37 ± 1.04 / 24.51 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">0.17 ± 0.83 / 25.26 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.33</td> <!-- ScandEval rank -->
   <td class="sv ner">40.68 ± 2.32 / 24.33 ± 2.43</td> <!-- SUC3 -->
   <td class="sv sent">68.96 ± 2.04 / 72.76 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">4.77 ± 1.97 / 43.64 ± 5.60</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.73 ± 0.76 / 56.63 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.93 ± 0.49 / 14.76 ± 0.77</td> <!-- SweDN -->
   <td class="sv know">13.55 ± 1.27 / 34.97 ± 0.99</td> <!-- MMLU-sv -->
   <td class="sv reason">5.27 ± 1.49 / 27.92 ± 1.10</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">3.33</td> <!-- ScandEval rank -->
   <td class="sv ner">47.24 ± 3.36 / 24.94 ± 3.21</td> <!-- SUC3 -->
   <td class="sv sent">77.91 ± 1.42 / 76.08 ± 2.54</td> <!-- SweReC -->
   <td class="sv la">5.55 ± 2.55 / 48.57 ± 3.21</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.41 ± 0.74 / 57.55 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.11 ± 1.02 / 17.57 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">1.49 ± 1.11 / 25.90 ± 0.71</td> <!-- MMLU-sv -->
   <td class="sv reason">3.97 ± 0.92 / 27.45 ± 0.68</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="sv ner">41.49 ± 2.82 / 38.09 ± 2.86</td> <!-- SUC3 -->
   <td class="sv sent">75.64 ± 1.51 / 76.06 ± 1.42</td> <!-- SweReC -->
   <td class="sv la">0.66 ± 1.97 / 33.73 ± 0.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">57.48 ± 0.54 / 63.85 ± 0.46</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.94 ± 1.10 / 13.29 ± 0.34</td> <!-- SweDN -->
   <td class="sv know">10.56 ± 1.14 / 31.45 ± 0.92</td> <!-- MMLU-sv -->
   <td class="sv reason">5.03 ± 1.36 / 28.41 ± 0.76</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="sv ner">24.98 ± 2.04 / 25.50 ± 1.92</td> <!-- SUC3 -->
   <td class="sv sent">79.36 ± 1.35 / 76.34 ± 3.44</td> <!-- SweReC -->
   <td class="sv la">5.75 ± 2.23 / 41.27 ± 4.75</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.74 ± 0.84 / 60.74 ± 0.65</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.60 ± 1.09 / 18.36 ± 0.56</td> <!-- SweDN -->
   <td class="sv know">3.83 ± 1.03 / 26.46 ± 0.77</td> <!-- MMLU-sv -->
   <td class="sv reason">4.40 ± 1.42 / 28.14 ± 1.05</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="sv ner">59.26 ± 2.00 / 52.73 ± 2.71</td> <!-- SUC3 -->
   <td class="sv sent">28.63 ± 1.24 / 50.95 ± 0.75</td> <!-- SweReC -->
   <td class="sv la">11.43 ± 1.88 / 53.31 ± 1.74</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.67 ± 1.97 / 53.24 ± 1.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.88 ± 0.30 / 18.58 ± 0.16</td> <!-- SweDN -->
   <td class="sv know">17.95 ± 1.18 / 36.41 ± 1.02</td> <!-- MMLU-sv -->
   <td class="sv reason">13.55 ± 1.32 / 33.39 ± 1.32</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="sv ner">51.45 ± 3.13 / 26.49 ± 3.00</td> <!-- SUC3 -->
   <td class="sv sent">63.64 ± 3.74 / 65.08 ± 2.46</td> <!-- SweReC -->
   <td class="sv la">5.80 ± 1.74 / 51.04 ± 1.54</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.95 ± 1.00 / 57.09 ± 0.92</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.18 ± 0.57 / 16.32 ± 0.33</td> <!-- SweDN -->
   <td class="sv know">4.88 ± 0.59 / 25.13 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">4.63 ± 1.09 / 27.29 ± 1.02</td> <!-- HellaSwag-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="sv ner">28.73 ± 3.63 / 20.43 ± 3.72</td> <!-- SUC3 -->
   <td class="sv sent">77.47 ± 1.36 / 78.60 ± 1.25</td> <!-- SweReC -->
   <td class="sv la">8.78 ± 2.01 / 42.28 ± 3.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.57 ± 0.94 / 56.51 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">62.41 ± 0.85 / 16.45 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">5.23 ± 1.02 / 28.63 ± 0.82</td> <!-- MMLU-sv -->
   <td class="sv reason">5.39 ± 0.81 / 28.86 ± 0.60</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-33B@1000B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,080 ± 700 / 331 ± 117</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="sv ner">42.35 ± 1.51 / 28.31 ± 3.87</td> <!-- SUC3 -->
   <td class="sv sent">77.68 ± 1.11 / 78.86 ± 0.93</td> <!-- SweReC -->
   <td class="sv la">8.08 ± 1.69 / 50.52 ± 2.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.57 ± 1.25 / 60.34 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.30 ± 1.94 / 14.29 ± 0.83</td> <!-- SweDN -->
   <td class="sv know">1.73 ± 1.04 / 24.98 ± 0.69</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.32 ± 1.25 / 25.53 ± 0.82</td> <!-- HellaSwag-sv -->
   <td>12.9.0</td> <!-- SUC3 version -->
   <td>12.9.0</td> <!-- SweReC version -->
   <td>12.9.0</td> <!-- ScaLA-sv version -->
   <td>12.9.0</td> <!-- ScandiQA-sv version -->
   <td>12.9.0</td> <!-- SweDN version -->
   <td>12.9.0</td> <!-- MMLU-sv version -->
   <td>12.9.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="sv ner">15.70 ± 1.54 / 14.65 ± 1.52</td> <!-- SUC3 -->
   <td class="sv sent">68.23 ± 3.81 / 71.17 ± 3.07</td> <!-- SweReC -->
   <td class="sv la">12.39 ± 1.39 / 50.99 ± 3.37</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.04 ± 0.97 / 60.86 ± 0.77</td> <!-- ScandiQA-sv -->
   <td class="sv summ">65.44 ± 0.22 / 19.75 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">6.86 ± 0.91 / 29.83 ± 1.12</td> <!-- MMLU-sv -->
   <td class="sv reason">6.92 ± 0.75 / 28.96 ± 0.67</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>9.3.1</td> <!-- ScandiQA-sv version -->
   <td>9.3.1</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.44</td> <!-- ScandEval rank -->
   <td class="sv ner">48.78 ± 5.08 / 26.81 ± 3.42</td> <!-- SUC3 -->
   <td class="sv sent">76.09 ± 1.23 / 74.78 ± 1.97</td> <!-- SweReC -->
   <td class="sv la">2.53 ± 2.80 / 47.37 ± 2.29</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.93 ± 0.97 / 55.09 ± 0.85</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.49 ± 2.27 / 16.17 ± 0.78</td> <!-- SweDN -->
   <td class="sv know">1.28 ± 1.28 / 23.12 ± 0.63</td> <!-- MMLU-sv -->
   <td class="sv reason">1.27 ± 0.61 / 25.74 ± 0.70</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="sv ner">31.55 ± 4.67 / 18.37 ± 2.73</td> <!-- SUC3 -->
   <td class="sv sent">78.66 ± 1.03 / 78.34 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">5.69 ± 2.24 / 44.98 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.93 ± 1.30 / 57.87 ± 1.27</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.05 ± 1.20 / 13.94 ± 0.43</td> <!-- SweDN -->
   <td class="sv know">1.32 ± 1.02 / 23.28 ± 0.65</td> <!-- MMLU-sv -->
   <td class="sv reason">0.35 ± 0.66 / 25.33 ± 0.66</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.47</td> <!-- ScandEval rank -->
   <td class="sv ner">41.60 ± 2.74 / 37.22 ± 3.26</td> <!-- SUC3 -->
   <td class="sv sent">71.86 ± 2.01 / 71.15 ± 2.16</td> <!-- SweReC -->
   <td class="sv la">3.72 ± 1.40 / 48.04 ± 1.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.57 ± 1.35 / 52.90 ± 1.42</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.69 ± 0.79 / 13.27 ± 0.37</td> <!-- SweDN -->
   <td class="sv know">14.64 ± 0.91 / 35.56 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">3.10 ± 0.87 / 26.60 ± 0.68</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="sv ner">38.00 ± 4.39 / 29.74 ± 5.04</td> <!-- SUC3 -->
   <td class="sv sent">75.15 ± 0.55 / 61.46 ± 0.82</td> <!-- SweReC -->
   <td class="sv la">1.04 ± 2.08 / 34.49 ± 1.17</td> <!-- ScaLA-sv -->
   <td class="sv rc">53.11 ± 0.53 / 58.91 ± 0.32</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.63 ± 1.02 / 13.45 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">8.72 ± 0.93 / 30.92 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">3.19 ± 0.62 / 26.88 ± 0.62</td> <!-- HellaSwag-sv -->
   <td>12.10.8</td> <!-- SUC3 version -->
   <td>12.10.8</td> <!-- SweReC version -->
   <td>12.10.8</td> <!-- ScaLA-sv version -->
   <td>12.10.8</td> <!-- ScandiQA-sv version -->
   <td>12.10.8</td> <!-- SweDN version -->
   <td>12.10.8</td> <!-- MMLU-sv version -->
   <td>12.10.8</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="sv ner">36.01 ± 3.07 / 24.61 ± 4.22</td> <!-- SUC3 -->
   <td class="sv sent">57.18 ± 5.33 / 62.72 ± 5.30</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 2.14 / 38.30 ± 3.62</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.04 ± 0.95 / 56.97 ± 0.96</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.57 ± 0.73 / 15.09 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">13.42 ± 0.96 / 34.81 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">7.33 ± 1.70 / 29.31 ± 1.45</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="sv ner">14.67 ± 4.71 / 14.85 ± 3.77</td> <!-- SUC3 -->
   <td class="sv sent">75.45 ± 1.10 / 64.08 ± 1.47</td> <!-- SweReC -->
   <td class="sv la">3.82 ± 1.23 / 44.81 ± 3.55</td> <!-- ScaLA-sv -->
   <td class="sv rc">51.73 ± 0.88 / 57.35 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.72 ± 1.46 / 15.26 ± 0.64</td> <!-- SweDN -->
   <td class="sv know">10.98 ± 0.98 / 31.92 ± 0.80</td> <!-- MMLU-sv -->
   <td class="sv reason">4.24 ± 0.47 / 27.53 ± 0.44</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.56</td> <!-- ScandEval rank -->
   <td class="sv ner">14.58 ± 1.30 / 14.79 ± 1.27</td> <!-- SUC3 -->
   <td class="sv sent">56.60 ± 3.37 / 62.73 ± 3.61</td> <!-- SweReC -->
   <td class="sv la">10.92 ± 1.83 / 52.63 ± 2.98</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.18 ± 0.54 / 57.90 ± 0.53</td> <!-- ScandiQA-sv -->
   <td class="sv summ">64.89 ± 0.15 / 18.79 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">6.16 ± 0.81 / 28.35 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">10.90 ± 0.86 / 32.01 ± 0.54</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="sv ner">33.34 ± 3.41 / 30.50 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.00 ± 1.15 / 69.12 ± 2.00</td> <!-- SweReC -->
   <td class="sv la">0.25 ± 1.72 / 43.46 ± 3.96</td> <!-- ScaLA-sv -->
   <td class="sv rc">52.53 ± 1.03 / 57.96 ± 0.98</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.86 ± 1.75 / 11.38 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">11.71 ± 0.83 / 32.71 ± 0.95</td> <!-- MMLU-sv -->
   <td class="sv reason">0.81 ± 0.88 / 25.27 ± 0.59</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.8</td> <!-- SweDN version -->
   <td>12.10.8</td> <!-- MMLU-sv version -->
   <td>12.10.8</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-33b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">501 ± 50 / 238 ± 69</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="sv ner">33.61 ± 6.02 / 22.18 ± 4.32</td> <!-- SUC3 -->
   <td class="sv sent">76.75 ± 1.17 / 74.66 ± 1.20</td> <!-- SweReC -->
   <td class="sv la">1.66 ± 1.36 / 33.60 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">50.68 ± 1.94 / 56.96 ± 1.73</td> <!-- ScandiQA-sv -->
   <td class="sv summ">56.37 ± 1.71 / 12.78 ± 0.63</td> <!-- SweDN -->
   <td class="sv know">-0.31 ± 0.91 / 25.20 ± 0.62</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.04 ± 0.62 / 25.05 ± 0.50</td> <!-- HellaSwag-sv -->
   <td>12.9.1</td> <!-- SUC3 version -->
   <td>12.9.1</td> <!-- SweReC version -->
   <td>12.10.0</td> <!-- ScaLA-sv version -->
   <td>12.10.0</td> <!-- ScandiQA-sv version -->
   <td>12.10.0</td> <!-- SweDN version -->
   <td>12.10.0</td> <!-- MMLU-sv version -->
   <td>12.10.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="sv ner">19.04 ± 2.67 / 19.98 ± 2.64</td> <!-- SUC3 -->
   <td class="sv sent">73.34 ± 1.34 / 68.41 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.90 ± 1.74 / 44.43 ± 4.49</td> <!-- ScaLA-sv -->
   <td class="sv rc">47.45 ± 0.58 / 54.69 ± 0.56</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.33 ± 0.86 / 17.11 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">0.65 ± 1.12 / 25.94 ± 0.76</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.18 ± 0.36 / 24.70 ± 0.60</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="sv ner">30.64 ± 4.19 / 23.90 ± 3.44</td> <!-- SUC3 -->
   <td class="sv sent">72.02 ± 3.18 / 72.36 ± 3.96</td> <!-- SweReC -->
   <td class="sv la">1.08 ± 1.36 / 38.63 ± 3.03</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.72 ± 1.05 / 54.59 ± 1.10</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.93 ± 2.32 / 13.16 ± 1.05</td> <!-- SweDN -->
   <td class="sv know">1.14 ± 0.79 / 22.39 ± 0.53</td> <!-- MMLU-sv -->
   <td class="sv reason">1.13 ± 1.01 / 25.61 ± 0.65</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-13b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,520 ± 736 / 823 ± 273</td> <!-- Model inference speed -->
   <td class="rank">3.62</td> <!-- ScandEval rank -->
   <td class="sv ner">32.19 ± 4.64 / 24.93 ± 4.09</td> <!-- SUC3 -->
   <td class="sv sent">72.26 ± 6.90 / 72.58 ± 5.87</td> <!-- SweReC -->
   <td class="sv la">2.39 ± 1.29 / 48.49 ± 2.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">48.92 ± 2.28 / 53.44 ± 2.49</td> <!-- ScandiQA-sv -->
   <td class="sv summ">57.46 ± 1.64 / 13.21 ± 0.57</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.50 / 25.03 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.50 ± 1.04 / 25.50 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>12.6.1</td> <!-- SUC3 version -->
   <td>12.6.1</td> <!-- SweReC version -->
   <td>12.6.1</td> <!-- ScaLA-sv version -->
   <td>12.6.1</td> <!-- ScandiQA-sv version -->
   <td>12.6.1</td> <!-- SweDN version -->
   <td>12.6.1</td> <!-- MMLU-sv version -->
   <td>12.6.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4065</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,027 ± 503 / 903 ± 296</td> <!-- Model inference speed -->
   <td class="rank">3.65</td> <!-- ScandEval rank -->
   <td class="sv ner">20.97 ± 2.51 / 16.21 ± 2.03</td> <!-- SUC3 -->
   <td class="sv sent">77.76 ± 0.75 / 67.99 ± 2.31</td> <!-- SweReC -->
   <td class="sv la">2.35 ± 1.63 / 38.48 ± 1.53</td> <!-- ScaLA-sv -->
   <td class="sv rc">28.65 ± 2.11 / 38.84 ± 1.85</td> <!-- ScandiQA-sv -->
   <td class="sv summ">63.75 ± 0.70 / 17.94 ± 0.22</td> <!-- SweDN -->
   <td class="sv know">9.17 ± 0.61 / 31.89 ± 0.41</td> <!-- MMLU-sv -->
   <td class="sv reason">3.98 ± 1.37 / 26.35 ± 1.13</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.4</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="sv ner">51.76 ± 4.53 / 41.73 ± 6.65</td> <!-- SUC3 -->
   <td class="sv sent">70.61 ± 1.12 / 60.47 ± 1.13</td> <!-- SweReC -->
   <td class="sv la">6.24 ± 3.11 / 46.34 ± 5.43</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.67 ± 1.34 / 50.56 ± 1.33</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.31 ± 2.13 / 7.20 ± 1.44</td> <!-- SweDN -->
   <td class="sv know">7.41 ± 0.75 / 30.14 ± 0.39</td> <!-- MMLU-sv -->
   <td class="sv reason">5.42 ± 0.79 / 29.15 ± 0.59</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.70</td> <!-- ScandEval rank -->
   <td class="sv ner">50.10 ± 4.30 / 42.80 ± 5.47</td> <!-- SUC3 -->
   <td class="sv sent">65.67 ± 3.92 / 64.00 ± 3.84</td> <!-- SweReC -->
   <td class="sv la">4.55 ± 2.18 / 45.11 ± 4.32</td> <!-- ScaLA-sv -->
   <td class="sv rc">42.83 ± 1.02 / 49.35 ± 1.09</td> <!-- ScandiQA-sv -->
   <td class="sv summ">45.16 ± 0.70 / 11.84 ± 0.27</td> <!-- SweDN -->
   <td class="sv know">7.58 ± 0.88 / 28.54 ± 0.85</td> <!-- MMLU-sv -->
   <td class="sv reason">3.79 ± 0.85 / 27.39 ± 0.57</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.71</td> <!-- ScandEval rank -->
   <td class="sv ner">20.94 ± 3.73 / 18.26 ± 2.84</td> <!-- SUC3 -->
   <td class="sv sent">52.54 ± 3.33 / 60.44 ± 3.13</td> <!-- SweReC -->
   <td class="sv la">0.34 ± 1.22 / 36.61 ± 1.57</td> <!-- ScaLA-sv -->
   <td class="sv rc">43.55 ± 1.14 / 50.53 ± 1.40</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.19 ± 0.69 / 15.92 ± 0.24</td> <!-- SweDN -->
   <td class="sv know">10.74 ± 0.92 / 32.65 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">4.83 ± 0.62 / 28.76 ± 0.55</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.5.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.72</td> <!-- ScandEval rank -->
   <td class="sv ner">37.26 ± 4.28 / 29.89 ± 5.96</td> <!-- SUC3 -->
   <td class="sv sent">5.20 ± 7.35 / 30.65 ± 4.97</td> <!-- SweReC -->
   <td class="sv la">1.85 ± 1.54 / 33.71 ± 0.46</td> <!-- ScaLA-sv -->
   <td class="sv rc">54.15 ± 0.58 / 60.15 ± 0.59</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.24 ± 1.76 / 16.02 ± 0.88</td> <!-- SweDN -->
   <td class="sv know">22.04 ± 0.60 / 41.36 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">14.76 ± 1.28 / 35.27 ± 1.32</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.72</td> <!-- ScandEval rank -->
   <td class="sv ner">29.89 ± 7.13 / 27.65 ± 6.45</td> <!-- SUC3 -->
   <td class="sv sent">74.33 ± 1.07 / 73.73 ± 1.77</td> <!-- SweReC -->
   <td class="sv la">1.06 ± 1.79 / 43.95 ± 3.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.89 ± 2.72 / 52.70 ± 3.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.06 ± 2.11 / 12.53 ± 0.81</td> <!-- SweDN -->
   <td class="sv know">0.93 ± 1.44 / 26.10 ± 1.04</td> <!-- MMLU-sv -->
   <td class="sv reason">0.09 ± 1.37 / 24.84 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="sv ner">18.83 ± 6.41 / 17.59 ± 4.55</td> <!-- SUC3 -->
   <td class="sv sent">53.68 ± 10.39 / 58.92 ± 10.87</td> <!-- SweReC -->
   <td class="sv la">3.49 ± 2.20 / 46.13 ± 4.13</td> <!-- ScaLA-sv -->
   <td class="sv rc">49.81 ± 0.70 / 55.99 ± 0.69</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.05 ± 1.33 / 15.89 ± 0.85</td> <!-- SweDN -->
   <td class="sv know">1.22 ± 0.65 / 26.19 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">0.60 ± 1.34 / 25.62 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>11.0.0</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>11.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="sv ner">6.08 ± 5.75 / 8.77 ± 4.46</td> <!-- SUC3 -->
   <td class="sv sent">71.38 ± 1.76 / 73.21 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">1.17 ± 1.07 / 49.78 ± 0.86</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.55 ± 0.85 / 51.69 ± 0.79</td> <!-- ScandiQA-sv -->
   <td class="sv summ">60.11 ± 1.59 / 15.02 ± 0.84</td> <!-- SweDN -->
   <td class="sv know">2.20 ± 0.88 / 25.62 ± 0.86</td> <!-- MMLU-sv -->
   <td class="sv reason">0.67 ± 1.39 / 25.25 ± 0.51</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="sv ner">18.01 ± 6.41 / 18.55 ± 4.65</td> <!-- SUC3 -->
   <td class="sv sent">51.91 ± 4.78 / 59.44 ± 4.65</td> <!-- SweReC -->
   <td class="sv la">1.49 ± 1.95 / 40.76 ± 4.07</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.83 ± 0.63 / 51.87 ± 0.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.82 ± 1.62 / 14.43 ± 0.68</td> <!-- SweDN -->
   <td class="sv know">11.54 ± 0.73 / 32.55 ± 0.60</td> <!-- MMLU-sv -->
   <td class="sv reason">7.19 ± 1.40 / 29.76 ± 1.22</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="sv ner">27.07 ± 6.33 / 25.24 ± 4.89</td> <!-- SUC3 -->
   <td class="sv sent">61.96 ± 2.69 / 67.81 ± 2.27</td> <!-- SweReC -->
   <td class="sv la">2.65 ± 1.46 / 40.25 ± 4.08</td> <!-- ScaLA-sv -->
   <td class="sv rc">46.16 ± 0.91 / 52.35 ± 0.87</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.11 ± 1.21 / 12.07 ± 0.32</td> <!-- SweDN -->
   <td class="sv know">0.32 ± 0.43 / 21.99 ± 0.56</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.00 ± 0.01 / 25.00 ± 0.77</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.3.2</td> <!-- SweReC version -->
   <td>12.3.2</td> <!-- ScaLA-sv version -->
   <td>12.3.2</td> <!-- ScandiQA-sv version -->
   <td>12.3.2</td> <!-- SweDN version -->
   <td>12.3.2</td> <!-- MMLU-sv version -->
   <td>12.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.82</td> <!-- ScandEval rank -->
   <td class="sv ner">23.25 ± 1.99 / 20.55 ± 2.20</td> <!-- SUC3 -->
   <td class="sv sent">71.70 ± 1.09 / 71.01 ± 2.36</td> <!-- SweReC -->
   <td class="sv la">-0.82 ± 2.23 / 40.80 ± 4.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">40.48 ± 1.52 / 46.93 ± 1.61</td> <!-- ScandiQA-sv -->
   <td class="sv summ">54.39 ± 1.68 / 13.19 ± 0.61</td> <!-- SweDN -->
   <td class="sv know">-0.43 ± 1.13 / 24.95 ± 0.64</td> <!-- MMLU-sv -->
   <td class="sv reason">1.98 ± 0.99 / 26.14 ± 0.86</td> <!-- HellaSwag-sv -->
   <td>13.0.0</td> <!-- SUC3 version -->
   <td>13.0.0</td> <!-- SweReC version -->
   <td>13.0.0</td> <!-- ScaLA-sv version -->
   <td>13.0.0</td> <!-- ScandiQA-sv version -->
   <td>13.0.0</td> <!-- SweDN version -->
   <td>13.0.0</td> <!-- MMLU-sv version -->
   <td>13.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="sv ner">14.84 ± 1.63 / 15.90 ± 1.71</td> <!-- SUC3 -->
   <td class="sv sent">59.00 ± 3.60 / 54.09 ± 1.46</td> <!-- SweReC -->
   <td class="sv la">0.06 ± 1.21 / 34.76 ± 1.15</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.37 ± 1.36 / 40.44 ± 1.53</td> <!-- ScandiQA-sv -->
   <td class="sv summ">61.28 ± 0.92 / 14.60 ± 0.79</td> <!-- SweDN -->
   <td class="sv know">0.48 ± 1.07 / 23.44 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">0.33 ± 0.50 / 25.01 ± 0.76</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.94</td> <!-- ScandEval rank -->
   <td class="sv ner">37.36 ± 2.11 / 28.59 ± 3.03</td> <!-- SUC3 -->
   <td class="sv sent">72.08 ± 1.20 / 63.52 ± 3.36</td> <!-- SweReC -->
   <td class="sv la">-0.86 ± 1.61 / 33.84 ± 0.59</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.16 ± 0.96 / 51.46 ± 0.93</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.03 ± 0.33 / 4.86 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.83 ± 1.04 / 25.47 ± 0.54</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.62 ± 0.73 / 24.51 ± 0.53</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="sv ner">13.79 ± 8.46 / 14.43 ± 7.23</td> <!-- SUC3 -->
   <td class="sv sent">71.59 ± 2.78 / 59.82 ± 1.71</td> <!-- SweReC -->
   <td class="sv la">-0.89 ± 1.22 / 43.82 ± 3.45</td> <!-- ScaLA-sv -->
   <td class="sv rc">38.33 ± 1.79 / 44.00 ± 1.70</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.77 ± 0.83 / 14.15 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">-0.39 ± 1.21 / 22.30 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.52 ± 1.01 / 25.20 ± 0.85</td> <!-- HellaSwag-sv -->
   <td>10.0.0</td> <!-- SUC3 version -->
   <td>10.0.0</td> <!-- SweReC version -->
   <td>10.0.0</td> <!-- ScaLA-sv version -->
   <td>10.0.0</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="sv ner">27.31 ± 4.23 / 26.33 ± 4.40</td> <!-- SUC3 -->
   <td class="sv sent">45.94 ± 12.82 / 55.94 ± 8.25</td> <!-- SweReC -->
   <td class="sv la">-0.97 ± 1.64 / 36.69 ± 2.34</td> <!-- ScaLA-sv -->
   <td class="sv rc">35.57 ± 2.45 / 41.66 ± 2.41</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.79 ± 0.24 / 10.61 ± 0.29</td> <!-- SweDN -->
   <td class="sv know">0.14 ± 1.02 / 24.76 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.83 / 25.53 ± 0.62</td> <!-- HellaSwag-sv -->
   <td>9.1.2</td> <!-- SUC3 version -->
   <td>9.1.2</td> <!-- SweReC version -->
   <td>9.1.2</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>9.1.2</td> <!-- MMLU-sv version -->
   <td>9.1.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.05</td> <!-- ScandEval rank -->
   <td class="sv ner">20.49 ± 7.78 / 19.50 ± 6.82</td> <!-- SUC3 -->
   <td class="sv sent">70.04 ± 2.28 / 60.77 ± 3.00</td> <!-- SweReC -->
   <td class="sv la">2.28 ± 1.77 / 36.86 ± 3.97</td> <!-- ScaLA-sv -->
   <td class="sv rc">45.85 ± 1.19 / 51.08 ± 1.21</td> <!-- ScandiQA-sv -->
   <td class="sv summ">39.53 ± 0.34 / 5.71 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">0.69 ± 0.90 / 24.20 ± 0.89</td> <!-- MMLU-sv -->
   <td class="sv reason">0.12 ± 1.51 / 24.97 ± 1.28</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.09</td> <!-- ScandEval rank -->
   <td class="sv ner">22.38 ± 3.00 / 22.09 ± 2.85</td> <!-- SUC3 -->
   <td class="sv sent">31.11 ± 12.17 / 36.84 ± 11.52</td> <!-- SweReC -->
   <td class="sv la">0.09 ± 0.67 / 33.42 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">44.36 ± 1.34 / 50.14 ± 1.15</td> <!-- ScandiQA-sv -->
   <td class="sv summ">55.44 ± 0.79 / 12.95 ± 0.51</td> <!-- SweDN -->
   <td class="sv know">1.12 ± 0.42 / 25.27 ± 0.68</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.91 ± 0.96 / 24.26 ± 0.64</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">4.11</td> <!-- ScandEval rank -->
   <td class="sv ner">33.51 ± 2.12 / 23.48 ± 2.69</td> <!-- SUC3 -->
   <td class="sv sent">43.97 ± 1.64 / 57.41 ± 1.18</td> <!-- SweReC -->
   <td class="sv la">0.53 ± 1.09 / 39.60 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">39.39 ± 1.04 / 47.28 ± 1.02</td> <!-- ScandiQA-sv -->
   <td class="sv summ">40.55 ± 6.41 / 11.10 ± 1.63</td> <!-- SweDN -->
   <td class="sv know">11.06 ± 0.98 / 31.69 ± 0.81</td> <!-- MMLU-sv -->
   <td class="sv reason">1.03 ± 0.85 / 25.55 ± 0.60</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="sv ner">28.96 ± 2.39 / 26.49 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">26.58 ± 5.12 / 28.64 ± 5.35</td> <!-- SweReC -->
   <td class="sv la">-1.88 ± 1.46 / 35.45 ± 2.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">34.59 ± 1.06 / 40.95 ± 1.11</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.36 ± 1.44 / 12.82 ± 0.58</td> <!-- SweDN -->
   <td class="sv know">6.52 ± 1.02 / 28.83 ± 0.78</td> <!-- MMLU-sv -->
   <td class="sv reason">1.91 ± 1.30 / 26.10 ± 0.65</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="sv ner">13.28 ± 4.32 / 13.40 ± 2.95</td> <!-- SUC3 -->
   <td class="sv sent">60.17 ± 8.39 / 65.99 ± 4.66</td> <!-- SweReC -->
   <td class="sv la">1.52 ± 1.94 / 45.19 ± 3.80</td> <!-- ScaLA-sv -->
   <td class="sv rc">37.23 ± 1.07 / 46.83 ± 0.82</td> <!-- ScandiQA-sv -->
   <td class="sv summ">46.68 ± 0.33 / 12.40 ± 0.17</td> <!-- SweDN -->
   <td class="sv know">-0.03 ± 1.31 / 23.73 ± 1.11</td> <!-- MMLU-sv -->
   <td class="sv reason">0.02 ± 0.88 / 25.04 ± 0.61</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="sv ner">18.57 ± 4.62 / 17.69 ± 4.61</td> <!-- SUC3 -->
   <td class="sv sent">40.23 ± 5.86 / 49.01 ± 4.77</td> <!-- SweReC -->
   <td class="sv la">0.21 ± 1.06 / 39.60 ± 3.61</td> <!-- ScaLA-sv -->
   <td class="sv rc">29.49 ± 2.47 / 35.01 ± 2.72</td> <!-- ScandiQA-sv -->
   <td class="sv summ">53.29 ± 6.52 / 13.04 ± 1.68</td> <!-- SweDN -->
   <td class="sv know">2.59 ± 0.72 / 26.87 ± 0.72</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.84 ± 1.01 / 24.44 ± 0.61</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>11.0.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.5.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="sv ner">23.77 ± 3.70 / 23.06 ± 3.46</td> <!-- SUC3 -->
   <td class="sv sent">34.29 ± 11.64 / 36.76 ± 7.46</td> <!-- SweReC -->
   <td class="sv la">1.57 ± 1.70 / 40.84 ± 1.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">33.70 ± 1.46 / 38.82 ± 1.54</td> <!-- ScandiQA-sv -->
   <td class="sv summ">51.36 ± 2.01 / 10.76 ± 0.54</td> <!-- SweDN -->
   <td class="sv know">-0.96 ± 1.08 / 21.85 ± 0.45</td> <!-- MMLU-sv -->
   <td class="sv reason">0.30 ± 0.48 / 25.10 ± 0.69</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.2</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.2</td> <!-- MMLU-sv version -->
   <td>9.3.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">4.25</td> <!-- ScandEval rank -->
   <td class="sv ner">23.92 ± 6.88 / 22.42 ± 6.73</td> <!-- SUC3 -->
   <td class="sv sent">31.93 ± 14.68 / 43.80 ± 8.79</td> <!-- SweReC -->
   <td class="sv la">0.46 ± 1.91 / 43.45 ± 3.64</td> <!-- ScaLA-sv -->
   <td class="sv rc">30.81 ± 2.73 / 35.67 ± 2.95</td> <!-- ScandiQA-sv -->
   <td class="sv summ">52.68 ± 0.76 / 11.19 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">-0.85 ± 1.05 / 24.38 ± 0.51</td> <!-- MMLU-sv -->
   <td class="sv reason">-1.24 ± 0.90 / 24.30 ± 0.63</td> <!-- HellaSwag-sv -->
   <td>0.0.0</td> <!-- SUC3 version -->
   <td>0.0.0</td> <!-- SweReC version -->
   <td>0.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>0.0.0</td> <!-- MMLU-sv version -->
   <td>0.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.35</td> <!-- ScandEval rank -->
   <td class="sv ner">23.05 ± 2.31 / 24.35 ± 1.99</td> <!-- SUC3 -->
   <td class="sv sent">12.47 ± 7.10 / 23.03 ± 8.78</td> <!-- SweReC -->
   <td class="sv la">0.08 ± 0.16 / 33.34 ± 0.30</td> <!-- ScaLA-sv -->
   <td class="sv rc">20.43 ± 2.69 / 24.25 ± 2.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.80 ± 0.93 / 14.56 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">0.72 ± 0.72 / 23.30 ± 0.96</td> <!-- MMLU-sv -->
   <td class="sv reason">0.11 ± 0.91 / 25.15 ± 0.81</td> <!-- HellaSwag-sv -->
   <td>9.3.2</td> <!-- SUC3 version -->
   <td>9.3.2</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.4.0</td> <!-- ScandiQA-sv version -->
   <td>12.4.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.42</td> <!-- ScandEval rank -->
   <td class="sv ner">29.39 ± 3.08 / 29.93 ± 3.14</td> <!-- SUC3 -->
   <td class="sv sent">38.95 ± 11.78 / 43.61 ± 8.46</td> <!-- SweReC -->
   <td class="sv la">-1.35 ± 1.76 / 40.70 ± 4.25</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.85 ± 3.77 / 20.30 ± 4.04</td> <!-- ScandiQA-sv -->
   <td class="sv summ">43.75 ± 0.28 / 4.67 ± 0.12</td> <!-- SweDN -->
   <td class="sv know">-0.22 ± 0.80 / 23.76 ± 0.84</td> <!-- MMLU-sv -->
   <td class="sv reason">0.75 ± 1.00 / 25.27 ± 0.56</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.1.0</td> <!-- SweReC version -->
   <td>12.1.0</td> <!-- ScaLA-sv version -->
   <td>12.1.0</td> <!-- ScandiQA-sv version -->
   <td>12.1.0</td> <!-- SweDN version -->
   <td>12.1.0</td> <!-- MMLU-sv version -->
   <td>12.1.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">34.63 ± 9.69 / 40.92 ± 6.88</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 8.92 ± 2.90</td> <!-- ScandiQA-sv -->
   <td class="sv summ">59.04 ± 0.07 / 10.84 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.25 ± 0.97 / 21.96 ± 0.57</td> <!-- MMLU-sv -->
   <td class="sv reason">0.08 ± 0.78 / 24.93 ± 0.77</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>9.3.1</td> <!-- SweReC version -->
   <td>9.3.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.3.1</td> <!-- MMLU-sv version -->
   <td>9.3.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.71</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">28.62 ± 12.67 / 35.36 ± 8.35</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 19.59 ± 6.84</td> <!-- ScandiQA-sv -->
   <td class="sv summ">58.16 ± 0.07 / 8.81 ± 0.07</td> <!-- SweDN -->
   <td class="sv know">0.47 ± 0.86 / 22.03 ± 0.59</td> <!-- MMLU-sv -->
   <td class="sv reason">0.71 ± 0.64 / 25.02 ± 0.72</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4065</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.72</td> <!-- ScandEval rank -->
   <td class="sv ner">9.75 ± 3.30 / 9.18 ± 3.19</td> <!-- SUC3 -->
   <td class="sv sent">17.76 ± 4.89 / 28.16 ± 7.50</td> <!-- SweReC -->
   <td class="sv la">1.22 ± 0.95 / 43.54 ± 3.79</td> <!-- ScaLA-sv -->
   <td class="sv rc">14.98 ± 2.49 / 18.46 ± 2.99</td> <!-- ScandiQA-sv -->
   <td class="sv summ">48.74 ± 1.72 / 10.30 ± 0.36</td> <!-- SweDN -->
   <td class="sv know">-0.62 ± 1.15 / 22.04 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">0.99 ± 1.35 / 25.36 ± 0.92</td> <!-- HellaSwag-sv -->
   <td>12.10.5</td> <!-- SUC3 version -->
   <td>12.10.5</td> <!-- SweReC version -->
   <td>12.10.5</td> <!-- ScaLA-sv version -->
   <td>12.10.5</td> <!-- ScandiQA-sv version -->
   <td>12.10.5</td> <!-- SweDN version -->
   <td>12.10.5</td> <!-- MMLU-sv version -->
   <td>12.10.5</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.76</td> <!-- ScandEval rank -->
   <td class="sv ner">5.66 ± 4.11 / 8.37 ± 3.24</td> <!-- SUC3 -->
   <td class="sv sent">8.15 ± 8.87 / 24.31 ± 7.12</td> <!-- SweReC -->
   <td class="sv la">-0.81 ± 1.16 / 36.81 ± 2.47</td> <!-- ScaLA-sv -->
   <td class="sv rc">16.40 ± 2.88 / 19.18 ± 3.18</td> <!-- ScandiQA-sv -->
   <td class="sv summ">51.48 ± 1.14 / 10.63 ± 0.31</td> <!-- SweDN -->
   <td class="sv know">-0.49 ± 0.60 / 22.53 ± 0.75</td> <!-- MMLU-sv -->
   <td class="sv reason">1.17 ± 0.86 / 25.54 ± 0.87</td> <!-- HellaSwag-sv -->
   <td>9.2.0</td> <!-- SUC3 version -->
   <td>9.2.0</td> <!-- SweReC version -->
   <td>9.2.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>9.2.0</td> <!-- MMLU-sv version -->
   <td>9.2.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">5.06</td> <!-- ScandEval rank -->
   <td class="sv ner">0.31 ± 0.55 / 0.29 ± 0.50</td> <!-- SUC3 -->
   <td class="sv sent">27.42 ± 12.16 / 38.74 ± 10.05</td> <!-- SweReC -->
   <td class="sv la">0.07 ± 1.06 / 35.80 ± 1.73</td> <!-- ScaLA-sv -->
   <td class="sv rc">17.82 ± 11.21 / 31.12 ± 8.39</td> <!-- ScandiQA-sv -->
   <td class="sv summ">27.09 ± 0.29 / 6.80 ± 0.12</td> <!-- SweDN -->
   <td class="sv know">-0.67 ± 0.81 / 22.55 ± 0.71</td> <!-- MMLU-sv -->
   <td class="sv reason">0.86 ± 0.82 / 25.38 ± 0.51</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">5.10</td> <!-- ScandEval rank -->
   <td class="sv ner">0.26 ± 0.16 / 0.26 ± 0.14</td> <!-- SUC3 -->
   <td class="sv sent">4.75 ± 2.54 / 27.85 ± 1.59</td> <!-- SweReC -->
   <td class="sv la">-0.60 ± 1.56 / 40.53 ± 2.93</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.06 ± 0.09 / 1.07 ± 0.35</td> <!-- ScandiQA-sv -->
   <td class="sv summ">41.84 ± 0.24 / 5.74 ± 0.09</td> <!-- SweDN -->
   <td class="sv know">-0.41 ± 1.39 / 24.48 ± 0.97</td> <!-- MMLU-sv -->
   <td class="sv reason">0.52 ± 0.81 / 25.32 ± 0.65</td> <!-- HellaSwag-sv -->
   <td>10.0.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>10.0.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">5.15</td> <!-- ScandEval rank -->
   <td class="sv ner">0.01 ± 0.02 / 0.11 ± 0.12</td> <!-- SUC3 -->
   <td class="sv sent">33.50 ± 13.13 / 39.30 ± 11.93</td> <!-- SweReC -->
   <td class="sv la">-0.02 ± 0.60 / 34.92 ± 2.99</td> <!-- ScaLA-sv -->
   <td class="sv rc">4.79 ± 3.55 / 18.06 ± 2.80</td> <!-- ScandiQA-sv -->
   <td class="sv summ">26.97 ± 0.41 / 6.56 ± 0.18</td> <!-- SweDN -->
   <td class="sv know">-0.11 ± 1.16 / 23.32 ± 0.92</td> <!-- MMLU-sv -->
   <td class="sv reason">0.56 ± 1.22 / 24.79 ± 0.91</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>10.0.1</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>11.0.0</td> <!-- SweDN version -->
   <td>10.0.1</td> <!-- MMLU-sv version -->
   <td>10.0.1</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">5.20</td> <!-- ScandEval rank -->
   <td class="sv ner">1.47 ± 1.90 / 1.32 ± 1.69</td> <!-- SUC3 -->
   <td class="sv sent">5.50 ± 4.49 / 28.77 ± 3.76</td> <!-- SweReC -->
   <td class="sv la">-2.19 ± 1.29 / 40.52 ± 3.02</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.10 ± 0.06 / 4.36 ± 0.44</td> <!-- ScandiQA-sv -->
   <td class="sv summ">37.40 ± 0.61 / 6.53 ± 0.13</td> <!-- SweDN -->
   <td class="sv know">-0.53 ± 1.01 / 24.38 ± 1.08</td> <!-- MMLU-sv -->
   <td class="sv reason">0.25 ± 1.22 / 25.23 ± 0.73</td> <!-- HellaSwag-sv -->
   <td>12.5.2</td> <!-- SUC3 version -->
   <td>12.5.2</td> <!-- SweReC version -->
   <td>12.5.2</td> <!-- ScaLA-sv version -->
   <td>12.5.2</td> <!-- ScandiQA-sv version -->
   <td>12.5.2</td> <!-- SweDN version -->
   <td>12.5.2</td> <!-- MMLU-sv version -->
   <td>12.5.2</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.26</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">0.00 ± 0.00 / 19.32 ± 0.16</td> <!-- SweReC -->
   <td class="sv la">0.49 ± 1.29 / 39.12 ± 3.92</td> <!-- ScaLA-sv -->
   <td class="sv rc">6.24 ± 3.13 / 7.85 ± 3.67</td> <!-- ScandiQA-sv -->
   <td class="sv summ">31.89 ± 0.27 / 2.03 ± 0.10</td> <!-- SweDN -->
   <td class="sv know">-0.37 ± 1.08 / 22.43 ± 0.55</td> <!-- MMLU-sv -->
   <td class="sv reason">0.36 ± 0.83 / 25.08 ± 0.77</td> <!-- HellaSwag-sv -->
   <td>9.3.1</td> <!-- SUC3 version -->
   <td>10.0.1</td> <!-- SweReC version -->
   <td>11.0.0</td> <!-- ScaLA-sv version -->
   <td>12.5.1</td> <!-- ScandiQA-sv version -->
   <td>12.0.0</td> <!-- SweDN version -->
   <td>11.0.0</td> <!-- MMLU-sv version -->
   <td>11.0.0</td> <!-- HellaSwag-sv version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">5.29</td> <!-- ScandEval rank -->
   <td class="sv ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- SUC3 -->
   <td class="sv sent">-3.60 ± 3.63 / 20.29 ± 1.99</td> <!-- SweReC -->
   <td class="sv la">0.00 ± 0.00 / 33.30 ± 0.27</td> <!-- ScaLA-sv -->
   <td class="sv rc">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- ScandiQA-sv -->
   <td class="sv summ">39.68 ± 0.08 / 1.23 ± 0.02</td> <!-- SweDN -->
   <td class="sv know">-0.20 ± 0.77 / 24.13 ± 0.67</td> <!-- MMLU-sv -->
   <td class="sv reason">-0.25 ± 0.67 / 24.68 ± 0.44</td> <!-- HellaSwag-sv -->
   <td>12.7.0</td> <!-- SUC3 version -->
   <td>12.7.0</td> <!-- SweReC version -->
   <td>12.7.0</td> <!-- ScaLA-sv version -->
   <td>12.7.0</td> <!-- ScandiQA-sv version -->
   <td>12.7.0</td> <!-- SweDN version -->
   <td>12.7.0</td> <!-- MMLU-sv version -->
   <td>12.7.0</td> <!-- HellaSwag-sv version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/swedish-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Swedish NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-HMMEK&quot; src=&quot;https://datawrapper.dwcdn.net/HMMEK/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
