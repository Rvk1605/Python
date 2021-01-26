def count()


n=int(input())
for i in range(n):
    p,c,m=map(int, input().split())
    numc=p//c
    rem=numc%m
    num=(numc-rem)//m
    print(numc+num)
