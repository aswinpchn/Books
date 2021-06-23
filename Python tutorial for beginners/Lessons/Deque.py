from collections import deque

# deque is Double ended queue where you can add and remove from both ends efficiently.
# https://en.wikipedia.org/wiki/Double-ended_queue
# Here you can check the time complexity for deque operations. https://wiki.python.org/moin/TimeComplexity
# O(1) for append, appendleft, pop, and popleft.

d = deque()
d.append(1)  # Appends to the right
d.append(2)
d.append(3)
print(d)  # [1, 2, 3]
print(d.popleft())  # Removes oldest item, works like queue removal. 1
print(d.pop())  # Removes newest item, works like stack removal. 3
