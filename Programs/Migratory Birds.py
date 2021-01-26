n=int(input("Enter No. of Birds:"))
a=[]
for i in range(n):
    a.append(int(input().split()))
b=[]
for i in range(5):
    x=a.count(i+1)
    b.append(x)
print(b)