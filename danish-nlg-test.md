---
layout: leaderboard
title: Danish NLG 🇩🇰
---

<center>Last updated: 05/12/2024 16:17:34 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="danish-nlg-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">DANSK</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Angry Tweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish reading comprehension - Exact Match / F1-score">ScandiQA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish summarization - BERTScore / ROUGE-L">Nordjylland-News</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">Danske Talemaader</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish knowledge - Matthews Correlation Coefficient / Accuracy">Danish Citizen Tests</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on DANSK">DANSK version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Angry Tweets">Angry Tweets version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-da">ScaLA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScandiQA-da">ScandiQA-da version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Nordjylland-News">Nordjylland-News version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Danske Talemaader">Danske Talemaader version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Danish Citizen Tests">Danish Citizen Tests version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-da">HellaSwag-da version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.16</td> <!-- ScandEval rank -->
   <td class="da ner">64.94 ± 1.96 / 45.76 ± 3.31</td> <!-- DANSK -->
   <td class="da sent">59.97 ± 2.65 / 73.06 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">71.56 ± 2.49 / 85.36 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">56.43 ± 2.98 / 68.46 ± 1.64</td> <!-- ScandiQA-da -->
   <td class="da summ">66.76 ± 0.34 / 18.99 ± 0.52</td> <!-- Nordjylland-News -->
   <td class="da know">94.93 ± 1.03 / 96.21 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">93.98 ± 2.15 / 95.94 ± 1.44</td> <!-- Danish Citizen Tests -->
   <td class="da reason">81.64 ± 1.80 / 86.17 ± 1.34</td> <!-- HellaSwag-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.21</td> <!-- ScandEval rank -->
   <td class="da ner">66.80 ± 3.01 / 45.69 ± 2.85</td> <!-- DANSK -->
   <td class="da sent">61.62 ± 2.17 / 73.99 ± 1.48</td> <!-- Angry Tweets -->
   <td class="da la">66.84 ± 3.27 / 82.79 ± 1.86</td> <!-- ScaLA-da -->
   <td class="da rc">56.85 ± 2.62 / 68.83 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">66.21 ± 0.44 / 18.02 ± 0.61</td> <!-- Nordjylland-News -->
   <td class="da know">95.21 ± 0.55 / 96.41 ± 0.41</td> <!-- Danske Talemaader -->
   <td class="da know">97.19 ± 1.15 / 98.12 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">78.74 ± 3.12 / 83.91 ± 2.42</td> <!-- HellaSwag-da -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.2</td> <!-- Danske Talemaader version -->
   <td>12.10.2</td> <!-- Danish Citizen Tests version -->
   <td>12.10.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.26</td> <!-- ScandEval rank -->
   <td class="da ner">71.15 ± 2.89 / 52.24 ± 3.76</td> <!-- DANSK -->
   <td class="da sent">49.42 ± 3.29 / 61.74 ± 2.59</td> <!-- Angry Tweets -->
   <td class="da la">64.59 ± 2.97 / 79.93 ± 1.88</td> <!-- ScaLA-da -->
   <td class="da rc">57.35 ± 2.51 / 67.87 ± 1.75</td> <!-- ScandiQA-da -->
   <td class="da summ">66.03 ± 0.24 / 17.74 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">96.41 ± 0.63 / 97.30 ± 0.48</td> <!-- Danske Talemaader -->
   <td class="da know">97.68 ± 1.06 / 98.44 ± 0.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">85.96 ± 1.48 / 89.41 ± 1.15</td> <!-- HellaSwag-da -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.2</td> <!-- Angry Tweets version -->
   <td>12.10.2</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.2</td> <!-- Danske Talemaader version -->
   <td>12.10.2</td> <!-- Danish Citizen Tests version -->
   <td>12.10.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>syvai/danskgpt-chat-llama3-70b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,283 ± 279 / 291 ± 92</td> <!-- Model inference speed -->
   <td class="rank">1.40</td> <!-- ScandEval rank -->
   <td class="da ner">65.40 ± 1.90 / 54.29 ± 1.61</td> <!-- DANSK -->
   <td class="da sent">62.78 ± 3.01 / 75.05 ± 1.92</td> <!-- Angry Tweets -->
   <td class="da la">57.88 ± 3.35 / 78.50 ± 3.07</td> <!-- ScaLA-da -->
   <td class="da rc">62.24 ± 2.43 / 68.23 ± 1.77</td> <!-- ScandiQA-da -->
   <td class="da summ">66.78 ± 0.52 / 20.59 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">86.20 ± 2.09 / 88.64 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">80.14 ± 3.75 / 85.73 ± 2.73</td> <!-- Danish Citizen Tests -->
   <td class="da reason">66.22 ± 2.53 / 74.34 ± 2.01</td> <!-- HellaSwag-da -->
   <td>12.10.0</td> <!-- DANSK version -->
   <td>12.10.0</td> <!-- Angry Tweets version -->
   <td>12.10.0</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.0</td> <!-- Danske Talemaader version -->
   <td>12.10.0</td> <!-- Danish Citizen Tests version -->
   <td>12.10.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.46</td> <!-- ScandEval rank -->
   <td class="da ner">59.94 ± 1.58 / 38.00 ± 1.88</td> <!-- DANSK -->
   <td class="da sent">59.06 ± 0.91 / 72.86 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">58.57 ± 2.19 / 78.63 ± 1.31</td> <!-- ScaLA-da -->
   <td class="da rc">57.48 ± 0.75 / 65.60 ± 0.65</td> <!-- ScandiQA-da -->
   <td class="da summ">68.12 ± 1.10 / 23.96 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">85.20 ± 0.83 / 88.80 ± 0.65</td> <!-- Danske Talemaader -->
   <td class="da know">84.02 ± 1.63 / 89.32 ± 1.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">71.26 ± 1.64 / 78.17 ± 1.28</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.48</td> <!-- ScandEval rank -->
   <td class="da ner">63.62 ± 3.74 / 53.29 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">60.19 ± 3.31 / 73.13 ± 2.17</td> <!-- Angry Tweets -->
   <td class="da la">50.07 ± 5.86 / 72.94 ± 4.16</td> <!-- ScaLA-da -->
   <td class="da rc">60.97 ± 2.76 / 66.71 ± 2.27</td> <!-- ScandiQA-da -->
   <td class="da summ">67.33 ± 1.41 / 22.84 ± 1.49</td> <!-- Nordjylland-News -->
   <td class="da know">83.94 ± 1.20 / 87.93 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">78.83 ± 3.17 / 85.39 ± 2.14</td> <!-- Danish Citizen Tests -->
   <td class="da reason">60.69 ± 4.11 / 69.38 ± 3.63</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4094</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.62</td> <!-- ScandEval rank -->
   <td class="da ner">61.31 ± 2.34 / 49.86 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">52.52 ± 2.05 / 68.10 ± 1.35</td> <!-- Angry Tweets -->
   <td class="da la">57.63 ± 2.80 / 77.01 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da rc">57.03 ± 1.95 / 65.51 ± 1.48</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 0.26 / 18.03 ± 0.27</td> <!-- Nordjylland-News -->
   <td class="da know">81.95 ± 2.61 / 86.33 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">77.66 ± 2.57 / 85.08 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">62.21 ± 2.60 / 71.05 ± 2.09</td> <!-- HellaSwag-da -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.68</td> <!-- ScandEval rank -->
   <td class="da ner">63.10 ± 2.12 / 55.10 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">53.09 ± 3.85 / 68.18 ± 2.27</td> <!-- Angry Tweets -->
   <td class="da la">40.98 ± 4.46 / 69.10 ± 2.72</td> <!-- ScaLA-da -->
   <td class="da rc">51.13 ± 1.89 / 63.12 ± 1.61</td> <!-- ScandiQA-da -->
   <td class="da summ">67.76 ± 0.99 / 23.19 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">85.18 ± 1.92 / 88.91 ± 1.44</td> <!-- Danske Talemaader -->
   <td class="da know">79.22 ± 2.40 / 85.70 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">70.19 ± 2.71 / 77.54 ± 2.05</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="da ner">49.05 ± 2.41 / 30.91 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">52.26 ± 1.31 / 64.13 ± 1.93</td> <!-- Angry Tweets -->
   <td class="da la">58.38 ± 1.21 / 78.98 ± 0.68</td> <!-- ScaLA-da -->
   <td class="da rc">55.34 ± 0.82 / 64.41 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="da summ">67.67 ± 1.05 / 23.18 ± 1.13</td> <!-- Nordjylland-News -->
   <td class="da know">80.62 ± 0.77 / 85.41 ± 0.58</td> <!-- Danske Talemaader -->
   <td class="da know">75.37 ± 2.23 / 83.59 ± 1.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">66.17 ± 1.45 / 74.39 ± 1.13</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-32b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">32296</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,288 ± 337 / 791 ± 252</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="da ner">61.15 ± 3.15 / 40.96 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">56.39 ± 0.85 / 69.83 ± 1.08</td> <!-- Angry Tweets -->
   <td class="da la">37.75 ± 1.59 / 67.36 ± 1.49</td> <!-- ScaLA-da -->
   <td class="da rc">58.09 ± 1.26 / 65.87 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="da summ">67.60 ± 0.98 / 23.65 ± 0.89</td> <!-- Nordjylland-News -->
   <td class="da know">66.13 ± 1.19 / 74.34 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">73.67 ± 1.81 / 82.52 ± 1.19</td> <!-- Danish Citizen Tests -->
   <td class="da reason">69.23 ± 1.33 / 76.78 ± 1.02</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="da ner">58.06 ± 2.48 / 50.10 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">53.24 ± 4.04 / 67.81 ± 2.74</td> <!-- Angry Tweets -->
   <td class="da la">39.71 ± 4.96 / 65.90 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da rc">62.51 ± 1.48 / 67.47 ± 1.39</td> <!-- ScandiQA-da -->
   <td class="da summ">67.39 ± 1.23 / 23.85 ± 1.20</td> <!-- Nordjylland-News -->
   <td class="da know">84.43 ± 1.72 / 88.28 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">71.35 ± 2.55 / 80.47 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">54.31 ± 2.56 / 65.20 ± 2.09</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32764</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.80</td> <!-- ScandEval rank -->
   <td class="da ner">56.96 ± 2.39 / 45.84 ± 1.75</td> <!-- DANSK -->
   <td class="da sent">55.11 ± 4.11 / 69.60 ± 2.69</td> <!-- Angry Tweets -->
   <td class="da la">42.64 ± 3.22 / 71.04 ± 1.56</td> <!-- ScaLA-da -->
   <td class="da rc">54.58 ± 2.19 / 64.12 ± 1.41</td> <!-- ScandiQA-da -->
   <td class="da summ">66.80 ± 1.09 / 20.36 ± 1.51</td> <!-- Nordjylland-News -->
   <td class="da know">83.94 ± 1.81 / 87.97 ± 1.38</td> <!-- Danske Talemaader -->
   <td class="da know">73.32 ± 4.97 / 81.64 ± 3.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">60.52 ± 3.33 / 70.08 ± 2.52</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="da ner">63.59 ± 2.16 / 42.42 ± 3.34</td> <!-- DANSK -->
   <td class="da sent">29.47 ± 4.78 / 50.59 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">38.37 ± 9.13 / 60.56 ± 8.53</td> <!-- ScaLA-da -->
   <td class="da rc">54.63 ± 0.51 / 65.79 ± 0.42</td> <!-- ScandiQA-da -->
   <td class="da summ">65.94 ± 0.11 / 17.32 ± 0.29</td> <!-- Nordjylland-News -->
   <td class="da know">80.46 ± 4.74 / 84.69 ± 3.92</td> <!-- Danske Talemaader -->
   <td class="da know">76.16 ± 4.99 / 83.11 ± 4.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">62.12 ± 2.52 / 70.60 ± 2.10</td> <!-- HellaSwag-da -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- Nordjylland-News version -->
   <td>12.11.0</td> <!-- Danske Talemaader version -->
   <td>12.11.0</td> <!-- Danish Citizen Tests version -->
   <td>12.11.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-chat-v2.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,085 ± 998 / 1,306 ± 404</td> <!-- Model inference speed -->
   <td class="rank">2.04</td> <!-- ScandEval rank -->
   <td class="da ner">51.08 ± 1.60 / 35.83 ± 1.84</td> <!-- DANSK -->
   <td class="da sent">54.69 ± 0.99 / 69.50 ± 0.93</td> <!-- Angry Tweets -->
   <td class="da la">30.95 ± 1.48 / 62.15 ± 1.83</td> <!-- ScaLA-da -->
   <td class="da rc">56.56 ± 0.76 / 64.32 ± 0.40</td> <!-- ScandiQA-da -->
   <td class="da summ">66.90 ± 0.23 / 20.90 ± 0.64</td> <!-- Nordjylland-News -->
   <td class="da know">79.39 ± 1.11 / 84.29 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">73.22 ± 1.83 / 81.91 ± 1.32</td> <!-- Danish Citizen Tests -->
   <td class="da reason">48.16 ± 1.14 / 60.83 ± 0.97</td> <!-- HellaSwag-da -->
   <td>12.0.0</td> <!-- DANSK version -->
   <td>12.0.0</td> <!-- Angry Tweets version -->
   <td>12.0.0</td> <!-- ScaLA-da version -->
   <td>12.0.0</td> <!-- ScandiQA-da version -->
   <td>12.0.0</td> <!-- Nordjylland-News version -->
   <td>12.0.0</td> <!-- Danske Talemaader version -->
   <td>12.0.0</td> <!-- Danish Citizen Tests version -->
   <td>12.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="da ner">44.16 ± 3.11 / 25.93 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">38.84 ± 2.31 / 45.52 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">43.42 ± 3.95 / 69.40 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">60.11 ± 0.96 / 66.24 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 1.14 / 24.10 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">81.68 ± 0.62 / 86.22 ± 0.47</td> <!-- Danske Talemaader -->
   <td class="da know">77.77 ± 1.30 / 85.06 ± 0.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">50.04 ± 3.99 / 61.09 ± 3.31</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.06</td> <!-- ScandEval rank -->
   <td class="da ner">58.03 ± 2.18 / 38.25 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">46.63 ± 2.35 / 59.02 ± 3.07</td> <!-- Angry Tweets -->
   <td class="da la">15.09 ± 3.06 / 40.04 ± 1.77</td> <!-- ScaLA-da -->
   <td class="da rc">62.15 ± 0.63 / 67.21 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">66.81 ± 1.08 / 22.82 ± 1.04</td> <!-- Nordjylland-News -->
   <td class="da know">64.79 ± 1.37 / 73.46 ± 1.07</td> <!-- Danske Talemaader -->
   <td class="da know">68.59 ± 2.23 / 78.59 ± 1.60</td> <!-- Danish Citizen Tests -->
   <td class="da reason">65.29 ± 0.94 / 73.54 ± 0.74</td> <!-- HellaSwag-da -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.5.3</td> <!-- Nordjylland-News version -->
   <td>12.5.3</td> <!-- Danske Talemaader version -->
   <td>12.5.3</td> <!-- Danish Citizen Tests version -->
   <td>12.5.3</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="da ner">53.20 ± 1.97 / 32.89 ± 2.00</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 1.18 / 67.38 ± 0.95</td> <!-- Angry Tweets -->
   <td class="da la">32.72 ± 1.79 / 62.53 ± 2.00</td> <!-- ScaLA-da -->
   <td class="da rc">56.44 ± 0.99 / 65.36 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 0.76 / 23.35 ± 0.88</td> <!-- Nordjylland-News -->
   <td class="da know">59.78 ± 1.61 / 69.68 ± 1.23</td> <!-- Danske Talemaader -->
   <td class="da know">58.63 ± 2.54 / 71.72 ± 1.82</td> <!-- Danish Citizen Tests -->
   <td class="da reason">50.74 ± 1.16 / 62.79 ± 0.92</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,493 ± 466 / 773 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="da ner">51.44 ± 3.28 / 41.38 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">54.91 ± 2.59 / 67.84 ± 2.53</td> <!-- Angry Tweets -->
   <td class="da la">22.77 ± 3.96 / 52.29 ± 3.81</td> <!-- ScaLA-da -->
   <td class="da rc">56.51 ± 1.80 / 64.01 ± 1.12</td> <!-- ScandiQA-da -->
   <td class="da summ">68.06 ± 1.42 / 24.28 ± 1.31</td> <!-- Nordjylland-News -->
   <td class="da know">74.24 ± 2.14 / 80.62 ± 1.61</td> <!-- Danske Talemaader -->
   <td class="da know">70.86 ± 3.58 / 80.31 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">41.49 ± 2.88 / 55.86 ± 2.17</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/sol (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,701 ± 876 / 771 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="da ner">54.91 ± 1.53 / 36.29 ± 1.85</td> <!-- DANSK -->
   <td class="da sent">44.38 ± 2.83 / 57.19 ± 3.61</td> <!-- Angry Tweets -->
   <td class="da la">21.11 ± 3.23 / 45.43 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">58.96 ± 1.71 / 65.85 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">66.89 ± 0.89 / 22.65 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">61.12 ± 1.49 / 70.29 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">64.86 ± 2.64 / 76.05 ± 1.94</td> <!-- Danish Citizen Tests -->
   <td class="da reason">67.96 ± 1.07 / 75.68 ± 0.86</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024001</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="da ner">53.95 ± 2.29 / 34.84 ± 2.23</td> <!-- DANSK -->
   <td class="da sent">48.97 ± 1.81 / 64.19 ± 1.99</td> <!-- Angry Tweets -->
   <td class="da la">31.78 ± 4.52 / 61.53 ± 5.44</td> <!-- ScaLA-da -->
   <td class="da rc">56.44 ± 1.24 / 65.53 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">66.24 ± 0.66 / 20.00 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">67.09 ± 1.38 / 74.85 ± 1.04</td> <!-- Danske Talemaader -->
   <td class="da know">72.87 ± 2.11 / 81.97 ± 1.42</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.77 ± 2.30 / 55.61 ± 2.33</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="da ner">52.49 ± 1.89 / 38.85 ± 1.94</td> <!-- DANSK -->
   <td class="da sent">49.67 ± 1.40 / 65.83 ± 1.40</td> <!-- Angry Tweets -->
   <td class="da la">22.80 ± 5.31 / 55.25 ± 6.92</td> <!-- ScaLA-da -->
   <td class="da rc">57.07 ± 0.68 / 64.46 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">66.75 ± 0.97 / 21.86 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">59.57 ± 1.49 / 69.19 ± 1.13</td> <!-- Danske Talemaader -->
   <td class="da know">65.34 ± 2.38 / 76.95 ± 1.56</td> <!-- Danish Citizen Tests -->
   <td class="da reason">53.97 ± 2.40 / 64.76 ± 2.17</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt-mixtral (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.22</td> <!-- ScandEval rank -->
   <td class="da ner">49.17 ± 2.72 / 34.74 ± 2.27</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 1.63 / 66.73 ± 1.63</td> <!-- Angry Tweets -->
   <td class="da la">32.04 ± 2.30 / 64.63 ± 1.42</td> <!-- ScaLA-da -->
   <td class="da rc">58.52 ± 0.97 / 66.15 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.83 ± 0.63 / 21.53 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">65.77 ± 2.06 / 74.26 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">77.56 ± 1.97 / 85.02 ± 1.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">30.34 ± 1.47 / 46.85 ± 1.17</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>utter-project/EuroLLM-9B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9152</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,763 ± 1,178 / 1,390 ± 446</td> <!-- Model inference speed -->
   <td class="rank">2.24</td> <!-- ScandEval rank -->
   <td class="da ner">34.00 ± 2.69 / 25.49 ± 2.06</td> <!-- DANSK -->
   <td class="da sent">53.97 ± 1.21 / 68.40 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">32.21 ± 4.81 / 56.97 ± 5.83</td> <!-- ScaLA-da -->
   <td class="da rc">57.10 ± 0.99 / 63.73 ± 0.85</td> <!-- ScandiQA-da -->
   <td class="da summ">67.55 ± 1.08 / 23.77 ± 0.94</td> <!-- Nordjylland-News -->
   <td class="da know">80.75 ± 1.25 / 85.31 ± 0.98</td> <!-- Danske Talemaader -->
   <td class="da know">74.77 ± 1.93 / 83.14 ± 1.29</td> <!-- Danish Citizen Tests -->
   <td class="da reason">36.86 ± 1.37 / 51.61 ± 1.09</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin2 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 459 / 767 ± 241</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="da ner">51.53 ± 2.82 / 40.66 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">47.95 ± 3.02 / 55.70 ± 3.32</td> <!-- Angry Tweets -->
   <td class="da la">14.10 ± 3.79 / 40.80 ± 3.64</td> <!-- ScaLA-da -->
   <td class="da rc">58.28 ± 1.98 / 64.33 ± 1.60</td> <!-- ScandiQA-da -->
   <td class="da summ">68.04 ± 1.34 / 24.72 ± 1.42</td> <!-- Nordjylland-News -->
   <td class="da know">67.37 ± 4.12 / 75.55 ± 3.01</td> <!-- Danske Talemaader -->
   <td class="da know">66.75 ± 3.42 / 77.34 ± 2.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.21 ± 3.40 / 56.48 ± 2.62</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da ner">52.22 ± 2.07 / 38.82 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">50.66 ± 1.88 / 62.04 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">23.57 ± 3.82 / 56.09 ± 4.62</td> <!-- ScaLA-da -->
   <td class="da rc">53.82 ± 2.13 / 61.94 ± 1.63</td> <!-- ScandiQA-da -->
   <td class="da summ">67.13 ± 0.72 / 21.62 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">69.26 ± 2.89 / 76.99 ± 2.16</td> <!-- Danske Talemaader -->
   <td class="da know">46.40 ± 2.92 / 59.45 ± 2.63</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.72 ± 2.48 / 53.83 ± 2.19</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="da ner">53.02 ± 2.85 / 41.35 ± 3.42</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 3.42 / 66.57 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">19.73 ± 4.11 / 57.07 ± 3.09</td> <!-- ScaLA-da -->
   <td class="da rc">51.69 ± 2.29 / 61.26 ± 1.32</td> <!-- ScandiQA-da -->
   <td class="da summ">67.33 ± 1.40 / 22.77 ± 1.39</td> <!-- Nordjylland-News -->
   <td class="da know">65.38 ± 2.59 / 73.95 ± 1.84</td> <!-- Danske Talemaader -->
   <td class="da know">62.78 ± 4.04 / 74.61 ± 2.90</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.07 ± 2.57 / 53.83 ± 2.06</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>RJuro/munin-neuralbeagle-SkoleGPTOpenOrca-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,008 ± 429 / 991 ± 323</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da ner">50.83 ± 2.28 / 36.96 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">43.41 ± 2.56 / 48.74 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">19.72 ± 4.69 / 52.71 ± 5.26</td> <!-- ScaLA-da -->
   <td class="da rc">57.87 ± 2.32 / 64.53 ± 1.73</td> <!-- ScandiQA-da -->
   <td class="da summ">66.77 ± 0.99 / 21.60 ± 0.91</td> <!-- Nordjylland-News -->
   <td class="da know">72.92 ± 2.52 / 79.69 ± 1.88</td> <!-- Danske Talemaader -->
   <td class="da know">68.11 ± 3.00 / 78.52 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">40.62 ± 3.23 / 55.12 ± 2.44</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/BeagleCatMunin-Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,890 ± 401 / 1,155 ± 348</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da ner">50.40 ± 2.92 / 38.57 ± 2.82</td> <!-- DANSK -->
   <td class="da sent">52.30 ± 2.65 / 64.19 ± 2.60</td> <!-- Angry Tweets -->
   <td class="da la">21.30 ± 3.52 / 47.78 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da rc">58.17 ± 1.71 / 63.79 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="da summ">66.25 ± 1.29 / 20.33 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">65.32 ± 3.33 / 73.95 ± 2.50</td> <!-- Danske Talemaader -->
   <td class="da know">64.76 ± 3.24 / 75.94 ± 2.37</td> <!-- Danish Citizen Tests -->
   <td class="da reason">33.70 ± 2.78 / 50.16 ± 2.01</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/BeagleCatMunin (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,495 ± 458 / 775 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.30</td> <!-- ScandEval rank -->
   <td class="da ner">47.62 ± 3.01 / 36.77 ± 2.96</td> <!-- DANSK -->
   <td class="da sent">54.73 ± 3.20 / 68.74 ± 2.21</td> <!-- Angry Tweets -->
   <td class="da la">21.80 ± 4.54 / 51.07 ± 4.11</td> <!-- ScaLA-da -->
   <td class="da rc">57.26 ± 1.76 / 63.60 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="da summ">67.31 ± 1.40 / 23.24 ± 1.64</td> <!-- Nordjylland-News -->
   <td class="da know">66.49 ± 2.90 / 74.84 ± 2.12</td> <!-- Danske Talemaader -->
   <td class="da know">60.41 ± 1.95 / 72.97 ± 1.45</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.51 ± 3.95 / 45.74 ± 3.03</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-slerp (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,467 ± 469 / 762 ± 244</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da ner">45.94 ± 3.62 / 35.68 ± 3.35</td> <!-- DANSK -->
   <td class="da sent">51.75 ± 4.52 / 62.28 ± 4.29</td> <!-- Angry Tweets -->
   <td class="da la">28.04 ± 3.83 / 58.31 ± 5.00</td> <!-- ScaLA-da -->
   <td class="da rc">57.65 ± 1.66 / 62.03 ± 1.50</td> <!-- ScandiQA-da -->
   <td class="da summ">66.65 ± 1.28 / 21.98 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">68.88 ± 2.98 / 76.64 ± 2.22</td> <!-- Danske Talemaader -->
   <td class="da know">64.81 ± 3.96 / 75.78 ± 2.64</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.63 ± 2.25 / 42.03 ± 2.02</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-task-arithmetic (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,500 ± 469 / 762 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.32</td> <!-- ScandEval rank -->
   <td class="da ner">46.06 ± 3.28 / 35.43 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">51.51 ± 4.23 / 61.68 ± 4.43</td> <!-- Angry Tweets -->
   <td class="da la">27.68 ± 4.25 / 57.59 ± 5.15</td> <!-- ScaLA-da -->
   <td class="da rc">57.78 ± 1.43 / 62.26 ± 1.36</td> <!-- ScandiQA-da -->
   <td class="da summ">66.62 ± 1.35 / 21.92 ± 1.28</td> <!-- Nordjylland-News -->
   <td class="da know">68.64 ± 3.34 / 76.45 ± 2.52</td> <!-- Danske Talemaader -->
   <td class="da know">66.17 ± 3.73 / 76.72 ± 2.55</td> <!-- Danish Citizen Tests -->
   <td class="da reason">23.95 ± 2.64 / 42.19 ± 2.42</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,822 ± 1,283 / 1,336 ± 430</td> <!-- Model inference speed -->
   <td class="rank">2.33</td> <!-- ScandEval rank -->
   <td class="da ner">50.80 ± 2.33 / 34.04 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">42.79 ± 2.38 / 54.47 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">23.25 ± 3.17 / 56.31 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da rc">59.90 ± 0.84 / 65.47 ± 0.43</td> <!-- ScandiQA-da -->
   <td class="da summ">67.50 ± 0.95 / 23.95 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">66.61 ± 0.93 / 74.86 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">64.80 ± 1.46 / 76.46 ± 1.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.18 ± 0.99 / 46.64 ± 0.76</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Rapid-Cycling (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,346 ± 450 / 666 ± 249</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="da ner">49.99 ± 2.62 / 38.37 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">51.25 ± 2.70 / 62.67 ± 2.82</td> <!-- Angry Tweets -->
   <td class="da la">20.66 ± 5.69 / 49.98 ± 4.94</td> <!-- ScaLA-da -->
   <td class="da rc">56.82 ± 1.75 / 62.40 ± 1.40</td> <!-- ScandiQA-da -->
   <td class="da summ">65.58 ± 1.30 / 17.82 ± 1.12</td> <!-- Nordjylland-News -->
   <td class="da know">67.48 ± 3.13 / 75.62 ± 2.33</td> <!-- Danske Talemaader -->
   <td class="da know">63.69 ± 2.43 / 75.31 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">32.11 ± 3.47 / 48.55 ± 2.67</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="da ner">47.68 ± 2.50 / 32.67 ± 2.45</td> <!-- DANSK -->
   <td class="da sent">49.71 ± 1.43 / 64.00 ± 1.96</td> <!-- Angry Tweets -->
   <td class="da la">25.48 ± 2.83 / 58.45 ± 2.63</td> <!-- ScaLA-da -->
   <td class="da rc">60.31 ± 1.24 / 65.79 ± 0.84</td> <!-- ScandiQA-da -->
   <td class="da summ">64.74 ± 0.50 / 17.82 ± 0.98</td> <!-- Nordjylland-News -->
   <td class="da know">57.60 ± 1.58 / 67.81 ± 1.23</td> <!-- Danske Talemaader -->
   <td class="da know">65.98 ± 1.72 / 77.34 ± 1.16</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.65 ± 2.52 / 45.11 ± 2.33</td> <!-- HellaSwag-da -->
   <td>12.11.0</td> <!-- DANSK version -->
   <td>12.11.0</td> <!-- Angry Tweets version -->
   <td>12.11.0</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>four-two-labs/orpo-llama-3-swe (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,974 ± 1,208 / 1,032 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da ner">46.75 ± 2.79 / 29.40 ± 2.22</td> <!-- DANSK -->
   <td class="da sent">51.73 ± 1.40 / 66.43 ± 1.93</td> <!-- Angry Tweets -->
   <td class="da la">24.73 ± 4.78 / 53.98 ± 6.10</td> <!-- ScaLA-da -->
   <td class="da rc">59.97 ± 1.27 / 65.74 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">65.21 ± 0.51 / 18.86 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">55.72 ± 2.05 / 66.59 ± 1.56</td> <!-- Danske Talemaader -->
   <td class="da know">61.59 ± 2.64 / 73.95 ± 1.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.43 ± 2.44 / 43.11 ± 2.03</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da ner">57.19 ± 1.73 / 44.34 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">51.30 ± 1.32 / 64.44 ± 1.47</td> <!-- Angry Tweets -->
   <td class="da la">10.31 ± 3.91 / 42.59 ± 5.19</td> <!-- ScaLA-da -->
   <td class="da rc">48.80 ± 1.66 / 60.46 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="da summ">67.38 ± 1.09 / 23.21 ± 0.94</td> <!-- Nordjylland-News -->
   <td class="da know">61.78 ± 1.70 / 71.28 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">66.61 ± 1.90 / 77.73 ± 1.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">39.62 ± 2.26 / 53.92 ± 1.96</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="da ner">46.31 ± 3.22 / 29.09 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">51.29 ± 1.47 / 66.35 ± 1.70</td> <!-- Angry Tweets -->
   <td class="da la">25.70 ± 4.59 / 55.65 ± 5.87</td> <!-- ScaLA-da -->
   <td class="da rc">59.79 ± 1.21 / 65.44 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">65.16 ± 0.48 / 18.74 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">56.20 ± 2.22 / 66.91 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">61.16 ± 2.54 / 73.63 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.99 ± 2.12 / 42.57 ± 1.91</td> <!-- HellaSwag-da -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">39.12 ± 4.28 / 28.74 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">36.47 ± 4.90 / 50.72 ± 6.21</td> <!-- Angry Tweets -->
   <td class="da la">26.76 ± 4.78 / 57.02 ± 5.13</td> <!-- ScaLA-da -->
   <td class="da rc">58.75 ± 1.19 / 64.41 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="da summ">67.89 ± 1.20 / 24.67 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">91.32 ± 0.66 / 93.45 ± 0.50</td> <!-- Danske Talemaader -->
   <td class="da know">79.92 ± 1.83 / 85.82 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.76 ± 3.27 / 42.17 ± 2.72</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.4.0</td> <!-- Nordjylland-News version -->
   <td>12.4.0</td> <!-- Danske Talemaader version -->
   <td>12.4.0</td> <!-- Danish Citizen Tests version -->
   <td>12.4.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">52.61 ± 1.77 / 33.64 ± 2.67</td> <!-- DANSK -->
   <td class="da sent">49.81 ± 1.43 / 66.32 ± 1.25</td> <!-- Angry Tweets -->
   <td class="da la">19.64 ± 1.63 / 54.22 ± 2.32</td> <!-- ScaLA-da -->
   <td class="da rc">48.03 ± 1.24 / 57.94 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">66.67 ± 0.87 / 21.08 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">57.65 ± 1.99 / 68.08 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">51.99 ± 3.67 / 66.43 ± 2.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">44.44 ± 1.52 / 58.16 ± 1.21</td> <!-- HellaSwag-da -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>syvai/llama3-da-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,191 ± 1,053 / 446 ± 147</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="da ner">49.97 ± 3.05 / 34.87 ± 3.11</td> <!-- DANSK -->
   <td class="da sent">48.61 ± 1.35 / 60.53 ± 2.13</td> <!-- Angry Tweets -->
   <td class="da la">28.16 ± 3.02 / 59.87 ± 3.44</td> <!-- ScaLA-da -->
   <td class="da rc">59.55 ± 1.23 / 65.50 ± 0.77</td> <!-- ScandiQA-da -->
   <td class="da summ">66.16 ± 0.83 / 20.83 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">54.55 ± 2.11 / 65.21 ± 1.63</td> <!-- Danske Talemaader -->
   <td class="da know">62.19 ± 2.34 / 74.20 ± 1.57</td> <!-- Danish Citizen Tests -->
   <td class="da reason">20.36 ± 2.18 / 38.27 ± 2.03</td> <!-- HellaSwag-da -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- Nordjylland-News version -->
   <td>12.9.0</td> <!-- Danske Talemaader version -->
   <td>12.9.0</td> <!-- Danish Citizen Tests version -->
   <td>12.9.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>timpal0l/dolphin-2.9-llama3-8b-flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,018 ± 1,216 / 996 ± 324</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="da ner">51.37 ± 2.38 / 37.56 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">52.17 ± 3.44 / 67.14 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">27.98 ± 7.51 / 60.57 ± 5.72</td> <!-- ScaLA-da -->
   <td class="da rc">51.65 ± 0.84 / 59.94 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">66.25 ± 1.15 / 19.93 ± 1.18</td> <!-- Nordjylland-News -->
   <td class="da know">57.31 ± 2.81 / 68.05 ± 2.05</td> <!-- Danske Talemaader -->
   <td class="da know">54.17 ± 2.95 / 68.20 ± 1.83</td> <!-- Danish Citizen Tests -->
   <td class="da reason">27.65 ± 3.28 / 44.53 ± 2.63</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="da ner">57.74 ± 2.06 / 40.66 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">48.43 ± 3.31 / 62.09 ± 3.62</td> <!-- Angry Tweets -->
   <td class="da la">27.12 ± 2.83 / 60.40 ± 2.70</td> <!-- ScaLA-da -->
   <td class="da rc">46.76 ± 1.20 / 59.77 ± 0.51</td> <!-- ScandiQA-da -->
   <td class="da summ">66.36 ± 0.47 / 19.75 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">57.87 ± 1.67 / 67.43 ± 1.34</td> <!-- Danske Talemaader -->
   <td class="da know">50.42 ± 3.32 / 65.43 ± 2.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.17 ± 2.24 / 44.59 ± 2.00</td> <!-- HellaSwag-da -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-expanse-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,581 ± 1,066 / 1,471 ± 483</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da ner">51.32 ± 3.82 / 25.54 ± 2.10</td> <!-- DANSK -->
   <td class="da sent">52.00 ± 1.67 / 66.25 ± 1.77</td> <!-- Angry Tweets -->
   <td class="da la">18.48 ± 2.44 / 52.18 ± 4.28</td> <!-- ScaLA-da -->
   <td class="da rc">52.43 ± 1.19 / 62.08 ± 0.60</td> <!-- ScandiQA-da -->
   <td class="da summ">66.18 ± 0.84 / 21.10 ± 0.69</td> <!-- Nordjylland-News -->
   <td class="da know">41.32 ± 1.11 / 55.43 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">52.24 ± 1.55 / 68.01 ± 1.05</td> <!-- Danish Citizen Tests -->
   <td class="da reason">37.67 ± 0.80 / 53.26 ± 0.60</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ThatsGroes/munin-SkoleGPTOpenOrca-7b-16bit (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,006 ± 479 / 1,053 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="da ner">45.37 ± 2.53 / 28.99 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">39.63 ± 1.90 / 46.93 ± 2.68</td> <!-- Angry Tweets -->
   <td class="da la">21.77 ± 3.54 / 47.96 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da rc">58.28 ± 0.73 / 64.76 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">67.91 ± 0.79 / 24.44 ± 0.46</td> <!-- Nordjylland-News -->
   <td class="da know">78.71 ± 1.22 / 83.82 ± 0.94</td> <!-- Danske Talemaader -->
   <td class="da know">63.74 ± 2.06 / 74.88 ± 1.46</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.58 ± 0.96 / 45.97 ± 0.76</td> <!-- HellaSwag-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Munin-NeuralBeagle-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,903 ± 407 / 1,157 ± 350</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da rc">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="da summ">67.69 ± 1.19 / 23.90 ± 1.25</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/WestLake-Munin-Cat-NorskGPT (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 391 / 1,142 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da ner">51.85 ± 3.08 / 40.02 ± 2.48</td> <!-- DANSK -->
   <td class="da sent">44.02 ± 2.44 / 47.74 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 4.99 / 34.29 ± 1.62</td> <!-- ScaLA-da -->
   <td class="da rc">57.69 ± 2.29 / 64.09 ± 1.68</td> <!-- ScandiQA-da -->
   <td class="da summ">67.69 ± 1.19 / 23.88 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">68.45 ± 3.11 / 76.37 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">65.51 ± 3.45 / 76.56 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">42.09 ± 3.27 / 56.33 ± 2.56</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/njord-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,431 ± 1,267 / 1,139 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="da ner">38.25 ± 3.75 / 28.14 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">39.37 ± 2.09 / 56.57 ± 1.90</td> <!-- Angry Tweets -->
   <td class="da la">29.76 ± 3.24 / 61.80 ± 2.22</td> <!-- ScaLA-da -->
   <td class="da rc">57.02 ± 1.28 / 63.16 ± 0.90</td> <!-- ScandiQA-da -->
   <td class="da summ">67.57 ± 1.27 / 24.15 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">83.45 ± 1.44 / 87.17 ± 1.20</td> <!-- Danske Talemaader -->
   <td class="da know">70.43 ± 2.76 / 79.43 ± 1.95</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.43 ± 1.75 / 33.75 ± 1.91</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,141 ± 994 / 905 ± 299</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da ner">36.72 ± 3.33 / 27.73 ± 2.57</td> <!-- DANSK -->
   <td class="da sent">46.48 ± 1.17 / 55.20 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">26.10 ± 3.17 / 59.19 ± 3.94</td> <!-- ScaLA-da -->
   <td class="da rc">58.00 ± 0.91 / 64.11 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">67.23 ± 1.11 / 23.15 ± 1.07</td> <!-- Nordjylland-News -->
   <td class="da know">82.84 ± 0.94 / 87.01 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">75.27 ± 1.67 / 83.44 ± 1.19</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.55 ± 2.72 / 33.99 ± 2.19</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="da ner">52.72 ± 2.21 / 39.49 ± 3.47</td> <!-- DANSK -->
   <td class="da sent">49.11 ± 3.91 / 64.78 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">16.09 ± 3.74 / 54.94 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da rc">46.28 ± 1.53 / 56.13 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">66.62 ± 0.96 / 21.03 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">60.03 ± 5.14 / 70.04 ± 3.73</td> <!-- Danske Talemaader -->
   <td class="da know">59.83 ± 4.38 / 72.27 ± 3.40</td> <!-- Danish Citizen Tests -->
   <td class="da reason">40.40 ± 3.24 / 55.04 ± 2.57</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/Flashback-Bellman (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,887 ± 403 / 1,144 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da ner">47.71 ± 3.50 / 35.65 ± 3.07</td> <!-- DANSK -->
   <td class="da sent">48.21 ± 3.58 / 60.08 ± 3.41</td> <!-- Angry Tweets -->
   <td class="da la">19.55 ± 5.35 / 50.98 ± 5.74</td> <!-- ScaLA-da -->
   <td class="da rc">56.46 ± 1.48 / 61.69 ± 1.28</td> <!-- ScandiQA-da -->
   <td class="da summ">65.46 ± 1.23 / 17.73 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">61.29 ± 2.33 / 70.82 ± 1.78</td> <!-- Danske Talemaader -->
   <td class="da know">60.29 ± 2.58 / 72.97 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.33 ± 2.11 / 45.86 ± 1.72</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>birgermoell/NeuralBeagle-Flashback (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,904 ± 405 / 1,155 ± 349</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da ner">48.28 ± 2.73 / 36.42 ± 3.04</td> <!-- DANSK -->
   <td class="da sent">44.20 ± 2.63 / 53.54 ± 3.36</td> <!-- Angry Tweets -->
   <td class="da la">22.79 ± 5.54 / 54.63 ± 6.09</td> <!-- ScaLA-da -->
   <td class="da rc">57.96 ± 0.80 / 63.50 ± 0.73</td> <!-- ScandiQA-da -->
   <td class="da summ">65.62 ± 1.30 / 17.98 ± 1.11</td> <!-- Nordjylland-News -->
   <td class="da know">62.80 ± 2.47 / 72.15 ± 1.80</td> <!-- Danske Talemaader -->
   <td class="da know">61.54 ± 2.29 / 73.98 ± 1.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.54 ± 2.80 / 43.01 ± 1.95</td> <!-- HellaSwag-da -->
   <td>9.3.0</td> <!-- DANSK version -->
   <td>9.3.0</td> <!-- Angry Tweets version -->
   <td>9.3.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-alpha (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,116 ± 1,049 / 1,784 ± 577</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="da ner">40.60 ± 2.25 / 28.71 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">36.89 ± 2.27 / 43.77 ± 2.64</td> <!-- Angry Tweets -->
   <td class="da la">26.41 ± 5.40 / 53.03 ± 6.56</td> <!-- ScaLA-da -->
   <td class="da rc">57.81 ± 1.11 / 63.44 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">67.27 ± 1.15 / 23.82 ± 0.97</td> <!-- Nordjylland-News -->
   <td class="da know">77.63 ± 1.33 / 83.01 ± 1.00</td> <!-- Danske Talemaader -->
   <td class="da know">67.83 ± 1.25 / 77.91 ± 0.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.16 ± 2.44 / 42.68 ± 2.10</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.4.0</td> <!-- Angry Tweets version -->
   <td>12.4.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.4.0</td> <!-- Danske Talemaader version -->
   <td>12.4.0</td> <!-- Danish Citizen Tests version -->
   <td>12.4.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>KennethEnevoldsen/munin_mistral-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,543 ± 466 / 787 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="da ner">46.70 ± 3.49 / 36.30 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">47.52 ± 3.90 / 55.98 ± 4.69</td> <!-- Angry Tweets -->
   <td class="da la">8.04 ± 5.32 / 36.02 ± 2.59</td> <!-- ScaLA-da -->
   <td class="da rc">60.05 ± 1.30 / 64.15 ± 1.20</td> <!-- ScandiQA-da -->
   <td class="da summ">67.18 ± 1.23 / 22.71 ± 1.10</td> <!-- Nordjylland-News -->
   <td class="da know">70.49 ± 3.13 / 77.89 ± 2.32</td> <!-- Danske Talemaader -->
   <td class="da know">66.28 ± 4.60 / 76.88 ± 3.34</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.13 ± 3.45 / 43.24 ± 2.58</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.1</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.9 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 458 / 750 ± 240</td> <!-- Model inference speed -->
   <td class="rank">2.49</td> <!-- ScandEval rank -->
   <td class="da ner">45.61 ± 3.06 / 35.04 ± 2.94</td> <!-- DANSK -->
   <td class="da sent">53.73 ± 3.06 / 67.51 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">17.08 ± 5.36 / 52.62 ± 5.62</td> <!-- ScaLA-da -->
   <td class="da rc">56.67 ± 1.19 / 61.18 ± 1.07</td> <!-- ScandiQA-da -->
   <td class="da summ">66.14 ± 1.40 / 20.98 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">60.58 ± 2.62 / 69.80 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">57.89 ± 3.66 / 70.00 ± 2.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.45 ± 1.87 / 35.47 ± 1.77</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>AI-Sweden-Models/tyr (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,079 ± 1,051 / 1,760 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="da ner">47.01 ± 2.76 / 36.47 ± 3.27</td> <!-- DANSK -->
   <td class="da sent">50.60 ± 3.33 / 65.49 ± 2.38</td> <!-- Angry Tweets -->
   <td class="da la">13.73 ± 3.33 / 52.15 ± 3.17</td> <!-- ScaLA-da -->
   <td class="da rc">56.35 ± 1.68 / 61.63 ± 1.33</td> <!-- ScandiQA-da -->
   <td class="da summ">66.82 ± 1.02 / 22.26 ± 1.10</td> <!-- Nordjylland-News -->
   <td class="da know">57.53 ± 3.61 / 67.77 ± 2.64</td> <!-- Danske Talemaader -->
   <td class="da know">67.04 ± 2.33 / 78.12 ± 1.58</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.16 ± 1.56 / 40.90 ± 1.34</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.3.2</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama3-8b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,695 ± 1,277 / 532 ± 183</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="da ner">51.40 ± 3.08 / 37.70 ± 3.28</td> <!-- DANSK -->
   <td class="da sent">42.13 ± 0.57 / 45.91 ± 0.39</td> <!-- Angry Tweets -->
   <td class="da la">3.91 ± 2.02 / 34.38 ± 0.47</td> <!-- ScaLA-da -->
   <td class="da rc">57.81 ± 1.03 / 66.28 ± 0.48</td> <!-- ScandiQA-da -->
   <td class="da summ">66.70 ± 0.98 / 21.56 ± 0.85</td> <!-- Nordjylland-News -->
   <td class="da know">65.15 ± 1.40 / 73.55 ± 1.05</td> <!-- Danske Talemaader -->
   <td class="da know">57.36 ± 2.49 / 70.88 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">44.55 ± 1.98 / 57.29 ± 1.77</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.52</td> <!-- ScandEval rank -->
   <td class="da ner">19.59 ± 2.54 / 15.47 ± 2.19</td> <!-- DANSK -->
   <td class="da sent">46.55 ± 1.89 / 59.52 ± 3.56</td> <!-- Angry Tweets -->
   <td class="da la">32.64 ± 2.91 / 63.84 ± 1.69</td> <!-- ScaLA-da -->
   <td class="da rc">59.40 ± 1.02 / 64.81 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">66.63 ± 0.82 / 22.82 ± 0.62</td> <!-- Nordjylland-News -->
   <td class="da know">74.32 ± 0.96 / 80.31 ± 0.79</td> <!-- Danske Talemaader -->
   <td class="da know">65.58 ± 2.10 / 76.41 ± 1.54</td> <!-- Danish Citizen Tests -->
   <td class="da reason">24.74 ± 2.86 / 39.03 ± 1.70</td> <!-- HellaSwag-da -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- Nordjylland-News version -->
   <td>12.9.1</td> <!-- Danske Talemaader version -->
   <td>12.9.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Llama-3-8B-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">967 ± 125 / 402 ± 116</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="da ner">41.74 ± 3.18 / 30.54 ± 2.87</td> <!-- DANSK -->
   <td class="da sent">50.07 ± 1.52 / 60.95 ± 2.42</td> <!-- Angry Tweets -->
   <td class="da la">24.49 ± 1.98 / 57.72 ± 2.71</td> <!-- ScaLA-da -->
   <td class="da rc">59.29 ± 0.86 / 65.18 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="da summ">66.24 ± 0.55 / 20.03 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">55.51 ± 1.94 / 65.80 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">48.43 ± 2.35 / 64.28 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">19.64 ± 2.14 / 37.09 ± 1.65</td> <!-- HellaSwag-da -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- Nordjylland-News version -->
   <td>12.9.1</td> <!-- Danske Talemaader version -->
   <td>12.9.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="da ner">44.58 ± 2.62 / 33.50 ± 2.75</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.36 / 64.63 ± 1.18</td> <!-- Angry Tweets -->
   <td class="da la">19.20 ± 2.44 / 53.44 ± 4.36</td> <!-- ScaLA-da -->
   <td class="da rc">58.41 ± 1.36 / 63.32 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="da summ">65.64 ± 0.99 / 21.12 ± 0.86</td> <!-- Nordjylland-News -->
   <td class="da know">32.05 ± 2.18 / 47.54 ± 1.78</td> <!-- Danske Talemaader -->
   <td class="da know">47.42 ± 1.74 / 65.02 ± 1.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.73 ± 1.32 / 46.04 ± 1.04</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Mabeck/Heidrun-Mistral-7B-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,823 ± 967 / 860 ± 280</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da ner">40.14 ± 2.41 / 28.08 ± 1.67</td> <!-- DANSK -->
   <td class="da sent">39.38 ± 1.56 / 49.16 ± 2.84</td> <!-- Angry Tweets -->
   <td class="da la">21.85 ± 3.24 / 53.75 ± 4.63</td> <!-- ScaLA-da -->
   <td class="da rc">58.07 ± 1.13 / 63.63 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">67.06 ± 1.05 / 23.60 ± 0.84</td> <!-- Nordjylland-News -->
   <td class="da know">60.78 ± 1.64 / 69.96 ± 1.28</td> <!-- Danske Talemaader -->
   <td class="da know">61.29 ± 2.78 / 73.50 ± 1.95</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.26 ± 1.96 / 35.70 ± 1.73</td> <!-- HellaSwag-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Mistral-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,443 ± 451 / 761 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da ner">50.76 ± 1.60 / 32.89 ± 2.11</td> <!-- DANSK -->
   <td class="da sent">40.41 ± 0.79 / 44.17 ± 0.56</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">57.26 ± 0.79 / 63.80 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="da summ">66.89 ± 0.71 / 21.43 ± 0.57</td> <!-- Nordjylland-News -->
   <td class="da know">64.32 ± 1.99 / 73.00 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">53.18 ± 2.37 / 67.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">43.42 ± 1.05 / 57.50 ± 0.80</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="da ner">43.60 ± 2.94 / 32.17 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.92 ± 1.50 / 61.91 ± 1.50</td> <!-- Angry Tweets -->
   <td class="da la">15.43 ± 3.79 / 46.20 ± 5.54</td> <!-- ScaLA-da -->
   <td class="da rc">59.13 ± 0.86 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.33 ± 0.98 / 22.03 ± 0.96</td> <!-- Nordjylland-News -->
   <td class="da know">53.81 ± 1.88 / 64.81 ± 1.53</td> <!-- Danske Talemaader -->
   <td class="da know">61.06 ± 2.83 / 73.89 ± 2.00</td> <!-- Danish Citizen Tests -->
   <td class="da reason">20.64 ± 1.95 / 39.21 ± 1.79</td> <!-- HellaSwag-da -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-ties (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,457 ± 451 / 757 ± 237</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="da ner">45.39 ± 2.46 / 34.45 ± 2.56</td> <!-- DANSK -->
   <td class="da sent">51.95 ± 2.65 / 65.69 ± 2.11</td> <!-- Angry Tweets -->
   <td class="da la">13.25 ± 6.27 / 45.66 ± 5.58</td> <!-- ScaLA-da -->
   <td class="da rc">58.51 ± 1.35 / 62.73 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="da summ">66.33 ± 1.33 / 21.24 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">57.16 ± 3.03 / 66.99 ± 2.44</td> <!-- Danske Talemaader -->
   <td class="da know">60.06 ± 3.26 / 71.17 ± 2.36</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.62 ± 3.14 / 33.40 ± 2.67</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="da ner">43.65 ± 2.87 / 32.21 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">45.86 ± 1.63 / 61.89 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">15.19 ± 3.67 / 46.19 ± 5.60</td> <!-- ScaLA-da -->
   <td class="da rc">59.14 ± 0.90 / 64.43 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.30 ± 1.02 / 21.99 ± 1.01</td> <!-- Nordjylland-News -->
   <td class="da know">53.67 ± 1.74 / 64.67 ± 1.45</td> <!-- Danske Talemaader -->
   <td class="da know">54.52 ± 2.51 / 68.59 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">20.51 ± 2.03 / 39.10 ± 1.86</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.1</td> <!-- Angry Tweets version -->
   <td>12.5.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.1</td> <!-- Danske Talemaader version -->
   <td>12.5.1</td> <!-- Danish Citizen Tests version -->
   <td>12.5.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NLPnorth/snakmodel-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,028 ± 534 / 941 ± 289</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="da ner">35.82 ± 4.16 / 29.62 ± 3.38</td> <!-- DANSK -->
   <td class="da sent">50.46 ± 1.30 / 64.72 ± 2.20</td> <!-- Angry Tweets -->
   <td class="da la">18.60 ± 3.80 / 52.87 ± 6.20</td> <!-- ScaLA-da -->
   <td class="da rc">58.57 ± 0.74 / 64.68 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.71 ± 0.63 / 21.52 ± 0.74</td> <!-- Nordjylland-News -->
   <td class="da know">64.57 ± 3.20 / 71.20 ± 3.20</td> <!-- Danske Talemaader -->
   <td class="da know">57.45 ± 2.47 / 71.64 ± 1.61</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.33 ± 1.03 / 29.66 ± 0.99</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.2.0</td> <!-- Angry Tweets version -->
   <td>13.2.0</td> <!-- ScaLA-da version -->
   <td>13.2.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.6 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,515 ± 465 / 785 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="da ner">46.03 ± 3.93 / 34.23 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">49.59 ± 3.26 / 63.45 ± 2.61</td> <!-- Angry Tweets -->
   <td class="da la">12.72 ± 3.51 / 46.56 ± 5.33</td> <!-- ScaLA-da -->
   <td class="da rc">57.03 ± 1.13 / 61.58 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="da summ">65.24 ± 1.45 / 19.37 ± 1.48</td> <!-- Nordjylland-News -->
   <td class="da know">59.88 ± 2.64 / 69.41 ± 2.10</td> <!-- Danske Talemaader -->
   <td class="da know">59.51 ± 3.33 / 71.02 ± 2.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.86 ± 4.05 / 34.77 ± 3.07</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="da ner">44.89 ± 2.46 / 29.13 ± 1.92</td> <!-- DANSK -->
   <td class="da sent">48.09 ± 1.00 / 65.40 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">19.06 ± 2.34 / 58.77 ± 1.37</td> <!-- ScaLA-da -->
   <td class="da rc">51.56 ± 1.16 / 60.81 ± 0.74</td> <!-- ScandiQA-da -->
   <td class="da summ">66.84 ± 0.77 / 21.21 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">51.60 ± 1.33 / 63.50 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.85 ± 2.68 / 52.62 ± 2.08</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.21 ± 1.60 / 40.78 ± 1.32</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="da ner">44.00 ± 2.63 / 29.00 ± 2.26</td> <!-- DANSK -->
   <td class="da sent">45.41 ± 1.79 / 62.27 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">16.17 ± 2.17 / 56.93 ± 1.29</td> <!-- ScaLA-da -->
   <td class="da rc">57.06 ± 0.83 / 63.94 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">66.88 ± 0.98 / 21.84 ± 1.04</td> <!-- Nordjylland-News -->
   <td class="da know">45.21 ± 1.90 / 57.54 ± 1.55</td> <!-- Danske Talemaader -->
   <td class="da know">51.06 ± 2.13 / 67.44 ± 1.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.50 ± 1.48 / 36.77 ± 1.21</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.11.0</td> <!-- ScandiQA-da version -->
   <td>12.11.0</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.68</td> <!-- ScandEval rank -->
   <td class="da ner">45.42 ± 2.88 / 32.66 ± 2.49</td> <!-- DANSK -->
   <td class="da sent">43.16 ± 1.69 / 54.53 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">8.79 ± 3.23 / 38.38 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da rc">59.43 ± 1.04 / 64.55 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="da summ">66.47 ± 1.00 / 22.11 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">53.26 ± 1.94 / 64.50 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">58.26 ± 2.62 / 71.56 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.53 ± 2.03 / 37.79 ± 1.68</td> <!-- HellaSwag-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da ner">43.17 ± 2.78 / 31.37 ± 2.95</td> <!-- DANSK -->
   <td class="da sent">43.40 ± 2.20 / 57.24 ± 3.52</td> <!-- Angry Tweets -->
   <td class="da la">11.08 ± 2.98 / 43.40 ± 4.66</td> <!-- ScaLA-da -->
   <td class="da rc">56.81 ± 0.70 / 63.10 ± 0.35</td> <!-- ScandiQA-da -->
   <td class="da summ">67.46 ± 0.28 / 22.85 ± 0.60</td> <!-- Nordjylland-News -->
   <td class="da know">52.94 ± 1.40 / 64.04 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">41.65 ± 1.43 / 59.92 ± 0.88</td> <!-- Danish Citizen Tests -->
   <td class="da reason">17.57 ± 1.83 / 37.68 ± 1.55</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.69</td> <!-- ScandEval rank -->
   <td class="da ner">42.43 ± 3.36 / 29.30 ± 2.53</td> <!-- DANSK -->
   <td class="da sent">47.82 ± 2.00 / 63.19 ± 2.09</td> <!-- Angry Tweets -->
   <td class="da la">16.51 ± 2.59 / 52.73 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">56.95 ± 1.21 / 62.20 ± 0.83</td> <!-- ScandiQA-da -->
   <td class="da summ">65.43 ± 1.12 / 20.36 ± 0.95</td> <!-- Nordjylland-News -->
   <td class="da know">50.76 ± 1.75 / 62.66 ± 1.43</td> <!-- Danske Talemaader -->
   <td class="da know">50.82 ± 1.17 / 66.66 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.47 ± 2.35 / 34.86 ± 1.97</td> <!-- HellaSwag-da -->
   <td>12.5.3</td> <!-- DANSK version -->
   <td>12.5.3</td> <!-- Angry Tweets version -->
   <td>12.5.3</td> <!-- ScaLA-da version -->
   <td>12.5.3</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.5.3</td> <!-- Danske Talemaader version -->
   <td>12.5.3</td> <!-- Danish Citizen Tests version -->
   <td>12.5.3</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da ner">47.08 ± 3.39 / 32.34 ± 2.97</td> <!-- DANSK -->
   <td class="da sent">47.16 ± 1.21 / 63.47 ± 1.57</td> <!-- Angry Tweets -->
   <td class="da la">8.41 ± 2.40 / 37.31 ± 1.66</td> <!-- ScaLA-da -->
   <td class="da rc">58.83 ± 0.73 / 63.96 ± 0.56</td> <!-- ScandiQA-da -->
   <td class="da summ">65.03 ± 0.98 / 20.21 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">36.64 ± 1.30 / 49.92 ± 1.19</td> <!-- Danske Talemaader -->
   <td class="da know">39.24 ± 1.63 / 59.45 ± 1.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">27.29 ± 1.22 / 45.01 ± 0.99</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/hestenettetLM (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,160 ± 804 / 1,654 ± 516</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="da ner">44.90 ± 3.15 / 31.91 ± 2.65</td> <!-- DANSK -->
   <td class="da sent">42.61 ± 1.79 / 53.47 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 3.44 / 38.18 ± 4.21</td> <!-- ScaLA-da -->
   <td class="da rc">59.62 ± 1.12 / 64.70 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">66.48 ± 0.99 / 22.13 ± 1.09</td> <!-- Nordjylland-News -->
   <td class="da know">52.83 ± 1.98 / 64.27 ± 1.66</td> <!-- Danske Talemaader -->
   <td class="da know">57.96 ± 2.76 / 71.31 ± 1.89</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.11 ± 3.15 / 37.65 ± 2.44</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="da ner">28.22 ± 1.66 / 19.95 ± 1.55</td> <!-- DANSK -->
   <td class="da sent">47.11 ± 1.36 / 63.36 ± 1.39</td> <!-- Angry Tweets -->
   <td class="da la">19.99 ± 1.86 / 58.86 ± 1.11</td> <!-- ScaLA-da -->
   <td class="da rc">48.00 ± 0.98 / 58.49 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">66.73 ± 1.01 / 21.91 ± 1.06</td> <!-- Nordjylland-News -->
   <td class="da know">52.85 ± 1.36 / 63.72 ± 1.12</td> <!-- Danske Talemaader -->
   <td class="da know">52.74 ± 1.77 / 68.55 ± 1.20</td> <!-- Danish Citizen Tests -->
   <td class="da reason">29.94 ± 1.28 / 47.03 ± 1.01</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-13B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,856 ± 645 / 709 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da ner">44.17 ± 3.14 / 31.63 ± 3.03</td> <!-- DANSK -->
   <td class="da sent">44.28 ± 1.94 / 55.59 ± 3.06</td> <!-- Angry Tweets -->
   <td class="da la">3.11 ± 1.88 / 34.35 ± 0.74</td> <!-- ScaLA-da -->
   <td class="da rc">55.59 ± 0.65 / 63.25 ± 0.37</td> <!-- ScandiQA-da -->
   <td class="da summ">66.63 ± 0.92 / 21.44 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">59.51 ± 1.28 / 69.11 ± 1.02</td> <!-- Danske Talemaader -->
   <td class="da know">50.89 ± 1.72 / 67.29 ± 1.12</td> <!-- Danish Citizen Tests -->
   <td class="da reason">25.32 ± 1.41 / 43.22 ± 1.13</td> <!-- HellaSwag-da -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Llama-3-8B-flashback-v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,807 ± 1,152 / 979 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="da ner">46.59 ± 4.16 / 31.16 ± 3.95</td> <!-- DANSK -->
   <td class="da sent">50.25 ± 1.25 / 66.18 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">14.46 ± 2.48 / 50.96 ± 4.22</td> <!-- ScaLA-da -->
   <td class="da rc">56.86 ± 1.23 / 62.50 ± 0.92</td> <!-- ScandiQA-da -->
   <td class="da summ">61.98 ± 1.03 / 15.41 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">46.91 ± 1.59 / 59.57 ± 1.13</td> <!-- Danske Talemaader -->
   <td class="da know">50.98 ± 1.94 / 66.25 ± 1.43</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.33 ± 2.72 / 35.98 ± 2.43</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>neph1/bellman-7b-mistral-instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,518 ± 463 / 779 ± 243</td> <!-- Model inference speed -->
   <td class="rank">2.74</td> <!-- ScandEval rank -->
   <td class="da ner">46.11 ± 3.27 / 28.75 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">47.58 ± 1.41 / 63.81 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">18.41 ± 2.11 / 57.44 ± 2.11</td> <!-- ScaLA-da -->
   <td class="da rc">52.78 ± 1.15 / 60.80 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="da summ">65.65 ± 0.82 / 18.78 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">41.77 ± 1.71 / 55.65 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">35.86 ± 2.28 / 52.48 ± 1.70</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.59 ± 1.75 / 32.81 ± 1.55</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="da ner">44.92 ± 3.05 / 32.65 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">49.31 ± 1.35 / 66.02 ± 1.10</td> <!-- Angry Tweets -->
   <td class="da la">10.14 ± 2.87 / 44.99 ± 4.82</td> <!-- ScaLA-da -->
   <td class="da rc">57.34 ± 0.99 / 63.24 ± 0.44</td> <!-- ScandiQA-da -->
   <td class="da summ">66.02 ± 0.75 / 20.91 ± 0.70</td> <!-- Nordjylland-News -->
   <td class="da know">33.71 ± 1.69 / 49.70 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">43.55 ± 3.67 / 62.50 ± 2.36</td> <!-- Danish Citizen Tests -->
   <td class="da reason">21.34 ± 1.27 / 39.77 ± 1.09</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.82</td> <!-- ScandEval rank -->
   <td class="da ner">41.28 ± 3.92 / 31.98 ± 3.26</td> <!-- DANSK -->
   <td class="da sent">23.01 ± 3.87 / 36.55 ± 6.42</td> <!-- Angry Tweets -->
   <td class="da la">23.50 ± 2.75 / 58.11 ± 3.45</td> <!-- ScaLA-da -->
   <td class="da rc">60.29 ± 0.81 / 65.52 ± 0.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.28 ± 1.20 / 21.69 ± 1.21</td> <!-- Nordjylland-News -->
   <td class="da know">50.30 ± 2.37 / 61.85 ± 1.93</td> <!-- Danske Talemaader -->
   <td class="da know">56.24 ± 2.29 / 70.27 ± 1.64</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.43 ± 0.95 / 35.31 ± 0.71</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">2.83</td> <!-- ScandEval rank -->
   <td class="da ner">41.12 ± 3.39 / 32.50 ± 2.74</td> <!-- DANSK -->
   <td class="da sent">42.77 ± 2.76 / 54.70 ± 4.19</td> <!-- Angry Tweets -->
   <td class="da la">11.52 ± 3.01 / 49.37 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">51.14 ± 1.03 / 60.18 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">65.19 ± 0.78 / 18.34 ± 1.22</td> <!-- Nordjylland-News -->
   <td class="da know">49.78 ± 1.52 / 62.29 ± 1.14</td> <!-- Danske Talemaader -->
   <td class="da know">45.88 ± 2.43 / 63.96 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">21.89 ± 1.77 / 41.16 ± 1.43</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>bineric/NorskGPT-Llama-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,384 ± 879 / 1,746 ± 553</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da ner">41.63 ± 2.33 / 28.51 ± 2.43</td> <!-- DANSK -->
   <td class="da sent">47.73 ± 1.52 / 60.64 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.41 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">54.25 ± 0.85 / 61.70 ± 0.71</td> <!-- ScandiQA-da -->
   <td class="da summ">66.02 ± 0.52 / 19.78 ± 0.57</td> <!-- Nordjylland-News -->
   <td class="da know">47.16 ± 1.82 / 59.60 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">38.28 ± 1.21 / 58.13 ± 0.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">22.27 ± 1.19 / 41.07 ± 1.07</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da ner">37.93 ± 2.71 / 23.54 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">44.49 ± 2.56 / 60.64 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">14.09 ± 2.94 / 42.43 ± 3.30</td> <!-- ScaLA-da -->
   <td class="da rc">51.38 ± 2.31 / 58.78 ± 1.27</td> <!-- ScandiQA-da -->
   <td class="da summ">65.80 ± 0.93 / 19.91 ± 1.41</td> <!-- Nordjylland-News -->
   <td class="da know">45.07 ± 1.34 / 58.18 ± 1.03</td> <!-- Danske Talemaader -->
   <td class="da know">35.36 ± 2.19 / 55.82 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">14.85 ± 1.19 / 35.26 ± 1.24</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.89</td> <!-- ScandEval rank -->
   <td class="da ner">40.19 ± 2.55 / 29.73 ± 1.44</td> <!-- DANSK -->
   <td class="da sent">42.31 ± 1.55 / 59.29 ± 2.00</td> <!-- Angry Tweets -->
   <td class="da la">1.14 ± 1.22 / 33.83 ± 0.72</td> <!-- ScaLA-da -->
   <td class="da rc">57.89 ± 1.16 / 63.95 ± 0.82</td> <!-- ScandiQA-da -->
   <td class="da summ">66.68 ± 0.81 / 22.38 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">44.30 ± 2.46 / 57.00 ± 2.30</td> <!-- Danske Talemaader -->
   <td class="da know">48.76 ± 2.39 / 65.51 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.44 ± 1.66 / 35.82 ± 1.14</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.2.0</td> <!-- Angry Tweets version -->
   <td>12.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.1</td> <!-- Danske Talemaader version -->
   <td>12.3.1</td> <!-- Danish Citizen Tests version -->
   <td>12.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>neuralmagic/Sparse-Llama-3.1-8B-2of4 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,841 ± 509 / 865 ± 263</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="da ner">27.60 ± 3.21 / 25.68 ± 2.70</td> <!-- DANSK -->
   <td class="da sent">37.08 ± 2.51 / 54.37 ± 2.72</td> <!-- Angry Tweets -->
   <td class="da la">10.84 ± 2.11 / 49.05 ± 4.51</td> <!-- ScaLA-da -->
   <td class="da rc">58.67 ± 0.97 / 63.61 ± 0.83</td> <!-- ScandiQA-da -->
   <td class="da summ">63.45 ± 1.07 / 17.77 ± 1.01</td> <!-- Nordjylland-News -->
   <td class="da know">38.31 ± 1.15 / 53.54 ± 0.91</td> <!-- Danske Talemaader -->
   <td class="da know">46.65 ± 1.64 / 63.48 ± 1.21</td> <!-- Danish Citizen Tests -->
   <td class="da reason">28.92 ± 3.15 / 44.79 ± 3.01</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.2.0</td> <!-- Angry Tweets version -->
   <td>13.2.0</td> <!-- ScaLA-da version -->
   <td>13.2.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">2.95</td> <!-- ScandEval rank -->
   <td class="da ner">41.13 ± 2.85 / 27.15 ± 1.82</td> <!-- DANSK -->
   <td class="da sent">38.90 ± 1.93 / 44.34 ± 1.64</td> <!-- Angry Tweets -->
   <td class="da la">9.60 ± 2.51 / 44.34 ± 5.20</td> <!-- ScaLA-da -->
   <td class="da rc">56.85 ± 1.27 / 62.25 ± 0.88</td> <!-- ScandiQA-da -->
   <td class="da summ">63.35 ± 0.50 / 15.11 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">45.46 ± 1.79 / 57.79 ± 1.31</td> <!-- Danske Talemaader -->
   <td class="da know">46.77 ± 2.98 / 64.61 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">12.19 ± 0.97 / 33.27 ± 0.89</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="da ner">35.44 ± 3.00 / 24.63 ± 1.65</td> <!-- DANSK -->
   <td class="da sent">44.88 ± 1.45 / 62.35 ± 1.33</td> <!-- Angry Tweets -->
   <td class="da la">9.74 ± 1.96 / 47.42 ± 4.19</td> <!-- ScaLA-da -->
   <td class="da rc">55.04 ± 0.79 / 61.34 ± 0.81</td> <!-- ScandiQA-da -->
   <td class="da summ">66.15 ± 0.67 / 19.69 ± 0.94</td> <!-- Nordjylland-News -->
   <td class="da know">32.17 ± 2.28 / 46.67 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">35.74 ± 2.46 / 55.18 ± 1.81</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.32 ± 0.41 / 32.24 ± 0.79</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.97</td> <!-- ScandEval rank -->
   <td class="da ner">37.93 ± 3.09 / 29.50 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">44.62 ± 1.98 / 62.62 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">0.28 ± 0.54 / 33.48 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">58.05 ± 1.02 / 62.89 ± 0.89</td> <!-- ScandiQA-da -->
   <td class="da summ">66.05 ± 1.13 / 21.82 ± 0.96</td> <!-- Nordjylland-News -->
   <td class="da know">38.54 ± 1.47 / 53.57 ± 1.26</td> <!-- Danske Talemaader -->
   <td class="da know">45.89 ± 3.00 / 63.14 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">12.38 ± 1.99 / 33.54 ± 1.61</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>emillykkejensen/Phi-3-mini-4k-instruct-dansk (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,360 ± 179 / 566 ± 190</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="da ner">39.96 ± 3.11 / 25.49 ± 2.71</td> <!-- DANSK -->
   <td class="da sent">44.93 ± 1.13 / 62.99 ± 0.87</td> <!-- Angry Tweets -->
   <td class="da la">4.01 ± 1.10 / 45.80 ± 2.61</td> <!-- ScaLA-da -->
   <td class="da rc">55.01 ± 0.80 / 60.67 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="da summ">65.29 ± 0.58 / 20.29 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">35.28 ± 1.37 / 51.43 ± 1.04</td> <!-- Danske Talemaader -->
   <td class="da know">41.62 ± 2.04 / 60.84 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.81 ± 1.05 / 33.65 ± 0.84</td> <!-- HellaSwag-da -->
   <td>12.10.4</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.4</td> <!-- ScandiQA-da version -->
   <td>12.10.4</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,172 ± 813 / 1,647 ± 518</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="da ner">37.02 ± 5.66 / 27.64 ± 3.92</td> <!-- DANSK -->
   <td class="da sent">40.65 ± 2.10 / 57.47 ± 2.56</td> <!-- Angry Tweets -->
   <td class="da la">7.48 ± 2.51 / 46.56 ± 4.52</td> <!-- ScaLA-da -->
   <td class="da rc">52.71 ± 0.70 / 59.07 ± 0.65</td> <!-- ScandiQA-da -->
   <td class="da summ">64.46 ± 0.75 / 14.29 ± 0.40</td> <!-- Nordjylland-News -->
   <td class="da know">47.26 ± 2.07 / 60.38 ± 1.55</td> <!-- Danske Talemaader -->
   <td class="da know">49.54 ± 1.64 / 66.15 ± 1.06</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.02 ± 1.22 / 30.79 ± 0.64</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="da ner">43.83 ± 1.93 / 34.03 ± 1.59</td> <!-- DANSK -->
   <td class="da sent">29.21 ± 1.92 / 52.86 ± 1.54</td> <!-- Angry Tweets -->
   <td class="da la">12.96 ± 1.67 / 55.83 ± 0.88</td> <!-- ScaLA-da -->
   <td class="da rc">49.76 ± 0.59 / 56.52 ± 0.50</td> <!-- ScandiQA-da -->
   <td class="da summ">65.36 ± 1.08 / 19.65 ± 1.01</td> <!-- Nordjylland-News -->
   <td class="da know">41.30 ± 1.79 / 54.09 ± 1.68</td> <!-- Danske Talemaader -->
   <td class="da know">31.26 ± 2.75 / 52.68 ± 2.10</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.02 ± 1.01 / 34.38 ± 0.79</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">3.02</td> <!-- ScandEval rank -->
   <td class="da ner">41.37 ± 2.50 / 24.64 ± 2.50</td> <!-- DANSK -->
   <td class="da sent">42.60 ± 1.06 / 61.52 ± 0.75</td> <!-- Angry Tweets -->
   <td class="da la">6.52 ± 1.34 / 45.01 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">50.57 ± 1.03 / 57.75 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">64.55 ± 0.78 / 19.26 ± 0.48</td> <!-- Nordjylland-News -->
   <td class="da know">38.64 ± 1.52 / 53.92 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">42.12 ± 2.16 / 61.23 ± 1.46</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.66 ± 1.32 / 35.16 ± 1.02</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="da ner">21.47 ± 3.87 / 16.98 ± 3.19</td> <!-- DANSK -->
   <td class="da sent">48.39 ± 0.66 / 64.51 ± 1.38</td> <!-- Angry Tweets -->
   <td class="da la">12.46 ± 2.22 / 52.33 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">52.51 ± 1.57 / 58.49 ± 1.58</td> <!-- ScandiQA-da -->
   <td class="da summ">66.53 ± 1.15 / 21.82 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">36.65 ± 2.42 / 48.70 ± 2.50</td> <!-- Danske Talemaader -->
   <td class="da know">49.97 ± 2.70 / 65.62 ± 1.94</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.64 ± 1.49 / 28.33 ± 0.91</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-40b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">39927</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">409 ± 53 / 182 ± 54</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da ner">26.57 ± 5.22 / 17.35 ± 2.79</td> <!-- DANSK -->
   <td class="da sent">47.81 ± 1.32 / 64.26 ± 1.28</td> <!-- Angry Tweets -->
   <td class="da la">11.13 ± 2.06 / 51.34 ± 3.02</td> <!-- ScaLA-da -->
   <td class="da rc">53.78 ± 0.70 / 60.13 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">66.21 ± 1.17 / 21.48 ± 1.27</td> <!-- Nordjylland-News -->
   <td class="da know">33.48 ± 3.59 / 46.04 ± 3.05</td> <!-- Danske Talemaader -->
   <td class="da know">29.86 ± 1.89 / 49.82 ± 1.71</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.67 ± 1.87 / 29.53 ± 1.25</td> <!-- HellaSwag-da -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- Nordjylland-News version -->
   <td>12.9.1</td> <!-- Danske Talemaader version -->
   <td>12.9.1</td> <!-- Danish Citizen Tests version -->
   <td>12.9.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="da ner">35.96 ± 2.61 / 28.58 ± 2.58</td> <!-- DANSK -->
   <td class="da sent">42.04 ± 1.42 / 60.76 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">8.65 ± 1.52 / 49.56 ± 3.60</td> <!-- ScaLA-da -->
   <td class="da rc">53.68 ± 0.94 / 59.73 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="da summ">63.22 ± 1.14 / 16.73 ± 1.50</td> <!-- Nordjylland-News -->
   <td class="da know">37.79 ± 1.24 / 52.64 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">29.62 ± 1.33 / 52.29 ± 1.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">16.87 ± 1.18 / 37.41 ± 0.90</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="da ner">48.44 ± 1.69 / 36.99 ± 1.77</td> <!-- DANSK -->
   <td class="da sent">39.07 ± 1.03 / 56.85 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">9.72 ± 1.58 / 46.85 ± 3.66</td> <!-- ScaLA-da -->
   <td class="da rc">51.18 ± 0.92 / 56.54 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">63.93 ± 0.79 / 17.49 ± 0.73</td> <!-- Nordjylland-News -->
   <td class="da know">33.11 ± 2.59 / 49.31 ± 2.03</td> <!-- Danske Talemaader -->
   <td class="da know">18.96 ± 2.16 / 46.29 ± 1.39</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.03 ± 1.28 / 31.42 ± 1.04</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,002 ± 95 / 416 ± 105</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="da ner">48.55 ± 1.75 / 37.15 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">39.16 ± 0.95 / 56.83 ± 1.90</td> <!-- Angry Tweets -->
   <td class="da la">10.43 ± 1.91 / 46.99 ± 3.74</td> <!-- ScaLA-da -->
   <td class="da rc">51.28 ± 0.95 / 56.75 ± 0.70</td> <!-- ScandiQA-da -->
   <td class="da summ">63.95 ± 0.80 / 17.51 ± 0.73</td> <!-- Nordjylland-News -->
   <td class="da know">33.33 ± 2.25 / 49.48 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">17.65 ± 1.77 / 45.43 ± 1.14</td> <!-- Danish Citizen Tests -->
   <td class="da reason">8.97 ± 1.07 / 31.39 ± 0.89</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="da ner">41.79 ± 2.11 / 32.67 ± 2.33</td> <!-- DANSK -->
   <td class="da sent">41.86 ± 1.28 / 61.22 ± 0.99</td> <!-- Angry Tweets -->
   <td class="da la">11.86 ± 1.80 / 50.92 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da rc">51.97 ± 0.76 / 59.28 ± 0.61</td> <!-- ScandiQA-da -->
   <td class="da summ">64.86 ± 0.75 / 19.26 ± 0.79</td> <!-- Nordjylland-News -->
   <td class="da know">29.55 ± 1.68 / 46.85 ± 1.40</td> <!-- Danske Talemaader -->
   <td class="da know">26.20 ± 2.23 / 51.29 ± 1.34</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.64 ± 0.91 / 27.01 ± 0.69</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="merged-model">
   <td>merge-crew/da-sv-dare-ties-density-0.3 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,461 ± 476 / 773 ± 248</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="da ner">30.16 ± 4.47 / 25.03 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">48.49 ± 2.41 / 63.06 ± 1.91</td> <!-- Angry Tweets -->
   <td class="da la">5.52 ± 4.66 / 38.81 ± 4.27</td> <!-- ScaLA-da -->
   <td class="da rc">52.44 ± 1.32 / 57.22 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="da summ">64.24 ± 1.42 / 18.43 ± 1.20</td> <!-- Nordjylland-News -->
   <td class="da know">43.57 ± 3.32 / 56.56 ± 2.69</td> <!-- Danske Talemaader -->
   <td class="da know">35.60 ± 4.28 / 50.86 ± 3.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.76 ± 2.77 / 28.91 ± 2.38</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="da ner">31.77 ± 3.29 / 22.31 ± 2.29</td> <!-- DANSK -->
   <td class="da sent">43.91 ± 1.94 / 61.54 ± 2.33</td> <!-- Angry Tweets -->
   <td class="da la">0.31 ± 0.61 / 33.43 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">58.44 ± 0.83 / 63.54 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="da summ">65.50 ± 0.82 / 19.96 ± 0.95</td> <!-- Nordjylland-News -->
   <td class="da know">20.18 ± 1.80 / 38.69 ± 1.57</td> <!-- Danske Talemaader -->
   <td class="da know">35.69 ± 2.31 / 57.05 ± 1.60</td> <!-- Danish Citizen Tests -->
   <td class="da reason">7.93 ± 1.49 / 29.76 ± 0.92</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="da ner">32.28 ± 3.16 / 23.24 ± 3.51</td> <!-- DANSK -->
   <td class="da sent">39.62 ± 2.39 / 56.09 ± 2.89</td> <!-- Angry Tweets -->
   <td class="da la">5.38 ± 2.18 / 36.31 ± 1.96</td> <!-- ScaLA-da -->
   <td class="da rc">54.16 ± 0.89 / 60.63 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">62.74 ± 1.62 / 16.48 ± 1.77</td> <!-- Nordjylland-News -->
   <td class="da know">37.49 ± 1.84 / 51.62 ± 1.43</td> <!-- Danske Talemaader -->
   <td class="da know">29.21 ± 3.46 / 52.40 ± 2.50</td> <!-- Danish Citizen Tests -->
   <td class="da reason">15.58 ± 1.48 / 36.33 ± 1.08</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-instruct-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,617 ± 995 / 1,623 ± 540</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da ner">45.90 ± 2.53 / 33.00 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">37.11 ± 1.88 / 56.47 ± 1.59</td> <!-- Angry Tweets -->
   <td class="da la">11.70 ± 2.16 / 50.31 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">50.11 ± 0.83 / 55.71 ± 0.49</td> <!-- ScandiQA-da -->
   <td class="da summ">63.86 ± 0.96 / 18.38 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">32.44 ± 2.29 / 46.63 ± 2.29</td> <!-- Danske Talemaader -->
   <td class="da know">7.46 ± 1.83 / 39.41 ± 1.17</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.62 ± 1.16 / 28.71 ± 0.79</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>tollefj/nordavind-7b-instruct-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,450 ± 961 / 2,082 ± 658</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="da ner">38.39 ± 3.57 / 24.87 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">49.44 ± 1.03 / 66.00 ± 0.88</td> <!-- Angry Tweets -->
   <td class="da la">7.50 ± 2.07 / 47.53 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da rc">51.24 ± 1.09 / 57.72 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="da summ">66.09 ± 1.40 / 22.03 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">3.53 ± 1.44 / 24.18 ± 1.19</td> <!-- Danske Talemaader -->
   <td class="da know">12.86 ± 2.99 / 40.23 ± 2.31</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.29 ± 1.23 / 25.61 ± 0.84</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,194 ± 949 / 1,967 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="da ner">39.83 ± 2.18 / 25.99 ± 1.56</td> <!-- DANSK -->
   <td class="da sent">47.48 ± 2.00 / 63.93 ± 1.86</td> <!-- Angry Tweets -->
   <td class="da la">4.55 ± 2.34 / 42.91 ± 4.05</td> <!-- ScaLA-da -->
   <td class="da rc">49.23 ± 0.63 / 57.45 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="da summ">66.17 ± 1.09 / 21.29 ± 0.90</td> <!-- Nordjylland-News -->
   <td class="da know">10.83 ± 2.01 / 28.99 ± 1.32</td> <!-- Danske Talemaader -->
   <td class="da know">14.66 ± 2.21 / 41.21 ± 0.84</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.71 ± 0.74 / 26.10 ± 0.82</td> <!-- HellaSwag-da -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8193</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.20</td> <!-- ScandEval rank -->
   <td class="da ner">17.29 ± 2.84 / 13.87 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 2.71 / 42.58 ± 3.24</td> <!-- Angry Tweets -->
   <td class="da la">6.39 ± 2.41 / 45.03 ± 4.32</td> <!-- ScaLA-da -->
   <td class="da rc">54.94 ± 1.00 / 59.95 ± 1.03</td> <!-- ScandiQA-da -->
   <td class="da summ">64.82 ± 1.05 / 20.37 ± 1.06</td> <!-- Nordjylland-News -->
   <td class="da know">48.07 ± 1.24 / 60.50 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">45.03 ± 1.84 / 63.40 ± 1.23</td> <!-- Danish Citizen Tests -->
   <td class="da reason">9.10 ± 1.03 / 30.51 ± 1.01</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da ner">16.72 ± 2.23 / 15.96 ± 2.08</td> <!-- DANSK -->
   <td class="da sent">45.89 ± 2.13 / 63.12 ± 1.98</td> <!-- Angry Tweets -->
   <td class="da la">11.25 ± 2.33 / 51.88 ± 2.35</td> <!-- ScaLA-da -->
   <td class="da rc">53.17 ± 0.79 / 59.30 ± 0.66</td> <!-- ScandiQA-da -->
   <td class="da summ">66.51 ± 1.29 / 22.13 ± 1.19</td> <!-- Nordjylland-News -->
   <td class="da know">14.84 ± 2.11 / 33.02 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">27.95 ± 3.54 / 48.55 ± 2.35</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.41 ± 1.06 / 26.59 ± 0.72</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.21</td> <!-- ScandEval rank -->
   <td class="da ner">34.25 ± 2.28 / 30.39 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">45.67 ± 2.41 / 58.41 ± 3.04</td> <!-- Angry Tweets -->
   <td class="da la">10.62 ± 2.37 / 53.20 ± 3.73</td> <!-- ScaLA-da -->
   <td class="da rc">50.77 ± 2.48 / 56.92 ± 2.42</td> <!-- ScandiQA-da -->
   <td class="da summ">65.67 ± 1.05 / 19.97 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">2.31 ± 1.92 / 24.65 ± 1.65</td> <!-- Danske Talemaader -->
   <td class="da know">10.57 ± 2.47 / 40.33 ± 1.67</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.64 ± 1.55 / 25.40 ± 0.77</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="da ner">32.34 ± 3.77 / 24.48 ± 3.17</td> <!-- DANSK -->
   <td class="da sent">29.50 ± 3.63 / 42.61 ± 4.86</td> <!-- Angry Tweets -->
   <td class="da la">3.89 ± 1.49 / 37.29 ± 3.65</td> <!-- ScaLA-da -->
   <td class="da rc">53.67 ± 0.84 / 59.15 ± 0.69</td> <!-- ScandiQA-da -->
   <td class="da summ">64.48 ± 0.83 / 19.25 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">24.40 ± 2.55 / 42.44 ± 1.87</td> <!-- Danske Talemaader -->
   <td class="da know">31.93 ± 1.90 / 54.43 ± 1.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">10.00 ± 1.73 / 32.31 ± 0.87</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">3.27</td> <!-- ScandEval rank -->
   <td class="da ner">35.21 ± 2.52 / 23.65 ± 2.52</td> <!-- DANSK -->
   <td class="da sent">12.73 ± 2.87 / 22.69 ± 1.80</td> <!-- Angry Tweets -->
   <td class="da la">4.75 ± 2.45 / 35.71 ± 3.01</td> <!-- ScaLA-da -->
   <td class="da rc">55.95 ± 1.09 / 61.53 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">64.28 ± 0.93 / 18.81 ± 0.83</td> <!-- Nordjylland-News -->
   <td class="da know">46.17 ± 1.83 / 59.04 ± 1.44</td> <!-- Danske Talemaader -->
   <td class="da know">36.46 ± 2.46 / 57.64 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">18.01 ± 1.66 / 38.12 ± 1.37</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-33B@1000B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,080 ± 700 / 331 ± 117</td> <!-- Model inference speed -->
   <td class="rank">3.28</td> <!-- ScandEval rank -->
   <td class="da ner">34.22 ± 2.47 / 22.52 ± 1.93</td> <!-- DANSK -->
   <td class="da sent">45.05 ± 2.49 / 62.23 ± 1.84</td> <!-- Angry Tweets -->
   <td class="da la">9.40 ± 2.63 / 44.83 ± 4.69</td> <!-- ScaLA-da -->
   <td class="da rc">54.92 ± 1.00 / 60.33 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">62.78 ± 0.97 / 15.36 ± 1.96</td> <!-- Nordjylland-News -->
   <td class="da know">0.43 ± 1.04 / 24.15 ± 0.82</td> <!-- Danske Talemaader -->
   <td class="da know">4.81 ± 3.43 / 36.58 ± 2.02</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.77 ± 0.76 / 26.00 ± 0.65</td> <!-- HellaSwag-da -->
   <td>12.9.0</td> <!-- DANSK version -->
   <td>12.9.0</td> <!-- Angry Tweets version -->
   <td>12.9.0</td> <!-- ScaLA-da version -->
   <td>12.9.0</td> <!-- ScandiQA-da version -->
   <td>12.9.0</td> <!-- Nordjylland-News version -->
   <td>12.9.0</td> <!-- Danske Talemaader version -->
   <td>12.9.0</td> <!-- Danish Citizen Tests version -->
   <td>12.9.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="da ner">4.51 ± 2.12 / 3.71 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">40.85 ± 1.26 / 59.79 ± 1.32</td> <!-- Angry Tweets -->
   <td class="da la">5.43 ± 1.74 / 46.21 ± 4.13</td> <!-- ScaLA-da -->
   <td class="da rc">51.76 ± 0.73 / 58.44 ± 0.54</td> <!-- ScandiQA-da -->
   <td class="da summ">64.64 ± 0.66 / 19.18 ± 0.74</td> <!-- Nordjylland-News -->
   <td class="da know">37.45 ± 1.45 / 52.86 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">36.39 ± 2.23 / 56.50 ± 1.51</td> <!-- Danish Citizen Tests -->
   <td class="da reason">17.42 ± 0.78 / 38.06 ± 0.55</td> <!-- HellaSwag-da -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.9.1</td> <!-- ScaLA-da version -->
   <td>12.9.1</td> <!-- ScandiQA-da version -->
   <td>12.9.1</td> <!-- Nordjylland-News version -->
   <td>12.10.0</td> <!-- Danske Talemaader version -->
   <td>12.10.0</td> <!-- Danish Citizen Tests version -->
   <td>12.10.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="da ner">27.41 ± 3.48 / 19.03 ± 1.76</td> <!-- DANSK -->
   <td class="da sent">30.23 ± 3.43 / 41.05 ± 4.38</td> <!-- Angry Tweets -->
   <td class="da la">11.34 ± 2.73 / 46.62 ± 5.48</td> <!-- ScaLA-da -->
   <td class="da rc">52.80 ± 0.68 / 59.56 ± 0.57</td> <!-- ScandiQA-da -->
   <td class="da summ">64.47 ± 1.21 / 18.39 ± 1.63</td> <!-- Nordjylland-News -->
   <td class="da know">11.04 ± 2.43 / 29.26 ± 1.97</td> <!-- Danske Talemaader -->
   <td class="da know">22.71 ± 2.48 / 46.50 ± 1.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.03 ± 1.08 / 26.49 ± 0.59</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>12.10.0</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>9.3.1</td> <!-- ScandiQA-da version -->
   <td>9.3.1</td> <!-- Nordjylland-News version -->
   <td>12.9.0</td> <!-- Danske Talemaader version -->
   <td>12.9.0</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-warm (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,175 ± 456 / 1,186 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.35</td> <!-- ScandEval rank -->
   <td class="da ner">37.80 ± 2.75 / 24.74 ± 2.30</td> <!-- DANSK -->
   <td class="da sent">40.51 ± 1.75 / 55.84 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">3.35 ± 1.84 / 44.60 ± 4.67</td> <!-- ScaLA-da -->
   <td class="da rc">49.08 ± 1.74 / 55.58 ± 1.57</td> <!-- ScandiQA-da -->
   <td class="da summ">65.81 ± 1.29 / 21.55 ± 1.19</td> <!-- Nordjylland-News -->
   <td class="da know">-0.90 ± 1.63 / 23.10 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">3.61 ± 2.89 / 35.10 ± 1.82</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.40 ± 1.28 / 25.12 ± 0.72</td> <!-- HellaSwag-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da ner">33.80 ± 2.66 / 25.32 ± 3.06</td> <!-- DANSK -->
   <td class="da sent">31.57 ± 2.65 / 46.48 ± 3.84</td> <!-- Angry Tweets -->
   <td class="da la">2.76 ± 1.76 / 44.96 ± 3.93</td> <!-- ScaLA-da -->
   <td class="da rc">54.20 ± 1.63 / 59.50 ± 1.54</td> <!-- ScandiQA-da -->
   <td class="da summ">64.19 ± 1.01 / 17.67 ± 1.44</td> <!-- Nordjylland-News -->
   <td class="da know">17.75 ± 1.41 / 35.70 ± 1.27</td> <!-- Danske Talemaader -->
   <td class="da know">28.24 ± 2.88 / 52.50 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.50 ± 0.85 / 27.33 ± 0.64</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.4</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.4</td> <!-- Danske Talemaader version -->
   <td>12.10.4</td> <!-- Danish Citizen Tests version -->
   <td>12.10.4</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="da ner">37.37 ± 2.46 / 26.81 ± 2.24</td> <!-- DANSK -->
   <td class="da sent">31.44 ± 1.82 / 48.96 ± 2.35</td> <!-- Angry Tweets -->
   <td class="da la">5.27 ± 2.40 / 40.63 ± 4.68</td> <!-- ScaLA-da -->
   <td class="da rc">48.41 ± 1.10 / 55.05 ± 0.97</td> <!-- ScandiQA-da -->
   <td class="da summ">63.82 ± 0.97 / 18.09 ± 0.88</td> <!-- Nordjylland-News -->
   <td class="da know">18.25 ± 1.54 / 38.38 ± 1.12</td> <!-- Danske Talemaader -->
   <td class="da know">19.54 ± 2.59 / 46.35 ± 1.91</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.64 ± 1.03 / 26.88 ± 0.77</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4097</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="da ner">28.60 ± 4.69 / 20.29 ± 3.37</td> <!-- DANSK -->
   <td class="da sent">48.71 ± 1.27 / 60.90 ± 2.95</td> <!-- Angry Tweets -->
   <td class="da la">2.30 ± 1.34 / 37.21 ± 2.50</td> <!-- ScaLA-da -->
   <td class="da rc">53.85 ± 1.73 / 58.96 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="da summ">64.05 ± 0.93 / 16.99 ± 1.44</td> <!-- Nordjylland-News -->
   <td class="da know">0.55 ± 0.59 / 24.15 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 2.29 / 35.66 ± 1.43</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.36 ± 1.09 / 25.24 ± 0.60</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.39</td> <!-- ScandEval rank -->
   <td class="da ner">38.62 ± 3.40 / 27.71 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">35.47 ± 1.35 / 52.70 ± 2.05</td> <!-- Angry Tweets -->
   <td class="da la">5.07 ± 1.76 / 43.91 ± 4.86</td> <!-- ScaLA-da -->
   <td class="da rc">45.21 ± 0.84 / 50.96 ± 0.94</td> <!-- ScandiQA-da -->
   <td class="da summ">62.50 ± 0.59 / 15.45 ± 0.50</td> <!-- Nordjylland-News -->
   <td class="da know">13.46 ± 2.03 / 33.24 ± 1.59</td> <!-- Danske Talemaader -->
   <td class="da know">15.31 ± 3.62 / 43.65 ± 2.19</td> <!-- Danish Citizen Tests -->
   <td class="da reason">6.00 ± 1.15 / 29.24 ± 0.76</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.40</td> <!-- ScandEval rank -->
   <td class="da ner">35.08 ± 2.24 / 25.02 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">4.00 ± 2.43 / 18.67 ± 0.94</td> <!-- Angry Tweets -->
   <td class="da la">3.68 ± 2.25 / 35.69 ± 1.87</td> <!-- ScaLA-da -->
   <td class="da rc">55.09 ± 0.79 / 60.88 ± 0.55</td> <!-- ScandiQA-da -->
   <td class="da summ">64.15 ± 1.03 / 18.95 ± 0.93</td> <!-- Nordjylland-News -->
   <td class="da know">34.07 ± 2.13 / 50.17 ± 1.60</td> <!-- Danske Talemaader -->
   <td class="da know">33.75 ± 2.28 / 54.22 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">13.61 ± 1.51 / 34.38 ± 1.20</td> <!-- HellaSwag-da -->
   <td>9.3.2</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.43</td> <!-- ScandEval rank -->
   <td class="da ner">19.97 ± 3.91 / 16.51 ± 3.20</td> <!-- DANSK -->
   <td class="da sent">40.21 ± 1.00 / 46.73 ± 1.82</td> <!-- Angry Tweets -->
   <td class="da la">2.27 ± 2.39 / 38.71 ± 4.03</td> <!-- ScaLA-da -->
   <td class="da rc">50.55 ± 1.22 / 56.27 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">63.07 ± 1.07 / 16.98 ± 0.98</td> <!-- Nordjylland-News -->
   <td class="da know">15.04 ± 1.21 / 35.51 ± 0.80</td> <!-- Danske Talemaader -->
   <td class="da know">30.63 ± 3.36 / 50.02 ± 2.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.90 ± 0.95 / 28.18 ± 0.88</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="da ner">35.45 ± 2.41 / 30.39 ± 1.72</td> <!-- DANSK -->
   <td class="da sent">36.94 ± 1.08 / 49.24 ± 1.41</td> <!-- Angry Tweets -->
   <td class="da la">1.12 ± 2.21 / 44.63 ± 2.92</td> <!-- ScaLA-da -->
   <td class="da rc">44.61 ± 0.84 / 53.34 ± 0.63</td> <!-- ScandiQA-da -->
   <td class="da summ">61.33 ± 1.47 / 15.38 ± 1.23</td> <!-- Nordjylland-News -->
   <td class="da know">27.14 ± 1.18 / 43.89 ± 1.09</td> <!-- Danske Talemaader -->
   <td class="da know">18.57 ± 1.82 / 46.35 ± 1.18</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.16 ± 0.85 / 26.86 ± 0.87</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-13b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,520 ± 736 / 823 ± 273</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="da ner">28.72 ± 2.61 / 20.53 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">37.19 ± 3.92 / 53.63 ± 4.06</td> <!-- Angry Tweets -->
   <td class="da la">2.96 ± 1.73 / 46.67 ± 3.16</td> <!-- ScaLA-da -->
   <td class="da rc">49.53 ± 1.49 / 54.83 ± 1.67</td> <!-- ScandiQA-da -->
   <td class="da summ">61.62 ± 1.05 / 14.33 ± 1.71</td> <!-- Nordjylland-News -->
   <td class="da know">1.17 ± 2.28 / 24.76 ± 1.52</td> <!-- Danske Talemaader -->
   <td class="da know">11.38 ± 3.80 / 38.52 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.16 ± 1.02 / 25.19 ± 0.70</td> <!-- HellaSwag-da -->
   <td>12.6.1</td> <!-- DANSK version -->
   <td>12.6.1</td> <!-- Angry Tweets version -->
   <td>12.6.1</td> <!-- ScaLA-da version -->
   <td>12.6.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.6.1</td> <!-- Danske Talemaader version -->
   <td>12.6.1</td> <!-- Danish Citizen Tests version -->
   <td>12.6.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="da ner">24.93 ± 4.36 / 22.23 ± 3.32</td> <!-- DANSK -->
   <td class="da sent">31.65 ± 2.94 / 51.95 ± 2.92</td> <!-- Angry Tweets -->
   <td class="da la">0.06 ± 1.20 / 34.30 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">51.47 ± 1.82 / 57.00 ± 1.94</td> <!-- ScandiQA-da -->
   <td class="da summ">62.67 ± 1.16 / 17.33 ± 1.12</td> <!-- Nordjylland-News -->
   <td class="da know">16.13 ± 2.67 / 36.80 ± 2.07</td> <!-- Danske Talemaader -->
   <td class="da know">24.21 ± 2.83 / 49.43 ± 1.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.27 ± 0.82 / 25.59 ± 0.52</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.8</td> <!-- Danske Talemaader version -->
   <td>12.10.8</td> <!-- Danish Citizen Tests version -->
   <td>12.10.8</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-33b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">33119</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4099</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">501 ± 50 / 238 ± 69</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da ner">25.35 ± 3.59 / 17.77 ± 2.25</td> <!-- DANSK -->
   <td class="da sent">44.70 ± 1.80 / 60.56 ± 2.77</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.60 / 34.16 ± 1.04</td> <!-- ScaLA-da -->
   <td class="da rc">52.29 ± 0.96 / 58.32 ± 0.75</td> <!-- ScandiQA-da -->
   <td class="da summ">62.23 ± 0.78 / 14.60 ± 1.38</td> <!-- Nordjylland-News -->
   <td class="da know">-1.01 ± 1.58 / 23.28 ± 1.25</td> <!-- Danske Talemaader -->
   <td class="da know">1.33 ± 1.98 / 33.83 ± 1.11</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.19 ± 0.99 / 25.04 ± 0.66</td> <!-- HellaSwag-da -->
   <td>12.9.1</td> <!-- DANSK version -->
   <td>12.9.1</td> <!-- Angry Tweets version -->
   <td>12.10.0</td> <!-- ScaLA-da version -->
   <td>12.10.0</td> <!-- ScandiQA-da version -->
   <td>12.10.0</td> <!-- Nordjylland-News version -->
   <td>12.10.0</td> <!-- Danske Talemaader version -->
   <td>12.10.0</td> <!-- Danish Citizen Tests version -->
   <td>12.10.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-instruct-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,059 ± 1,947 / 2,201 ± 728</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="da ner">37.21 ± 2.75 / 27.74 ± 2.59</td> <!-- DANSK -->
   <td class="da sent">31.54 ± 2.39 / 50.61 ± 2.88</td> <!-- Angry Tweets -->
   <td class="da la">6.30 ± 1.61 / 49.09 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da rc">44.86 ± 0.80 / 51.51 ± 0.91</td> <!-- ScandiQA-da -->
   <td class="da summ">61.56 ± 0.49 / 13.64 ± 0.97</td> <!-- Nordjylland-News -->
   <td class="da know">17.92 ± 1.52 / 37.22 ± 1.29</td> <!-- Danske Talemaader -->
   <td class="da know">10.79 ± 2.32 / 40.86 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.70 ± 1.10 / 26.14 ± 0.76</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,351 ± 448 / 707 ± 216</td> <!-- Model inference speed -->
   <td class="rank">3.53</td> <!-- ScandEval rank -->
   <td class="da ner">20.84 ± 2.40 / 16.93 ± 1.98</td> <!-- DANSK -->
   <td class="da sent">18.07 ± 3.41 / 27.21 ± 2.91</td> <!-- Angry Tweets -->
   <td class="da la">10.54 ± 2.38 / 48.37 ± 3.58</td> <!-- ScaLA-da -->
   <td class="da rc">51.22 ± 0.94 / 57.23 ± 0.68</td> <!-- ScandiQA-da -->
   <td class="da summ">65.15 ± 1.16 / 18.96 ± 1.15</td> <!-- Nordjylland-News -->
   <td class="da know">6.34 ± 2.61 / 28.14 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">18.00 ± 3.09 / 45.08 ± 1.79</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.57 ± 0.93 / 28.66 ± 0.66</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="da ner">28.45 ± 1.61 / 22.90 ± 1.63</td> <!-- DANSK -->
   <td class="da sent">39.09 ± 1.15 / 45.25 ± 0.82</td> <!-- Angry Tweets -->
   <td class="da la">1.43 ± 1.26 / 37.98 ± 2.74</td> <!-- ScaLA-da -->
   <td class="da rc">51.67 ± 2.31 / 57.34 ± 2.60</td> <!-- ScandiQA-da -->
   <td class="da summ">57.67 ± 0.91 / 11.58 ± 0.72</td> <!-- Nordjylland-News -->
   <td class="da know">11.94 ± 1.37 / 32.30 ± 0.94</td> <!-- Danske Talemaader -->
   <td class="da know">18.18 ± 2.76 / 45.98 ± 1.68</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.67 ± 1.70 / 26.59 ± 1.10</td> <!-- HellaSwag-da -->
   <td>12.10.8</td> <!-- DANSK version -->
   <td>12.10.8</td> <!-- Angry Tweets version -->
   <td>12.10.8</td> <!-- ScaLA-da version -->
   <td>12.10.8</td> <!-- ScandiQA-da version -->
   <td>12.10.8</td> <!-- Nordjylland-News version -->
   <td>12.10.8</td> <!-- Danske Talemaader version -->
   <td>12.10.8</td> <!-- Danish Citizen Tests version -->
   <td>12.10.8</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="da ner">28.18 ± 3.39 / 24.25 ± 3.30</td> <!-- DANSK -->
   <td class="da sent">29.32 ± 7.19 / 41.08 ± 8.29</td> <!-- Angry Tweets -->
   <td class="da la">2.90 ± 2.18 / 37.93 ± 4.98</td> <!-- ScaLA-da -->
   <td class="da rc">56.48 ± 1.11 / 62.92 ± 0.96</td> <!-- ScandiQA-da -->
   <td class="da summ">53.81 ± 1.18 / 9.42 ± 0.33</td> <!-- Nordjylland-News -->
   <td class="da know">27.86 ± 1.78 / 43.42 ± 1.51</td> <!-- Danske Talemaader -->
   <td class="da know">34.62 ± 2.93 / 55.21 ± 2.08</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.73 ± 0.61 / 27.77 ± 0.53</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b-v2-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 451 / 718 ± 221</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="da ner">15.35 ± 1.38 / 14.74 ± 1.30</td> <!-- DANSK -->
   <td class="da sent">2.85 ± 1.54 / 18.05 ± 0.23</td> <!-- Angry Tweets -->
   <td class="da la">10.99 ± 2.52 / 54.07 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da rc">50.51 ± 0.90 / 58.22 ± 0.76</td> <!-- ScandiQA-da -->
   <td class="da summ">66.38 ± 1.07 / 21.48 ± 1.21</td> <!-- Nordjylland-News -->
   <td class="da know">30.90 ± 3.84 / 43.86 ± 4.18</td> <!-- Danske Talemaader -->
   <td class="da know">16.81 ± 3.84 / 42.03 ± 2.42</td> <!-- Danish Citizen Tests -->
   <td class="da reason">11.08 ± 1.35 / 32.13 ± 1.04</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,969 ± 1,109 / 1,134 ± 374</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="da ner">23.98 ± 3.74 / 17.18 ± 2.86</td> <!-- DANSK -->
   <td class="da sent">38.74 ± 2.15 / 49.48 ± 3.14</td> <!-- Angry Tweets -->
   <td class="da la">1.04 ± 1.57 / 33.67 ± 0.22</td> <!-- ScaLA-da -->
   <td class="da rc">50.17 ± 0.92 / 56.29 ± 0.78</td> <!-- ScandiQA-da -->
   <td class="da summ">61.96 ± 0.87 / 13.71 ± 1.26</td> <!-- Nordjylland-News -->
   <td class="da know">-0.06 ± 0.90 / 23.97 ± 0.72</td> <!-- Danske Talemaader -->
   <td class="da know">-1.04 ± 2.16 / 34.90 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.73 ± 0.90 / 25.11 ± 0.51</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,136 ± 558 / 942 ± 290</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="da ner">23.87 ± 1.61 / 20.19 ± 1.60</td> <!-- DANSK -->
   <td class="da sent">31.21 ± 1.84 / 50.13 ± 2.79</td> <!-- Angry Tweets -->
   <td class="da la">2.04 ± 1.44 / 45.31 ± 3.73</td> <!-- ScaLA-da -->
   <td class="da rc">47.36 ± 0.81 / 54.08 ± 0.86</td> <!-- ScandiQA-da -->
   <td class="da summ">62.33 ± 0.49 / 16.36 ± 0.61</td> <!-- Nordjylland-News -->
   <td class="da know">17.68 ± 1.52 / 37.53 ± 1.55</td> <!-- Danske Talemaader -->
   <td class="da know">17.54 ± 2.35 / 45.41 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.72 ± 1.01 / 25.87 ± 0.82</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.2.0</td> <!-- ScaLA-da version -->
   <td>13.2.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,027 ± 503 / 903 ± 296</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="da ner">13.78 ± 2.85 / 11.90 ± 2.13</td> <!-- DANSK -->
   <td class="da sent">42.16 ± 0.68 / 45.21 ± 0.45</td> <!-- Angry Tweets -->
   <td class="da la">3.52 ± 1.90 / 39.81 ± 3.18</td> <!-- ScaLA-da -->
   <td class="da rc">20.02 ± 2.31 / 31.67 ± 2.19</td> <!-- ScandiQA-da -->
   <td class="da summ">65.03 ± 0.55 / 18.00 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">40.74 ± 1.91 / 53.17 ± 1.96</td> <!-- Danske Talemaader -->
   <td class="da know">43.43 ± 1.76 / 61.76 ± 1.32</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.50 ± 0.94 / 26.55 ± 0.96</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.4</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="da ner">24.44 ± 2.59 / 17.37 ± 2.03</td> <!-- DANSK -->
   <td class="da sent">34.03 ± 2.50 / 52.42 ± 2.16</td> <!-- Angry Tweets -->
   <td class="da la">2.25 ± 1.28 / 42.33 ± 3.11</td> <!-- ScaLA-da -->
   <td class="da rc">42.12 ± 1.18 / 49.76 ± 1.22</td> <!-- ScandiQA-da -->
   <td class="da summ">62.41 ± 1.21 / 17.66 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">15.16 ± 1.35 / 31.61 ± 1.92</td> <!-- Danske Talemaader -->
   <td class="da know">12.67 ± 1.89 / 41.99 ± 1.17</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.67 ± 1.17 / 26.82 ± 0.69</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NLPnorth/snakmodel-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,083 ± 531 / 983 ± 297</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da ner">23.74 ± 3.07 / 16.59 ± 1.61</td> <!-- DANSK -->
   <td class="da sent">44.71 ± 1.49 / 54.12 ± 2.35</td> <!-- Angry Tweets -->
   <td class="da la">21.24 ± 2.55 / 57.23 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 19.32 ± 0.59</td> <!-- ScandiQA-da -->
   <td class="da summ">58.05 ± 1.71 / 10.44 ± 0.71</td> <!-- Nordjylland-News -->
   <td class="da know">47.83 ± 2.75 / 58.23 ± 2.54</td> <!-- Danske Talemaader -->
   <td class="da know">55.62 ± 2.21 / 69.71 ± 1.67</td> <!-- Danish Citizen Tests -->
   <td class="da reason">5.51 ± 0.63 / 27.63 ± 0.81</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,745 ± 978 / 686 ± 159</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="da ner">22.31 ± 2.55 / 19.30 ± 2.14</td> <!-- DANSK -->
   <td class="da sent">34.05 ± 2.37 / 52.43 ± 2.46</td> <!-- Angry Tweets -->
   <td class="da la">0.70 ± 1.11 / 40.47 ± 3.04</td> <!-- ScaLA-da -->
   <td class="da rc">41.82 ± 2.07 / 48.91 ± 2.47</td> <!-- ScandiQA-da -->
   <td class="da summ">65.27 ± 0.25 / 17.79 ± 0.40</td> <!-- Nordjylland-News -->
   <td class="da know">6.27 ± 1.52 / 27.63 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">6.25 ± 3.25 / 37.75 ± 2.53</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.11 ± 1.44 / 26.00 ± 0.86</td> <!-- HellaSwag-da -->
   <td>9.1.2</td> <!-- DANSK version -->
   <td>9.1.2</td> <!-- Angry Tweets version -->
   <td>9.1.2</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.1.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.66</td> <!-- ScandEval rank -->
   <td class="da ner">31.80 ± 2.87 / 23.06 ± 2.09</td> <!-- DANSK -->
   <td class="da sent">6.85 ± 2.25 / 19.42 ± 0.91</td> <!-- Angry Tweets -->
   <td class="da la">0.97 ± 1.10 / 36.48 ± 3.91</td> <!-- ScaLA-da -->
   <td class="da rc">49.83 ± 1.73 / 55.19 ± 1.84</td> <!-- ScandiQA-da -->
   <td class="da summ">63.43 ± 0.90 / 16.85 ± 1.02</td> <!-- Nordjylland-News -->
   <td class="da know">15.97 ± 1.54 / 36.37 ± 1.08</td> <!-- Danske Talemaader -->
   <td class="da know">17.19 ± 2.72 / 45.23 ± 1.84</td> <!-- Danish Citizen Tests -->
   <td class="da reason">3.07 ± 0.91 / 27.05 ± 0.83</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-6.7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,285 ± 443 / 671 ± 205</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="da ner">18.23 ± 5.87 / 14.77 ± 3.36</td> <!-- DANSK -->
   <td class="da sent">22.71 ± 5.21 / 35.11 ± 6.59</td> <!-- Angry Tweets -->
   <td class="da la">5.03 ± 2.51 / 49.00 ± 2.64</td> <!-- ScaLA-da -->
   <td class="da rc">49.11 ± 1.16 / 55.56 ± 1.21</td> <!-- ScandiQA-da -->
   <td class="da summ">64.58 ± 1.03 / 18.26 ± 1.00</td> <!-- Nordjylland-News -->
   <td class="da know">1.11 ± 2.19 / 24.85 ± 1.14</td> <!-- Danske Talemaader -->
   <td class="da know">8.76 ± 3.09 / 37.32 ± 1.76</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.70 ± 0.84 / 26.17 ± 0.62</td> <!-- HellaSwag-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>11.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,971 ± 3,654 / 3,609 ± 1,197</td> <!-- Model inference speed -->
   <td class="rank">3.69</td> <!-- ScandEval rank -->
   <td class="da ner">29.44 ± 1.81 / 20.31 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">18.49 ± 2.47 / 35.29 ± 2.83</td> <!-- Angry Tweets -->
   <td class="da la">1.73 ± 1.63 / 38.18 ± 4.15</td> <!-- ScaLA-da -->
   <td class="da rc">44.39 ± 0.80 / 50.40 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">61.76 ± 1.10 / 15.33 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">22.03 ± 1.83 / 37.29 ± 1.77</td> <!-- Danske Talemaader -->
   <td class="da know">12.61 ± 2.43 / 41.82 ± 1.61</td> <!-- Danish Citizen Tests -->
   <td class="da reason">2.06 ± 0.89 / 26.03 ± 0.67</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,544 ± 1,000 / 1,106 ± 359</td> <!-- Model inference speed -->
   <td class="rank">3.72</td> <!-- ScandEval rank -->
   <td class="da ner">14.73 ± 1.84 / 14.44 ± 1.74</td> <!-- DANSK -->
   <td class="da sent">27.14 ± 1.93 / 42.34 ± 2.51</td> <!-- Angry Tweets -->
   <td class="da la">2.65 ± 1.66 / 40.63 ± 4.02</td> <!-- ScaLA-da -->
   <td class="da rc">46.38 ± 0.61 / 54.18 ± 0.52</td> <!-- ScandiQA-da -->
   <td class="da summ">65.48 ± 0.73 / 19.58 ± 1.08</td> <!-- Nordjylland-News -->
   <td class="da know">0.32 ± 0.71 / 23.38 ± 0.86</td> <!-- Danske Talemaader -->
   <td class="da know">7.00 ± 3.44 / 37.91 ± 1.85</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.13 ± 0.25 / 25.04 ± 0.54</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131073</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="da ner">19.82 ± 4.70 / 17.20 ± 3.57</td> <!-- DANSK -->
   <td class="da sent">35.97 ± 3.00 / 49.88 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">2.14 ± 2.61 / 44.16 ± 4.48</td> <!-- ScaLA-da -->
   <td class="da rc">46.59 ± 5.44 / 51.92 ± 6.14</td> <!-- ScandiQA-da -->
   <td class="da summ">58.65 ± 1.07 / 11.57 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">2.65 ± 1.26 / 25.17 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">9.51 ± 2.67 / 40.41 ± 1.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 1.13 / 24.79 ± 0.98</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HPLT/gpt-7b-nordic-prerelease (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7550</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,404 ± 931 / 1,638 ± 542</td> <!-- Model inference speed -->
   <td class="rank">3.77</td> <!-- ScandEval rank -->
   <td class="da ner">21.98 ± 3.33 / 18.42 ± 2.62</td> <!-- DANSK -->
   <td class="da sent">37.77 ± 3.06 / 55.35 ± 4.51</td> <!-- Angry Tweets -->
   <td class="da la">1.26 ± 1.86 / 34.03 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da rc">46.03 ± 1.44 / 52.54 ± 1.95</td> <!-- ScandiQA-da -->
   <td class="da summ">58.21 ± 1.54 / 11.61 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">-0.87 ± 1.27 / 35.70 ± 1.49</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.00 ± 0.00 / 25.18 ± 0.77</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.3.2</td> <!-- Angry Tweets version -->
   <td>12.3.2</td> <!-- ScaLA-da version -->
   <td>12.3.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.3.2</td> <!-- Danske Talemaader version -->
   <td>12.3.2</td> <!-- Danish Citizen Tests version -->
   <td>12.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>norallm/normistral-7b-scratch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,192 ± 454 / 1,198 ± 357</td> <!-- Model inference speed -->
   <td class="rank">3.78</td> <!-- ScandEval rank -->
   <td class="da ner">14.88 ± 3.92 / 14.02 ± 2.63</td> <!-- DANSK -->
   <td class="da sent">34.66 ± 1.82 / 46.40 ± 1.53</td> <!-- Angry Tweets -->
   <td class="da la">0.29 ± 1.86 / 41.01 ± 2.54</td> <!-- ScaLA-da -->
   <td class="da rc">42.16 ± 0.88 / 47.49 ± 0.98</td> <!-- ScandiQA-da -->
   <td class="da summ">63.19 ± 1.17 / 17.04 ± 1.07</td> <!-- Nordjylland-News -->
   <td class="da know">0.58 ± 1.06 / 23.87 ± 1.16</td> <!-- Danske Talemaader -->
   <td class="da know">4.60 ± 3.52 / 37.09 ± 1.52</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.34 ± 1.37 / 24.79 ± 0.73</td> <!-- HellaSwag-da -->
   <td>10.0.0</td> <!-- DANSK version -->
   <td>10.0.0</td> <!-- Angry Tweets version -->
   <td>10.0.0</td> <!-- ScaLA-da version -->
   <td>10.0.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-alpaca (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,607 ± 592 / 680 ± 208</td> <!-- Model inference speed -->
   <td class="rank">3.80</td> <!-- ScandEval rank -->
   <td class="da ner">12.95 ± 3.80 / 11.68 ± 2.31</td> <!-- DANSK -->
   <td class="da sent">27.68 ± 3.64 / 46.61 ± 4.11</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.96 / 47.94 ± 2.55</td> <!-- ScaLA-da -->
   <td class="da rc">38.60 ± 0.65 / 47.40 ± 0.64</td> <!-- ScandiQA-da -->
   <td class="da summ">63.32 ± 0.32 / 16.03 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">4.49 ± 1.44 / 27.32 ± 0.89</td> <!-- Danske Talemaader -->
   <td class="da know">12.81 ± 4.57 / 37.83 ± 2.98</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.68 ± 1.31 / 25.00 ± 0.79</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,855 ± 1,373 / 1,223 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="da ner">11.28 ± 0.96 / 11.02 ± 0.85</td> <!-- DANSK -->
   <td class="da sent">34.94 ± 3.80 / 49.66 ± 3.96</td> <!-- Angry Tweets -->
   <td class="da la">2.08 ± 1.48 / 45.41 ± 3.83</td> <!-- ScaLA-da -->
   <td class="da rc">36.59 ± 1.41 / 42.03 ± 1.44</td> <!-- ScandiQA-da -->
   <td class="da summ">63.38 ± 0.84 / 15.95 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">-0.09 ± 1.02 / 23.32 ± 0.76</td> <!-- Danske Talemaader -->
   <td class="da know">-0.76 ± 3.27 / 35.04 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.28 ± 0.39 / 25.19 ± 0.77</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-1.7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1711</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">16,249 ± 3,690 / 3,689 ± 1,226</td> <!-- Model inference speed -->
   <td class="rank">3.82</td> <!-- ScandEval rank -->
   <td class="da ner">24.47 ± 3.42 / 18.70 ± 2.18</td> <!-- DANSK -->
   <td class="da sent">9.93 ± 2.70 / 23.57 ± 3.00</td> <!-- Angry Tweets -->
   <td class="da la">1.22 ± 1.81 / 35.31 ± 1.93</td> <!-- ScaLA-da -->
   <td class="da rc">42.09 ± 2.63 / 47.54 ± 2.94</td> <!-- ScandiQA-da -->
   <td class="da summ">61.62 ± 0.72 / 14.36 ± 0.73</td> <!-- Nordjylland-News -->
   <td class="da know">19.65 ± 1.47 / 36.46 ± 1.24</td> <!-- Danske Talemaader -->
   <td class="da know">19.01 ± 2.56 / 46.27 ± 1.71</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.34 ± 1.16 / 25.88 ± 0.65</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-1.3b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1445</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,608 ± 988 / 1,115 ± 354</td> <!-- Model inference speed -->
   <td class="rank">3.84</td> <!-- ScandEval rank -->
   <td class="da ner">8.80 ± 5.54 / 8.63 ± 4.48</td> <!-- DANSK -->
   <td class="da sent">28.65 ± 2.81 / 47.83 ± 3.55</td> <!-- Angry Tweets -->
   <td class="da la">2.84 ± 1.81 / 49.21 ± 1.95</td> <!-- ScaLA-da -->
   <td class="da rc">45.34 ± 0.88 / 51.59 ± 0.80</td> <!-- ScandiQA-da -->
   <td class="da summ">62.17 ± 1.12 / 14.96 ± 1.16</td> <!-- Nordjylland-News -->
   <td class="da know">-1.31 ± 1.31 / 24.58 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">3.02 ± 3.77 / 36.58 ± 2.16</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.33 ± 1.17 / 24.65 ± 0.48</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.85</td> <!-- ScandEval rank -->
   <td class="da ner">18.00 ± 2.52 / 14.88 ± 1.68</td> <!-- DANSK -->
   <td class="da sent">26.58 ± 2.81 / 45.88 ± 3.40</td> <!-- Angry Tweets -->
   <td class="da la">0.63 ± 1.48 / 33.42 ± 0.28</td> <!-- ScaLA-da -->
   <td class="da rc">41.66 ± 1.48 / 49.40 ± 1.53</td> <!-- ScandiQA-da -->
   <td class="da summ">57.19 ± 1.18 / 11.87 ± 0.68</td> <!-- Nordjylland-News -->
   <td class="da know">22.17 ± 1.31 / 39.97 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">12.85 ± 3.11 / 42.13 ± 2.09</td> <!-- Danish Citizen Tests -->
   <td class="da reason">7.01 ± 0.62 / 30.16 ± 0.46</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.5.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1335</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,964 ± 2,255 / 1,299 ± 433</td> <!-- Model inference speed -->
   <td class="rank">3.85</td> <!-- ScandEval rank -->
   <td class="da ner">30.63 ± 2.60 / 20.55 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">22.35 ± 2.26 / 44.97 ± 2.66</td> <!-- Angry Tweets -->
   <td class="da la">1.95 ± 1.48 / 46.94 ± 1.55</td> <!-- ScaLA-da -->
   <td class="da rc">37.30 ± 0.69 / 43.95 ± 1.09</td> <!-- ScandiQA-da -->
   <td class="da summ">59.66 ± 0.68 / 13.59 ± 0.61</td> <!-- Nordjylland-News -->
   <td class="da know">2.78 ± 1.18 / 25.53 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">11.15 ± 3.42 / 38.81 ± 1.43</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.22 ± 0.88 / 24.33 ± 0.84</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.2.0</td> <!-- Angry Tweets version -->
   <td>13.2.0</td> <!-- ScaLA-da version -->
   <td>13.2.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.87</td> <!-- ScandEval rank -->
   <td class="da ner">9.83 ± 3.50 / 8.97 ± 2.64</td> <!-- DANSK -->
   <td class="da sent">29.03 ± 2.48 / 46.75 ± 3.69</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.87 / 33.34 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">46.43 ± 0.74 / 53.20 ± 0.47</td> <!-- ScandiQA-da -->
   <td class="da summ">56.43 ± 1.74 / 11.67 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">14.86 ± 1.85 / 33.52 ± 1.63</td> <!-- Danske Talemaader -->
   <td class="da know">17.56 ± 2.63 / 45.31 ± 1.78</td> <!-- Danish Citizen Tests -->
   <td class="da reason">4.78 ± 1.48 / 27.73 ± 1.32</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32769</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.91</td> <!-- ScandEval rank -->
   <td class="da ner">17.58 ± 1.95 / 15.48 ± 1.39</td> <!-- DANSK -->
   <td class="da sent">10.47 ± 3.28 / 19.91 ± 2.67</td> <!-- Angry Tweets -->
   <td class="da la">1.23 ± 1.53 / 36.92 ± 3.53</td> <!-- ScaLA-da -->
   <td class="da rc">42.56 ± 1.07 / 49.37 ± 1.19</td> <!-- ScandiQA-da -->
   <td class="da summ">62.56 ± 1.43 / 17.47 ± 1.30</td> <!-- Nordjylland-News -->
   <td class="da know">2.18 ± 1.10 / 24.56 ± 1.33</td> <!-- Danske Talemaader -->
   <td class="da know">4.94 ± 4.46 / 38.22 ± 2.74</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.84 ± 0.96 / 26.18 ± 0.79</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-356m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,758 ± 1,348 / 1,215 ± 391</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="da ner">16.13 ± 4.02 / 14.90 ± 3.13</td> <!-- DANSK -->
   <td class="da sent">27.61 ± 2.14 / 39.77 ± 1.85</td> <!-- Angry Tweets -->
   <td class="da la">1.96 ± 2.25 / 38.40 ± 2.99</td> <!-- ScaLA-da -->
   <td class="da rc">34.79 ± 1.52 / 39.67 ± 1.69</td> <!-- ScandiQA-da -->
   <td class="da summ">59.05 ± 1.42 / 12.41 ± 1.13</td> <!-- Nordjylland-News -->
   <td class="da know">1.00 ± 1.72 / 23.91 ± 0.88</td> <!-- Danske Talemaader -->
   <td class="da know">4.85 ± 3.16 / 36.78 ± 1.41</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.28 ± 0.38 / 25.19 ± 0.78</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.2</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>mhenrichsen/danskgpt-tiny (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1100</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,597 ± 1,983 / 1,926 ± 600</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="da ner">14.13 ± 3.50 / 12.15 ± 3.14</td> <!-- DANSK -->
   <td class="da sent">26.31 ± 5.33 / 44.07 ± 6.36</td> <!-- Angry Tweets -->
   <td class="da la">-0.54 ± 1.46 / 44.56 ± 3.34</td> <!-- ScaLA-da -->
   <td class="da rc">32.12 ± 1.62 / 38.99 ± 1.42</td> <!-- ScandiQA-da -->
   <td class="da summ">62.61 ± 0.99 / 15.12 ± 0.59</td> <!-- Nordjylland-News -->
   <td class="da know">-2.76 ± 1.71 / 22.41 ± 1.17</td> <!-- Danske Talemaader -->
   <td class="da know">5.08 ± 2.61 / 35.14 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.70 ± 0.94 / 24.83 ± 0.59</td> <!-- HellaSwag-da -->
   <td>0.0.0</td> <!-- DANSK version -->
   <td>0.0.0</td> <!-- Angry Tweets version -->
   <td>0.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>0.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.97</td> <!-- ScandEval rank -->
   <td class="da ner">26.76 ± 3.11 / 19.46 ± 2.38</td> <!-- DANSK -->
   <td class="da sent">30.76 ± 4.38 / 44.83 ± 4.36</td> <!-- Angry Tweets -->
   <td class="da la">0.55 ± 1.73 / 39.40 ± 4.57</td> <!-- ScaLA-da -->
   <td class="da rc">45.65 ± 1.22 / 52.49 ± 1.01</td> <!-- ScandiQA-da -->
   <td class="da summ">50.86 ± 0.68 / 9.46 ± 0.54</td> <!-- Nordjylland-News -->
   <td class="da know">0.26 ± 1.33 / 23.32 ± 0.83</td> <!-- Danske Talemaader -->
   <td class="da know">6.94 ± 1.82 / 37.66 ± 1.18</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.11 ± 0.71 / 24.99 ± 0.40</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-1b-a400m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1385</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,808 ± 2,183 / 1,289 ± 428</td> <!-- Model inference speed -->
   <td class="rank">4.00</td> <!-- ScandEval rank -->
   <td class="da ner">16.82 ± 3.53 / 14.28 ± 3.01</td> <!-- DANSK -->
   <td class="da sent">17.52 ± 2.86 / 27.96 ± 2.94</td> <!-- Angry Tweets -->
   <td class="da la">1.53 ± 2.06 / 36.59 ± 3.39</td> <!-- ScaLA-da -->
   <td class="da rc">40.21 ± 1.57 / 44.65 ± 1.79</td> <!-- ScandiQA-da -->
   <td class="da summ">60.13 ± 0.88 / 11.98 ± 0.53</td> <!-- Nordjylland-News -->
   <td class="da know">0.29 ± 0.73 / 24.16 ± 0.72</td> <!-- Danske Talemaader -->
   <td class="da know">0.55 ± 2.81 / 35.78 ± 1.38</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.21 ± 0.87 / 25.02 ± 0.65</td> <!-- HellaSwag-da -->
   <td>13.2.0</td> <!-- DANSK version -->
   <td>13.2.0</td> <!-- Angry Tweets version -->
   <td>13.2.0</td> <!-- ScaLA-da version -->
   <td>13.2.0</td> <!-- ScandiQA-da version -->
   <td>13.2.0</td> <!-- Nordjylland-News version -->
   <td>13.2.0</td> <!-- Danske Talemaader version -->
   <td>13.2.0</td> <!-- Danish Citizen Tests version -->
   <td>13.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.10</td> <!-- ScandEval rank -->
   <td class="da ner">17.38 ± 2.04 / 15.74 ± 1.99</td> <!-- DANSK -->
   <td class="da sent">10.72 ± 3.35 / 25.21 ± 3.80</td> <!-- Angry Tweets -->
   <td class="da la">1.32 ± 1.08 / 42.05 ± 3.69</td> <!-- ScaLA-da -->
   <td class="da rc">34.58 ± 0.97 / 40.37 ± 1.02</td> <!-- ScandiQA-da -->
   <td class="da summ">55.87 ± 5.22 / 11.87 ± 1.03</td> <!-- Nordjylland-News -->
   <td class="da know">4.56 ± 1.88 / 25.87 ± 1.72</td> <!-- Danske Talemaader -->
   <td class="da know">22.41 ± 3.16 / 42.73 ± 0.96</td> <!-- Danish Citizen Tests -->
   <td class="da reason">1.71 ± 0.99 / 25.84 ± 0.79</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>11.0.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="da ner">7.52 ± 3.92 / 6.60 ± 2.84</td> <!-- DANSK -->
   <td class="da sent">18.30 ± 3.89 / 27.62 ± 5.78</td> <!-- Angry Tweets -->
   <td class="da la">3.23 ± 1.94 / 45.74 ± 3.06</td> <!-- ScaLA-da -->
   <td class="da rc">46.35 ± 1.42 / 51.37 ± 1.43</td> <!-- ScandiQA-da -->
   <td class="da summ">53.01 ± 1.10 / 10.72 ± 0.80</td> <!-- Nordjylland-News -->
   <td class="da know">2.17 ± 1.53 / 23.73 ± 0.99</td> <!-- Danske Talemaader -->
   <td class="da know">0.22 ± 2.74 / 35.08 ± 1.48</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.65 ± 1.58 / 24.75 ± 1.03</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.17</td> <!-- ScandEval rank -->
   <td class="da ner">19.01 ± 1.91 / 17.08 ± 1.83</td> <!-- DANSK -->
   <td class="da sent">8.88 ± 1.86 / 24.27 ± 2.45</td> <!-- Angry Tweets -->
   <td class="da la">0.66 ± 1.41 / 37.98 ± 4.14</td> <!-- ScaLA-da -->
   <td class="da rc">32.78 ± 2.33 / 38.31 ± 2.81</td> <!-- ScandiQA-da -->
   <td class="da summ">55.57 ± 1.04 / 8.04 ± 0.82</td> <!-- Nordjylland-News -->
   <td class="da know">7.21 ± 1.78 / 29.73 ± 1.08</td> <!-- Danske Talemaader -->
   <td class="da know">16.56 ± 3.13 / 42.30 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.62 ± 1.30 / 25.65 ± 0.72</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,717 ± 1,553 / 2,013 ± 625</td> <!-- Model inference speed -->
   <td class="rank">4.26</td> <!-- ScandEval rank -->
   <td class="da ner">13.98 ± 1.54 / 13.46 ± 1.42</td> <!-- DANSK -->
   <td class="da sent">6.37 ± 3.38 / 25.43 ± 4.09</td> <!-- Angry Tweets -->
   <td class="da la">0.41 ± 0.80 / 33.31 ± 0.24</td> <!-- ScaLA-da -->
   <td class="da rc">20.46 ± 2.90 / 24.27 ± 3.23</td> <!-- ScandiQA-da -->
   <td class="da summ">60.87 ± 0.92 / 12.82 ± 1.14</td> <!-- Nordjylland-News -->
   <td class="da know">0.53 ± 1.10 / 24.39 ± 0.85</td> <!-- Danske Talemaader -->
   <td class="da know">4.72 ± 3.89 / 35.76 ± 1.86</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.07 ± 0.75 / 24.90 ± 0.90</td> <!-- HellaSwag-da -->
   <td>11.0.0</td> <!-- DANSK version -->
   <td>9.3.2</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.4.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="da ner">10.12 ± 1.24 / 9.84 ± 1.12</td> <!-- DANSK -->
   <td class="da sent">10.65 ± 3.65 / 28.33 ± 5.27</td> <!-- Angry Tweets -->
   <td class="da la">-0.66 ± 1.24 / 33.61 ± 0.26</td> <!-- ScaLA-da -->
   <td class="da rc">26.08 ± 3.96 / 28.87 ± 4.21</td> <!-- ScandiQA-da -->
   <td class="da summ">56.92 ± 0.98 / 8.57 ± 0.76</td> <!-- Nordjylland-News -->
   <td class="da know">0.10 ± 1.50 / 26.50 ± 1.00</td> <!-- Danske Talemaader -->
   <td class="da know">4.29 ± 5.87 / 35.00 ± 1.75</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 1.17 / 24.43 ± 0.74</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">22,023 ± 6,203 / 3,675 ± 1,231</td> <!-- Model inference speed -->
   <td class="rank">4.37</td> <!-- ScandEval rank -->
   <td class="da ner">12.68 ± 1.39 / 12.32 ± 1.19</td> <!-- DANSK -->
   <td class="da sent">3.61 ± 2.69 / 19.01 ± 3.95</td> <!-- Angry Tweets -->
   <td class="da la">1.79 ± 0.97 / 36.23 ± 3.19</td> <!-- ScaLA-da -->
   <td class="da rc">28.12 ± 3.14 / 32.48 ± 3.57</td> <!-- ScandiQA-da -->
   <td class="da summ">56.85 ± 1.37 / 10.17 ± 1.17</td> <!-- Nordjylland-News -->
   <td class="da know">-0.03 ± 0.59 / 23.99 ± 0.76</td> <!-- Danske Talemaader -->
   <td class="da know">6.03 ± 3.05 / 37.58 ± 1.59</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.20 ± 0.86 / 25.12 ± 0.70</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-360M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">362</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">21,777 ± 6,115 / 3,617 ± 1,211</td> <!-- Model inference speed -->
   <td class="rank">4.44</td> <!-- ScandEval rank -->
   <td class="da ner">8.97 ± 3.18 / 8.62 ± 2.72</td> <!-- DANSK -->
   <td class="da sent">2.66 ± 2.70 / 16.29 ± 2.34</td> <!-- Angry Tweets -->
   <td class="da la">1.65 ± 1.38 / 44.50 ± 3.21</td> <!-- ScaLA-da -->
   <td class="da rc">24.92 ± 1.68 / 28.73 ± 1.90</td> <!-- ScandiQA-da -->
   <td class="da summ">55.39 ± 0.68 / 10.01 ± 0.63</td> <!-- Nordjylland-News -->
   <td class="da know">0.28 ± 0.93 / 23.92 ± 0.72</td> <!-- Danske Talemaader -->
   <td class="da know">3.55 ± 3.45 / 35.45 ± 1.54</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.41 ± 1.41 / 25.02 ± 0.71</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,602 ± 7,583 / 3,953 ± 1,325</td> <!-- Model inference speed -->
   <td class="rank">4.49</td> <!-- ScandEval rank -->
   <td class="da ner">12.11 ± 1.07 / 11.48 ± 1.07</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 3.22 / 18.95 ± 3.93</td> <!-- Angry Tweets -->
   <td class="da la">0.25 ± 1.87 / 39.65 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da rc">14.02 ± 2.56 / 16.74 ± 2.74</td> <!-- ScandiQA-da -->
   <td class="da summ">56.53 ± 0.95 / 8.45 ± 0.77</td> <!-- Nordjylland-News -->
   <td class="da know">1.05 ± 1.51 / 26.37 ± 0.83</td> <!-- Danske Talemaader -->
   <td class="da know">10.81 ± 4.60 / 38.73 ± 1.77</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.50 ± 0.85 / 24.15 ± 0.67</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.49</td> <!-- ScandEval rank -->
   <td class="da ner">12.82 ± 2.64 / 12.37 ± 1.95</td> <!-- DANSK -->
   <td class="da sent">3.55 ± 3.64 / 22.75 ± 4.02</td> <!-- Angry Tweets -->
   <td class="da la">0.68 ± 1.41 / 35.13 ± 0.98</td> <!-- ScaLA-da -->
   <td class="da rc">19.85 ± 1.75 / 24.31 ± 1.88</td> <!-- ScandiQA-da -->
   <td class="da summ">55.58 ± 0.58 / 10.39 ± 0.63</td> <!-- Nordjylland-News -->
   <td class="da know">-0.11 ± 1.59 / 25.69 ± 0.65</td> <!-- Danske Talemaader -->
   <td class="da know">-2.13 ± 4.41 / 33.89 ± 3.03</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.88 ± 0.62 / 25.49 ± 0.74</td> <!-- HellaSwag-da -->
   <td>12.10.5</td> <!-- DANSK version -->
   <td>12.10.5</td> <!-- Angry Tweets version -->
   <td>12.10.5</td> <!-- ScaLA-da version -->
   <td>12.10.5</td> <!-- ScandiQA-da version -->
   <td>12.10.5</td> <!-- Nordjylland-News version -->
   <td>12.10.5</td> <!-- Danske Talemaader version -->
   <td>12.10.5</td> <!-- Danish Citizen Tests version -->
   <td>12.10.5</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2051</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.50</td> <!-- ScandEval rank -->
   <td class="da ner">13.39 ± 2.60 / 12.39 ± 2.46</td> <!-- DANSK -->
   <td class="da sent">17.94 ± 5.58 / 32.80 ± 3.63</td> <!-- Angry Tweets -->
   <td class="da la">-2.02 ± 2.28 / 40.63 ± 4.12</td> <!-- ScaLA-da -->
   <td class="da rc">23.65 ± 2.96 / 26.24 ± 3.20</td> <!-- ScandiQA-da -->
   <td class="da summ">48.87 ± 1.42 / 5.39 ± 0.62</td> <!-- Nordjylland-News -->
   <td class="da know">-0.33 ± 0.61 / 23.91 ± 0.71</td> <!-- Danske Talemaader -->
   <td class="da know">0.05 ± 2.96 / 34.67 ± 1.78</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.08 ± 0.81 / 25.21 ± 0.56</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.1.0</td> <!-- Angry Tweets version -->
   <td>12.1.0</td> <!-- ScaLA-da version -->
   <td>12.1.0</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>12.1.0</td> <!-- Danske Talemaader version -->
   <td>12.1.0</td> <!-- Danish Citizen Tests version -->
   <td>12.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6051</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,556 ± 580 / 681 ± 214</td> <!-- Model inference speed -->
   <td class="rank">4.53</td> <!-- ScandEval rank -->
   <td class="da ner">0.24 ± 0.25 / 0.25 ± 0.21</td> <!-- DANSK -->
   <td class="da sent">27.80 ± 6.39 / 43.80 ± 5.16</td> <!-- Angry Tweets -->
   <td class="da la">0.56 ± 0.51 / 34.04 ± 1.28</td> <!-- ScaLA-da -->
   <td class="da rc">6.84 ± 6.83 / 21.33 ± 6.27</td> <!-- ScandiQA-da -->
   <td class="da summ">53.76 ± 0.47 / 11.17 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">-1.83 ± 1.68 / 23.94 ± 1.25</td> <!-- Danske Talemaader -->
   <td class="da know">0.99 ± 3.76 / 34.10 ± 2.62</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.48 ± 0.94 / 24.73 ± 0.61</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.58</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">13.00 ± 4.17 / 24.41 ± 3.12</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 12.39 ± 1.52</td> <!-- ScandiQA-da -->
   <td class="da summ">61.25 ± 0.17 / 12.03 ± 0.21</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 0.14 / 25.18 ± 0.77</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>9.3.1</td> <!-- Angry Tweets version -->
   <td>9.3.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.3.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-126m (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">186</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,958 ± 1,815 / 2,240 ± 696</td> <!-- Model inference speed -->
   <td class="rank">4.59</td> <!-- ScandEval rank -->
   <td class="da ner">3.43 ± 2.66 / 5.56 ± 1.90</td> <!-- DANSK -->
   <td class="da sent">9.18 ± 4.25 / 26.36 ± 3.94</td> <!-- Angry Tweets -->
   <td class="da la">-0.22 ± 1.53 / 34.20 ± 0.84</td> <!-- ScaLA-da -->
   <td class="da rc">16.64 ± 3.32 / 19.46 ± 3.63</td> <!-- ScandiQA-da -->
   <td class="da summ">52.34 ± 1.60 / 8.84 ± 0.78</td> <!-- Nordjylland-News -->
   <td class="da know">-0.58 ± 0.97 / 24.00 ± 0.77</td> <!-- Danske Talemaader -->
   <td class="da know">5.18 ± 4.75 / 36.68 ± 2.20</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.28 ± 0.99 / 24.75 ± 0.93</td> <!-- HellaSwag-da -->
   <td>9.2.0</td> <!-- DANSK version -->
   <td>9.2.0</td> <!-- Angry Tweets version -->
   <td>9.2.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>9.2.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,373 ± 120 / 709 ± 172</td> <!-- Model inference speed -->
   <td class="rank">4.63</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">4.81 ± 2.69 / 19.31 ± 1.01</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 30.05 ± 4.99</td> <!-- ScandiQA-da -->
   <td class="da summ">61.06 ± 0.14 / 12.02 ± 0.15</td> <!-- Nordjylland-News -->
   <td class="da know">0.00 ± 0.00 / 24.00 ± 0.73</td> <!-- Danske Talemaader -->
   <td class="da know">0.00 ± 0.00 / 35.86 ± 1.26</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.15 ± 0.64 / 25.21 ± 0.79</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>HuggingFaceTB/SmolLM2-135M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,346 ± 7,812 / 4,082 ± 1,372</td> <!-- Model inference speed -->
   <td class="rank">4.70</td> <!-- ScandEval rank -->
   <td class="da ner">13.72 ± 1.83 / 13.41 ± 1.52</td> <!-- DANSK -->
   <td class="da sent">3.79 ± 3.11 / 21.06 ± 4.74</td> <!-- Angry Tweets -->
   <td class="da la">-0.45 ± 0.70 / 39.69 ± 4.95</td> <!-- ScaLA-da -->
   <td class="da rc">14.69 ± 2.86 / 17.28 ± 3.01</td> <!-- ScandiQA-da -->
   <td class="da summ">47.44 ± 1.55 / 6.04 ± 0.58</td> <!-- Nordjylland-News -->
   <td class="da know">-0.58 ± 2.44 / 25.72 ± 1.40</td> <!-- Danske Talemaader -->
   <td class="da know">10.99 ± 5.42 / 38.26 ± 1.92</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.51 ± 1.30 / 24.79 ± 0.70</td> <!-- HellaSwag-da -->
   <td>13.1.0</td> <!-- DANSK version -->
   <td>13.1.0</td> <!-- Angry Tweets version -->
   <td>13.1.0</td> <!-- ScaLA-da version -->
   <td>13.1.0</td> <!-- ScandiQA-da version -->
   <td>13.1.0</td> <!-- Nordjylland-News version -->
   <td>13.1.0</td> <!-- Danske Talemaader version -->
   <td>13.1.0</td> <!-- Danish Citizen Tests version -->
   <td>13.1.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NbAiLab/nb-gpt-j-6B@sharded (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,630 ± 605 / 684 ± 217</td> <!-- Model inference speed -->
   <td class="rank">4.73</td> <!-- ScandEval rank -->
   <td class="da ner">0.36 ± 0.40 / 1.82 ± 1.16</td> <!-- DANSK -->
   <td class="da sent">11.00 ± 7.09 / 26.09 ± 6.96</td> <!-- Angry Tweets -->
   <td class="da la">-0.11 ± 1.16 / 33.76 ± 0.86</td> <!-- ScaLA-da -->
   <td class="da rc">5.15 ± 6.60 / 17.35 ± 5.86</td> <!-- ScandiQA-da -->
   <td class="da summ">51.83 ± 0.77 / 10.14 ± 0.49</td> <!-- Nordjylland-News -->
   <td class="da know">-0.96 ± 1.47 / 23.86 ± 1.33</td> <!-- Danske Talemaader -->
   <td class="da know">3.51 ± 3.46 / 35.41 ± 2.22</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.73 ± 1.39 / 25.54 ± 1.00</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorGLM/NorGPT-369M (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,896 ± 5,099 / 3,848 ± 1,251</td> <!-- Model inference speed -->
   <td class="rank">4.79</td> <!-- ScandEval rank -->
   <td class="da ner">1.13 ± 1.19 / 0.97 ± 1.03</td> <!-- DANSK -->
   <td class="da sent">2.06 ± 2.30 / 20.38 ± 2.71</td> <!-- Angry Tweets -->
   <td class="da la">-0.36 ± 0.97 / 41.52 ± 4.00</td> <!-- ScaLA-da -->
   <td class="da rc">0.32 ± 0.12 / 4.20 ± 0.61</td> <!-- ScandiQA-da -->
   <td class="da summ">54.00 ± 0.80 / 9.08 ± 0.87</td> <!-- Nordjylland-News -->
   <td class="da know">-2.57 ± 2.04 / 23.19 ± 1.37</td> <!-- Danske Talemaader -->
   <td class="da know">3.26 ± 1.64 / 29.55 ± 2.52</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.62 ± 0.87 / 24.55 ± 0.66</td> <!-- HellaSwag-da -->
   <td>12.5.2</td> <!-- DANSK version -->
   <td>12.5.2</td> <!-- Angry Tweets version -->
   <td>12.5.2</td> <!-- ScaLA-da version -->
   <td>12.5.2</td> <!-- ScandiQA-da version -->
   <td>12.5.2</td> <!-- Nordjylland-News version -->
   <td>12.5.2</td> <!-- Danske Talemaader version -->
   <td>12.5.2</td> <!-- Danish Citizen Tests version -->
   <td>12.5.2</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>peter-sk/gpt-neox-da (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1515</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,025 ± 1,442 / 1,342 ± 431</td> <!-- Model inference speed -->
   <td class="rank">4.91</td> <!-- ScandEval rank -->
   <td class="da ner">0.64 ± 0.89 / 0.52 ± 0.69</td> <!-- DANSK -->
   <td class="da sent">-0.52 ± 1.72 / 28.55 ± 1.60</td> <!-- Angry Tweets -->
   <td class="da la">-0.02 ± 1.55 / 36.82 ± 2.52</td> <!-- ScaLA-da -->
   <td class="da rc">0.48 ± 0.27 / 2.89 ± 0.53</td> <!-- ScandiQA-da -->
   <td class="da summ">50.23 ± 0.89 / 6.09 ± 0.27</td> <!-- Nordjylland-News -->
   <td class="da know">0.90 ± 0.92 / 26.20 ± 1.02</td> <!-- Danske Talemaader -->
   <td class="da know">4.10 ± 2.68 / 33.71 ± 1.88</td> <!-- Danish Citizen Tests -->
   <td class="da reason">0.04 ± 1.16 / 25.21 ± 0.48</td> <!-- HellaSwag-da -->
   <td>10.0.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>10.0.1</td> <!-- ScaLA-da version -->
   <td>10.0.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>10.0.1</td> <!-- Danske Talemaader version -->
   <td>10.0.1</td> <!-- Danish Citizen Tests version -->
   <td>10.0.1</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ssmits/Falcon2-5.5B-multilingual (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">5465</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">65</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,692 ± 1,423 / 1,960 ± 644</td> <!-- Model inference speed -->
   <td class="rank">5.13</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.02 ± 0.02 / 0.03 ± 0.03</td> <!-- ScandiQA-da -->
   <td class="da summ">42.82 ± 0.93 / 0.20 ± 0.02</td> <!-- Nordjylland-News -->
   <td class="da know">4.55 ± 2.15 / 25.74 ± 1.15</td> <!-- Danske Talemaader -->
   <td class="da know">-1.17 ± 3.12 / 34.84 ± 1.63</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.26 ± 1.34 / 24.88 ± 0.69</td> <!-- HellaSwag-da -->
   <td>13.0.0</td> <!-- DANSK version -->
   <td>13.0.0</td> <!-- Angry Tweets version -->
   <td>13.0.0</td> <!-- ScaLA-da version -->
   <td>13.0.0</td> <!-- ScandiQA-da version -->
   <td>13.0.0</td> <!-- Nordjylland-News version -->
   <td>13.0.0</td> <!-- Danske Talemaader version -->
   <td>13.0.0</td> <!-- Danish Citizen Tests version -->
   <td>13.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.21</td> <!-- ScandEval rank -->
   <td class="da ner">0.65 ± 0.68 / 0.59 ± 0.63</td> <!-- DANSK -->
   <td class="da sent">2.61 ± 2.75 / 20.51 ± 2.48</td> <!-- Angry Tweets -->
   <td class="da la">-0.73 ± 1.72 / 41.15 ± 3.71</td> <!-- ScaLA-da -->
   <td class="da rc">1.99 ± 1.69 / 2.68 ± 1.87</td> <!-- ScandiQA-da -->
   <td class="da summ">35.64 ± 4.11 / 4.70 ± 2.01</td> <!-- Nordjylland-News -->
   <td class="da know">-0.61 ± 0.54 / 24.71 ± 1.18</td> <!-- Danske Talemaader -->
   <td class="da know">6.94 ± 3.67 / 38.18 ± 1.72</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-1.12 ± 0.87 / 24.71 ± 0.88</td> <!-- HellaSwag-da -->
   <td>9.3.1</td> <!-- DANSK version -->
   <td>10.0.1</td> <!-- Angry Tweets version -->
   <td>11.0.0</td> <!-- ScaLA-da version -->
   <td>12.5.1</td> <!-- ScandiQA-da version -->
   <td>12.6.1</td> <!-- Nordjylland-News version -->
   <td>11.0.0</td> <!-- Danske Talemaader version -->
   <td>11.0.0</td> <!-- Danish Citizen Tests version -->
   <td>11.0.0</td> <!-- HellaSwag-da version -->
   </tr>
  <tr class="not-merged-model">
   <td>Sigurdur/icebreaker (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">110</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">48,619 ± 7,681 / 13,831 ± 4,404</td> <!-- Model inference speed -->
   <td class="rank">5.34</td> <!-- ScandEval rank -->
   <td class="da ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- DANSK -->
   <td class="da sent">0.00 ± 0.00 / 18.12 ± 0.19</td> <!-- Angry Tweets -->
   <td class="da la">0.00 ± 0.00 / 33.25 ± 0.23</td> <!-- ScaLA-da -->
   <td class="da rc">0.00 ± 0.00 / 0.04 ± 0.01</td> <!-- ScandiQA-da -->
   <td class="da summ">37.85 ± 0.55 / 0.76 ± 0.08</td> <!-- Nordjylland-News -->
   <td class="da know">0.26 ± 0.46 / 23.72 ± 0.47</td> <!-- Danske Talemaader -->
   <td class="da know">-0.75 ± 1.90 / 34.96 ± 1.13</td> <!-- Danish Citizen Tests -->
   <td class="da reason">-0.88 ± 0.48 / 24.60 ± 0.50</td> <!-- HellaSwag-da -->
   <td>12.7.0</td> <!-- DANSK version -->
   <td>12.7.0</td> <!-- Angry Tweets version -->
   <td>12.7.0</td> <!-- ScaLA-da version -->
   <td>12.7.0</td> <!-- ScandiQA-da version -->
   <td>12.7.0</td> <!-- Nordjylland-News version -->
   <td>12.7.0</td> <!-- Danske Talemaader version -->
   <td>12.7.0</td> <!-- Danish Citizen Tests version -->
   <td>12.7.0</td> <!-- HellaSwag-da version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/danish-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Danish NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-95k2s&quot; src=&quot;https://datawrapper.dwcdn.net/95k2s/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
