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


# Dijkstra's Algo  ------
# 1. init all the dis to inf + pi to none.
# 2. min heap for all the vertices
# 3. till the queue is not empty - pop the min and update his adj distance...


def Dijkstra(graph, source):
    for vertex in graph.vertices:
        vertex.dist = float("inf")
        vertex.pi = None

    source.dist = 0
    res = []
    queue = [vertex for vertex in graph.vertices]
    while len(queue):
        u = queue.pop_min(0)
        res.append(u)
        for vertex in graph.adj(u):
            if vertex.dist > u.dist + graph.w[u][vertex]:
                vertex.dist = u.dist + graph.w[u][vertex]
                vertex.pi = u
    return res
