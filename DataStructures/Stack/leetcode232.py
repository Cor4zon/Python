# 232. Implement Queue using Stacks
from collections import deque
class Stack:
    def __init__(self):
        self.stack = []

    def __iter__(self):
        for elem in self.stack:
            yield elem

    def __len__(self):
        counter = 0
        for elem in self.stack:
            counter += 1
        return counter

    def pop(self):
        if len(self.stack) == 0:
            print("Stack underflow")
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)


class MyQueue:

    def __init__(self):
        self.queue = Stack()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        if len(self.queue) == 0:
            print("Queue underflow")
            return None

        tempStack = Stack()
        while self.queue:
            tempStack.push(self.queue.pop())

        res = tempStack.pop()
        while tempStack:
            self.queue.push(tempStack.pop())

        return res

    def peek(self) -> int:
        if self.empty():
            print("Queue underflow")
            return None

        tempStack = Stack()
        while self.queue:
            tempStack.push(self.queue.pop())

        res = tempStack.pop()
        tempStack.push(res)

        while tempStack:
            self.queue.push(tempStack.pop())

        return res

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())

