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

print("==========================================")


# Request player to choose the path of their choice
# Learnt of the function .strip() that it clears white space so I added it to my code to minimize errors from users of my game.
game_path = str(input("You discover a CAVE, a RIVER, and an OLD TOWER. Choose an option: ")).strip()
game_path = game_path.upper()
error_message = "Restart the game and enter the correct information as needed."



if game_path == "CAVE" or game_path == "RIVER" or game_path == "OLD TOWER": # This code compares Treasure Hunters input choice and makes a decision
    print(f"You have entered the {game_path} PATH ...") # This code prints a statement of confirmation according to the choice made by the Treasure Hunter
    if game_path == "CAVE":                             # This code is marks the beginning of how the rest of the game will be if the Treasure Hunter selected CAVE and compares the players choice to the word "CAVE" and takes a decision
        decision_cave = input("Do you want to LIGHT A TORCH or WALK IN THE DARK? ").upper().strip() # This code asks Treasure Hunter for further input after choosing CAVE and stores the answer in a variable for furture use
        print(f"Treasure Hunter chose to {decision_cave}")         # This code prints a confirmation statement of the choice made by Treasure Hunter to "LIGHT A TORCH or WALK IN THE DARK" 
        if decision_cave == "LIGHT A TORCH":            # This code compares the Treasure Hunters choice to the option of "LIGHT A TORCH" and takes a decision
            decision_cave2 = input("Do you want to OPEN CHEST or WALK AWAY? ").upper().strip() # This code asks for an input from the Treasure Hunter and stores the input into a variable (decision_cave2) for future use
            print(f"Treasure Hunter chose to {decision_cave2}") # This code prints a confirmation statement of the Treasure Hunter's choice to "OPEN CHEST or WALK AWAY"
            if decision_cave2 == "OPEN CHEST":          # This code compares the Treasure Hunters choice against the option of "WALK AWAY" and OPEN CHEST
                print("Treasure Found")
            elif decision_cave2 == "WALK AWAY":
                print("Safe Exit")                 # ... and prints the congratulatory message to show the Treasure Hunter has completed the game.
            else:
                print(f"{error_message}")                      # This code prints the alternative action after the choice between "OPEN CHEST" and "WALK AWAY" has been made.
        elif decision_cave == "WALK IN THE DARK":       # This code runs the next line of action if Treasure Hunter chooses "WALK IN THE DARK" option. It compares Treasure Hunter's choice to the hard coded "WALK IN THE DARK" and makes a decision.
            decision_cave3 = str(input("You hear growling. RUN or STAND STILL: ")).upper().strip() # This code collects response from Treasure Hunter and stores it into the variable (decision_cave3) for furture use.
            print(f"Treasure Hunter chose to {decision_cave3}")    # This code print confirmation of the choice Treasure Hunter made between "RUN and STAND STILL".
            if decision_cave3 == "RUN":                 # This code compares the Treasure Hunters choice against the option of "RUN" and "STAND STILL"             
               print("Treasure Hunter Escaped")                    # This code prints a confimatory statement of the action taken after the Treasure Hunter's choice between "RUN" and "STAND STILL" 
            elif decision_cave3 == "STAND STILL":
                print("Bear finds and eats you")         # This code prints the alternative action after the choice between "RUN" and "STAND STILL" has been made.
            else:
                print(f"{error_message}")
        else:
            print(f"{error_message}")


