import numpy as np

a=np.array([[10,20,30,40],
               [40,50,60,70]])
print(a)
print(type(a),a.dtype)
#Changing Data Type
b=np.array([[1,2,3,4],[9,8,7,7]],dtype=float)
print(b)
print(b.dtype)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
