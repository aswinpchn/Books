# Iterable is something that can be iterated over. Generally it's iterated using the 'for' construct.
# Familiar examples of iterables are lists, tuples, and strings - any such sequence can be iterated over in a for-loop.
# We will also encounter important non-sequential collections, like dictionaries and sets; these are iterables as well.

# https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html#:~:text=Definition%3A,over%20in%20a%20for%2Dloop.
# Functions that act on iterables
# Here are some useful built-in functions that accept iterables as arguments:
#
# list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
#
# sum: sum the contents of an iterable.
#
# sorted: return a list of the sorted contents of an iterable
#
# any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable.
#
# all: returns True only if bool(item) was True for all items in the iterable.
#
# max: return the largest value in an iterable.
#
# min: return the smallest value in an iterable.


# Examples
# >>> list("I am a cow")
# ['I', ' ', 'a', 'm', ' ', 'a', ' ', 'c', 'o', 'w']
#
# >>> sum([1, 2, 3])
# 6
#
# >>> sorted("gheliabciou")
# ['a', 'b', 'c', 'e', 'g', 'h', 'i', 'i', 'l', 'o', 'u']
#
# # `bool(item)` evaluates to `False` for each of these items
# >>> any((0, None, [], 0))
# False
#
# # `bool(item)` evaluates to  `True` for each of these items
# >>> all([1, (0, 1), True, "hi"])
# True
#
# >>> max((5, 8, 9, 0))
# 9
#
# >>> min("hello")
# 'e'