k=5
print("the pattern is :")
for i in range(1,5):
    for p in range(1,k):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    k=k-1    
    print("")    
    
