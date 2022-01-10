# 225  Implement Stack using Queues


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stack = self.stack[::-1]

    def pop(self) -> int:
        if self.empty():
            return None
        return self.stack.pop()

    def top(self) -> int:
        if self.empty():
            return None
        return self.stack[len(self.stack) - 1]

    def empty(self) -> bool:
        if not len(self.stack):
            return True
        return False


obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()