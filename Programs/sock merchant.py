from collections import Counter
n=int(input())
a=list(map(int, input().split()))

b=list(Counter(a).values())
count=0
for i in range(len(b)):
    count=count+(b[i]//2)
print(count)



