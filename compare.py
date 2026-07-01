class Box:
    def __init__(self,size):
        self.s=size
    def compare(self,other):
        if self.s==other.s:
            print("these are equal")
        else:
            print("not equal")

b1=Box(10)
b2=Box(23)
b1.compare(b2)
    