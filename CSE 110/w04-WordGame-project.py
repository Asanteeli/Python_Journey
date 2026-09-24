# print("**********************************")
# print("Welcome to the word guessing game") # This is meant to print the introductory message to the game
# print("**********************************")
# print()

# # These are the needed variables at this stage of the project
# secret_word = "Example".upper() 
# guess_word = "".upper()
# count = 0

# # Use a loop to generate the initial hint (all underscores with spaces)
# initial_hint = ""
# for i in range(len(secret_word)):
#     initial_hint += "_ "
# print(f"Your hint is: {initial_hint.strip()}")
# print()

# while guess_word != secret_word: # This line gives a condition that for the time being that as it is true, the code loops
#     guess_word = input("Guess the word: ").upper() # This line gives the player the chance to input the guess
#     count += 1
    
#     if guess_word == secret_word:                   # This give a situation that compares the guess and secret word and acts upon the results
#         print("Congratulations! You guessed right") # This line prints a congratulatory message if user guessed right
#     else:
#         print("Your guess is not correct")          # This line print a note informing user answer is not what is expected
        
#         # Add a check to verify that the length of the guess is the same as the length of the secret word
#         if len(guess_word) != len(secret_word):
#             print(f"Sorry, the guess must be the same length as the secret word ({len(secret_word)} letters).")
#         else:
#             # If they are the same, then proceed to generate and give the hint using a loop
#             hint = ""
#             for i in range(len(secret_word)):
#                 current_letter = guess_word[i]
                
#                 # Letters that are present in the secret word at that exact spot (uppercase)
#                 if current_letter == secret_word[i]:
#                     hint += current_letter.upper() + " "
#                 # Letters that are present in the secret word, but in a different spot (lowercase)
#                 elif current_letter in secret_word:
#                     hint += current_letter.lower() + " "
#                 # Letters that are not present at all in the secret word (underscore _)
#                 else:
#                     hint += "_ "
            
#             print(f"Your hint is: {hint.strip()}")
#         print() # Adds a clean empty line between rounds

# print(f"You have guessed {count} times")            # This line counts the number of times a user tried.


print("**********************************")
print("Welcome to the word guessing game") # This is meant to print the introductory message to the game
print("**********************************")
print()

# These are the needed variables at this stage of the project
secret_word = "Example".upper() 
guess_word = "".upper()
count = 0

# Use a loop to generate the initial hint (all underscores with spaces)
initial_hint = ""
for i in range(len(secret_word)):
    initial_hint += "_ "
print(f"Your hint is: {initial_hint.strip()}")
print()

# Keep track of the persistent hint state across rounds
# We convert it to a list without spaces to easily update letters by index position
discovered_hints = ["_"] * len(secret_word)

while guess_word != secret_word: # This line gives a condition that for the time being that as it is true, the code loops
    guess_word = input("Guess the word: ").upper() # This line gives the player the chance to input the guess
    count += 1
    
    if guess_word == secret_word:                   # This give a situation that compares the guess and secret word and acts upon the results
        print("Congratulations! You guessed right") # This line prints a congratulatory message if user guessed right
    else:
        print("Your guess is not correct")          # This line print a note informing user answer is not what is expected
        
        # Add a check to verify that the length of the guess is the same as the length of the secret word
        if len(guess_word) != len(secret_word):
            print(f"Sorry, the guess must be the same length as the secret word ({len(secret_word)} letters).")
        else:
            # If they are the same, analyze the guess to permanently upgrade our saved hints
            for i in range(len(secret_word)):
                current_letter = guess_word[i]
                
                # Rule 1: Letters that are present in the secret word at that exact spot (uppercase)
                if current_letter == secret_word[i]:
                    discovered_hints[i] = current_letter.upper()
                
                # Rule 2: Letters present but in a different spot (lowercase)
                # Only save this if an exact uppercase match hasn't already claimed this slot
                elif current_letter in secret_word and not discovered_hints[i].isupper():
                    discovered_hints[i] = current_letter.lower()
            
            # Construct the final display string using a loop to add spaces after every character
            display_hint = ""
            for char in discovered_hints:
                display_hint += char + " "
                
            print(f"Your hint is: {display_hint.strip()}")
        print() # Adds a clean empty line between rounds

print(f"You have guessed {count} times")            # This line counts the number of times a user tried.
