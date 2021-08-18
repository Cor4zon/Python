# это ужасно медлено
class Queue:
    def __init__(self):
        self.queue = []

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def push(self, item):
        self.queue.append(item)


q = Queue()

q.push(1)
q.push(2)
q.push(3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())