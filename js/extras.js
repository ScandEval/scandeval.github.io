// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Show merged models when checkbox is checked
var input = document.getElementById('merged-models-checkbox')
if (input) {
  var filterMergedModels = function() {
    var mergedModels = document.getElementsByClassName('merged-model');
    for (var i = 0; i < mergedModels.length; i++) {
      mergedModels[i].style.display = input.checked ? 'table-row' : 'none';
    }
  }
  input.addEventListener('change', filterMergedModels)
  filterMergedModels()
}

// Sort the language model benchmark by the Score column
scoreColumn = document.getElementById('score-col')
if(scoreColumn){
  var click = new MouseEvent("click", {
      view: window,
      bubbles: true,
      cancelable: true,
      clientX: 20,
  });
  scoreColumn.dispatchEvent(click);
}
