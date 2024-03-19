---
layout: leaderboard
title: Insular Scandinavian NLU
---

<center>Last updated: 19/03/2024 10:57:12 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="insular-scandinavian-nlu-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval rank, computed as 1 + the average number of standard deviations from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic rank, computed as 1 + the average number of standard deviations from the best model">Icelandic Rank</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese rank, computed as 1 + the average number of standard deviations from the best model">Faroese Rank</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-is</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic question answering - Exact Match / F1-score">NQiI</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">FoNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-fo</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version">Version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">1.34</td> <!-- ScandEval rank -->
   <td class="is-rank">1.68</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.00</td> <!-- Faroese rank -->
   <td class="is ner">73.92 ± 1.40 / 75.86 ± 1.21</td> <!-- MIM-GOLD-NER -->
   <td class="is la">11.77 ± 5.19 / 43.60 ± 7.11</td> <!-- ScaLA-is -->
   <td class="is qa">11.84 ± 1.07 / 48.30 ± 1.02</td> <!-- NQiI -->
   <td class="fo ner">88.21 ± 0.97 / 88.63 ± 0.87</td> <!-- FoNE -->
   <td class="fo la">3.16 ± 2.26 / 38.93 ± 4.61</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">1.97</td> <!-- ScandEval rank -->
   <td class="is-rank">2.94</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.00</td> <!-- Faroese rank -->
   <td class="is ner">74.30 ± 2.15 / 76.10 ± 2.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.06 ± 2.43 / 37.04 ± 4.14</td> <!-- ScaLA-is -->
   <td class="is qa">11.47 ± 0.96 / 48.11 ± 0.94</td> <!-- NQiI -->
   <td class="fo ner">88.24 ± 0.58 / 88.48 ± 0.54</td> <!-- FoNE -->
   <td class="fo la">1.73 ± 1.70 / 42.32 ± 5.16</td> <!-- ScaLA-fo -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="is-rank">2.60</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.40</td> <!-- Faroese rank -->
   <td class="is ner">47.24 ± 2.54 / 37.77 ± 3.87</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.35 ± 1.70 / 39.37 ± 3.87</td> <!-- ScaLA-is -->
   <td class="is qa">26.26 ± 4.88 / 49.53 ± 5.23</td> <!-- NQiI -->
   <td class="fo ner">62.63 ± 3.44 / 57.85 ± 3.72</td> <!-- FoNE -->
   <td class="fo la">2.84 ± 1.84 / 42.62 ± 4.53</td> <!-- ScaLA-fo -->
   <td>9.1.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.11</td> <!-- ScandEval rank -->
   <td class="is-rank">2.57</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.66</td> <!-- Faroese rank -->
   <td class="is ner">27.54 ± 3.01 / 23.54 ± 2.16</td> <!-- MIM-GOLD-NER -->
   <td class="is la">4.61 ± 1.64 / 41.57 ± 3.41</td> <!-- ScaLA-is -->
   <td class="is qa">28.12 ± 3.77 / 54.61 ± 3.42</td> <!-- NQiI -->
   <td class="fo ner">46.50 ± 3.24 / 45.65 ± 2.54</td> <!-- FoNE -->
   <td class="fo la">3.95 ± 2.03 / 46.57 ± 3.18</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="is-rank">2.84</td> <!-- Icelandic rank -->
   <td class="fo-rank">1.40</td> <!-- Faroese rank -->
   <td class="is ner">49.86 ± 4.28 / 42.54 ± 5.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.26 ± 3.83 / 48.46 ± 2.37</td> <!-- ScaLA-is -->
   <td class="is qa">22.42 ± 4.37 / 55.49 ± 2.89</td> <!-- NQiI -->
   <td class="fo ner">62.78 ± 3.13 / 59.73 ± 3.23</td> <!-- FoNE -->
   <td class="fo la">3.69 ± 5.47 / 48.72 ± 3.41</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.39</td> <!-- ScandEval rank -->
   <td class="is-rank">2.61</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.17</td> <!-- Faroese rank -->
   <td class="is ner">43.11 ± 2.23 / 29.34 ± 3.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.40 ± 1.87 / 48.75 ± 1.47</td> <!-- ScaLA-is -->
   <td class="is qa">19.03 ± 3.72 / 49.63 ± 2.61</td> <!-- NQiI -->
   <td class="fo ner">61.28 ± 2.98 / 54.02 ± 3.55</td> <!-- FoNE -->
   <td class="fo la">1.68 ± 1.41 / 50.06 ± 1.22</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.66</td> <!-- ScandEval rank -->
   <td class="is-rank">3.03</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.29</td> <!-- Faroese rank -->
   <td class="is ner">32.71 ± 2.77 / 32.17 ± 2.13</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.66 ± 1.75 / 40.36 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">18.31 ± 3.62 / 40.78 ± 4.26</td> <!-- NQiI -->
   <td class="fo ner">52.34 ± 5.11 / 52.53 ± 4.79</td> <!-- FoNE -->
   <td class="fo la">0.11 ± 1.45 / 33.49 ± 0.47</td> <!-- ScaLA-fo -->
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="is-rank">2.81</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.74</td> <!-- Faroese rank -->
   <td class="is ner">28.35 ± 2.89 / 26.44 ± 2.75</td> <!-- MIM-GOLD-NER -->
   <td class="is la">3.14 ± 1.74 / 44.57 ± 3.85</td> <!-- ScaLA-is -->
   <td class="is qa">19.80 ± 2.66 / 43.44 ± 1.74</td> <!-- NQiI -->
   <td class="fo ner">60.54 ± 2.28 / 58.62 ± 1.89</td> <!-- FoNE -->
   <td class="fo la">-0.33 ± 1.12 / 37.78 ± 3.09</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="is-rank">3.30</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.29</td> <!-- Faroese rank -->
   <td class="is ner">36.04 ± 2.59 / 24.74 ± 2.79</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.36 ± 1.36 / 33.94 ± 0.32</td> <!-- ScaLA-is -->
   <td class="is qa">17.92 ± 3.21 / 42.41 ± 2.86</td> <!-- NQiI -->
   <td class="fo ner">55.42 ± 2.12 / 46.41 ± 2.50</td> <!-- FoNE -->
   <td class="fo la">1.11 ± 2.41 / 36.79 ± 4.00</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="is-rank">3.43</td> <!-- Icelandic rank -->
   <td class="fo-rank">2.74</td> <!-- Faroese rank -->
   <td class="is ner">41.10 ± 3.35 / 40.54 ± 3.19</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.07 ± 2.09 / 44.83 ± 2.20</td> <!-- ScaLA-is -->
   <td class="is qa">16.12 ± 2.50 / 39.44 ± 1.99</td> <!-- NQiI -->
   <td class="fo ner">59.77 ± 3.38 / 56.97 ± 4.30</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.61 / 36.94 ± 2.79</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="is-rank">3.76</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.16</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.31 ± 1.95 / 45.42 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">16.08 ± 2.91 / 37.41 ± 2.44</td> <!-- NQiI -->
   <td class="fo ner">0.11 ± 0.09 / 0.10 ± 0.09</td> <!-- FoNE -->
   <td class="fo la">1.28 ± 1.43 / 39.41 ± 3.29</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.63</td> <!-- ScandEval rank -->
   <td class="is-rank">4.12</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.15</td> <!-- Faroese rank -->
   <td class="is ner">0.25 ± 0.15 / 0.24 ± 0.15</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.78 ± 1.70 / 44.74 ± 3.57</td> <!-- ScaLA-is -->
   <td class="is qa">7.92 ± 1.32 / 23.57 ± 1.69</td> <!-- NQiI -->
   <td class="fo ner">0.38 ± 0.20 / 0.42 ± 0.18</td> <!-- FoNE -->
   <td class="fo la">0.15 ± 2.21 / 34.34 ± 0.53</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="is-rank">4.20</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.16</td> <!-- Faroese rank -->
   <td class="is ner">0.03 ± 0.04 / 0.03 ± 0.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.94 ± 1.34 / 40.66 ± 3.73</td> <!-- ScaLA-is -->
   <td class="is qa">6.31 ± 1.01 / 20.24 ± 2.02</td> <!-- NQiI -->
   <td class="fo ner">0.09 ± 0.09 / 0.10 ± 0.08</td> <!-- FoNE -->
   <td class="fo la">1.14 ± 1.66 / 37.04 ± 3.83</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="is-rank">3.76</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.72</td> <!-- Faroese rank -->
   <td class="is ner">0.15 ± 0.10 / 0.13 ± 0.09</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.59 ± 1.86 / 39.93 ± 4.19</td> <!-- ScaLA-is -->
   <td class="is qa">15.98 ± 3.74 / 39.67 ± 3.36</td> <!-- NQiI -->
   <td class="fo ner">0.31 ± 0.14 / 0.31 ± 0.14</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="is-rank">3.76</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.73</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">2.12 ± 1.40 / 38.45 ± 2.47</td> <!-- ScaLA-is -->
   <td class="is qa">16.85 ± 2.51 / 40.63 ± 2.83</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.28 ± 0.79 / 33.70 ± 0.64</td> <!-- ScaLA-fo -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="is-rank">4.03</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.72</td> <!-- Faroese rank -->
   <td class="is ner">0.05 ± 0.07 / 0.05 ± 0.07</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.35 ± 2.01 / 44.36 ± 4.13</td> <!-- ScaLA-is -->
   <td class="is qa">14.46 ± 2.66 / 32.31 ± 1.66</td> <!-- NQiI -->
   <td class="fo ner">0.13 ± 0.09 / 0.13 ± 0.09</td> <!-- FoNE -->
   <td class="fo la">-0.42 ± 2.18 / 34.33 ± 1.47</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.88</td> <!-- ScandEval rank -->
   <td class="is-rank">4.03</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.72</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.02 ± 0.03</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.55 ± 1.06 / 39.57 ± 3.61</td> <!-- ScaLA-is -->
   <td class="is qa">14.11 ± 3.08 / 34.56 ± 2.38</td> <!-- NQiI -->
   <td class="fo ner">0.06 ± 0.04 / 0.06 ± 0.04</td> <!-- FoNE -->
   <td class="fo la">-0.36 ± 1.07 / 35.09 ± 1.96</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="is-rank">4.65</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.14</td> <!-- Faroese rank -->
   <td class="is ner">1.24 ± 1.10 / 1.38 ± 1.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-1.04 ± 0.90 / 34.46 ± 1.41</td> <!-- ScaLA-is -->
   <td class="is qa">1.51 ± 0.68 / 13.16 ± 3.12</td> <!-- NQiI -->
   <td class="fo ner">1.26 ± 1.64 / 1.50 ± 2.05</td> <!-- FoNE -->
   <td class="fo la">1.01 ± 2.39 / 39.75 ± 4.10</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.92</td> <!-- ScandEval rank -->
   <td class="is-rank">4.13</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.72</td> <!-- Faroese rank -->
   <td class="is ner">0.17 ± 0.10 / 0.19 ± 0.10</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.71 ± 2.00 / 36.90 ± 2.10</td> <!-- ScaLA-is -->
   <td class="is qa">6.38 ± 1.58 / 34.47 ± 1.82</td> <!-- NQiI -->
   <td class="fo ner">0.40 ± 0.18 / 0.38 ± 0.16</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.26 ± 0.34</td> <!-- ScaLA-fo -->
   <td>12.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.99</td> <!-- ScandEval rank -->
   <td class="is-rank">4.54</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.43</td> <!-- Faroese rank -->
   <td class="is ner">9.48 ± 1.48 / 10.10 ± 1.44</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.07 ± 1.06 / 43.54 ± 3.63</td> <!-- ScaLA-is -->
   <td class="is qa">1.04 ± 0.96 / 7.36 ± 3.51</td> <!-- NQiI -->
   <td class="fo ner">18.86 ± 4.67 / 19.80 ± 5.33</td> <!-- FoNE -->
   <td class="fo la">-0.43 ± 1.33 / 39.75 ± 4.08</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.01</td> <!-- ScandEval rank -->
   <td class="is-rank">4.31</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.71</td> <!-- Faroese rank -->
   <td class="is ner">0.32 ± 0.38 / 0.29 ± 0.36</td> <!-- MIM-GOLD-NER -->
   <td class="is la">1.76 ± 1.62 / 38.51 ± 3.72</td> <!-- ScaLA-is -->
   <td class="is qa">3.10 ± 0.76 / 17.78 ± 2.28</td> <!-- NQiI -->
   <td class="fo ner">1.30 ± 0.69 / 1.29 ± 0.68</td> <!-- FoNE -->
   <td class="fo la">-0.54 ± 1.72 / 36.22 ± 2.35</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="is-rank">4.22</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.20</td> <!-- Faroese rank -->
   <td class="is ner">0.30 ± 0.32 / 0.26 ± 0.28</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.01 ± 2.13 / 46.02 ± 2.71</td> <!-- ScaLA-is -->
   <td class="is qa">11.00 ± 2.30 / 37.81 ± 0.70</td> <!-- NQiI -->
   <td class="fo ner">0.67 ± 1.13 / 0.67 ± 1.10</td> <!-- FoNE -->
   <td class="fo la">-1.62 ± 2.08 / 43.25 ± 3.61</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="is-rank">4.73</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.73</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 11.90 ± 2.74</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">0.00 ± 0.00 / 33.40 ± 0.34</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.23</td> <!-- ScandEval rank -->
   <td class="is-rank">4.73</td> <!-- Icelandic rank -->
   <td class="fo-rank">3.73</td> <!-- Faroese rank -->
   <td class="is ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- MIM-GOLD-NER -->
   <td class="is la">0.00 ± 0.00 / 33.69 ± 0.28</td> <!-- ScaLA-is -->
   <td class="is qa">0.00 ± 0.00 / 0.05 ± 0.03</td> <!-- NQiI -->
   <td class="fo ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- FoNE -->
   <td class="fo la">-0.24 ± 0.93 / 43.16 ± 3.72</td> <!-- ScaLA-fo -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.39</td> <!-- ScandEval rank -->
   <td class="is-rank">4.58</td> <!-- Icelandic rank -->
   <td class="fo-rank">4.20</td> <!-- Faroese rank -->
   <td class="is ner">1.14 ± 0.32 / 1.03 ± 0.27</td> <!-- MIM-GOLD-NER -->
   <td class="is la">-0.57 ± 1.20 / 41.25 ± 3.51</td> <!-- ScaLA-is -->
   <td class="is qa">3.31 ± 0.82 / 16.86 ± 2.98</td> <!-- NQiI -->
   <td class="fo ner">1.18 ± 0.35 / 1.28 ± 0.36</td> <!-- FoNE -->
   <td class="fo la">-1.47 ± 1.54 / 35.84 ± 1.76</td> <!-- ScaLA-fo -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/insular-scandinavian-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Insular Scandinavian NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-UgWP5&quot; src=&quot;https://datawrapper.dwcdn.net/UgWP5/11/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
