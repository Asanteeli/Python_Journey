# def greetings(dude):
#     """Purpose: This function greets new users"""
#     print(f"What's up {dude}. Welcome for visiting our site")
# user = input("What username will you prefer to use? ")

# greetings(user)

# def greetings(age, amount):
#     """Purpose: This function greets new users"""
#     print(f"What's up I am {age} years old. You will get a bonus of ${amount} for visiting our site")
# user = input("Enter your age: ")
# figure = 25

# greetings(user, figure)

def calc(number1, number2):
    """Purpose: Testing a function that does some calculations and returns the value to the caller"""
    total_age = number1 + number2
    return total_age


age1 = 23
age2 = 27
final_answer = calc(age1, age2)
print(final_answer)
# x = 10
# y = 25
# final_answer = calc(x, y)
# print(final_answer)

final_answer = calc(age1, age1)
print(final_answer)

