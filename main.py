import time
import string

from hangman_pics import HANGMANPICS

word = "Python".lower()
blanks = list("_" * len(word))
alphabet = list(string.ascii_lowercase)

guessed_letters = []
wrong_letters = []
attempts = 7

while attempts > 0:

        if "".join(guessed_letters) == word:
            print("You win!")
            exit(1)

        print("HANGMAN")
        print(HANGMANPICS[len(wrong_letters)])

        print("".join(blanks))
        guess = str(input("Guess a letter: ")).lower()


        if guess not in alphabet or len(guess) >= 2:
            print("Enter a single letter")
            time.sleep(2)
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter")
            time.sleep(2)
            continue

        guessed_letters.append(guess)


        if guess in word:
            wordIndex = word.find(guess)
            blanks[wordIndex] = guess
            print("".join(blanks))

        else:
            wrong_letters.append(word)
            attempts -= 1

print(f"You are out of attempts! The word was {word}")
#playAgain = input("Do you want to play again? Y/N")
