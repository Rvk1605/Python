def avg(x,y):
    """This Function Works For Only Two Numbers and this is a Docstring.
    Is tells the Usability of Function Or Any Warnings in using Function"""
    avg=(x+y)/2
    print(avg)



a=int(input())
b=int(input())
avg(a,b)
print(avg.__doc__)  #This Is Syntax to see Docstring