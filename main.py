secretWord = "Python"

attempt_count = 0
attempt_limit = 10

incorrectChar = []
correctChar = []

print("H A N G M A N")
blanks = "_" * len(secretWord)
print(blanks)

while attempt_count != attempt_limit:

    charInput = input("Guess a character from the word: ")

    if charInput.lower() not in "abcdefghijklmnopqrstuvwxyz":
        print("Enter a character from the alphabet, a-z")
        continue

    if charInput.lower() in secretWord.lower():
        print("The word contains " + charInput)
        attempt_count += 1
        incorrectChar.append(charInput)

    else:
        print(charInput + " is not in the word")
        attempt_count += 1
        incorrectChar.append(charInput)


print("You failed, out of attempts!")
