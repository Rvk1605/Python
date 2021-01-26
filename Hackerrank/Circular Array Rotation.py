n,k,q=map(int ,input().split())
a=list(map(int, input().split()))
m=[]
for i in range(q):
    x=int(input())
    m.append(x)
l1=len(a)
l2=len(a)
for i in range(k):
    temp=a[l1-1]
    for j in range(l1-2):
        a[l1-1]=a[l2-2]
    a[0]=temp
print(a)

