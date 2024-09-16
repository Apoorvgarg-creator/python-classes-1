# x = 10

# print("Hello World")

# Procedural Paradigm -->
# salary = 1000
# overtime_rate = 0.2

# salary_employee_2 = 100000

# def return_salary():
#     return salary

# OOPs
# classes and Object

# Encapsulation --> Binding of attributes and methods in one single entity (called class)
class Employee():
    
    # this is the first function that will be called at the moment of initialization --> Constructor
    def __init__(self, salary):
        self.__salary = salary  # private attribute !!
        self.overtime_rate = 0.2

    def return_salary(self):
        return self.__salary
    

emp = Employee(2322434) # Making an Object of a Class

print(emp.return_salary())
print("*****")
# Python does not enforce strict private access
print(emp._Employee__salary)
