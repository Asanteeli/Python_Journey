"""
Author: Elijah Asante
Purpose: Shopping Cart - Milestone I
"""
cart = []
item = ""
cart_total = ""
message = "Please select one of the following:\n" \
"1. Add item\n" \
"2. View Cart\n" \
"3. Remove Item\n" \
"4. Compute Total\n" \
"5. Quit"
# add_item = 1
print("Welcome to the Shopping Cart Program!")
print(f"{message}")

first_action = int(input("Please enter an action: "))

while item != "Quit":
    item = input("What item will you like to add? ").capitalize()
    if item != "Quit":
        cart.append(item)
        print(f"{item} has been added to the cart.")

for i in range(len(cart)):
    item = cart[i]
    print(f"{item}")
print(f"{message}")


    
    # elif first_action == 2:
    #     view_cart = print(cart)
    # elif first_action == 3:
    #     remove_item = cart.pop(input("Which item will you like to remove?"))
    # elif first_action == 4:
    #     print(f"The total price of items in the cart is{cart_total}")
    # elif first_action != "Quit":
    #     print()