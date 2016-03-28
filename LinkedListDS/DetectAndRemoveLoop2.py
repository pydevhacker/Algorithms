'''
Detect and Remove Loop based on counting nodes
'''

from LinkedListDS.LinkedListUtil import printNode
from LinkedListDS.LinkedList import LinkedList


def removeLoop(loop_node, head):
    ptr1 = loop_node
    ptr2 = loop_node

    #count the number of nodes
    k = 1
    while(ptr1.next.data != ptr2.data):
        ptr1 = ptr1.next
        k += 1

    #Fix one pointer to head
    ptr1 = head
    #another pointer after k nodes from head
    ptr2 = head
    for i in range(k):
        ptr2 = ptr2.next

    while ptr2.data != ptr1.data:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    ptr2 = ptr2.next
    while ptr2.next.data != ptr1.data:
        ptr2 = ptr2.next

    ptr2.next = None


def detectAndRemove(head):
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow.data == fast.data:
            print("LOOP DETECTED")
            removeLoop(slow, head)
            return 1
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
