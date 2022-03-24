class Stuck(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def print(self):
        temp = Stuck()
        while not self.isEmpty():
            x = self.pop()
            print(x)
            temp.push(x)
        while not temp.isEmpty():
            self.push(temp.pop())
        print('-'*40)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        print('stuck is empty')

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# implementation of a queue
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def __sizeof__(self):
        return len(self.items)


def balance_check(arr):
    if len(arr) % 2 != 0:
        return False

    opening = set('([{')

    # matches = {('(', ')'), ('[', ']'), ('{', '}')}
    matches = {('(', ')'), ('[', ']'), ('{', '}')}
    stuck = Stuck()

    for p in arr:
        if p in opening:
            stuck.push(p)
        else:
            if stuck.isEmpty():
                return False
            last_open = stuck.pop()
            if (last_open, p) not in matches:
                return False

    return stuck.isEmpty()


class QueueUse2stuck(object):

    def __init__(self):
        self.stack1 = Stuck()
        self.stack2 = Stuck()

    def isEmpty(self):
        return self.stack1.isEmpty()

    def enqueue(self, item):
        if self.stack1.isEmpty():
            self.stack1.push(item)
        else:
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
            self.stack1.push(item)
            while not self.stack2.isEmpty():
                self.stack1.push(self.stack2.pop())

    def dequeue(self):
        return self.stack1.pop()

    def size(self):
        return self.stack1.size()