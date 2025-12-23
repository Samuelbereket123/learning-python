"""
    COMMENT OUT ONE CODE TO CHECK EVERY CODES

Encapsulation is all about protecting your data.

We use __ to make the attribues private or let's say to make them in safe mode.

#######################################################################################################

So let's have a code of this in practical example => Line 25-32 -- YOU CAN COPY AND RUN THE CODE LOCALLY

How to make the code to read the code reads and execute that? We use the Get method
Line 41-50 will make sur that the attribute __age will also run.

To modify any of our attributes we can use the Set Method. Code line in 58-77.

So the Get and the Set Methods are just Python convention so we can use any word but those two are used for readiablity and shit.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Samuel", 20)
print(p1.name)
print(p1.__age)

####################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
p1 = Person("Samuel", 19)

print(p1.name) 
print(p1.__age)


####################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
p1 = Person("Samuel", 19)
print(p1.et_age())

#####################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 18:
            self.__age = age
        else:
            print("Age must be postive")


p1 = Person("Samuel", 19)
print(p1.get_age())

p1.set_age(20)
print(p1.get_age())
