class Box:
    def __init__(self,size):
        self.s=size
    def compare(self,small,large):
        if self.s>small:
            print("self is greater")
        elif small>large:
            print("small is largest")
        else:
            

b1=Box(10)
b2=Box(23)
b1.compare(b2)
    