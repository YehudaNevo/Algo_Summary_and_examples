# A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected,
# edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum
# possible total edge weight.


# Kruskal’s Minimum Spanning Tree Algorithm ----------------------------------
import sys


def KruskalMST(self):
    result = []

    # An index variable, used for sorted edges
    i = 0

    # An index variable, used for result[]
    e = 0

    # Step 1:  Sort all the edges in
    # non-decreasing order of their
    # weight.  If we are not allowed to change the
    # given graph, we can create a copy of graph
    self.graph = sorted(self.graph,
                        key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(self.V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < self.V - 1:

        # Step 2: Pick the smallest edge and increment
        # the index for next iteration
        u, v, w = self.graph[i]
        i = i + 1
        x = self.find(parent, u)
        y = self.find(parent, v)

        # If including this edge does't
        #  cause cycle, include it in result
        #  and increment the indexof result
        # for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            self.union(parent, rank, x, y)
        # Else discard the edge

    minimumCost = 0
    print("Edges in the constructed MST")
    for u, v, weight in result:
        minimumCost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree", minimumCost)

    # Prim’s Minimum Spanning Tree----------------------

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)
