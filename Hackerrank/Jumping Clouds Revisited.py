n,k=map(int, input().split())
c=list(map(int, input().split()))
E=100
for i in range(0,n,k):
    if(c[i]==0):
        E=E-1
    elif(c[i]==1):
        E=E-3
print(E)
