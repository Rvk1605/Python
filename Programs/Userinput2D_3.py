from numpy import*
a=ones((3,4),dtype=int)  #Here 3 = No. of Rows nad 4 =No. of Colums
print(a)
#printing Using For Loop
print("Using For Loop")
print("1st Method")
for i in a:
    for j in i:
        print(j,end=" ")
    print()
print("2nd Method")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end="")
    print()
#using For Loop
print("Using For Loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end="-")
        j+=1
    i+=1
    print()