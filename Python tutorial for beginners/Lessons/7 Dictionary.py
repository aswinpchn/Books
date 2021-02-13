
# Dictionary is like hashmap

dic = {1: 4, 2: 5, 3: 'asw'}

print(dic[3])  # Error message if a key is not present.
print(dic.get(3))  # Another way to get.
print(dic.get(10, 'not found'))  # In get method, there is second parameter, returned when key not found.

del dic[1]  # This deletes the item with key 1.
print(dic)

dic.clear()  # clears entire dictionary.
dic.keys()  # Gives all the keys as a set.
dic.values()  # Gives all the values as a list.

# Tricky thing. To create an empty set.(Anomaly)
sey = {}
print(type(sey))  # This would produce a dictionary rather than a set. To create an empty set
ss = set()  # This is how you can create an empty set.
print(type(ss))
