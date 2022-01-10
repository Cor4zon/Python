# great default choice
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()


q = Queue()

q.push(1)
q.push(2)
q.push(3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())