from numpy import*
arr=zeros((4,2),dtype=int)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        x=int(input())
        arr[i][j]=x
print(arr)
print("Shape = ",arr.shape)
print("Dimension = ",arr.ndim)
print("Bytes = ",arr[0].nbytes)