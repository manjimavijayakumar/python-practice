import time
print(time.ctime())
t=time.localtime()
print(t.tm_year)
print(t.tm_mon)
print('start...')
time.sleep(2)
print('stop')
for i in range(1,6):
    print(i)
    time.sleep(2)
