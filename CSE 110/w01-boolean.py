
num_men = int(input("How many men have been selected to play? "))
num_women = int(input("How many women have been selected to play? "))
total = num_women + num_men

enough_women = num_women >= 4
total_needed = total >= 7

if enough_women and total_needed:
    print("We can play the game")
else:
    print("We cannot play the game.")

if not total_needed:
    print("Can we play a practice game instead?")

