# self represents the instance of the class.
# By using the “self” keyword we can access the *** attributes and methods *** of the class in python.
# It binds the attributes with the given arguments.
# Putting self as first parameter in every class method is mandatory.
# https://www.programiz.com/article/python-self-why
# https://www.geeksforgeeks.org/self-in-python-class/


class Car:

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
