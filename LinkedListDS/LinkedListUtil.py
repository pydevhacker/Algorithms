

def printNode(node):
    print("Printing List : ", end = " ")
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print('\n')
