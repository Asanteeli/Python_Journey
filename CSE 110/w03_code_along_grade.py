"""
Author: Elijah Asante
Purpose: Student Score Grading Progam
"""

grade = int(input("What is your grade? ")) # code to request student score from user

# This is the code I earlier wrote and after visiting the sample solution I decided to correct it.
# I have searched and learnt that writing the code the second way stores the response for later use
# and does not print the response righ away and forget about what happened like the first set of code.

# Code for grading the various scores
"""
if grade >= 90:
    print(f"You have passed the course with grade {grade}.") 
elif grade >= 80:
    print(f"You have passed the course with grade {grade}.")
elif grade >= 70:
    print(f"You have passed the course with grade {grade}.")
elif grade >= 60:
    print(f"You have passed the course with grade {grade}")
else:
    print(f"You have failed the course with grade {grade}")
"""

# The second set of code to store scores into grading alphabets
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Code for adding + or - to the student grades
extra_sign = ""

last_digit = grade % 10

if last_digit >= 7:
    extra_sign = "+"
elif last_digit < 3:
    extra_sign = "-"
else:
    extra_sign = ""

# Code for A+ grades
if grade >= 93:
    extra_sign = ""

# Code for F+ and F- grades
if letter == "F":
    extra_sign = ""

print(f"Your letter grade is: {letter}{extra_sign}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")