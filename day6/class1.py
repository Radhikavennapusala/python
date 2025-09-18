class Student:
    def __init__(self,name,age,branch):
        self.Stdname=name
        self.age=age
        self.branch=branch
    def display(self):
        print(f"Student name is:{self.Student}")
        print(f"Student age is:{self.age}")
        print(f"Student branch is:{self.branch}")
S1=Student("scott",20,"CSE")
S1.display()
S2=Student("Hema",21,"CSD")
S2.display()

