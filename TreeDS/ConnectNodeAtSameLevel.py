'''

'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.nextRight = None


def connectUtil(node):
    if node is None:
        return

    if node.left is not None:
        node.left.nextRight = node.right

    if node.right is not None:
        if node.nextRight is not None:
            node.right.nextRight = node.nextRight.left
        else:
            node.right.nextRignt = None

def connect(node):
    if node is None:
        return

    node.nextRight = None
    conectUtil(node)


