"""
Program Author: Elijah Asante
Purpose: A Word Guessing Game where the player tries to produce random category of words 
and still construct a meaningful sentence.
"""
# First requirement for the game 
adjective = input("Give an Adjective: ")

# Second requirement for the game
animal = input("Mention the name of an animal: ")

# Third requirement for the game
verb = input("Mention any verb: ")

# Last requirement for the game
exclamation = input("Provide any exlamatory remark: ")

# Final instruction to display the results of the game on screen
# Included in the print code are the signs \n for next line and \" \" to get the double quotes printed on screen
print(f"The other day, I was really in trouble. It all started when I saw a very \n big {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}\"! I yelled. But all \n I could think to do was to {verb.lower()} over and over. Miraculously, \n that caused it to stop, but not before it tried to {verb.lower()} \n right in front of my family.")