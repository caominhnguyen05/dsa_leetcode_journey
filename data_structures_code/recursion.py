# # Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1: F(n) = F(n-1) + F(n-2)

# Time: O(2^n), Space: O(n)
def F(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return F(n-1) + F(n-2)

print(F(12))

# Linked Lists
class SinglyNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val)
  
head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

head.next = A
A.next = B
B.next = C

print(head)

# Time: O(n)
def reverse_print(node):
  if not node:
    return
  
  reverse_print(node.next)
  print(node)

reverse_print(head)

def reverse_linked_list(head):
  prev = None
  current = head

  while current:
    next_node = current.next # Store next node
    current.next = prev # Reverse the link
    prev = current # Move prev to current
    current = next_node # Move to next node
  return prev

# Reverse our linked list
reversed_head = reverse_linked_list(head)

# Print reversed list
current = reversed_head
while current:
  print(current.val, end=" -> " if current.next else "")
  current = current.next