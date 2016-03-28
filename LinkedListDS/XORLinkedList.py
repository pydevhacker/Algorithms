'''
Memory Efficient Doubly Linked List
based on bitwise XOR, do not store pointer to previous and next node
inplace of storing pointer to next and prev node it stores xor of prev and next node
Node = {data, xor}
for head node it will be {data, xor(null, next)} since prev of head is null
for travarsal do the xor with prev node
A -> b-> c -> d
for forward traversal do the xor(a, b.xor) that will give c, since b.xor = xor(a, c) and if we xor it again with a it will give c
for backward traversal do the xor(d, c.xor) that will give b, c.xor = xor(b, d) and we do xor it again with d it will give b
for each traversal we need prev visited node
'''



class Node:

    def __init__(self, data):
        self.data = data
        self.xorpointer = None

def insert(head, data):
    newNode = Node(data)
    newNode.xorpointer = None ^ head #xor of previous and next node

    if head is not None:
        next = head.xorpointer ^ None
        head.xorpointer = newNode ^ next

    return newNode

def printForward(head):
    cur = head
    prev = 0
    next = None
    while cur:
        next = prev ^ cur
        prev = cur
        cur = next


def test():
    head = Node(4)
    head.xorpointer = 0
    head = insert(head, 3)

    printForward(head)

if __name__ == '__main__':
    test()
