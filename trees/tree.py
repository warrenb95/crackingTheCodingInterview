from node import Node
from collections import deque

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

    def binSearch(self, node, value):        
        if node == None:
            return False
        
        if node.data == value:
            return True
        
        if value < node.data:
            return self.binSearch(node.left, value)
        else:
            return self.binSearch(node.right, value)

        return False

    def dfs(self, value):
        return self.dfsUtil(value, self.root, [])

    def dfsUtil(self, value, node, visited):
        if node == None:
            return
             
        if node.data == value:
            return True
        
        if node.left != None and node.left.data not in visited :
            visited.append(node.left.data)
            return self.dfsUtil(value, node.left, visited)
        
        if node.right != None and node.right.data not in visited:
            visited.append(node.right.data)
            return self.dfsUtil(value, node.right, visited)

    def bfs(self, value):
        queue = deque()
        visited = []

        visited.append(self.root.data)
        queue.append(self.root)
        
        while len(queue) > 0:
            node = queue.pop()
            if node.data == value:
                return True

            print(node.data)
            
            if node.left != None and node.left.data not in visited:
                visited.append(node.left.data)
                queue.append(node.left)
            if node.right != None and node.right.data not in visited:
                visited.append(node.right.data)
                queue.append(node.right)

        return False


t = Tree(Node(5))

for i in range(10):
    node = Node(i)
    t.add(node)

t.printInOrder()
# print('-------------------------')
# t.printPreOrder()
# print('-------------------------')
# t.printPostOrder()

print('-------------------------')
print(t.bfs(8))
