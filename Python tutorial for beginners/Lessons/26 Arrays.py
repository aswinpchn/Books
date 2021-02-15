# https://docs.python.org/3.9/library/array.html
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

# The arrays module in python is more like a thin wrapper over C arrays, it's not used on day to day usages. It's
# used when performance is very very important. It's not important to learn Array concept in Python.

# list
#     flexible
#     can be heterogeneous
# array
#     array of uniform values
#     homogeneous
#     compact (in size)
#     efficient (functionality and speed)
#     convenient

import array

arr = array.array('i', [1, 2, 0, -1])  # first parameter shows the type that the array can hold.
print(arr)

