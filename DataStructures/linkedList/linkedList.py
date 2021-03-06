
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is emplty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, targer_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == targer_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == targer_node_data:
                new_node.next = node
                prev_node.next = new_node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % targer_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            return Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


llist = LinkedList(['a', 'b', 'c'])
print(llist) # None

for elem in llist:
    print(elem)


# llist.add_first(Node('x'))
# llist.add_first(Node('y'))
#
# llist.add_last(Node('x'))
# llist.add_last(Node('x'))
# llist.add_last(Node('x'))
# print(llist)
#
#
# llist.add_before('c', Node('V'))
# print(llist)
#
#
# llist.remove_node('V')
# print(llist)