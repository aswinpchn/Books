lis = [1, 2, 3]

listing = [1, 2, 'asw', 4]  # A list can have different types of content.

print(listing[0:3])  # Slicing can be done.

lis.remove(1)  # Remove the given value
lis.pop(0)  # Remove the value at given index

del listing[2:]  # del can be used to delete multiple values.
print(listing)

print(max([1, 2, 3]))
print(sum([1, 2, 3]))


# * operator makes a shallow copy of the sequence.
# Note: If the content being multiplied is nested. Results will be weird
# https://stackoverflow.com/questions/29306418/python-operator-creating-list-with-default-value
l1 = [0] * 4
l1[0] = 5
print(l1)  # [5, 0, 0, 0]

l2 = [[None]] * 4
l2[0].append(5)
print(l2)  # [[None, 5], [None, 5], [None, 5], [None, 5]] Same list is being reference at all times.
