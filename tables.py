def table(n):
    for i in range(1,n+1):
        with open(f"table of {i}.txt","w") as f:
            for k in range(1,11):
                 print(f.write(f"{i}X{k}={i*k}\n"))
        #break                       
table(6)                 
