from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hii")  
t1=hello()
t2=hi()
t1.start()
t2.start()

