##### OBJECT-ORIENTED PROGRAMMING #####
# You work with objects.
# EX: entity: Student, primary key: ID, secondary keys: name, grade.

# Products: ID, name, price, Customers is the E.R.D.
# All together, they are called a class.

# Class: A template for an entity. Any copies created off of it are known as an object.
# Object: Copy created off of the template.
# Entity: Something of interest which has properties and methods. EX: Study is a method for students entity.

class Student: # Student is the name of the class.
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name}.{last_name}@gmail.com'
        self.score = score

    # Called as a method because it is defined inside a class
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

student1 = Student("Joe", "Doe",85)
student2 = Student("Dr", "Phil",78)
print(student1.email)
print(student2.email)

print(student1.fullname())
print(student2.fullname())
# The period shows everything attached to student1.

"""
student1 = Student()
student1.first_name = 'Joe'
student1.last_name = 'Doe'
student1.email = 'Joe.Doe@gmail.com'
student1.score = 85

student2 = Student()
student2.first_name = 'Dr'
student2.last_name = 'Phil'
student2.email = 'Dr.Phil@gmail.com'
student2.score = 78

print(student1) # Prints __main__.Student object
print(student2) # Prints __main__.Student object
"""
