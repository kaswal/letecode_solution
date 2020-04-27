class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert at the end
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            # newnode.next = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            # newnode.next = None

    # insert at the beginning
    def push(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def printll(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()


ll1.append(1)
ll1.append(2)
ll1.append(4)
#ll2.append(2)
ll2.append(1)
ll2.append(3)
ll2.append(4)
#ll2.append(10)


# function to merge 2 linked lists
def merge(p, q):

    while p and q:

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        ll3.append(s.data)

    while p:
        s = p
        p = s.next
        ll3.append(s.data)

    while q:
        s = q
        q = s.next
        ll3.append(s.data)


    return ll3.printll()


print("printing sorted linked list 1:")
ll1.printll()

print("printing sorted linked list 2:")
ll2.printll()

print("merging 2 sorted linked lists:")
print(merge(ll1.head, ll2.head))

