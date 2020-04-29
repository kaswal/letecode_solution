class Stack:
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def top(self):
        return self.item[-1]

    def update(self, data):
        self.top()[1] = data

    def printstack(self):
        return self.item


s = Stack()


def merge_overlapping(arr):
    arr.sort()
    s.push(arr[0])

    for i in range(1, len(arr)):
        if arr[i][0] > s.top()[1]:
            s.push(arr[i])
        elif s.top()[0] <= arr[i][0] <= s.top()[1]:
            if arr[i][1] > s.top()[1]:
                s.update(arr[i][1])

    return s.printstack()




input_array = [[6,8],[1,9],[2,4],[4,7]]

print(merge_overlapping(input_array))
