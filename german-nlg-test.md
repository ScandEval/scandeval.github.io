---
layout: leaderboard
title: German NLG
---

<center>Last updated: 06/04/2024 13:19:15 CET</center>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
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
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.20</td> <!-- ScandEval rank -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
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
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de qa">25.22 ± 3.76 / 60.93 ± 2.96</td> <!-- GermanQuAD -->
   <td class="de summ">67.31 ± 1.05 / 24.72 ± 2.95</td> <!-- MLSum -->
   <td class="de know">35.84 ± 2.16 / 51.64 ± 1.56</td> <!-- MMLU-de -->
   <td class="de reason">49.13 ± 2.71 / 61.68 ± 2.03</td> <!-- HellaSwag-de -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>9.3.2</td> <!-- GermanQuAD version -->
   <td>9.3.2</td> <!-- MLSum version -->
   <td>9.3.2</td> <!-- MMLU-de version -->
   <td>9.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="de ner">55.76 ± 1.16 / 40.04 ± 3.21</td> <!-- GermEval -->
   <td class="de sent">55.91 ± 2.49 / 70.31 ± 1.76</td> <!-- SB10k -->
   <td class="de la">22.47 ± 3.37 / 56.77 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">35.95 ± 1.89 / 66.86 ± 2.33</td> <!-- GermanQuAD -->
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
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
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
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="de ner">48.11 ± 2.01 / 39.66 ± 3.29</td> <!-- GermEval -->
   <td class="de sent">54.96 ± 2.69 / 69.64 ± 2.09</td> <!-- SB10k -->
   <td class="de la">21.57 ± 4.18 / 55.63 ± 4.56</td> <!-- ScaLA-de -->
   <td class="de qa">31.49 ± 3.11 / 61.33 ± 3.41</td> <!-- GermanQuAD -->
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
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="de ner">50.46 ± 2.44 / 41.15 ± 3.05</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de qa">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td class="de summ">69.43 ± 0.97 / 29.48 ± 2.59</td> <!-- MLSum -->
   <td class="de know">32.56 ± 1.16 / 49.02 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">23.61 ± 2.42 / 41.55 ± 2.14</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
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
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,070 ± 1,042 / 1,769 ± 573</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="de ner">48.92 ± 3.09 / 38.74 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">52.57 ± 1.74 / 61.25 ± 2.84</td> <!-- SB10k -->
   <td class="de la">20.74 ± 3.20 / 56.59 ± 3.27</td> <!-- ScaLA-de -->
   <td class="de qa">32.87 ± 1.83 / 62.31 ± 2.13</td> <!-- GermanQuAD -->
   <td class="de summ">68.88 ± 0.80 / 27.84 ± 2.07</td> <!-- MLSum -->
   <td class="de know">31.38 ± 0.94 / 48.36 ± 0.62</td> <!-- MMLU-de -->
   <td class="de reason">29.83 ± 1.76 / 46.77 ± 1.39</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
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
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,065 ± 1,038 / 1,766 ± 570</td> <!-- Model inference speed -->
   <td class="rank">1.73</td> <!-- ScandEval rank -->
   <td class="de ner">48.50 ± 3.37 / 38.85 ± 2.26</td> <!-- GermEval -->
   <td class="de sent">52.51 ± 1.72 / 61.27 ± 2.77</td> <!-- SB10k -->
   <td class="de la">20.36 ± 3.59 / 56.14 ± 3.61</td> <!-- ScaLA-de -->
   <td class="de qa">32.88 ± 1.78 / 62.19 ± 2.05</td> <!-- GermanQuAD -->
   <td class="de summ">68.82 ± 0.81 / 27.89 ± 2.09</td> <!-- MLSum -->
   <td class="de know">31.36 ± 0.96 / 48.34 ± 0.63</td> <!-- MMLU-de -->
   <td class="de reason">29.98 ± 1.64 / 46.82 ± 1.33</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.3.2</td> <!-- SB10k version -->
   <td>12.3.2</td> <!-- ScaLA-de version -->
   <td>12.3.2</td> <!-- GermanQuAD version -->
   <td>12.3.2</td> <!-- MLSum version -->
   <td>12.3.2</td> <!-- MMLU-de version -->
   <td>12.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="de ner">55.15 ± 1.17 / 41.83 ± 1.49</td> <!-- GermEval -->
   <td class="de sent">47.85 ± 2.29 / 65.02 ± 1.69</td> <!-- SB10k -->
   <td class="de la">24.29 ± 2.18 / 60.90 ± 1.65</td> <!-- ScaLA-de -->
   <td class="de qa">24.00 ± 2.19 / 57.66 ± 1.94</td> <!-- GermanQuAD -->
   <td class="de summ">67.54 ± 0.72 / 22.69 ± 1.75</td> <!-- MLSum -->
   <td class="de know">25.96 ± 1.60 / 44.05 ± 1.25</td> <!-- MMLU-de -->
   <td class="de reason">31.06 ± 1.24 / 47.46 ± 0.90</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.2.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.2</td> <!-- MMLU-de version -->
   <td>9.3.2</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="de ner">47.74 ± 1.95 / 41.60 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de qa">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td class="de summ">69.31 ± 0.68 / 28.27 ± 1.70</td> <!-- MLSum -->
   <td class="de know">32.49 ± 0.91 / 48.82 ± 0.70</td> <!-- MMLU-de -->
   <td class="de reason">22.25 ± 2.13 / 40.28 ± 1.67</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.2.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="merged-model">
   <td>mayflowergmbh/Wiedervereinigung-7b-dpo (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,374 ± 432 / 744 ± 230</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="de ner">53.57 ± 3.49 / 40.72 ± 3.06</td> <!-- GermEval -->
   <td class="de sent">51.92 ± 3.19 / 67.12 ± 2.11</td> <!-- SB10k -->
   <td class="de la">29.06 ± 5.04 / 62.77 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de qa">14.59 ± 2.77 / 50.41 ± 3.79</td> <!-- GermanQuAD -->
   <td class="de summ">63.78 ± 0.48 / 15.45 ± 0.60</td> <!-- MLSum -->
   <td class="de know">35.38 ± 1.08 / 51.48 ± 0.84</td> <!-- MMLU-de -->
   <td class="de reason">34.16 ± 3.12 / 49.73 ± 2.20</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="de ner">56.71 ± 1.34 / 47.69 ± 2.04</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.03 / 62.42 ± 3.31</td> <!-- SB10k -->
   <td class="de la">19.92 ± 3.22 / 52.83 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de qa">27.87 ± 2.01 / 57.64 ± 2.05</td> <!-- GermanQuAD -->
   <td class="de summ">66.93 ± 0.93 / 24.06 ± 2.22</td> <!-- MLSum -->
   <td class="de know">26.02 ± 1.00 / 44.42 ± 0.74</td> <!-- MMLU-de -->
   <td class="de reason">24.88 ± 1.44 / 43.25 ± 1.25</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,467 ± 656 / 986 ± 297</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="de ner">4.73 ± 2.55 / 4.53 ± 2.26</td> <!-- GermEval -->
   <td class="de sent">52.36 ± 2.24 / 67.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">24.27 ± 2.29 / 59.60 ± 3.10</td> <!-- ScaLA-de -->
   <td class="de qa">31.57 ± 2.96 / 59.99 ± 3.89</td> <!-- GermanQuAD -->
   <td class="de summ">69.01 ± 1.14 / 28.41 ± 2.35</td> <!-- MLSum -->
   <td class="de know">34.97 ± 0.62 / 51.12 ± 0.50</td> <!-- MMLU-de -->
   <td class="de reason">29.00 ± 1.78 / 45.94 ± 1.48</td> <!-- HellaSwag-de -->
   <td>12.5.1</td> <!-- GermEval version -->
   <td>12.5.1</td> <!-- SB10k version -->
   <td>12.5.1</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>12.5.1</td> <!-- MLSum version -->
   <td>12.5.1</td> <!-- MMLU-de version -->
   <td>12.5.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="de ner">51.79 ± 0.92 / 36.09 ± 1.73</td> <!-- GermEval -->
   <td class="de sent">47.27 ± 3.06 / 63.50 ± 2.88</td> <!-- SB10k -->
   <td class="de la">22.15 ± 1.83 / 56.64 ± 4.04</td> <!-- ScaLA-de -->
   <td class="de qa">24.35 ± 3.75 / 54.56 ± 4.42</td> <!-- GermanQuAD -->
   <td class="de summ">67.79 ± 1.11 / 25.91 ± 2.97</td> <!-- MLSum -->
   <td class="de know">26.88 ± 0.94 / 44.64 ± 0.79</td> <!-- MMLU-de -->
   <td class="de reason">20.34 ± 1.39 / 39.65 ± 0.94</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="de ner">44.97 ± 1.75 / 35.79 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">53.14 ± 2.67 / 67.89 ± 2.15</td> <!-- SB10k -->
   <td class="de la">7.64 ± 2.47 / 37.95 ± 2.67</td> <!-- ScaLA-de -->
   <td class="de qa">30.19 ± 1.61 / 57.19 ± 2.48</td> <!-- GermanQuAD -->
   <td class="de summ">66.27 ± 1.20 / 22.97 ± 2.48</td> <!-- MLSum -->
   <td class="de know">29.80 ± 0.81 / 47.29 ± 0.57</td> <!-- MMLU-de -->
   <td class="de reason">22.91 ± 1.13 / 41.18 ± 1.10</td> <!-- HellaSwag-de -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>10.0.0</td> <!-- SB10k version -->
   <td>10.0.0</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>12.0.0</td> <!-- MLSum version -->
   <td>10.0.1</td> <!-- MMLU-de version -->
   <td>10.0.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM_German_7b_v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,972 ± 315 / 689 ± 204</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="de ner">42.48 ± 2.68 / 32.20 ± 1.31</td> <!-- GermEval -->
   <td class="de sent">48.67 ± 3.85 / 59.21 ± 4.18</td> <!-- SB10k -->
   <td class="de la">8.72 ± 2.15 / 43.37 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">36.12 ± 2.35 / 66.54 ± 2.34</td> <!-- GermanQuAD -->
   <td class="de summ">68.47 ± 1.27 / 26.03 ± 3.68</td> <!-- MLSum -->
   <td class="de know">23.99 ± 1.15 / 41.69 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">20.76 ± 1.28 / 38.13 ± 1.29</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.27</td> <!-- ScandEval rank -->
   <td class="de ner">50.00 ± 1.33 / 38.45 ± 1.68</td> <!-- GermEval -->
   <td class="de sent">46.54 ± 2.92 / 63.66 ± 2.14</td> <!-- SB10k -->
   <td class="de la">15.30 ± 1.79 / 55.12 ± 1.92</td> <!-- ScaLA-de -->
   <td class="de qa">25.57 ± 3.59 / 56.09 ± 3.74</td> <!-- GermanQuAD -->
   <td class="de summ">67.61 ± 0.90 / 23.51 ± 2.44</td> <!-- MLSum -->
   <td class="de know">20.13 ± 1.16 / 39.49 ± 1.04</td> <!-- MMLU-de -->
   <td class="de reason">13.92 ± 1.52 / 34.03 ± 1.27</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="de ner">41.88 ± 1.87 / 31.88 ± 1.77</td> <!-- GermEval -->
   <td class="de sent">50.17 ± 2.52 / 65.78 ± 1.89</td> <!-- SB10k -->
   <td class="de la">15.82 ± 2.45 / 53.27 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">28.56 ± 5.07 / 55.55 ± 6.16</td> <!-- GermanQuAD -->
   <td class="de summ">68.67 ± 0.97 / 26.95 ± 1.81</td> <!-- MLSum -->
   <td class="de know">18.43 ± 1.34 / 38.16 ± 1.18</td> <!-- MMLU-de -->
   <td class="de reason">8.37 ± 1.83 / 30.00 ± 1.48</td> <!-- HellaSwag-de -->
   <td>9.2.0</td> <!-- GermEval version -->
   <td>9.2.0</td> <!-- SB10k version -->
   <td>9.2.0</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>11.0.0</td> <!-- MLSum version -->
   <td>9.2.0</td> <!-- MMLU-de version -->
   <td>9.2.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="de ner">31.51 ± 8.45 / 28.51 ± 7.54</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de qa">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td class="de summ">65.56 ± 1.65 / 20.45 ± 2.68</td> <!-- MLSum -->
   <td class="de know">23.76 ± 0.70 / 42.77 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">20.92 ± 1.16 / 40.56 ± 0.86</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="de ner">39.09 ± 2.92 / 31.71 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">47.83 ± 2.81 / 60.24 ± 3.30</td> <!-- SB10k -->
   <td class="de la">10.31 ± 2.60 / 46.65 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">26.13 ± 3.79 / 53.13 ± 4.50</td> <!-- GermanQuAD -->
   <td class="de summ">66.72 ± 1.03 / 23.80 ± 2.02</td> <!-- MLSum -->
   <td class="de know">19.03 ± 1.31 / 36.85 ± 1.79</td> <!-- MMLU-de -->
   <td class="de reason">10.10 ± 1.81 / 30.36 ± 1.81</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="de ner">21.52 ± 6.77 / 20.73 ± 6.40</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de qa">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td class="de summ">65.88 ± 1.25 / 21.37 ± 1.87</td> <!-- MLSum -->
   <td class="de know">21.32 ± 1.14 / 40.66 ± 0.96</td> <!-- MMLU-de -->
   <td class="de reason">21.35 ± 0.89 / 40.77 ± 0.65</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="de ner">34.53 ± 1.35 / 26.72 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de qa">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td class="de summ">63.02 ± 2.00 / 19.54 ± 1.33</td> <!-- MLSum -->
   <td class="de know">12.27 ± 1.33 / 33.40 ± 1.08</td> <!-- MMLU-de -->
   <td class="de reason">6.57 ± 0.74 / 28.60 ± 0.70</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="de ner">14.07 ± 3.23 / 13.30 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td class="de summ">66.80 ± 0.96 / 22.24 ± 1.37</td> <!-- MLSum -->
   <td class="de know">12.11 ± 0.94 / 33.12 ± 0.90</td> <!-- MMLU-de -->
   <td class="de reason">7.32 ± 1.40 / 30.11 ± 1.16</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   <td>12.1.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="de ner">26.77 ± 2.51 / 22.36 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de qa">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td class="de summ">61.47 ± 1.67 / 12.62 ± 1.40</td> <!-- MLSum -->
   <td class="de know">13.44 ± 1.22 / 34.26 ± 0.98</td> <!-- MMLU-de -->
   <td class="de reason">8.31 ± 1.08 / 31.05 ± 0.84</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   <td>12.5.0</td> <!-- MLSum version -->
   <td>12.1.0</td> <!-- MMLU-de version -->
   <td>12.1.0</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="de ner">35.78 ± 2.37 / 26.98 ± 1.75</td> <!-- GermEval -->
   <td class="de sent">34.13 ± 7.00 / 46.96 ± 8.23</td> <!-- SB10k -->
   <td class="de la">2.18 ± 1.60 / 38.27 ± 3.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.99 ± 4.02 / 38.26 ± 5.37</td> <!-- GermanQuAD -->
   <td class="de summ">62.21 ± 0.48 / 18.52 ± 0.80</td> <!-- MLSum -->
   <td class="de know">3.58 ± 1.15 / 27.49 ± 0.72</td> <!-- MMLU-de -->
   <td class="de reason">0.56 ± 1.62 / 24.97 ± 1.14</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>9.3.1</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.19</td> <!-- ScandEval rank -->
   <td class="de ner">6.64 ± 2.06 / 9.38 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de qa">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td class="de summ">61.74 ± 1.58 / 14.71 ± 1.12</td> <!-- MLSum -->
   <td class="de know">13.65 ± 1.17 / 33.35 ± 0.91</td> <!-- MMLU-de -->
   <td class="de reason">8.86 ± 0.99 / 30.21 ± 0.77</td> <!-- HellaSwag-de -->
   <td>12.3.2</td> <!-- GermEval version -->
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
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.37</td> <!-- ScandEval rank -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.54 ± 5.12 / 49.63 ± 5.78</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.44 ± 3.30 / 45.51 ± 3.32</td> <!-- GermanQuAD -->
   <td class="de summ">60.50 ± 0.63 / 13.71 ± 0.75</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   <td>12.4.0</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de qa">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
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
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.61</td> <!-- ScandEval rank -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de qa">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
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
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.18</td> <!-- ScandEval rank -->
   <td class="de ner">21.46 ± 2.04 / 20.83 ± 1.63</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de qa">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
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
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.19</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 14.61 ± 0.65</td> <!-- GermanQuAD -->
   <td class="de summ">59.43 ± 0.04 / 10.87 ± 0.07</td> <!-- MLSum -->
   <td class="de know">1.16 ± 0.57 / 22.46 ± 0.56</td> <!-- MMLU-de -->
   <td class="de reason">0.31 ± 0.50 / 24.18 ± 0.53</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>9.3.1</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>9.3.1</td> <!-- MLSum version -->
   <td>9.3.1</td> <!-- MMLU-de version -->
   <td>9.3.1</td> <!-- HellaSwag-de version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.71</td> <!-- ScandEval rank -->
   <td class="de ner">0.30 ± 0.60 / 0.26 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">0.29 ± 1.28 / 17.22 ± 1.25</td> <!-- SB10k -->
   <td class="de la">-0.11 ± 1.16 / 36.65 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.54 ± 0.12</td> <!-- GermanQuAD -->
   <td class="de summ">29.53 ± 0.57 / 1.46 ± 0.22</td> <!-- MLSum -->
   <td class="de know">-0.60 ± 1.00 / 22.86 ± 0.47</td> <!-- MMLU-de -->
   <td class="de reason">0.61 ± 1.22 / 24.32 ± 0.63</td> <!-- HellaSwag-de -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>11.0.0</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   <td>12.0.0</td> <!-- MLSum version -->
   <td>11.0.0</td> <!-- MMLU-de version -->
   <td>11.0.0</td> <!-- HellaSwag-de version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;German NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-1EiJY&quot; src=&quot;https://datawrapper.dwcdn.net/1EiJY/943/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
