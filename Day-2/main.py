# Data Types :

# Strings
"Hello"
"123"
#Anything that is inside quotes, is a string.

# Integer
123
print(123 + 456)

# Float
537.23

# Boolean
True
False

print("---------")

# To know the data type
print(type("Hello World!"))
print(type(8))
print(type(45.76))
print(type(True))

print("---------")

# changing data types
num_char = len(input("What is your name? "))
print(num_char)
print(type(num_char))

new_num_char = str(num_char)
print(type(new_num_char))
"""
Converting to float:
float()
Converting to int:
int()
Converting to string:
str()
"""

print("---------")

# Checking data types
n = 4.234
type(n) #result float

print("---------")

# Exercise 1
"""
Write a program that adds the digits in a 2 digit number e.g if the input was 35, then the output should be 3 + 5 = 8

NOTE: Do not change the code on lines 39-41. Your program should work for different inputs e.g any two-digit number.
"""
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

########################################
#Write your code below this line 👇
firstDigit = int(two_digit_number[0])
secondDigit = int(two_digit_number[1])
result = firstDigit + secondDigit

print(result)

print("---------")

# Mathematical operations
"""
Addition, plus 👉 +
Subtraction, minus 👉 -
Multiplication 👉 *
Devision 👉 /
Power of 2 👉 ** 

Follow the BDMAS rule:
B = Braces/Paranthesis
D = Division
M = Multiplication
A = Addition
S = Subtraction

"""

# Exercise 2
"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height e.g if a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight(kg) / height^2(m^2)

NOTE: You should convert the result to a whole number.
"""
# 🚨 Don't change the code below 👇
height = input("enter your height in cm: ")  # Change to cm
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height) / 100

bmi = weight_as_int / (height_as_float ** 2)

bmi_rounded = round(bmi)

print(bmi_rounded)

print("---------")

# Round function
print(8/5)         # prints 1.6
print(round(8/5))  # prints 2

print("---------")

# Removes all digits after decimal point
print(8 // 5)

print("---------")

# f-string
score = 10
height = 2.3
isWinning = True

print(f"You score is {score}, your height is {height}, you are winning is {isWinning}")

# Escaping a Sting
speech = "My friend said: \"Hello\""
print(speech)

# the  += Operator
my_number = 4
my_number += 2
#result is 6

# The Modulo Operator
5 % 2    #result is 1

print("----------")

# Errors
"""
1. Syntax Error
Syntax errors happen when your code
does not make any sense to the computer.
This can happen because you've misspelt
something or there's too many brackets or
a missing comma.

2. Name Error
This happens when there is a variable
with a name that the computer
does not recognise. It's usually because
you've misspelt the name of a variable
you created earlier.
Note: variable names are case sensitive!

3. Zero Division Error
This happens when you try to divide by zero,
This is something that is mathematically
impossible so Python will also complain.
"""

# Exercise 3
"""
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

TODO: You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

NOTE: Your output should match the words in the example output precisely. You should round the results to the nearest whole number.

EXAMPLE INPUT:
56
EXAMPLE OUTPUT:
You have 12410 days, 1768 weeks, and 408 months left.
"""
# 🚨 Don't Change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

ageAsInt = int(age)

yearsRemaining = 90 - ageAsInt
daysRemaining = yearsRemaining * 365
weeksRemaining = yearsRemaining * 52
monthsRemaining = yearsRemaining *12

print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")

print("--------------")

# DAY-2 : FINAL PROJECT

print("Welcome to the tip calculator")

totalBill = input("What was the total bill? $")
totalBillAsInt = float(totalBill)

percentageTip = input("What percentage tip would you like to give? 10, 12 or 15? ")
percentageTipAsInt = int(percentageTip)

splitBill = input("How many people to split the bill? ")
splitBillAsInt = int(splitBill)

toPay = (totalBillAsInt * (1 + percentageTipAsInt / 100)) / splitBillAsInt

toPay = round(toPay, 2)

print(f"Each person should pay: ${toPay}")