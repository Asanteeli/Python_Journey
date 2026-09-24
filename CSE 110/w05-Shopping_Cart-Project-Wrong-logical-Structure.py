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
"5. Quit"
# add_item = 1
print("Welcome to the Shopping Cart Program!")

while True:
    print(f"{message}")
    first_action = int(input("Please enter an action: "))
    if first_action == 1:
        item = input("What item will you like to add? ").capitalize()
        price.append(float(input("What is the price of the item? ")))
        if item != "Quit":
            cart.append(item)
            print(f"{item} has been added to the cart.")
        else:
            print()
    elif len(cart) == 0: 
        print("You need to first add an item to your cart")
    
    print("The content of the shopping cart are: ")
    for i in range(len(cart)):
        # item = cart[i]
        print(f"{i+1}.{cart[i]} - ${price[i]:.2f}")
        # print(f"{message}")

    first_action = int(input("Please enter an action: "))
    print(f"{message}")
    if first_action == 2:
        view_cart = print(cart)
        print(f"{message}")
        int(input("Please enter an action: "))
    elif first_action == 3:
        remove_item = int(input("Which item will you like to remove? "))
        cart.pop(remove_item)
        print(cart)
    elif first_action == 4:
        print(f"The total price of items in the cart is{cart_total}")
    elif first_action == 5:
        break