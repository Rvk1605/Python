import math
s=input()
l=len(s)
r1=int(math.sqrt(l))
count=0
r2=r1+1
if r1*r2<l:
    r1=r1+1
for i in range(r1+1):
    for j in range(i,l,r2):
        print(s[j],end='')
    print(end="\t")