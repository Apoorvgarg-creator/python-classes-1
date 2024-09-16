# Inheritance

class Person(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name)
        print(self.id)
    
    def details(self):
        print("Name is {}".format(self.name))
        print("id is {}".format(self.id))


class Student(Person):

    def __init__(self, name, id, className, std):
        self.className = className
        self.std = std
        Person.__init__(self, name, id)
    
    def details(self):
        print("Name is {}".format(self.name))
        print("id is {}".format(self.id))
        print("className is {}".format(self.className))


kundana = Student("kundana", "1", "asd",8)

kundana.display()

kundana.details()