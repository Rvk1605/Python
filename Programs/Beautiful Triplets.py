n,d=map(int, input().split())
a=list(map(int, input().split()))
count=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            d1=a[j]-a[i]
            d2=a[k]-a[j]
            if d1==d and d2==d:
               count=count+1

print(count)
