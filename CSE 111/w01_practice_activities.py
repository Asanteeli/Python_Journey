from datetime import datetime

# subtotal = float(input("Enter the subtotal for your purchases: "))

subtotal = 0
price = float(input("Please enter the price of the item: "))

while price != 0:
    qty = int(input("Please enter the quantity: "))
    subtotal = subtotal + (qty * price)
    price = float(input("Please enter the price of the item: "))

current_date_and_time = datetime.now()
week_day = current_date_and_time.weekday()

# Weekday(): Monday = 0, Tuesday = 1, Wednesday = 2, 
# Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6

#week_day = 5
discount = 0

if week_day == 1 or week_day == 2:
    if subtotal >= 50:
        discount = subtotal * 0.10
        subtotal = subtotal - discount
    else:
        amount_needed = 50 - subtotal 
        print(f"You are ${amount_needed:.2f} away from enjoying a 10% discount")
else:
    print("Come shop with us on a Tuesday or Wednesday to enjoy a 10% discount")

sales_tax = subtotal * 0.06
total = subtotal + sales_tax

if discount > 0:
    print(f"Discount amount: ${discount:.2f}")
print(f"The sales tax is: ${sales_tax:.2f}")
print(f"Total amount: ${total:.2f}")