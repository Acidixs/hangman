import time
import string
import random

from words import words
from hangman_pics import HANGMANPICS

def playAgain():
    user_input = input("Do you wanna play again? Y/N: ")
    if user_input == "Y":
        startGame()
    else:
     print("Thanks for playing!")
     exit(1)

def get_random_word():
    word = random.choice(words)
    return word

def startGame():
    word = get_random_word()
    blanks = list("_" * len(word))
    alphabet = list(string.ascii_lowercase)

    guessed_letters = []
    wrong_letters = []
    attempts = 7

    while attempts > 0:

        print(word)
        print("HANGMAN")
        print(HANGMANPICS[len(wrong_letters)])
        print("".join(blanks))
        guess = str(input("Guess a letter: ")).lower()

        # Checks if user input is invalid
        if guess not in alphabet or len(guess) >= 2:
            print("(!) Enter a single letter")
            time.sleep(2)
            continue

        # Checks if letter has been guessed before
        if guess in guessed_letters:
            print("(!) You have already guessed that letter")
            time.sleep(2)
            continue


        for i in range(len(word)): # for every char in word
            if word[i] == guess: # if any char in word is equal to guess
                blanks[i] = guess  # replace char with guess
                guessed_letters.append(guess)


        if guess not in word:
            wrong_letters.append(guess)
            guessed_letters.append(guess)
            attempts -= 1


        # Checks if user has guessed the word
        if "".join(blanks) == word:
            print("You win!" + "\nYou guessed the word '{0}'".format(word))
            playAgain()

# starts the game
startGame()
playAgain()