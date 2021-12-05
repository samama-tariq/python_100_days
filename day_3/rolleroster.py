print("Welcome to the rolleroster")
height=int(input("What is your height in cm?"))

# ==, >=, <=, !=, <, >
if height>120:
    print("You can ride!")
    age=int(input("what is your age?"))
    if age<12:
        print("please pay $5")
    elif age<=18:
        print("please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, You can't ride!")