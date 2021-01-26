def get(a,b):
    def add(x,y):
        return x+y
    return add(a,b)+5
a=int(input("Enter Two Numbers:"))
b=int(input("Enter Two Numbers:"))
result=get(a,b)
print(result)