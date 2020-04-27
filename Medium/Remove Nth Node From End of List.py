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

    def del_node(self, delnodenum):
        current = self.head
        prev = None
        length = 1
        while current is not None:
            if length == delnodenum and current != self.head:
                prev.next = current.next
                current = None
            elif length == delnodenum and current == self.head:
                self.head = current.next
                current = None
            else:
                length += 1
                prev = current
                current = current.next

        return self.head

    def remove_n_node(self, n):
        current = self.head
        hash_map = {}
        length = 1
        while current is not None:
            hash_map[current.data] = length
            current = current.next
            length += 1

        val = length - n

        for k, v in hash_map.items():
            if v == val:
                return val

    def printll(self):
        if self.head is None:
            return "nothing to print"
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


ll1 = LinkedList()

ll1.append(11)
ll1.append(12)
ll1.append(13)
ll1.append(14)
ll1.append(15)

print("original linked list:")
ll1.printll()

z = int(input("value of n: "))

print("new linked list after removing nth node:")
node_to_be_deleted = ll1.remove_n_node(z)
ll1.del_node(node_to_be_deleted)
ll1.printll()
