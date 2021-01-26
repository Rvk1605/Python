n=int(input())
c=list(map(int, input().split()))
count=0
i=0
while i<=n:
    if i==len(c)-2:
        i=i+1
    elif c[i+1] == 0 and c[i+2] == 0 or c[i+1] == 1:
        i=i+2
    elif c[i+1]==0 and c[i+2]==1:
        i=i+1
    count=count+1
    if(i==len(c)-1):
        break
print(count)
