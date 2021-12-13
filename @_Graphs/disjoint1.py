"""
leetcode card:
https://leetcode.com/explore/featured/card/graph/
leetcode problem:
https://leetcode.com/problems/number-of-provinces/


The Definition of “graphs” and Terminologies

“Graphs” are non-linear data structure consisting of vertices and edges. There are a lot of terminologies to describe
    a graph.

⤍ Vertex: nodes are called vertices of the graph.
⤍ Edge: The connection between two vertices are the edges of the graph.
⤍ Path: the sequence of vertices to go through from one vertex to another.
    There can be multiple paths between two vertices.
⤍ Path Length: the number of edges in a path.
⤍ Cycle: a path where the starting point and endpoint are the same vertex.
⤍ Negative Weight Cycle: In a “weighted graph”, if the sum of the weights of all edges of a cycle is a negative value,
    it is a negative weight cycle.
⤍ Connectivity: if there exists at least one path between two vertices, these two vertices are connected.
⤍ Degree of a Vertex: the term “degree” applies to unweighted graphs. The degree of a vertex is the number of edges
    connecting the vertex.
⤍ In-Degree: “in-degree” is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional
    edges incident to the vertex.
⤍ Out-Degree: “out-degree” is a concept in directed graphs. If the out-degree of a vertex is d, there are d edges
    incident from the vertex.

"""


class UnionFind1:  # Quick Find
    """
    a.k.a Disjoint Set
    - find()
    - union()
    - connected()
    """
    def __init__(self, size):
        # initially the element at the index should be the index itself
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


class UnionFind3:  # Quick Union by Rank
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        """ Find the root """
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class UnionFind4:
    """ Union Find / Disjoint Set 1st implementation from memory """
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class DisjointSet1:
    def __init__(self, n):
        pass

    def union(self, x, y):
        pass

    def find(self, x):
        pass

    def connected(self, x, y):
        pass


def use_uf1():
    uf = UnionFind1(10)
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

    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true








# end of file
