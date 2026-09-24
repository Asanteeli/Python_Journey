"""
Author: Elijah Asante
Purpose: Adventure Game
"""

print("Welcome to this adventure game. Lets begin")

print("==========================================")

# Instructions for the game
print("This is a text-based adventure game, as a Treasure Hunter you are " \
"presented a scenario with different options. " \
"Make a choice, your choice will determine the path you take.")

print("==========================================")

print("Good Luck")


# Request player to choose the path of their choice
game_path = str(input("You discover a CAVE, a RIVER, and an OLD TOWER. Choose an option: "))
game_path = game_path.upper()



if game_path == "CAVE" or game_path == "RIVER" or game_path == "OLD TOWER": # This code compares Treasure Hunters input choice and makes a decision
    print(f"You have entered the {game_path} PATH ...") # This code prints a statement of confirmation according to the choice made by the Treasure Hunter
    if game_path == "CAVE":                             # This code is marks the beginning of how the rest of the game will be if the Treasure Hunter selected CAVE and compares the players choice to the word "CAVE" and takes a decision
        decision_cave = input("Do you want to LIGHT A TORCH or WALK IN THE DARK? ").upper() # This code asks Treasure Hunter for further input after choosing CAVE and stores the answer in a variable for furture use
        print(f"Treasure Hunter chose to {decision_cave}")         # This code prints a confirmation statement of the choice made by Treasure Hunter to "LIGHT A TORCH or WALK IN THE DARK" 
        if decision_cave == "LIGHT A TORCH":            # This code compares the Treasure Hunters choice to the option of "LIGHT A TORCH" and takes a decision
            decision_cave2 = input("Do you want to OPEN CHEST or WALK AWAY? ").upper() # This code asks for an input from the Treasure Hunter and stores the input into a variable (decision_cave2) for future use
            print(f"Treasure Hunter chose to {decision_cave2}") # This code prints a confirmation statement of the Treasure Hunter's choice to "OPEN CHEST or WALK AWAY"
            if decision_cave2 == "OPEN CHEST":          # This code compares the Treasure Hunters choice against the option of "WALK AWAY" and OPEN CHEST
                print("Treasure Found")                 # ... and prints the congratulatory message to show the Treasure Hunter has completed the game.
            else:
                print("Safe Exit")                      # This code prints the alternative action after the choice between "OPEN CHEST" and "WALK AWAY" has been made.
