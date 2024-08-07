---
layout: leaderboard
title: German NLU 🇩🇪
---

<center>Last updated: 07/08/2024 09:50:30 CET</center>

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
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">GermEval</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">SB10k</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-de</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="German reading comprehension - Exact Match / F1-score">GermanQuAD</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermEval">GermEval version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SB10k">SB10k version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-de">ScaLA-de version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on GermanQuAD">GermanQuAD version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>deepset/gbert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">337</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,109 ± 3,442 / 4,438 ± 1,468</td> <!-- Model inference speed -->
   <td class="rank">1.17</td> <!-- ScandEval rank -->
   <td class="de ner">80.30 ± 0.94 / 79.06 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">65.12 ± 1.34 / 76.67 ± 0.90</td> <!-- SB10k -->
   <td class="de la">75.12 ± 1.07 / 87.22 ± 0.63</td> <!-- ScaLA-de -->
   <td class="de rc">28.91 ± 1.58 / 56.61 ± 1.98</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/rembert</td> <!-- Model ID -->
   <td class="num_model_parameters">575</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,736 ± 2,822 / 2,102 ± 677</td> <!-- Model inference speed -->
   <td class="rank">1.35</td> <!-- ScandEval rank -->
   <td class="de ner">77.62 ± 0.80 / 76.16 ± 0.79</td> <!-- GermEval -->
   <td class="de sent">60.65 ± 2.10 / 73.52 ± 1.58</td> <!-- SB10k -->
   <td class="de la">62.60 ± 2.16 / 81.12 ± 1.14</td> <!-- ScaLA-de -->
   <td class="de rc">33.62 ± 1.34 / 60.41 ± 1.36</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>FacebookAI/xlm-roberta-large</td> <!-- Model ID -->
   <td class="num_model_parameters">561</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">17,897 ± 3,921 / 3,463 ± 1,141</td> <!-- Model inference speed -->
   <td class="rank">1.36</td> <!-- ScandEval rank -->
   <td class="de ner">80.64 ± 0.81 / 80.03 ± 0.97</td> <!-- GermEval -->
   <td class="de sent">63.02 ± 1.62 / 75.25 ± 1.08</td> <!-- SB10k -->
   <td class="de la">54.83 ± 9.12 / 76.02 ± 5.19</td> <!-- ScaLA-de -->
   <td class="de rc">29.09 ± 1.00 / 55.68 ± 1.11</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large-instruct</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">514</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,947 ± 1,301 / 1,129 ± 374</td> <!-- Model inference speed -->
   <td class="rank">1.46</td> <!-- ScandEval rank -->
   <td class="de ner">79.77 ± 1.22 / 78.93 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">65.72 ± 1.70 / 76.73 ± 1.23</td> <!-- SB10k -->
   <td class="de la">49.82 ± 10.56 / 73.61 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">28.42 ± 1.71 / 55.35 ± 1.55</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8220</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="de ner">69.48 ± 2.32 / 54.66 ± 2.17</td> <!-- GermEval -->
   <td class="de sent">64.91 ± 1.86 / 75.96 ± 1.59</td> <!-- SB10k -->
   <td class="de la">50.23 ± 4.16 / 74.54 ± 2.10</td> <!-- ScaLA-de -->
   <td class="de rc">33.17 ± 1.86 / 65.14 ± 1.53</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-large</td> <!-- Model ID -->
   <td class="num_model_parameters">560</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,732 ± 1,273 / 1,633 ± 523</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="de ner">79.73 ± 1.38 / 78.52 ± 1.44</td> <!-- GermEval -->
   <td class="de sent">64.78 ± 1.34 / 76.30 ± 0.98</td> <!-- SB10k -->
   <td class="de la">47.24 ± 13.67 / 71.51 ± 8.03</td> <!-- ScaLA-de -->
   <td class="de rc">28.11 ± 0.94 / 54.87 ± 1.08</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/use-cmlm-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">472</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,231 ± 8,171 / 4,863 ± 1,598</td> <!-- Model inference speed -->
   <td class="rank">1.51</td> <!-- ScandEval rank -->
   <td class="de ner">77.03 ± 1.06 / 76.61 ± 1.13</td> <!-- GermEval -->
   <td class="de sent">59.50 ± 1.14 / 72.91 ± 0.76</td> <!-- SB10k -->
   <td class="de la">59.30 ± 1.32 / 78.31 ± 0.74</td> <!-- ScaLA-de -->
   <td class="de rc">26.67 ± 0.90 / 50.81 ± 0.88</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.58</td> <!-- ScandEval rank -->
   <td class="de ner">69.04 ± 2.51 / 61.10 ± 3.39</td> <!-- GermEval -->
   <td class="de sent">63.51 ± 2.57 / 75.01 ± 1.74</td> <!-- SB10k -->
   <td class="de la">37.41 ± 2.43 / 67.63 ± 1.05</td> <!-- ScaLA-de -->
   <td class="de rc">38.29 ± 3.54 / 69.69 ± 2.78</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gwlms/deberta-base-dewiki-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">112</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">18,084 ± 2,413 / 5,561 ± 1,826</td> <!-- Model inference speed -->
   <td class="rank">1.63</td> <!-- ScandEval rank -->
   <td class="de ner">79.67 ± 1.47 / 78.63 ± 1.31</td> <!-- GermEval -->
   <td class="de sent">50.90 ± 2.77 / 66.61 ± 2.07</td> <!-- SB10k -->
   <td class="de la">75.16 ± 1.45 / 87.41 ± 0.72</td> <!-- ScaLA-de -->
   <td class="de rc">18.57 ± 2.14 / 41.99 ± 2.69</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="de ner">68.94 ± 2.50 / 44.89 ± 2.85</td> <!-- GermEval -->
   <td class="de sent">60.47 ± 2.94 / 72.79 ± 1.90</td> <!-- SB10k -->
   <td class="de la">51.26 ± 4.94 / 74.76 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">30.04 ± 1.30 / 58.77 ± 1.50</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>setu4993/LaBSE</td> <!-- Model ID -->
   <td class="num_model_parameters">471</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">501</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,418 ± 6,435 / 4,536 ± 1,452</td> <!-- Model inference speed -->
   <td class="rank">1.67</td> <!-- ScandEval rank -->
   <td class="de ner">79.44 ± 0.96 / 78.42 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">58.65 ± 1.67 / 72.12 ± 1.18</td> <!-- SB10k -->
   <td class="de la">52.19 ± 2.96 / 74.17 ± 1.82</td> <!-- ScaLA-de -->
   <td class="de rc">23.66 ± 0.97 / 45.11 ± 1.50</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">1.70</td> <!-- ScandEval rank -->
   <td class="de ner">68.11 ± 1.32 / 56.25 ± 1.65</td> <!-- GermEval -->
   <td class="de sent">59.79 ± 1.60 / 71.47 ± 1.54</td> <!-- SB10k -->
   <td class="de la">35.45 ± 3.06 / 66.13 ± 1.28</td> <!-- ScaLA-de -->
   <td class="de rc">37.27 ± 1.23 / 68.54 ± 1.94</td> <!-- GermanQuAD -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gwlms/teams-base-dewiki-v1-discriminator</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,608 ± 4,466 / 8,477 ± 2,725</td> <!-- Model inference speed -->
   <td class="rank">1.72</td> <!-- ScandEval rank -->
   <td class="de ner">79.59 ± 0.89 / 78.76 ± 0.74</td> <!-- GermEval -->
   <td class="de sent">47.85 ± 2.41 / 64.86 ± 1.71</td> <!-- SB10k -->
   <td class="de la">68.48 ± 2.29 / 83.93 ± 1.25</td> <!-- ScaLA-de -->
   <td class="de rc">19.90 ± 1.38 / 41.74 ± 2.30</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/mdeberta-v3-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">251</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,637 ± 3,925 / 4,497 ± 1,502</td> <!-- Model inference speed -->
   <td class="rank">1.77</td> <!-- ScandEval rank -->
   <td class="de ner">77.42 ± 1.30 / 76.39 ± 1.16</td> <!-- GermEval -->
   <td class="de sent">50.90 ± 6.20 / 66.89 ± 4.34</td> <!-- SB10k -->
   <td class="de la">59.38 ± 2.00 / 79.12 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">20.28 ± 1.15 / 42.79 ± 1.37</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">1.79</td> <!-- ScandEval rank -->
   <td class="de ner">63.71 ± 2.43 / 57.08 ± 2.70</td> <!-- GermEval -->
   <td class="de sent">58.17 ± 2.51 / 71.34 ± 1.62</td> <!-- SB10k -->
   <td class="de la">36.33 ± 5.00 / 64.51 ± 3.38</td> <!-- ScaLA-de -->
   <td class="de rc">36.06 ± 2.89 / 69.62 ± 2.81</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-german-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">37,150 ± 6,555 / 8,659 ± 2,843</td> <!-- Model inference speed -->
   <td class="rank">1.82</td> <!-- ScandEval rank -->
   <td class="de ner">78.54 ± 1.02 / 77.24 ± 0.95</td> <!-- GermEval -->
   <td class="de sent">53.91 ± 1.63 / 69.21 ± 1.06</td> <!-- SB10k -->
   <td class="de la">59.23 ± 3.17 / 78.21 ± 2.03</td> <!-- ScaLA-de -->
   <td class="de rc">13.71 ± 1.48 / 32.14 ± 2.81</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">127903</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.83</td> <!-- ScandEval rank -->
   <td class="de ner">69.99 ± 1.63 / 45.58 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">54.82 ± 2.19 / 68.42 ± 1.67</td> <!-- SB10k -->
   <td class="de la">43.66 ± 5.67 / 64.64 ± 4.65</td> <!-- ScaLA-de -->
   <td class="de rc">30.06 ± 1.04 / 60.77 ± 1.11</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.2</td> <!-- SB10k version -->
   <td>12.10.2</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-german-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">36,020 ± 6,698 / 8,035 ± 2,647</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="de ner">77.55 ± 0.54 / 75.74 ± 0.56</td> <!-- GermEval -->
   <td class="de sent">56.48 ± 1.78 / 70.91 ± 1.23</td> <!-- SB10k -->
   <td class="de la">63.49 ± 4.58 / 80.65 ± 2.60</td> <!-- ScaLA-de -->
   <td class="de rc">12.39 ± 0.86 / 30.22 ± 1.38</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>deepset/gbert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">37,268 ± 6,577 / 8,719 ± 2,865</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="de ner">80.09 ± 0.84 / 78.71 ± 0.84</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 2.24 / 73.18 ± 1.49</td> <!-- SB10k -->
   <td class="de la">47.48 ± 7.30 / 70.97 ± 3.94</td> <!-- ScaLA-de -->
   <td class="de rc">14.39 ± 0.71 / 32.78 ± 1.01</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gwlms/bert-base-dewiki-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">30,650 ± 4,495 / 8,500 ± 2,755</td> <!-- Model inference speed -->
   <td class="rank">1.86</td> <!-- ScandEval rank -->
   <td class="de ner">80.53 ± 1.03 / 79.35 ± 1.07</td> <!-- GermEval -->
   <td class="de sent">45.61 ± 1.73 / 63.19 ± 1.32</td> <!-- SB10k -->
   <td class="de la">67.09 ± 2.48 / 82.65 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">16.61 ± 0.99 / 35.77 ± 1.33</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32793</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.87</td> <!-- ScandEval rank -->
   <td class="de ner">65.19 ± 2.58 / 56.17 ± 3.57</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 2.15 / 71.98 ± 1.46</td> <!-- SB10k -->
   <td class="de la">41.86 ± 5.44 / 69.70 ± 2.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.51 ± 3.79 / 63.19 ± 2.48</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.90</td> <!-- ScandEval rank -->
   <td class="de ner">75.20 ± 2.15 / 64.06 ± 3.60</td> <!-- GermEval -->
   <td class="de sent">54.38 ± 3.31 / 68.02 ± 2.21</td> <!-- SB10k -->
   <td class="de la">36.59 ± 4.24 / 67.36 ± 1.77</td> <!-- ScaLA-de -->
   <td class="de rc">26.90 ± 2.67 / 58.28 ± 2.22</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">1.91</td> <!-- ScandEval rank -->
   <td class="de ner">60.46 ± 1.26 / 47.72 ± 1.69</td> <!-- GermEval -->
   <td class="de sent">58.57 ± 2.53 / 71.30 ± 1.70</td> <!-- SB10k -->
   <td class="de la">26.25 ± 5.90 / 61.41 ± 3.94</td> <!-- ScaLA-de -->
   <td class="de rc">34.85 ± 3.43 / 64.05 ± 3.68</td> <!-- GermanQuAD -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>intfloat/multilingual-e5-base</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,965 ± 2,890 / 3,322 ± 1,074</td> <!-- Model inference speed -->
   <td class="rank">1.92</td> <!-- ScandEval rank -->
   <td class="de ner">74.79 ± 1.45 / 75.10 ± 1.37</td> <!-- GermEval -->
   <td class="de sent">63.29 ± 1.54 / 75.42 ± 1.03</td> <!-- SB10k -->
   <td class="de la">45.32 ± 8.38 / 71.30 ± 4.11</td> <!-- ScaLA-de -->
   <td class="de rc">16.42 ± 0.54 / 34.46 ± 1.03</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-HerO (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,477 ± 467 / 744 ± 232</td> <!-- Model inference speed -->
   <td class="rank">1.95</td> <!-- ScandEval rank -->
   <td class="de ner">59.70 ± 2.05 / 50.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">60.22 ± 2.99 / 72.76 ± 2.10</td> <!-- SB10k -->
   <td class="de la">35.99 ± 4.53 / 67.21 ± 2.14</td> <!-- ScaLA-de -->
   <td class="de rc">29.68 ± 3.29 / 65.65 ± 3.10</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="de ner">65.01 ± 0.68 / 43.34 ± 2.80</td> <!-- GermEval -->
   <td class="de sent">51.80 ± 1.29 / 67.45 ± 0.87</td> <!-- SB10k -->
   <td class="de la">36.18 ± 1.31 / 67.86 ± 0.51</td> <!-- ScaLA-de -->
   <td class="de rc">32.12 ± 2.08 / 67.30 ± 1.66</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-7b-LaserChat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,387 ± 456 / 717 ± 226</td> <!-- Model inference speed -->
   <td class="rank">1.96</td> <!-- ScandEval rank -->
   <td class="de ner">64.73 ± 1.02 / 48.09 ± 2.90</td> <!-- GermEval -->
   <td class="de sent">51.08 ± 1.67 / 67.20 ± 1.34</td> <!-- SB10k -->
   <td class="de la">36.46 ± 1.89 / 67.99 ± 0.80</td> <!-- ScaLA-de -->
   <td class="de rc">33.30 ± 1.87 / 67.32 ± 1.73</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">1.98</td> <!-- ScandEval rank -->
   <td class="de ner">61.50 ± 2.96 / 46.22 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">55.50 ± 2.58 / 68.96 ± 2.00</td> <!-- SB10k -->
   <td class="de la">38.96 ± 4.39 / 68.89 ± 2.54</td> <!-- ScaLA-de -->
   <td class="de rc">30.20 ± 1.59 / 56.58 ± 1.78</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>facebook/xlm-v-base</td> <!-- Model ID -->
   <td class="num_model_parameters">778</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">902</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">25,396 ± 6,394 / 4,534 ± 1,421</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="de ner">76.45 ± 1.57 / 76.50 ± 1.16</td> <!-- GermEval -->
   <td class="de sent">58.25 ± 2.98 / 72.01 ± 1.97</td> <!-- SB10k -->
   <td class="de la">34.43 ± 16.58 / 61.45 ± 12.19</td> <!-- ScaLA-de -->
   <td class="de rc">21.08 ± 1.57 / 41.84 ± 1.98</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="de ner">68.18 ± 0.95 / 57.72 ± 1.15</td> <!-- GermEval -->
   <td class="de sent">58.33 ± 2.83 / 69.31 ± 3.16</td> <!-- SB10k -->
   <td class="de la">29.12 ± 3.17 / 63.60 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 1.99 / 56.42 ± 3.34</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131104</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">1.99</td> <!-- ScandEval rank -->
   <td class="de ner">67.61 ± 1.23 / 60.39 ± 1.02</td> <!-- GermEval -->
   <td class="de sent">59.96 ± 2.00 / 70.71 ± 1.80</td> <!-- SB10k -->
   <td class="de la">28.25 ± 3.57 / 59.54 ± 3.88</td> <!-- ScaLA-de -->
   <td class="de rc">28.79 ± 2.02 / 55.82 ± 3.28</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/FC-SauerkrautLM-7b-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,160 ± 514 / 668 ± 256</td> <!-- Model inference speed -->
   <td class="rank">2.00</td> <!-- ScandEval rank -->
   <td class="de ner">56.70 ± 1.55 / 41.89 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">53.39 ± 1.89 / 67.16 ± 1.65</td> <!-- SB10k -->
   <td class="de la">35.64 ± 1.50 / 66.83 ± 0.97</td> <!-- ScaLA-de -->
   <td class="de rc">34.22 ± 1.43 / 67.00 ± 1.27</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128030</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.02</td> <!-- ScandEval rank -->
   <td class="de ner">67.90 ± 1.07 / 45.53 ± 3.11</td> <!-- GermEval -->
   <td class="de sent">51.88 ± 5.19 / 67.24 ± 3.71</td> <!-- SB10k -->
   <td class="de la">46.77 ± 2.33 / 69.48 ± 2.55</td> <!-- ScaLA-de -->
   <td class="de rc">24.70 ± 1.31 / 56.87 ± 0.77</td> <!-- GermanQuAD -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.11.0</td> <!-- SB10k version -->
   <td>12.11.0</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.05</td> <!-- ScandEval rank -->
   <td class="de ner">56.00 ± 1.94 / 43.49 ± 2.05</td> <!-- GermEval -->
   <td class="de sent">56.40 ± 3.89 / 70.17 ± 2.91</td> <!-- SB10k -->
   <td class="de la">22.01 ± 5.17 / 56.97 ± 3.54</td> <!-- ScaLA-de -->
   <td class="de rc">35.39 ± 2.49 / 64.61 ± 2.42</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>cstr/Spaetzle-v8-7b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,980 ± 1,031 / 1,714 ± 552</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="de ner">58.90 ± 2.30 / 45.55 ± 3.30</td> <!-- GermEval -->
   <td class="de sent">61.34 ± 1.90 / 72.98 ± 1.30</td> <!-- SB10k -->
   <td class="de la">31.58 ± 4.39 / 65.51 ± 2.23</td> <!-- ScaLA-de -->
   <td class="de rc">24.91 ± 3.98 / 60.88 ± 3.31</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,584 ± 217 / 635 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.07</td> <!-- ScandEval rank -->
   <td class="de ner">55.76 ± 1.16 / 40.04 ± 3.21</td> <!-- GermEval -->
   <td class="de sent">55.91 ± 2.49 / 70.31 ± 1.76</td> <!-- SB10k -->
   <td class="de la">22.47 ± 3.37 / 56.77 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de rc">35.95 ± 1.89 / 66.86 ± 2.33</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="de ner">62.39 ± 2.72 / 50.86 ± 2.31</td> <!-- GermEval -->
   <td class="de sent">53.16 ± 3.17 / 64.24 ± 3.42</td> <!-- SB10k -->
   <td class="de la">31.81 ± 5.15 / 62.15 ± 4.02</td> <!-- ScaLA-de -->
   <td class="de rc">28.99 ± 2.22 / 60.53 ± 2.92</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="de ner">64.81 ± 3.03 / 53.01 ± 3.41</td> <!-- GermEval -->
   <td class="de sent">59.60 ± 2.81 / 72.42 ± 1.83</td> <!-- SB10k -->
   <td class="de la">27.06 ± 4.53 / 63.33 ± 2.30</td> <!-- ScaLA-de -->
   <td class="de rc">25.22 ± 3.84 / 60.93 ± 2.99</td> <!-- GermanQuAD -->
   <td>9.3.2</td> <!-- GermEval version -->
   <td>9.3.2</td> <!-- SB10k version -->
   <td>9.3.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-uncased</td> <!-- Model ID -->
   <td class="num_model_parameters">168</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">106</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">13,993 ± 3,217 / 2,752 ± 893</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="de ner">77.50 ± 0.62 / 75.76 ± 0.94</td> <!-- GermEval -->
   <td class="de sent">43.25 ± 2.74 / 61.05 ± 2.91</td> <!-- SB10k -->
   <td class="de la">51.74 ± 4.31 / 74.76 ± 2.15</td> <!-- ScaLA-de -->
   <td class="de rc">17.83 ± 1.29 / 39.43 ± 1.61</td> <!-- GermanQuAD -->
   <td>12.10.1</td> <!-- GermEval version -->
   <td>12.10.1</td> <!-- SB10k version -->
   <td>12.10.1</td> <!-- ScaLA-de version -->
   <td>12.10.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">2.12</td> <!-- ScandEval rank -->
   <td class="de ner">59.68 ± 0.41 / 48.00 ± 2.44</td> <!-- GermEval -->
   <td class="de sent">54.75 ± 2.36 / 68.54 ± 1.62</td> <!-- SB10k -->
   <td class="de la">30.22 ± 2.94 / 64.51 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">29.27 ± 1.03 / 59.19 ± 2.46</td> <!-- GermanQuAD -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="de ner">39.88 ± 2.56 / 35.40 ± 2.63</td> <!-- GermEval -->
   <td class="de sent">56.23 ± 3.17 / 68.87 ± 2.73</td> <!-- SB10k -->
   <td class="de la">32.71 ± 1.60 / 64.55 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">36.58 ± 2.81 / 64.92 ± 2.97</td> <!-- GermanQuAD -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.18</td> <!-- ScandEval rank -->
   <td class="de ner">64.38 ± 1.60 / 50.26 ± 2.53</td> <!-- GermEval -->
   <td class="de sent">54.44 ± 1.45 / 69.32 ± 1.02</td> <!-- SB10k -->
   <td class="de la">26.03 ± 2.23 / 61.88 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">25.68 ± 2.81 / 62.48 ± 2.93</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ZurichNLP/unsup-simcse-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,520 ± 7,443 / 6,730 ± 2,224</td> <!-- Model inference speed -->
   <td class="rank">2.19</td> <!-- ScandEval rank -->
   <td class="de ner">74.50 ± 1.06 / 74.21 ± 0.83</td> <!-- GermEval -->
   <td class="de sent">58.23 ± 1.13 / 72.00 ± 0.75</td> <!-- SB10k -->
   <td class="de la">34.74 ± 14.22 / 64.18 ± 7.54</td> <!-- ScaLA-de -->
   <td class="de rc">11.19 ± 3.07 / 26.81 ± 6.54</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.20</td> <!-- ScandEval rank -->
   <td class="de ner">55.37 ± 1.32 / 44.65 ± 2.48</td> <!-- GermEval -->
   <td class="de sent">54.27 ± 1.71 / 68.13 ± 1.16</td> <!-- SB10k -->
   <td class="de la">23.12 ± 4.07 / 57.81 ± 3.70</td> <!-- ScaLA-de -->
   <td class="de rc">31.89 ± 3.29 / 59.77 ± 4.31</td> <!-- GermanQuAD -->
   <td>9.1.2</td> <!-- GermEval version -->
   <td>9.1.2</td> <!-- SB10k version -->
   <td>9.1.2</td> <!-- ScaLA-de version -->
   <td>12.5.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>jhu-clsp/bernice</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,567 ± 450 / 2,483 ± 798</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="de ner">72.25 ± 1.06 / 71.08 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">62.00 ± 2.11 / 74.40 ± 1.38</td> <!-- SB10k -->
   <td class="de la">48.10 ± 4.34 / 71.95 ± 3.29</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google-bert/bert-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">179</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,083 ± 3,264 / 2,738 ± 889</td> <!-- Model inference speed -->
   <td class="rank">2.25</td> <!-- ScandEval rank -->
   <td class="de ner">79.11 ± 0.83 / 77.83 ± 0.76</td> <!-- GermEval -->
   <td class="de sent">42.97 ± 2.64 / 61.71 ± 1.79</td> <!-- SB10k -->
   <td class="de la">42.66 ± 6.60 / 69.03 ± 3.13</td> <!-- ScaLA-de -->
   <td class="de rc">14.98 ± 0.98 / 35.52 ± 1.24</td> <!-- GermanQuAD -->
   <td>12.10.1</td> <!-- GermEval version -->
   <td>12.10.1</td> <!-- SB10k version -->
   <td>12.10.1</td> <!-- ScaLA-de version -->
   <td>12.10.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">130976</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="de ner">55.36 ± 0.81 / 36.14 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">53.05 ± 2.34 / 65.57 ± 1.92</td> <!-- SB10k -->
   <td class="de la">23.08 ± 1.54 / 58.65 ± 2.04</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 1.09 / 62.02 ± 2.17</td> <!-- GermanQuAD -->
   <td>12.9.1</td> <!-- GermEval version -->
   <td>12.9.1</td> <!-- SB10k version -->
   <td>12.9.1</td> <!-- ScaLA-de version -->
   <td>12.9.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.26</td> <!-- ScandEval rank -->
   <td class="de ner">55.41 ± 1.45 / 48.39 ± 1.46</td> <!-- GermEval -->
   <td class="de sent">52.58 ± 2.42 / 67.52 ± 1.82</td> <!-- SB10k -->
   <td class="de la">24.10 ± 2.12 / 59.47 ± 2.92</td> <!-- ScaLA-de -->
   <td class="de rc">31.52 ± 2.95 / 60.03 ± 3.81</td> <!-- GermanQuAD -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/xlm-align-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,744 ± 2,870 / 3,265 ± 1,053</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="de ner">79.38 ± 0.80 / 79.33 ± 0.74</td> <!-- GermEval -->
   <td class="de sent">58.58 ± 2.31 / 72.09 ± 1.64</td> <!-- SB10k -->
   <td class="de la">15.34 ± 5.24 / 52.99 ± 1.90</td> <!-- ScaLA-de -->
   <td class="de rc">16.58 ± 6.50 / 32.33 ± 11.35</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.29</td> <!-- ScandEval rank -->
   <td class="de ner">63.36 ± 2.68 / 51.59 ± 3.44</td> <!-- GermEval -->
   <td class="de sent">59.80 ± 3.18 / 72.32 ± 2.23</td> <!-- SB10k -->
   <td class="de la">22.98 ± 8.11 / 60.88 ± 3.98</td> <!-- ScaLA-de -->
   <td class="de rc">20.96 ± 3.59 / 57.36 ± 2.94</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="de ner">55.32 ± 1.55 / 48.33 ± 1.45</td> <!-- GermEval -->
   <td class="de sent">52.49 ± 2.16 / 67.50 ± 1.61</td> <!-- SB10k -->
   <td class="de la">24.34 ± 2.29 / 59.66 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">31.54 ± 3.00 / 59.96 ± 3.89</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,475 ± 7,465 / 6,712 ± 2,223</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="de ner">74.89 ± 0.86 / 73.54 ± 0.84</td> <!-- GermEval -->
   <td class="de sent">63.01 ± 1.50 / 75.21 ± 1.03</td> <!-- SB10k -->
   <td class="de la">36.60 ± 2.17 / 64.93 ± 1.39</td> <!-- ScaLA-de -->
   <td class="de rc">0.65 ± 0.25 / 5.05 ± 1.30</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">2.34</td> <!-- ScandEval rank -->
   <td class="de ner">57.57 ± 1.46 / 44.84 ± 2.12</td> <!-- GermEval -->
   <td class="de sent">49.40 ± 2.11 / 63.02 ± 2.68</td> <!-- SB10k -->
   <td class="de la">23.32 ± 2.20 / 59.16 ± 2.36</td> <!-- ScaLA-de -->
   <td class="de rc">30.24 ± 1.18 / 61.10 ± 1.87</td> <!-- GermanQuAD -->
   <td>12.11.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.11.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-de-en (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,992 ± 319 / 706 ± 211</td> <!-- Model inference speed -->
   <td class="rank">2.35</td> <!-- ScandEval rank -->
   <td class="de ner">48.11 ± 2.01 / 39.66 ± 3.29</td> <!-- GermEval -->
   <td class="de sent">54.96 ± 2.69 / 69.64 ± 2.09</td> <!-- SB10k -->
   <td class="de la">21.57 ± 4.18 / 55.63 ± 4.56</td> <!-- ScaLA-de -->
   <td class="de rc">31.49 ± 3.11 / 61.33 ± 3.41</td> <!-- GermanQuAD -->
   <td>12.3.2</td> <!-- GermEval version -->
   <td>12.3.1</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.3.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-base</td> <!-- Model ID -->
   <td class="num_model_parameters">279</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,514 ± 2,041 / 2,862 ± 918</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="de ner">70.35 ± 1.34 / 69.09 ± 1.36</td> <!-- GermEval -->
   <td class="de sent">55.03 ± 2.38 / 69.65 ± 1.75</td> <!-- SB10k -->
   <td class="de la">43.87 ± 8.85 / 69.71 ± 6.73</td> <!-- ScaLA-de -->
   <td class="de rc">2.81 ± 0.73 / 10.15 ± 2.34</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-7B-German-V0.1-DPO (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,070 ± 1,042 / 1,769 ± 573</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="de ner">48.92 ± 2.76 / 38.62 ± 2.42</td> <!-- GermEval -->
   <td class="de sent">52.57 ± 1.74 / 61.25 ± 2.84</td> <!-- SB10k -->
   <td class="de la">20.74 ± 3.20 / 56.59 ± 3.27</td> <!-- ScaLA-de -->
   <td class="de rc">32.87 ± 1.83 / 62.31 ± 2.13</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.2</td> <!-- SB10k version -->
   <td>12.3.2</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-7B-German-V0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,065 ± 1,038 / 1,766 ± 570</td> <!-- Model inference speed -->
   <td class="rank">2.37</td> <!-- ScandEval rank -->
   <td class="de ner">48.35 ± 2.96 / 38.58 ± 2.35</td> <!-- GermEval -->
   <td class="de sent">52.51 ± 1.72 / 61.27 ± 2.77</td> <!-- SB10k -->
   <td class="de la">20.36 ± 3.59 / 56.14 ± 3.61</td> <!-- ScaLA-de -->
   <td class="de rc">32.88 ± 1.78 / 62.19 ± 2.05</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.3.2</td> <!-- SB10k version -->
   <td>12.3.2</td> <!-- ScaLA-de version -->
   <td>12.3.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,410 ± 299 / 370 ± 127</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="de ner">41.41 ± 2.64 / 26.93 ± 1.92</td> <!-- GermEval -->
   <td class="de sent">52.78 ± 4.59 / 66.87 ± 4.26</td> <!-- SB10k -->
   <td class="de la">27.75 ± 1.14 / 63.54 ± 0.69</td> <!-- ScaLA-de -->
   <td class="de rc">29.24 ± 2.44 / 58.33 ± 3.45</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">2.38</td> <!-- ScandEval rank -->
   <td class="de ner">52.63 ± 1.89 / 42.99 ± 2.40</td> <!-- GermEval -->
   <td class="de sent">43.16 ± 4.45 / 57.79 ± 4.61</td> <!-- SB10k -->
   <td class="de la">27.09 ± 1.92 / 60.29 ± 1.99</td> <!-- ScaLA-de -->
   <td class="de rc">34.01 ± 4.01 / 63.29 ± 3.97</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.2.0</td> <!-- SB10k version -->
   <td>12.3.1</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="de ner">52.08 ± 1.86 / 46.67 ± 1.17</td> <!-- GermEval -->
   <td class="de sent">46.38 ± 2.70 / 60.32 ± 2.80</td> <!-- SB10k -->
   <td class="de la">22.39 ± 3.96 / 57.26 ± 4.22</td> <!-- ScaLA-de -->
   <td class="de rc">33.43 ± 2.38 / 62.65 ± 2.83</td> <!-- GermanQuAD -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="de ner">51.39 ± 1.35 / 44.47 ± 2.77</td> <!-- GermEval -->
   <td class="de sent">47.30 ± 4.44 / 62.28 ± 4.24</td> <!-- SB10k -->
   <td class="de la">21.83 ± 1.98 / 57.05 ± 2.18</td> <!-- ScaLA-de -->
   <td class="de rc">31.55 ± 3.67 / 60.39 ± 4.29</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>clips/mfaq</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,591 ± 187 / 3,349 ± 1,105</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="de ner">76.68 ± 0.91 / 76.46 ± 0.98</td> <!-- GermEval -->
   <td class="de sent">59.51 ± 1.54 / 72.84 ± 1.06</td> <!-- SB10k -->
   <td class="de la">32.54 ± 11.48 / 60.57 ± 7.28</td> <!-- ScaLA-de -->
   <td class="de rc">1.53 ± 0.96 / 2.39 ± 1.52</td> <!-- GermanQuAD -->
   <td>0.0.0</td> <!-- GermEval version -->
   <td>0.0.0</td> <!-- SB10k version -->
   <td>0.0.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-13B-German-V0.1-DPO (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">789 ± 78 / 346 ± 102</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="de ner">52.45 ± 2.98 / 47.91 ± 2.37</td> <!-- GermEval -->
   <td class="de sent">49.73 ± 2.78 / 63.68 ± 2.80</td> <!-- SB10k -->
   <td class="de la">20.72 ± 4.25 / 53.77 ± 5.69</td> <!-- ScaLA-de -->
   <td class="de rc">30.18 ± 4.61 / 60.07 ± 5.86</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="de ner">50.66 ± 1.53 / 39.89 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">54.79 ± 3.53 / 68.79 ± 3.00</td> <!-- SB10k -->
   <td class="de la">20.17 ± 1.69 / 58.67 ± 1.13</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 4.70 / 54.38 ± 5.91</td> <!-- GermanQuAD -->
   <td>12.5.3</td> <!-- GermEval version -->
   <td>12.5.3</td> <!-- SB10k version -->
   <td>12.5.3</td> <!-- ScaLA-de version -->
   <td>12.5.3</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Twitter/twhin-bert-large</td> <!-- Model ID -->
   <td class="num_model_parameters">562</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">9,707 ± 1,664 / 2,549 ± 831</td> <!-- Model inference speed -->
   <td class="rank">2.43</td> <!-- ScandEval rank -->
   <td class="de ner">74.36 ± 1.33 / 73.61 ± 1.47</td> <!-- GermEval -->
   <td class="de sent">53.52 ± 2.28 / 68.49 ± 1.49</td> <!-- SB10k -->
   <td class="de la">22.26 ± 11.63 / 58.51 ± 6.63</td> <!-- ScaLA-de -->
   <td class="de rc">11.68 ± 4.11 / 22.54 ± 7.80</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">2.45</td> <!-- ScandEval rank -->
   <td class="de ner">57.02 ± 1.39 / 47.95 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.02 / 62.41 ± 3.30</td> <!-- SB10k -->
   <td class="de la">19.80 ± 3.22 / 52.76 ± 5.45</td> <!-- ScaLA-de -->
   <td class="de rc">27.86 ± 2.01 / 57.65 ± 2.01</td> <!-- GermanQuAD -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,002 ± 95 / 416 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.47</td> <!-- ScandEval rank -->
   <td class="de ner">59.07 ± 0.78 / 51.00 ± 2.06</td> <!-- GermEval -->
   <td class="de sent">49.75 ± 2.44 / 65.93 ± 1.66</td> <!-- SB10k -->
   <td class="de la">14.71 ± 2.21 / 53.75 ± 3.07</td> <!-- ScaLA-de -->
   <td class="de rc">29.45 ± 2.13 / 56.14 ± 2.53</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.50</td> <!-- ScandEval rank -->
   <td class="de ner">55.10 ± 1.35 / 41.89 ± 1.61</td> <!-- GermEval -->
   <td class="de sent">47.69 ± 2.35 / 64.93 ± 1.71</td> <!-- SB10k -->
   <td class="de la">24.14 ± 2.09 / 60.83 ± 1.63</td> <!-- ScaLA-de -->
   <td class="de rc">23.93 ± 2.11 / 57.64 ± 1.89</td> <!-- GermanQuAD -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM_German_7b_v1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,972 ± 315 / 689 ± 204</td> <!-- Model inference speed -->
   <td class="rank">2.57</td> <!-- ScandEval rank -->
   <td class="de ner">42.39 ± 2.43 / 32.42 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">48.67 ± 3.85 / 59.21 ± 4.18</td> <!-- SB10k -->
   <td class="de la">8.72 ± 2.15 / 43.37 ± 3.69</td> <!-- ScaLA-de -->
   <td class="de rc">36.12 ± 2.35 / 66.54 ± 2.34</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">2.58</td> <!-- ScandEval rank -->
   <td class="de ner">43.02 ± 1.93 / 32.69 ± 1.98</td> <!-- GermEval -->
   <td class="de sent">50.21 ± 2.43 / 65.81 ± 1.82</td> <!-- SB10k -->
   <td class="de la">15.79 ± 2.35 / 53.25 ± 4.45</td> <!-- ScaLA-de -->
   <td class="de rc">28.57 ± 5.09 / 55.54 ± 6.14</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">109</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">85</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,099 ± 5,881 / 5,178 ± 1,665</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="de ner">72.97 ± 0.68 / 71.83 ± 0.80</td> <!-- GermEval -->
   <td class="de sent">41.51 ± 1.91 / 60.79 ± 1.27</td> <!-- SB10k -->
   <td class="de la">45.39 ± 1.52 / 71.60 ± 0.73</td> <!-- ScaLA-de -->
   <td class="de rc">1.89 ± 0.52 / 6.88 ± 1.73</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32797</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.59</td> <!-- ScandEval rank -->
   <td class="de ner">47.19 ± 3.74 / 33.02 ± 2.09</td> <!-- GermEval -->
   <td class="de sent">47.26 ± 3.14 / 63.48 ± 2.94</td> <!-- SB10k -->
   <td class="de la">22.32 ± 1.78 / 56.73 ± 4.00</td> <!-- ScaLA-de -->
   <td class="de rc">24.36 ± 3.78 / 54.61 ± 4.44</td> <!-- GermanQuAD -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">2.60</td> <!-- ScandEval rank -->
   <td class="de ner">48.20 ± 1.57 / 39.04 ± 2.38</td> <!-- GermEval -->
   <td class="de sent">47.12 ± 4.20 / 59.69 ± 4.45</td> <!-- SB10k -->
   <td class="de la">12.39 ± 1.39 / 45.13 ± 3.93</td> <!-- ScaLA-de -->
   <td class="de rc">30.50 ± 3.67 / 57.48 ± 4.51</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="merged-model">
   <td>mayflowergmbh/Wiedervereinigung-7b-dpo (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,374 ± 432 / 744 ± 230</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="de ner">52.17 ± 2.87 / 40.26 ± 2.43</td> <!-- GermEval -->
   <td class="de sent">51.92 ± 3.19 / 67.12 ± 2.11</td> <!-- SB10k -->
   <td class="de la">29.06 ± 5.04 / 62.77 ± 2.22</td> <!-- ScaLA-de -->
   <td class="de rc">14.59 ± 2.77 / 50.41 ± 3.79</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/stsb-xlm-r-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,040 ± 2,953 / 3,417 ± 1,100</td> <!-- Model inference speed -->
   <td class="rank">2.64</td> <!-- ScandEval rank -->
   <td class="de ner">67.47 ± 1.09 / 66.34 ± 1.08</td> <!-- GermEval -->
   <td class="de sent">52.85 ± 1.53 / 68.48 ± 1.02</td> <!-- SB10k -->
   <td class="de la">29.59 ± 6.40 / 60.98 ± 2.57</td> <!-- ScaLA-de -->
   <td class="de rc">0.73 ± 0.17 / 4.35 ± 1.32</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>0.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="de ner">50.09 ± 1.33 / 38.59 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">46.52 ± 2.85 / 63.64 ± 2.10</td> <!-- SB10k -->
   <td class="de la">15.23 ± 1.71 / 55.08 ± 1.88</td> <!-- ScaLA-de -->
   <td class="de rc">25.54 ± 3.58 / 56.07 ± 3.76</td> <!-- GermanQuAD -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-xlm-r-multilingual-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,154 ± 4,438 / 3,890 ± 1,256</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="de ner">69.45 ± 0.82 / 68.02 ± 0.87</td> <!-- GermEval -->
   <td class="de sent">57.94 ± 2.12 / 71.92 ± 1.45</td> <!-- SB10k -->
   <td class="de la">21.81 ± 12.05 / 58.13 ± 4.73</td> <!-- ScaLA-de -->
   <td class="de rc">0.33 ± 0.15 / 3.03 ± 1.06</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/infoxlm-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,735 ± 7,558 / 6,846 ± 2,312</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="de ner">77.84 ± 0.92 / 77.81 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">59.16 ± 2.05 / 72.70 ± 1.38</td> <!-- SB10k -->
   <td class="de la">3.66 ± 2.14 / 49.63 ± 2.38</td> <!-- ScaLA-de -->
   <td class="de rc">3.67 ± 2.18 / 10.66 ± 4.52</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1160k</td> <!-- Model ID -->
   <td class="num_model_parameters">355</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">14,014 ± 2,384 / 3,625 ± 1,146</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="de ner">68.93 ± 1.48 / 67.48 ± 1.55</td> <!-- GermEval -->
   <td class="de sent">46.81 ± 1.79 / 64.02 ± 1.31</td> <!-- SB10k -->
   <td class="de la">3.39 ± 3.01 / 39.29 ± 4.82</td> <!-- ScaLA-de -->
   <td class="de rc">18.62 ± 1.74 / 34.87 ± 2.36</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="de ner">42.08 ± 1.65 / 36.90 ± 2.00</td> <!-- GermEval -->
   <td class="de sent">41.52 ± 3.53 / 57.69 ± 3.35</td> <!-- SB10k -->
   <td class="de la">12.78 ± 3.75 / 46.43 ± 5.48</td> <!-- ScaLA-de -->
   <td class="de rc">29.35 ± 2.51 / 59.90 ± 2.80</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-mpnet-base-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">278</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">15,100 ± 3,019 / 3,369 ± 1,103</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="de ner">65.28 ± 0.73 / 64.04 ± 0.52</td> <!-- GermEval -->
   <td class="de sent">60.29 ± 1.25 / 73.42 ± 0.83</td> <!-- SB10k -->
   <td class="de la">16.83 ± 13.26 / 56.96 ± 5.68</td> <!-- ScaLA-de -->
   <td class="de rc">0.11 ± 0.09 / 0.60 ± 0.52</td> <!-- GermanQuAD -->
   <td>12.10.1</td> <!-- GermEval version -->
   <td>12.10.1</td> <!-- SB10k version -->
   <td>12.10.1</td> <!-- ScaLA-de version -->
   <td>12.10.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/Llama3-German-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,383 ± 462 / 673 ± 210</td> <!-- Model inference speed -->
   <td class="rank">2.78</td> <!-- ScandEval rank -->
   <td class="de ner">54.34 ± 2.04 / 46.23 ± 2.24</td> <!-- GermEval -->
   <td class="de sent">58.32 ± 1.14 / 70.24 ± 0.99</td> <!-- SB10k -->
   <td class="de la">25.70 ± 5.38 / 58.58 ± 4.44</td> <!-- ScaLA-de -->
   <td class="de rc">0.50 ± 0.11 / 35.35 ± 1.23</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/roberta-large-1350k</td> <!-- Model ID -->
   <td class="num_model_parameters">354</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,744 ± 969 / 1,539 ± 492</td> <!-- Model inference speed -->
   <td class="rank">2.79</td> <!-- ScandEval rank -->
   <td class="de ner">67.24 ± 1.51 / 66.01 ± 1.32</td> <!-- GermEval -->
   <td class="de sent">45.84 ± 2.11 / 63.35 ± 1.48</td> <!-- SB10k -->
   <td class="de la">2.28 ± 1.62 / 35.18 ± 2.11</td> <!-- ScaLA-de -->
   <td class="de rc">18.17 ± 1.85 / 33.37 ± 2.80</td> <!-- GermanQuAD -->
   <td>10.0.1</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>10.0.1</td> <!-- ScaLA-de version -->
   <td>10.0.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="de ner">39.41 ± 2.30 / 36.17 ± 2.32</td> <!-- GermEval -->
   <td class="de sent">49.42 ± 4.33 / 61.57 ± 5.43</td> <!-- SB10k -->
   <td class="de la">6.02 ± 2.53 / 46.41 ± 4.35</td> <!-- ScaLA-de -->
   <td class="de rc">27.69 ± 4.39 / 54.92 ± 5.38</td> <!-- GermanQuAD -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">2.94</td> <!-- ScandEval rank -->
   <td class="de ner">34.81 ± 2.51 / 30.33 ± 2.95</td> <!-- GermEval -->
   <td class="de sent">51.01 ± 2.18 / 65.35 ± 2.23</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">25.40 ± 3.91 / 49.38 ± 4.65</td> <!-- GermanQuAD -->
   <td>12.10.8</td> <!-- GermEval version -->
   <td>12.10.8</td> <!-- SB10k version -->
   <td>12.10.8</td> <!-- ScaLA-de version -->
   <td>12.10.8</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">2.98</td> <!-- ScandEval rank -->
   <td class="de ner">37.68 ± 1.26 / 33.74 ± 1.78</td> <!-- GermEval -->
   <td class="de sent">46.00 ± 3.63 / 61.88 ± 2.94</td> <!-- SB10k -->
   <td class="de la">0.83 ± 0.84 / 33.38 ± 0.28</td> <!-- ScaLA-de -->
   <td class="de rc">26.65 ± 4.01 / 53.15 ± 4.26</td> <!-- GermanQuAD -->
   <td>12.10.5</td> <!-- GermEval version -->
   <td>12.10.5</td> <!-- SB10k version -->
   <td>12.10.5</td> <!-- ScaLA-de version -->
   <td>12.10.5</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="de ner">54.20 ± 1.00 / 48.58 ± 1.53</td> <!-- GermEval -->
   <td class="de sent">15.43 ± 3.70 / 43.11 ± 2.77</td> <!-- SB10k -->
   <td class="de la">17.49 ± 1.23 / 57.46 ± 1.12</td> <!-- ScaLA-de -->
   <td class="de rc">28.68 ± 5.36 / 60.07 ± 4.46</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-base-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">111</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,047 ± 4,407 / 3,844 ± 1,259</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="de ner">65.35 ± 1.08 / 63.62 ± 1.05</td> <!-- GermEval -->
   <td class="de sent">37.77 ± 2.20 / 58.20 ± 1.43</td> <!-- SB10k -->
   <td class="de la">16.07 ± 3.83 / 54.09 ± 2.44</td> <!-- ScaLA-de -->
   <td class="de rc">5.67 ± 1.14 / 16.63 ± 2.52</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>EuropeanParliament/EUBERT</td> <!-- Model ID -->
   <td class="num_model_parameters">94</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">66</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">20,070 ± 3,977 / 4,400 ± 1,435</td> <!-- Model inference speed -->
   <td class="rank">3.04</td> <!-- ScandEval rank -->
   <td class="de ner">49.95 ± 0.72 / 49.10 ± 0.71</td> <!-- GermEval -->
   <td class="de sent">40.29 ± 2.70 / 59.76 ± 1.78</td> <!-- SB10k -->
   <td class="de la">25.88 ± 6.61 / 61.54 ± 3.28</td> <!-- ScaLA-de -->
   <td class="de rc">2.59 ± 0.71 / 8.94 ± 2.03</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="de ner">49.38 ± 2.20 / 42.66 ± 3.24</td> <!-- GermEval -->
   <td class="de sent">41.72 ± 4.07 / 60.45 ± 3.07</td> <!-- SB10k -->
   <td class="de la">7.67 ± 1.52 / 46.66 ± 3.23</td> <!-- ScaLA-de -->
   <td class="de rc">13.70 ± 2.43 / 30.21 ± 3.80</td> <!-- GermanQuAD -->
   <td>13.0.0</td> <!-- GermEval version -->
   <td>13.0.0</td> <!-- SB10k version -->
   <td>13.0.0</td> <!-- ScaLA-de version -->
   <td>13.0.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="de ner">31.52 ± 2.96 / 29.20 ± 1.88</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 3.29 / 53.66 ± 3.20</td> <!-- SB10k -->
   <td class="de la">3.27 ± 2.51 / 34.30 ± 1.29</td> <!-- ScaLA-de -->
   <td class="de rc">27.55 ± 3.12 / 57.60 ± 3.34</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">118</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">29,201 ± 6,282 / 6,045 ± 2,027</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="de ner">60.54 ± 1.96 / 59.68 ± 1.94</td> <!-- GermEval -->
   <td class="de sent">54.99 ± 2.05 / 70.00 ± 1.37</td> <!-- SB10k -->
   <td class="de la">0.52 ± 2.01 / 49.40 ± 1.06</td> <!-- ScaLA-de -->
   <td class="de rc">0.80 ± 0.23 / 7.76 ± 2.10</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-medium-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">42</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">24,291 ± 4,887 / 5,096 ± 1,655</td> <!-- Model inference speed -->
   <td class="rank">3.12</td> <!-- ScandEval rank -->
   <td class="de ner">61.09 ± 1.60 / 58.40 ± 1.55</td> <!-- GermEval -->
   <td class="de sent">39.91 ± 2.58 / 59.74 ± 1.80</td> <!-- SB10k -->
   <td class="de la">17.16 ± 2.71 / 53.58 ± 1.55</td> <!-- ScaLA-de -->
   <td class="de rc">3.26 ± 0.68 / 12.02 ± 2.33</td> <!-- GermanQuAD -->
   <td>12.10.1</td> <!-- GermEval version -->
   <td>12.10.1</td> <!-- SB10k version -->
   <td>12.10.1</td> <!-- ScaLA-de version -->
   <td>12.10.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.14</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">52.66 ± 2.45 / 67.63 ± 1.87</td> <!-- SB10k -->
   <td class="de la">7.33 ± 2.53 / 37.69 ± 2.51</td> <!-- ScaLA-de -->
   <td class="de rc">30.05 ± 1.59 / 57.13 ± 2.48</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/quora-distilbert-multilingual</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">26,458 ± 5,992 / 5,274 ± 1,731</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="de ner">64.12 ± 0.92 / 62.50 ± 0.85</td> <!-- GermEval -->
   <td class="de sent">49.66 ± 1.68 / 66.33 ± 1.12</td> <!-- SB10k -->
   <td class="de la">0.58 ± 1.23 / 49.27 ± 0.86</td> <!-- ScaLA-de -->
   <td class="de rc">0.05 ± 0.06 / 0.36 ± 0.30</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,753 ± 8,349 / 5,937 ± 1,946</td> <!-- Model inference speed -->
   <td class="rank">3.18</td> <!-- ScandEval rank -->
   <td class="de ner">63.78 ± 0.75 / 62.34 ± 0.64</td> <!-- GermEval -->
   <td class="de sent">49.69 ± 1.56 / 66.32 ± 1.07</td> <!-- SB10k -->
   <td class="de la">0.74 ± 0.83 / 48.97 ± 0.85</td> <!-- ScaLA-de -->
   <td class="de rc">0.02 ± 0.02 / 0.20 ± 0.17</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32797</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">47.67 ± 2.82 / 60.09 ± 3.28</td> <!-- SB10k -->
   <td class="de la">9.67 ± 2.79 / 46.35 ± 4.48</td> <!-- ScaLA-de -->
   <td class="de rc">26.23 ± 3.79 / 53.16 ± 4.52</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">3.31</td> <!-- ScandEval rank -->
   <td class="de ner">34.53 ± 1.24 / 29.89 ± 1.96</td> <!-- GermEval -->
   <td class="de sent">42.90 ± 2.66 / 56.64 ± 4.71</td> <!-- SB10k -->
   <td class="de la">1.51 ± 1.64 / 43.36 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">15.83 ± 1.42 / 29.77 ± 2.54</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="de ner">19.29 ± 5.77 / 20.20 ± 3.59</td> <!-- GermEval -->
   <td class="de sent">43.88 ± 3.42 / 61.04 ± 2.69</td> <!-- SB10k -->
   <td class="de la">5.63 ± 1.32 / 49.95 ± 1.54</td> <!-- ScaLA-de -->
   <td class="de rc">17.02 ± 2.10 / 36.47 ± 2.53</td> <!-- GermanQuAD -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="de ner">24.35 ± 1.72 / 21.90 ± 0.85</td> <!-- GermEval -->
   <td class="de sent">43.35 ± 3.81 / 60.49 ± 3.18</td> <!-- SB10k -->
   <td class="de la">2.38 ± 1.21 / 37.27 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">15.56 ± 2.24 / 34.68 ± 3.15</td> <!-- GermanQuAD -->
   <td>12.7.0</td> <!-- GermEval version -->
   <td>12.7.0</td> <!-- SB10k version -->
   <td>12.7.0</td> <!-- ScaLA-de version -->
   <td>12.7.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>VAGOsolutions/SauerkrautLM-Gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,607 ± 565 / 1,212 ± 349</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="de ner">12.21 ± 2.76 / 11.93 ± 2.08</td> <!-- GermEval -->
   <td class="de sent">44.84 ± 2.70 / 57.27 ± 3.65</td> <!-- SB10k -->
   <td class="de la">2.02 ± 2.19 / 37.47 ± 3.26</td> <!-- ScaLA-de -->
   <td class="de rc">24.59 ± 2.70 / 49.79 ± 2.96</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="de ner">28.04 ± 2.71 / 24.08 ± 1.58</td> <!-- GermEval -->
   <td class="de sent">36.21 ± 3.42 / 54.82 ± 3.32</td> <!-- SB10k -->
   <td class="de la">3.12 ± 1.42 / 46.21 ± 2.93</td> <!-- ScaLA-de -->
   <td class="de rc">16.33 ± 3.22 / 41.91 ± 4.34</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="de ner">36.62 ± 1.56 / 28.22 ± 1.66</td> <!-- GermEval -->
   <td class="de sent">28.54 ± 2.70 / 50.10 ± 1.65</td> <!-- SB10k -->
   <td class="de la">1.15 ± 1.66 / 38.16 ± 2.78</td> <!-- ScaLA-de -->
   <td class="de rc">23.39 ± 1.00 / 51.61 ± 1.04</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.4.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v2</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">33,247 ± 8,123 / 6,017 ± 1,977</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="de ner">41.82 ± 3.25 / 42.03 ± 3.15</td> <!-- GermEval -->
   <td class="de sent">49.38 ± 1.72 / 66.10 ± 1.17</td> <!-- SB10k -->
   <td class="de la">4.77 ± 2.08 / 49.48 ± 2.07</td> <!-- ScaLA-de -->
   <td class="de rc">0.05 ± 0.06 / 0.92 ± 0.55</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">19,206 ± 4,451 / 3,658 ± 1,187</td> <!-- Model inference speed -->
   <td class="rank">3.38</td> <!-- ScandEval rank -->
   <td class="de ner">40.20 ± 3.20 / 40.33 ± 3.13</td> <!-- GermEval -->
   <td class="de sent">48.71 ± 1.60 / 65.32 ± 1.57</td> <!-- SB10k -->
   <td class="de la">5.53 ± 1.92 / 51.10 ± 1.38</td> <!-- ScaLA-de -->
   <td class="de rc">0.06 ± 0.06 / 1.12 ± 1.10</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="de ner">16.95 ± 2.96 / 15.80 ± 2.16</td> <!-- GermEval -->
   <td class="de sent">44.96 ± 3.30 / 61.27 ± 2.88</td> <!-- SB10k -->
   <td class="de la">0.77 ± 1.22 / 33.68 ± 0.59</td> <!-- ScaLA-de -->
   <td class="de rc">17.92 ± 4.72 / 40.68 ± 6.34</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">3.42</td> <!-- ScandEval rank -->
   <td class="de ner">30.85 ± 4.69 / 24.38 ± 3.10</td> <!-- GermEval -->
   <td class="de sent">49.77 ± 2.81 / 64.87 ± 2.42</td> <!-- SB10k -->
   <td class="de la">2.67 ± 1.77 / 41.55 ± 4.54</td> <!-- ScaLA-de -->
   <td class="de rc">4.09 ± 1.94 / 12.70 ± 2.66</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.46</td> <!-- ScandEval rank -->
   <td class="de ner">36.17 ± 2.52 / 27.29 ± 1.74</td> <!-- GermEval -->
   <td class="de sent">34.17 ± 7.08 / 46.97 ± 8.28</td> <!-- SB10k -->
   <td class="de la">2.21 ± 1.64 / 38.29 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 3.04 / 30.89 ± 4.33</td> <!-- GermanQuAD -->
   <td>12.9.0</td> <!-- GermEval version -->
   <td>12.9.0</td> <!-- SB10k version -->
   <td>12.9.0</td> <!-- ScaLA-de version -->
   <td>12.9.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="de ner">27.22 ± 1.38 / 24.48 ± 1.76</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 5.06 / 49.68 ± 5.74</td> <!-- SB10k -->
   <td class="de la">0.45 ± 0.91 / 35.24 ± 3.71</td> <!-- ScaLA-de -->
   <td class="de rc">20.44 ± 3.29 / 45.50 ± 3.33</td> <!-- GermanQuAD -->
   <td>9.3.1</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>9.3.1</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>sentence-transformers/distiluse-base-multilingual-cased-v1</td> <!-- Model ID -->
   <td class="num_model_parameters">135</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">120</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">34,042 ± 8,482 / 5,951 ± 1,950</td> <!-- Model inference speed -->
   <td class="rank">3.49</td> <!-- ScandEval rank -->
   <td class="de ner">28.29 ± 6.50 / 27.54 ± 6.33</td> <!-- GermEval -->
   <td class="de sent">51.70 ± 1.63 / 67.81 ± 1.08</td> <!-- SB10k -->
   <td class="de la">2.12 ± 2.30 / 49.13 ± 2.33</td> <!-- ScaLA-de -->
   <td class="de rc">0.03 ± 0.05 / 0.69 ± 0.53</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>DiscoResearch/DiscoLM-70b (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">291 ± 23 / 163 ± 39</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="de ner">62.16 ± 2.83 / 48.46 ± 3.31</td> <!-- GermEval -->
   <td class="de sent">27.56 ± 3.62 / 47.04 ± 4.06</td> <!-- SB10k -->
   <td class="de la">0.59 ± 1.16 / 32.41 ± 0.74</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 4.44 ± 0.39</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="de ner">25.69 ± 1.43 / 25.95 ± 1.23</td> <!-- GermEval -->
   <td class="de sent">33.48 ± 2.83 / 47.14 ± 4.43</td> <!-- SB10k -->
   <td class="de la">3.73 ± 1.14 / 44.43 ± 4.17</td> <!-- ScaLA-de -->
   <td class="de rc">14.82 ± 2.69 / 35.50 ± 3.15</td> <!-- GermanQuAD -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="de ner">9.23 ± 4.86 / 10.43 ± 3.83</td> <!-- GermEval -->
   <td class="de sent">38.30 ± 2.90 / 56.94 ± 2.83</td> <!-- SB10k -->
   <td class="de la">0.39 ± 1.17 / 33.47 ± 0.34</td> <!-- ScaLA-de -->
   <td class="de rc">16.67 ± 3.02 / 41.61 ± 3.00</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>seedboxai/KafkaLM-70B-German-V0.1 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4125</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">294 ± 21 / 168 ± 42</td> <!-- Model inference speed -->
   <td class="rank">3.74</td> <!-- ScandEval rank -->
   <td class="de ner">59.23 ± 2.95 / 52.06 ± 3.03</td> <!-- GermEval -->
   <td class="de sent">-5.01 ± 4.03 / 18.00 ± 0.71</td> <!-- SB10k -->
   <td class="de la">3.19 ± 4.99 / 37.63 ± 3.16</td> <!-- ScaLA-de -->
   <td class="de rc">19.84 ± 2.17 / 56.60 ± 3.00</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-mini-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">12</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">47,122 ± 9,661 / 9,714 ± 3,152</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="de ner">38.71 ± 2.23 / 36.92 ± 1.95</td> <!-- GermEval -->
   <td class="de sent">34.21 ± 2.42 / 55.54 ± 1.69</td> <!-- SB10k -->
   <td class="de la">1.59 ± 1.31 / 49.57 ± 1.09</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>dbmdz/bert-tiny-historic-multilingual-cased</td> <!-- Model ID -->
   <td class="num_model_parameters">5</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">78,027 ± 15,466 / 17,064 ± 5,335</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="de ner">33.18 ± 2.13 / 32.48 ± 2.13</td> <!-- GermEval -->
   <td class="de sent">33.61 ± 2.23 / 55.01 ± 2.11</td> <!-- SB10k -->
   <td class="de la">1.83 ± 1.54 / 49.40 ± 1.24</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>3ebdola/Dialectal-Arabic-XLM-R-Base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">12,783 ± 2,537 / 2,712 ± 885</td> <!-- Model inference speed -->
   <td class="rank">3.83</td> <!-- ScandEval rank -->
   <td class="de ner">30.18 ± 6.85 / 29.11 ± 6.64</td> <!-- GermEval -->
   <td class="de sent">32.66 ± 3.87 / 53.17 ± 4.09</td> <!-- SB10k -->
   <td class="de la">2.10 ± 1.30 / 47.10 ± 2.29</td> <!-- ScaLA-de -->
   <td class="de rc">0.46 ± 0.39 / 4.04 ± 2.36</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">3.95</td> <!-- ScandEval rank -->
   <td class="de ner">14.06 ± 5.31 / 12.90 ± 4.52</td> <!-- GermEval -->
   <td class="de sent">28.07 ± 6.33 / 38.61 ± 7.42</td> <!-- SB10k -->
   <td class="de la">2.31 ± 1.88 / 44.45 ± 4.23</td> <!-- ScaLA-de -->
   <td class="de rc">6.89 ± 2.35 / 17.95 ± 3.37</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.5.2</td> <!-- SB10k version -->
   <td>12.5.2</td> <!-- ScaLA-de version -->
   <td>12.5.2</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.03</td> <!-- ScandEval rank -->
   <td class="de ner">24.67 ± 0.99 / 23.98 ± 0.73</td> <!-- GermEval -->
   <td class="de sent">9.31 ± 2.97 / 21.50 ± 2.70</td> <!-- SB10k -->
   <td class="de la">1.11 ± 1.69 / 37.88 ± 4.05</td> <!-- ScaLA-de -->
   <td class="de rc">13.60 ± 1.60 / 29.10 ± 1.94</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>11.0.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.5.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="de ner">27.34 ± 1.95 / 24.46 ± 1.25</td> <!-- GermEval -->
   <td class="de sent">10.64 ± 5.31 / 26.79 ± 4.73</td> <!-- SB10k -->
   <td class="de la">0.33 ± 1.20 / 35.20 ± 2.45</td> <!-- ScaLA-de -->
   <td class="de rc">11.81 ± 2.10 / 27.38 ± 2.49</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>10.0.1</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2080</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.20</td> <!-- ScandEval rank -->
   <td class="de ner">21.46 ± 2.04 / 20.83 ± 1.63</td> <!-- GermEval -->
   <td class="de sent">21.03 ± 6.33 / 38.33 ± 7.79</td> <!-- SB10k -->
   <td class="de la">0.13 ± 1.48 / 43.17 ± 4.90</td> <!-- ScaLA-de -->
   <td class="de rc">0.71 ± 0.53 / 6.02 ± 1.37</td> <!-- GermanQuAD -->
   <td>12.5.2</td> <!-- GermEval version -->
   <td>12.1.0</td> <!-- SB10k version -->
   <td>12.1.0</td> <!-- ScaLA-de version -->
   <td>12.1.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-xlm-roberta-base</td> <!-- Model ID -->
   <td class="num_model_parameters">277</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">250</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,214 ± 94 / 1,494 ± 229</td> <!-- Model inference speed -->
   <td class="rank">4.24</td> <!-- ScandEval rank -->
   <td class="de ner">8.03 ± 1.35 / 8.63 ± 1.36</td> <!-- GermEval -->
   <td class="de sent">23.44 ± 7.21 / 42.87 ± 7.78</td> <!-- SB10k -->
   <td class="de la">-0.17 ± 1.13 / 39.21 ± 4.70</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>12.6.1</td> <!-- GermEval version -->
   <td>12.6.1</td> <!-- SB10k version -->
   <td>12.6.1</td> <!-- ScaLA-de version -->
   <td>12.6.1</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>fresh-electra-small</td> <!-- Model ID -->
   <td class="num_model_parameters">13</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">31</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,840 ± 1,538 / 3,024 ± 438</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="de ner">9.53 ± 0.71 / 9.93 ± 0.76</td> <!-- GermEval -->
   <td class="de sent">13.29 ± 8.29 / 29.94 ± 8.32</td> <!-- SB10k -->
   <td class="de la">-0.15 ± 0.77 / 33.37 ± 0.37</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermanQuAD -->
   <td>12.8.0</td> <!-- GermEval version -->
   <td>12.8.0</td> <!-- SB10k version -->
   <td>12.8.0</td> <!-- ScaLA-de version -->
   <td>12.8.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">4.68</td> <!-- ScandEval rank -->
   <td class="de ner">5.80 ± 1.56 / 5.41 ± 1.56</td> <!-- GermEval -->
   <td class="de sent">4.45 ± 1.73 / 29.26 ± 3.66</td> <!-- SB10k -->
   <td class="de la">-0.48 ± 1.33 / 43.09 ± 3.56</td> <!-- ScaLA-de -->
   <td class="de rc">0.08 ± 0.12 / 4.02 ± 1.17</td> <!-- GermanQuAD -->
   <td>12.10.4</td> <!-- GermEval version -->
   <td>12.10.4</td> <!-- SB10k version -->
   <td>12.10.4</td> <!-- ScaLA-de version -->
   <td>12.10.4</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">541</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">4.83</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.00 ± 0.00 / 17.05 ± 0.35</td> <!-- SB10k -->
   <td class="de la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 14.17 ± 0.79</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2077</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">4.83</td> <!-- ScandEval rank -->
   <td class="de ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- GermEval -->
   <td class="de sent">0.19 ± 1.24 / 17.20 ± 1.22</td> <!-- SB10k -->
   <td class="de la">-0.12 ± 0.91 / 36.65 ± 3.92</td> <!-- ScaLA-de -->
   <td class="de rc">0.00 ± 0.00 / 1.29 ± 0.49</td> <!-- GermanQuAD -->
   <td>12.10.0</td> <!-- GermEval version -->
   <td>12.10.0</td> <!-- SB10k version -->
   <td>12.10.0</td> <!-- ScaLA-de version -->
   <td>12.10.0</td> <!-- GermanQuAD version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/german-nlu-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;German NLU&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-qBtwv&quot; src=&quot;https://datawrapper.dwcdn.net/qBtwv/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
