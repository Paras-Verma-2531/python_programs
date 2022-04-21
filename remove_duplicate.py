list=[]
for i in range(0,5):
    list.append(int(input(f"enter  the {i+1} number : ")))
list.append(50)
for i in range(0,4):
    list.pop()
print(f"the content of list is : {list}")   




