class Employee:
    def __init__(self,Empname,Empnum,Designation,Salary,Department):
        self.Empname=Empname
        self.Empnum=Empnum
        self.Designation=Designation
        self.Salary=Salary
        self.Department=Department
    def display(self):
        print(f"Employee name is:{self.Empname}")
        print(f"Employee number is:{self.Empnum}")
        print(f"Employee Designation is:{self.Designation}")
        print(f"Employee Salary is:{self.Salary}")
        print(f"Employee Department is:{self.Department}")
E1=Employee("Rama",228,"testing",50000,901)
E1.display()


