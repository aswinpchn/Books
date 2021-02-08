# a tuple is like a list that cannot be changed once it’s created (and populated with data). Tuples
# are immutable: they cannot change.

vowels = ('a', 'e', 'i', 'o', 'u')  # Brackets are the difference from set.
print(vowels)  # ('a', 'e', 'i', 'o', 'u').

t = ('python')
print(type(t))  # <class 'str'>. You though this parenthesis would have given a tuple, but it was a string!
# This has happened due to a syntactical quirk in the Python language. If you create a single object tuple, it will
# will be treated as a string. Just remember this rule, it is a anomaly in python interpreter itself.

s = ('python', )  # This is a way to create a single tuple python.
print(type(s))  # <class 'tuple'>
