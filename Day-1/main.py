# Printing to the console in Python 🐍

print("Hello World!")

print("----")

# Exercise 1 - Printing

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("----")

# Exercise 2 - Debugging Practice

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
# print("e.g. print("Hello " + "world")")  # this is wrong, correct line is below
print("e.g. print('Hello ' + 'World')")
print("New lines can be created with a backslash and n")


print("----")

# Line changing
print("Hello world!\nHello World!")

print("----")

# Concatanation
print("Hello" + " " + "World!")
print("Hello " + "I " + "am " + "Aditya Raj.")

print("----")

# input function
"""
input("What is your name?")
print("Hello " + input("What is your name?"))
"""


print("----")

#variables
work = "I am learning to code"   # name is a variables
print(work)

print("----")

# Exercise 3 

# Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
#NOTE: Your program should work for different inputs. e.g. any name that you input.

#userName = input("What is your name? ")
#print("Your name is " + str(len(userName)) + " characters long.")

print("----")

# Exercise 4
"""
#Write a program that switches the values stored in the variable a and b. NOTE: Do not change the code on lines 64-65 and 78-79. Your program should work for different inputs.e.g any value of a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input ("b: ")
# 🚨 Don't change the code above 👆

#####################################
#Write your code below this line 👇
c = a
a = b
b = c


#Write yout code above this line 👆
######################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
# 🚨 Don't change the code above 👆

print("----")

"""

# DAY 1 - FINAL PROJECT

# Project : Brand Name Generator
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.

print("Welcome to the Band Name Generator!!")
cityName = input("What's the name of the city you grew up in? ")
petName = input("What's your pet name? ")
print("Your Band Name is " + cityName + " " + petName)
