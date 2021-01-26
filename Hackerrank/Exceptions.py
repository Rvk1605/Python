n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(input())
    b.append(input())

for i in range(n):
    try:
        print(int(a[i])//int(b[i]))
    except ZeroDivisionError or ValueError as e:
        print("Error Code:", e)
