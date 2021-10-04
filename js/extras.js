// Enable tooltips everywhere
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Get the rows in the pretrained leaderboard and the list of tasks, so that we
// can fill in all the aggregated score columns
pretrained = document.getElementById('pretrained-leaderboard')
if(pretrained){
    var rows = pretrained.getElementsByTagName('tr')
    var languages = ['da', 'no', 'sv', 'is', 'fo']
    var tasks = ['ner', 'pos', 'dep', 'clf']

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
                    if (value > 0) {
                        languageScoreMean += value
                        languageSeMean += se
                        numDatasets += 1
                    }
                }

                // Add the task score to the language score
                if (languageScoreMean > 0 && numDatasets > 0) {
                    taskScoreMean += languageScoreMean / numDatasets
                    taskSeMean += languageSeMean / numDatasets
                    numLanguages += 1
                }
            }

            // Set the task score in the row
            scoreElements = row.getElementsByClassName(`${task}-score`)
            if (scoreElements.length > 0 && numLanguages > 0 && taskScoreMean > 0){
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
                    if (value > 0) {
                        taskScoreMean += value
                        taskSeMean += se
                        numDatasets += 1
                    }
                }

                // Add the task score to the language score
                if (taskScoreMean > 0 && numDatasets > 0) {
                    languageScoreMean += taskScoreMean / numDatasets
                    languageSeMean += taskSeMean / numDatasets
                    numTasks += 1
                }
            }

            // Set the language score in the row
            scoreElements = row.getElementsByClassName(`${language}-score`)
            if (scoreElements.length > 0 && languageScoreMean > 0 && numTasks > 0){
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


// Get the rows in the finetuned leaderboard and the list of tasks, so that we
// can fill in all the aggregated score columns
finetuned = document.getElementById('finetuned-leaderboard')
if(finetuned){
    var rows = finetuned.getElementsByTagName('tr')
    var languages = ['da', 'no', 'sv', 'is', 'fo']
    var tasks = ['ner', 'pos', 'dep', 'sent']

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

                    if (value > 0) {
                        languageScoreMean += value
                        languageSeMean += se
                        numDatasets += 1
                    }
                }

                // Add the task score to the language score
                if (languageScoreMean > 0 && numDatasets > 0) {
                    taskScoreMean += languageScoreMean / numDatasets
                    taskSeMean += languageSeMean / numDatasets
                    numLanguages += 1
                }
            }

            // Set the task score in the row
            scoreElements = row.getElementsByClassName(`${task}-score`)
            if (scoreElements.length > 0 && numLanguages > 0 && taskScoreMean > 0){
                taskScoreMean = taskScoreMean / numLanguages
                taskSeMean = taskSeMean / numLanguages
                taskScoreMean = ('00' + taskScoreMean.toFixed(2)).slice(-5)
                taskSeMean = taskSeMean.toFixed(2)
                scoreElements[0].innerHTML = `${taskScoreMean} ± ${taskSeMean}`
            }
        }
    }
}


// Sort the pretrained leaderboard by the Score column and the finetuned
// benchmark by the NER column
var click = new MouseEvent("click", {
    view: window,
    bubbles: true,
    cancelable: true,
    clientX: 20,
});
if(finetuned){
    document.getElementById('finetuned-ner-col').dispatchEvent(click);
}
if(pretrained){
    document.getElementById('score-col').dispatchEvent(click);
}
