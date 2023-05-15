# Hangman Game

This is a simple implementation of the Hangman game using Python. The game involves two parties: a guesser and an executioner. The executioner chooses a word, and the guesser tries to guess the word by suggesting letters. The game continues until the guesser either guesses the word correctly or runs out of lives.

## How to Play

1. Run the Python script to start the game.
2. You will be prompted to input a letter. Please input only one letter at a time.
3. If the letter you guessed is correct and present in the chosen word, it will be revealed in the word's correct positions.
4. If the letter you guessed is incorrect, you will lose one life.
5. Keep guessing letters until you either guess the word correctly or run out of lives.
6. The game will end with a win if you guess the word correctly or a loss if you run out of lives.

## Rules

1. You have a limited number of lives at the start of the game.
2. Each incorrect guess will decrease the number of lives.
3. You cannot guess the same letter again.
4. The game will provide feedback on correct and incorrect guesses.
5. The game will display the progress of the word, showing the correctly guessed letters and underscores for the remaining letters.
6. You win the game by correctly guessing the word before running out of lives.

## Code Structure

The Hangman game is implemented using a Python class called `Hangman`. The class has the following methods:

- `__init__(self, number_of_lives)`: Initializes the game with the specified number of lives.
- `input_letter(self)`: Asks the user to input a letter and validates the input.
- `choose_random_word(self)`: Chooses a random word from a text file.
- `convert_random_word(self)`: Converts the chosen random word into a list of underscores to represent the hidden letters.
- `check_letter(self)`: Checks if the guessed letter is correct or incorrect and updates the game accordingly.
- `play_again(self)`: Allows the user to play the game again.
- `play_game(self)`: Executes the game by calling the necessary methods.

## Requirements

* Python 3.x
* words.txt File

## Getting Started

Once you have Python 3.x installed and the `words.txt` file ready, you can run the Python script to start playing the Hangman game.

Make sure to read the README.md file for instructions on how to play the game and understand the code structure.

Enjoy playing Hangman!