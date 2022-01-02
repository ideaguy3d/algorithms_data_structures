import unittest
from typing import List


class Solution1:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]):
        pass


class TestSolution:
    def test_s1(self):
        l1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
        l2 = [[1, 5], [8, 12], [15, 24], [25, 26]]
        io = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        s = Solution1

#
