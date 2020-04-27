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

    def rem_dup(self, head):

        temp = head
        current = head

        while current is not None:

            if current.next is None and temp.next is None:
                return head

            temp = current.next

            if temp.data == current.data:
                current.next = temp.next
                temp = current.next
                current = temp

            else:
                current = temp

        return head


ll = LinkedList()

ll.append(1)
ll.append(1)
ll.append(2)
# ll.append(3)
# ll.append(3)

print("original linked list:")
ll.printll()

print("linked list after removal of duplicates")
ll.rem_dup(ll.head)
ll.printll()