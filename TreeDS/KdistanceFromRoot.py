'''


'''


def kdist(node, k):
    if node is None:
        return

    if k == 0:
        print(node.key)
        return
    else:
        kdist(node.left, k-1)
        kdist(node.right, k-1)