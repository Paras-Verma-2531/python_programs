from re import S


class list_sum:
    list=[]
    def __init__(self,list):
       self.list=list
    def cal_sum(self):
        s=0
        for i in self.list:
            s=s+i
        return s
list=[1,2,3,4,5]
ob1=list_sum(list)
print(f"the  sum is : ",ob1.cal_sum())




