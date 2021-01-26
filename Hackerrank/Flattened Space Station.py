n,m=map(int, input().split())
l=list(map(int ,input().split()))
d=[]
for i in range(n):
    if n==m:
        d.append(0)
        break
    else:
        print(n-m+1)