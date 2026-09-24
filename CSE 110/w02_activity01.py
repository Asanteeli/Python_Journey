# Code Author: Elijah Asante
# Activiy 1: Ask user of his age and use the response to create a sentence

user_age = int(input("What is your age? ")) # Request for user's age and convert response to an integer

birthday_age = user_age + 1 # Add 1 to the age of the user

print(f"You will be {birthday_age} on your next birthday.")

# Activity 2: Ask user for number of eggs and multiply the response by 12

eggs_per_carton = 12
user_egg_cartons = int(input("How many egg cartons do you have? ")) # Ask user for number of cartons of egg

total_eggs = user_egg_cartons * eggs_per_carton # multiply the number of cartons by the number of eggs per carton

print(f"The total numer of eggs available are {total_eggs}.")

# Activity 3: Ask user for number of eggs and multiply the response by 12

number_of_cookies = int(input("What is the number of cookies? ")) # request for number of cookies available

number_of_people = int(input("Enter the number of people: ")) # request for number of people to share

share_cookies = number_of_cookies / number_of_people # share cookies amongst number of people

print(f"Then everyone gets {share_cookies} cookies.") # print final answer.