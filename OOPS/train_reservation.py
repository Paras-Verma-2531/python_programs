class Train :
    def __init__(self, name, fair, no_of_seats):
        self.name = name
        self.fair = fair
        self.no_of_seats=[]
        for i in range(0,no_of_seats+1):
            self.no_of_seats.append(i)
        self.length=len(self.no_of_seats)    

    def getStatus(self):
        print("     ******************         ")
        print(f"the name of the train is {self.name} ")
        print(f" the number of seats available are : {self.length-1}")

    def fairInfo(self):
        print("                     *****************       ")
        print(f" the fair of the train {self.name} is {self.fair} ")

    def bookTicket(self):
        print("         *********       ")
        if self.length> 0:
            print("your booking is confirmed ")
            print(f"you seat number is {self.no_of_seats.pop(self.length-1)}")
            self.length=self.length-1
        else:
            print("please try in tatkal")
    def cancelTicket(self,seat_number):
        print("****|||||||||||****")
        print("your ticket has been cancelled");
        self.no_of_seats.append(seat_number)
        self.length=self.length+1   

shatabdi = Train("Shatabdi : 23031", 230, 10)
shatabdi.getStatus()
shatabdi.fairInfo()
shatabdi.bookTicket()
shatabdi.getStatus()
shatabdi.bookTicket()
shatabdi.getStatus()
shatabdi.cancelTicket(7)
shatabdi.bookTicket()
shatabdi.getStatus()
