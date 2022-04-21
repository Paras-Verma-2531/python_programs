list=[]
c=0
string=input("Enter the string in both upper and lower case : ")
for i in range(len(string)):
    char=ord(string[i])
    if(char>=65 and char <=90):
        list.append(chr(char))
    elif(char>=97 and char <=122):
        char1=char-32
        list.append(chr(char1))
for i in range(65,91):
    for j in range(len(list)):
        char2=ord(list[j])
        if(i==char2):
            c=c+1
    if(c>0):        
     print(f"{chr(i)} is present {c} times") 
    c=0

        
        

            


