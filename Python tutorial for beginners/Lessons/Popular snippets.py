# Imports
from collections import defaultdict
import math

# Sorting in a list of list.
# https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

# [[1, 60], [1, 65], [2, 76], [2, 77], [1, 87], [1, 91], [1, 92], [2, 93], [2, 97], [1, 100], [2, 100]]  Sort by second.
print(sorted(items, key=lambda x: x[1]))

# [[1, 100], [2, 100], [2, 97], [2, 93], [1, 92], [1, 91], [1, 87], [2, 77], [2, 76], [1, 65], [1, 60]] Sort by second.
# Reversed.
print(sorted(items, key=lambda x: -x[1]))

# [[1, 100], [2, 100], [2, 97], [2, 93], [1, 92], [1, 91], [1, 87], [2, 77], [2, 76], [1, 65], [1, 60]] Sort by second.
# Reversed.
print(sorted(items, key=lambda x: x[1], reverse=True))

# [[1, 100], [1, 92], [1, 91], [1, 87], [1, 65], [1, 60], [2, 100], [2, 97], [2, 93], [2, 77], [2, 76]]
# Sort by first element and if two first element items are same, then by negative second element.
# Note: If you want to sort based on multiple keys it should be a tuple.
print(sorted(items, key=lambda x: (x[0], -x[1])))

# [[1, 60], [1, 65], [2, 76], [2, 77], [1, 87], [1, 91], [1, 92], [2, 93], [2, 97], [1, 100], [2, 100]]
# All the above ones create a new sorted list. The one below sorts in place.
items.sort(key=lambda x: x[1])
print(items)

#
#
# Integer to digits in a list
num = 555
li = list(map(int, str(num)))

# Replace function (Replace First '6' with '9')
# '669'.replace('6', '9', 1) - Using python.
s = '669'
for i in range(len(s)):
    if s[i] == '6':
        s = s[0:i] + '9' + s[i+1:len(s)]
        break
print(s)

#
#
# defaultdict means that if a key is not found in the dictionary when accessed, then instead of a KeyError being thrown,
# a new entry is created. The type of this new entry is given by the argument of defaultdict.
# https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work

d = defaultdict(list)  # In this default dict, it we access a key that is not there, an empty list created to that
# because we are sending list a parameter.
print(d[0])  # []  an empty list is being created even if the key is not in the dictionary.
d = defaultdict(int)  # Defaults to zero when key not found.
print(d[0])  # 0


# Sum of the digits of an integer
num = 57
sum_of_digits = sum(map(int, str(num)))  # A list is created with the digits, then summed up.
print(sum_of_digits)


# Check if two numbers are zero easily.
a, b = 0, 0
print(a == b == 0)  # True

# Reverse a word using slicing
word = 'aswin'
print(word[-1:-len(word)-1:-1])  # Start index: -1 End index: -6 Step: -1
print(word[::-1])  # This is the best solution as per stackoverflow. But I don't know how it's working
# https://stackoverflow.com/questions/931092/reverse-a-string-in-python
