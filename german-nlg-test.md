---
layout: leaderboard
title: German NLG 🇩🇪
---

<center>Last updated: 31/10/2024 16:23:29 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="german-nlg-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German reading comprehension - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German summarization - BERTScore / ROUGE-L">MLSum</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermEval">GermEval version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SB10k">SB10k version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-de">ScaLA-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermanQuAD">GermanQuAD version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MLSum">MLSum version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-de">MMLU-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-de">HellaSwag-de version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8220</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.22</td> <!-- ScandEval rank -->
   <td class="de ner">69.48 ± 2.32 / 54.66 ± 2.17</td> <!-- GermEval -->
   <td class="de sent">64.91 ± 1.86 / 75.96 ± 1.59</td> <!-- SB10k -->
   <td class="de la">50.23 ± 4.16 / 74.54 ± 2.10</td> <!-- ScaLA-de -->
   <td class="de rc">33.17 ± 1.86 / 65.14 ± 1.53</td> <!-- GermanQuAD -->
   <td class="de summ">66.35 ± 0.59 / 19.81 ± 1.46</td> <!-- MLSum -->
   <td class="de know">71.92 ± 2.22 / 78.79 ± 1.65</td> <!-- MMLU-de -->
   <td class="de reason">82.85 ± 1.48 / 86.99 ± 1.12</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="de ner">68.94 ± 2.50 / 44.89 ± 2.85</td> <!-- GermEval -->
   <td class="de sent">60.47 ± 2.94 / 72.79 ± 1.90</td> <!-- SB10k -->
   <td class="de la">51.26 ± 4.94 / 74.76 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">30.04 ± 1.30 / 58.77 ± 1.50</td> <!-- GermanQuAD -->
   <td class="de summ">63.62 ± 0.65 / 13.08 ± 0.87</td> <!-- MLSum -->
   <td class="de know">73.80 ± 2.03 / 80.31 ± 1.54</td> <!-- MMLU-de -->
   <td class="de reason">83.93 ± 2.38 / 87.85 ± 1.80</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.10.2</td> <!-- MMLU-de version -->
   <td>12.10.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="de ner">69.04 ± 2.51 / 61.10 ± 3.39</td> <!-- GermEval -->
   <td class="de sent">63.51 ± 2.57 / 75.01 ± 1.74</td> <!-- SB10k -->
   <td class="de la">37.41 ± 2.43 / 67.63 ± 1.05</td> <!-- ScaLA-de -->
   <td class="de rc">38.29 ± 3.54 / 69.69 ± 2.78</td> <!-- GermanQuAD -->
   <td class="de summ">70.00 ± 1.41 / 29.78 ± 3.58</td> <!-- MLSum -->
   <td class="de know">64.93 ± 2.76 / 73.71 ± 2.07</td> <!-- MMLU-de -->
   <td class="de reason">66.54 ± 4.29 / 74.45 ± 3.24</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127903</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.44</td> <!-- ScandEval rank -->
   <td class="de ner">69.99 ± 1.63 / 45.58 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">54.82 ± 2.19 / 68.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">43.66 ± 5.67 / 64.64 ± 4.65</td> <!-- ScaLA-de -->
   <td class="de rc">30.06 ± 1.04 / 60.77 ± 1.11</td> <!-- GermanQuAD -->
   <td class="de summ">63.80 ± 0.60 / 13.87 ± 1.05</td> <!-- MLSum -->
   <td class="de know">74.13 ± 1.60 / 80.59 ± 1.22</td> <!-- MMLU-de -->
   <td class="de reason">88.18 ± 1.79 / 91.13 ± 1.34</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.2</td> <!-- MMLU-de version -->
   <td>12.10.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="de ner">64.13 ± 1.65 / 55.46 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">60.28 ± 1.75 / 73.37 ± 1.43</td> <!-- SB10k -->
   <td class="de la">46.69 ± 1.99 / 71.96 ± 0.73</td> <!-- ScaLA-de -->
   <td class="de rc">28.54 ± 1.38 / 59.38 ± 1.85</td> <!-- GermanQuAD -->
   <td class="de summ">67.87 ± 0.99 / 24.26 ± 2.65</td> <!-- MLSum -->
   <td class="de know">59.43 ± 0.82 / 69.41 ± 0.61</td> <!-- MMLU-de -->
   <td class="de reason">71.59 ± 1.49 / 78.30 ± 1.23</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="de ner">75.20 ± 2.15 / 64.06 ± 3.60</td> <!-- GermEval -->
   <td class="de sent">54.38 ± 3.31 / 68.02 ± 2.21</td> <!-- SB10k -->
   <td class="de la">36.59 ± 4.24 / 67.36 ± 1.77</td> <!-- ScaLA-de -->
   <td class="de rc">26.90 ± 2.67 / 58.28 ± 2.22</td> <!-- GermanQuAD -->
   <td class="de summ">68.63 ± 1.20 / 26.12 ± 3.00</td> <!-- MLSum -->
   <td class="de know">62.69 ± 1.83 / 71.95 ± 1.40</td> <!-- MMLU-de -->
   <td class="de reason">69.18 ± 2.73 / 76.41 ± 2.08</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">1.60</td> <!-- ScandEval rank -->
   <td class="de ner">68.11 ± 1.32 / 56.25 ± 1.65</td> <!-- GermEval -->
   <td class="de sent">59.79 ± 1.60 / 71.47 ± 1.54</td> <!-- SB10k -->
   <td class="de la">35.45 ± 3.06 / 66.13 ± 1.28</td> <!-- ScaLA-de -->
   <td class="de rc">37.27 ± 1.23 / 68.54 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.95 / 28.82 ± 2.24</td> <!-- MLSum -->
   <td class="de know">41.20 ± 0.85 / 55.90 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">72.65 ± 0.69 / 79.18 ± 0.58</td> <!-- HellaSwag-de -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- MLSum version -->
   <td>12.5.3</td> <!-- MMLU-de version -->
   <td>12.5.3</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32793</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="de ner">65.19 ± 2.58 / 56.17 ± 3.57</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 2.15 / 71.98 ± 1.46</td> <!-- SB10k -->
   <td class="de la">41.86 ± 5.44 / 69.70 ± 2.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.51 ± 3.79 / 63.19 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.76 / 20.65 ± 1.59</td> <!-- MLSum -->
   <td class="de know">55.18 ± 3.35 / 66.48 ± 2.49</td> <!-- MMLU-de -->
   <td class="de reason">61.68 ± 3.07 / 70.78 ± 2.37</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">1.69</td> <!-- ScandEval rank -->
   <td class="de ner">47.39 ± 1.96 / 34.14 ± 1.70</td> <!-- GermEval -->
   <td class="de sent">62.89 ± 2.21 / 74.51 ± 1.63</td> <!-- SB10k -->
   <td class="de la">37.22 ± 4.67 / 67.37 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de rc">39.11 ± 2.14 / 67.67 ± 2.90</td> <!-- GermanQuAD -->
   <td class="de summ">70.44 ± 1.18 / 30.83 ± 2.69</td> <!-- MLSum -->
   <td class="de know">53.28 ± 1.15 / 64.86 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">54.51 ± 2.74 / 64.51 ± 2.33</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.71</td> <!-- ScandEval rank -->
   <td class="de ner">50.35 ± 2.81 / 39.72 ± 2.62</td> <!-- GermEval -->
   <td class="de sent">58.60 ± 2.21 / 71.12 ± 1.12</td> <!-- SB10k -->
   <td class="de la">45.78 ± 1.55 / 70.64 ± 0.61</td> <!-- ScaLA-de -->
   <td class="de rc">30.46 ± 0.98 / 60.56 ± 2.25</td> <!-- GermanQuAD -->
   <td class="de summ">67.99 ± 1.12 / 24.07 ± 2.91</td> <!-- MLSum -->
   <td class="de know">53.61 ± 0.60 / 64.92 ± 0.47</td> <!-- MMLU-de -->
   <td class="de reason">68.16 ± 0.75 / 75.71 ± 0.65</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="de ner">66.00 ± 1.13 / 54.14 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.76 ± 3.11 / 68.36 ± 2.92</td> <!-- SB10k -->
   <td class="de la">33.55 ± 4.69 / 63.49 ± 2.99</td> <!-- ScaLA-de -->
   <td class="de rc">32.69 ± 1.98 / 64.23 ± 2.89</td> <!-- GermanQuAD -->
   <td class="de summ">69.65 ± 1.12 / 27.94 ± 2.90</td> <!-- MLSum -->
   <td class="de know">43.46 ± 0.81 / 57.37 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">68.11 ± 1.40 / 75.60 ± 1.16</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="de ner">63.71 ± 2.43 / 57.08 ± 2.70</td> <!-- GermEval -->
   <td class="de sent">58.17 ± 2.51 / 71.34 ± 1.62</td> <!-- SB10k -->
   <td class="de la">36.33 ± 5.00 / 64.51 ± 3.38</td> <!-- ScaLA-de -->
   <td class="de rc">36.06 ± 2.89 / 69.62 ± 2.81</td> <!-- GermanQuAD -->
   <td class="de summ">69.82 ± 1.03 / 30.79 ± 2.46</td> <!-- MLSum -->
   <td class="de know">46.44 ± 2.49 / 59.88 ± 1.74</td> <!-- MMLU-de -->
   <td class="de reason">48.89 ± 2.85 / 61.33 ± 2.06</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024032</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="de ner">66.27 ± 1.13 / 49.86 ± 1.62</td> <!-- GermEval -->
   <td class="de sent">57.70 ± 2.68 / 71.63 ± 1.94</td> <!-- SB10k -->
   <td class="de la">35.54 ± 4.25 / 60.12 ± 5.53</td> <!-- ScaLA-de -->
   <td class="de rc">34.45 ± 1.61 / 66.90 ± 2.58</td> <!-- GermanQuAD -->
   <td class="de summ">68.65 ± 1.15 / 25.16 ± 2.66</td> <!-- MLSum -->
   <td class="de know">47.05 ± 1.12 / 60.01 ± 0.86</td> <!-- MMLU-de -->
   <td class="de reason">52.68 ± 3.39 / 63.07 ± 2.88</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128030</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">1.81</td> <!-- ScandEval rank -->
   <td class="de ner">67.90 ± 1.07 / 45.53 ± 3.11</td> <!-- GermEval -->
   <td class="de sent">51.88 ± 5.19 / 67.24 ± 3.71</td> <!-- SB10k -->
   <td class="de la">46.77 ± 2.33 / 69.48 ± 2.55</td> <!-- ScaLA-de -->
   <td class="de rc">24.70 ± 1.31 / 56.87 ± 0.77</td> <!-- GermanQuAD -->
   <td class="de summ">64.65 ± 0.10 / 14.11 ± 0.26</td> <!-- MLSum -->
   <td class="de know">51.72 ± 2.53 / 62.88 ± 2.10</td> <!-- MMLU-de -->
   <td class="de reason">62.80 ± 1.97 / 70.65 ± 1.80</td> <!-- HellaSwag-de -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- MLSum version -->
   <td>12.11.0</td> <!-- MMLU-de version -->
   <td>12.11.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">1.88</td> <!-- ScandEval rank -->
   <td class="de ner">57.82 ± 1.85 / 43.22 ± 2.36</td> <!-- GermEval -->
   <td class="de sent">59.45 ± 1.95 / 72.95 ± 1.33</td> <!-- SB10k -->
   <td class="de la">36.75 ± 2.58 / 67.88 ± 1.50</td> <!-- ScaLA-de -->
   <td class="de rc">33.55 ± 2.29 / 63.95 ± 2.83</td> <!-- GermanQuAD -->
   <td class="de summ">69.37 ± 0.84 / 28.13 ± 2.16</td> <!-- MLSum -->
   <td class="de know">50.96 ± 0.60 / 63.17 ± 0.44</td> <!-- MMLU-de -->
   <td class="de reason">39.28 ± 2.50 / 52.23 ± 2.22</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="de ner">65.01 ± 0.68 / 43.34 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">51.80 ± 1.29 / 67.45 ± 0.87</td> <!-- SB10k -->
   <td class="de la">36.18 ± 1.31 / 67.86 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de rc">32.12 ± 2.08 / 67.30 ± 1.66</td> <!-- GermanQuAD -->
   <td class="de summ">66.92 ± 0.41 / 23.23 ± 1.24</td> <!-- MLSum -->
   <td class="de know">37.90 ± 1.03 / 53.36 ± 0.80</td> <!-- MMLU-de -->
   <td class="de reason">60.66 ± 1.28 / 70.32 ± 1.01</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-LaserChat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,387 ± 456 / 717 ± 226</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="de ner">64.73 ± 1.02 / 48.09 ± 2.90</td> <!-- GermEval -->
   <td class="de sent">51.08 ± 1.67 / 67.20 ± 1.34</td> <!-- SB10k -->
   <td class="de la">36.46 ± 1.89 / 67.99 ± 0.80</td> <!-- ScaLA-de -->
   <td class="de rc">33.30 ± 1.87 / 67.32 ± 1.73</td> <!-- GermanQuAD -->
   <td class="de summ">66.30 ± 0.24 / 21.71 ± 0.72</td> <!-- MLSum -->
   <td class="de know">38.13 ± 1.08 / 53.46 ± 0.82</td> <!-- MMLU-de -->
   <td class="de reason">58.71 ± 1.26 / 68.77 ± 1.01</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="de ner">58.69 ± 1.32 / 45.79 ± 2.60</td> <!-- GermEval -->
   <td class="de sent">56.49 ± 2.69 / 70.39 ± 2.14</td> <!-- SB10k -->
   <td class="de la">30.04 ± 2.28 / 62.58 ± 2.34</td> <!-- ScaLA-de -->
   <td class="de rc">36.36 ± 1.07 / 66.01 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">69.07 ± 1.43 / 28.50 ± 3.72</td> <!-- MLSum -->
   <td class="de know">32.49 ± 1.21 / 48.62 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">55.40 ± 1.43 / 65.83 ± 1.23</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="de ner">61.29 ± 1.06 / 39.58 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">59.19 ± 1.49 / 71.64 ± 1.07</td> <!-- SB10k -->
   <td class="de la">33.31 ± 3.00 / 64.35 ± 2.80</td> <!-- ScaLA-de -->
   <td class="de rc">22.29 ± 2.02 / 57.68 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">69.05 ± 1.11 / 26.68 ± 3.04</td> <!-- MLSum -->
   <td class="de know">44.87 ± 0.70 / 58.71 ± 0.53</td> <!-- MMLU-de -->
   <td class="de reason">63.66 ± 0.91 / 72.68 ± 0.68</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de rc">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">64.90 ± 0.22 / 15.99 ± 0.32</td> <!-- MLSum -->
   <td class="de know">35.39 ± 3.89 / 51.41 ± 2.98</td> <!-- MMLU-de -->
   <td class="de reason">56.88 ± 2.50 / 66.76 ± 2.02</td> <!-- HellaSwag-de -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   <td>0.0.0</td> <!-- MLSum version -->
   <td>0.0.0</td> <!-- MMLU-de version -->
   <td>0.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="de ner">52.61 ± 1.79 / 42.68 ± 2.71</td> <!-- GermEval -->
   <td class="de sent">61.70 ± 1.45 / 74.22 ± 1.00</td> <!-- SB10k -->
   <td class="de la">23.89 ± 4.13 / 57.16 ± 4.48</td> <!-- ScaLA-de -->
   <td class="de rc">33.72 ± 1.25 / 62.41 ± 1.53</td> <!-- GermanQuAD -->
   <td class="de summ">70.32 ± 0.87 / 31.24 ± 2.42</td> <!-- MLSum -->
   <td class="de know">39.82 ± 0.77 / 54.72 ± 0.59</td> <!-- MMLU-de -->
   <td class="de reason">53.82 ± 1.15 / 64.95 ± 0.94</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.03</td> <!-- ScandEval rank -->
   <td class="de ner">60.46 ± 1.26 / 47.72 ± 1.69</td> <!-- GermEval -->
   <td class="de sent">58.57 ± 2.53 / 71.30 ± 1.70</td> <!-- SB10k -->
   <td class="de la">26.25 ± 5.90 / 61.41 ± 3.94</td> <!-- ScaLA-de -->
   <td class="de rc">34.85 ± 3.43 / 64.05 ± 3.68</td> <!-- GermanQuAD -->
   <td class="de summ">69.58 ± 1.37 / 28.95 ± 2.96</td> <!-- MLSum -->
   <td class="de know">38.77 ± 0.95 / 53.99 ± 0.67</td> <!-- MMLU-de -->
   <td class="de reason">34.29 ± 1.05 / 49.79 ± 0.88</td> <!-- HellaSwag-de -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="de ner">67.61 ± 1.23 / 60.39 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">59.96 ± 2.00 / 70.71 ± 1.80</td> <!-- SB10k -->
   <td class="de la">28.25 ± 3.57 / 59.54 ± 3.88</td> <!-- ScaLA-de -->
   <td class="de rc">28.79 ± 2.02 / 55.82 ± 3.28</td> <!-- GermanQuAD -->
   <td class="de summ">66.87 ± 0.54 / 21.31 ± 1.47</td> <!-- MLSum -->
   <td class="de know">40.00 ± 0.97 / 54.88 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">45.93 ± 1.38 / 58.95 ± 1.06</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-HerO (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 467 / 744 ± 232</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="de ner">59.70 ± 2.05 / 50.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">60.22 ± 2.99 / 72.76 ± 2.10</td> <!-- SB10k -->
   <td class="de la">35.99 ± 4.53 / 67.21 ± 2.14</td> <!-- ScaLA-de -->
   <td class="de rc">29.68 ± 3.29 / 65.65 ± 3.10</td> <!-- GermanQuAD -->
   <td class="de summ">66.73 ± 0.80 / 21.40 ± 1.87</td> <!-- MLSum -->
   <td class="de know">30.53 ± 2.51 / 47.62 ± 1.82</td> <!-- MMLU-de -->
   <td class="de reason">45.02 ± 2.33 / 57.93 ± 1.79</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="de ner">59.68 ± 0.41 / 48.00 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.75 ± 2.36 / 68.54 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.22 ± 2.94 / 64.51 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">29.27 ± 1.03 / 59.19 ± 2.46</td> <!-- GermanQuAD -->
   <td class="de summ">66.64 ± 0.91 / 22.90 ± 2.24</td> <!-- MLSum -->
   <td class="de know">39.50 ± 0.93 / 54.61 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">51.29 ± 1.38 / 63.10 ± 1.12</td> <!-- HellaSwag-de -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.5</td> <!-- MMLU-de version -->
   <td>12.10.5</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>cstr/Spaetzle-v8-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,980 ± 1,031 / 1,714 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="de ner">58.90 ± 2.30 / 45.55 ± 3.30</td> <!-- GermEval -->
   <td class="de sent">61.34 ± 1.90 / 72.98 ± 1.30</td> <!-- SB10k -->
   <td class="de la">31.58 ± 4.39 / 65.51 ± 2.23</td> <!-- ScaLA-de -->
   <td class="de rc">24.91 ± 3.98 / 60.88 ± 3.31</td> <!-- GermanQuAD -->
   <td class="de summ">67.25 ± 1.06 / 22.95 ± 2.64</td> <!-- MLSum -->
   <td class="de know">34.62 ± 2.20 / 50.43 ± 1.52</td> <!-- MMLU-de -->
   <td class="de reason">48.70 ± 2.47 / 61.05 ± 1.79</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de rc">25.22 ± 3.84 / 60.93 ± 2.99</td> <!-- GermanQuAD -->
   <td class="de summ">67.31 ± 1.05 / 24.72 ± 2.95</td> <!-- MLSum -->
   <td class="de know">35.84 ± 2.16 / 51.64 ± 1.56</td> <!-- MMLU-de -->
   <td class="de reason">49.13 ± 2.71 / 61.68 ± 2.03</td> <!-- HellaSwag-de -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>9.3.2</td> <!-- MLSum version -->
   <td>9.3.2</td> <!-- MMLU-de version -->
   <td>9.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.14</td> <!-- ScandEval rank -->
   <td class="de ner">64.38 ± 1.60 / 50.26 ± 2.53</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.45 / 69.32 ± 1.02</td> <!-- SB10k -->
   <td class="de la">26.03 ± 2.23 / 61.88 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">25.68 ± 2.81 / 62.48 ± 2.93</td> <!-- GermanQuAD -->
   <td class="de summ">68.16 ± 0.95 / 24.52 ± 2.45</td> <!-- MLSum -->
   <td class="de know">33.84 ± 1.54 / 50.24 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">50.99 ± 0.99 / 63.11 ± 0.75</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="de ner">39.88 ± 2.56 / 35.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">56.23 ± 3.17 / 68.87 ± 2.73</td> <!-- SB10k -->
   <td class="de la">32.71 ± 1.60 / 64.55 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">36.58 ± 2.81 / 64.92 ± 2.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.41 ± 1.20 / 29.96 ± 3.00</td> <!-- MLSum -->
   <td class="de know">41.56 ± 0.82 / 54.79 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">30.77 ± 2.85 / 43.20 ± 2.53</td> <!-- HellaSwag-de -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.9.1</td> <!-- MLSum version -->
   <td>12.9.1</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="de ner">68.18 ± 0.95 / 57.72 ± 1.15</td> <!-- GermEval -->
   <td class="de sent">58.33 ± 2.83 / 69.31 ± 3.16</td> <!-- SB10k -->
   <td class="de la">29.12 ± 3.17 / 63.60 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 1.99 / 56.42 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.23 ± 0.49 / 16.56 ± 0.94</td> <!-- MLSum -->
   <td class="de know">38.44 ± 0.81 / 53.38 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">37.69 ± 1.00 / 51.24 ± 0.73</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/FC-SauerkrautLM-7b-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,160 ± 514 / 668 ± 256</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="de ner">56.70 ± 1.55 / 41.89 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">53.39 ± 1.89 / 67.16 ± 1.65</td> <!-- SB10k -->
   <td class="de la">35.64 ± 1.50 / 66.83 ± 0.97</td> <!-- ScaLA-de -->
   <td class="de rc">34.22 ± 1.43 / 67.00 ± 1.27</td> <!-- GermanQuAD -->
   <td class="de summ">64.79 ± 0.22 / 17.18 ± 0.74</td> <!-- MLSum -->
   <td class="de know">32.85 ± 0.79 / 49.55 ± 0.59</td> <!-- MMLU-de -->
   <td class="de reason">39.00 ± 2.60 / 53.77 ± 2.03</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="de ner">56.00 ± 1.94 / 43.49 ± 2.05</td> <!-- GermEval -->
   <td class="de sent">56.40 ± 3.89 / 70.17 ± 2.91</td> <!-- SB10k -->
   <td class="de la">22.01 ± 5.17 / 56.97 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de rc">35.39 ± 2.49 / 64.61 ± 2.42</td> <!-- GermanQuAD -->
   <td class="de summ">68.92 ± 0.99 / 26.93 ± 2.01</td> <!-- MLSum -->
   <td class="de know">38.12 ± 0.75 / 53.52 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">31.37 ± 1.37 / 47.65 ± 1.09</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">130976</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="de ner">55.36 ± 0.81 / 36.14 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">53.05 ± 2.34 / 65.57 ± 1.92</td> <!-- SB10k -->
   <td class="de la">23.08 ± 1.54 / 58.65 ± 2.04</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 1.09 / 62.02 ± 2.17</td> <!-- GermanQuAD -->
   <td class="de summ">67.33 ± 0.98 / 24.07 ± 2.44</td> <!-- MLSum -->
   <td class="de know">39.57 ± 0.74 / 54.67 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">51.26 ± 0.93 / 63.03 ± 0.69</td> <!-- HellaSwag-de -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="de ner">62.39 ± 2.72 / 50.86 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">53.16 ± 3.17 / 64.24 ± 3.42</td> <!-- SB10k -->
   <td class="de la">31.81 ± 5.15 / 62.15 ± 4.02</td> <!-- ScaLA-de -->
   <td class="de rc">28.99 ± 2.22 / 60.53 ± 2.92</td> <!-- GermanQuAD -->
   <td class="de summ">66.98 ± 0.87 / 22.66 ± 2.41</td> <!-- MLSum -->
   <td class="de know">35.72 ± 3.05 / 51.99 ± 2.09</td> <!-- MMLU-de -->
   <td class="de reason">35.26 ± 3.73 / 50.59 ± 3.17</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="de ner">55.76 ± 1.16 / 40.04 ± 3.21</td> <!-- GermEval -->
   <td class="de sent">55.91 ± 2.49 / 70.31 ± 1.76</td> <!-- SB10k -->
   <td class="de la">22.47 ± 3.37 / 56.77 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de rc">35.95 ± 1.89 / 66.86 ± 2.33</td> <!-- GermanQuAD -->
   <td class="de summ">68.08 ± 0.49 / 25.46 ± 1.45</td> <!-- MLSum -->
   <td class="de know">33.77 ± 0.86 / 49.44 ± 0.57</td> <!-- MMLU-de -->
   <td class="de reason">33.15 ± 1.86 / 48.23 ± 1.64</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.3.1</td> <!-- MMLU-de version -->
   <td>12.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="de ner">63.36 ± 2.68 / 51.59 ± 3.44</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 3.18 / 72.32 ± 2.23</td> <!-- SB10k -->
   <td class="de la">22.98 ± 8.11 / 60.88 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de rc">20.96 ± 3.59 / 57.36 ± 2.94</td> <!-- GermanQuAD -->
   <td class="de summ">67.58 ± 1.11 / 24.69 ± 2.94</td> <!-- MLSum -->
   <td class="de know">36.08 ± 1.55 / 51.68 ± 1.14</td> <!-- MMLU-de -->
   <td class="de reason">47.99 ± 2.87 / 60.55 ± 2.08</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de rc">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
   <td class="de summ">68.24 ± 0.70 / 25.71 ± 1.33</td> <!-- MLSum -->
   <td class="de know">35.63 ± 1.12 / 51.69 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">26.40 ± 1.86 / 43.98 ± 1.58</td> <!-- HellaSwag-de -->
   <td>9.1.2</td> <!-- GermEval version -->
   <td>9.1.2</td> <!-- SB10k version -->
   <td>9.1.2</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>11.0.0</td> <!-- MLSum version -->
   <td>9.1.2</td> <!-- MMLU-de version -->
   <td>9.2.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="de ner">54.68 ± 1.38 / 46.36 ± 2.67</td> <!-- GermEval -->
   <td class="de sent">55.48 ± 2.67 / 69.91 ± 1.90</td> <!-- SB10k -->
   <td class="de la">26.89 ± 0.86 / 62.51 ± 0.48</td> <!-- ScaLA-de -->
   <td class="de rc">31.27 ± 1.89 / 62.30 ± 2.09</td> <!-- GermanQuAD -->
   <td class="de summ">66.33 ± 0.75 / 20.58 ± 1.77</td> <!-- MLSum -->
   <td class="de know">33.98 ± 0.82 / 50.12 ± 0.65</td> <!-- MMLU-de -->
   <td class="de reason">34.59 ± 1.42 / 49.13 ± 1.25</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,410 ± 299 / 370 ± 127</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="de ner">41.41 ± 2.64 / 26.93 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">52.78 ± 4.59 / 66.87 ± 4.26</td> <!-- SB10k -->
   <td class="de la">27.75 ± 1.14 / 63.54 ± 0.69</td> <!-- ScaLA-de -->
   <td class="de rc">29.24 ± 2.44 / 58.33 ± 3.45</td> <!-- GermanQuAD -->
   <td class="de summ">66.11 ± 1.41 / 22.22 ± 3.65</td> <!-- MLSum -->
   <td class="de know">42.38 ± 0.74 / 56.56 ± 0.55</td> <!-- MMLU-de -->
   <td class="de reason">44.47 ± 2.47 / 56.41 ± 2.21</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="de ner">55.32 ± 1.55 / 48.33 ± 1.45</td> <!-- GermEval -->
   <td class="de sent">52.49 ± 2.16 / 67.50 ± 1.61</td> <!-- SB10k -->
   <td class="de la">24.34 ± 2.29 / 59.66 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">31.54 ± 3.00 / 59.96 ± 3.89</td> <!-- GermanQuAD -->
   <td class="de summ">68.98 ± 1.14 / 28.30 ± 2.36</td> <!-- MLSum -->
   <td class="de know">35.12 ± 0.59 / 51.23 ± 0.46</td> <!-- MMLU-de -->
   <td class="de reason">28.89 ± 1.81 / 45.85 ± 1.47</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="de ner">55.41 ± 1.45 / 48.39 ± 1.46</td> <!-- GermEval -->
   <td class="de sent">52.58 ± 2.42 / 67.52 ± 1.82</td> <!-- SB10k -->
   <td class="de la">24.10 ± 2.12 / 59.47 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">31.52 ± 2.95 / 60.03 ± 3.81</td> <!-- GermanQuAD -->
   <td class="de summ">68.96 ± 1.13 / 28.26 ± 2.32</td> <!-- MLSum -->
   <td class="de know">35.06 ± 0.54 / 51.20 ± 0.43</td> <!-- MMLU-de -->
   <td class="de reason">28.85 ± 1.70 / 45.83 ± 1.39</td> <!-- HellaSwag-de -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="de ner">48.11 ± 2.01 / 39.66 ± 3.29</td> <!-- GermEval -->
   <td class="de sent">54.96 ± 2.69 / 69.64 ± 2.09</td> <!-- SB10k -->
   <td class="de la">21.57 ± 4.18 / 55.63 ± 4.56</td> <!-- ScaLA-de -->
   <td class="de rc">31.49 ± 3.11 / 61.33 ± 3.41</td> <!-- GermanQuAD -->
   <td class="de summ">68.88 ± 0.67 / 27.13 ± 1.71</td> <!-- MLSum -->
   <td class="de know">32.39 ± 0.86 / 49.12 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">29.84 ± 1.54 / 46.53 ± 1.31</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.3.1</td> <!-- GermanQuAD version -->
   <td>12.3.1</td> <!-- MLSum version -->
   <td>12.3.1</td> <!-- MMLU-de version -->
   <td>12.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="de ner">52.63 ± 1.89 / 42.99 ± 2.40</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de rc">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.43 ± 0.97 / 29.48 ± 2.59</td> <!-- MLSum -->
   <td class="de know">32.56 ± 1.16 / 49.02 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">23.61 ± 2.42 / 41.55 ± 2.14</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.2.0</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.3.1</td> <!-- MMLU-de version -->
   <td>12.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-7B-German-V0.1-DPO (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,070 ± 1,042 / 1,769 ± 573</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="de ner">48.92 ± 2.76 / 38.62 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">52.57 ± 1.74 / 61.25 ± 2.84</td> <!-- SB10k -->
   <td class="de la">20.74 ± 3.20 / 56.59 ± 3.27</td> <!-- ScaLA-de -->
   <td class="de rc">32.87 ± 1.83 / 62.31 ± 2.13</td> <!-- GermanQuAD -->
   <td class="de summ">68.88 ± 0.80 / 27.84 ± 2.07</td> <!-- MLSum -->
   <td class="de know">31.38 ± 0.94 / 48.36 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">29.83 ± 1.76 / 46.77 ± 1.39</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.2</td> <!-- SB10k version -->
   <td>12.3.2</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.3.2</td> <!-- MMLU-de version -->
   <td>12.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-7B-German-V0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,065 ± 1,038 / 1,766 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="de ner">48.35 ± 2.96 / 38.58 ± 2.35</td> <!-- GermEval -->
   <td class="de sent">52.51 ± 1.72 / 61.27 ± 2.77</td> <!-- SB10k -->
   <td class="de la">20.36 ± 3.59 / 56.14 ± 3.61</td> <!-- ScaLA-de -->
   <td class="de rc">32.88 ± 1.78 / 62.19 ± 2.05</td> <!-- GermanQuAD -->
   <td class="de summ">68.82 ± 0.81 / 27.89 ± 2.09</td> <!-- MLSum -->
   <td class="de know">31.36 ± 0.96 / 48.34 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">29.98 ± 1.64 / 46.82 ± 1.33</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.2</td> <!-- SB10k version -->
   <td>12.3.2</td> <!-- ScaLA-de version -->
   <td>12.3.2</td> <!-- GermanQuAD version -->
   <td>12.3.2</td> <!-- MLSum version -->
   <td>12.3.2</td> <!-- MMLU-de version -->
   <td>12.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="de ner">57.57 ± 1.46 / 44.84 ± 2.12</td> <!-- GermEval -->
   <td class="de sent">49.40 ± 2.11 / 63.02 ± 2.68</td> <!-- SB10k -->
   <td class="de la">23.32 ± 2.20 / 59.16 ± 2.36</td> <!-- ScaLA-de -->
   <td class="de rc">30.24 ± 1.18 / 61.10 ± 1.87</td> <!-- GermanQuAD -->
   <td class="de summ">68.01 ± 1.28 / 25.44 ± 3.23</td> <!-- MLSum -->
   <td class="de know">27.06 ± 0.92 / 45.06 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">26.96 ± 0.49 / 44.79 ± 0.39</td> <!-- HellaSwag-de -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   <td>12.11.0</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="de ner">52.08 ± 1.86 / 46.67 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">46.38 ± 2.70 / 60.32 ± 2.80</td> <!-- SB10k -->
   <td class="de la">22.39 ± 3.96 / 57.26 ± 4.22</td> <!-- ScaLA-de -->
   <td class="de rc">33.43 ± 2.38 / 62.65 ± 2.83</td> <!-- GermanQuAD -->
   <td class="de summ">69.50 ± 1.29 / 29.74 ± 3.10</td> <!-- MLSum -->
   <td class="de know">28.79 ± 1.53 / 45.87 ± 1.26</td> <!-- MMLU-de -->
   <td class="de reason">21.50 ± 2.52 / 39.80 ± 2.47</td> <!-- HellaSwag-de -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="de ner">51.39 ± 1.35 / 44.47 ± 2.77</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.68 / 28.27 ± 1.70</td> <!-- MLSum -->
   <td class="de know">32.49 ± 0.91 / 48.82 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">22.25 ± 2.13 / 40.28 ± 1.67</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.2.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-13B-German-V0.1-DPO (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">789 ± 78 / 346 ± 102</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="de ner">52.45 ± 2.98 / 47.91 ± 2.37</td> <!-- GermEval -->
   <td class="de sent">49.73 ± 2.78 / 63.68 ± 2.80</td> <!-- SB10k -->
   <td class="de la">20.72 ± 4.25 / 53.77 ± 5.69</td> <!-- ScaLA-de -->
   <td class="de rc">30.18 ± 4.61 / 60.07 ± 5.86</td> <!-- GermanQuAD -->
   <td class="de summ">68.97 ± 0.69 / 26.66 ± 1.82</td> <!-- MLSum -->
   <td class="de know">27.71 ± 0.66 / 45.34 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">21.44 ± 2.29 / 40.21 ± 1.74</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="de ner">57.02 ± 1.39 / 47.95 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.02 / 62.41 ± 3.30</td> <!-- SB10k -->
   <td class="de la">19.80 ± 3.22 / 52.76 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 2.01 / 57.65 ± 2.01</td> <!-- GermanQuAD -->
   <td class="de summ">66.83 ± 0.91 / 23.62 ± 2.07</td> <!-- MLSum -->
   <td class="de know">25.99 ± 1.00 / 44.39 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">24.90 ± 1.40 / 43.26 ± 1.22</td> <!-- HellaSwag-de -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>mayflowergmbh/Wiedervereinigung-7b-dpo (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,374 ± 432 / 744 ± 230</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="de ner">52.17 ± 2.87 / 40.26 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">51.92 ± 3.19 / 67.12 ± 2.11</td> <!-- SB10k -->
   <td class="de la">29.06 ± 5.04 / 62.77 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de rc">14.59 ± 2.77 / 50.41 ± 3.79</td> <!-- GermanQuAD -->
   <td class="de summ">63.78 ± 0.48 / 15.45 ± 0.60</td> <!-- MLSum -->
   <td class="de know">35.38 ± 1.08 / 51.48 ± 0.84</td> <!-- MMLU-de -->
   <td class="de reason">34.16 ± 3.12 / 49.73 ± 2.20</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="de ner">55.10 ± 1.35 / 41.89 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">47.69 ± 2.35 / 64.93 ± 1.71</td> <!-- SB10k -->
   <td class="de la">24.14 ± 2.09 / 60.83 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">23.93 ± 2.11 / 57.64 ± 1.89</td> <!-- GermanQuAD -->
   <td class="de summ">67.51 ± 0.71 / 22.63 ± 1.73</td> <!-- MLSum -->
   <td class="de know">26.06 ± 1.65 / 44.13 ± 1.29</td> <!-- MMLU-de -->
   <td class="de reason">31.09 ± 1.35 / 47.48 ± 0.98</td> <!-- HellaSwag-de -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="de ner">50.66 ± 1.53 / 39.89 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">54.79 ± 3.53 / 68.79 ± 3.00</td> <!-- SB10k -->
   <td class="de la">20.17 ± 1.69 / 58.67 ± 1.13</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 4.70 / 54.38 ± 5.91</td> <!-- GermanQuAD -->
   <td class="de summ">65.53 ± 1.07 / 19.46 ± 1.48</td> <!-- MLSum -->
   <td class="de know">27.04 ± 1.04 / 44.99 ± 0.77</td> <!-- MMLU-de -->
   <td class="de reason">17.47 ± 3.26 / 36.70 ± 2.93</td> <!-- HellaSwag-de -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   <td>12.5.3</td> <!-- MLSum version -->
   <td>12.5.3</td> <!-- MMLU-de version -->
   <td>12.5.3</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="de ner">37.31 ± 2.28 / 31.09 ± 2.10</td> <!-- GermEval -->
   <td class="de sent">46.23 ± 2.32 / 63.45 ± 1.57</td> <!-- SB10k -->
   <td class="de la">23.26 ± 1.16 / 60.73 ± 0.24</td> <!-- ScaLA-de -->
   <td class="de rc">28.01 ± 1.95 / 59.66 ± 2.10</td> <!-- GermanQuAD -->
   <td class="de summ">66.35 ± 0.99 / 21.43 ± 2.27</td> <!-- MLSum -->
   <td class="de know">30.11 ± 1.02 / 47.48 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">35.25 ± 0.64 / 50.80 ± 0.55</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="de ner">49.85 ± 1.96 / 41.04 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.65 ± 1.58 / 65.94 ± 2.42</td> <!-- SB10k -->
   <td class="de la">3.17 ± 5.20 / 36.54 ± 5.71</td> <!-- ScaLA-de -->
   <td class="de rc">29.37 ± 3.48 / 58.09 ± 4.16</td> <!-- GermanQuAD -->
   <td class="de summ">67.96 ± 1.38 / 25.30 ± 2.54</td> <!-- MLSum -->
   <td class="de know">29.56 ± 0.63 / 46.21 ± 0.55</td> <!-- MMLU-de -->
   <td class="de reason">16.15 ± 1.34 / 35.40 ± 1.27</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32797</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="de ner">47.19 ± 3.74 / 33.02 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">47.26 ± 3.14 / 63.48 ± 2.94</td> <!-- SB10k -->
   <td class="de la">22.32 ± 1.78 / 56.73 ± 4.00</td> <!-- ScaLA-de -->
   <td class="de rc">24.36 ± 3.78 / 54.61 ± 4.44</td> <!-- GermanQuAD -->
   <td class="de summ">67.75 ± 1.10 / 25.91 ± 2.95</td> <!-- MLSum -->
   <td class="de know">26.79 ± 1.01 / 44.58 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">20.33 ± 1.63 / 39.63 ± 1.09</td> <!-- HellaSwag-de -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="de ner">48.20 ± 1.57 / 39.04 ± 2.38</td> <!-- GermEval -->
   <td class="de sent">47.12 ± 4.20 / 59.69 ± 4.45</td> <!-- SB10k -->
   <td class="de la">12.39 ± 1.39 / 45.13 ± 3.93</td> <!-- ScaLA-de -->
   <td class="de rc">30.50 ± 3.67 / 57.48 ± 4.51</td> <!-- GermanQuAD -->
   <td class="de summ">65.48 ± 1.73 / 22.72 ± 3.33</td> <!-- MLSum -->
   <td class="de know">30.83 ± 1.40 / 48.12 ± 1.03</td> <!-- MMLU-de -->
   <td class="de reason">24.90 ± 1.67 / 43.21 ± 1.49</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM_German_7b_v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,972 ± 315 / 689 ± 204</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="de ner">42.39 ± 2.43 / 32.42 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">48.67 ± 3.85 / 59.21 ± 4.18</td> <!-- SB10k -->
   <td class="de la">8.72 ± 2.15 / 43.37 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de rc">36.12 ± 2.35 / 66.54 ± 2.34</td> <!-- GermanQuAD -->
   <td class="de summ">68.47 ± 1.27 / 26.03 ± 3.68</td> <!-- MLSum -->
   <td class="de know">23.99 ± 1.15 / 41.69 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">20.76 ± 1.28 / 38.13 ± 1.29</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.71</td> <!-- ScandEval rank -->
   <td class="de ner">55.52 ± 2.07 / 46.18 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">50.52 ± 2.29 / 62.39 ± 2.63</td> <!-- SB10k -->
   <td class="de la">9.87 ± 2.95 / 42.20 ± 3.60</td> <!-- ScaLA-de -->
   <td class="de rc">20.20 ± 3.28 / 47.02 ± 5.20</td> <!-- GermanQuAD -->
   <td class="de summ">66.40 ± 0.98 / 21.21 ± 2.33</td> <!-- MLSum -->
   <td class="de know">33.58 ± 0.41 / 50.27 ± 0.28</td> <!-- MMLU-de -->
   <td class="de reason">28.97 ± 1.01 / 46.45 ± 0.80</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="de ner">45.81 ± 1.27 / 39.33 ± 2.24</td> <!-- GermEval -->
   <td class="de sent">34.61 ± 3.47 / 44.53 ± 3.65</td> <!-- SB10k -->
   <td class="de la">16.19 ± 3.33 / 54.43 ± 3.53</td> <!-- ScaLA-de -->
   <td class="de rc">28.25 ± 4.10 / 57.52 ± 4.47</td> <!-- GermanQuAD -->
   <td class="de summ">67.90 ± 0.72 / 26.38 ± 1.63</td> <!-- MLSum -->
   <td class="de know">28.28 ± 0.88 / 46.06 ± 0.73</td> <!-- MMLU-de -->
   <td class="de reason">28.25 ± 2.23 / 45.60 ± 2.02</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="de ner">53.30 ± 0.87 / 47.62 ± 1.30</td> <!-- GermEval -->
   <td class="de sent">44.95 ± 3.84 / 62.77 ± 2.82</td> <!-- SB10k -->
   <td class="de la">18.67 ± 1.83 / 57.35 ± 3.01</td> <!-- ScaLA-de -->
   <td class="de rc">28.10 ± 1.17 / 58.38 ± 1.45</td> <!-- GermanQuAD -->
   <td class="de summ">65.95 ± 0.58 / 20.96 ± 1.39</td> <!-- MLSum -->
   <td class="de know">23.84 ± 0.97 / 42.69 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">16.86 ± 1.12 / 35.87 ± 1.30</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="de ner">59.07 ± 0.78 / 51.00 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.44 / 65.93 ± 1.66</td> <!-- SB10k -->
   <td class="de la">14.71 ± 2.21 / 53.75 ± 3.07</td> <!-- ScaLA-de -->
   <td class="de rc">29.45 ± 2.13 / 56.14 ± 2.53</td> <!-- GermanQuAD -->
   <td class="de summ">67.78 ± 1.54 / 26.66 ± 3.40</td> <!-- MLSum -->
   <td class="de know">16.39 ± 1.29 / 37.35 ± 0.95</td> <!-- MMLU-de -->
   <td class="de reason">10.68 ± 1.41 / 32.52 ± 1.35</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/Llama3-German-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 462 / 673 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="de ner">54.34 ± 2.04 / 46.23 ± 2.24</td> <!-- GermEval -->
   <td class="de sent">58.32 ± 1.14 / 70.24 ± 0.99</td> <!-- SB10k -->
   <td class="de la">25.70 ± 5.38 / 58.58 ± 4.44</td> <!-- ScaLA-de -->
   <td class="de rc">0.50 ± 0.11 / 35.35 ± 1.23</td> <!-- GermanQuAD -->
   <td class="de summ">62.61 ± 1.58 / 13.97 ± 1.64</td> <!-- MLSum -->
   <td class="de know">38.63 ± 0.90 / 53.83 ± 0.67</td> <!-- MMLU-de -->
   <td class="de reason">33.51 ± 2.18 / 49.52 ± 1.89</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="de ner">47.31 ± 1.67 / 31.36 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">48.28 ± 4.28 / 64.07 ± 3.81</td> <!-- SB10k -->
   <td class="de la">14.08 ± 1.29 / 52.67 ± 2.70</td> <!-- ScaLA-de -->
   <td class="de rc">28.37 ± 4.07 / 55.92 ± 4.76</td> <!-- GermanQuAD -->
   <td class="de summ">61.97 ± 1.94 / 19.06 ± 1.18</td> <!-- MLSum -->
   <td class="de know">22.99 ± 0.83 / 41.98 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">20.06 ± 1.95 / 38.69 ± 1.78</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="de ner">50.09 ± 1.33 / 38.59 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">46.52 ± 2.85 / 63.64 ± 2.10</td> <!-- SB10k -->
   <td class="de la">15.23 ± 1.71 / 55.08 ± 1.88</td> <!-- ScaLA-de -->
   <td class="de rc">25.54 ± 3.58 / 56.07 ± 3.76</td> <!-- GermanQuAD -->
   <td class="de summ">67.62 ± 0.89 / 23.52 ± 2.43</td> <!-- MLSum -->
   <td class="de know">20.12 ± 1.13 / 39.48 ± 1.02</td> <!-- MMLU-de -->
   <td class="de reason">13.98 ± 1.56 / 34.07 ± 1.30</td> <!-- HellaSwag-de -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="de ner">43.02 ± 1.93 / 32.69 ± 1.98</td> <!-- GermEval -->
   <td class="de sent">50.21 ± 2.43 / 65.81 ± 1.82</td> <!-- SB10k -->
   <td class="de la">15.79 ± 2.35 / 53.25 ± 4.45</td> <!-- ScaLA-de -->
   <td class="de rc">28.57 ± 5.09 / 55.54 ± 6.14</td> <!-- GermanQuAD -->
   <td class="de summ">68.68 ± 0.96 / 26.95 ± 1.81</td> <!-- MLSum -->
   <td class="de know">18.38 ± 1.36 / 38.12 ± 1.19</td> <!-- MMLU-de -->
   <td class="de reason">8.45 ± 1.86 / 30.07 ± 1.49</td> <!-- HellaSwag-de -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.87</td> <!-- ScandEval rank -->
   <td class="de ner">42.08 ± 1.65 / 36.90 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td class="de summ">65.56 ± 1.65 / 20.45 ± 2.68</td> <!-- MLSum -->
   <td class="de know">23.76 ± 0.70 / 42.77 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">20.92 ± 1.16 / 40.56 ± 0.86</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="de ner">54.45 ± 1.17 / 42.36 ± 2.59</td> <!-- GermEval -->
   <td class="de sent">43.62 ± 3.18 / 59.82 ± 2.70</td> <!-- SB10k -->
   <td class="de la">15.24 ± 1.87 / 55.49 ± 2.89</td> <!-- ScaLA-de -->
   <td class="de rc">26.00 ± 2.28 / 51.82 ± 2.70</td> <!-- GermanQuAD -->
   <td class="de summ">66.68 ± 1.30 / 24.80 ± 3.14</td> <!-- MLSum -->
   <td class="de know">15.81 ± 1.07 / 36.18 ± 0.94</td> <!-- MMLU-de -->
   <td class="de reason">9.60 ± 1.12 / 31.31 ± 1.02</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="de ner">39.41 ± 2.30 / 36.17 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">49.42 ± 4.33 / 61.57 ± 5.43</td> <!-- SB10k -->
   <td class="de la">6.02 ± 2.53 / 46.41 ± 4.35</td> <!-- ScaLA-de -->
   <td class="de rc">27.69 ± 4.39 / 54.92 ± 5.38</td> <!-- GermanQuAD -->
   <td class="de summ">66.75 ± 0.68 / 23.16 ± 0.88</td> <!-- MLSum -->
   <td class="de know">20.77 ± 0.92 / 39.29 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">10.47 ± 1.51 / 31.09 ± 1.36</td> <!-- HellaSwag-de -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="de ner">54.20 ± 1.00 / 48.58 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">15.43 ± 3.70 / 43.11 ± 2.77</td> <!-- SB10k -->
   <td class="de la">17.49 ± 1.23 / 57.46 ± 1.12</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 5.36 / 60.07 ± 4.46</td> <!-- GermanQuAD -->
   <td class="de summ">64.87 ± 0.47 / 22.25 ± 1.89</td> <!-- MLSum -->
   <td class="de know">22.10 ± 0.68 / 40.39 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">18.58 ± 1.48 / 36.49 ± 1.24</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="de ner">19.69 ± 4.71 / 19.53 ± 3.13</td> <!-- GermEval -->
   <td class="de sent">50.36 ± 2.83 / 60.36 ± 3.45</td> <!-- SB10k -->
   <td class="de la">9.07 ± 2.41 / 44.45 ± 4.37</td> <!-- ScaLA-de -->
   <td class="de rc">27.06 ± 4.74 / 53.36 ± 6.20</td> <!-- GermanQuAD -->
   <td class="de summ">68.52 ± 1.47 / 26.96 ± 3.01</td> <!-- MLSum -->
   <td class="de know">26.50 ± 0.89 / 44.19 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">9.36 ± 1.35 / 30.60 ± 1.18</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="de ner">39.21 ± 2.29 / 36.08 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">58.36 ± 1.80 / 71.98 ± 1.17</td> <!-- SB10k -->
   <td class="de la">7.03 ± 3.09 / 50.18 ± 3.74</td> <!-- ScaLA-de -->
   <td class="de rc">27.02 ± 3.09 / 51.94 ± 4.17</td> <!-- GermanQuAD -->
   <td class="de summ">68.59 ± 0.76 / 25.49 ± 2.17</td> <!-- MLSum -->
   <td class="de know">3.52 ± 0.84 / 26.38 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">0.06 ± 0.82 / 24.56 ± 0.78</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="de ner">40.61 ± 2.18 / 28.49 ± 2.11</td> <!-- GermEval -->
   <td class="de sent">31.86 ± 3.60 / 42.96 ± 3.98</td> <!-- SB10k -->
   <td class="de la">5.36 ± 3.96 / 37.83 ± 4.03</td> <!-- ScaLA-de -->
   <td class="de rc">25.99 ± 3.85 / 47.72 ± 4.74</td> <!-- GermanQuAD -->
   <td class="de summ">66.77 ± 0.94 / 23.71 ± 1.90</td> <!-- MLSum -->
   <td class="de know">22.17 ± 1.05 / 41.55 ± 0.85</td> <!-- MMLU-de -->
   <td class="de reason">22.61 ± 1.75 / 41.16 ± 1.46</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="de ner">31.52 ± 2.96 / 29.20 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de rc">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.88 ± 1.25 / 21.37 ± 1.87</td> <!-- MLSum -->
   <td class="de know">21.32 ± 1.14 / 40.66 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">21.35 ± 0.89 / 40.77 ± 0.65</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 2.45 / 67.63 ± 1.87</td> <!-- SB10k -->
   <td class="de la">7.33 ± 2.53 / 37.69 ± 2.51</td> <!-- ScaLA-de -->
   <td class="de rc">30.05 ± 1.59 / 57.13 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.09 ± 1.28 / 23.20 ± 2.54</td> <!-- MLSum -->
   <td class="de know">30.33 ± 0.78 / 47.68 ± 0.54</td> <!-- MMLU-de -->
   <td class="de reason">22.89 ± 1.14 / 41.15 ± 1.08</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="de ner">37.68 ± 1.26 / 33.74 ± 1.78</td> <!-- GermEval -->
   <td class="de sent">46.00 ± 3.63 / 61.88 ± 2.94</td> <!-- SB10k -->
   <td class="de la">0.83 ± 0.84 / 33.38 ± 0.28</td> <!-- ScaLA-de -->
   <td class="de rc">26.65 ± 4.01 / 53.15 ± 4.26</td> <!-- GermanQuAD -->
   <td class="de summ">64.14 ± 0.38 / 18.78 ± 0.63</td> <!-- MLSum -->
   <td class="de know">18.12 ± 0.96 / 37.66 ± 1.06</td> <!-- MMLU-de -->
   <td class="de reason">9.92 ± 2.59 / 31.17 ± 1.75</td> <!-- HellaSwag-de -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   <td>12.10.5</td> <!-- MLSum version -->
   <td>12.10.8</td> <!-- MMLU-de version -->
   <td>12.10.8</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.25</td> <!-- ScandEval rank -->
   <td class="de ner">34.81 ± 2.51 / 30.33 ± 2.95</td> <!-- GermEval -->
   <td class="de sent">51.01 ± 2.18 / 65.35 ± 2.23</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.40 ± 3.91 / 49.38 ± 4.65</td> <!-- GermanQuAD -->
   <td class="de summ">63.53 ± 2.45 / 17.65 ± 2.20</td> <!-- MLSum -->
   <td class="de know">11.23 ± 0.71 / 33.23 ± 0.76</td> <!-- MMLU-de -->
   <td class="de reason">7.25 ± 1.63 / 29.15 ± 1.35</td> <!-- HellaSwag-de -->
   <td>12.10.8</td> <!-- GermEval version -->
   <td>12.10.8</td> <!-- SB10k version -->
   <td>12.10.8</td> <!-- ScaLA-de version -->
   <td>12.10.8</td> <!-- GermanQuAD version -->
   <td>12.10.8</td> <!-- MLSum version -->
   <td>12.10.8</td> <!-- MMLU-de version -->
   <td>12.10.8</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32797</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">47.67 ± 2.82 / 60.09 ± 3.28</td> <!-- SB10k -->
   <td class="de la">9.67 ± 2.79 / 46.35 ± 4.48</td> <!-- ScaLA-de -->
   <td class="de rc">26.23 ± 3.79 / 53.16 ± 4.52</td> <!-- GermanQuAD -->
   <td class="de summ">65.42 ± 0.61 / 18.57 ± 0.70</td> <!-- MLSum -->
   <td class="de know">19.03 ± 1.34 / 36.86 ± 1.84</td> <!-- MMLU-de -->
   <td class="de reason">9.87 ± 1.98 / 30.31 ± 1.95</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="de ner">49.16 ± 2.12 / 40.34 ± 2.81</td> <!-- GermEval -->
   <td class="de sent">35.17 ± 4.48 / 51.15 ± 4.55</td> <!-- SB10k -->
   <td class="de la">9.79 ± 2.06 / 50.77 ± 3.64</td> <!-- ScaLA-de -->
   <td class="de rc">22.48 ± 2.59 / 45.90 ± 3.03</td> <!-- GermanQuAD -->
   <td class="de summ">60.81 ± 0.38 / 15.92 ± 0.54</td> <!-- MLSum -->
   <td class="de know">6.89 ± 0.76 / 28.82 ± 0.69</td> <!-- MMLU-de -->
   <td class="de reason">4.79 ± 0.91 / 28.40 ± 0.78</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="de ner">42.51 ± 1.31 / 37.05 ± 1.59</td> <!-- GermEval -->
   <td class="de sent">38.26 ± 2.34 / 55.52 ± 2.66</td> <!-- SB10k -->
   <td class="de la">5.48 ± 1.36 / 48.23 ± 2.44</td> <!-- ScaLA-de -->
   <td class="de rc">19.43 ± 3.10 / 41.82 ± 3.29</td> <!-- GermanQuAD -->
   <td class="de summ">60.81 ± 1.75 / 13.79 ± 2.22</td> <!-- MLSum -->
   <td class="de know">16.06 ± 1.35 / 36.96 ± 0.92</td> <!-- MMLU-de -->
   <td class="de reason">6.64 ± 0.55 / 29.12 ± 0.60</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,607 ± 565 / 1,212 ± 349</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="de ner">12.21 ± 2.76 / 11.93 ± 2.08</td> <!-- GermEval -->
   <td class="de sent">44.84 ± 2.70 / 57.27 ± 3.65</td> <!-- SB10k -->
   <td class="de la">2.02 ± 2.19 / 37.47 ± 3.26</td> <!-- ScaLA-de -->
   <td class="de rc">24.59 ± 2.70 / 49.79 ± 2.96</td> <!-- GermanQuAD -->
   <td class="de summ">62.87 ± 2.44 / 18.13 ± 1.20</td> <!-- MLSum -->
   <td class="de know">16.35 ± 0.62 / 36.72 ± 0.48</td> <!-- MMLU-de -->
   <td class="de reason">8.93 ± 0.99 / 30.43 ± 0.75</td> <!-- HellaSwag-de -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   <td>12.6.1</td> <!-- MLSum version -->
   <td>12.6.1</td> <!-- MMLU-de version -->
   <td>12.6.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="de ner">16.95 ± 2.96 / 15.80 ± 2.16</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de rc">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.96 / 22.24 ± 1.37</td> <!-- MLSum -->
   <td class="de know">12.11 ± 0.94 / 33.12 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">7.32 ± 1.40 / 30.11 ± 1.16</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="de ner">32.33 ± 2.48 / 30.20 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">26.39 ± 5.23 / 36.06 ± 6.62</td> <!-- SB10k -->
   <td class="de la">1.44 ± 1.38 / 33.60 ± 0.42</td> <!-- ScaLA-de -->
   <td class="de rc">28.15 ± 5.57 / 54.13 ± 6.75</td> <!-- GermanQuAD -->
   <td class="de summ">58.62 ± 3.80 / 13.54 ± 2.20</td> <!-- MLSum -->
   <td class="de know">14.94 ± 1.09 / 35.44 ± 0.89</td> <!-- MMLU-de -->
   <td class="de reason">8.70 ± 0.96 / 31.09 ± 0.58</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="de ner">36.62 ± 1.56 / 28.22 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de rc">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td class="de summ">63.02 ± 2.00 / 19.54 ± 1.33</td> <!-- MLSum -->
   <td class="de know">12.27 ± 1.33 / 33.40 ± 1.08</td> <!-- MMLU-de -->
   <td class="de reason">6.57 ± 0.74 / 28.60 ± 0.70</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="de ner">28.04 ± 2.71 / 24.08 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td class="de summ">61.47 ± 1.67 / 12.62 ± 1.40</td> <!-- MLSum -->
   <td class="de know">13.44 ± 1.22 / 34.26 ± 0.98</td> <!-- MMLU-de -->
   <td class="de reason">8.31 ± 1.08 / 31.05 ± 0.84</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-70B-German-V0.1 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">294 ± 21 / 168 ± 42</td> <!-- Model inference speed -->
   <td class="rank">3.66</td> <!-- ScandEval rank -->
   <td class="de ner">59.23 ± 2.95 / 52.06 ± 3.03</td> <!-- GermEval -->
   <td class="de sent">-5.01 ± 4.03 / 18.00 ± 0.71</td> <!-- SB10k -->
   <td class="de la">3.19 ± 4.99 / 37.63 ± 3.16</td> <!-- ScaLA-de -->
   <td class="de rc">19.84 ± 2.17 / 56.60 ± 3.00</td> <!-- GermanQuAD -->
   <td class="de summ">62.42 ± 4.28 / 22.39 ± 3.89</td> <!-- MLSum -->
   <td class="de know">18.40 ± 3.05 / 34.38 ± 2.84</td> <!-- MMLU-de -->
   <td class="de reason">1.52 ± 1.25 / 26.80 ± 1.34</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.67</td> <!-- ScandEval rank -->
   <td class="de ner">34.53 ± 1.24 / 29.89 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">42.90 ± 2.66 / 56.64 ± 4.71</td> <!-- SB10k -->
   <td class="de la">1.51 ± 1.64 / 43.36 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">15.83 ± 1.42 / 29.77 ± 2.54</td> <!-- GermanQuAD -->
   <td class="de summ">61.40 ± 3.15 / 14.84 ± 2.07</td> <!-- MLSum -->
   <td class="de know">-1.84 ± 1.09 / 23.98 ± 0.66</td> <!-- MMLU-de -->
   <td class="de reason">-0.12 ± 1.30 / 24.41 ± 0.96</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="de ner">24.79 ± 6.48 / 22.92 ± 5.74</td> <!-- GermEval -->
   <td class="de sent">47.65 ± 2.85 / 63.11 ± 2.17</td> <!-- SB10k -->
   <td class="de la">2.39 ± 1.46 / 39.92 ± 4.38</td> <!-- ScaLA-de -->
   <td class="de rc">13.39 ± 4.13 / 33.76 ± 5.50</td> <!-- GermanQuAD -->
   <td class="de summ">61.07 ± 4.19 / 16.72 ± 4.33</td> <!-- MLSum -->
   <td class="de know">3.94 ± 1.35 / 27.78 ± 1.07</td> <!-- MMLU-de -->
   <td class="de reason">0.90 ± 0.98 / 25.40 ± 0.65</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.72</td> <!-- ScandEval rank -->
   <td class="de ner">25.69 ± 1.43 / 25.95 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">33.48 ± 2.83 / 47.14 ± 4.43</td> <!-- SB10k -->
   <td class="de la">3.73 ± 1.14 / 44.43 ± 4.17</td> <!-- ScaLA-de -->
   <td class="de rc">14.82 ± 2.69 / 35.50 ± 3.15</td> <!-- GermanQuAD -->
   <td class="de summ">63.85 ± 2.30 / 21.16 ± 3.79</td> <!-- MLSum -->
   <td class="de know">2.96 ± 0.44 / 26.82 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">1.88 ± 0.93 / 26.35 ± 1.20</td> <!-- HellaSwag-de -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="de ner">49.38 ± 2.20 / 42.66 ± 3.24</td> <!-- GermEval -->
   <td class="de sent">41.72 ± 4.07 / 60.45 ± 3.07</td> <!-- SB10k -->
   <td class="de la">7.67 ± 1.52 / 46.66 ± 3.23</td> <!-- ScaLA-de -->
   <td class="de rc">13.70 ± 2.43 / 30.21 ± 3.80</td> <!-- GermanQuAD -->
   <td class="de summ">45.88 ± 3.36 / 8.30 ± 1.98</td> <!-- MLSum -->
   <td class="de know">8.73 ± 1.03 / 31.46 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">6.18 ± 1.33 / 29.78 ± 1.02</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="de ner">9.23 ± 4.86 / 10.43 ± 3.83</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de rc">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td class="de summ">61.74 ± 1.58 / 14.71 ± 1.12</td> <!-- MLSum -->
   <td class="de know">13.65 ± 1.17 / 33.35 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">8.86 ± 0.99 / 30.21 ± 0.77</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 5.06 / 49.68 ± 5.74</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de rc">20.44 ± 3.29 / 45.50 ± 3.33</td> <!-- GermanQuAD -->
   <td class="de summ">60.50 ± 0.63 / 13.71 ± 0.75</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="de ner">24.35 ± 1.72 / 21.90 ± 0.85</td> <!-- GermEval -->
   <td class="de sent">43.35 ± 3.81 / 60.49 ± 3.18</td> <!-- SB10k -->
   <td class="de la">2.38 ± 1.21 / 37.27 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">15.56 ± 2.24 / 34.68 ± 3.15</td> <!-- GermanQuAD -->
   <td class="de summ">57.47 ± 0.69 / 14.10 ± 0.73</td> <!-- MLSum -->
   <td class="de know">4.67 ± 0.91 / 27.88 ± 0.81</td> <!-- MMLU-de -->
   <td class="de reason">1.77 ± 1.29 / 25.47 ± 0.78</td> <!-- HellaSwag-de -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   <td>12.7.0</td> <!-- MLSum version -->
   <td>12.7.0</td> <!-- MMLU-de version -->
   <td>12.7.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="de ner">19.29 ± 5.77 / 20.20 ± 3.59</td> <!-- GermEval -->
   <td class="de sent">43.88 ± 3.42 / 61.04 ± 2.69</td> <!-- SB10k -->
   <td class="de la">5.63 ± 1.32 / 49.95 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">17.02 ± 2.10 / 36.47 ± 2.53</td> <!-- GermanQuAD -->
   <td class="de summ">54.94 ± 1.06 / 14.92 ± 1.40</td> <!-- MLSum -->
   <td class="de know">5.89 ± 0.78 / 27.89 ± 0.68</td> <!-- MMLU-de -->
   <td class="de reason">4.11 ± 0.97 / 27.05 ± 0.97</td> <!-- HellaSwag-de -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.89</td> <!-- ScandEval rank -->
   <td class="de ner">36.17 ± 2.52 / 27.29 ± 1.74</td> <!-- GermEval -->
   <td class="de sent">34.17 ± 7.08 / 46.97 ± 8.28</td> <!-- SB10k -->
   <td class="de la">2.21 ± 1.64 / 38.29 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 3.04 / 30.89 ± 4.33</td> <!-- GermanQuAD -->
   <td class="de summ">51.97 ± 2.69 / 10.46 ± 2.09</td> <!-- MLSum -->
   <td class="de know">3.68 ± 1.19 / 27.54 ± 0.71</td> <!-- MMLU-de -->
   <td class="de reason">0.64 ± 1.58 / 25.05 ± 1.13</td> <!-- HellaSwag-de -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   <td>12.9.0</td> <!-- MLSum version -->
   <td>12.9.0</td> <!-- MMLU-de version -->
   <td>12.9.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM-70b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">291 ± 23 / 163 ± 39</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="de ner">62.16 ± 2.83 / 48.46 ± 3.31</td> <!-- GermEval -->
   <td class="de sent">27.56 ± 3.62 / 47.04 ± 4.06</td> <!-- SB10k -->
   <td class="de la">0.59 ± 1.16 / 32.41 ± 0.74</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 4.44 ± 0.39</td> <!-- GermanQuAD -->
   <td class="de summ">52.77 ± 0.13 / 4.84 ± 0.05</td> <!-- MLSum -->
   <td class="de know">4.04 ± 2.64 / 22.46 ± 1.78</td> <!-- MMLU-de -->
   <td class="de reason">7.33 ± 5.87 / 28.83 ± 3.05</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.07</td> <!-- ScandEval rank -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td class="de summ">59.71 ± 2.14 / 12.23 ± 1.08</td> <!-- MLSum -->
   <td class="de know">6.34 ± 1.10 / 29.19 ± 0.75</td> <!-- MMLU-de -->
   <td class="de reason">2.94 ± 0.65 / 27.16 ± 0.61</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">56.42 ± 7.64 / 11.68 ± 1.75</td> <!-- MLSum -->
   <td class="de know">2.75 ± 0.91 / 27.17 ± 0.72</td> <!-- MMLU-de -->
   <td class="de reason">3.41 ± 1.30 / 27.45 ± 0.79</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="de ner">30.85 ± 4.69 / 24.38 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.81 / 64.87 ± 2.42</td> <!-- SB10k -->
   <td class="de la">2.67 ± 1.77 / 41.55 ± 4.54</td> <!-- ScaLA-de -->
   <td class="de rc">4.09 ± 1.94 / 12.70 ± 2.66</td> <!-- GermanQuAD -->
   <td class="de summ">42.64 ± 0.22 / 4.37 ± 0.10</td> <!-- MLSum -->
   <td class="de know">1.94 ± 0.76 / 26.86 ± 0.44</td> <!-- MMLU-de -->
   <td class="de reason">1.24 ± 0.75 / 25.78 ± 0.82</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32800</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="de ner">21.96 ± 1.53 / 18.48 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">18.66 ± 3.01 / 35.11 ± 2.93</td> <!-- SB10k -->
   <td class="de la">0.16 ± 1.78 / 37.84 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">7.08 ± 1.91 / 18.42 ± 2.90</td> <!-- GermanQuAD -->
   <td class="de summ">56.47 ± 2.05 / 11.00 ± 1.46</td> <!-- MLSum -->
   <td class="de know">1.65 ± 1.53 / 26.62 ± 0.88</td> <!-- MMLU-de -->
   <td class="de reason">0.02 ± 1.24 / 25.61 ± 0.98</td> <!-- HellaSwag-de -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   <td>13.0.0</td> <!-- MLSum version -->
   <td>13.0.0</td> <!-- MMLU-de version -->
   <td>13.0.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.40</td> <!-- ScandEval rank -->
   <td class="de ner">14.06 ± 5.31 / 12.90 ± 4.52</td> <!-- GermEval -->
   <td class="de sent">28.07 ± 6.33 / 38.61 ± 7.42</td> <!-- SB10k -->
   <td class="de la">2.31 ± 1.88 / 44.45 ± 4.23</td> <!-- ScaLA-de -->
   <td class="de rc">6.89 ± 2.35 / 17.95 ± 3.37</td> <!-- GermanQuAD -->
   <td class="de summ">43.42 ± 0.26 / 5.42 ± 0.11</td> <!-- MLSum -->
   <td class="de know">1.66 ± 1.18 / 25.51 ± 0.86</td> <!-- MMLU-de -->
   <td class="de reason">1.50 ± 0.90 / 26.46 ± 0.95</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   <td>12.5.2</td> <!-- MLSum version -->
   <td>12.5.2</td> <!-- MMLU-de version -->
   <td>12.5.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">541</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.68</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 14.17 ± 0.79</td> <!-- GermanQuAD -->
   <td class="de summ">59.26 ± 0.09 / 9.32 ± 0.09</td> <!-- MLSum -->
   <td class="de know">1.16 ± 0.57 / 22.46 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">0.31 ± 0.50 / 24.18 ± 0.53</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.70</td> <!-- ScandEval rank -->
   <td class="de ner">21.46 ± 2.04 / 20.83 ± 1.63</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de rc">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td class="de summ">39.77 ± 0.20 / 4.80 ± 0.05</td> <!-- MLSum -->
   <td class="de know">-0.08 ± 0.53 / 25.19 ± 1.04</td> <!-- MMLU-de -->
   <td class="de reason">-0.63 ± 0.73 / 24.55 ± 0.49</td> <!-- HellaSwag-de -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">5.05</td> <!-- ScandEval rank -->
   <td class="de ner">5.80 ± 1.56 / 5.41 ± 1.56</td> <!-- GermEval -->
   <td class="de sent">4.45 ± 1.73 / 29.26 ± 3.66</td> <!-- SB10k -->
   <td class="de la">-0.48 ± 1.33 / 43.09 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">0.08 ± 0.12 / 4.02 ± 1.17</td> <!-- GermanQuAD -->
   <td class="de summ">35.92 ± 0.71 / 3.53 ± 0.24</td> <!-- MLSum -->
   <td class="de know">0.77 ± 0.60 / 23.33 ± 0.60</td> <!-- MMLU-de -->
   <td class="de reason">-0.34 ± 1.16 / 24.39 ± 0.86</td> <!-- HellaSwag-de -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   <td>12.10.4</td> <!-- MLSum version -->
   <td>12.10.4</td> <!-- MMLU-de version -->
   <td>12.10.4</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.29</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.19 ± 1.24 / 17.20 ± 1.22</td> <!-- SB10k -->
   <td class="de la">-0.12 ± 0.91 / 36.65 ± 3.92</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 1.29 ± 0.49</td> <!-- GermanQuAD -->
   <td class="de summ">29.43 ± 1.80 / 2.35 ± 0.59</td> <!-- MLSum -->
   <td class="de know">-0.69 ± 0.79 / 22.79 ± 0.51</td> <!-- MMLU-de -->
   <td class="de reason">0.15 ± 0.35 / 24.25 ± 0.59</td> <!-- HellaSwag-de -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   <td>12.10.0</td> <!-- MLSum version -->
   <td>12.10.0</td> <!-- MMLU-de version -->
   <td>12.10.0</td> <!-- HellaSwag-de version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;German NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-dcwH0&quot; src=&quot;https://datawrapper.dwcdn.net/dcwH0/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
