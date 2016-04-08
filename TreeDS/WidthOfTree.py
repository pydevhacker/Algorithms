'''
find width using pre order traversal
'''

def width(node, count, level):
    if node is None:
        return

    count[level] += 1
    width(node.left, count, level+1)
    width(node.right, count, level+1)


def height(node):
    if node is None:
        return
    return max(height(node.left), height(node.right)) + 1


def calc_width(node):
    if node is None:
        return

    h = height(node)
    count = [0] * (h+1)

    width(node, count, 0)

    print('Max Width : ', max(count))


