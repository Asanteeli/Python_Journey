"""
Author: Elijah Asante
Purpose: Qualifying for a Loan
"""
#employment = input("Are you currently employed? ")
#employment_period = input("How long have you been working? ")
loan_size = int(input("On a scale of 1 to 10, rate the size of the amount needed: "))
credit_history = int(input("On a scale of 1 to 10, rate your credit history: "))
income = int(input("On a scale of 1 to 10, rate your monthly income: "))
down_payment = input("What is your downpayment? ")
can_loan = False


if loan_size >= 5:
    print("Answer the following questions....")
elif credit_history <= 7 and income <= 7:
    print("The decision is Yes")

    if (credit_history >= 7 or income >= 7) and down_payment >= 5:
        print("The decision is Yes")
    else:
        print("The decision is No")

elif loan_size <= 5:
        print("Answert the following questions")
elif credit_history < 4:
     print("The decision is No")
     if income >= 7 or down_payment >= 7:
          print("The decision is Yes")
     elif income >= 5 and down_payment >= 4:
          print("The answer is Yes")
     else:
          print("The decision is No")

