---
layout: leaderboard
title: German NLU
---

<center>Last updated: 19/03/2024 10:17:23 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="german-nlu-test" class="sortable fixed centered small-font">
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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version">Version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">1.20</td> <!-- ScandEval rank -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de qa">25.22 ± 3.76 / 60.93 ± 2.96</td> <!-- GermanQuAD -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">7,778 ± 1,755 / 1,703 ± 552</td> <!-- Model inference speed -->
   <td class="rank">1.55</td> <!-- ScandEval rank -->
   <td class="de ner">56.71 ± 1.34 / 47.69 ± 2.04</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.03 / 62.42 ± 3.31</td> <!-- SB10k -->
   <td class="de la">19.92 ± 3.22 / 52.83 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de qa">27.87 ± 2.01 / 57.64 ± 2.05</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,538 ± 415 / 821 ± 253</td> <!-- Model inference speed -->
   <td class="rank">1.57</td> <!-- ScandEval rank -->
   <td class="de ner">55.15 ± 1.17 / 41.83 ± 1.49</td> <!-- GermEval -->
   <td class="de sent">47.85 ± 2.29 / 65.02 ± 1.69</td> <!-- SB10k -->
   <td class="de la">24.29 ± 2.18 / 60.90 ± 1.65</td> <!-- ScaLA-de -->
   <td class="de qa">23.98 ± 2.16 / 57.70 ± 1.94</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">1.59</td> <!-- ScandEval rank -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de qa">22.94 ± 3.05 / 47.19 ± 4.45</td> <!-- GermanQuAD -->
   <td>9.1.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,443 ± 1,273 / 1,144 ± 364</td> <!-- Model inference speed -->
   <td class="rank">1.66</td> <!-- ScandEval rank -->
   <td class="de ner">51.79 ± 0.92 / 36.09 ± 1.73</td> <!-- GermEval -->
   <td class="de sent">47.27 ± 3.06 / 63.50 ± 2.88</td> <!-- SB10k -->
   <td class="de la">22.15 ± 1.83 / 56.64 ± 4.04</td> <!-- ScaLA-de -->
   <td class="de qa">24.30 ± 3.79 / 54.51 ± 4.48</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,786 ± 532 / 784 ± 250</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="de ner">44.97 ± 1.75 / 35.79 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">53.14 ± 2.67 / 67.89 ± 2.15</td> <!-- SB10k -->
   <td class="de la">7.64 ± 2.47 / 37.95 ± 2.67</td> <!-- ScaLA-de -->
   <td class="de qa">30.12 ± 1.55 / 57.17 ± 2.38</td> <!-- GermanQuAD -->
   <td>9.3.2</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">1.85</td> <!-- ScandEval rank -->
   <td class="de ner">50.00 ± 1.33 / 38.45 ± 1.68</td> <!-- GermEval -->
   <td class="de sent">46.54 ± 2.92 / 63.66 ± 2.14</td> <!-- SB10k -->
   <td class="de la">15.30 ± 1.79 / 55.12 ± 1.92</td> <!-- ScaLA-de -->
   <td class="de qa">25.57 ± 3.57 / 56.05 ± 3.74</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
   <td class="de ner">0.75 ± 0.48 / 0.69 ± 0.43</td> <!-- GermEval -->
   <td class="de sent">54.96 ± 2.69 / 69.64 ± 2.09</td> <!-- SB10k -->
   <td class="de la">21.57 ± 4.18 / 55.63 ± 4.56</td> <!-- ScaLA-de -->
   <td class="de qa">31.49 ± 3.11 / 61.33 ± 3.41</td> <!-- GermanQuAD -->
   <td>12.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="de ner">0.67 ± 0.43 / 0.59 ± 0.41</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de qa">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,401 ± 2,529 / 2,123 ± 690</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="de ner">39.09 ± 2.92 / 31.71 ± 2.34</td> <!-- GermEval -->
   <td class="de sent">47.83 ± 2.81 / 60.24 ± 3.30</td> <!-- SB10k -->
   <td class="de la">10.31 ± 2.60 / 46.65 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">26.13 ± 3.79 / 53.13 ± 4.50</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,648 ± 467 / 799 ± 250</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="de ner">41.88 ± 1.87 / 31.88 ± 1.77</td> <!-- GermEval -->
   <td class="de sent">50.17 ± 2.52 / 65.78 ± 1.89</td> <!-- SB10k -->
   <td class="de la">15.82 ± 2.45 / 53.27 ± 4.50</td> <!-- ScaLA-de -->
   <td class="de qa">18.35 ± 2.70 / 39.71 ± 4.79</td> <!-- GermanQuAD -->
   <td>9.2.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,741 ± 987 / 1,554 ± 494</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="de ner">68.39 ± 0.98 / 67.24 ± 1.10</td> <!-- GermEval -->
   <td class="de sent">45.91 ± 3.76 / 62.57 ± 3.33</td> <!-- SB10k -->
   <td class="de la">2.79 ± 2.11 / 39.08 ± 4.38</td> <!-- ScaLA-de -->
   <td class="de qa">18.83 ± 1.45 / 35.01 ± 2.44</td> <!-- GermanQuAD -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="de ner">67.24 ± 1.51 / 66.01 ± 1.32</td> <!-- GermEval -->
   <td class="de sent">45.84 ± 2.11 / 63.35 ± 1.48</td> <!-- SB10k -->
   <td class="de la">2.28 ± 1.62 / 35.18 ± 2.11</td> <!-- ScaLA-de -->
   <td class="de qa">18.17 ± 1.85 / 33.37 ± 2.80</td> <!-- GermanQuAD -->
   <td>10.0.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM_German_7b_v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,972 ± 315 / 689 ± 204</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="de ner">2.21 ± 0.62 / 2.06 ± 0.54</td> <!-- GermEval -->
   <td class="de sent">48.67 ± 3.85 / 59.21 ± 4.18</td> <!-- SB10k -->
   <td class="de la">8.72 ± 2.15 / 43.37 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">34.07 ± 3.77 / 65.17 ± 3.27</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="merged-model">
   <td>mayflowergmbh/Wiedervereinigung-7b-dpo (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,374 ± 432 / 744 ± 230</td> <!-- Model inference speed -->
   <td class="rank">2.23</td> <!-- ScandEval rank -->
   <td class="de ner">6.74 ± 2.59 / 5.82 ± 2.08</td> <!-- GermEval -->
   <td class="de sent">51.92 ± 3.19 / 67.12 ± 2.11</td> <!-- SB10k -->
   <td class="de la">29.06 ± 5.04 / 62.77 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de qa">15.01 ± 2.99 / 50.63 ± 3.70</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="de ner">0.33 ± 0.21 / 0.31 ± 0.20</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de qa">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="de ner">0.74 ± 0.52 / 0.73 ± 0.52</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de qa">7.23 ± 2.21 / 44.27 ± 2.77</td> <!-- GermanQuAD -->
   <td>12.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model-->
   <td class="speed">4,880 ± 1,052 / 1,181 ± 380</td> <!-- Model inference speed -->
   <td class="rank">2.65</td> <!-- ScandEval rank -->
   <td class="de ner">35.78 ± 2.37 / 26.98 ± 1.75</td> <!-- GermEval -->
   <td class="de sent">34.13 ± 7.00 / 46.96 ± 8.23</td> <!-- SB10k -->
   <td class="de la">2.18 ± 1.60 / 38.27 ± 3.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.99 ± 4.02 / 38.26 ± 5.37</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="de ner">0.76 ± 0.52 / 0.70 ± 0.49</td> <!-- GermEval -->
   <td class="de sent">55.91 ± 2.49 / 70.31 ± 1.76</td> <!-- SB10k -->
   <td class="de la">22.47 ± 3.37 / 56.77 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de qa">3.85 ± 1.44 / 42.38 ± 3.92</td> <!-- GermanQuAD -->
   <td>12.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="de ner">0.19 ± 0.23 / 0.18 ± 0.23</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de qa">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model-->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">2.80</td> <!-- ScandEval rank -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.54 ± 5.12 / 49.63 ± 5.78</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de qa">20.40 ± 3.28 / 45.47 ± 3.32</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">2.84</td> <!-- ScandEval rank -->
   <td class="de ner">1.08 ± 0.45 / 1.10 ± 0.44</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de qa">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">2.99</td> <!-- ScandEval rank -->
   <td class="de ner">1.45 ± 0.53 / 1.42 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de qa">16.36 ± 3.23 / 41.95 ± 4.35</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model-->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="de ner">5.27 ± 1.04 / 4.51 ± 1.00</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de qa">23.48 ± 0.97 / 51.64 ± 1.00</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.07</td> <!-- ScandEval rank -->
   <td class="de ner">0.03 ± 0.05 / 0.04 ± 0.04</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de qa">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">3.54</td> <!-- ScandEval rank -->
   <td class="de ner">3.95 ± 1.07 / 3.57 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de qa">13.61 ± 1.64 / 29.08 ± 1.96</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model-->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">3.58</td> <!-- ScandEval rank -->
   <td class="de ner">5.85 ± 1.31 / 5.47 ± 1.00</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de qa">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model-->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">3.79</td> <!-- ScandEval rank -->
   <td class="de ner">7.27 ± 1.04 / 7.22 ± 1.14</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de qa">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td>12.1.0</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model-->
   <td class="speed">13,551 ± 4,259 / 2,563 ± 838</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="de ner">0.30 ± 0.60 / 0.26 ± 0.50</td> <!-- GermEval -->
   <td class="de sent">0.29 ± 1.28 / 17.22 ± 1.25</td> <!-- SB10k -->
   <td class="de la">-0.11 ± 1.16 / 36.65 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 1.54 ± 0.12</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model-->
   <td class="speed">9,757 ± 2,047 / 2,200 ± 705</td> <!-- Model inference speed -->
   <td class="rank">4.21</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de qa">0.00 ± 0.00 / 14.60 ± 0.67</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- ScandEval version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;German NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-I9boM&quot; src=&quot;https://datawrapper.dwcdn.net/I9boM/9/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
