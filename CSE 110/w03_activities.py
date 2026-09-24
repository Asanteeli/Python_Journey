"""
Author: Elijah Asante
Purpose: Compare numbers and favorite animal.
"""
first_number = int(input("Input the first number of your choice: "))
second_number = int(input("Input the second number of your choice: "))

if first_number > second_number:
    print(f"The first number is greater than second number")
else:
    print(f"The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")


if second_number > first_number:
    print("The second number is greater")
else:
    print("The second_number is not greater")

print("")

fav_animal = input("What is your favourite animal? ")
fav_animal = fav_animal.lower()
if fav_animal == "cat":
    print("That's my favourite animal too!")
else:
    print("That one is not my favorite animal.")