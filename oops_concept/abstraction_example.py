# Abstraction 
# ?? --> Simple interface and reduce the impact of change...

class MyClass():
    # this
    # constructor --> __init__
    def __init__(self,a,b):
        self.__a = a # private attributes
        self.__b = b
    
    def mul(self):
        print(self.__a * self.__b)
        pass

obj = MyClass(2,4)

# print(obj.__a)

obj.mul()