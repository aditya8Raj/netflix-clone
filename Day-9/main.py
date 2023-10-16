# logical operators = used on conditional statements

#              and = checks two or more conditions if True
#              or  = checks if at least one condition is True
#              not = True if condition is False, and vice versa

temp = float(input("What is the temperature? "))

if temp > 0 and temp <= 30:
    print("Temperature is good.")
else:
    print("Temperature is bad.")

# Find function find()
name = input("What's your name? ")
result = name.find("z")
print(result)


# Conuntdown time program
import time

myTime = int(input("Set your timer(in seconds): "))

for x in range(myTime, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times UP!!")

# functions with arguments
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old!")

happy_birthday("Aditya", 20)
happy_birthday("John", 24)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("John", 50, "August 22, 2022")

# return statement
def addition(x, y):
    z = x + y
    return z

print(addition(1, 2))


first_name = input("First Name: ")
last_name = input("Last Name: ")
def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = createName(first_name, last_name)

print(f"You name is: {full_name}")

# exception handling
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except Exception:
    print("Something went wrong :(")