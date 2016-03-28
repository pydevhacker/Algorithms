'''
Swap nodes in a linked list without swapping data
http://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

swap node x and y without swapping data
#swap next pointer
temp = y.next
y.next = x.next
x.next = temp

#swap prev pointer
(y-1).next = x
(x-1).next = y


1. if x is head node
2. if y is head node
'''

from LinkedList import LinkedList

def swapNodes(head, x, y):
    #if nodes are None then nothing to do
    if x is None or y is None:
        return

    #Nothing to do
    if x == y:
        return

    prevX = None
    curX = head
    while curX is not None and curX.data != x:
        prevX = curX
        curX = curX.next

    prevY = None
    curY = head
    while curY != None and curY.data != y:
        prevY = curY
        curY = curY.next

    #Key not found
    if curX is None or curY is None:
        return

    if prevX is not None:
        prevX.next = curY
    else:
        head = curY

    if prevY is not None:
        prevY.next = curX
    else:
        head = curX

    #swap next pointer
    temp = curX.next
    curX.next = curY.next
    curY.next = temp

    return head


def test():
    lst = LinkedList()
    lst.push(7)
    lst.push(6)
    lst.push(5)
    lst.push(4)
    lst.push(3)
    lst.push(2)
    lst.push(1)
    lst.print_list()
    swapNodes(lst.head, 4, 3)
    lst.print_list()

if __name__ == '__main__':
    test()

