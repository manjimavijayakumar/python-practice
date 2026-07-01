import random
user=int(input("enter the value:"))
system=random.randint(1,5)
if user==system:
    print("you won")
else:
    print("you lose",system)