'''
http://www.geeksforgeeks.org/convert-binary-tree-threaded-binary-tree/
The idea of threaded binary trees is to make inorder traversal faster and do it without stack and without recursion. A binary tree is made threaded by making all right child pointers that would normally be NULL point to the inorder successor of the node (if it exists).
There are two types of threaded binary trees.
Single Threaded: Where a NULL right pointers is made to point to the inorder successor (if successor exists)
Double Threaded: Where both left and right NULL pointers are made to point to inorder predecessor and inorder successor respectively. The predecessor threads are useful for reverse inorder traversal and postorder traversal.
The threads are also useful for fast accessing ancestors of a node.
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.threaded = False

#populate queue based on in order traversal
def populate_queue(root, q):
    if root is None:
        return
    if root.left is not None:
        populate_queue(root.left, q)
    q.append(root)
    if root.right is not None:
        populate_queue(root.right, q)

def create_threaded_util(root, queue):
    if root is None:
        return

    if root.left is not None:
        create_threaded_util(root.left, queue)

    queue.pop(0)

    if root.right is not None:
        create_threaded_util(root.right, queue)
    elif queue:
        root.right = queue[0]
        root.threaded = True


def left_most(node):
    while node is not None and node.left is not None:
        node = node.left
    return node


def in_order(node):
    if node is None:
        return

    cur = left_most(node)
    while cur is not None:
        print(cur.key, end=' ')
        if cur.threaded:
            cur = cur.right
        else:
            cur = left_most(cur.right)

def create_threaded(root):
    queue = []
    populate_queue(root, queue)
    create_threaded_util(root, queue)


def test():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    create_threaded(root)
    print("In Order Traversal of Threaded Binary Tree")
    in_order(root)


if __name__ == '__main__':
    test()

