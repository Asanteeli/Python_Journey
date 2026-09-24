"""
Author: Elijah Asante
Purpose: Word Guessing Game
"""

print("**********************************")
print("Welcome to the word guessing game") # This is meant to print the introductory message to the game
print("**********************************")
print()

# These are the needed variables at this stage of the project
secret_word = "Example".upper() 
guess_word = "".upper()
count = 0
hint = " ".join(["_"] * len(secret_word))

while guess_word != secret_word: # This line gives a condition that for the time being that as it is true, the code loops
    count += 1
    guess_word = input("Guess the word: ").upper() # This line gives the player the chance to input the guess
    for character in range (len(guess_word)):
        if character == 0 or character % 2 == 0:
            #guess_word = character + " ".strip()
            print(f"{guess_word}", end="")
        else:
            guess_word = "_ ".strip()
    print(f"The hint is {hint}")
    if guess_word == secret_word:                   # This give a situation that compares the guess and secret word and acts upon the results
        print("Congratulations! You guessed right") # This line prints a congratulatory message if user guessed right
    else:
        print("Your guess is not correct")          # This line print a note informing user answer is not what is expected
print(f"You have guessed {count} times")            # This line counts the number of times a user tried.

