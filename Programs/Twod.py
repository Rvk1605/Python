from numpy import*
a=zeros((3,2),dtype=int)
print(a)
# printing using for Loop
# (1st Method)
print("After Using For Loop")
print("1st Method")
for i in a:
    for j in i:
        print(j,end='')
    print()
#2nd Method
print("2nd Method")
for k in range(len(a)):
    for l in range(len(a[i])):
        print(a[k][l],end='')
    print()



#printing using While Loop
print("After Using While Loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
