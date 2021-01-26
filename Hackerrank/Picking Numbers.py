from collections import Counter
n=int(input())
a=list(map(int, input().split()))
b=[]
c=[]
flag=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if abs(a[i]-a[j])<=1:
            flag=1
        else:
            flag=0
        if flag==1:
            count=count+1
    b.append(count)
print(b)
l=Counter(b).keys()
print((l))