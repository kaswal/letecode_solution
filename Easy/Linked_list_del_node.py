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

    def del_node(self, head, node_to_del):

        current = head
        temp = head

        while current is not None:

            if temp.data == node_to_del:
                temp = current.next
                current = temp
                self.head = current
                return head

            temp = current.next

            if temp.data == node_to_del:
                current.next = temp.next
                return head

            else:
                current = temp


ll = LinkedList()

ll.append(4)
ll.append(5)
ll.append(1)
ll.append(9)

print("original linked list:")
ll.printll()

print("modified linked list after deletion of node:")
ll.del_node(ll.head, 1)
ll.printll()
