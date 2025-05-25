# Queue

from collections import deque

queue = deque()

# Enqueue - Add element to the right - O(1)
queue.append(5)
queue.append(6)
queue.append(7)
print(queue)

# Dequeu (pop left) - Remove element from the left - O(1)
queue.popleft()
print(queue)

# Peek from left side - O(1)
print(queue[0])

# Peek from right side - O(1)
print(queue[-1])