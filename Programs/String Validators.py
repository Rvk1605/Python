a=input()

for i in range(len(a)):
    if a[i].isalnum():
        print("True")
        break
    else:
        print("False")
for i in range(len(a)):
    if a[i].isalpha():
        print("True")
        break
    else:
        print("False")
for i in range(len(a)):
    if a[i].isdigit():
        print("True")
        break
    else:
        print("False")

for i in range(len(a)):
    if a[i].islower():
        print("True")
        break
    else:
        print("False")

for i in range(len(a)):
    if a[i].isupper():
        print("True")
        break

