a=int(input("enter the number whose table u want on system file "))
with open('tabletxt','w') as f:
    for i in range(1,11 ):
        f.write(f"{a} X {i} = {a*i}\n")
       
        