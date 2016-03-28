'''
Detect and Remove Loop in a Linked List

'''

from LinkedListDS.LinkedList import LinkedList
from LinkedListDS.LinkedListUtil import printNode


def removeLoop(loop_node, head):
    ptr1 = head
    while True:
        ptr2 = loop_node
        while ptr2.next.data != loop_node.data and ptr2.next.data != ptr1.data:
            ptr2 = ptr2.next

        if ptr2.next.data == ptr1.data:
            break

        ptr1 = ptr1.next

    ptr2.next = None

def detectAndRemove(head):
    slow = fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow.data == fast.data:
            print('Loop detected')
            removeLoop(slow, head)
            return 1

    #No loop found
    return 0


def test():
    lst = LinkedList()
    lst.push(10)
    lst.push(4)
    lst.push(15)
    lst.push(20)
    lst.push(50)

    #create a loop
    lst.head.next.next.next.next.next = lst.head.next.next

    detectAndRemove(lst.head)
    printNode(lst.head)

if __name__ == '__main__':
    test()
