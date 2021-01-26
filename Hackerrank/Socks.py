from numpy import*
n=int(input())
a=zeros(n,dtype=int)
for i in range(len(a)):
    x=int(input())
    a[i]=x
print(a)