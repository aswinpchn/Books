# id(object) is a function in python that returns identity of an object.

# It's important to note that everything in Python is an object, even numbers, and Classes.
# Hence, integer 5 has a unique id. The id of the integer 5 remains constant during the lifetime.

print(id(5))
a = 5
print(id(a))  # both print the same as, they both point to same 5. Remember that this is different from Addresses that
# you see in other languages, so at first this may seem wierd.
