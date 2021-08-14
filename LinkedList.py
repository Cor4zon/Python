class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curIndex = 0
        head = self.head
        while curIndex < index and head:
            head = head.next
            curIndex += 1
        if head:
            return head.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.head = Node(val)
            return
        head = self.head
        while head.next:
            head = head.next
        head.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        curIndex = 0
        head = self.head

        while curIndex <= index and head:
            if curIndex == index:
                break
            lastNode = head
            head = head.next
            curIndex += 1

        if head:
            newNode = Node(val)
            newNode.next = head
            lastNode.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self.head
        if index == 0:
            self.head = head.next
            head = None
            return

        curIndex = 0
        head = self.head
        while curIndex < index and head:
            lastNode = head
            head = head.next
            curIndex += 1

        if head:
            lastNode.next = head.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
obj = MyLinkedList()

["MyLinkedList","addAtHead","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtTail","addAtTail","addAtIndex","deleteAtIndex","deleteAtIndex","addAtTail"]
[[],[0],[1,4],[8],[5],[4,3],[0],[5],[6,3],[7],[5],[4]]

obj.addAtHead(0)
obj.addAtIndex(1, 4)
# obj.deleteAtIndex(1)
