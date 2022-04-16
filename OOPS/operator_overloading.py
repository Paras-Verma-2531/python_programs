class operator:
    a=0
    def __init__(self,a):
        self.a=a
    def __add__(self,ob1): # just change the operator name to different binary operators for operator overloading
        return self.a+ob1.a
ob1=operator(30)
ob2=operator(30)
sum=ob1+ob2
print(sum)
