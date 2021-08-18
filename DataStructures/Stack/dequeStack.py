from collections import deque
# deque - двухстороняя очередь

class Stack:
    def __init__(self):
        self.stack = deque()

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)


obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())