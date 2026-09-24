"""""
Author: Elijah Asante
Purpose: Word guessing game 
"""
# I have intentionally left all my try and error codes so the instructors views how I was initially struggling with how to go about the project
"""print("Welcome to the word guessing game!")
secret_word = "Mosiah"
length_secret_word = len(secret_word)

guess_word = "_ _ _ _ _ _"
length_guess_word = len(guess_word)
count = 0
"""
# for guess_word in secret_word:
#     count += 1
#     if len(guess_word) != (secret_word):
#         print("Sorry, the guess must have the same number of letters as the secret word")
#         guess_word = str(input("Guess the letter: "))
#     else:
#         print("Congratulations, you guessed right")
# print(f"It took you {count}")

# while guess_word != secret_word:
#     print(f"Your hint is: {guess_word}")
#     count += 1
#     for guess_word in secret_word:
#         print(len(secret_word))
# import random
# word_list = ["food", "hand", "best"]
secret_word = "explain"
guess = ""
display_word = " ".join(["_"] * len(secret_word))
guess_counter = 0
hint = "Your hint is: "
instruction = "Sorry, the guess must have the same number of letters as the secret word"

print("Welcome to the word guessing game!")

while guess != secret_word:
    guess = input("What is your guess word? ").upper()
    guess_counter += 1
    # for letter in secret_word:
        # if letter in guess:
        #     print(f"{display_word} + {letter} + ' ' ")
        # else:
        #     print(f"{display_word}  + '_' ")
    










        




        








