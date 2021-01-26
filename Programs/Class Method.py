class school:
    no_students=200

    def __init__(self,name,roll,sec):
        self.name=name
        self.roll=roll
        self.sec=sec
    def printdetails(self):
        print(f"Student Name = {self.name}\n"
              f"Roll No.= {self.roll}\n"
              f"Section = {self.sec}")

    @classmethod
    def change_studentsno(cls, number):
        cls.no_students=number

S1=school("Rajveer",1906351,"IT-5")
S2=school("Rahul",1906348,"IT-5")
S3=school("Divi",1906326,"IT-4")
print("S1 Details \n")
S1.printdetails()
print("\nS2 Details\n")
S2.printdetails()
print("\ns3 Details\n")
S3.printdetails()


#Class Method OPerations (Used To make Changes in Class Variables using Instance Varilbles)
# rohan=school()
#
# rohan.change_studentsno(500)
# print(school.no_students)
