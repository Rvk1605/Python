def get(n):


    if n==1:
        return n
    else:
        sum=n+get(n-1)
        return sum
x=int(input("Enter A number:"))
res=get(x)
print(res)