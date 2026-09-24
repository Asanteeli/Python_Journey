"""Author: Elijah Asante
Purpose: Word Guessing Game
"""
print("**********************************")
print("Welcome to the word guessing game") # This code prints the introductory message to the game
print("**********************************")
print()

# These are the needed variables for the game
secret_word = "Example".upper() 
guess_word = "".upper() 
count = 0 # To count the number of attempts
 # Hint variable to display all underscores separated by spaces


while guess_word != secret_word: # This line gives a condition that for the time being that as it is true, the code loops
    hint = " ".join(["_"] * len(secret_word))
    guess_word = input("What is your guess? ").upper() # This line gives the player the chance to input the guess
    count += 1
    
    # Verify guess length matches secret word length
    if len(guess_word) != len(secret_word):
        print(f"Sorry, the guess must be the same length as the secret word ({len(secret_word)} letters).")
        print(f"The hint is {hint}")
        print()
        continue # Skip processing hints and prompt for a guess again
        
    # Convert the current hint string into a list of indexs to safely replace indices
    hint_list = hint.split()
    
    # This is your index loop tracking index positions
    for index in range(len(guess_word)):
        current_letter = guess_word[index]
        
        # This if block checks the exact match at that spot
        if current_letter == secret_word[index]:
            hint_list[index] = current_letter.upper()
            
        # This elif block only overwrites if the slot isn't already locked with an uppercase match
        elif current_letter in secret_word and not hint_list[index].isupper():
            hint_list[index] = current_letter.lower()
            
    # This code block reassembles the list back
    hint = " ".join(hint_list)
    print(f"The hint is {hint}")
    
    if guess_word == secret_word:                   # This line of code compares the guess and secret word and acts upon the results
        print("Congratulations! You guessed right") # This line of code prints a congratulatory message if user guessed right
    else:
        print("Your guess is not correct")          # This line prints a note informing user answer is not what is expected
    print()                                         # To provide white space

print(f"You have guessed {count} times")            # This line counts the number of times a user tried.
