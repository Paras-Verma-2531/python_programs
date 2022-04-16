for i in range(1,11):
    with open(f"table_of_{i}.txt","w")as f:
       for j in range(1,11):
        f.write(f"{i} X {j} = {j*i}\n")