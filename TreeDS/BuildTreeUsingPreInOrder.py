'''
Construct Tree from given Inorder and Preorder traversals
http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
'''


from Tree.TreeNode import TreeNode as node

preOrderIdx = 0

def search(a, start, end, key):
    for i in range(start, end+1):
        if a[i] == key:
            return i

def inOrderTraversal(n):
    if n is None: return
    inOrderTraversal(n.left)
    print(n.key, end=" ")
    inOrderTraversal(n.right)

def buildTree(preOrder, inOrder, start, end):
    global preOrderIdx

    if start > end: return None

    n = node(preOrder[preOrderIdx])
    preOrderIdx += 1

    if start == end: return n

    inOrderIdx = search(inOrder, start, end , n.key)

    n.left = buildTree(preOrder, inOrder, start, inOrderIdx-1)
    n.right = buildTree(preOrder, inOrder, inOrderIdx+1, end)
    return n


def test():
    global preOrderIdx
    preOrderIdx = 0
    inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    root = buildTree(preOrder, inOrder, 0, len(inOrder) - 1)
    inOrderTraversal(root)

if __name__ == '__main__':
    test()


