class Employee:
    def printdetails(self):
        print(f"Name = {self.name}\n"
              f"Roll no.= {self.roll}\n"
              f"Branch = {self.branch}\n"
              f"Year = {self.year}\n")

Raj=Employee()
Rahul=Employee()

Raj.name="Rajveer"
Raj.roll=1906351
Raj.branch="IT"
Raj.year="B-19"
Raj.printdetails()

