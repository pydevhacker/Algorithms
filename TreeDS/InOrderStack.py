'''

'''

from Tree.TreeNode import TreeNode
def in_order(root):
    current = root
    stack = []
    done = 0

    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.key,)
                current = current.right
            else:
                done = 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
in_order(root)