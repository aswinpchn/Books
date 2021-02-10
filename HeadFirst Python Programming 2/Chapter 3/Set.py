# Sets also support 'sorted' function that returns the set elements in sorted order.
# We can use set like operations difference, intersection, and union.

d = {'a', 'e'}
print(type(d))  # <class 'set'>

s = {}
print(type(s))  # <class 'dict'>

s = set()  # Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
print(type(s))  # <class 'set'> To make a set without any elements, we use the set() function without any argument.
print(s)  # set(). You would have thought that this '{}' will be printed, but '{}' is empty dictionary. set() is
# empty dictionary.

string = 'aswin prasad'
se = set(string)  # Set constructor accepts an iterable and creates a set out of it.
print(se)  # {'a', 's', 'r', 'p', ' ', 'd', 'i', 'n', 'w'}

vowels = set('aeiou')
word = 'hello'
uni = vowels.union(set(word))  # union method works on a set and take another set as argument and finds union of them.
print(uni)
# Set also has other set methods like difference, intersection, etc.
