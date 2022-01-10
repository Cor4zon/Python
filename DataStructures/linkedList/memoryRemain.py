class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(str(node.data))
            node = node.next
        return ' -> '.join(arr)

    def add_first(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node


    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        for elem in



    def add_between(self, data, position):
        pass

    def remove_data(self, data):
        pass

    def remove_at_pos(self, position):
        pass


lst = [1, 2, 3]
ll = LinkedList(lst)
print(ll)