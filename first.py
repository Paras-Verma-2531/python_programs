'''
print('hello this is my first python program')
a=int(input(" enter a number "))

c=0
for i in range (1,a):
    if(a%i==0):
        c=c+1
if(c>1):
    print("the number is not prime")
else:
    print("the number is prime")

'''
# a=int(input("enter the marks of english subject "))
# b=int(input("enter the marks of maths  subject "))
# c=int(input("enter the marks of science subject "))
# d=(a+b+c)/3
# print(f"the average is {d}")
name="paras"
print(name[:5])