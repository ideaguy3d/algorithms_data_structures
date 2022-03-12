"""
Dynamic Programming
Binary Search
Array
"""

import unittest
from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution1a:
    @staticmethod
    def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for i, c in enumerate(colors):
            hashmap[c].append(i)

        query_results = []
        for i, (target_idx, color) in enumerate(queries):
            if color not in hashmap:
                query_results.append(-1)
                continue

            index_list = hashmap[color]
            insert = bisect_left(index_list, target_idx)

            _min = min(insert, len(index_list) - 1)
            _max = max(0, insert - 1)

            left_closest = abs(index_list[_max] - target_idx)
            right_closest = abs(index_list[_min] - target_idx)
            query_results.append(min(left_closest, right_closest))

        return query_results

        pass  # END_OF: shortestDistanceColor()


class TestSolutions(unittest.TestCase):
    """
    [1,1,2,1,3,2,2,3,3]
    [[1,3],[2,2],[6,1]]
    
    [1,2]
    [[0,3]]
    """
    a1 = [1, 1, 2, 1, 3, 2, 2, 3, 3]
    a2 = [[1, 3], [2, 2], [6, 1]]
    b1 = [1, 2]
    b2 = [[0, 3]]

    def test_s1(self):
        s = Solution1a
        self.assertEqual(s.shortestDistanceColor(self.a1, self.a2),
                         [3, 0, 3],
                         "1. test that shortest paths are properly found")
        self.assertEqual(s.shortestDistanceColor(self.b1, self.b2),
                         [-1],
                         "2. test that -1 is returned since color doesn't exist")


if __name__ == '__main__':
    unittest.main(verbosity=3)
