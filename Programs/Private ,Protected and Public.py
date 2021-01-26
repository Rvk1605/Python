class Employee:
    Number_of_leaves = 18
    __years=4

    def __init__(self,empid,description,salary):
        self.empid=empid
        self.description=description
        self.salary=salary
    def printdetails(self):
        print(f"Employee id = {self.empid}\n"
              f"Description = {self.description}\n"
              f"Salary = {self.salary}\n"
              f"No. of leaves Allowed=  {self.Number_of_leaves}")
    @classmethod
    def change_leaves(cls,leaves):
        cls.Number_of_leaves=cls.Number_of_leaves-leaves
        print("Leaves Changed\n")

    @staticmethod
    def check_leaves(leaves):
        if leaves>18:
            print("Warning!! Leaves are Excessive\n")
        else:
            print("Leaves are Left")
            l=18-leaves
            print("Leaves = ",l)

E1=Employee(1906351,"Student",100000)
E1.printdetails()
E1.change_leaves(10)
E1.check_leaves(10)
print(E1.Number_of_leaves)
#private Acess By Name Mangling
print(E1._Employee__years)





