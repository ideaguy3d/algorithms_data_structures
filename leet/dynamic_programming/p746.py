"""
topics
- dynamic programming
- arrays

recurrence relation:
f(n) = min(minCost[n-1]+cost[n-1], minCost[n-2]+cost[n-2])
"""
import unittest
from typing import List


class Solution1:
    """
    bottom-up dynamic programming (tabulation)
    space: O(N)
    time:  O(N)
    """

    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        top = len(cost) + 1
        min_cost = [0] * top
        for i in range(2, top):
            take_one_step = min_cost[i - 1] + cost[i - 1]
            take_two_steps = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one_step, take_two_steps)
        return min_cost[-1]


class Test_Solutions(unittest.TestCase):
    def test_s1(self):
        s = Solution1
        self.assertEqual(s.minCostClimbingStairs([10, 15, 20]), 15, 'test that input returns 15')
        self.assertEqual(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6, 'test that input returns 6')


if __name__ == '__main__':
    unittest.main(verbosity=3)

# end of file
