def natural(n):
    sum=(n*(n+1))/2;
    print(f"the sum of first {n} natural number is {sum}")
def fibonacci(n):
    print(f"fibonacci series of {n} terms is : ")
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
      c=a+b
      print(c,end=" ")
      a=b
      b=c
natural(5)   
fibonacci(5)