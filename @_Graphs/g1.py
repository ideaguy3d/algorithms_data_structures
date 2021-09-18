"""
https://leetcode.com/explore/featured/card/graph/

The Definition of “graphs” and Terminologies

“Graphs” are non-linear data structure consisting of vertices and edges. There are a lot of terminologies to describe a graph. If you encounter an unfamiliar term in the following Explore Card, you may look up the definition below.

⤍ Vertex: In Figure 1, nodes such as A, B, and C are called vertices of the graph.
⤍ Edge: The connection between two vertices are the edges of the graph. In Figure 1, the connection between person A and B is an edge of the graph.
⤍ Path: the sequence of vertices to go through from one vertex to another. In Figure 1, a path from A to C is [A, B, C], or [A, G, B, C], or [A, E, F, D, B, C].
                **Note**: there can be multiple paths between two vertices.
⤍ Path Length: the number of edges in a path. In Figure 1, the path lengths from person A to C are 2, 3, and 5, respectively.
⤍ Cycle: a path where the starting point and endpoint are the same vertex. In Figure 1, [A, B, D, F, E] forms a cycle. Similarly, [A, G, B] forms another cycle.
⤍ Negative Weight Cycle: In a “weighted graph”, if the sum of the weights of all edges of a cycle is a negative value, it is a negative weight cycle. In Figure 4, the sum of weights is -3.
⤍ Connectivity: if there exists at least one path between two vertices, these two vertices are connected. In Figure 1, A and C are connected because there is at least one path connecting them.
⤍ Degree of a Vertex: the term “degree” applies to unweighted graphs. The degree of a vertex is the number of edges connecting the vertex. In Figure 1, the degree of vertex A is 3 because three edges are connecting it.
⤍ In-Degree: “in-degree” is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional edges incident to the vertex. In Figure 2, A’s indegree is 1, i.e., the edge from F to A.
⤍ Out-Degree: “out-degree” is a concept in directed graphs. If the out-degree of a vertex is d, there are d edges incident from the vertex. In Figure 2, A’s outdegree is 3, i,e, the edges A to B, A to C, and A to G.

"""


class UnionFind1:  # Quick Find
    """
    a.k.a Disjoint Set
    - find()
    - union()
    - connected()
    """
    def __init__(self, size):
        self.root = [_ for _ in range(size)]

    def find(self, i):
        return self.root[i]

    def union(self, i, j):
        iroot = self.root[i]
        jroot = self.root[j]
        if iroot != jroot:
            for n in range(len(self.root)):
                if self.root[n] == jroot:
                    self.root[n] = iroot

    def connected(self, i, j):
        return self.root[i] == self.root[j]


class UnionFind2:  # Quick Union
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class UnionFind:  # Quick Union by Rank
    def __init__(self, size):
        pass

    def find(self, x):
        pass

    def union(self, x, y):
        pass

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)
# 1-2-5-6-7
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
# 3-8-9
uf.union(3, 8)
uf.union(8, 9)
# 4 is an island since it was not unioned to anything

print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false










#
