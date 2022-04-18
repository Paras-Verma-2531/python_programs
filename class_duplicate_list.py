from ctypes import sizeof


class remove:
    list1=[]
    list2=[]
    size=int(input("enter the size of list: "))
    for i in range(size):
     list1.append(input(f"enter the {i+1} number: "))
    def remove_dup(self):
        for i in range(self.size):
            if (self.list1[i] in self.list2):
                continue
            else:
                self.list2.append(self.list1[i])
    def print_list(self):
        print("the updated list is : ",self.list2)      
ob1=remove()
ob1.remove_dup()
ob1.print_list()
                

         
        






 
            


