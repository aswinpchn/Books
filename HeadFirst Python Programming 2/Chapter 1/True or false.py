# Every object in Python has a truth value associated with it, in that the object evaluates to either
# 'True or False'. 'True', 'False' is the way how T/F is stored in python.

# Something is False if it evaluates to 0, the value None, an empty string,
# or an empty built-in data structure. This means all of these examples are False:

print(bool(0), bool(0.0), bool(''), bool([]), bool({}), bool(None))  # All of the equate to False.

print(bool(1), bool(-1), True)  # All of these equate to True.
