# Python has Object Oriented programming concepts like Other languages.
# Good intro to Classes in Python - https://www.geeksforgeeks.org/python-classes-and-objects/

# init is similar to constructor in Java
# https://www.geeksforgeeks.org/__init__-in-python/

# self represents the instance of the class. (Similar to this in Java) By using the “self” keyword we can access the
# *** attributes and methods *** of the class in python. It binds the attributes with the given arguments. Putting
# self as first parameter in every class method is mandatory. Because this is how the method can access the object
# variables. https://www.geeksforgeeks.org/self-in-python-class/

# We can have classes inside classes. This concept is called inner classes.
# https://www.geeksforgeeks.org/inner-class-in-python/

class Car:

    name = 'car'  # This is similar to static variable in Java. One variable across all objects.

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)

    def test1(self):
        self.show()  # To call another class method. Self has to be used.


audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()
ferrari.show()
print(Car.name)  # car
