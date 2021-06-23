from collections import deque

# from queue import Queue  # This is another way to implement Queue in Python.
# https://www.geeksforgeeks.org/queue-in-python/

# Double ended queue can be used to implement both Queue and stack
q = deque()  # When inserting, it just goes in the order as you put.
q.append(1)
q.append(2)
q.append(3)
print(q)  # can be easily printed [1, 2, 3]
print(q.popleft())  # 1 is popped off. Which is the oldest, so this is a queue
print(q.pop()) # 3 is popped. Which is the newest. So this behaves as a stack.
