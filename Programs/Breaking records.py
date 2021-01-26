n = int(input())
a = list(map(int, input().split()))
h=a[0]
l=a[0]
c1=0
c2=0
for i in range(n):
    if a[i]>h:
        h=a[i]
        c1=c1+1
    elif a[i]<l:
        l=a[i]
        c2=c2+1
    elif a[i]==h or a[i]==l:
        pass
print(c1,c2)

