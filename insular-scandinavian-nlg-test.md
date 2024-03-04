---
layout: leaderboard
title: Insular Scandinavian NLG
---

<center>Last updated: 04/03/2024 17:54:30 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="insular-scandinavian-nlg-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, mean of language ranks">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Mean Icelandic rank">Icelandic Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Mean Faroese rank">Faroese Rank</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic summarization - BERTScore / ROUGE-L">RRN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,344 ± 455 / 4,023 ± 590</td> <!-- Model inference speed -->
   <td class="rank">1.08</td> <!-- ScandEval rank -->
   <td class="is-rank">1.17</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.00</td> <!-- Faroese rank -->
   <td class="is ner">69.59 ± 4.54 / 54.49 ± 4.31</td> <!-- MIM-GOLD-NER -->
   <td class="is la">7.28 ± 4.10 / 52.96 ± 2.00</td> <!-- ScaLA-is -->
   <td class="is qa">28.50 ± 1.79 / 50.29 ± 1.79</td> <!-- NQiI -->
   <td class="is summ">67.10 ± 0.30 / 19.43 ± 0.48</td> <!-- RRN -->
   <td class="is know">23.78 ± 2.81 / 42.70 ± 2.13</td> <!-- MMLU-is -->
   <td class="is reason">24.78 ± 2.63 / 42.97 ± 1.94</td> <!-- HellaSwag-is -->
   <td class="fo ner">72.48 ± 2.39 / 67.50 ± 2.38</td> <!-- FoNE -->
   <td class="fo la">8.29 ± 5.92 / 42.34 ± 3.49</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="is-rank">2.17</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.50</td> <!-- Faroese rank -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="is summ">61.96 ± 3.10 / 16.11 ± 1.80</td> <!-- RRN -->
   <td class="is know">10.31 ± 1.06 / 32.74 ± 0.64</td> <!-- MMLU-is -->
   <td class="is reason">6.55 ± 1.30 / 29.83 ± 1.01</td> <!-- HellaSwag-is -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="is-rank">2.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.50</td> <!-- Faroese rank -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.42 ± 4.37 / 55.49 ± 2.89</td> <!-- NQiI -->
   <td class="is summ">65.60 ± 0.69 / 19.46 ± 0.80</td> <!-- RRN -->
   <td class="is know">10.13 ± 2.94 / 32.62 ± 2.20</td> <!-- MMLU-is -->
   <td class="is reason">2.06 ± 2.74 / 25.59 ± 1.92</td> <!-- HellaSwag-is -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="is-rank">2.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.00</td> <!-- Faroese rank -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is qa">19.03 ± 3.72 / 49.63 ± 2.61</td> <!-- NQiI -->
   <td class="is summ">64.97 ± 1.57 / 18.31 ± 1.39</td> <!-- RRN -->
   <td class="is know">7.55 ± 0.67 / 29.89 ± 0.47</td> <!-- MMLU-is -->
   <td class="is reason">5.31 ± 1.03 / 29.05 ± 0.67</td> <!-- HellaSwag-is -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="is-rank">2.67</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.50</td> <!-- Faroese rank -->
   <td class="is ner">27.54 ± 3.01 / 23.54 ± 2.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.61 ± 1.64 / 41.57 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">28.12 ± 3.77 / 54.61 ± 3.42</td> <!-- NQiI -->
   <td class="is summ">68.35 ± 0.29 / 22.27 ± 0.52</td> <!-- RRN -->
   <td class="is know">3.32 ± 1.54 / 27.67 ± 1.22</td> <!-- MMLU-is -->
   <td class="is reason">2.41 ± 1.03 / 25.89 ± 0.88</td> <!-- HellaSwag-is -->
   <td class="fo ner">46.50 ± 3.24 / 45.65 ± 2.54</td> <!-- FoNE -->
   <td class="fo la">3.95 ± 2.03 / 46.57 ± 3.18</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="is-rank">3.00</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.50</td> <!-- Faroese rank -->
   <td class="is ner">28.35 ± 2.89 / 26.44 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.14 ± 1.74 / 44.57 ± 3.85</td> <!-- ScaLA-is -->
   <td class="is qa">19.80 ± 2.66 / 43.44 ± 1.74</td> <!-- NQiI -->
   <td class="is summ">65.49 ± 0.40 / 19.56 ± 0.64</td> <!-- RRN -->
   <td class="is know">7.74 ± 1.21 / 30.25 ± 1.07</td> <!-- MMLU-is -->
   <td class="is reason">2.72 ± 1.12 / 26.48 ± 0.75</td> <!-- HellaSwag-is -->
   <td class="fo ner">60.54 ± 2.28 / 58.62 ± 1.89</td> <!-- FoNE -->
   <td class="fo la">-0.33 ± 1.12 / 37.78 ± 3.09</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.92</td> <!-- ScandEval rank -->
   <td class="is-rank">3.33</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.50</td> <!-- Faroese rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">17.92 ± 3.21 / 42.41 ± 2.86</td> <!-- NQiI -->
   <td class="is summ">62.82 ± 1.66 / 15.30 ± 1.00</td> <!-- RRN -->
   <td class="is know">7.22 ± 1.33 / 29.40 ± 1.04</td> <!-- MMLU-is -->
   <td class="is reason">3.12 ± 1.36 / 27.42 ± 0.86</td> <!-- HellaSwag-is -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="is-rank">3.67</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.50</td> <!-- Faroese rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.31 ± 3.62 / 40.78 ± 4.26</td> <!-- NQiI -->
   <td class="is summ">60.73 ± 3.02 / 14.02 ± 1.57</td> <!-- RRN -->
   <td class="is know">5.05 ± 1.56 / 28.95 ± 1.00</td> <!-- MMLU-is -->
   <td class="is reason">0.80 ± 1.18 / 25.46 ± 0.72</td> <!-- HellaSwag-is -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="is-rank">3.83</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.50</td> <!-- Faroese rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.12 ± 2.50 / 39.44 ± 1.99</td> <!-- NQiI -->
   <td class="is summ">62.28 ± 0.90 / 13.27 ± 1.36</td> <!-- RRN -->
   <td class="is know">3.27 ± 0.84 / 26.91 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">1.54 ± 0.83 / 26.63 ± 0.65</td> <!-- HellaSwag-is -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="is-rank">4.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.00</td> <!-- Faroese rank -->
   <td class="is ner">22.55 ± 3.91 / 22.44 ± 3.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.44 ± 0.79 / 33.03 ± 0.29</td> <!-- ScaLA-is -->
   <td class="is qa">11.98 ± 2.87 / 33.09 ± 1.83</td> <!-- NQiI -->
   <td class="is summ">65.35 ± 0.78 / 19.71 ± 0.93</td> <!-- RRN -->
   <td class="is know">2.15 ± 0.98 / 24.92 ± 0.93</td> <!-- MMLU-is -->
   <td class="is reason">0.34 ± 1.06 / 25.83 ± 0.66</td> <!-- HellaSwag-is -->
   <td class="fo ner">54.17 ± 4.15 / 54.25 ± 4.13</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">4.83</td> <!-- ScandEval rank -->
   <td class="is-rank">5.17</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.50</td> <!-- Faroese rank -->
   <td class="is ner">0.25 ± 0.15 / 0.24 ± 0.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">7.92 ± 1.32 / 23.57 ± 1.69</td> <!-- NQiI -->
   <td class="is summ">57.36 ± 1.38 / 10.41 ± 0.99</td> <!-- RRN -->
   <td class="is know">3.87 ± 0.97 / 26.29 ± 0.94</td> <!-- MMLU-is -->
   <td class="is reason">1.09 ± 1.19 / 25.08 ± 0.90</td> <!-- HellaSwag-is -->
   <td class="fo ner">0.38 ± 0.20 / 0.42 ± 0.18</td> <!-- FoNE -->
   <td class="fo la">0.15 ± 2.21 / 34.34 ± 0.53</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">4.92</td> <!-- ScandEval rank -->
   <td class="is-rank">5.83</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.00</td> <!-- Faroese rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.36 ± 3.51</td> <!-- NQiI -->
   <td class="is summ">57.59 ± 1.46 / 12.99 ± 0.73</td> <!-- RRN -->
   <td class="is know">0.74 ± 0.76 / 25.88 ± 1.33</td> <!-- MMLU-is -->
   <td class="is reason">-0.01 ± 0.72 / 24.46 ± 0.37</td> <!-- HellaSwag-is -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">5.00</td> <!-- ScandEval rank -->
   <td class="is-rank">4.00</td> <!-- Icelandic rank -->
   <td class="fo-rank">6.00</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">16.85 ± 2.51 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="is summ">60.02 ± 3.15 / 14.22 ± 1.52</td> <!-- RRN -->
   <td class="is know">8.44 ± 0.73 / 31.23 ± 0.59</td> <!-- MMLU-is -->
   <td class="is reason">1.76 ± 1.09 / 25.68 ± 0.87</td> <!-- HellaSwag-is -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 0.79 / 33.70 ± 0.64</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">5.00</td> <!-- ScandEval rank -->
   <td class="is-rank">5.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.50</td> <!-- Faroese rank -->
   <td class="is ner">0.32 ± 0.38 / 0.29 ± 0.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is qa">3.10 ± 0.76 / 17.78 ± 2.28</td> <!-- NQiI -->
   <td class="is summ">58.94 ± 1.53 / 10.09 ± 1.39</td> <!-- RRN -->
   <td class="is know">2.82 ± 0.73 / 26.56 ± 0.56</td> <!-- MMLU-is -->
   <td class="is reason">1.31 ± 0.92 / 26.54 ± 0.57</td> <!-- HellaSwag-is -->
   <td class="fo ner">1.30 ± 0.69 / 1.29 ± 0.68</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.72 / 36.22 ± 2.35</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">5.25</td> <!-- ScandEval rank -->
   <td class="is-rank">5.50</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.00</td> <!-- Faroese rank -->
   <td class="is ner">1.14 ± 0.32 / 1.03 ± 0.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="is summ">56.00 ± 3.13 / 10.05 ± 0.73</td> <!-- RRN -->
   <td class="is know">2.71 ± 0.84 / 24.35 ± 0.86</td> <!-- MMLU-is -->
   <td class="is reason">0.95 ± 1.17 / 25.82 ± 0.62</td> <!-- HellaSwag-is -->
   <td class="fo ner">1.18 ± 0.35 / 1.28 ± 0.36</td> <!-- FoNE -->
   <td class="fo la">-1.47 ± 1.54 / 35.84 ± 1.76</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">5.33</td> <!-- ScandEval rank -->
   <td class="is-rank">5.67</td> <!-- Icelandic rank -->
   <td class="fo-rank">5.00</td> <!-- Faroese rank -->
   <td class="is ner">0.03 ± 0.04 / 0.03 ± 0.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is qa">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="is summ">55.32 ± 3.49 / 8.91 ± 1.05</td> <!-- RRN -->
   <td class="is know">3.79 ± 1.12 / 25.76 ± 0.91</td> <!-- MMLU-is -->
   <td class="is reason">-0.53 ± 1.24 / 24.76 ± 0.93</td> <!-- HellaSwag-is -->
   <td class="fo ner">0.09 ± 0.09 / 0.10 ± 0.08</td> <!-- FoNE -->
   <td class="fo la">1.14 ± 1.66 / 37.04 ± 3.83</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">6.33</td> <!-- ScandEval rank -->
   <td class="is-rank">6.67</td> <!-- Icelandic rank -->
   <td class="fo-rank">6.00</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 11.90 ± 2.74</td> <!-- NQiI -->
   <td class="is summ">55.33 ± 0.17 / 6.93 ± 0.19</td> <!-- RRN -->
   <td class="is know">0.00 ± 0.00 / 21.57 ± 0.58</td> <!-- MMLU-is -->
   <td class="is reason">0.00 ± 0.00 / 24.86 ± 0.79</td> <!-- HellaSwag-is -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
  </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">6.33</td> <!-- ScandEval rank -->
   <td class="is-rank">6.67</td> <!-- Icelandic rank -->
   <td class="fo-rank">6.00</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="is summ">17.11 ± 1.37 / 0.96 ± 0.09</td> <!-- RRN -->
   <td class="is know">0.69 ± 0.98 / 23.34 ± 0.72</td> <!-- MMLU-is -->
   <td class="is reason">-0.36 ± 1.12 / 24.96 ± 0.63</td> <!-- HellaSwag-is -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.24 ± 0.93 / 43.16 ± 3.72</td> <!-- ScaLA-fo -->
  </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlg-test.csv" target="_blank">Download as CSV</a>
</div>