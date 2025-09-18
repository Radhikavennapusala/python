# Person Class
class Person:
    def __init__(self, name, age, gender, contact_number, nationality, aadhar_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.nationality = nationality
        self.aadhar_number = aadhar_number

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
              f"Contact: {self.contact_number}, Nationality: {self.nationality}, "
              f"Aadhar: {self.aadhar_number}")

# Creating 5 person objects
person1 = Person("Rahul", 25, "Male", "9876543210", "Indian", "1234-5678-9012")
person2 = Person("Priya", 30, "Female", "9876501234", "Indian", "2345-6789-0123")
person3 = Person("Amit", 28, "Male", "9876512345", "Indian", "3456-7890-1234")
person4 = Person("Sneha", 22, "Female", "9876523456", "Indian", "4567-8901-2345")
person5 = Person("Rohit", 35, "Male", "9876534567", "Indian", "5678-9012-3456")

# Accessing person data
print("---- Person Data ----")
person1.display()
person2.display()
person3.display()
person4.display()
person5.display()
