# Functions
# defineing a function
def myfunction():
    name = input("What's your name bruv? ")
    nameLength = len(name)
    print(f"Your name is {nameLength} characters long.")

# calling/executing/running a function
myfunction()
# Take a look at all the in-built functions here: https://docs.python.org/3/library/functions.html

print("--------------")

# while loop
n = 1
while n < 100:
    print(n)

i = 0
while(i<3):
    print(i)
    i = i + 1

a = 0
while(a <= 43):
    a = int(input("Enter any number: "))
    print(a)