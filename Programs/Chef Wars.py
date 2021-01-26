def check():
    h,p=map(int,input().split())

    for i in range(p):
        h=h-p
        if(h<=0):
            break
        p=p//2
    if h<=0:
        return 1
    else:
        return 0

n=int(input())
res=[]
for i in range(n):
    res.append(check())
for j in res:
    print(j)
