---
layout: leaderboard
title: Pretrained Benchmark
---

<div class="table-wrapper centered">
<table id="pretrained-leaderboard" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model size, in megabytes">Size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model inference speed, in samples per second">Speed</span></th>
   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score - Macro-average across tasks">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score - Macro-average across tasks">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score - Macro-average across tasks">SV</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Icelandic score - Macro-average across tasks">IS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Faroese score - Macro-average across tasks">FO</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total NER tagging score - Macro-average across languages">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total POS tagging score - Macro-average across languages">POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total dependency parsing score - Macro-average across languages">DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total classification score - Macro-average across languages">CLF</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish NER tagging - Micro-F1 / Micro-F1 without MISC tags">DaNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish POS tagging - Accuracy">DDT-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish dependency parsing - LAS / UAS">DDT-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">AngryTweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">TwitterSent</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">Europarl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">LCC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish hate speech classification - Macro-F1">DKHate</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NB</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NN</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål POS tagging - Accuracy">NDT-NB-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk POS tagging - Accuracy">NDT-NN-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål dependency parsing - LAS / UAS">NDT-NB-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk dependency parsing - LAS / UAS">NDT-NN-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Macro-F1">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian dialect classification - Macro-F1">NorDial</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish NER tagging - Micro-F1 / Micro-F1 without MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish POS tagging - Accuracy">SDT-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish dependency parsing - LAS / UAS">SDT-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish correct grammar classification - Macro-F1">DaLaJ</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish immigration sentiment classification - Macro-F1">ABSAbank-Imm</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic NER tagging - Micro-F1">MIM-GOLD-NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic POS tagging - Accuracy">IDT-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic dependency parsing - LAS / UAS">IDT-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Macro-F1">NoReC-IS</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese NER tagging - Micro-F1">WikiANN-FO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese POS tagging - Accuracy">FDT-POS</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese dependency parsing - LAS / UAS">FDT-DEP</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Macro-F1">NoReC-FO</span></th>
  </tr>
 </thead>
 <tbody>
   <tr>
    <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
    <td class="size">424</td> <!-- Model size -->
    <td class="speed">2.78 ± 0.07</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">74.29 ± 0.34 / 77.94 ± 0.41</td> <!-- DaNE -->
    <td class="da pos">97.72 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep">61.06 ± 0.19 / 63.55 ± 0.19</td> <!-- DDT-DEP -->
    <td class="da clf">61.03 ± 0.53</td> <!-- AngryTweets -->
    <td class="da clf">61.61 ± 0.48</td> <!-- TwitterSent -->
    <td class="da clf">64.02 ± 0.64</td> <!-- Europarl -->
    <td class="da clf">59.19 ± 0.80</td> <!-- LCC -->
    <td class="da clf">70.56 ± 0.57</td> <!-- DKHate -->
    <td class="no ner">77.27 ± 0.22 / 79.72 ± 0.15</td> <!-- NorNE-NB -->
    <td class="no ner">75.54 ± 0.27 / 78.42 ± 0.28</td> <!-- NorNE-NN -->
    <td class="no pos">97.32 ± 0.04</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.47 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">79.99 ± 0.36 / 82.25 ± 0.35</td> <!-- NDT-NB-DEP -->
    <td class="no dep">71.15 ± 0.28 / 74.16 ± 0.28</td> <!-- NDT-NN-DEP -->
    <td class="no clf">57.47 ± 2.35</td> <!-- NoReC -->
    <td class="no clf">68.74 ± 1.16</td> <!-- NorDial -->
    <td class="sv ner">71.37 ± 0.15 / 74.52 ± 0.17</td> <!-- SUC3 -->
    <td class="sv pos">91.57 ± 0.05</td> <!-- SDT-POS -->
    <td class="sv dep">44.38 ± 0.21 / 48.61 ± 0.19</td> <!-- SDT-DEP -->
    <td class="sv clf">33.14 ± 0.12</td> <!-- DaLaJ -->
    <td class="sv clf">30.75 ± 0.51</td> <!-- ABSAbank-Imm -->
   </tr>
 </tbody>
</table>
</div>
