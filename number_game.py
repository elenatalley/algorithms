
number = 7

user_input = input("Enter y if you want to play").lower()
if user_input == "y":
    user_number = int(input("enter your number "))
    if user_number == number:
        print("you are right")
    else:
        print("it is wrong")




