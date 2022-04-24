class A:
    a="paras"
    @staticmethod
    def greet():
        print("hello user")
ob=A()
ob.a="verma"    
print(A.a)
print(ob.a)
ob.greet()