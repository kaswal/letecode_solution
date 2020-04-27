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

    def modified(self, header):
        current = header
        p = current.next

        while current.next is not None:
            q = p
            prev = None

            while q.next is not None:
                prev = q
                q = q.next

            if q == p:
                break

            else:
                current.next = q
                q.next = p
                current = p
                p = current.next
                prev.next = None

        return header


ll1 = LinkedList()

print("original linkedlist:")
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.append(6)
ll1.append(7)
# ll1.append(8)

ll1.printll()

print("modified linkedlist:")
ll1.modified(ll1.head)
ll1.printll()
