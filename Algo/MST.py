# A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected,
# edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum
# possible total edge weight.
import sys


class DisJoinSets():
    def __init__(self, elements):
        self.sets = {element for element in elements}

    def find(self, element):
        if self.sets[element] == element:
            return element
        return self.find(self.sets[element])

    def union(self, ele1, ele2):
        self.sets[self.find(ele1)] = self.find(ele2)


# Kruskal’s Minimum Spanning Tree Algorithm ----------------------------------
def Kruskal(graph):
    res = []
    sets = DisJoinSets(graph.v)
    sorted_e = sorted(graph.edges, key=lambda e: graph.w[e])
    for (u, v) in sorted_e:
        if sets.find(u) != sets.find(v):
            res.append((u, v))
            sets.union(u, v)
    return res


# Prim Algo ------------------------------------------------------

def Prim(graph, sorce):
    for vertex in graph.vertices:
        vertex.dis = float("inf")
        vertex.pi = None

    sorce.dis = 0;
    queue = [vertex for vertex in graph.vertices]
    while len(queue):
        u = queue.pop(0)
        for vertex in graph.adjancy(u):
            if vertex in queue and graph.w[u, vertex] < vertex.d:
                vertex.d = graph.w[u, vertex]
                vertex, pi = u
