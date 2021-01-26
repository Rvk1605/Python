t=int(input())
c=[]
for i in range(t):
    count=0
    x=int(input())
    s=list(str(x))
    for j in range(len(s)):
        if int(s[j])==0:
            pass
        elif x%int(s[j])==0:
            count=count+1
    c.append(count)
for i in c:
    print(i)

