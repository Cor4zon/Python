# amazon task
class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minVal = val

        if val < self.minVal:
            self.minVal = val
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None

        if len(self.stack) == 1:
            self.minVal = None

        if self.stack[-1] == self.minVal:
            self.minVal = self.stack[0]
            for i in range(len(self.stack) - 1):
                if self.stack[i] < self.minVal:
                    self.minVal = self.stack[i]

        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
