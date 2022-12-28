// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Get the rows in the language model benchmark and the list of tasks, so that we can
// fill in all the aggregated score columns
nlu_benchmark = document.getElementById('nlu-benchmark')
if(nlu_benchmark){
    var rows = nlu_benchmark.getElementsByTagName('tr')
    var languages = ['da', 'no', 'sv']
    var tasks = ['ner', 'sent', 'la', 'qa']

    // Loop over all rows
    for (var row_idx=0; row_idx < rows.length; row_idx++){
        var row = rows[row_idx]
        var overallScore = 0
        var overallSe = 0

        // Loop over all the tasks
        for (var task_idx=0; task_idx < tasks.length; task_idx++){
            var task = tasks[task_idx]
            var taskScoreMean = 0
            var taskSeMean = 0
            var numLanguages = 0

            // Loop over all the languages
            for (var lang_idx=0; lang_idx < languages.length; lang_idx++){
                var language = languages[lang_idx]
                var elements = row.getElementsByClassName(`${language} ${task}`)
                var languageScoreMean = 0
                var languageSeMean = 0
                var numDatasets = 0

                // Compute the language score from the row
                for (var elt_idx=0; elt_idx < elements.length; elt_idx++){
                    var value = parseFloat(elements[elt_idx]
                                           .innerHTML
                                           .replace(/ \/.*/g, '')
                                           .replace(/ ± [0-9.]+/g, ''))
                    var se = parseFloat(elements[elt_idx]
                                        .innerHTML
                                        .replace(/ \/.*/g, '')
                                        .replace(/[0-9.]+ ± /g, ''))
                    languageScoreMean += value
                    languageSeMean += se
                    numDatasets += 1
                }

                // Add the task score to the language score
                if (numDatasets > 0) {
                    taskScoreMean += languageScoreMean / numDatasets
                    taskSeMean += languageSeMean / numDatasets
                    numLanguages += 1
                }
            }

            // Set the task score in the row
            scoreElements = row.getElementsByClassName(`${task}-score`)
            if (scoreElements.length > 0 && numLanguages > 0){
                taskScoreMean = taskScoreMean / numLanguages
                taskSeMean = taskSeMean / numLanguages
                taskScoreMean = ('00' + taskScoreMean.toFixed(2)).slice(-5)
                taskSeMean = taskSeMean.toFixed(2)
                scoreElements[0].innerHTML = `${taskScoreMean} ± ${taskSeMean}`
            }
        }

        // Reset the number of languages
        numLanguages = 0

        // Loop over all the languages
        for (var lang_idx=0; lang_idx < languages.length; lang_idx++){
            var language = languages[lang_idx]
            var languageScoreMean = 0
            var languageSeMean = 0
            var numTasks = 0

            // Loop over all the tasks for the given row
            for (var task_idx=0; task_idx < tasks.length; task_idx++){
                var task = tasks[task_idx]
                var elements = row.getElementsByClassName(`${language} ${task}`)
                var taskScoreMean = 0
                var taskSeMean = 0
                var numDatasets = 0

                // Compute the task score from the row
                for (var elt_idx=0; elt_idx < elements.length; elt_idx++){
                    var value = parseFloat(elements[elt_idx]
                                           .innerHTML
                                           .replace(/ \/.*/g, '')
                                           .replace(/ ± [0-9.]+/g, ''))
                    var se = parseFloat(elements[elt_idx]
                                        .innerHTML
                                        .replace(/ \/.*/g, '')
                                        .replace(/[0-9.]+ ± /g, ''))
                    taskScoreMean += value
                    taskSeMean += se
                    numDatasets += 1
                }

                // Add the task score to the language score
                if (numDatasets > 0) {
                    languageScoreMean += taskScoreMean / numDatasets
                    languageSeMean += taskSeMean / numDatasets
                    numTasks += 1
                }
            }

            // Set the language score in the row
            scoreElements = row.getElementsByClassName(`${language}-score`)
            if (scoreElements.length > 0 && numTasks > 0){
                languageScoreMean = languageScoreMean / numTasks
                languageSeMean = languageSeMean / numTasks
                overallScore += languageScoreMean
                overallSe += languageSeMean
                languageScoreMean = ('00' + languageScoreMean.toFixed(2)).slice(-5)
                languageSeMean = languageSeMean.toFixed(2)
                scoreElements[0].innerHTML = `${languageScoreMean} ± ${languageSeMean}`
                numLanguages += 1
            }
        }

        // Set overall score in the row
        var scoreElements = row.getElementsByClassName('score')
        if (scoreElements.length > 0 && numLanguages > 0){
            overallScore = overallScore / numLanguages
            overallSe = overallSe / numLanguages
            overallScore = ('00' + overallScore.toFixed(2)).slice(-5)
            overallSe = overallSe.toFixed(2)
            scoreElements[0].innerHTML = `${overallScore} ± ${overallSe}`
        }
    }
}


// Sort the language model benchmark by the Score column
var click = new MouseEvent("click", {
    view: window,
    bubbles: true,
    cancelable: true,
    clientX: 20,
});
if(nlu_benchmark){
    document.getElementById('score-col').dispatchEvent(click);
}

// Fill in the rank column
var rows = nlu_benchmark.getElementsByTagName('tr')
for (var row_idx=0; row_idx < rows.length; row_idx++){
    var row = rows[row_idx]
    var rankElements = row.getElementsByClassName('rank')
    if (rankElements.length > 0){
        rankElements[0].innerHTML = row_idx + 1
    }
}
