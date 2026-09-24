temperature = float(input("What is the temperature outside today? "))

if temperature < -15:
    print("It is too cold outside, you cannot go for your walk")

elif temperature < -5:
    weather = input("What is the weather condition outside? Eg. rainy, snowy, sunny ")
    weather = weather.lower().strip()
    

    if weather == "snowy":
        print("It is too cold outside do not go for the walk")
    elif weather == "rainy":
        print("You can go for the walk but go with your rain gear")
    elif weather == "sunny":
        print("You are free to go for the walk")
    else:
        print("Come again, I did not get your response")

else:
    print("Thanks for using this app, all comments are welcome")