def add(x,y):
    def diff(a,b):
        return a-b
    return x+y,diff(x,y)
a=int(input("Enter a No.:"))
b=int(input("Enter a No.:"))
result=add(a,b)
print(result)