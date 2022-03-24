import collections
# implementation of a tree

def Binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, t, [], []])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, t, [], []])

    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left(root):
    return root[1]


def get_right(root):
    return root[2]


class BinaryTree(object):

    def __init__(self, root_obj):

        self.key = root_obj
        self.left = None
        self.right = None

    def __insert_left(self, item):

        if self.left is None:
            self.left = BinaryTree(item)
        else:
            self.left.insert(item)

    def __insert_right(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            self.right.insert(item)

    def insert(self, item):

        if item <= self.key:
            self.__insert_left(item)
        else:
            self.__insert_right(item)

    def traverse_inorder(self):
        if self.left is None:
            print(self.key)
            if not self.right is None:
                self.right.traverse_inorder()
        else:
            self.left.traverse_inorder()
            print(self.key)
            if not self.right is None:
                self.right.traverse_inorder()


class BinHeap(object):

    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def perc_up(self, i):

        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def insert(self,item):
        self.heap_list.append(item)
        self.size = self.size + 1
        self.perc_up(self.size)


def level_order_print(tree):

    if not tree:
        return
    nodes = collections.deque([tree])

    current_count = 1
    next_count = 0

    while len(nodes) != 0:

        current_node = nodes.popleft()
        current_count -= 1

        print(current_node.key)

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1
        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        if current_count == 0:
            print('\n')
            current_count,next_count = next_count,current_count