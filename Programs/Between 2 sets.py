n,m=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
d=[]
f=[]
for i in a:
    for j in b:
        x=j//i
        if x<=min(b):
            d.append(x)
print(d)


