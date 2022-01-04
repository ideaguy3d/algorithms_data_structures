import unittest
from typing import List


class Solution1:
    @staticmethod
    def missingElement(nums: List[int], k: int) -> int:
        def missing(idx):
            return nums[idx] - nums[0] - idx

        n = len(nums)

        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        left, right = 0, n - 1
        while left != right:
            pivot = left + (right - left) // 2
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot

        return nums[left - 1] + k - missing(left - 1)


class TestSolutions(unittest.TestCase):
    """
    [4,7,9,10]
    1

    [4,7,9,10]
    3

    [1,2,4]
    3
    """

    def test_s1(self):
        s = Solution1
        self.assertEqual(s.missingElement([4, 7, 9, 10], 1), 5, "Test input returns 5")
        self.assertEqual(s.missingElement([4, 7, 9, 10], 3), 8, "Test input return 8")
        self.assertEqual(s.missingElement([1,2,4], 3), 6, "Test when k is greater than last element")


if __name__ == '__main__':
    unittest.main(verbosity=3)

# end of file
