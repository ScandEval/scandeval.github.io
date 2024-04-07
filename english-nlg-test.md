---
layout: leaderboard
title: English NLG
---

<center>Last updated: 07/04/2024 15:43:14 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlg-test" class="sortable fixed centered small-font">
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
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.16</td> <!-- ScandEval rank -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
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
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.35 ± 1.25</td> <!-- SQuAD -->
   <td class="en summ">70.55 ± 0.73 / 26.32 ± 0.97</td> <!-- CNN-DailyMail -->
   <td class="en know">51.74 ± 1.82 / 63.44 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">71.96 ± 2.38 / 78.87 ± 1.66</td> <!-- HellaSwag -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>9.3.2</td> <!-- SST5 version -->
   <td>9.3.2</td> <!-- ScaLA-en version -->
   <td>9.3.2</td> <!-- SQuAD version -->
   <td>9.3.2</td> <!-- CNN-DailyMail version -->
   <td>9.3.2</td> <!-- MMLU version -->
   <td>9.3.2</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.46</td> <!-- ScandEval rank -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">73.45 ± 1.83 / 84.54 ± 1.42</td> <!-- SQuAD -->
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
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">1.47</td> <!-- ScandEval rank -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en qa">75.89 ± 1.84 / 85.86 ± 1.03</td> <!-- SQuAD -->
   <td class="en summ">64.51 ± 0.30 / 18.84 ± 0.32</td> <!-- CNN-DailyMail -->
   <td class="en know">50.89 ± 0.77 / 63.01 ± 0.60</td> <!-- MMLU -->
   <td class="en reason">68.29 ± 0.74 / 75.90 ± 0.62</td> <!-- HellaSwag -->
   <td>9.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.0</td> <!-- SST5 version -->
   <td>10.0.0</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.0.0</td> <!-- CNN-DailyMail version -->
   <td>10.0.1</td> <!-- MMLU version -->
   <td>10.0.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="en ner">60.90 ± 3.17 / 53.69 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">66.54 ± 1.42 / 69.26 ± 0.83</td> <!-- SST5 -->
   <td class="en la">23.60 ± 3.72 / 57.65 ± 4.08</td> <!-- ScaLA-en -->
   <td class="en qa">75.14 ± 1.51 / 87.25 ± 0.61</td> <!-- SQuAD -->
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
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="en ner">55.89 ± 1.43 / 52.75 ± 1.23</td> <!-- CoNLL-en -->
   <td class="en sent">60.55 ± 1.54 / 68.53 ± 0.71</td> <!-- SST5 -->
   <td class="en la">28.60 ± 3.36 / 60.31 ± 4.06</td> <!-- ScaLA-en -->
   <td class="en qa">70.49 ± 0.74 / 82.68 ± 0.52</td> <!-- SQuAD -->
   <td class="en summ">68.67 ± 0.11 / 21.65 ± 0.21</td> <!-- CNN-DailyMail -->
   <td class="en know">39.82 ± 0.76 / 54.62 ± 0.57</td> <!-- MMLU -->
   <td class="en reason">51.82 ± 1.03 / 63.79 ± 0.79</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="en ner">57.64 ± 1.43 / 54.58 ± 1.36</td> <!-- CoNLL-en -->
   <td class="en sent">59.62 ± 1.29 / 68.55 ± 0.56</td> <!-- SST5 -->
   <td class="en la">28.55 ± 3.97 / 60.49 ± 4.25</td> <!-- ScaLA-en -->
   <td class="en qa">70.04 ± 0.89 / 82.09 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">67.27 ± 0.39 / 19.77 ± 0.31</td> <!-- CNN-DailyMail -->
   <td class="en know">38.68 ± 1.02 / 53.45 ± 0.74</td> <!-- MMLU -->
   <td class="en reason">47.47 ± 1.28 / 60.44 ± 1.02</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>10.0.1</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.38 ± 1.76 / 81.90 ± 0.57</td> <!-- SQuAD -->
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
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="en ner">56.07 ± 4.01 / 51.66 ± 3.99</td> <!-- CoNLL-en -->
   <td class="en sent">65.29 ± 1.43 / 69.38 ± 0.73</td> <!-- SST5 -->
   <td class="en la">25.78 ± 2.57 / 61.50 ± 2.24</td> <!-- ScaLA-en -->
   <td class="en qa">73.13 ± 4.05 / 83.85 ± 2.69</td> <!-- SQuAD -->
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
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en qa">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
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
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">1.76</td> <!-- ScandEval rank -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.27 ± 2.09 / 77.85 ± 0.70</td> <!-- SQuAD -->
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
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="en ner">60.58 ± 2.67 / 56.83 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.10 ± 1.65 / 68.81 ± 0.76</td> <!-- SST5 -->
   <td class="en la">20.17 ± 3.68 / 54.76 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">75.29 ± 1.37 / 86.48 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.63 ± 0.46 / 25.61 ± 0.45</td> <!-- CNN-DailyMail -->
   <td class="en know">38.48 ± 1.10 / 53.32 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">27.67 ± 2.08 / 43.61 ± 2.08</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>12.2.0</td> <!-- SST5 version -->
   <td>12.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>12.4.0</td> <!-- CNN-DailyMail version -->
   <td>12.3.1</td> <!-- MMLU version -->
   <td>12.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>danish-foundation-models/munin-7b-v0.1dev0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,113 ± 1,044 / 1,790 ± 579</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="en ner">56.38 ± 2.95 / 50.80 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">66.04 ± 1.68 / 65.21 ± 1.48</td> <!-- SST5 -->
   <td class="en la">22.15 ± 3.57 / 57.71 ± 4.24</td> <!-- ScaLA-en -->
   <td class="en qa">71.32 ± 1.41 / 83.70 ± 0.93</td> <!-- SQuAD -->
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
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.45 ± 1.39 / 80.79 ± 0.79</td> <!-- SQuAD -->
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
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,467 ± 656 / 986 ± 297</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">7.03 ± 1.24 / 6.26 ± 1.11</td> <!-- CoNLL-en -->
   <td class="en sent">67.10 ± 0.81 / 70.66 ± 0.76</td> <!-- SST5 -->
   <td class="en la">29.86 ± 5.28 / 62.88 ± 4.77</td> <!-- ScaLA-en -->
   <td class="en qa">73.50 ± 1.70 / 84.27 ± 1.31</td> <!-- SQuAD -->
   <td class="en summ">68.99 ± 0.54 / 23.86 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">47.47 ± 1.20 / 60.33 ± 0.91</td> <!-- MMLU -->
   <td class="en reason">35.77 ± 4.27 / 49.83 ± 3.77</td> <!-- HellaSwag -->
   <td>12.5.1</td> <!-- CoNLL-en version -->
   <td>12.5.1</td> <!-- SST5 version -->
   <td>12.5.1</td> <!-- ScaLA-en version -->
   <td>12.5.1</td> <!-- SQuAD version -->
   <td>12.5.1</td> <!-- CNN-DailyMail version -->
   <td>12.5.1</td> <!-- MMLU version -->
   <td>12.5.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="en ner">56.78 ± 2.99 / 53.55 ± 2.47</td> <!-- CoNLL-en -->
   <td class="en sent">63.32 ± 1.29 / 68.50 ± 0.53</td> <!-- SST5 -->
   <td class="en la">18.92 ± 2.39 / 57.96 ± 1.89</td> <!-- ScaLA-en -->
   <td class="en qa">72.38 ± 2.57 / 83.46 ± 1.49</td> <!-- SQuAD -->
   <td class="en summ">68.61 ± 0.55 / 23.48 ± 0.74</td> <!-- CNN-DailyMail -->
   <td class="en know">37.04 ± 1.33 / 52.33 ± 1.02</td> <!-- MMLU -->
   <td class="en reason">23.54 ± 2.08 / 40.78 ± 1.59</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.2.0</td> <!-- MMLU version -->
   <td>12.2.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/phi-2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,472 ± 885 / 728 ± 239</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="en ner">49.16 ± 3.09 / 43.10 ± 2.58</td> <!-- CoNLL-en -->
   <td class="en sent">62.41 ± 1.51 / 67.24 ± 1.18</td> <!-- SST5 -->
   <td class="en la">12.31 ± 2.96 / 48.73 ± 5.08</td> <!-- ScaLA-en -->
   <td class="en qa">75.79 ± 1.88 / 86.40 ± 1.10</td> <!-- SQuAD -->
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
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">69.82 ± 2.49 / 81.43 ± 1.73</td> <!-- SQuAD -->
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
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="en ner">53.39 ± 2.97 / 47.76 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">65.21 ± 1.35 / 65.73 ± 1.61</td> <!-- SST5 -->
   <td class="en la">12.63 ± 2.60 / 50.10 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en qa">65.74 ± 2.31 / 77.95 ± 1.84</td> <!-- SQuAD -->
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
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="en ner">37.22 ± 3.24 / 34.07 ± 3.11</td> <!-- CoNLL-en -->
   <td class="en sent">64.34 ± 1.18 / 62.90 ± 1.36</td> <!-- SST5 -->
   <td class="en la">15.30 ± 1.17 / 55.67 ± 1.16</td> <!-- ScaLA-en -->
   <td class="en qa">64.41 ± 1.29 / 75.79 ± 0.97</td> <!-- SQuAD -->
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
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">2.41</td> <!-- ScandEval rank -->
   <td class="en ner">37.80 ± 3.14 / 37.17 ± 2.80</td> <!-- CoNLL-en -->
   <td class="en sent">55.33 ± 1.77 / 64.53 ± 0.70</td> <!-- SST5 -->
   <td class="en la">11.23 ± 1.81 / 52.85 ± 2.65</td> <!-- ScaLA-en -->
   <td class="en qa">60.69 ± 1.44 / 74.24 ± 0.82</td> <!-- SQuAD -->
   <td class="en summ">67.23 ± 0.14 / 18.87 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">26.84 ± 0.41 / 44.86 ± 0.31</td> <!-- MMLU -->
   <td class="en reason">23.89 ± 1.20 / 42.78 ± 0.95</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>11.0.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.5.0</td> <!-- SQuAD version -->
   <td>12.5.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="en ner">19.00 ± 5.82 / 17.02 ± 5.30</td> <!-- CoNLL-en -->
   <td class="en sent">62.14 ± 1.16 / 67.81 ± 0.65</td> <!-- SST5 -->
   <td class="en la">8.30 ± 1.63 / 45.01 ± 3.82</td> <!-- ScaLA-en -->
   <td class="en qa">66.30 ± 1.42 / 77.75 ± 0.63</td> <!-- SQuAD -->
   <td class="en summ">66.51 ± 0.85 / 21.76 ± 0.84</td> <!-- CNN-DailyMail -->
   <td class="en know">20.38 ± 0.82 / 38.44 ± 0.70</td> <!-- MMLU -->
   <td class="en reason">7.41 ± 1.01 / 29.08 ± 0.61</td> <!-- HellaSwag -->
   <td>12.3.2</td> <!-- CoNLL-en version -->
   <td>12.1.0</td> <!-- SST5 version -->
   <td>12.1.0</td> <!-- ScaLA-en version -->
   <td>12.1.0</td> <!-- SQuAD version -->
   <td>12.1.0</td> <!-- CNN-DailyMail version -->
   <td>12.1.0</td> <!-- MMLU version -->
   <td>12.1.0</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">2.70</td> <!-- ScandEval rank -->
   <td class="en ner">40.05 ± 2.56 / 33.77 ± 1.94</td> <!-- CoNLL-en -->
   <td class="en sent">48.83 ± 1.00 / 60.88 ± 0.70</td> <!-- SST5 -->
   <td class="en la">5.83 ± 1.52 / 50.74 ± 1.73</td> <!-- ScaLA-en -->
   <td class="en qa">63.77 ± 1.40 / 76.59 ± 0.77</td> <!-- SQuAD -->
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
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="en ner">37.51 ± 1.56 / 33.24 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">57.15 ± 2.35 / 52.82 ± 1.40</td> <!-- SST5 -->
   <td class="en la">2.94 ± 2.00 / 44.53 ± 3.65</td> <!-- ScaLA-en -->
   <td class="en qa">42.57 ± 1.97 / 55.17 ± 1.29</td> <!-- SQuAD -->
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
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="en ner">33.86 ± 2.16 / 32.80 ± 2.21</td> <!-- CoNLL-en -->
   <td class="en sent">55.41 ± 2.17 / 54.48 ± 1.65</td> <!-- SST5 -->
   <td class="en la">1.15 ± 1.81 / 34.47 ± 1.12</td> <!-- ScaLA-en -->
   <td class="en qa">53.34 ± 1.21 / 64.09 ± 1.26</td> <!-- SQuAD -->
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
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en qa">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
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
   <td class="max_sequence_length">2304</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="en ner">38.23 ± 3.10 / 36.38 ± 2.60</td> <!-- CoNLL-en -->
   <td class="en sent">60.70 ± 1.80 / 66.82 ± 1.12</td> <!-- SST5 -->
   <td class="en la">-0.19 ± 2.28 / 38.77 ± 3.32</td> <!-- ScaLA-en -->
   <td class="en qa">61.93 ± 1.98 / 73.71 ± 1.57</td> <!-- SQuAD -->
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
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2304</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.50</td> <!-- ScandEval rank -->
   <td class="en ner">26.47 ± 6.25 / 28.27 ± 5.35</td> <!-- CoNLL-en -->
   <td class="en sent">60.05 ± 3.94 / 56.18 ± 1.90</td> <!-- SST5 -->
   <td class="en la">0.72 ± 1.90 / 42.84 ± 3.50</td> <!-- ScaLA-en -->
   <td class="en qa">43.87 ± 2.49 / 55.59 ± 2.44</td> <!-- SQuAD -->
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
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.49 ± 2.08 / 50.69 ± 1.88</td> <!-- SQuAD -->
   <td class="en summ">60.11 ± 1.39 / 16.29 ± 0.69</td> <!-- CNN-DailyMail -->
   <td class="en know">3.71 ± 0.75 / 28.35 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">0.62 ± 0.99 / 24.68 ± 0.55</td> <!-- HellaSwag -->
   <td>9.3.1</td> <!-- CoNLL-en version -->
   <td>9.3.1</td> <!-- SST5 version -->
   <td>9.3.1</td> <!-- ScaLA-en version -->
   <td>12.4.0</td> <!-- SQuAD version -->
   <td>9.3.1</td> <!-- CNN-DailyMail version -->
   <td>9.3.1</td> <!-- MMLU version -->
   <td>9.3.1</td> <!-- HellaSwag version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.32</td> <!-- ScandEval rank -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en qa">0.00 ± 0.00 / 3.68 ± 0.43</td> <!-- SQuAD -->
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
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.69</td> <!-- ScandEval rank -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en qa">5.58 ± 3.10 / 11.12 ± 4.66</td> <!-- SQuAD -->
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
  <a href="https://scandeval.com/english-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;English NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-TSn2m&quot; src=&quot;https://datawrapper.dwcdn.net/TSn2m/954/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
