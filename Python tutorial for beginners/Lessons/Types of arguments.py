# See the 32. Functions for additional details.
# https://www.programiz.com/python-programming/function-argument

# Named arguments
def division(x, y):
    return x / y


print(division(y=5, x=10))  # This concept is called named arguments. We can change order of function calling arguments.

# Default arguments
# If an argument is given a value during declaration, it's called default value. It's optional during call.
# Any number of arguments in a function can have a default value. But once we have a default argument,
# all the arguments to its right must also have default values.
# Check programiz link for detailed info on python functions.


def function(name='Aswin'):  # Default value.
    print('Hello dude ' + name)


function()
function('Dog!')


# Variable length arguments. Denoted by *
# All extra calling arguments are put into a tuple. Which we can use later.

def sumi(a, *b):  # 1 goes into a, (2, 3, 4) goes as a tuple in b
    print(a, b)


sumi(1, 2, 3, 4)
