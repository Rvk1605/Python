a=int(input("Enter No. of Rows nad Columns:"))
n=bool(int(input("Enter 1 or 0:")))
if n is True:
    print("Pattern Will Be")
    for i in range(a):
        for j in range(i+1):
            print("*",end="")
        print()
else:
    print("Pattern Will Be")
    for i in range(a):
        for j in range(a-i):
            print("*",end="")
        print()

print("\n2nd Method")

a=int(input("Enter No. of Rows nad Columns:"))
n=bool(int(input("Enter 1 or 0:")))
if n is True:
    print("Pattern Will Be")
    for i in range(1,a+1,1):
        print("*"*i)

else:
    print("Pattern Will Be")
    for i in range(a,0,-1):
        print("*"*i)


