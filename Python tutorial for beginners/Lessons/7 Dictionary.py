import collections

# Dictionary is like hashmap

dic = {1: 4, 2: 5, 3: 'asw'}

print(dic[3])  # Error message if a key is not present.
print(dic.get(3))  # Another way to get.
print(dic.get(10, 'not found'))  # In get method, there is second parameter, returned when key not found.

del dic[1]  # This deletes the item with key 1.
print(dic)

for key in dic:  # Print keys in a dictionary.
    print(key)

for item in dic.items():  # Print key value pair in a dictionary each as a tuple.
    print(item)

dic.clear()  # clears entire dictionary.
dic.keys()  # Gives all the keys as a set.
dic.values()  # Gives all the values as a list.

arr = [1, 1, 2, 2, 4, 5]
print(collections.Counter(arr))  # Counter({1: 2, 2: 2, 4: 1, 5: 1})
print(dict(collections.Counter(arr)))  # {1: 2, 2: 2, 4: 1, 5: 1}

# Tricky thing. To create an empty set.(Anomaly)
sey = {}
print(type(sey))  # This would produce a dictionary rather than a set. To create an empty set
ss = set()  # This is how you can create an empty set.
print(type(ss))

# Keys and Values sorted in alphabetical order by the key.
key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
for i in sorted(key_value):
    print((i, key_value[i]), end=" ")  # (1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18)

# Sort based on value
print(' ')
for i in sorted(key_value, key=key_value.get):  # for sorted, we are giving a parameter key, which is the value.
    print((i, key_value[i]), end=" ")  # (1, 2) (5, 12) (6, 18) (4, 24) (2, 56) (3, 323)
