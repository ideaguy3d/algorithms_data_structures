import unittest
from typing import List


class Solution1a:
    @staticmethod
    def findPeakGrid(matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            mid = (top + bottom) // 2
            if max(matrix[mid]) > max(matrix[mid + 1]):
                bottom = mid
            else:
                top = mid + 1

        return [bottom, matrix[bottom].index(max(matrix[bottom]))]


class TestSolutions(unittest.TestCase):
    """
    [[1,4],[3,2]]
    [[10,20,15],[21,30,14],[7,16,32]]
    """

    def test_s1(self):
        """
        [0,1]
        [2,2] """
        s = Solution1a
        self.assertEqual(s.findPeakGrid([[1, 4], [3, 2]]),
                         [0, 1],
                         "1. assert input returns expected output")
        self.assertEqual(s.findPeakGrid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]),
                         [2, 2],
                         "2. assert input returns expected output")


if __name__ == '__main__':
    unittest.main(verbosity=3)

# end of file
