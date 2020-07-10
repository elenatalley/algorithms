"""
 write a program that prints out numbers from 1 to 100 under the following conditions:
 Multiples of three, (3, 6, 9, 12, etc.) must be replaced by the word Fizz in the printout,
 multiples of five, (5, 10, 15, 25, etc.) must be replaced by Buzz, and multiples of both three
 and five (15, 30, 45, etc.) must be replaced by FizzBuzz
"""

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBu zz')
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:

        print(num)