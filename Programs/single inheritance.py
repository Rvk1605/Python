class school:
    Leaves_allowed = 10

    def __init__(self, name, roll, section, contact):
        self.name = name
        self.roll = roll
        self.section = section
        self.contact = contact

    def printdetails(self):
        print(f"Students Name = {self.name}\n"
              f"Roll NO. = {self.roll}\n"
              f"Section = {self.section}\n"
              f"Contact No.= {self.contact}")

    @classmethod
    def change_leaves_allowed(cls, leaves):
        cls.Leaves_allowed = leaves




class Report(school):
     def __init__(self, maths, science, english, history, computer):
         self.maths = maths
         self.science = science
         self.english = english
         self.history = history
         self.computer = computer
     def print_marks(self):
         print(f"\nMaths = {self.maths}\n"
               f"Science = {self.science}\n"
               f"English = {self.english}\n"
               f"History = {self.history}\n"
               f"Computer = {self.computer}")

     @staticmethod
     def check_result(total, *marks):
         sum = 0
         for i in range(len(marks)):
             sum = sum + float(marks[i])
         percent = (sum / total) * 100
         if percent < 40:
             print(f"\nSorry Percentage = {percent:.2f}\n"
                   f"Result = Fail")
         elif percent > 90:
             print(f"\n    CONGRATULAIONS!!! Pecentage = {percent:.2f}\n"
                   f"         Result = PASS              ")
         else:
             print(f"\nPercentage = {percent:.2f}\n"
                   f" Result = Pass ")




s1=school("Rajveer",1906351,"B-19",9304121798)
s1.printdetails()
marks=list(map(float, input("Enter Marks :").split()))

s1=Report(5,99,80,89,90)
s1.print_marks()
s1.check_result(500,*marks)

