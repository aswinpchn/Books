# A list in Python is very similar to the notion of an array in other
# programming languages, in that you can think of a list as being an indexed
# collection of related objects, with each slot in the list numbered from zero
# upward.

# Unlike arrays in a lot of other programming languages, though, lists are
# dynamic in Python, in that they can grow (and shrink) on demand. There
# is no need to pre-declare the size of a list prior to using it to store any objects.

# Lists are also heterogeneous, in that you do not need to pre-declare the type
# of the object you’re storing—you can mix’n’match objects of different types
# in the one list if you like.

# Lists are mutable, in that you can change a list at any time by adding,
# removing, or changing objects.


letters = ['a', 'b', 'c', 'd']

print(letters[-1])
# as 0 is the starting index, -1 is the last index and -2 is last before and so on.

letters.remove('d')
# Removes the first occurrence of the value. Raises ValueError if the value is not present.

letters.pop(2)
# Removes the object at the given index. Raises IndexError if list is empty or index is out of range.

# Appends a single object to end of the list
letters.append('e')

letters.extend([])
# We already know that append appends a single object at end of the list.
# Extend appends a given list to end of another list.

letters.insert(1, [1, 2])
# We already know append and extend, but they add only at the end of the list.
# insert function inserts the object before given index
print(letters)  # ['a', [1, 2], 'b']
# Note that [1, 2] itself is considered as an object and inserted before index 1.

letters.copy()
# This returns shallow copy of the list. If you do equal to sign, only reference is assigned.

text = "Don't panic"
textList = list(text)  # text String is converted into a list.
print(textList)
print(textList[0:10:3])  # ['D', "'", 'p', 'i']     Every third letter up to (but not including) index location 10
print(letters[3:])  # Skip the first three letters, then give me everything else.
print(letters[:10])  # All letters up to (but not including) index location 10
print(letters[::2])  # Every second letter)
# This slicing behaviour is similar to what we seen before with range (Start, stop, step)
# Slicing a list is non-destructive.
