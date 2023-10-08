# COMPARISON OPERATORS

"""
Operator    |    Meaning
--------------------------
1.  >       |   Greater than
2.  <       |    Less than
3.  >=      |   Greater than or equal to
4.  <=      |   Less than or equal to
5.  ==      |     Equal to
6.  !=      |    Not equal to
"""

#CONDITIONAL STATEMENTS

# if else function
print("Welcome to ROLER COSTER!!")

height = int(input("What is your height in centimeters? "))

if height >= 120:
    print("YAY! You can ride!!")
else:
    print("Wait buddy! You can't go ahead!")

# Exercise 1
"""
Write a program that workrs out whether if a given number is an odd or even number.
Even numebers can be divided by 2 with no remainder.

e.g. 86 is even because 86 / 2 = 43
43 does not have any decimal places. Therefore the devision is clean.

e.g. 59 is odd because 59 / 2 = 36.875
36.875 is not a whole number, it has decimal places. Therefore there is a remainder of 0.875, so the division is not clean.

The modulo is written as percentage sign(%) is Python. It gives you the remainder after a division.

e.g.
6 / 2 = 3 with no remainder

NOTE: Your output should match the Example Output format exactly, even the positions of the commas and full stops.
EXAMPLE INPUT 1:
43
EXAMPLE OUTPUT 1:
This is an odd number.

EXAMPLE OUTPUT 2:
94
EXAMPLE OUTPUT 2:
This is an even number.

"""
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to chech? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_check = int(number % 2)

if number_check == 0 :
    print("This is an even number.")
else:
    print("This is an odd number.")


print("----------")

# nested if-else statements
print("Welcome to ROLER COSTER!!")

height = int(input("What is your height in centimeters? "))

if height >= 120:
    print("YAY! You can ride!!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Wait buddy! You can't go ahead!")


print("---------")

# elif statments
print("Welcome to ROLER COSTER!!")

height = int(input("What is your height in centimeters? "))

if height >= 120:
    print("YAY! You can ride!!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age >= 18:
        print("Please pay $12")
    else:
        print("Please pay $7.")
else:
    print("Wait buddy! You can't go ahead!")

print("---------")
