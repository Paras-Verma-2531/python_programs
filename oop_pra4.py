class Train:
    seats=200
    def __init__(self,trainname,name):
        self.trainname=trainname
        self.name=name
    def bookticket(self):
        if(Train.seats>0):
         print(f"{self.name} your train  booking is succesful")
         Train.seats-=1
        else:
            print("no seats available")
    def showdetails(self):   
        if(Train.seats>0):      
         print(f"details : train name {self.trainname} \n your seat no. is {Train.seats} ") 
        else:
            print("no seats available")

passenger1=Train("garibrath","paras")           
passenger1.bookticket()
passenger1.showdetails()
passenger2=Train("rajdhani","simran")
passenger2.bookticket()
passenger2.showdetails()
