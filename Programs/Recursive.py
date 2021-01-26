def fibo(n):
    f1=0
    f2=1
    if n==1:
        return 1
    else:
        f=f1+f2+fibo(n-1)
    print(f)





n=int(input("Enter no. of Elements:"))
fibo(n)