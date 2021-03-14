# For loop is used to run over an sequence. We need not provide increment conditions.

data = [1, 2, 3, 'aswin']
for i in data:  # Every element in the sequence is run through.
    print(i)

for i in range(10):  # range() returns a sequence, range object.
    print(i)

# When you want to access both the index and the element at that index, we have to use
# Enumerate. It is the Python way to for loop.
# https://realpython.com/python-enumerate/
for index, value in enumerate(data):
    print(index, value)


# Note: If you want to be able to modify the loop variable in the loop (and have it affect subsequent iterations),
# you have to use a while loop:
# https://stackoverflow.com/questions/9450446/how-do-i-use-a-c-style-for-loop-in-python
