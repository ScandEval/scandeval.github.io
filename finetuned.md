---
layout: leaderboard
title: Finetuned Benchmark
---

<div class="table-wrapper centered">
<table id="finetuned-leaderboard" class="sortable fixed centered small-font">
 <thead>
   <tr>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model size, in megabytes">Size</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model inference speed, in samples per second">Speed</span></th>
     <th id="finetuned-ner-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total NER tagging score - Macro-average across languages">NER</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total POS tagging score - Macro-average across languages">POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total dependency parsing score - Macro-average across languages">DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification score - Macro-average across languages">SENT</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish hate speech classification - Macro-F1">DKHate</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian dialect classification - Macro-F1">NorDial</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish correct grammar classification - Macro-F1">DaLaJ</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish immigration sentiment classification - Macro-F1">ABSAbank-Imm</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="NER tagging - Micro-F1 / Micro-F1 without MISC tags">DaNE</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NB</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NN</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish NER tagging - Micro-F1 / Micro-F1 without MISC tags">SUC3</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic NER tagging - Micro-F1">MIM-GOLD-NER</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese NER tagging - Micro-F1">WikiANN-FO</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish POS tagging - Accuracy">DDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål POS tagging - Accuracy">NDT-NB-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk POS tagging - Accuracy">NDT-NN-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish POS tagging - Accuracy">SDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic POS tagging - Accuracy">IDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese POS tagging - Accuracy">FDT-POS</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish dependency parsing - LAS / UAS">DDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål dependency parsing - LAS / UAS">NDT-NB-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk dependency parsing - LAS / UAS">NDT-NN-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish dependency parsing - LAS / UAS">SDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic dependency parsing - LAS / UAS">IDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese dependency parsing - LAS / UAS">FDT-DEP</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">AngryTweets</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">TwitterSent</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">Europarl</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">LCC</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Macro-F1">NoReC</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Macro-F1">NoReC-IS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Macro-F1">NoReC-FO</span></th>
  </tr>
 </thead>
 <tbody>
   <tr>
    <td>spacy/da_core_news_sm</td> <!-- Model ID -->
    <td class="size">18</td> <!-- Model size -->
    <td class="speed">83.30 ± 18.90</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">66.31 ± 1.32 / 67.72 ± 1.36</td> <!-- DaNE -->
    <td class="no ner">45.91 ± 0.36 / 48.79 ± 0.39</td> <!-- NorNE-NB -->
    <td class="no ner">44.93 ± 0.54 / 49.60 ± 0.61</td> <!-- NorNE-NN -->
    <td class="sv ner">16.80 ± 0.11 / 21.72 ± 0.18</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">19.69 ± 0.64</td> <!-- WikiANN-FO -->
    <td class="da pos">94.70 ± 0.17</td> <!-- DDT-POS -->
    <td class="no pos">73.28 ± 0.13</td> <!-- NDT-NB-POS -->
    <td class="no pos">62.25 ± 0.11</td> <!-- NDT-NN-POS -->
    <td class="sv pos">53.75 ± 0.24</td> <!-- SDT-POS -->
    <td class="is pos">32.74 ± 0.43</td> <!-- IDT-POS -->
    <td class="fo pos">45.47 ± 0.42</td> <!-- FDT-POS -->
    <td class="da dep">74.41 ± 0.33 / 78.34 ± 0.28</td> <!-- DDT-DEP -->
    <td class="no dep">48.17 ± 0.29 / 59.00 ± 0.25</td> <!-- NDT-NB-DEP -->
    <td class="no dep">34.03 ± 0.25 / 46.02 ± 0.31</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">21.38 ± 0.30 / 33.22 ± 0.34</td> <!-- SDT-DEP -->
    <td class="is dep">9.62 ± 0.25 / 21.15 ± 0.43</td> <!-- IDT-DEP -->
    <td class="fo dep">14.19 ± 0.31 / 27.58 ± 0.52</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/da_core_news_md</td> <!-- Model ID -->
    <td class="size">46</td> <!-- Model size -->
    <td class="speed">78.40 ± 6.68</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">71.70 ± 1.09 / 73.47 ± 1.20</td> <!-- DaNE -->
    <td class="no ner">53.47 ± 0.33 / 56.96 ± 0.28</td> <!-- NorNE-NB -->
    <td class="no ner">37.44 ± 0.67 / 40.55 ± 0.77</td> <!-- NorNE-NN -->
    <td class="sv ner">19.34 ± 0.15 / 23.30 ± 0.17</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">16.58 ± 0.48</td> <!-- WikiANN-FO -->
    <td class="da pos">95.69 ± 0.19</td> <!-- DDT-POS -->
    <td class="no pos">76.24 ± 0.17</td> <!-- NDT-NB-POS -->
    <td class="no pos">61.98 ± 0.10</td> <!-- NDT-NN-POS -->
    <td class="sv pos">53.37 ± 0.20</td> <!-- SDT-POS -->
    <td class="is pos">31.10 ± 0.38</td> <!-- IDT-POS -->
    <td class="fo pos">41.78 ± 0.37</td> <!-- FDT-POS -->
    <td class="da dep">76.77 ± 0.34 / 80.15 ± 0.33</td> <!-- DDT-DEP -->
    <td class="no dep">52.30 ± 0.34 / 62.00 ± 0.30</td> <!-- NDT-NB-DEP -->
    <td class="no dep">35.33 ± 0.29 / 46.05 ± 0.26</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">22.41 ± 0.26 / 33.16 ± 0.27</td> <!-- SDT-DEP -->
    <td class="is dep">7.89 ± 0.26 / 18.25 ± 0.35</td> <!-- IDT-DEP -->
    <td class="fo dep">12.68 ± 0.19 / 24.04 ± 0.29</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/da_core_news_lg</td> <!-- Model ID -->
    <td class="size">547</td> <!-- Model size -->
    <td class="speed">75.67 ± 7.25</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">73.27 ± 1.09 / 76.06 ± 1.25</td> <!-- DaNE -->
    <td class="no ner">57.04 ± 0.34 / 62.39 ± 0.39</td> <!-- NorNE-NB -->
    <td class="no ner">37.68 ± 0.51 / 42.75 ± 0.64</td> <!-- NorNE-NN -->
    <td class="sv ner">20.95 ± 0.15 / 27.08 ± 0.17</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">15.39 ± 0.71</td> <!-- WikiANN-FO -->
    <td class="da pos">96.05 ± 0.14</td> <!-- DDT-POS -->
    <td class="no pos">76.55 ± 0.12</td> <!-- NDT-NB-POS -->
    <td class="no pos">61.98 ± 0.12</td> <!-- NDT-NN-POS -->
    <td class="sv pos">53.27 ± 0.23</td> <!-- SDT-POS -->
    <td class="is pos">28.56 ± 0.38</td> <!-- IDT-POS -->
    <td class="fo pos">42.82 ± 0.34</td> <!-- FDT-POS -->
    <td class="da dep">76.40 ± 0.27 / 79.98 ± 0.29</td> <!-- DDT-DEP -->
    <td class="no dep">51.85 ± 0.31 / 61.33 ± 0.27</td> <!-- NDT-NB-DEP -->
    <td class="no dep">33.14 ± 0.21 / 43.12 ± 0.24</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">21.30 ± 0.20 / 32.81 ± 0.25</td> <!-- SDT-DEP -->
    <td class="is dep">7.15 ± 0.20 / 18.32 ± 0.28</td> <!-- IDT-DEP -->
    <td class="fo dep">13.05 ± 0.14 / 23.85 ± 0.16</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/da_core_news_trf</td> <!-- Model ID -->
    <td class="size">422</td> <!-- Model size -->
    <td class="speed">4.13 ± 0.18</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">77.24 ± 1.24 / 78.83 ± 1.23</td> <!-- DaNE -->
    <td class="no ner">57.71 ± 0.47 / 64.05 ± 0.58</td> <!-- NorNE-NB -->
    <td class="no ner">30.04 ± 0.88 / 37.34 ± 0.99</td> <!-- NorNE-NN -->
    <td class="sv ner">21.93 ± 0.19 / 27.50 ± 0.23</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">26.67 ± 0.67</td> <!-- WikiANN-FO -->
    <td class="da pos">98.20 ± 0.11</td> <!-- DDT-POS -->
    <td class="no pos">84.85 ± 0.16</td> <!-- NDT-NB-POS -->
    <td class="no pos">70.08 ± 0.16</td> <!-- NDT-NN-POS -->
    <td class="sv pos">66.11 ± 0.21</td> <!-- SDT-POS -->
    <td class="is pos">20.54 ± 0.33</td> <!-- IDT-POS -->
    <td class="fo pos">35.87 ± 0.31</td> <!-- FDT-POS -->
    <td class="da dep">84.88 ± 0.36 / 87.30 ± 0.35</td> <!-- DDT-DEP -->
    <td class="no dep">67.97 ± 0.35 / 76.12 ± 0.30</td> <!-- NDT-NB-DEP -->
    <td class="no dep">50.15 ± 0.36 / 60.00 ± 0.39</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">40.67 ± 0.35 / 49.80 ± 0.47</td> <!-- SDT-DEP -->
    <td class="is dep">5.61 ± 0.12 / 14.87 ± 0.18</td> <!-- IDT-DEP -->
    <td class="fo dep">8.77 ± 0.22 / 18.25 ± 0.36</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>chcaa/da_dacy_small_trf</td> <!-- Model ID -->
    <td class="size">52</td> <!-- Model size -->
    <td class="speed">15.16 ± 0.80</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">77.00 ± 0.92 / 79.04 ± 1.03</td> <!-- DaNE -->
    <td class="no ner">47.81 ± 0.42 / 54.65 ± 0.51</td> <!-- NorNE-NB -->
    <td class="no ner">26.28 ± 0.50 / 32.65 ± 0.78</td> <!-- NorNE-NN -->
    <td class="sv ner">18.72 ± 0.10 / 24.07 ± 0.11</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">22.97 ± 0.38</td> <!-- WikiANN-FO -->
    <td class="da pos">97.95 ± 0.11</td> <!-- DDT-POS -->
    <td class="no pos">77.89 ± 0.16</td> <!-- NDT-NB-POS -->
    <td class="no pos">61.30 ± 0.12</td> <!-- NDT-NN-POS -->
    <td class="sv pos">51.52 ± 0.16</td> <!-- SDT-POS -->
    <td class="is pos">18.11 ± 0.36</td> <!-- IDT-POS -->
    <td class="fo pos">34.62 ± 0.29</td> <!-- FDT-POS -->
    <td class="da dep">82.21 ± 0.39 / 84.94 ± 0.40</td> <!-- DDT-DEP -->
    <td class="no dep">55.83 ± 0.33 / 65.25 ± 0.32</td> <!-- NDT-NB-DEP -->
    <td class="no dep">36.07 ± 0.21 / 46.22 ± 0.21</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">25.45 ± 0.23 / 35.24 ± 0.30</td> <!-- SDT-DEP -->
    <td class="is dep">4.41 ± 0.09 / 16.25 ± 0.22</td> <!-- IDT-DEP -->
    <td class="fo dep">8.63 ± 0.15 / 20.79 ± 0.30</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>chcaa/da_dacy_medium_trf</td> <!-- Model ID -->
    <td class="size">422</td> <!-- Model size -->
    <td class="speed">2.27 ± 0.07</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">76.67 ± 1.20 / 78.62 ± 1.20</td> <!-- DaNE -->
    <td class="no ner">56.99 ± 0.56 / 62.44 ± 0.63</td> <!-- NorNE-NB -->
    <td class="no ner">29.23 ± 0.68 / 35.00 ± 0.86</td> <!-- NorNE-NN -->
    <td class="sv ner">21.40 ± 0.13 / 25.44 ± 0.15</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">21.78 ± 0.64</td> <!-- WikiANN-FO -->
    <td class="da pos">97.90 ± 0.11</td> <!-- DDT-POS -->
    <td class="no pos">83.58 ± 0.14</td> <!-- NDT-NB-POS -->
    <td class="no pos">67.12 ± 0.15</td> <!-- NDT-NN-POS -->
    <td class="sv pos">53.87 ± 0.17</td> <!-- SDT-POS -->
    <td class="is pos">16.52 ± 0.28</td> <!-- IDT-POS -->
    <td class="fo pos">31.72 ± 0.26</td> <!-- FDT-POS -->
    <td class="da dep">84.35 ± 0.39 / 86.94 ± 0.36</td> <!-- DDT-DEP -->
    <td class="no dep">65.56 ± 0.29 / 74.36 ± 0.25</td> <!-- NDT-NB-DEP -->
    <td class="no dep">46.78 ± 0.26 / 57.10 ± 0.27</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">26.81 ± 0.20 / 36.77 ± 0.27</td> <!-- SDT-DEP -->
    <td class="is dep">4.06 ± 0.11 / 13.78 ± 0.21</td> <!-- IDT-DEP -->
    <td class="fo dep">7.04 ± 0.16 / 16.45 ± 0.22</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>chcaa/da_dacy_large_trf</td> <!-- Model ID -->
    <td class="size">2090</td> <!-- Model size -->
    <td class="speed">0.65 ± 0.01</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">83.61 ± 1.18 / 85.33 ± 1.08</td> <!-- DaNE -->
    <td class="no ner">78.90 ± 0.49 / 83.13 ± 0.39</td> <!-- NorNE-NB -->
    <td class="no ner">72.62 ± 0.58 / 81.73 ± 0.67</td> <!-- NorNE-NN -->
    <td class="sv ner">53.35 ± 0.17 / 63.05 ± 0.19</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">51.72 ± 0.52</td> <!-- WikiANN-FO -->
    <td class="da pos">98.50 ± 0.07</td> <!-- DDT-POS -->
    <td class="no pos">88.68 ± 0.09</td> <!-- NDT-NB-POS -->
    <td class="no pos">85.30 ± 0.16</td> <!-- NDT-NN-POS -->
    <td class="sv pos">92.21 ± 0.09</td> <!-- SDT-POS -->
    <td class="is pos">86.32 ± 0.26</td> <!-- IDT-POS -->
    <td class="fo pos">73.05 ± 0.20</td> <!-- FDT-POS -->
    <td class="da dep">87.08 ± 0.32 / 89.13 ± 0.34</td> <!-- DDT-DEP -->
    <td class="no dep">72.77 ± 0.20 / 80.02 ± 0.16</td> <!-- NDT-NB-DEP -->
    <td class="no dep">69.22 ± 0.32 / 77.53 ± 0.31</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">71.97 ± 0.36 / 79.57 ± 0.44</td> <!-- SDT-DEP -->
    <td class="is dep">42.49 ± 0.63 / 54.85 ± 0.71</td> <!-- IDT-DEP -->
    <td class="fo dep">40.63 ± 0.53 / 54.65 ± 0.50</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>radbrt/nb_nocy_trf</td> <!-- Model ID -->
    <td class="size">425</td> <!-- Model size -->
    <td class="speed">4.03 ± 0.26</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">56.82 ± 1.63 / 66.82 ± 1.56</td> <!-- DaNE -->
    <td class="no ner">68.20 ± 0.75 / 77.52 ± 0.56</td> <!-- NorNE-NB -->
    <td class="no ner">69.22 ± 1.04 / 78.98 ± 0.87</td> <!-- NorNE-NN -->
    <td class="sv ner">31.63 ± 0.29 / 37.88 ± 0.32</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">12.91 ± 0.50</td> <!-- WikiANN-FO -->
    <td class="da pos">82.45 ± 0.33</td> <!-- DDT-POS -->
    <td class="no pos">98.44 ± 0.09</td> <!-- NDT-NB-POS -->
    <td class="no pos">95.49 ± 0.15</td> <!-- NDT-NN-POS -->
    <td class="sv pos">28.52 ± 0.22</td> <!-- SDT-POS -->
    <td class="is pos">13.22 ± 0.30</td> <!-- IDT-POS -->
    <td class="fo pos">27.64 ± 0.41</td> <!-- FDT-POS -->
    <td class="da dep">59.27 ± 0.45 / 67.59 ± 0.48</td> <!-- DDT-DEP -->
    <td class="no dep">91.27 ± 0.22 / 92.75 ± 0.20</td> <!-- NDT-NB-DEP -->
    <td class="no dep">88.53 ± 0.35 / 91.05 ± 0.28</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">14.35 ± 0.16 / 18.13 ± 0.17</td> <!-- SDT-DEP -->
    <td class="is dep">2.38 ± 0.10 / 5.91 ± 0.18</td> <!-- IDT-DEP -->
    <td class="fo dep">5.47 ± 0.22 / 9.06 ± 0.32</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>pin/senda</td> <!-- Model ID -->
    <td class="size">422</td> <!-- Model size -->
    <td class="speed">2.61 ± 0.05</td> <!-- Inference speed -->
    <td class="ner-score">-</td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score"></td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">34.21 ± 0.94</td> <!-- ABSAbank-Imm -->
    <td class="da ner">-</td> <!-- DaNE -->
    <td class="no ner">-</td> <!-- NorNE-NB -->
    <td class="no ner">-</td> <!-- NorNE-NN -->
    <td class="sv ner">-</td> <!-- SUC3 -->
    <td class="is ner">-</td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">-</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">80.91 ± 0.95</td> <!-- AngryTweets -->
    <td class="da sent">71.53 ± 0.91</td> <!-- TwitterSent -->
    <td class="da sent">59.21 ± 2.13</td> <!-- Europarl -->
    <td class="da sent">61.68 ± 1.88</td> <!-- LCC -->
    <td class="no sent">34.52 ± 2.15</td> <!-- NoReC -->
    <td class="is sent">26.46 ± 0.93</td> <!-- NoReC-IS -->
    <td class="fo sent">27.18 ± 1.13</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>saattrupdan/nbailab-base-ner-scandi</td> <!-- Model ID -->
    <td class="size">676</td> <!-- Model size -->
    <td class="speed">4.16 ± 0.18</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">87.44 ± 0.81 / 89.50 ± 0.92</td> <!-- DaNE -->
    <td class="no ner">91.06 ± 0.26 / 92.65 ± 0.35</td> <!-- NorNE-NB -->
    <td class="no ner">90.42 ± 0.61 / 93.90 ± 0.56</td> <!-- NorNE-NN -->
    <td class="sv ner">88.37 ± 0.17 / 91.00 ± 0.16</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">90.22 ± 0.46</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Maltehb/-l-ctra-danish-electra-small-cased-ner-dane</td> <!-- Model ID -->
    <td class="size">52</td> <!-- Model size -->
    <td class="speed">25.43 ± 1.67</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">63.96 ± 1.54 / 73.15 ± 1.55</td> <!-- DaNE -->
    <td class="no ner">38.63 ± 0.54 / 39.89 ± 0.55</td> <!-- NorNE-NB -->
    <td class="no ner">18.47 ± 0.50 / 18.91 ± 0.52</td> <!-- NorNE-NN -->
    <td class="sv ner">23.07 ± 0.29 / 23.80 ± 0.29</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">21.96 ± 0.34</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Maltehb/-l-ctra-danish-electra-small-uncased-ner-dane</td> <!-- Model ID -->
    <td class="size">52</td> <!-- Model size -->
    <td class="speed">25.38 ± 1.67</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">70.41 ± 1.19 / 80.79 ± 1.06</td> <!-- DaNE -->
    <td class="no ner">48.76 ± 0.70 / 50.95 ± 0.75</td> <!-- NorNE-NB -->
    <td class="no ner">27.58 ± 0.61 / 28.69 ± 0.64</td> <!-- NorNE-NN -->
    <td class="sv ner">35.39 ± 0.38 / 37.38 ± 0.38</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">28.30 ± 0.29</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Maltehb/danish-bert-botxo-ner-dane</td> <!-- Model ID -->
    <td class="size">420</td> <!-- Model size -->
    <td class="speed">4.17 ± 0.13</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">69.25 ± 1.17 / 79.28 ± 1.30</td> <!-- DaNE -->
    <td class="no ner">60.57 ± 0.27 / 63.30 ± 0.31</td> <!-- NorNE-NB -->
    <td class="no ner">35.60 ± 1.19 / 37.21 ± 1.26</td> <!-- NorNE-NN -->
    <td class="sv ner">38.37 ± 0.26 / 40.43 ± 0.31</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">27.88 ± 0.48</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>RecordedFuture/Swedish-NER</td> <!-- Model ID -->
    <td class="size">474</td> <!-- Model size -->
    <td class="speed">4.23 ± 0.12</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">64.09 ± 0.97 / 72.37 ± 1.20</td> <!-- DaNE -->
    <td class="no ner">61.74 ± 0.50 / 64.40 ± 0.45</td> <!-- NorNE-NB -->
    <td class="no ner">56.67 ± 0.79 / 59.81 ± 0.84</td> <!-- NorNE-NN -->
    <td class="sv ner">66.60 ± 0.27 / 77.36 ± 0.33</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">42.16 ± 0.83</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/xx_ent_wiki_sm</td> <!-- Model ID -->
    <td class="size">11</td> <!-- Model size -->
    <td class="speed">215.86 ± 26.94</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">37.98 ± 0.97 / 42.57 ± 0.93</td> <!-- DaNE -->
    <td class="no ner">34.15 ± 0.60 / 36.10 ± 0.61</td> <!-- NorNE-NB -->
    <td class="no ner">38.05 ± 0.32 / 39.99 ± 0.50</td> <!-- NorNE-NN -->
    <td class="sv ner">13.14 ± 0.09 / 15.46 ± 0.13</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">25.83 ± 0.87</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/nb_core_news_sm</td> <!-- Model ID -->
    <td class="size">15</td> <!-- Model size -->
    <td class="speed">81.49 ± 7.81</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">51.41 ± 1.22 / 56.03 ± 1.42</td> <!-- DaNE -->
    <td class="no ner">66.33 ± 0.79 / 68.30 ± 0.84</td> <!-- NorNE-NB -->
    <td class="no ner">62.72 ± 0.68 / 63.70 ± 0.76</td> <!-- NorNE-NN -->
    <td class="sv ner">19.68 ± 0.10 / 24.18 ± 0.11</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">20.09 ± 0.71</td> <!-- WikiANN-FO -->
    <td class="da pos">77.02 ± 0.35</td> <!-- DDT-POS -->
    <td class="no pos">96.34 ± 0.08</td> <!-- NDT-NB-POS -->
    <td class="no pos">80.33 ± 0.17</td> <!-- NDT-NN-POS -->
    <td class="sv pos">57.10 ± 0.19</td> <!-- SDT-POS -->
    <td class="is pos">30.31 ± 0.45</td> <!-- IDT-POS -->
    <td class="fo pos">44.94 ± 0.36</td> <!-- FDT-POS -->
    <td class="da dep">49.35 ± 0.39 / 58.39 ± 0.49</td> <!-- DDT-DEP -->
    <td class="no dep">84.32 ± 0.14 / 87.06 ± 0.13</td> <!-- NDT-NB-DEP -->
    <td class="no dep">59.63 ± 0.38 / 67.75 ± 0.37</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">27.57 ± 0.28 / 38.27 ± 0.32</td> <!-- SDT-DEP -->
    <td class="is dep">10.06 ± 0.26 / 21.18 ± 0.38</td> <!-- IDT-DEP -->
    <td class="fo dep">16.57 ± 0.19 / 27.59 ± 0.28</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/nb_core_news_md</td> <!-- Model ID -->
    <td class="size">44</td> <!-- Model size -->
    <td class="speed">76.67	 ± 05.56</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">41.66 ± 0.68 / 45.24 ± 0.64</td> <!-- DaNE -->
    <td class="no ner">77.75 ± 0.75 / 80.98 ± 0.76</td> <!-- NorNE-NB -->
    <td class="no ner">71.40 ± 0.72 / 73.33 ± 0.78</td> <!-- NorNE-NN -->
    <td class="sv ner">20.29 ± 0.16 / 27.52 ± 0.20</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">21.05 ± 0.76</td> <!-- WikiANN-FO -->
    <td class="da pos">75.38 ± 0.31</td> <!-- DDT-POS -->
    <td class="no pos">96.92 ± 0.06</td> <!-- NDT-NB-POS -->
    <td class="no pos">82.37 ± 0.15</td> <!-- NDT-NN-POS -->
    <td class="sv pos">52.66 ± 0.11</td> <!-- SDT-POS -->
    <td class="is pos">27.57 ± 0.40</td> <!-- IDT-POS -->
    <td class="fo pos">43.16 ± 0.35</td> <!-- FDT-POS -->
    <td class="da dep">46.44 ± 0.50 / 55.31 ± 0.56</td> <!-- DDT-DEP -->
    <td class="no dep">85.70 ± 0.17 / 87.99 ± 0.15</td> <!-- NDT-NB-DEP -->
    <td class="no dep">63.80 ± 0.24 / 70.42 ± 0.28</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">25.99 ± 0.25 / 35.89 ± 0.39</td> <!-- SDT-DEP -->
    <td class="is dep">8.10 ± 0.21 / 20.02 ± 0.22</td> <!-- IDT-DEP -->
    <td class="fo dep">14.45 ± 0.32 / 25.79 ± 0.47</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>spacy/nb_core_news_lg</td> <!-- Model ID -->
    <td class="size">546</td> <!-- Model size -->
    <td class="speed">73.61 ± 6.59</td> <!-- Inference speed -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">52.38 ± 1.08 / 59.33 ± 1.28</td> <!-- DaNE -->
    <td class="no ner">78.85 ± 0.62 / 81.52 ± 0.66</td> <!-- NorNE-NB -->
    <td class="no ner">71.62 ± 0.57 / 73.90 ± 0.68</td> <!-- NorNE-NN -->
    <td class="sv ner">21.06 ± 0.15 / 26.70 ± 0.15</td> <!-- SUC3 -->
    <td class="is ner"></td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">18.17 ± 0.77</td> <!-- WikiANN-FO -->
    <td class="da pos">75.81 ± 0.34</td> <!-- DDT-POS -->
    <td class="no pos">97.05 ± 0.08</td> <!-- NDT-NB-POS -->
    <td class="no pos">81.65 ± 0.12</td> <!-- NDT-NN-POS -->
    <td class="sv pos">52.64 ± 0.13</td> <!-- SDT-POS -->
    <td class="is pos">25.64 ± 0.37</td> <!-- IDT-POS -->
    <td class="fo pos">42.52 ± 0.21</td> <!-- FDT-POS -->
    <td class="da dep">47.85 ± 0.52 / 57.16 ± 0.58</td> <!-- DDT-DEP -->
    <td class="no dep">85.81 ± 0.17 / 88.34 ± 0.14</td> <!-- NDT-NB-DEP -->
    <td class="no dep">63.77 ± 0.38 / 70.37 ± 0.36</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">26.13 ± 0.17 / 36.44 ± 0.26</td> <!-- SDT-DEP -->
    <td class="is dep">7.33 ± 0.19 / 17.94 ± 0.32</td> <!-- IDT-DEP -->
    <td class="fo dep">15.02 ± 0.25 / 25.07 ± 0.45</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>DaNLP/da-bert-tone-sentiment-polarity</td> <!-- Model ID -->
    <td class="size">422</td> <!-- Model size -->
    <td class="speed">2.87 ± 0.05</td> <!-- Inference speed -->
    <td class="ner-score">-</td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score"></td> <!-- Mean sentiment classification score -->
    <td class="da">-</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">38.17 ± 1.63</td> <!-- ABSAbank-Imm -->
    <td class="da ner">-</td> <!-- DaNE -->
    <td class="no ner">-</td> <!-- NorNE-NB -->
    <td class="no ner">-</td> <!-- NorNE-NN -->
    <td class="sv ner">-</td> <!-- SUC3 -->
    <td class="is ner">-</td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">-</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">68.89 ± 1.05</td> <!-- AngryTweets -->
    <td class="da sent">70.00 ± 0.79</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">67.11 ± 2.83</td> <!-- LCC -->
    <td class="no sent">36.08 ± 3.05</td> <!-- NoReC -->
    <td class="is sent">29.40 ± 0.55</td> <!-- NoReC-IS -->
    <td class="fo sent">32.53 ± 1.04</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Guscode/DKbert-hatespeech-detection</td> <!-- Model ID -->
    <td class="size">422</td> <!-- Model size -->
    <td class="speed">2.21 ± 0.03</td> <!-- Inference speed -->
    <td class="ner-score">-</td> <!-- Mean NER score -->
    <td class="pos-score">-</td> <!-- Mean POS score -->
    <td class="dep-score">-</td> <!-- Mean dependency parsing score -->
    <td class="sent-score">-</td> <!-- Mean sentiment classification score -->
    <td class="da">74.78 ± 2.04</td> <!-- DKHate -->
    <td class="no">-</td> <!-- NorDial -->
    <td class="sv">-</td> <!-- DaLaJ -->
    <td class="sv">-</td> <!-- ABSAbank-Imm -->
    <td class="da ner">-</td> <!-- DaNE -->
    <td class="no ner">-</td> <!-- NorNE-NB -->
    <td class="no ner">-</td> <!-- NorNE-NN -->
    <td class="sv ner">-</td> <!-- SUC3 -->
    <td class="is ner">-</td> <!-- MIM-GOLD-NER -->
    <td class="fo ner">-</td> <!-- WikiANN-FO -->
    <td class="da pos">-</td> <!-- DDT-POS -->
    <td class="no pos">-</td> <!-- NDT-NB-POS -->
    <td class="no pos">-</td> <!-- NDT-NN-POS -->
    <td class="sv pos">-</td> <!-- SDT-POS -->
    <td class="is pos">-</td> <!-- IDT-POS -->
    <td class="fo pos">-</td> <!-- FDT-POS -->
    <td class="da dep">-</td> <!-- DDT-DEP -->
    <td class="no dep">-</td> <!-- NDT-NB-DEP -->
    <td class="no dep">-</td> <!-- NDT-NN-DEP -->
    <td class="sv dep">-</td> <!-- SDT-DEP -->
    <td class="is dep">-</td> <!-- IDT-DEP -->
    <td class="fo dep">-</td> <!-- FDT-DEP -->
    <td class="da sent">-</td> <!-- AngryTweets -->
    <td class="da sent">-</td> <!-- TwitterSent -->
    <td class="da sent">-</td> <!-- Europarl -->
    <td class="da sent">-</td> <!-- LCC -->
    <td class="no sent">-</td> <!-- NoReC -->
    <td class="is sent">-</td> <!-- NoReC-IS -->
    <td class="fo sent">-</td> <!-- NoReC-FO -->
   </tr>
 </tbody>
</table>
</div>
