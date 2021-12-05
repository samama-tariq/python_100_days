height=float(input("Enter the height in meter"))
weight=float(input("Enter the weight in kg"))

bmi=round(weight/(height**2),2)

if bmi<=18.5:
    print("You're under weight")
elif bmi >18.5 and bmi <25:
    print("You have normal weights'")
elif bmi >25 and bmi <30:
    print("Youre over weight")
elif bmi>30 and bmi<35:
    print("Youre obese")
else:
    print("clinically obese")
