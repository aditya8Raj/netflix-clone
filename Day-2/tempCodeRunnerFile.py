
print("Welcome to the tip calculator")

totalBill = input("What was the total bill? $")
totalBillAsInt = float(totalBill)

percentageTip = input("What percentage tip would you like to give? 10, 12 or 15? ")
percentageTipAsInt = int(percentageTip)

splitBill = input("How many people to split the bill? ")
splitBillAsInt = int(splitBill)

toPay = (totalBillAsInt * (1 + percentageTipAsInt / 100)) / splitBillAsInt

toPay = round(toPay, 2)

print(f"Each person should pay: ${toPay}")