def disp():
    def show():
        return("Rajveer")
    print("My name Is")
    return show
ret=disp()
print(ret())
print("---------------------------------------------------------------------------")
#Defining functions Seperately
def disp():
    return("My Name Is "+show())
def show():
    return "Rajveer"
res=disp()
print(res)