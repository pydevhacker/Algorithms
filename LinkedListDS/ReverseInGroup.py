'''
Reverse a Linked List in groups of given size

'''


from LinkedListDS.LinkedList import LinkedList
from LinkedListDS.LinkedListUtil import printNode

def reverse(node, k):

    prev = None
    cur = node
    count = 0
    next = None

    while cur is not None and count < k:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        count += 1

    if next is not None:
        node.next = reverse(next, k)

    return prev

def test():
    lst = LinkedList()
    lst.push(9)
    lst.push(8)
    lst.push(7)
    lst.push(6)
    lst.push(5)
    lst.push(4)
    lst.push(3)
    lst.push(2)
    lst.push(1)
    lst.print_list()
    head = reverse(lst.head, 3)
    printNode(head)

if __name__ == '__main__':
    test()