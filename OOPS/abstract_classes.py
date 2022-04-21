from abc import ABC,abstractmethod
class paras(ABC):
    @abstractmethod
    def name(self):
        pass
class verma(paras):
    def name(self):
        print("hello!! body provided!!")
ob1=verma()
ob1.name()

