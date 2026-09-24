"""
Author: Elijah Asante
Purpose: A code to calculate the volume of a tire
"""

import math
from datetime import datetime 

name = input("Please enter your name: ").capitalize()
while name == "":
    print("Try again")
    name = input("Please enter your name: ").capitalize()
print("====================================================================================")
print(f"Welcome {name}. This is a small beginner project to calculate the volume of a tire")
print("====================================================================================")
print("Enter the following details to get the calculation done")
print()

while True:
    # Taking data from user and storing them into variables
    width = float(input("Width of your tire: "))
    aspect_ratio = float(input("Aspect ratio of your tire: "))
    diameter = float(input("Diameter of your tire: "))

    # Variables to create the tire volume calculation formular
    part_I = math.pi * (width ** 2) * aspect_ratio
    part_II = width * aspect_ratio + (2540 * diameter)

    # Formular
    volume = (part_I * part_II) / 10000000000

    # Printing the final output
    print(f"The approximate volume of the tire is {volume:.2f} liters")

    # Getting time from system
    date = datetime.now().strftime("%Y-%m-%d")

    # Writing data into a file
    with open("volume.txt", "a") as file:
        file.write("------------------------------\n")
        file.write(f"Name of User: {name}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Width of Tire: {width}\n")
        file.write(f"Aspect Ratio: {aspect_ratio}\n")
        file.write(f"Diameter of Tire: {diameter}\n")
        file.write(f"Volume of Tire: {volume:.2f}\n")

    # Request from user if they want to calculate for another tire
    again = input("Do you want to calculate for another tire? ").capitalize()
    if again == "Yes":
        continue

    print(f"Thank you {name} for using the tire volume calculator.")
    break





