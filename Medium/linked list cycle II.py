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
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


ll = LinkedList()


def linkedlistcycle(head):

    p = head
    q = head
    flag = True

    while flag:

        p = p.next.next
        q = q.next

        if p == q:
            print("loop detected")
            q = head
            flag2 = True
            pos = 0

            while flag2:
                if p == q:
                    return pos
                else:
                    q = q.next
                    p = p.next
                    pos += 1

                    if p == q:
                        return pos
    return "No Loop Detected"


ll.append(3)
ll.append(2)
ll.append(0)
ll.append(-4)
# ll.append(50)



print("Print the linked list")
ll.printll()

print("intentionally putting loop condition")
ll.head.next.next.next.next = ll.head.next

print(linkedlistcycle(ll.head))