class Emp:
    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch = branch
    def printdetails(self):
        print(f"Name = {self.name}\n"
              f"Roll no.= {self.roll}\n"
              f"Branch = {self.branch}\n")
Raj=Emp("Rajveer",1906351,"B-19")
Raj.printdetails()