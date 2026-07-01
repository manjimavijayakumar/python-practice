class person:
    count=0
    def __init__(self):
        person.count+=1

p1=person()
p2=person()
p3=person()
print(person.count)
        