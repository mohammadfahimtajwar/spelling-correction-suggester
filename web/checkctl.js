const app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {

    console.log("loaded");

    $scope.input_word = "";
    $scope.correct_prompt="Enter your correction here.";
    $scope.word_correct = false;
    $scope.haveAnswers = false;

    $scope.haveInput    =   function() {
        return $scope.input_word.length;
    }

    $scope.reset_submission = function() {
        $scope.word_correct = false;
        $scope.input_word = ""
    };

    $scope.check = function() {
        console.log("Word to check is  = ", $scope.input_word)

        $scope.correction_response = null;

        $scope.correct_word = ""
        $scope.correct_prompt = ""

        $http.get('/api/check?word=' + $scope.input_word).
        then(function(response) {
            $scope.greeting = response.data;
            if (response.data.status == "CORRECT") {
                $scope.word_correct=true;
                console.log("The word is correct.")
            }
            else {
                $scope.word_correct = false;
                $scope.haveAnswers=true;
                console.log("Possible words = " + JSON.stringify(response.data, null, 2));
                $scope.corrected_words = response.data.suggestions;
                if ($scope.corrected_words.length > 0) {
                    $scope.correct_prompt = "Click on a word to choose a correction or enter your own correction."
                }
                else {
                    $scope.correct_prompt = "No corrections were found. You can enter your own correction."
                }
            }
        });

    };

    $scope.chose_word   =   function(w) {
        console.log("You chose " + w);
        $scope.correct_word = w;
    }

    $scope.corrected = function(w) {
        console.log("You clicked " + w);
        $scope.correct_word = w;
        $scope.correct_prompt=null;
    };

    $scope.submit_correction = function(w) {
        console.log($scope.input_word + " CORRECTION TO " + $scope.correct_word + " IS ON THE WAY.");
        data = {
            corrected_word : $scope.correct_word,
            original_word: $scope.input_word
        }
        $http.post('/api/correct', data).
        then(function(response) {
            $scope.correction_response = response.data.msg;
            $scope.input_word = ""
            $scope.corrected_words = ""
            $scope.haveAnswers = false;
            $scope.$apply()
        });
    };

    $scope.show_correction_rsp  =   function() {
        if ($scope.correction_response !== null) {
            return true;
        }
        else {
            return false;
        }
    }
    console.log("Done.");
});