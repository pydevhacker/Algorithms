'''
max distance from one node to another node
'''

from Tree.TreeNode import TreeNode


def diameter(root):
    if root is None:
        return tuple((0,0))
    ldia = diameter(root.left)
    rdia = diameter(root.right)

    h = 1 + max(ldia[0], rdia[0])
    d = ldia[0] + rdia[0] + 1
    dia = max(d, max(ldia[1], rdia[1]))

    return tuple((h, dia))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))
