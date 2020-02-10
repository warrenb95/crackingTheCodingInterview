from node import Node

class Tree:
    
    def __init__(self, node):
        self.root = node

    def add(self, node, root = 0):
        if root == 0:
            root = self.root
        
        if node.data == root.data:
            return

        if node.data < root.data:
            if root.left == None:
                root.left = node
            else:
                self.add(node, root.left)
        else:
            if root.right == None:
                root.right = node
            else:
                self.add(node, root.right)

    def printInOrder(self, node = 0):
        if node == 0:
            node = self.root

        if node != None:
            self.printInOrder(node.left)
            print(node.data)
            self.printInOrder(node.right)

    def printPreOrder(self, node = 0):
        if node == 0:
            node = self.root

        if node != None:
            print(node.data)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self, node = 0):
        if node == 0:
            node = self.root

        if node != None:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.data)

t = Tree(Node(5))

for i in range(10):
    node = Node(i)
    t.add(node)

t.printInOrder()
print('-------------------------')
t.printPreOrder()
print('-------------------------')
t.printPostOrder()