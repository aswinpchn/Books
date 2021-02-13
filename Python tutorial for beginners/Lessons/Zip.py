# https://realpython.com/python-zip-function/
# Zip function in python is used to aggregate items iterables.
# Using Zip on Zero or One iterables is pointless. It is primarily used to aggregate more than 2 iterables.
# Zip works best of ordered collections like List, tuple. As in Unordered sets(Set, dict), the order will not be fixed.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(zip(list1, list2))  # This just prints address of Zip and not any contents.
print(list(zip(list1, list2)))  # [(1, 4), (2, 5), (3, 6)] List of tuple is returned.
print(dict(zip(list1, list2)))  # {1: 4, 2: 5, 3: 6} Using this we can create a dictionary from two lists.
