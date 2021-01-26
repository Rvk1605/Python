b,nk,nu=input().split()
b=int(b)
nk=int(nk)
nu=int(nu)
k=list(map(int, input().split()))
u=list(map(int, input().split()))
price=[]
for i in k:
    for j in u:
        if i+j<=b:
            price.append(i+j)
if len(price)==0:
    print("-1")
else:
    print(max(price))


