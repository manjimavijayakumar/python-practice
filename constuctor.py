class person:
    def __init__(self,name,age,place):
        self.n=name
        self.a=age
        self.p=place
    def display(self):
        print(self.n,self.a,self.p)

p1=person('anu',23,'kochi')
p1.display()
p2=person('anju',34,'palakkad')
p2.display()
