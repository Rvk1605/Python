
n=int(input())
a=list(map(int, input().split()))
c=[]
count=0
for i in range(len(a)):
    c.append(len(a))
    if len(a)==0:
        break
    m=min(a)
    a.sort()
    a.reverse()
    for j in a:
        if j == m:
            for k in range(a.count(m)):
                a.pop()
for j in range(c.count(0)):
    c.remove(0)
for k in c:
    print(k)