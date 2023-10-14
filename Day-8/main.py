# PRACTICE EXERCISES

# |  1  |
# Calculator Program
operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = round(num1 + num2, 3)
    print(result)
elif operator == "-":
    result = round(num1 - num2, 3)
    print(result)
elif operator == "*":
    result = round(num1 * num2, 3)
    print(result)
elif operator == "/":
    result = round(num1 / num2, 3)
    print(result)
else:
    print(f"{operator} is not a valid operator.")


# |  2  |
# Weight convesion
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Grams? (kg or g): ")

if unit == "kg":
    weight = round(weight * 1000, 2)
    print(f"Your weight is: {weight} kilograms.") 
elif unit == "g":
    weight = round(weight / 1000, 2)
    print(f"Your weight is: {weight} grams.")
else:
    print(f"{unit} is not valid!")


# |  3  |
# Temperature conversion program
unit = input("Temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is {temp}°C")
else:
    print(f"{unit} is an invalid unit of mesurement!")
