lis = [1, 2, 3]

listing = [1, 2, 'asw', 4]  # A list can have different types of content.

print(listing[0:3])  # Slicing can be done.

lis.remove(1)  # Remove the given value
lis.pop(0)  # Remove the value at given index

del listing[2:]  # del can be used to delete multiple values.
print(listing)

print(max([1, 2, 3]))
print(sum([1, 2, 3]))