
from Tree.TreeNode import TreeNode


def in_order(root):
    if root:
        in_order(root.left)
        print(root.key),
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.key)


def pre_order(root):
    if root:
        print(root.key)
        pre_order(root.left)
        pre_order(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal")
in_order(root)

print("Post Traversal")
post_order(root)

print("Pre Traversal")
pre_order(root)