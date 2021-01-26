l1=[10,4,3,4,6,'Taj',98]
for i in range(len(l1)):
    if type(l1[i]) is int:
        if l1[i]>6:
            print(l1[i])

#2nd Method
print("2nd Method")
for item in l1:
    if str(item).isnumeric() and item>6:
        print(item)