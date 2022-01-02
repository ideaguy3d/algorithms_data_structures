import unittest
from typing import List


class Solution:
    """ Linear Scan """

    @staticmethod
    def findPeakElement(nums: List[int]) -> int:
        n_len = len(nums)
        for i, n in enumerate(nums):
            if n_len == i + 1: continue
            if nums[i] > nums[i + 1]:
                return i
        return n_len - 1


class TestSolution(unittest.TestCase):
    def test_s1(self):
        """
        [1,2,3,1]
        [1,2,1,3,5,6,4]
        """
        s = Solution
        self.assertEqual(s.findPeakElement([1, 2, 3, 1]), 2, "Test that input returns index 2")
        self.assertEqual(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]), 1, "Test that input returns index 1")


if __name__ == '__main__':
    unittest.main(verbosity=3)

# end of file
