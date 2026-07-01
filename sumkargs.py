def sum(*numbers):
    print(numbers)
    s=0
    for i in numbers:
        s+=i
    print(s)
    return
sum( 1,2,3,4,5,6,7,8,9,10)