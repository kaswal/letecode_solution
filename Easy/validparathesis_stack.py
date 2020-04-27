class Stack:

    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def len(self):
        return len(self.items)


s = Stack()


def validparenthesis(mystr):
    for i in range(len(mystr)):
        if s.len() == 0:
            s.push(mystr[i])
        elif (s.top() == '(' and mystr[i] == ')') or (s.top() == '[' and mystr[i] == ']') or (s.top() == '{' and '}' ==
                                                                                              mystr[i]):
            s.pop()
        else:
            s.push(mystr[i])

    return s.is_empty()


mystr = "(((((())))))"

print(validparenthesis(mystr))
