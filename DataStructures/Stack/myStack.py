
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


myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(len(myStack))
for i in myStack:
    print(i, end=" ")
print()

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
myStack.pop()

