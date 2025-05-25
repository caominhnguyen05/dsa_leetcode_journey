# Stacks

stack = []

# Append on top of stack - O(1)
stack.append(5)

stack.append(4)
stack.append(3)

print(stack)

# Pop from stack - O(1)
x = stack.pop()

print(x)
print(stack)

# Peek (see element on top of stack) - O(1)
print(stack[-1])

# Check if stack is not empty - O(1)
if stack:
    print(True)