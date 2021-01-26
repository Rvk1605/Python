from numpy import*
a=array([10,20,30,40,50])
b=array([[2,3,4,5],[3,6,8,5]],dtype=float)
# ndim attribute
print("1D Array=",a.ndim)
print("2D Array=",b.ndim)
print()
#Shape Attribute
print("1D Array=",a.shape)
print("2D Array=",b.shape)
print()
#Size Attribute
print("1D Array=",a.size)
print("2D Array=",b.size)
print()
# itemsize Attribute
print("1D Array=",a.itemsize)
print("2D Array=",b.itemsize)
print()
# dtype Attribute
print("1D Array=",a.dtype)
print("2D Array=",b.dtype)
print()
# nbytes Attribute
print("1D Array=",a.nbytes)
print("2D Array=",b.nbytes)
print()
