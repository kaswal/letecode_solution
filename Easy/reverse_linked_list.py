class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

    def printll(self):
        if self.head is None:
            return "nothing to print"
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

    def reverselinkedlist(self):
        current = self.head
        prev = None
        temp = None

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("print original linked list")
ll.printll()

print("reversing original linked list")
ll.reverselinkedlist()
ll.printll()