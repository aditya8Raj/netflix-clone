# For loop
fruits = ["Apple", "Banana", "Mango", "Grapes"]

for fruit in fruits:
    print(fruit)

print("---------")

# 👨‍🏫 Practice exercise 1
"""
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 / 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164

EXAMPLE INPUT:
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

EXAMPLE OUTPUT
171

NOTE: You can't use len() and sum() functions. You have to use For Loop only.
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code below 👆

# Write your code below this line 👇

addAllHeight = 0
for num in student_heights:
    addAllHeight += num

average = round(addAllHeight / len(student_heights))
print(f"Average height of the students is: {average}")


print("---------")

# 👨‍🏫 Practice exercise 2
"""
You are going to write a program that calculates the higest score from a list of scores.
e.g :-
|---------------------------------------------------|
| student_scores = [78, 65, 89, 86, 55, 91, 64, 89] |
|---------------------------------------------------|

NOTE: You aer not allowed to use the max or min functions. The output words must match the example. i.e

|--------------------------------------|
| The higest score im the class is: x  |
|--------------------------------------|

EXAMPLE INPUT : 
`78 65 89 86 55 91 64 89`

In this case, student_scores would be a list that looks like :-
[78, 65, 89, 86, 55, 91, 64, 89]

EXAMPLE OUTPUT : 
|--------------------------------------|
| The higest score im the class is: 91 |
|--------------------------------------|

"""

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores separated by spaces: ")
student_scores = student_scores.split()  # Split the string into a list
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# For loop with range
for number in range(1, 11):
    print(number)

total = 0
for num in range(1, 101):
    total += num
print(total)

# 👨‍🏫 Practice exercise 3
"""
INSTRUCTIONS:
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

e.g. 2 + 4 + 6 + 8 + 10 ... + 98 + 100

NOTE: There should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
"""
# Write your code below this line 👇
total = 0
for evenNumber in range (2, 101, 2):
    total += evenNumber
print(total)



print("-----------")


# 💪 PASSWORD GENERATOR PROJECT 💪
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PythonPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")