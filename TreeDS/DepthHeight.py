'''

'''

from Tree.TreeNode import TreeNode

def depth_height(root):
    if root is None:
        return 0

    ldepth = depth_height(root.left)
    rdepth = depth_height(root.right)

    depth = max(ldepth, rdepth)

    return depth + 1

def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(depth_height(root))

if __name__ == '__main__':
    test()
