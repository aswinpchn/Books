import functools


def is_even(x):
    return x % 2 == 0  # if x is 1, return False. if x is 2, returns True.


lis = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, lis))
# filter(function_name, iterable). filter returns iterator, so surround by list.
# filter, filters items that are true for the given condition.

# If you see here, the use of the function is only here. So we can use lambda in this case to make code elegant.
evens = list(filter(lambda x: x % 2 == 0, lis))  # each element in 'lis' is taken as x one by one.
print(evens)  # [2, 4, 6]


# -----------------------


def update(x):
    return x + 2


lis = [1, 2, 3, 4, 5, 6]
updated_list = list(map(update, lis))
# map(function_name, iterable). Map returns iterator, so surround by list.
# Map, takes an iterable, computes with given function and give an updated list.

updated_list = list(map(lambda x: x + 2, lis))
print(updated_list)  # [3, 4, 5, 6, 7, 8]


# ------------------------


def reduc(x, y):
    return x + y


lis = [1, 2, 3, 4, 5, 6]
reduced_value = functools.reduce(reduc, lis)
# functools.reduce(function_name, iterable). Returns a single value.
# Reduce takes an iterable, runs with given function and gives a value.

reduced_value = functools.reduce(lambda x, y: x + y, lis)
print(reduced_value)
