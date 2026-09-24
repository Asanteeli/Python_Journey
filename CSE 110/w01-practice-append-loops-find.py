first_num = input("Select any number of your choice: ")
sec_num = input("Select a second number of your choice: ")

final_ans = int(first_num) + int(sec_num)

print(final_ans)

print(sec_num.find('t'))


weight = float(input("Enter your weight: "))
unit = input("Kg or Lbs? ").capitalize()

if unit == "Kg":
    print(f"{weight / 0.45:.2f}Kg")
else:
    print(f"{weight * 0.45:.2f}Lbs")

i = 1
while i <= 10:
    print(i)
    i = i + 1

numbers = [1, 2, 3, 4, 5]
numbers.append(7)
print(numbers)

numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

for item in numbers:
    print(item)