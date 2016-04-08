'''
check if binary tree is subtree of another binary tree
tree1 big tree and tree2 subtree
start from root of both tree1 and tree2
if root are not equal traverse tree1 to find the subtree whose root if equal to tree2 root
if found traverse both tree and check if both are identical

or do inorder traversal of both the tree and see if first array contains element of second element
'''



def areIdentical(root1, root2):
    if root1 is None or root2 is None:
        return False

    if root1.key == root2.key and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right):
        return True

def isSubtree(T, S):
    if T is None or S is None:
        return False

    if areIdentical(T, S): return True

    return isSubtree(T.left, S) or isSubtree(T.right, S)

