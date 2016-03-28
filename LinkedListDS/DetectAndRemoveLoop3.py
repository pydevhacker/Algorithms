'''
Detect and Remove loop

size of linked list = a
Number of nodes before loop = m
slow and fast pointer meet at kth node of loop = k
speed of fast pointer = 2 * speed of slow pointer
(m + n*x + k) = 2(m + n*y + k)
where x is fast pointer speed and y is slow pointer speed n is number of cycles taked by slow and fast pointer

m + k = (x - 2y)*n

if we start slow pointer from head and fast pointer from meeting node in loop(k) and increment both the pointers by one then they will meet at starting point of loop.
By the time slow cover m distance, fast node will also cover m distance since both are moving at same speed. However fast node has started from kth node in loop ie k+m will complete one cycle.
Therefore both node will be at starting point of loop
'''

from LinkedListDS.LinkedListUtil import printNode
from LinkedListDS.LinkedList import LinkedList

def detectAndRemove(head):
    slow = head
    fast = head.next
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow.data == fast.data:
            print("LOOP DETECTED")
            break

    if slow.data == fast.data:
        slow = head
        while slow.data != fast.next.data:
            slow = slow.next
            fast = fast.next
        fast.next = None


def test():
    lst = LinkedList()
    lst.push(10)
    lst.push(4)
    lst.push(15)
    lst.push(20)
    lst.push(50)

    #create a loop
    lst.head.next.next.next.next.next = lst.head.next.next
    print('create loop at ', lst.head.next.next.next.next.next.data)
    detectAndRemove(lst.head)
    printNode(lst.head)

if __name__ == '__main__':
    test()
