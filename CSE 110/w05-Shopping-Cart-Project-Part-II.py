"""
Author: Elijah Asante
Purpose: Shopping Cart - Full Project
"""

cart = []
price = []
item = ""
cart_total = sum(price)

message = "Please select one of the following:\n" \
"1. Add item\n" \
"2. View Cart\n" \
"3. Remove Item\n" \
"4. Compute Total\n" \
"5. Quit"               # This block of code is the variable to store the menu instruction

print("Welcome to the Shopping Cart Program!")  # This line welcomes the user

while True:         # This marks the beginning of the loop. If True is true then the loop continues
    print(message)  # Menu instructions are printed here
    first_action = int(input("Please enter an action: "))   # This line requests an action from user to choose

    # Menu item 1
    if first_action == 1:   # This Line of code is for what happens when user chooses option 1

        while True:
            item = input("What item would you like to add? (Type 'quit' when done): ").capitalize()

            if item.lower() == "quit": # If user keys in quit the code execution ends.
                break

            item_price = float(input("What is the price of the item? "))

            cart.append(item)
            price.append(item_price)

            print(f"{item} has been added to the cart.\n")


    # Menu item 2   # This Line of code is for what happens when user chooses option 2
    elif first_action == 2:
        if len(cart) == 0:  # Once first action is 2 then content of the cart is scanned and as nothing is found ....
            print("Your shopping cart is empty.")   # .... This message is printed
        else:
            print("The contents of the shopping cart are:") # If after the comparison the cart contains an item(s) this is printed
            for i in range(len(cart)):      # Once the cart contains item(s) this loop sets in...
                print(f"{i + 1}. {cart[i]} - ${price[i]:.2f}")  # ... this line prints the content of the cart.


    # Menu Item 3   # This Line of code is for what happens when user chooses option 3
    elif first_action == 3:
        if len(cart) == 0:  # Once first action is 3 then content of the cart is scanned and as nothing is found ...
            print("Your shopping cart is empty.")   # .... This message is printed
        else:
            print("The contents of the shopping cart are:") # If after the comparison the cart contains an item(s) this is printed
            for i in range(len(cart)):   # Once the cart contains item(s) this loop sets in...
                print(f"{i + 1}. {cart[i]} - ${price[i]:.2f}")  # ... this line prints the content of the cart.
            remove_item = int(input("Which item would you like to remove? ")) # This is a variable storing the items inputed by user to be removed from the cart
            removed = cart.pop(remove_item - 1) # This is also a variable that stores the action of removing the item(s)
            price.pop(remove_item - 1) # This line removes the price of the item as well
            print(f"{removed} was removed.")    # This line prints the item(s) that were removed from the cart


    # Menu Item 4   # This Line of code is for what happens when user chooses option 4
    elif first_action == 4:
        cart_total = sum(price) # This line prints the sum of the value of item(s) in the cart on request from user
        print(f"The total price of the items in the shopping cart is ${cart_total:.2f}") # This line prints the result out


    # Menu Item 5   # This Line of code is for what happens when user chooses option 5
    elif first_action == 5:
        print("Thank you for your Usage") # Once option 5 is taken this line is printed
        break

    # User value not found in menu options 1 - 5
    else:
        print("Invalid option. Please choose between 1 and 5.") # This line prints when the value entered isn't in the menu range