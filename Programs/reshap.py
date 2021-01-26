#Array Created Using Linspace
from numpy import*
a=linspace(2,12,6,dtype=int)
print(a)
b=reshape(a,(3,2))
print(b)
#Array ceated Using Logspace
c=logspace(2,3,9,dtype=int)
print(c)
print("After Reshaping")
d=reshape(c,(3,1,3))
print(d)
#Converting from 2D to 1D
print("2D to 3D")
e=array([[1,2,3,4],[5,6,7,8]])
f=reshape(e,(8))
print(f)
#Converting 2 or 3D array to 1D using Flatten()
print("Using Faltten")
h=d.flatten()
print(h)