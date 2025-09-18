class Student:
    def __init__(self,name,age,branch):
        self.StdName=name
        self.Age=age
        self.branch=branch
S1=Student("scott",20,"CSE")
print(f"Student name is:,{S1.StdName}")
print(f"Student age is:,{S1.Age}")
print(f"Student branch is:,{S1.branch}")
