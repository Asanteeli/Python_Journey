"""# Practice on while loop

payment_amt = float(input("What is the payment from the customer? "))
penalty = 0
while payment_amt < 0:
    penalty = 1.5

    print("Sorry the payment cannot be negative.")
    payment_amt = float(input("What is the payment from the customer? "))

print(f"The amount is ${payment_amt:.2f} The penalty is ${penalty:.2f}")"""


"""number = 0

while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop") """

"""number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number please try again")
    number = int(input("Please type a positive number: "))
    
print(f"The number is: {number} ")"""

answer = ""

"""while answer != "yes":
    answer = input("May I have a piece of candy? ").upper()
    
print("Thank you")"""

"""animals = ["Goat", "Cow", "Elephant", "Sheep", "Bee", "Bear"]

for animal in animals:
    print(animals[1])
"""

"""colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)
    for i in range (2, 21, 2):
        print(f"---{i}")"""

"""scripture = "Pray without ceasing Thus saith the Lord"

for i in range(len(scripture)):
    letter = scripture[i]
    print(letter)"""

value = 20
while value < 20:
   value = value + 1
print(value)

value = 10
while value < 20:
   value = value + 1
print(value)

while value < 20:
   value = value + 1
print(value)