salary=int(input("enter the salary:"))
if salary>=10000 and salary<15000:
    tax=salary*(5/100)
elif (salary>=15000 and salary<20000):
    tax=salary*(10/100)
elif (salary>=20000 and salary<30000):
    tax=salary*(15/100)
elif (salary>30000):
    tax=salary*(18/100)
net_salary=salary-tax
print("tax amount is:",tax)
print("net salary is:",net_salary)