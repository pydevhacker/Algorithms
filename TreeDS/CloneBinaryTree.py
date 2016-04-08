'''

'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.random = None





def main():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    