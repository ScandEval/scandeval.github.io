---
layout: leaderboard
title: Dutch NLG
---

<center>Last updated: 06/02/2024 12:55:20 CET</center>

<div class="table-wrapper centered">

<input type="checkbox" id="merged-models-checkbox">
<label for="merged-models-checkbox">Include merged models</label>

<table id="dutch-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch question answering - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch summarization - BERTScore / ROUGE-L">Wiki-Lingua-NL</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">ARC-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-nl</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td class="rank">1</td> <!-- Rank -->
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="score">54.17 ± 2.88</td> <!-- ScandEval score -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl qa">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.13 ± 0.41 / 21.32 ± 0.75</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.28 ± 2.88 / 56.45 ± 2.26</td> <!-- MMLU-nl -->
   <td class="nl know">70.26 ± 3.35 / 77.66 ± 2.55</td> <!-- ARC-nl -->
   <td class="nl reason">61.52 ± 2.69 / 70.62 ± 2.20</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">39.08 ± 1.71</td> <!-- ScandEval score -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl qa">50.14 ± 2.64 / 59.42 ± 3.10</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.53 ± 0.85 / 19.96 ± 1.00</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.49 ± 0.57 / 51.51 ± 0.42</td> <!-- MMLU-nl -->
   <td class="nl know">57.52 ± 1.13 / 68.17 ± 0.86</td> <!-- ARC-nl -->
   <td class="nl reason">19.88 ± 1.80 / 39.13 ± 1.56</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">36.51 ± 2.02</td> <!-- ScandEval score -->
   <td class="nl ner">47.53 ± 1.90 / 32.42 ± 1.99</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.36 ± 2.96 / 28.11 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">30.67 ± 4.45 / 63.78 ± 2.80</td> <!-- ScaLA-nl -->
   <td class="nl qa">56.55 ± 0.70 / 67.56 ± 0.60</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.58 ± 0.85 / 22.14 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.12 ± 0.98 / 44.50 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl know">46.22 ± 0.75 / 59.41 ± 0.62</td> <!-- ARC-nl -->
   <td class="nl reason">11.70 ± 2.42 / 32.05 ± 1.90</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">34.76 ± 1.53</td> <!-- ScandEval score -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl qa">52.74 ± 0.82 / 67.11 ± 1.04</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.56 ± 0.63 / 18.08 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.06 ± 0.77 / 44.08 ± 0.51</td> <!-- MMLU-nl -->
   <td class="nl know">37.94 ± 1.16 / 53.23 ± 0.93</td> <!-- ARC-nl -->
   <td class="nl reason">14.26 ± 1.48 / 35.14 ± 1.18</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">32.99 ± 1.39</td> <!-- ScandEval score -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl qa">53.41 ± 0.79 / 66.24 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.83 ± 0.37 / 19.21 ± 0.42</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.19 ± 1.26 / 39.24 ± 1.03</td> <!-- MMLU-nl -->
   <td class="nl know">26.26 ± 1.73 / 44.67 ± 1.29</td> <!-- ARC-nl -->
   <td class="nl reason">11.42 ± 1.29 / 32.50 ± 1.10</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">27.88 ± 2.09</td> <!-- ScandEval score -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.51 ± 2.13 / 44.59 ± 2.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.20 ± 0.99 / 18.78 ± 0.94</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.36 ± 1.12 / 37.44 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl know">23.70 ± 1.11 / 41.80 ± 1.08</td> <!-- ARC-nl -->
   <td class="nl reason">6.68 ± 1.82 / 29.30 ± 1.02</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">23.00 ± 2.01</td> <!-- ScandEval score -->
   <td class="nl ner">35.30 ± 3.76 / 33.68 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.67 ± 2.21 / 31.30 ± 4.51</td> <!-- Dutch Social -->
   <td class="nl la">1.76 ± 2.37 / 47.60 ± 1.68</td> <!-- ScaLA-nl -->
   <td class="nl qa">45.05 ± 1.68 / 55.38 ± 1.66</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.15 ± 1.54 / 14.60 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">6.24 ± 1.54 / 29.02 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl know">1.00 ± 1.09 / 25.73 ± 0.99</td> <!-- ARC-nl -->
   <td class="nl reason">0.47 ± 1.20 / 24.89 ± 0.59</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">22.00 ± 1.60</td> <!-- ScandEval score -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl qa">37.61 ± 1.36 / 47.48 ± 1.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.24 ± 0.86 / 15.62 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.41 ± 1.15 / 27.75 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl know">3.88 ± 1.25 / 28.13 ± 0.79</td> <!-- ARC-nl -->
   <td class="nl reason">0.15 ± 0.98 / 25.59 ± 0.57</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">8.72 ± 0.35</td> <!-- ScandEval score -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.95 ± 1.17 / 9.87 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.00 ± 0.00 / 5.46 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.14 ± 0.15 / 10.07 ± 0.16</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.11 ± 0.64 / 24.32 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl know">0.00 ± 0.00 / 22.85 ± 0.60</td> <!-- ARC-nl -->
   <td class="nl reason">-0.13 ± 0.82 / 23.60 ± 0.33</td> <!-- HellaSwag-nl -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">5.18 ± 0.51</td> <!-- ScandEval score -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.00 ± 0.00 / 8.62 ± 0.30</td> <!-- Dutch Social -->
   <td class="nl la">0.15 ± 1.46 / 44.90 ± 4.37</td> <!-- ScaLA-nl -->
   <td class="nl qa">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">34.13 ± 0.14 / 3.38 ± 0.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.33 ± 1.18 / 24.67 ± 0.67</td> <!-- MMLU-nl -->
   <td class="nl know">0.83 ± 0.79 / 22.95 ± 0.63</td> <!-- ARC-nl -->
   <td class="nl reason">0.52 ± 0.55 / 23.64 ± 0.34</td> <!-- HellaSwag-nl -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/dutch-nlg.csv" target="_blank">Download as CSV</a>
</div>