# This Second set of code has the same logic as the above that deals with the "CAVE" option
# All comments above on the first set of codes for "CAVE" option applies to this set "RIVER" option

    elif game_path == "RIVER":
        decision_river = input("Do you want to SWIM or BUILD A RAFT? ").upper().strip()
        print(f"Treasure Hunter chose to {decision_river}.")
        if decision_river == "SWIM":
            decision_river2 = input("Do you want to FIGHT CURRENT or TURN BACK? ").upper().strip()
            print(f"Treasure Hunter chose to {decision_river2}")
            if decision_river2 == "FIGHT CURRENT":
                print("Treasure Hunter has found the island")
            elif decision_river2 == "TURN BACK":
                print("Safe Return")
            else:
                print(f"{error_message}")
        
        elif decision_river == "BUILD A RAFT":
            decision_river3 = input("With the raft, SAIL ACROSS or FOLLOW SHORE? ").upper().strip()
            print(f"Treasure Hunter chose to {decision_river3}")
            if decision_river3 == "SAIL ACROSS":
                print("Treasure Hunter found the treasure")
            elif decision_river3 == "FOLLOW SHORE":
                print("Back to the village empty handed")
            else:
                print(f"{error_message}")
        else:
            print(f"{error_message}")

# This Third set of code has the same logic as the first two set of codes above that deals with the "CAVE" & "RIVER" options
# All comments above on the first two sets of codes for "CAVE & RIVER" options applies to this set "OLD TOWER" option

    elif game_path == "OLD TOWER":
        decision_tower = input("Do you want to CLIMB STAIRS or OPEN BASEMENT? ").upper().strip()
        print(f"Treasure Hunter chose to {decision_tower}")
        if decision_tower == "CLIMB STAIRS":
            decision_tower2 = input("Do you want to LOOK THROUGH WINDOW or OPEN DOOR? ").upper().strip()
            print(f"Treasure Hunter {decision_tower2}")
            if decision_tower2 == "LOOK THROUGH WINDOW":
                print("Treasure Hunter finds treasure map")
            elif decision_tower2 == "OPEN DOOR":
                print("Treasure Hunter meets a Wizard")
            else:
                print(f"{error_message}")
        elif decision_tower == "OPEN BASEMENT":
            decision_tower3 = input("Basement opened. Now will you SEARCH BOXES or LEAVE: ").upper().strip()
            print(f"Treasure Hunter chose to {decision_tower3}")
            if decision_tower3 == "SEARCH BOXES":
             print("Magic key Found")
            elif decision_tower3 == "LEAVE":
                print("Treasure Hunter abandoned quest")
            else:
                print(f"{error_message}")
        else:
            print(f"{error_message}")
else:
    print(f"{error_message}")

# These set of code sends a message to user when the wrong input is made while playing the game
# I have a feeling the elifs are too much in this code is there a way to minimize it? Or I will still have to go through it
# I tried using the code below to check users that may enter wrong inputs 
# but after that it keeps printing the message at the last stage of the game 
# no matter the selection I make so I have commented it out. Please help me fix it. Thank you.

"""else game_path != "CAVE" or game_path != "RIVER" or game_path != "OLD TOWER":
    print(f"{wrong_input_message}")
        elif decision_cave != "LIGHT A TORCH" or decision_cave !=  "WALK IN THE DARK":
    print(f"{wrong_input_message}")
elif decision_cave2 != "OPEN CHEST" or decision_cave2 != "WALK AWAY":
    print(f"{wrong_input_message}")
elif decision_cave3 != "RUN" or decision_cave3 != "STAND STILL":
    print(f"{wrong_input_message}")
elif decision_river != "SWIM" or decision_river != "BUILD A RAFT":
    print(f"{wrong_input_message}")
elif decision_river2 != "FIGHT CURRENT" or decision_river2 != "TURN BACK":
    print(f"{wrong_input_message}")
elif decision_river3 != "SAIL ACCROSS" or decision_river3 != "FOLLOW SHORE":
     print(f"{wrong_input_message}")
elif decision_tower != "CLIMB STAIRS" or decision_tower != "OPEN BASEMENT":
    print(f"{wrong_input_message}")
elif decision_tower2 != "LOOK THROUGH WINDOW" or decision_tower2 != "OPEN DOOR":
    print(f"{wrong_input_message}")
elif decision_tower3 != "SEARCH BOXES" or decision_tower3 != "LEAVE":
    print(f"{wrong_input_message}")
else:
    print()
"""
  


# Program ended


    
    