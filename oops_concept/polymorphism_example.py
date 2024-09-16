# # Poly --> Many
# # morph - form 

class Bird:

    def intro(self):
        print("birds")
    
    def flight(self):
        print("most birds fly")

class sparrow(Bird): # Inheritance

    def intro(self):
        print("Sparrow")

class penguin(Bird):

    def intro(self):
        print("Penguin")

    def flight(self):
        print("I cannot fly, But I can swim")


sp = sparrow()

sp.intro()

sp.flight()

pe = penguin()

pe.flight()

