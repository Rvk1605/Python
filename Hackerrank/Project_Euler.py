n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)

for i in range(n):
    sum=0
    for j in range(1,a[i]):
        if j%3==0 or j%5==0:
            sum=sum+j
    print(sum)