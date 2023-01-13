# HangMan
Welcome to Hangman Games! In this game the computer chooses a word and he has to guess the letters of the word one by one. You have a certain number of chances to guess the word correctly. If you can guess the word within the number of chances given, you win the game. If you can't guess the word, you lose the game.

> Your computer must have Python installed to play the game. If you don't have Python installed, visit the official Python website Python: [Python](https://www.python.org/).

## How to play:
1. Open a terminal or command prompt and navigate to the directory where you saved the Hangman game files.
2. Start the game with the command ```python hangman.py```.
3. The computer selects a word and displays a series of underscores on the screen for each letter of the word. For example, if the word is "Python", the computer will display "_ _ _ _ _".
4. You will be prompted to enter a character. The underscore is replaced with the correct character if the character exists within a word. If the letter is not in the word, you lose one of your chances.
5. Keep guessing letters until you guess the word correctly or you run out of chances.
6. Whoever guesses the word correctly wins the game. If you run out of chances, you lose the game
![HANG-MAN](https://cdn.discordapp.com/attachments/966283152643465226/1059945602236027011/HANG-MAN.png)

## Example:
### Win:
```py
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: h
h _ _ _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: a
h a _ _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: z
h a z _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: e
h a z e _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: l
h a z e l _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: n
h a z e l n _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: u
h a z e l n u _

  +---+
  |   |
      |
      |
      |
      |
=========

Hint: This small, brown nut with a hard outer shell is often used in cooking and baking. It is also the main ingredient in chocolate-hazelnut spread.

Guess a letter: t
h a z e l n u t
You win.

  +---+
  |   |
      |
      |
      |
      |
=========
```

### Lose:

```py
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: l
You guessed l, that's not in the word. You lose a life.
_ _ _ _ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: o
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
      |
      |
      |
=========

Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: e
You guessed e, that's not in the word. You lose a life.
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: w
You guessed w, that's not in the word. You lose a life.
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: q
You guessed q, that's not in the word. You lose a life.
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter:         
You guessed     , that's not in the word. You lose a life.
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Hint: This marsupial is native to Australia and is known for its powerful legs and its ability to hop long distances.

Guess a letter: d
You guessed d, that's not in the word. You lose a life.
You lose, The Answer is kangaroo.
_ _ _ _ _ _ o o

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```
