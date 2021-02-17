# Every file in python is a module. So, it's easy creating modules in Python.

# So interpreter looks in some places for potential modules.
# 1. Working directory 2. Standard library location 3. Interpreter's site package location (Hard way).

# import Calc
# print(Calc.add(4, 5))  # If you just do 'import Calc'. You have to refer by Calc.add, Calc.sub etc.

from Calc import *
print(add(4, 5))  # Now as we have imported *, all the functions in Calc module can be accessed directly.

