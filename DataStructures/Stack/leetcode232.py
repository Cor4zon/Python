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
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        val = self.stack1.pop()
        while val:
            self.stack2.push(val)
            val = self.stack1.pop()

        self.stack1.push(x)
        val = self.stack2.pop()
        while val:
            self.stack1.push(val)
            val = self.stack2.pop()

    def pop(self) -> int:
        if self.empty():
            return None

        return self.stack1.pop()

        tempStack = Stack()
        while self.queue:
            tempStack.push(self.queue.pop())

        res = tempStack.pop()
        while tempStack:
            self.queue.push(tempStack.pop())

        return res

    def peek(self) -> int:
        val = self.stack1.pop()
        self.stack1.push(val)
        return val

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False