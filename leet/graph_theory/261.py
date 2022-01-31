from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ iterative depth first search """
        if len(edges) != n-1: return False
        adj_list = [[] for i in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if parent[node] == neighbor:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                stack.append(neighbor)

        return len(parent) == n


def test1():
    graph = Solution()
    if graph.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]):
        print('True')
    else:
        print('False')


def test2():
    graph = Solution()
    if graph.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]):
        print('True')
    else:
        print('False')



test1()
test2()

#
