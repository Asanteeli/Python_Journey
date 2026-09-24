"""
Author: Elijah Asante
Purpose: A code to calculate the volume of a tire
"""

import math
from datetime import datetime 

# Taking data from user and storing them into variables
width = float(input("Enter the width of your tire: "))
aspect_ratio = float(input("Enter the aspect ratio of your tire: "))
diameter = float(input("Enter the diameter of your tire: "))

# Variables to create the tire volume calculation formular
part_I = math.pi * (width ** 2) * aspect_ratio
part_II = width * aspect_ratio + (2540 * diameter)

# Formular
volume = (part_I * part_II)/10000000000

# Printing the final output
print(f"The approximate volume of the tire is {volume:.2f} liters")


