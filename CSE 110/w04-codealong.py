import random

secret_number = random.randint(1, 1000)
guess_count = 0

guess_number = int(input("Guess a number: "))
guess_count += 1
while guess_number != secret_number:
    if (guess_number > secret_number):
        print("That was too high, guess lower")
    else:
        print("That was too low, guess higher")
    guess_number = int(input("Guess a number: "))
    guess_count += 1
print("You got it")
print(f"and it only took you {guess_count} to get it right")
    


