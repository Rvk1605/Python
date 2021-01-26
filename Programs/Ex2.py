a=int(input("Enter 1st Number:"))
exp=input("Enter Your Mthematical Expression( +,-,*,/,%)")
b=int(input("Enter 2nd Number:"))
if exp is '+':
    if a is 56 and b is 9:
        print(77)
    else:
        print("Sum = ",(a+b))
elif exp is '-':
    print("Diff = ",(a-b))
elif exp is '*':
    if a is 45 and b is 3:
        print(555)
    else:
        print("Product = ",(a*b))
elif exp is '%':
    print("Remainder = ",(a%b))
else:
    if a is 56 and b is 6:
        print(4)
    else:
        print("Division = ",float(a/b))