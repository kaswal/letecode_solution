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


ll1 = LinkedList()
ll2 = LinkedList()

ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)

# print("print original linked list")
# ll1.printll()
#

ll3 = ll1
print("reversing original linked list")
reverselinkedlist(ll1.head)
ll2.printll()


print(".......................................")
ll1.printll()
ll2.printll()
