from numpy import*
a=zeros(5,dtype=int)
print("Enter Elements")
for i in range(len(a)):
    x=int(input())
    a[i]=x
for i in range(len(a)):
    print(a[i],end=' ')
