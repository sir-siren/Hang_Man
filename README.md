# HangMan
Welcome to the hangman game! In this game, the computer will select a word and you will have to guess the letters in the word one by one. You will have a certain number of chances to guess the word correctly. If you are able to guess the word within the allowed number of chances, you win the game. If you are not able to guess the word, you lose the game.

To play the game, you will need to have Python installed on your computer. If you do not have Python installed, you can download it from the official Python website: [Python](https://www.python.org/).

## How to play:
1. Open a terminal or command prompt and navigate to the directory where you have saved the hangman game file.
2. Run the game using the command ```python hangman.py```
3. The computer will select a word and display a number of underscores on the screen, one for each letter in the word. For example, if the word is "python", the computer will display "_ _ _ _ _".
4. You will be asked to enter a letter. If the letter is present in the word, the underscores will be replaced with the correct letters. If the letter is not present in the word, you will lose one of your chances.
5. Continue guessing letters until you are able to correctly guess the word or until you run out of chances.
6. If you are able to correctly guess the word, you win the game. If you run out of chances, you lose the game.

## Example:
```py
Welcome to Hangman!

The word is: _ _ _ _ _

Enter a letter: p
The word is: p _ _ _ p

Enter a letter: y
The word is: p y _ _ p

Enter a letter: t
The word is: p y t h _ p

Enter a letter: h
The word is: python

Congratulations, you won!
```
