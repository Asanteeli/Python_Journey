"""
Author : Elijah Asante
Purpose: Code is to compute the areas of three different shapes: a square, a rectangle and a circle 
"""

# Calculate the area of a square
length = float(input("What is the length of a side of the square? ")) # request user to input the length of a side

area_of_a_square = length ** 2 # square the result

print(f"The area of the square is {area_of_a_square}cm") # print the final answer

# Calculate the area of a rectangle
rectangle_length = float(input("What is the length of the rectangle? ")) # request user to input the length of the rectangle

rectangle_breadth = float(input("What is the breadth of the rectangle? ")) # request user to input the breadth of the rectangle

area_of_rectangle = rectangle_length * rectangle_breadth # formular to calculate the area of the rectangle

print(f"The area of the rectangle is {area_of_rectangle}cm") # print out final answer

# The area of a circle
radius_of_circle = float(input("What is the radius of the circle? ")) ** 2 # user input for the radius of the circle and the response is squared

pi = 3.14 # the value of pi

print(f"The area of the circle is {radius_of_circle * pi }.") # print out final answer



