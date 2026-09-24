"""cbm = float(input("What is the CBM of your package? "))

if cbm > 1:
    print("Your package will be charged $260")

elif cbm > 0.6:
    print("The charge for your package will be reduced to $240")

else:
    print("The last charge is $200")

print("Thank you for doing business with us")"""

animal = input("What is the name of your favorite animal? ")
sound = ""

if animal.lower() == "cat":
    sound = "meow"
elif animal == "dog":
    sound = "ruff"
else:
    sound = "unknown"

print(f"The {animal} makes the sound {sound}.")