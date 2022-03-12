"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# __TEMPLATE__
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pass
