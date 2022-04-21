from cmath import log10



def even(a):
    if(a%2==0):
        return a
list1=[1,2,3,4,5]
list2=list(filter(lambda a: a%2==0,list1))
#list2=list(filter(even,list1))
print(list2)

