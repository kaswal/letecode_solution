class MinStack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, data):
        if self.is_empty():
            self.items.append(data)
            self.min_items.append(data)
        else:
            if data > self.top():
                self.items.append(data)
            else:
                self.min_items.append(data)
                self.items.append(data)

    def top(self):
        return self.min_items[-1]

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            return "MinStack is empty, nothing to POP"
        else:
            p = self.items.pop()
            if p == self.top():
                self.min_items.pop()

    def getmin(self):
        return self.min_items[-1]


minstack = MinStack()

minstack.push(18)
minstack.push(19)
minstack.push(29)
minstack.push(15)
minstack.push(16)
print(minstack.getmin())

minstack.pop()
minstack.pop()
print(minstack.getmin())
