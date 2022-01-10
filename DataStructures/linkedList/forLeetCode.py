class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return self.data


class MyLinkedList:

    def __init__(self):
        self.head = None


    def __repr__(self):
        if self.head is None:
            return None

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def get(self, index: int) -> int:
        if index < 0:
            return -1

        node = self.head
        i = 0
        while i < index and node is not None:
            node = node.next
            i += 1

        if node is None:
            return -1

        return node.data

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node


    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return

        for node in self:
            node = node.next
        node.next = Node(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return -1

        node = self.head
        i = 0
        prev_node = node
        while i < index and node is not None:
            node = node.next
            prev_node = node
            i += 1

        if node is None:
            return -1

        newNode = Node(val)
        newNode.next = node
        prev_node.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return -1

        node = self.head
        prev_node = node
        i = 0
        while i < index and  node is not None:
            node = node.next
            prev_node = node

        if node is None:
            return -1

        prev_node.next = node.next


obj = MyLinkedList()
obj.addAtHead(10)
obj.addAtHead(20)
print(obj.get(0))
print(obj.get(10))
print(obj.get(1))
# obj.addAtTail(44)
print(obj)

for elem in obj:
    print(str(elem))

# print(obj)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
