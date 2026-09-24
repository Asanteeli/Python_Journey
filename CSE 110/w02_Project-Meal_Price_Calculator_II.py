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

print(f"The subtotal for the food is: ${sub_total:.2f}") # print the total of the child and adult food price

print( ) # for extra white space

sales_tax_rate = float(input("What is the sales tax rate? ")) # request for the sales tax rate

print( ) # for extra white space

sales_tax = (sub_total * sales_tax_rate) / 100 # compute the sales tax

print(f"Sales Tax: ${sales_tax:.2f}") # print the sales tax

meal_total = sub_total + sales_tax # compute the total cost for the meal

print(f"Total Spent: $ {meal_total:.2f}") # print the total spent

print( ) # for extra white space

payment_amount = float(input("What is the payment amount? ")) # request for the amount paid
amount_change = payment_amount - meal_total # compute the change left

print(f"Change: ${amount_change:.2f}") # print the change calculated.
