f=open("IO Basics.txt","rb") # Reading in Binary
r=f.read()
print(r)

print()

f=open("IO Basics.txt","rt") # Reading as Text
r=f.read()
print(r)

print()

f=open("IO Basics.txt","rb") # Reading in Binary only 4 characters
r=f.read(4)
print(r)

f.close() #Closes the Opened File

print()
print("Using For Loop")
f=open("IO Basics.txt") # Another Way of Printing Content in File
#r=f.read()
#print(r)
for line in f:
    print(line)

f.close()

print()
f=open("IO Basics.txt","rb") # Reading in Binary using Readline Function
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print()
f=open("IO Basics.txt") # Reading lines in Form Of List
print(f.readlines())
f.close()