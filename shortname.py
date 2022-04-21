name=input("enter your full name: ")
last_name_pos=name.rindex(" ")
last_name=name[last_name_pos+1:]
length=len(last_name)
shortname=name[0]
str=" "
for i in range(len(name)-length-1):
    if(name[i]==' '):
        str=name[i+1]
        shortname=shortname+"."+ str
        str=" "
newname=shortname+ "."+ last_name
print(newname)
        