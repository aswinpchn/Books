from collections import deque

# from queue import Queue  # This is another way to implement Queue in Python.
# https://www.geeksforgeeks.org/queue-in-python/

# Double ended queue can be used to implement both Queue and stack
q = deque()  # When inserting, it just goes in the order as you put.
q.append(1)
q.append(2)
q.append(3)
print(q)  # can be easily printed
print(q.popleft())  # If you do just pop. It will behave as stack.
