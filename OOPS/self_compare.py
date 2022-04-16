class paras:
    def __init__(self) :
        self.name="paras"
        self.age=19
    def update(self):
        self.age=18
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False        
ob1=paras()
ob2=paras()
ob2.update()
print(ob1.compare(ob2))

