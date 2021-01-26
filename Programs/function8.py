def check(sr,st):
    c=[]
    for i in range(sr,st):
        if(i%2==0):
            c.append(i)
        else:
            pass
    return c
n=int(input("Enter Starting Range:"))
m=int(input("Enter Ending:"))
result=check(n,m)
print(result)
