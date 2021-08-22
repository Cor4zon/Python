class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class MyLinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next


    def __repr__(self):
        if self.head is None:
            return 'None'

        nodes = []
        for elem in self:
            nodes.append(str(elem))

        nodes.append('None')
        return ' -> '.join(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def addAtTail(self, data):
        if self.head is None:
            return self.addAtHead(data)

        for elem in self:
            pass
        elem.next = Node(data)


    def addAtHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node



    def remove_node(self, target_data):
        if self.head is None:
            raise Exception("List is empty")

        prev_node = self.head
        for elem in self:
            if elem.data == target_data:
                prev_node.next = elem.next
                return
            prev_node = elem

        raise Exception("No data '%s' in list" % target_data)

    # TODO: оптимизировать
    def get(self, index):
        if self.head is None:
            return -1

        node = self.head
        i = 0
        while node and i < index:
            node = node.next
            i += 1


        if i == index and node is not None:
            return node.data
        return -1


    #TODO: можно без prev_node
    def addAtIndex(self, index, data):
        if index == 0:
            return self.addAtHead(data)


        i = 0
        prev_node = self.head
        for elem in self:
            if i == index:
                break
            i += 1
            prev_node = elem


        if i == index:
            node = Node(data)
            node.next = prev_node.next
            prev_node.next = node
            return

        return -1

    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return

        i = 0
        prev_node = self.head
        for elem in self:
            if i == index:
                break
            i += 1
            prev_node = elem

        if i == index:
            prev_node.next = elem.next
            elem = prev_node
            return
        return -1





llist = MyLinkedList()


llist.addAtHead(1)
llist.addAtHead(2)
llist.addAtHead(3)
llist.addAtHead(4)
llist.addAtHead(5)
# print(llist.get(0))
print(llist.get(5))
# print(llist.get(5))
print(llist)