# HangMan
Welcome to the hangman game! In this game, the computer will select a word and you will have to guess the letters in the word one by one. You will have a certain number of chances to guess the word correctly. If you are able to guess the word within the allowed number of chances, you win the game. If you are not able to guess the word, you lose the game.

> To play the game, you will need to have Python installed on your computer. If you do not have Python installed, you can download it from the official Python website: [Python](https://www.python.org/).

## How to play:
1. Open a terminal or command prompt and navigate to the directory where you have saved the hangman game file.
2. Run the game using the command ```python hangman.py```
3. The computer will select a word and display a number of underscores on the screen, one for each letter in the word. For example, if the word is "python", the computer will display "_ _ _ _ _".
4. You will be asked to enter a letter. If the letter is present in the word, the underscores will be replaced with the correct letters. If the letter is not present in the word, you will lose one of your chances.
5. Continue guessing letters until you are able to correctly guess the word or until you run out of chances.
6. If you are able to correctly guess the word, you win the game. If you run out of chances, you lose the game.

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

### Lose

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
