class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


    # TODO: надо улучшить; это не о чем
    def __repr__(self):
        return str('Node({0})'.format(self.node))


    def __str__(self):
        return str(self.data)


    def insert(self, data):
        if self.data == data:
            raise Exception("A BTS cannot contain duplicate data")

        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        elif data > self.data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True


    def minValueNode(self):
        pass


    def maxValueNode(self):
        pass


    def delete(self, data, root):
        pass


    def find(self, data):
        pass


    def preorder(self):
        pass


    def inorder(self):
        pass


    def postorder(self):
        pass

class Tree:
    '''
        TODO: можно сразу передать данные в списке
        и сформулировать сбаларсированное дерево
    '''
    def __init__(self):
        self.head = None


