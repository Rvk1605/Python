def bday():
    b,w=input().split()
    b=int(b)
    w=int(w)
    bc,wc,z=input().split()
    bc=int(bc)
    wc=int(wc)
    z=int(z)
    n=(b*bc)+(w*wc)
    print(n)
    if bc+z<wc:
        c=bc*b+(bc+z)*w
    elif (wc+z)<bc:
        c=(wc+z)*(b+wc)*w

    if bc==wc:
        cost=n
    else :
        cost=c





n=int(input())
c=[]
for i in range(n):
    cost=bday()
    l=c.append(cost)
    print(l)