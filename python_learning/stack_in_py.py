from collections import deque

from queue import LifoQueue

# stack using list - o(n)

# stack = []

# stack.append('x')
# stack.append('y')
# stack.append('z')

# print(stack)

# print(stack.pop())

# print(stack)



#  stack using Deque - o(1)

# stack = deque()
# stack.append("x")
# stack.append("y")
# stack.append("z")
# print(stack)

# print(stack.pop())
# print(stack)



#  stack using queue

stack = LifoQueue()

stack.put(2)
stack.put(3)
stack.put(4)

print(stack.qsize())
print(stack.full())

print(stack.get())