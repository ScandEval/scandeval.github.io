// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

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
