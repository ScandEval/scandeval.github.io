// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


// Set the background colors of the rows in the leaderboards
var table = document.getElementsByTagName('tbody')[0];
if (table) {
  var rows = table.getElementsByTagName('tr');
  var bgColours = ['rgb(255,255,255)', 'rgb(228,228,228)'];
  var bgColour = bgColours[0];
  var mergedColor = 'rgb(255,194,194)';
  for (var i = 0; i < rows.length; i++) {
    if (rows[i].classList.contains('merged-model')) {
      rows[i].style.backgroundColor = mergedColor;
    } else {
      rows[i].style.backgroundColor = bgColour;
      bgColour = bgColours[bgColours.indexOf(bgColour) ^ 1];
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
  }
  input.addEventListener('change', filterMergedModels)
  filterMergedModels()
}
