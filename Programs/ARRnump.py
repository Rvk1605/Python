import numpy
roll=numpy.array([100,101,102,103],dtype=float)
print("Datatype = ", roll.dtype)
print(roll)
#UNicode or Characters
gender=numpy.array(['Female','male','transgender'])
print("Datatype = ",gender.dtype)
print(gender)
#Using Line SPace
marks=numpy.linspace(30,95,5)
print(marks)
#Using Loop
n=len(marks)
for elements in gender:
    print(elements)
#using While Loop
i=0
while i<n:
    print(marks[i])
    i+=1