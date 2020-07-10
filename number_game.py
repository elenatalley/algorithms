
number = 7

user_input = input("Enter y if you want to play").lower()
if user_input == "y":
    user_number = int(input("enter your number "))
    if user_number == number:
        print("you are right")
    else:
        print("it is wrong")


''''
напишите код, который переводит целое число в строку, 
при том что его можно применить в любой системе счисления.'''

# Второй аргумент функции int отвечает за указание основания системы счисления:
print(int('ABC', 16))
