s1=int(input("enter mark:"))
s2=int(input("enter mark:"))
s3=int(input("enter mark:"))
s4=int(input("enter mark:"))
s5=int(input("enter mark:"))
total=s1+s2+s3+s4+s5
percentage=(total/500)*100
if percentage<40:
    print("failed")
elif percentage>=40 and percentage<55:
    print("average")
elif percentage>=55 and percentage<65:
    print("fair")
elif percentage>=65 and percentage<75:
    print("average")
elif percentage>=75 and percentage<85:
    print("good")
elif percentage<85:
    print("excellent")
else:
    print("great job")


