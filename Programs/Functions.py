def Calc(x,y):
    return (x+y,x-y)

a=int(input("Enter !st Number:"))
b=int(input("Enter 2nd Number:"))
sum,diff=Calc(a,b)
print("Sum = ",sum)
print("Difference = ",diff)
