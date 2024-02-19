---
layout: leaderboard
title: English NLG
---

<center>Last updated: 19/02/2024 17:44:35 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="english-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SST5</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-en</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English question answering - Exact Match / F1-score">SQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English summarization - BERTScore / ROUGE-L">CNN-DailyMail</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English knowledge - Matthews Correlation Coefficient / Accuracy">MMLU</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="English common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag</span></th>
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
   <td class="score">62.30 ± 2.30</td> <!-- ScandEval score -->
   <td class="en ner">71.48 ± 2.47 / 69.71 ± 1.59</td> <!-- CoNLL-en -->
   <td class="en sent">66.41 ± 2.66 / 68.72 ± 1.87</td> <!-- SST5 -->
   <td class="en la">41.43 ± 2.57 / 70.34 ± 1.35</td> <!-- ScaLA-en -->
   <td class="en qa">67.90 ± 1.61 / 85.57 ± 0.84</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.18 / 24.41 ± 0.39</td> <!-- CNN-DailyMail -->
   <td class="en know">43.69 ± 3.59 / 57.38 ± 3.06</td> <!-- MMLU -->
   <td class="en reason">75.60 ± 3.04 / 81.48 ± 2.31</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="score">58.47 ± 1.58</td> <!-- ScandEval score -->
   <td class="en ner">52.70 ± 2.29 / 48.83 ± 2.24</td> <!-- CoNLL-en -->
   <td class="en sent">68.66 ± 0.92 / 58.34 ± 0.37</td> <!-- SST5 -->
   <td class="en la">25.29 ± 4.29 / 54.31 ± 5.45</td> <!-- ScaLA-en -->
   <td class="en qa">75.83 ± 1.81 / 85.86 ± 1.01</td> <!-- SQuAD -->
   <td class="en summ">67.65 ± 0.23 / 23.26 ± 0.29</td> <!-- CNN-DailyMail -->
   <td class="en know">50.89 ± 0.77 / 63.01 ± 0.60</td> <!-- MMLU -->
   <td class="en reason">68.29 ± 0.74 / 75.90 ± 0.62</td> <!-- HellaSwag -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">58.34 ± 2.24</td> <!-- ScandEval score -->
   <td class="en ner">69.16 ± 2.80 / 57.28 ± 2.82</td> <!-- CoNLL-en -->
   <td class="en sent">63.85 ± 2.16 / 72.40 ± 1.71</td> <!-- SST5 -->
   <td class="en la">28.40 ± 3.60 / 62.70 ± 1.51</td> <!-- ScaLA-en -->
   <td class="en qa">52.69 ± 2.21 / 76.35 ± 1.25</td> <!-- SQuAD -->
   <td class="en summ">70.55 ± 0.73 / 26.32 ± 0.97</td> <!-- CNN-DailyMail -->
   <td class="en know">51.74 ± 1.82 / 63.44 ± 1.40</td> <!-- MMLU -->
   <td class="en reason">71.96 ± 2.38 / 78.87 ± 1.66</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">53.36 ± 2.39</td> <!-- ScandEval score -->
   <td class="en ner">63.40 ± 2.72 / 56.92 ± 2.17</td> <!-- CoNLL-en -->
   <td class="en sent">68.17 ± 1.33 / 70.74 ± 0.93</td> <!-- SST5 -->
   <td class="en la">30.92 ± 4.81 / 63.79 ± 4.42</td> <!-- ScaLA-en -->
   <td class="en qa">58.79 ± 1.97 / 69.65 ± 2.00</td> <!-- SQuAD -->
   <td class="en summ">69.57 ± 0.44 / 25.55 ± 0.51</td> <!-- CNN-DailyMail -->
   <td class="en know">47.74 ± 1.26 / 60.63 ± 0.97</td> <!-- MMLU -->
   <td class="en reason">34.96 ± 4.19 / 49.62 ± 3.28</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">51.92 ± 1.62</td> <!-- ScandEval score -->
   <td class="en ner">57.58 ± 2.30 / 47.94 ± 2.89</td> <!-- CoNLL-en -->
   <td class="en sent">61.44 ± 2.02 / 69.47 ± 0.98</td> <!-- SST5 -->
   <td class="en la">34.92 ± 2.40 / 66.67 ± 1.41</td> <!-- ScaLA-en -->
   <td class="en qa">65.46 ± 1.74 / 81.96 ± 0.56</td> <!-- SQuAD -->
   <td class="en summ">69.90 ± 0.35 / 25.08 ± 0.43</td> <!-- CNN-DailyMail -->
   <td class="en know">38.40 ± 0.98 / 53.43 ± 0.76</td> <!-- MMLU -->
   <td class="en reason">35.72 ± 1.56 / 49.69 ± 1.42</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="score">51.81 ± 1.91</td> <!-- ScandEval score -->
   <td class="en ner">64.93 ± 2.24 / 57.95 ± 1.24</td> <!-- CoNLL-en -->
   <td class="en sent">64.14 ± 1.61 / 68.00 ± 1.67</td> <!-- SST5 -->
   <td class="en la">28.08 ± 3.86 / 62.71 ± 2.98</td> <!-- ScaLA-en -->
   <td class="en qa">62.09 ± 1.68 / 79.57 ± 0.96</td> <!-- SQuAD -->
   <td class="en summ">68.84 ± 0.52 / 24.99 ± 0.80</td> <!-- CNN-DailyMail -->
   <td class="en know">36.49 ± 0.82 / 52.02 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">38.09 ± 2.61 / 52.60 ± 2.19</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="score">51.52 ± 1.98</td> <!-- ScandEval score -->
   <td class="en ner">62.11 ± 1.61 / 52.36 ± 2.00</td> <!-- CoNLL-en -->
   <td class="en sent">59.91 ± 2.10 / 68.92 ± 1.21</td> <!-- SST5 -->
   <td class="en la">30.66 ± 3.60 / 64.32 ± 2.03</td> <!-- ScaLA-en -->
   <td class="en qa">58.30 ± 2.09 / 77.85 ± 0.72</td> <!-- SQuAD -->
   <td class="en summ">69.80 ± 0.65 / 25.01 ± 0.78</td> <!-- CNN-DailyMail -->
   <td class="en know">34.93 ± 1.35 / 50.71 ± 1.00</td> <!-- MMLU -->
   <td class="en reason">44.91 ± 2.44 / 58.07 ± 1.93</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">48.95 ± 1.25</td> <!-- ScandEval score -->
   <td class="en ner">62.53 ± 1.35 / 53.42 ± 2.04</td> <!-- CoNLL-en -->
   <td class="en sent">62.23 ± 1.29 / 68.09 ± 1.34</td> <!-- SST5 -->
   <td class="en la">22.71 ± 1.81 / 60.79 ± 1.08</td> <!-- ScaLA-en -->
   <td class="en qa">64.54 ± 1.41 / 80.82 ± 0.81</td> <!-- SQuAD -->
   <td class="en summ">69.98 ± 0.33 / 25.77 ± 0.35</td> <!-- CNN-DailyMail -->
   <td class="en know">30.47 ± 0.70 / 46.82 ± 0.55</td> <!-- MMLU -->
   <td class="en reason">30.18 ± 1.87 / 45.85 ± 1.98</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">6</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">44.91 ± 1.93</td> <!-- ScandEval score -->
   <td class="en ner">53.39 ± 2.97 / 47.76 ± 2.67</td> <!-- CoNLL-en -->
   <td class="en sent">65.21 ± 1.35 / 65.73 ± 1.61</td> <!-- SST5 -->
   <td class="en la">12.63 ± 2.60 / 50.10 ± 3.87</td> <!-- ScaLA-en -->
   <td class="en qa">65.74 ± 2.31 / 77.95 ± 1.84</td> <!-- SQuAD -->
   <td class="en summ">68.05 ± 0.54 / 24.11 ± 0.59</td> <!-- CNN-DailyMail -->
   <td class="en know">31.65 ± 1.00 / 47.19 ± 0.83</td> <!-- MMLU -->
   <td class="en reason">17.69 ± 2.71 / 35.94 ± 2.08</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">7</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">41.75 ± 2.00</td> <!-- ScandEval score -->
   <td class="en ner">55.27 ± 2.79 / 50.25 ± 2.12</td> <!-- CoNLL-en -->
   <td class="en sent">65.16 ± 1.21 / 66.86 ± 1.32</td> <!-- SST5 -->
   <td class="en la">20.43 ± 3.69 / 55.98 ± 4.88</td> <!-- ScaLA-en -->
   <td class="en qa">44.64 ± 3.00 / 53.75 ± 3.18</td> <!-- SQuAD -->
   <td class="en summ">68.99 ± 0.60 / 24.81 ± 0.67</td> <!-- CNN-DailyMail -->
   <td class="en know">25.98 ± 0.90 / 42.52 ± 0.62</td> <!-- MMLU -->
   <td class="en reason">11.77 ± 1.81 / 31.25 ± 1.99</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">8</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">34.39 ± 2.85</td> <!-- ScandEval score -->
   <td class="en ner">45.86 ± 3.18 / 40.23 ± 2.41</td> <!-- CoNLL-en -->
   <td class="en sent">62.08 ± 3.29 / 55.11 ± 1.68</td> <!-- SST5 -->
   <td class="en la">6.62 ± 2.43 / 48.79 ± 3.77</td> <!-- ScaLA-en -->
   <td class="en qa">65.29 ± 1.81 / 77.71 ± 0.98</td> <!-- SQuAD -->
   <td class="en summ">43.45 ± 7.12 / 15.14 ± 2.47</td> <!-- CNN-DailyMail -->
   <td class="en know">9.10 ± 1.33 / 30.31 ± 0.94</td> <!-- MMLU -->
   <td class="en reason">8.35 ± 0.79 / 29.79 ± 0.76</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">9</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">20.26 ± 2.94</td> <!-- ScandEval score -->
   <td class="en ner">18.69 ± 7.23 / 18.50 ± 6.51</td> <!-- CoNLL-en -->
   <td class="en sent">21.95 ± 6.30 / 33.38 ± 4.79</td> <!-- SST5 -->
   <td class="en la">0.01 ± 1.91 / 39.40 ± 3.94</td> <!-- ScaLA-en -->
   <td class="en qa">36.70 ± 2.02 / 50.85 ± 1.85</td> <!-- SQuAD -->
   <td class="en summ">60.11 ± 1.39 / 16.29 ± 0.69</td> <!-- CNN-DailyMail -->
   <td class="en know">3.71 ± 0.75 / 28.35 ± 0.99</td> <!-- MMLU -->
   <td class="en reason">0.62 ± 0.99 / 24.68 ± 0.55</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">10</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">8.86 ± 0.16</td> <!-- ScandEval score -->
   <td class="en ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-en -->
   <td class="en sent">0.00 ± 0.00 / 19.61 ± 0.22</td> <!-- SST5 -->
   <td class="en la">0.41 ± 0.55 / 33.46 ± 0.37</td> <!-- ScaLA-en -->
   <td class="en qa">0.00 ± 0.00 / 3.66 ± 0.43</td> <!-- SQuAD -->
   <td class="en summ">61.26 ± 0.09 / 6.73 ± 0.06</td> <!-- CNN-DailyMail -->
   <td class="en know">0.00 ± 0.00 / 22.69 ± 0.63</td> <!-- MMLU -->
   <td class="en reason">0.36 ± 0.47 / 24.60 ± 0.43</td> <!-- HellaSwag -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">11</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">6.50 ± 1.62</td> <!-- ScandEval score -->
   <td class="en ner">1.55 ± 1.98 / 1.45 ± 1.82</td> <!-- CoNLL-en -->
   <td class="en sent">3.71 ± 3.16 / 22.09 ± 2.08</td> <!-- SST5 -->
   <td class="en la">-0.42 ± 1.56 / 40.58 ± 3.74</td> <!-- ScaLA-en -->
   <td class="en qa">5.57 ± 3.10 / 11.14 ± 4.67</td> <!-- SQuAD -->
   <td class="en summ">34.87 ± 0.08 / 3.34 ± 0.07</td> <!-- CNN-DailyMail -->
   <td class="en know">0.37 ± 0.93 / 24.18 ± 0.90</td> <!-- MMLU -->
   <td class="en reason">-0.17 ± 0.50 / 24.82 ± 0.41</td> <!-- HellaSwag -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/english-nlg.csv" target="_blank">Download as CSV</a>
</div>