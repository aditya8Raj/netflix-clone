# EXERCISE 1

"""
Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.
1. Under 18.5 they are underweight
2. Over 18.5 but below 25 they have a normal weight
3. Over 25 but below 30 they are overweight
4. Over 30 but below 35 they are obese
5. Above 35 they are clinically obese

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight(kg) / height^2 (m^2)

NOTE: You should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above e.g. underweight, normal weight, overweight, obese clinically obese.

EXAMPLE INPUT:
|-----------------|
|  weight = 80    |
|  height = 1.75  |
|-----------------|

EXAMPLE OUTPUT:
80 / 1.75 * 1.75 = 27.755102040816325
|----------------------------------------------|
| Your BMI is 28, you are slightly overweight  |
|----------------------------------------------|
"""
# 🚨 Don't change the code below 👇
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / (height ** 2))

bmi = round(weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


print("--------------")

# EXERCISE 2

"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on user's order, work out their final bill.
 ---------------------------------------------
|                                             |
| Small Pizza : $15                           |
| Medium Pizza : $20                          |
| Large Pizza : $25                           |
|                                             |
| Pepperoni for Small Pizza: +$2              |
| Pepperoni for Medium or Large Pizza: + $3   |
|                                             |
| Extra cheese for any size pizza: +$1        |
|                                             |
 ---------------------------------------------

EXAMPLE INPUT:
|------------------------|
| size = "L"             |
| add_pepperoni = "Y"    |
| extra_cheese = "N"     |
|------------------------|

EXAMPLE OUTPUT:
|--------------------------|
| Your final bill is: $29. |
|--------------------------|
"""
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
money = 0

# selecting size
if size == "S" or size == "s":
    money = 15
elif size == "M" or size == "m":
    money = 20
else:
    money = 25

# adding pepperoni
if add_pepperoni == "Y" or add_pepperoni == "y" and money == 15:
    money += 2
elif add_pepperoni == "Y" or add_pepperoni == "y" and money == 20 or money == 25:
    money += 3
else:
    money += 0

# extra cheese
if extra_cheese == "Y" or extra_cheese == "y":
    money += 1
else:
    money += 0

print(f"Your final bill is ${money}")