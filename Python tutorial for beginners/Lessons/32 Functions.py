# Python is a dynamically typed language, so the concept of overloading simply does not apply to it.
# https://stackoverflow.com/questions/6434482/python-function-overloading
# https://www.programiz.com/python-programming/function-argument


def greet():
    print('Hi Aswin!')


def greeting(name):
    print('Hi ' + name)


def addition(x, y):
    return x + y


def multiply(x, y):  # Returning two things in the return function.
    return x * y, 'multiply'


greet()
greeting('Aswin!')
print(addition(5, 10))
product, placeholder = multiply(5, 10)
