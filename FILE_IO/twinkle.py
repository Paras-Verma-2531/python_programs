with open("twinkle.txt","r") as f:
    data=f.read()
    if("twinkle" in data ):
        print("twinkle is present")
    else:
        print("twinkle is  not present")
