class Employee:
     
    def __init__(self,firstname,Lastname,pay):
        self.firstname=firstname
        self.Lastname=Lastname
        self.pay=pay
    def generateEmail(self):
      self.email=self.firstname+"."+self.Lastname+"@company.com"
    def printDetails(self):
        print(self.firstname)
        print(self.Lastname)
        print(self.pay)
        print(self.email)
employe1=Employee("Akshita","Singh","100000")
employe1.generateEmail()
employe1.printDetails()




        