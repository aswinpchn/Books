# This is try catch equivalent in Python

try:
    print([1, 2, 3].index(0))  # This will throw ValueError as 0 is not present in the list.
except ValueError:
    print('Not found')
