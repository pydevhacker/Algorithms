
'''

'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def search(node, key):
    if node is None:
        return

    if node.key == key:
        return node
    if node.key < key:
        return search(node.right, key)

    return search(node.left, key)


def insert(node, key):
    if node is None:
        node = Node(key)
        return node
    if node.key < key:
        node.left = insert(node.left, key)
    elif node.key > key:
        node.right = insert(node.right, key)

    return node


def delete(node, key):
    if node is None:
        return

    node = search(node, key)

    # if node is leaf node
    if node.left is None and node.right is None:
        node = None

    # if node has left child
    if node.left is not None and node.right is None:
        node.key = node.left.key
        node.left = None

    #if node has only right child
    if node.left is None and node.right is not None:
        node.key = node.right.key
        node.right = None

    #if node has both the childs
    if node.left is not None and node.right is not None:
        #find min in right sub tree ie find sucessor
        temp = node.right
        while temp.left:
            temp = temp.left
        node.key = temp.key
        temp = None


def minValue(node):
    if node is None:
        return
    temp = node
    while temp.left:
        temp = temp.left
    return temp

def maxValue(node):
    if node is None:
        return
    temp = node
    while temp.right:
        temp = temp.right
    return temp


def findPreSuc(node, key):
    if node is None:
        return
    pred = None
    suc = None
    if node.key == key:
        if node.left is not None:
            #find predecessor
            pred = maxValue(node.left)
        if node.right is not None:
            #find successor
            suc = minValue(node.right)
        return (pred, suc)
    if node.key < key:
        pred = node
        findPreSuc(node.right, key)
    else:
        suc = node
        findPreSuc(node.left, key)
    return (pred, suc)

'''
to check if the tree is bst or not
we can check using two variables min and max and compare if the left subtree min and max is smaller than root and same for right subtree
'''
def isBST(node, min, max):
    if node is None:
        return
    if node.key < min and node.key > max:
        return False
    return isBST(node.left, min, node.key-1) and isBST(node.right, node.key+1, max)


'''
lowest common ansiter lca
'''

def lca(node, n1, n2):
    if node is None:
        return

    if node.key > n1 and node.key > n2:
        return lca(node.left, n1, n2)

    if node.key < n1 and node.key < n2:
        return lca(node.right, n1, n2)

    return node


def successor(root, node):
    if node.right is not None:
        suc = minValue(node.right)
        return suc
    suc = None
    while root:
        if node.data < root:
            suc = root
            root = root.left
        elif node.data > root:
            root = root.right
        else:
            break

    return suc


def kSmallestElement(node, k):
    stack = []
    crawl = node
    while crawl:
        stack.append(crawl)
        crawl = crawl.left

    while stack:
        crawl = stack.pop()
        k = k-1
        if k == 0:
            break
        else:
            if crawl.right:
                temp = crawl.right
                while temp:
                    stack.append(temp)
                    temp = temp.left

    return crawl