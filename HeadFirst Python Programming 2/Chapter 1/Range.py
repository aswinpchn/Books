# The range type represents an immutable sequence of numbers. Range is of object type.
# 'range()' which is constructor of range, that returns sequence of numbers. 'range()' is a built in function.
# Typically used with for loop.

print(range(3))  # range(0, 3). This doesn't print actual numbers. To do it either convert to list or loop through.
print(type(range(3)))  # <class 'range'>

print(list(range(3)))  # [0, 1, 2]. Here we convert range to list, as range cannot be directly printed.

for i in range(3):  # This prints numbers.
    print(i)




