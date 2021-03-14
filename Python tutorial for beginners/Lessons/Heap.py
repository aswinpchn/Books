# Heap concept in Python can be got using Heapq
import heapq

nums = [1, 2, 3, 4]
li = []
for num in nums:
    heapq.heappush(li, num)
    if len(li) > 2:
        heapq.heappop(li)
print(li)  # list will contain the 2 biggest elements. This is min heap
# To get the max heap, the only way in python is to negate the elements when entering.
