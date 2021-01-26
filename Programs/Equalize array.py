from collections import Counter
n=int(input())
a=list(map(int,input().split()))
s=str(a)
c=Counter(a)
count=Counter(a).values()
r=len(a)-max(count)
print(r)



