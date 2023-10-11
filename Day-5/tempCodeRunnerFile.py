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