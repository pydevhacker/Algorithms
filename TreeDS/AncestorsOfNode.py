'''


'''



def ancestors(node, key):
    if node is None:
        return

    if node.key == key:
        return True

    if ancestors(node.left) or ancestors(node.right):
        print(node.key)
        return True
    return False