# String in python is of category, sequence. (Similar to list, tuple, etc.)
# A character in Python is actually a single length String.
# String in Python is immutable. Meaning, if you modify a string, a new string is created somewhere in the memory.


s = 'aswin'
print(s)
print(s[0])  # You can access a character by using index.
print(s[-1])  # Using negative indexes, you can access from the last. ('n')
print(s[0:3])  # You can use indexes like you use in range.

# Built-in functions to Work with Python
print(len(s))  # 5
print(list(enumerate(s)))  # Returns a list of tuple of the index and value of all the items in the string. This can
# be useful for iteration. [(index, item), ]
print(str(49.2))  # Virtually any object in Python can be rendered as a string. ('49.2')
print(ord('a'))  # Takes a single length string and returns the ascii value. (97)
print(chr(97))  # Opposite of ord method.
print(bin(100))  # Returns binary equivalent string of given integer. ('0b1100100')

# Common Python String methods.
print(s.lower())  # Returns lower cased string.
print('Aswin is a good boy.'.split(' '))  # Splits string based on the delimiting character and returns as list.
# There are more method like find(), replace()
print('ooo'.count('oo'))  # returns the number of non-overlapping occurrences of substring in a given string. (1)
print(bin(3).count('1'))  # Return 2.
print(s.find('as'))  # Returns the lowest index if the substring is found in the given string. -1 if not found. (0)
print(s.replace('as', 'dash'))  # Replaces occurrences of a substring within a string.

# Operators with String. ( + , *, in)
print('as' + 'win')  # Creates a new string by concatenating.
print('as' * 3)  # Created concatenated copies. (asasas)
print('as' in 'aswin')  # True  [Not in also available].

# Converting Between Strings and Lists
print(''.join(['as', 'win', ' ','prasad']))  # 'aswin prasad'
# s.join(<iterable>) returns the string that results from concatenating the objects in <iterable> separated by s.

print(list('aswin'))  # Returns a list of characters from a String. ['a', 's', 'w', 'i', 'n']



