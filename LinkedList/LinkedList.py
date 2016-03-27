class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in Linked List")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def delete_node(self, key):
        #store head node
        temp = self.head

        #If head node itself holds the key to be deleted
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        #Search for the key to be detected
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #if key not present in LL
        if temp is Node: return

        prev.next = temp.next
        temp = None

    def delete_index(self, position):
        if self.head is None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = next

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def count_rec(self):
        return self.count_rec_helper(self.head)

    def count_rec_helper(self, node):
        if not node:
            return 0
        return 1 + self.count_rec_helper(node.next)


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,)
            temp = temp.next

if __name__ == '__main__':
    lst = LinkedList()
    lst.append(6)
    lst.push(7)
    lst.push(1)
    lst.append(4)
    lst.insert_after(lst.head.next, 8)

    lst.print_list()
    print("Size", lst.count())
    lst.delete_node(8)
    print("This is the new list")
    lst.print_list()
    print("Size", lst.count())
    lst.delete_index(2)
    print("This is the new list")
    lst.print_list()
    print("Size", lst.count())