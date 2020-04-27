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


def add(ll1, ll2):
    curr1 = ll1.head
    curr2 = ll2.head
    store = 0

    while curr1 and curr2:
        newdata = curr1.data + curr2.data + store
        store = 0
        if newdata // 10 == 0:
            ll3.append(newdata % 10)
        else:
            store = newdata // 10
            ll3.append(newdata % 10)

        curr1 = curr1.next
        curr2 = curr2.next

    while curr1:
        newdata = curr1.data + store
        store = 0
        if newdata // 10 == 0:
            ll3.append(newdata % 10)
        else:
            store = newdata // 10
            ll3.append(newdata % 10)

        curr1 = curr1.next

    while curr2:
        newdata = curr2.data + store
        store = 0
        if newdata // 10 == 0:
            ll3.append(newdata % 10)
        else:
            store = newdata // 10
        ll3.append(newdata % 10)

        curr2 = curr2.next




    return ll3


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()

print("first linked list:")
ll1.append(2)
ll1.append(4)
ll1.append(3)
ll1.append(4)
ll1.printll()

print("second linked list:")
ll2.append(9)
ll2.append(9)
# ll2.append(4)
ll2.printll()

print("adding both linked list:")
add(ll1, ll2)
ll3.printll()
