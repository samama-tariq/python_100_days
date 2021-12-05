print("Welcome to the rolleroster")
height=int(input("What is your height in cm?"))
bill=0

if height>120:
    print("You can ride!")
    age=int(input("what is your age?"))
    if age<12:
        bill=bill+5
        print(f"your current bill is ${bill}")
    elif age<=18:
        bill=bill+7
        print(f"your current bill is ${bill}")
    else:
        bill=bill+12
        print(f"your current bill is ${bill}")
    photo=input("Do you want photos? Y or No ").lower()
    if photo=="y":
        bill=bill+3
        print(f"your total bill is ${bill}")
    else:
        bill=bill+0
        print(f"your total bill is ${bill}")
else:
    print("Sorry, You can't ride!")