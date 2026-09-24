import math
number_second = 0.1234567
number = math.pi
final_answer = math.ceil(number_second)
print(f"Then final answer is {number}")
print(f"The final answer is {number:.2f}")
print(f"The answer now is {final_answer}")


name = 25
print(f"The name is {name:05}!") # This format is for width -> The number occupies at least 5 character spaces.

print(f"{255:X}") 

print(f"{'Cat':<10}") # This format is for left alignment -> 
print(f"{'Cat':>10}") # This format is for right alignment -> 
print(f"{'Cat':^10}") # This format is for center alignment -> 

# This is for adding commas to large numbers
population = 123456789
print(f"{population:,}")

# This is for adding percentage sign
score = 0.8734
print(f"{score:.1%}")

# This is for scientific notations
number = 123456
print(f"{number:e}")

# Binary, Octal, and Hexadecimal
num = 20

print(f"{num:b}")   # Binary
print(f"{num:o}")   # Octal
print(f"{num:x}")   # Hexadecimal


# Leading Zeroes
number = 42
print(f"{number:05}")

# For sign display

num = 25
print(f"{num:+}")

# For thousands with decimals

salary = 1234567.891
print(f"{salary:,.2f}")