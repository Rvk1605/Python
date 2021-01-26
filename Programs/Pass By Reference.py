#Case 1
def val(lst):
    print("After Passing Befor Appending:",lst,id(lst))
    lst.append(4)
    print("After Passing After Appending:", lst, id(lst))

lst=[]
n=int(input("Enter No. Of Elements:"))
for i in range(n):
    x=int(input())
    lst.append(x)
print("Before Passing:",lst,id(lst))
val(lst)

#From This Result it Clear That list Is Mutable And Can Be Modified
# With New Object in it at same Address.


#Case 2
def val(lst):
    print("After Passing Befor Appending:",lst,id(lst))
    lst=[11,22,33]
    print("After Passing After Appending:", lst, id(lst))

lst=[]
n=int(input("Enter No. Of Elements:"))
for i in range(n):
    x=int(input())
    lst.append(x)
print("Before Passing:",lst,id(lst))
val(lst)
#In this case A new list is being created so lst identifier is tageed to new list with new Address
# and as it being Created in the Function It is not Accessible outside Function