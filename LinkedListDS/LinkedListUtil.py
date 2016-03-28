

def printNode(node):
    print("List : ", end = " ")
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print('\n')
