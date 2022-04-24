f=open("name.txt","w")
a=input("ENTER A STRING : ")
f.write(a)
f.close()
f=open("name.txt","r")
data=f.read()
word=data.split()
print("TOTAL WORDS : ",len(word))
f.close()


