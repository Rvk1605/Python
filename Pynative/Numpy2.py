from numpy import*
n=int(input("Enter Starting Element:"))
a=arange(n,n*2,10,dtype=int)

print(a)
b=reshape(a,(5,2))
print(b)