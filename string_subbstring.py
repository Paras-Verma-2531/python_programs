string=input("enter the string: ")
substring=input("enter the substring : ")
length1=len(substring)
c=0
for i in range(len(string)-length1):
    check=string[i:length1+i]
    #print(check)
    if(substring==check):
        c=c+1
if(c>0):
    print(f"the substring {substring} is present {c} times in {string}")      
else:
    print(f"the substring {substring} is not present in {string} ")    
