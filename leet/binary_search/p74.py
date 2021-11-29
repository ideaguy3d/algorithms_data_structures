"""
topics
- Binary Search
- Matrix
"""
import unittest
from typing import List


class Solution:
    """
    binary search
    - space: O(1)
    - time:  O(logMN)
    """

    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> False:
        m = len(matrix)
        if not m or m == 0:
            return False

        n = len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            pivot_index = (left + right) // 2
            pivot_elem = matrix[pivot_index // n][pivot_index % n]
            if pivot_elem == target:
                return True
            else:
                if target < pivot_elem:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1
        return False


class Test_Solution(unittest.TestCase):
    def test_s1(self):
        s = Solution
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertEqual(s.searchMatrix(matrix, 3), True, "Test that the target 3 is found in the matrix")
        self.assertEqual(s.searchMatrix(matrix, 13), False, "Test the the target 13 is NOT found in the matrix")


if __name__ == '__main__':
    unittest.main(verbosity=3)

#
