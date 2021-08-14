
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        curNode = self.head
        curIndex = 0
        while curIndex <= index:
            if curIndex == index:
                return curNode.val
            curIndex += 1
            curNode = curNode.next

        return -1

    def addAtHead(self, val: int) -> None:
        head = self.head
        newRot = Node(val)
        newRot.next = head
        self.head = newRot


    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return

        root = self.head
        while root.next:
            root = root.next
        root.next = Node(val)


    def addAtIndex(self, index: int, val: int) -> None:
        head = self.head
        newNode = Node(val)
        while index > 0:
            head = head.next
            index -= 1
        newNode.next = head.next
        head = newNode



    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return -1

        curIndex = 0
        head = self.head

        while head:
            if curIndex == index:
                break
            lastNode = head
            head = head.next

        lastNode.next = head
        head = None


    def showLinkedList(self):
        head = self.head
        while head:
            print(head.val)
            head = head.next



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

print(obj)
obj.addAtTail(11)
obj.addAtTail(21)
obj.addAtTail(13)
obj.addAtTail(1342)
obj.addAtTail(1333)
param_1 = obj.get(3)

obj.showLinkedList()
print()
print()
print()
obj.addAtIndex(3, 666)

obj.showLinkedList()


# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)