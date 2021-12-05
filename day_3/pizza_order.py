print("Welcome to the Pizza Deliveries! ")

bill=0

size=input("What size of pizza do you want? S, M, L").lower()
if size=="s":
    bill=bill+15
    print(f"your current bill is ${bill}")

elif size=="m":
    bill=bill+20
    print(f"your current bill is ${bill}")

elif size=="l":
    bill=bill+25
    print(f"your current bill is ${bill}")

pepperoni=input("Do you want to addd pepproni? Y or N").lower()
if pepperoni=='y':
    if size=="s":
        bill=bill+2
        print(f"pepperoni for small pizza is $2, your current bill is ${bill}")
    elif size=="m" or size=="l":
        bill=bill+3
        print(f"pepperoni for medium and large pizza is $3, your current bill is ${bill}")
else:
    bill = bill+0
    print(f"your total bill is ${bill}")


cheese=input("Do you want to extra add cheese? Y or N ").lower()
if cheese=="y":
    bill = bill+1
    print(f"your total bill is ${bill}")
else:
    bill=bill+0
    print(f"your total bill is ${bill}")