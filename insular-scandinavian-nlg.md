---
layout: leaderboard
title: Insular Scandinavian NLG
---

<center>Last updated: 06/02/2024 12:15:01 CET</center>

<div class="table-wrapper centered">

<input type="checkbox" id="merged-models-checkbox">
<label for="merged-models-checkbox">Include merged models</label>

<table id="insular-scandinavian-nlg" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval statistically significant model rank">Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score">Score</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Icelandic score">IS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Faroese score">FO</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">ARC-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-is</span></th>
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
   <td class="score">39.20 ± 3.36</td> <!-- ScandEval score -->
   <td class="is-score">38.01 ± 2.57</td> <!-- Icelandic score -->
   <td class="fo-score">40.39 ± 4.16</td> <!-- Faroese score -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">23.78 ± 2.81 / 42.70 ± 2.13</td> <!-- MMLU-is -->
   <td class="is know">37.79 ± 1.33 / 53.01 ± 1.03</td> <!-- ARC-is -->
   <td class="is reason">24.78 ± 2.63 / 42.97 ± 1.94</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="score">29.29 ± 2.38</td> <!-- ScandEval score -->
   <td class="is-score">25.84 ± 2.12</td> <!-- Icelandic score -->
   <td class="fo-score">32.73 ± 2.64</td> <!-- Faroese score -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td class="is summ">64.81 ± 1.16 / 19.31 ± 0.91</td> <!-- RRN -->
   <td class="is know">10.31 ± 1.06 / 32.74 ± 0.64</td> <!-- MMLU-is -->
   <td class="is know">7.36 ± 1.18 / 30.77 ± 0.78</td> <!-- ARC-is -->
   <td class="is reason">6.55 ± 1.30 / 29.83 ± 1.01</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="merged-model">
   <td class="rank">2=</td> <!-- Rank -->
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="score">29.02 ± 3.73</td> <!-- ScandEval score -->
   <td class="is-score">24.81 ± 3.16</td> <!-- Icelandic score -->
   <td class="fo-score">33.23 ± 4.30</td> <!-- Faroese score -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.42 ± 4.37 / 55.49 ± 2.89</td> <!-- NQiI -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">10.13 ± 2.94 / 32.62 ± 2.20</td> <!-- MMLU-is -->
   <td class="is know">5.19 ± 3.15 / 28.44 ± 2.45</td> <!-- ARC-is -->
   <td class="is reason">2.06 ± 2.74 / 25.59 ± 1.92</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="score">25.19 ± 2.15</td> <!-- ScandEval score -->
   <td class="is-score">20.76 ± 1.80</td> <!-- Icelandic score -->
   <td class="fo-score">29.62 ± 2.50</td> <!-- Faroese score -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.12 ± 2.50 / 39.44 ± 1.99</td> <!-- NQiI -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td class="is summ">64.14 ± 0.87 / 16.89 ± 1.86</td> <!-- RRN -->
   <td class="is know">3.27 ± 0.84 / 26.91 ± 0.86</td> <!-- MMLU-is -->
   <td class="is know">2.13 ± 1.49 / 27.86 ± 1.04</td> <!-- ARC-is -->
   <td class="is reason">1.54 ± 0.83 / 26.63 ± 0.65</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="score">24.66 ± 2.06</td> <!-- ScandEval score -->
   <td class="is-score">21.06 ± 1.86</td> <!-- Icelandic score -->
   <td class="fo-score">28.27 ± 2.27</td> <!-- Faroese score -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">17.92 ± 3.21 / 42.41 ± 2.86</td> <!-- NQiI -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td class="is summ">63.83 ± 1.29 / 17.92 ± 1.27</td> <!-- RRN -->
   <td class="is know">7.22 ± 1.33 / 29.40 ± 1.04</td> <!-- MMLU-is -->
   <td class="is know">4.34 ± 1.43 / 27.42 ± 1.06</td> <!-- ARC-is -->
   <td class="is reason">3.12 ± 1.36 / 27.42 ± 0.86</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="score">23.75 ± 2.26</td> <!-- ScandEval score -->
   <td class="is-score">22.27 ± 1.88</td> <!-- Icelandic score -->
   <td class="fo-score">25.23 ± 2.63</td> <!-- Faroese score -->
   <td class="is ner">27.54 ± 3.01 / 23.54 ± 2.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.61 ± 1.64 / 41.57 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">28.12 ± 3.77 / 54.61 ± 3.42</td> <!-- NQiI -->
   <td class="fo ner">46.50 ± 3.24 / 45.65 ± 2.54</td> <!-- FoNE -->
   <td class="fo la">3.95 ± 2.03 / 46.57 ± 3.18</td> <!-- ScaLA-fo -->
   <td class="is summ">68.35 ± 0.29 / 22.27 ± 0.52</td> <!-- RRN -->
   <td class="is know">3.32 ± 1.54 / 27.67 ± 1.22</td> <!-- MMLU-is -->
   <td class="is know">1.83 ± 1.54 / 27.24 ± 1.07</td> <!-- ARC-is -->
   <td class="is reason">2.41 ± 1.03 / 25.89 ± 0.88</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="score">23.21 ± 2.63</td> <!-- ScandEval score -->
   <td class="is-score">20.20 ± 1.98</td> <!-- Icelandic score -->
   <td class="fo-score">26.23 ± 3.28</td> <!-- Faroese score -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.31 ± 3.62 / 40.78 ± 4.26</td> <!-- NQiI -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td class="is summ">64.30 ± 1.22 / 19.07 ± 1.13</td> <!-- RRN -->
   <td class="is know">5.05 ± 1.56 / 28.95 ± 1.00</td> <!-- MMLU-is -->
   <td class="is know">3.84 ± 1.07 / 25.73 ± 1.14</td> <!-- ARC-is -->
   <td class="is reason">0.80 ± 1.18 / 25.46 ± 0.72</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">3=</td> <!-- Rank -->
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="score">22.03 ± 1.91</td> <!-- ScandEval score -->
   <td class="is-score">16.97 ± 1.74</td> <!-- Icelandic score -->
   <td class="fo-score">27.09 ± 2.08</td> <!-- Faroese score -->
   <td class="is ner">22.55 ± 3.91 / 22.44 ± 3.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.44 ± 0.79 / 33.03 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is qa">11.98 ± 2.87 / 33.09 ± 1.83</td> <!-- NQiI -->
   <td class="fo ner">54.17 ± 4.15 / 54.25 ± 4.13</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="is summ">65.35 ± 0.78 / 19.71 ± 0.93</td> <!-- RRN -->
   <td class="is know">2.15 ± 0.98 / 24.92 ± 0.93</td> <!-- MMLU-is -->
   <td class="is know">1.99 ± 1.11 / 25.64 ± 0.71</td> <!-- ARC-is -->
   <td class="is reason">0.34 ± 1.06 / 25.83 ± 0.66</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">4</td> <!-- Rank -->
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="score">10.38 ± 2.04</td> <!-- ScandEval score -->
   <td class="is-score">11.55 ± 1.09</td> <!-- Icelandic score -->
   <td class="fo-score">9.21 ± 3.00</td> <!-- Faroese score -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.36 ± 3.51</td> <!-- NQiI -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
   <td class="is summ">57.59 ± 1.46 / 12.99 ± 0.73</td> <!-- RRN -->
   <td class="is know">0.74 ± 0.76 / 25.88 ± 1.33</td> <!-- MMLU-is -->
   <td class="is know">1.47 ± 0.92 / 24.38 ± 1.72</td> <!-- ARC-is -->
   <td class="is reason">-0.01 ± 0.72 / 24.46 ± 0.37</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="score">4.61 ± 0.01</td> <!-- ScandEval score -->
   <td class="is-score">9.22 ± 0.03</td> <!-- Icelandic score -->
   <td class="fo-score">0.00 ± 0.00</td> <!-- Faroese score -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 11.90 ± 2.74</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="is summ">55.33 ± 0.17 / 6.93 ± 0.19</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 21.57 ± 0.58</td> <!-- MMLU-is -->
   <td class="is know">0.00 ± 0.00 / 21.46 ± 0.73</td> <!-- ARC-is -->
   <td class="is reason">0.00 ± 0.00 / 24.86 ± 0.79</td> <!-- HellaSwag-is -->
  </tr>
  <tr class="not-merged-model">
   <td class="rank">5=</td> <!-- Rank -->
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="score">2.45 ± 0.19</td> <!-- ScandEval score -->
   <td class="is-score">4.90 ± 0.38</td> <!-- Icelandic score -->
   <td class="fo-score">0.00 ± 0.00</td> <!-- Faroese score -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td class="is summ">30.20 ± 0.17 / 2.36 ± 0.06</td> <!-- RRN -->
   <td class="is know">0.85 ± 0.83 / 22.51 ± 0.58</td> <!-- MMLU-is -->
   <td class="is know">-1.13 ± 0.89 / 22.53 ± 0.61</td> <!-- ARC-is -->
   <td class="is reason">-0.67 ± 1.27 / 24.79 ± 0.84</td> <!-- HellaSwag-is -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlg.csv" target="_blank">Download as CSV</a>
</div>