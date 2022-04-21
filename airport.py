def check_baggage(baggage):
    if(baggage>=0 and baggage<=40):
        return True
    else:
        return False
def check_immigration(expiry_year):
    if(expiry_year >=2030 and expiry_year<=2050):
           return True
    else:
     return False
def check_security(noc_status):
    if(noc_status=='valid'or noc_status=='VALID'):
        return True
    else:
        return False
def traveller():
   traveller_name=input("enter your name : ")
   traveller_id=int(input("enter the traveller id :"))
   baggage=int(input("enter the baggage weight: "))
   noc_status=input("enter your noc_status(valid/not valid): ")
   expiry_year=int(input("enter the expiry year: "))
   if(check_baggage(baggage)and check_immigration(expiry_year)and check_security(noc_status)):
     print(f"the name of traveller is {traveller_name} and his traveller id is : {traveller_id}")
     print("allow traveller to fly!!")
   else:
     print(f"the name of traveller is {traveller_name} and his traveller id is : {traveller_id}")
     print("Detain traveller for Re-checking!!")
traveller()


