
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            print("Stack underflow")
            return None
        return self.stack.pop()


    def push(self, item):
        self.stack.append(item)


myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)

print(myStack.stack)

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
myStack.pop()