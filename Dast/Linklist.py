# implementation of a link list
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next_node = None


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next_node = None


class LinkList(object):

    def __init__(self):
        self.head = None
        # self.tail = None

    def insert(self, item):
        node = Node(item)
        node.next_node = self.head
        self.head = node

    def remove(self):
        if self.head is None:
            return False
        else:
            self.head = self.head.next_node


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.nextn_node is not None:
        marker1 = marker1.next_node
        marker2 = marker2.nextn_node.next_node

        if marker2 == marker1:
            return True
    return False


def reverse_linklist(linklist):
    pass