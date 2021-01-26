#                                    Health Management System
# first Question Whether to Lock or Retrieve.
# 3 Clients- Harry,Rohan ,Raj
# 3 Files Food Lock and 3 Files Exercise Lock
# Write a Function that takes as input Client name
# than Ask For What to Lock/retrieve (Exercise  or Diet)
# A Message Has to be displayed of Successfull locking or retrievijng.
# than write the Exercise or Diet and Before this there should be date and time returned by this function
def getdate():
    import datetime
    return datetime.datetime.now()

# Write one more function to retrieve and Show data for our selection

def lock():
    print("1.Harry || 2.Rohan || 3.Raj")
    y = int(input("Chose Client 1,2 or 3:"))
    print("1.Exercise || 2.Diet")
    z = int(input("Choose Exercise 1 or 2:"))
    if z==1:
        a= input("Enter Exercise :")
        if y == 1:
            with open("EHarry.txt","a") as f:
                f.write(str(getdate()) + a +"\n")
                print("Succesfully Entered")
        elif y == 2:
            with open("ERohan.txt","a") as f:
                f.write(str(getdate()) + a +"\n")
                print("Succesfully Entered")
        else:
            with open("ERaj.txt","a") as f:
                f.write(str(getdate()) + a +"\n")
                print("Succesfully Entered")
    else:
        b= input("Enter Diet :")
        if y == 1:
            with open("DHarry.txt","a") as f:
                f.write(str(getdate()) + b +"\n")
                print("Succesfully Entered")
        elif y == 2:
            with open("DRohan.txt","a") as f:
                f.write(str(getdate()) + b +"\n")
                print("Succesfully Entered")
        else:
            with open("DRaj.txt","a") as f:
                f.write(str(getdate()) + b +"\n")
                print("Succesfully Entered")

def retrieve():
    print("1.Harry || 2.Rohan || 3.Raj")
    y = int(input("Choose Client 1,2 or 3:"))
    print("1.Exercise || 2.Diet")
    z = int(input("Choose Your Exercise 1 or 2:"))
    if z == 1:
        if y == 1:
            with open("EHarry.txt", "r") as f:
                print(f.read())
        elif y == 2:
            with open("ERohan.txt","r") as f:
                print(f.read())
        else :
            with open("ERaj.txt","r") as f:
                print(f.read())
    else:
        if y == 1:
            with open("DHarry.txt", "r") as f:
                print(f.read())
        elif y == 2:
            with open("DRohan.txt","r") as f:
                print(f.read())
        else :
            with open("DRaj.txt","r") as f:
                print(f.read())

print("1.LOCK || 2.RETRIEVE")
x = int(input("Choose Your Option 1 or 2:"))
if x==1:
    lock()
else:
    retrieve()
