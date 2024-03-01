// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function updateBackgroundColors() {
  var table = document.getElementsByTagName('tbody')[0];
  if (table) {
    var rows = table.getElementsByTagName('tr');
    var bgColours = ['rgb(255,255,255)', 'rgb(228,228,228)'];
    var bgColour = bgColours[0];
    var mergedColor = 'rgba(255,194,194,0.4)';
    for (var i = 0; i < rows.length; i++) {
      if (rows[i].style.display !== 'none') {
        if (rows[i].classList.contains('merged-model')) {
          rows[i].style.backgroundColor = mergedColor;
        } else {
          rows[i].style.backgroundColor = bgColour;
          bgColour = bgColours[bgColours.indexOf(bgColour) ^ 1];
        }
      }
    }
  }
}

// Show merged models when checkbox is checked
var input = document.getElementById('merged-models-checkbox')
if (input) {
  var filterMergedModels = function() {
    var mergedModels = document.getElementsByClassName('merged-model');
    for (var i = 0; i < mergedModels.length; i++) {
      mergedModels[i].style.display = input.checked ? 'table-row' : 'none';
    }
    updateBackgroundColors()
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

// Sort the language model benchmark by the Rank column
rankColumn = document.getElementById('rank-col')
if(rankColumn){
  var click = new MouseEvent("click", {
      view: window,
      bubbles: true,
      cancelable: true,
      clientX: 20,
  });
  rankColumn.dispatchEvent(click);
  rankColumn.dispatchEvent(click);
}
