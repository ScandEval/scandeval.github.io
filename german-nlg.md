---
layout: leaderboard
title: German NLG
---

<center>Last updated: 07/02/2024 11:08:10 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="german-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German question answering - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German summarization - BERTScore / ROUGE-L">MLSum</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German knowledge - Matthews Correlation Coefficient / Accuracy">ARC-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-de</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1=</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">51.56 ± 2.47</td> <!-- ScandEval score -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de qa">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td class="de summ">64.90 ± 0.22 / 15.99 ± 0.32</td> <!-- MLSum -->
   <td class="de know">35.39 ± 3.89 / 51.41 ± 2.98</td> <!-- MMLU-de -->
   <td class="de know">70.58 ± 2.18 / 77.93 ± 1.65</td> <!-- ARC-de -->
   <td class="de reason">56.88 ± 2.50 / 66.76 ± 2.02</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="merged-model">
   <td class="rank">1=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">49.03 ± 2.87</td> <!-- ScandEval score -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de qa">25.22 ± 3.76 / 60.93 ± 2.96</td> <!-- GermanQuAD -->
   <td class="de summ">67.31 ± 1.05 / 24.72 ± 2.95</td> <!-- MLSum -->
   <td class="de know">35.84 ± 2.16 / 51.64 ± 1.56</td> <!-- MMLU-de -->
   <td class="de know">64.31 ± 2.19 / 73.28 ± 1.65</td> <!-- ARC-de -->
   <td class="de reason">49.13 ± 2.71 / 61.68 ± 2.03</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">42.69 ± 2.01</td> <!-- ScandEval score -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">22.94 ± 3.05 / 47.19 ± 4.45</td> <!-- GermanQuAD -->
   <td class="de summ">68.72 ± 0.87 / 28.11 ± 2.14</td> <!-- MLSum -->
   <td class="de know">35.63 ± 1.12 / 51.69 ± 0.85</td> <!-- MMLU-de -->
   <td class="de know">60.46 ± 1.23 / 70.30 ± 0.94</td> <!-- ARC-de -->
   <td class="de reason">26.40 ± 1.86 / 43.98 ± 1.58</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="score">40.03 ± 1.71</td> <!-- ScandEval score -->
   <td class="de ner">56.71 ± 1.34 / 47.69 ± 2.04</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.03 / 62.42 ± 3.31</td> <!-- SB10k -->
   <td class="de la">19.92 ± 3.22 / 52.83 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de qa">27.87 ± 2.01 / 57.64 ± 2.05</td> <!-- GermanQuAD -->
   <td class="de summ">66.93 ± 0.93 / 24.06 ± 2.22</td> <!-- MLSum -->
   <td class="de know">26.02 ± 1.00 / 44.42 ± 0.74</td> <!-- MMLU-de -->
   <td class="de know">42.29 ± 1.06 / 56.71 ± 0.82</td> <!-- ARC-de -->
   <td class="de reason">24.88 ± 1.44 / 43.25 ± 1.25</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">38.53 ± 1.91</td> <!-- ScandEval score -->
   <td class="de ner">51.79 ± 0.92 / 36.09 ± 1.73</td> <!-- GermEval -->
   <td class="de sent">47.27 ± 3.06 / 63.50 ± 2.88</td> <!-- SB10k -->
   <td class="de la">22.15 ± 1.83 / 56.64 ± 4.04</td> <!-- ScaLA-de -->
   <td class="de qa">24.30 ± 3.79 / 54.51 ± 4.48</td> <!-- GermanQuAD -->
   <td class="de summ">67.96 ± 1.05 / 26.56 ± 2.90</td> <!-- MLSum -->
   <td class="de know">26.88 ± 0.94 / 44.64 ± 0.79</td> <!-- MMLU-de -->
   <td class="de know">44.97 ± 1.73 / 58.53 ± 1.31</td> <!-- ARC-de -->
   <td class="de reason">20.34 ± 1.39 / 39.65 ± 0.94</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">34.81 ± 1.88</td> <!-- ScandEval score -->
   <td class="de ner">50.00 ± 1.33 / 38.45 ± 1.68</td> <!-- GermEval -->
   <td class="de sent">46.54 ± 2.92 / 63.66 ± 2.14</td> <!-- SB10k -->
   <td class="de la">15.30 ± 1.79 / 55.12 ± 1.92</td> <!-- ScaLA-de -->
   <td class="de qa">25.57 ± 3.57 / 56.05 ± 3.74</td> <!-- GermanQuAD -->
   <td class="de summ">67.66 ± 0.90 / 23.98 ± 2.48</td> <!-- MLSum -->
   <td class="de know">20.13 ± 1.16 / 39.49 ± 1.04</td> <!-- MMLU-de -->
   <td class="de know">29.29 ± 1.06 / 46.55 ± 0.89</td> <!-- ARC-de -->
   <td class="de reason">13.92 ± 1.52 / 34.03 ± 1.27</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">32.26 ± 2.33</td> <!-- ScandEval score -->
   <td class="de ner">39.09 ± 2.92 / 31.71 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">47.83 ± 2.81 / 60.24 ± 3.30</td> <!-- SB10k -->
   <td class="de la">10.31 ± 2.60 / 46.65 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">26.13 ± 3.79 / 53.13 ± 4.50</td> <!-- GermanQuAD -->
   <td class="de summ">66.72 ± 1.03 / 23.80 ± 2.02</td> <!-- MLSum -->
   <td class="de know">19.03 ± 1.31 / 36.85 ± 1.79</td> <!-- MMLU-de -->
   <td class="de know">32.26 ± 1.36 / 47.72 ± 1.23</td> <!-- ARC-de -->
   <td class="de reason">10.10 ± 1.81 / 30.36 ± 1.81</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">32.23 ± 1.99</td> <!-- ScandEval score -->
   <td class="de ner">41.88 ± 1.87 / 31.88 ± 1.77</td> <!-- GermEval -->
   <td class="de sent">50.17 ± 2.52 / 65.78 ± 1.89</td> <!-- SB10k -->
   <td class="de la">15.82 ± 2.45 / 53.27 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">18.35 ± 2.70 / 39.71 ± 4.79</td> <!-- GermanQuAD -->
   <td class="de summ">68.99 ± 1.06 / 28.97 ± 2.45</td> <!-- MLSum -->
   <td class="de know">18.43 ± 1.34 / 38.16 ± 1.18</td> <!-- MMLU-de -->
   <td class="de know">25.68 ± 1.63 / 43.75 ± 1.33</td> <!-- ARC-de -->
   <td class="de reason">8.37 ± 1.83 / 30.00 ± 1.48</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">22.22 ± 2.66</td> <!-- ScandEval score -->
   <td class="de ner">35.78 ± 2.37 / 26.98 ± 1.75</td> <!-- GermEval -->
   <td class="de sent">34.13 ± 7.00 / 46.96 ± 8.23</td> <!-- SB10k -->
   <td class="de la">2.18 ± 1.60 / 38.27 ± 3.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.99 ± 4.02 / 38.26 ± 5.37</td> <!-- GermanQuAD -->
   <td class="de summ">62.21 ± 0.48 / 18.52 ± 0.80</td> <!-- MLSum -->
   <td class="de know">3.58 ± 1.15 / 27.49 ± 0.72</td> <!-- MMLU-de -->
   <td class="de know">1.87 ± 1.88 / 26.56 ± 1.16</td> <!-- ARC-de -->
   <td class="de reason">0.56 ± 1.62 / 24.97 ± 1.14</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">20.36 ± 1.91</td> <!-- ScandEval score -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.54 ± 5.12 / 49.63 ± 5.78</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.40 ± 3.28 / 45.47 ± 3.32</td> <!-- GermanQuAD -->
   <td class="de summ">62.18 ± 0.62 / 16.27 ± 1.10</td> <!-- MLSum -->
   <td class="de know">-0.10 ± 0.93 / 25.16 ± 1.17</td> <!-- MMLU-de -->
   <td class="de know">-0.37 ± 1.14 / 24.56 ± 0.85</td> <!-- ARC-de -->
   <td class="de reason">-1.00 ± 1.03 / 24.94 ± 1.00</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">8.62 ± 0.12</td> <!-- ScandEval score -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 14.60 ± 0.67</td> <!-- GermanQuAD -->
   <td class="de summ">59.43 ± 0.04 / 10.87 ± 0.07</td> <!-- MLSum -->
   <td class="de know">1.16 ± 0.57 / 22.46 ± 0.56</td> <!-- MMLU-de -->
   <td class="de know">0.00 ± 0.00 / 23.37 ± 0.91</td> <!-- ARC-de -->
   <td class="de reason">0.31 ± 0.50 / 24.18 ± 0.53</td> <!-- HellaSwag-de -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8=</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">4.68 ± 0.67</td> <!-- ScandEval score -->
   <td class="de ner">0.30 ± 0.60 / 0.26 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">0.03 ± 0.44 / 17.26 ± 0.45</td> <!-- SB10k -->
   <td class="de la">0.72 ± 1.40 / 42.53 ± 3.84</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.54 ± 0.12</td> <!-- GermanQuAD -->
   <td class="de summ">30.97 ± 0.49 / 1.94 ± 0.26</td> <!-- MLSum -->
   <td class="de know">-0.35 ± 0.95 / 22.36 ± 0.43</td> <!-- MMLU-de -->
   <td class="de know">0.57 ± 0.90 / 23.42 ± 0.90</td> <!-- ARC-de -->
   <td class="de reason">0.64 ± 0.82 / 24.19 ± 0.54</td> <!-- HellaSwag-de -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlg.csv" target="_blank">Download as CSV</a>
</div>