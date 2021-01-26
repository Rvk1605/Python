n=int(input())
a=list(map(int, input().split()))
l=[]
for i in range(n):
    for j in range(n):
        if(a[i]==a[j]):
            d=abs(i-j)
            if d==0:
                pass
            else:
                l.append(d)
if len(l)==0:
    print("-1")
else:
    print(min(l))
