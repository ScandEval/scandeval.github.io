// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

var benchmarks = [
  ['mainland-scandinavian-nlu-benchmark', ['da', 'no', 'sv'], ['ner', 'sent', 'la', 'qa']],
  ['mainland-scandinavian-nlg-benchmark', ['da', 'no', 'sv'], ['ner', 'sent', 'la', 'qa', 'summ', 'know', 'reason']],
  ['insular-scandinavian-nlu-benchmark', ['is', 'fo'], ['ner', 'sent', 'la', 'qa']],
  ['insular-scandinavian-nlg-benchmark', ['is', 'fo'], ['ner', 'sent', 'la', 'qa', 'summ', 'know', 'reason']],
  ['german-nlu-benchmark', ['de'], ['ner', 'sent', 'la', 'qa']],
  ['german-nlg-benchmark', ['de'], ['ner', 'sent', 'la', 'qa', 'summ', 'know', 'reason']],
  ['dutch-nlu-benchmark', ['nl'], ['ner', 'sent', 'la', 'qa']],
  ['dutch-nlg-benchmark', ['nl'], ['ner', 'sent', 'la', 'qa', 'summ', 'know', 'reason']],
  ['english-nlu-benchmark', ['en'], ['ner', 'sent', 'la', 'qa']],
  ['english-nlg-benchmark', ['en'], ['ner', 'sent', 'la', 'qa', 'summ', 'know', 'reason']],
]

  // Sort the language model benchmark by the Score column
for (var benchmark_idx=0; benchmark_idx < benchmarks.length; benchmark_idx++){
  var click = new MouseEvent("click", {
      view: window,
      bubbles: true,
      cancelable: true,
      clientX: 20,
  });
  var benchmarkName = benchmarks[benchmark_idx][0]
  benchmark = document.getElementById(benchmarkName)
  if(benchmark){
      document.getElementById('score-col').dispatchEvent(click);
  }
}
