n,k=map(int, input().split())
a=list(map(int, input().split()))
pg=0
count=1
for i in a:
    for j in range(1,i+1):
        if j==k or j==i+1:
            pg=pg+1
        if j==pg:
            count=count+1

print(count)