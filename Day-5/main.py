# Random module
import random

random_integer = random.randint(1, 10)
print(random_integer)

print("--------------")

# creating python modules
import my_module

print(my_module)

print("--------------")

# random function
random_float = random.random()
print(random_float)


print("--------------")

# EXERCISE 1

"""
INSTRUCTIONS

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

NOTE: The first letter should be capitalised and spelt exactly like in the the example: Heads, not heads.

There are many ways of doing this. But to practice the concepts I have learnt so far, generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g
1 means Heads
0 means Tails
"""
# Write your code below this line 👇
import random

random_number = random.randint(0, 1)

print("VIRTUAL COIN TOSS")
if random_number == 0:
    print("TAILS")
else:
    print("HEADS")


print("------------")

# lists
"""
list = [item1, item2]
start counting the items in the list from 0

fruits = ["Cherry", "Apple", "Pear"]

Cherry = 0
Apple = 1
Pear = 2
"""

fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0])  # will print "Cherry"
print(fruits[-1])  # will print "Pear"

# list length
print(len(fruits))
# you can put all types of data in a list
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# range of index in lists
fruits2 = ["Cherry", "Apple", "Pear", "Banana", "Grapes", "Gwava"]
print(fruits2[2:4])
print(fruits2[2:])   #By leaving out the end value, the range will go on to the end of the list:

# Change list items 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "pineapple"
print(thislist)

# Exercicse 2

"""
INSTRUCTIONS
You are going to write a program which will slelct a random name from a list of names. The person selected will have to pay for everybody's food bill.

NOTE: You are not allowed to use the choice() function.

Split the string name_string into individual names and puts them inside a List called names. For this to work, you must enter all the names a name followed by comma then space. e.g. name, name, name

EXAMPLE INPUT:
Aditya, Ujjwal, Jay, Michael, Jenny

EXAMPLE OUTPUT:
Ujjwal is going to buy the meal today!
"""
import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(names)

# Generate a random index within the range of the list
random_index = random.randint(0, len(names) - 1)

# Access the name using the random index
random_person = names[random_index]
print(f"{random_person} is going to buy the meal today.")
