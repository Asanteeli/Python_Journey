# Source - https://stackoverflow.com/q/76449504
# Posted by grexrr
# Retrieved 2026-07-21, License - CC BY-SA 4.0

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

if chosen_word == guess in chosen_word:
    print("Right")
else:
    print("Wrong")