print("Welcome to tip calculator")

total_bill=float(input("what was the total bill? "))

percentage=int(input("What percentage tip would you like to give? 10,12 or 15? "))

person=int(input("How many people to split the bill? "))

calculated_bill=((total_bill*(percentage/100))+total_bill)/7

print(f"Each person should pay: ${calculated_bill}")