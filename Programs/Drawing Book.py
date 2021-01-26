def last(n,p):
    d=abs(n-p)
    if n%2!=0 and p%2!=0:
        c=d//2
    elif n%2!=0 and p%2==0:
        if d<2:
            c=0
        else:
            c=d//2
    elif n%2==0 and p%2!=0:
        c=(d//2)+1
    elif n%2==0 and p%2==0:
        c=d//2
    print(c)

def first(p):
    d=abs(p-1)
    if d==1:
        c=1
    elif p%2==0:
        c=(d//2)+1
    else:
        c=d//2
    print(c)

n=int(input())
p=int(input())
if abs(n-p)>abs(1-p):
    first(p)
else:
    last(n,p)