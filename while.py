even_count=0
odd_count=0
i=1
while i<=100:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print('even count is:',even_count)
print('odd count is:',odd_count)