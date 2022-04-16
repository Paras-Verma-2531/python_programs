class programmer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the age of the {self.name} is {self.age}")
        print(f"the salary of the {self.name} is {self.salary}")


paras = programmer("paras", 19, 100000)
akshita = programmer("akshita", 18, 100000)
prakriti = programmer("prakriti", 18, 100000)
paras.getdetails()
akshita.getdetails()
prakriti.getdetails()
