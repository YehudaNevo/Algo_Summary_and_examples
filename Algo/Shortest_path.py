# -----------------      DFS    BFS      ------------------------------------------------------

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            temp = queue.pop(0)
            array.append(temp.name)
            for child in temp.children:
                queue.append(child)

        return array



#

