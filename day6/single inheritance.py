class Person:
    def __init__(self,name,age,gender):
        print("Person class object is created")
        self.name=name
        self.age=age
        self.gender=gender
class Student(Person):
    def __init__(self,name,age,gender,id,branch):
        super().__init__(name,age,gender)
        self.id=id
        self.branch=branch
        print("Student class object is created")
S1=Student(1,2,3,4,5)


