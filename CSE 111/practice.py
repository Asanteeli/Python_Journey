# # Example 2
# # The input function always returns a string.
# k = input("Please enter a number: ")        # string
# m = input("Please enter another number: ")  # string
# n = k + m          # string plus string makes string
# print(f"k: {type(k)} {k}")
# print(f"m: {type(m)} {m}")
# print(f"n: {type(n)} {n}")
# print()
# # The int and float functions convert a string to a number.
# p = int(input("Please enter a number: "))          # int
# q = float(input("Please enter another number: "))  # float
# r = p + q                     # int plus float makes float
# print(f"p: {type(p)} {p}")
# print(f"q: {type(q)} {q}")
# print(f"r: {type(r)} {r}")

# a = 5 % 3
# print(a)

# Example 4
# Compute the total price of a pizza.
# The base price of a large pizza is $10.95
price = 10.95
# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))
# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping
# Add the cost of the toppings to the price of the pizza.
price = price + toppings_cost
# Print the price for the user to see.
print(f"Price: ${price:.2f}")