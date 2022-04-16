string=input("enter a alphanumeric string : ")
c=0;
for chr in string:
    if(chr == ' '):
        continue
    else:
     char1=ord(chr)
     if(char1>=65 and char1 <=90)or(char1>=97 or char1 <=122):
        c=c+1;
print(f" the number of aplhabets in {string} are {c}")     

