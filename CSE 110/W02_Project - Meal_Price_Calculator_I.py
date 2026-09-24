"""
Author: Elijah Asante
Purpose: Code a Meal Price Calculator
"""

child_price = float(input("What is the price of a child's meal? ")) # request for children food price

adult_price = float(input("What is the price of an adult's meal? ")) # request for adult food price

number_of_children = int(input("What is the number of children? ")) # request for total children

number_of_adult = int(input("What is the number of adults? ")) # request for total adults

child_total = child_price * number_of_children # compute subtotal for children's food

adult_total = adult_price * number_of_adult # compute subtotal for adult food

sub_total = child_total + adult_total # compute grand total of all purchases

print( ) # for extra white space

print(f"The subtotal for the food is: ${sub_total}") # print the total of the child and adult food price

