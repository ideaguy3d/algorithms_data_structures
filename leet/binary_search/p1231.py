"""
Binary Search
Array
"""
import unittest
from typing import List


class Solution1a:
    @staticmethod
    def maximizeSweetness(sweetness: List[int], k: int) -> int:
        num_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // num_people

        while left < right:
            mid = (left + right + 1) // 2
            current_sweetness = 0
            people_with_chocolate = 0

            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= mid:
                    people_with_chocolate += 1
                    current_sweetness = 0

            if people_with_chocolate >= k + 1:
                left = mid
            else:
                right = mid - 1

        return right


class TestSolution(unittest.TestCase):
    """
    [1,2,3,4,5,6,7,8,9]
    5
    [5,6,7,8,9,1,2,3,4]
    8
    [1,2,2,1,2,2,1,2,2]
    2
    """

    def test_s1(self):
        s = Solution1a
        self.assertEqual(s.maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
                         6, '1. assert input produces output')
        self.assertEqual(s.maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 9),
                         1, '2. assert input produces output')
        self.assertEqual(s.maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2),
                         5, '3. assert input outputs 5')


if __name__ == '__main__':
    unittest.main(verbosity=3)
