'''
http://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

Print vertical order of given binary tree
'''

from Tree.TreeNode import TreeNode


def calc_vertical_distance(r, hd, m):
    if r is None:
        return
    m.setdefault(hd, [])
    m[hd].append(r.key)

    calc_vertical_distance(r.left, hd-1, m)
    calc_vertical_distance(r.right, hd+1, m)


def print_vertical_order(r):
    m = {}
    hd = 0
    calc_vertical_distance(r, hd, m)

    for k in sorted(m):
        print(m[k])


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)
print("Vertical order traversal is")
print_vertical_order(root)