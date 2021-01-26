f=open("Sum.py","w")
f.write("a=int(input())\n")
f.write("b=int(input())\n")
f.write("sum=a+b\n")
f.write("print(sum)")
f.close()

f=open("sum.py","r+")

f.close()

print()
print("Second Method")

f=open("Product.py","w")
f.close()
f=open("Product.py","a")
f.write("\na=int(input())\nb=int(input())\nproduct=a*b\nprint(product)\n")
f.close()
f=open("Product.py","r")
print(f.read())