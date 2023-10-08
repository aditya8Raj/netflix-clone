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