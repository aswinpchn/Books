# Lists, dictionaries, and sets (being mutable) are always passed into a function by reference—
# any changes made to the variable’s data structure within the function’s suite are reflected in
# the calling code. The data is mutable, after all.

# Strings, integers, and tuples (being immutable) are always passed into a function by value—
# any changes to the variable within the function are private to the function and are not
# reflected in the calling code. As the data is immutable, it cannot change.

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


num = 10
double(num)
# Before: 10
# After: 20
print(num)  # 10. This straightforward, integer is passed by value.

saying = 'Hello '
double(saying)
# Before: Hello
# After: Hello Hello
print(saying)  # 'Hello '. This straightforward, string is passed by value. (Remember that in java string is by referen)

numbers = [42, 256, 16]
double(numbers)
# Before: [42, 256, 16]
# After: [42, 256, 16, 42, 256, 16]
print(numbers)  # [42, 256, 16]. You would think that as list is passed by reference, list changes would be retained, but they are not. Here is the reason below.
# Executing the code arg*2 creates a new value, which is assigned a new object reference, which is then assigned to the
# arg variable, overwriting the previous object reference stored in arg in the function’s suite. However, the “old”
# object reference still exists in the calling code and its value has’t changed. so the shell sees the original list,
# not the new doubled list created in Tom’s code.

numbers = [42, 256, 16]
change(numbers)
# Before: [42, 256, 16]
# After: [42, 256, 16, 'More data']
print(numbers)  # [42, 256, 16, 'More data']. This is straightforward, as list is passed, its pass by reference.
