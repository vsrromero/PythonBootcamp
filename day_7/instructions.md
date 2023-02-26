# Hangman game

## Getting a random word
Instead of using a predefined list of words, this exercise now retrieves a random word from the [Random Word API](https://random-word-api.herokuapp.com/home) using the requests package for Python. The reason for this change is to improve the user experience by allowing them to choose the difficulty level of the game based on the number of letters in the word.

By using this API, the app can generate a more varied selection of words, making the game more challenging and engaging for users. Additionally, the ability to customize the game's difficulty level based on the user's preferences provides a more personalized experience.

## Included beyond what was requested
* Getting words from an API
* 3 different levels
    * Easy: 3 to 5 letters
    * Normal: 6 to 8 letters
    * Hard: 9 to 15 letters
* Show already chosen words 


## Logic flowchart  

<img src='./imgs/flowchart.jpeg' height='45%' width='45%'>

### Steps followed to complete the project

#### Challenge 1 - Picking a random word and checking answers

* ~~Randomly choose a word from the word_list and assign it to a variable called `chosen_word`.~~  
Get a word from Random Word API and assign it to a variable called `chosen_word`.
* Ask the user to guess a letter and assign their answer a variable called `guess`. Make guess lowercase.
* Check if the letter the user guessed (`guess`) is one of the letters in the `chosen_word`.

#### Challenge 2 - Replacing blanks with guesses
* Create an empty list called `display`.
    * For each letter in the `chosen_word`, add a "_" to `display`.  
    So if the `chosen_word` was "apple", display be `["_", "_", "_", "_", "_"]` with 5 "\_" representing each letter to guess.
* Loop through each position in the `chosen_word`;
    * If the letter at that position matches "guess", then reveal that letter in the `display` at that position.
    e.g. If the user guessed "p" and the chosen word was "apple", then display should be `["_", "p", "p", "_", "_"]`.
* Print `display`and you should see the guessed letter in the correct position and every other letter replace with "\_".

#### Challenge 3 - Checking if the player has won
* Use a `while` loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the `chosen_word` and `display` has no more blanks ("\_"). Then the app can thell the user they've won.

#### Challenge 4 - Keeping track of the player's lives
* Create a variable called `lives` to keep track of the number of lives left.  
Set `lives` equals to 6.
* If `guess` is not a letter in the `chosen_word`, then reduce `lives` by 1. If lives goes down to 0 then the game should stop and it should print `You lose.`
* Print the ASCII art from `stages` (got from the project resource) that corresponds to the current number of `lives` the user has remaining.


[Project folder](../day_7/)