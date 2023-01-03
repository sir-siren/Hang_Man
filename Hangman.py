# import the necessary libraries
import random

# update the word list to use the 'word_list' from hangman_words.py
from hangman_words import words_and_hints as word_list

# choose a random word and hint from the list
word_and_hint = random.choice(word_list)
word = word_and_hint["word"]
hint = word_and_hint["hint"]
word_length = len(word)

# initialize variables
end_of_game = False
lives = 6
display = []
for _ in range(word_length):
    display += "_"

# import the logo from hangman_art.py and print it at the start of the game
from hangman_art import logo

print(logo)

# main game loop
while not end_of_game:
    print(f"Hint: {hint}\n")
    guess = input("Guess a letter: ").lower()

    # if the user has entered a letter they've already guessed, print the letter and let them know
    if guess in display:
        print(f"You've already guessed {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    # check if user is wrong
    if guess not in word:
        # if the letter is not in the word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose, The Answer is {word}.")

    # join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    # check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif guess == word:
        end_of_game = True
        print(f"You're correct! The word is {word}")

    # import the stages from hangman_art.py
    from hangman_art import stages
    print(stages[lives])
