items_list = []
individual_item = ""
print("Please enter the items of the shopping list (type: quit to finish):")

while individual_item != "quit":
    individual_item = input("Please enter the items of the shopping list: ")
    if individual_item != "quit":
        items_list.append(individual_item)

for i in range (len(items_list)):
    item = items_list[i]
    print(f"{i}.{item}")

# new_index = int(input("Which item will you want change? "))
# new_item = input("What is the new item? ")

# items_list[new_index] = new_item

# for i in range(len(items_list)):
#     item = items_list   
# items_list.pop(new_index)
# new_item.insert(2, "new_item")
# print({item})

