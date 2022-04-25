class Train:
    def __init__(self,train_name,train_number):
        self.train_name=train_name
        self.train_number=train_number
    def InputRoute(self,train_name):
        filename=self.train_name    
        with open(f"{filename}.txt","a") as f:
             f.write(input("enter the source:")+"\n")
             f.write(input("enter the destination:"))
    def displayRoute(self,train_name):
        print(f"Route for {self.train_name} with train number {self.train_number} is:")
        filename=self.train_name    
        with open(f"{filename}.txt","r") as f:
            data=f.read().split("\n")
            for details in data:
                print(details)
Rajdhani=Train("Rajdhani","1220431")
Rajdhani.InputRoute("Rajdhani")
Rajdhani.displayRoute("Rajdhani")            


             
            
