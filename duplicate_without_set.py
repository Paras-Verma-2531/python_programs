from black import lib2to3_parse


list1=[1,2,3,4,5,1,2,3]
list2=[]
for i in range(0,len(list1)):
    if(list1[i] in list2):
        continue
    else:
        list2.append(list1[i])
print("the list without duplicate elements is : ",list2)     
   