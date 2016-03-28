'''
Merge two sorted linked lists

'''

from LinkedList import LinkedList

def merge(a, b):
    if a is None: return b
    if b is None: return a

    if a.data <= b.data:
        result = a
        result.next = merge(a.next, b)
    else:
        result = b
        result.next = merge(a, b.next)
    return result

def printList(node):
    print("List : ", end = " ")
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print('\n')

def test():
    a = LinkedList()
    a.push(15)
    a.push(10)
    a.push(5)

    b = LinkedList()
    b.push(20)
    b.push(3)
    b.push(2)

    r = merge(a.head, b.head)
    printList(r)

if __name__ == '__main__':
    test()