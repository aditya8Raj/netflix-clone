from car import Car

car_1 =  Car("Chevy", "Corvette", 2021, "blue")

print(car_1.make)         #instance variable
print(car_1.model)        #instance variable
print(car_1.year)         #instance variable
print(car_1.color)        #instance variable

car_1.drive()
car_1.stop()

#--------------------
# walrus operator:  assigns values to variables as part of a larger expression

# happy = True
# print(happy)

print(happy := True)

# I know all other basic stuff, so I will skip to the complex project

# GUI project with tkinter
from tkinter import *

window = Tk()  #instantiate an instance of a window
window.geometry("420x420")
window.title("My GUI program")
window.config(background="#5cfcff")


window.mainloop() #place window on computer screen, listen for events.