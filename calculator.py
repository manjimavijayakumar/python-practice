a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
operator=input("enter any of the operator(+,-,*,/)")
if operator == '+':
    result=a+b
    print("Result =",result)
elif operator == '-':
    result=a-b
    print("Result =",result)
elif operator=='*':
    result=a*b
    print("Result =",result)
elif operator=='/':
    result=a/b
    print("Result =",result)    
else:
    print("no operations found")