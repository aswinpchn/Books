# In Python, we don't have the concept of 'pass by value' or 'pass by reference'. Instead, we have immutable or
# mutable arguments passed to the function. If we pass immutable objects like integer or string to function and try
# to update their value, their original value will not be updated instead a new variable will be created with updated
# value at new memory address and the calling code only knows the original address.
# If we pass mutable objects like list or dictionary and try to update them,
# their original value will be updated at the same memory address itself.

# This concept is slightly new in Python.
# https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=37

def double(arg):  # Arg too will point to same memory location as num.
    print('Before: ', arg, id(arg))
    arg = arg * 2  # Now arg will point to some new memory location holding the new value.
    print('After: ', arg, id(arg))


def change(arg):
    print('Before: ', arg, id(arg))
    arg.append('More data')
    print('After: ', arg, id(arg))  # As list is only modified internally, address wont change.


def replaceList(arg):
    print('Before: ', arg, id(arg))
    arg = [1, 2, 3]
    print('After: ', arg, id(arg))


num = 10  # num will point to some memory.
print('Before: ', num, id(num))
double(num)
print('After: ', num, id(num))  # 10. Num is always pointing to this value only, so no change.
print('------------------------------------')

saying = 'Hello '
print('Before: ', saying, id(saying))
double(saying)
print('After: ', saying, id(saying))
print(saying)  # 'Hello '. Same logic as num.
print('------------------------------------')

numbers = [42, 256, 16]
print('Before: ', numbers, id(numbers))
replaceList(numbers)
print('After: ', numbers, id(numbers))
print(numbers)  # [42, 256, 16].
# New object reference is assigned to the arg variable when assigned
# overwriting the previous object reference stored in arg in the function’s call. However, the “old”
# object reference still exists in the calling code and the value in that address
# has’t changed. so python sees the original list, not the new list created in the function.

print('------------------------------------')

numbers = [42, 256, 16]  # List will point to some memory.
print('Before: ', numbers, id(numbers))
change(numbers)
print('After: ', numbers, id(numbers))
print(numbers)  # [42, 256, 16, 'More data'].
