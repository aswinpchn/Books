from collections import deque

# from queue import LifoQueue  # This is another way to implement Queue in Python.
# https://www.geeksforgeeks.org/stack-in-python/

# Double ended queue can be used to implement both Queue and stack
s = deque()
s.append(1)
s.append(2)
s.append(3)
print(s)  # can be easily printed
print(s.pop())
