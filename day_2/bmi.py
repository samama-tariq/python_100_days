height=float(input("Enter the height in meter"))
weight=float(input("Enter the weight in kg"))

bmi=round(weight/(height**2),2)

print(f"Your calculated BMI is {bmi}")
