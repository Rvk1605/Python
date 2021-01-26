def solve(s):
    b=s.split()
    c=[]
    j=' '
    for items in b:
       c.append(items.title())
    j=j.join(c)
    return j



s=input()
result=solve(s)
print(result)