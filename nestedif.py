num=int(input("enter a value"))
if num%2==0:
    if num%3==0:
        print("number is divisible by 2 and 3")
    else:
        print("number is only divisible by 2 not by 3")
else:
    print("number is not divisible bt 2")