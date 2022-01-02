import unittest
from typing import List


class Solution1:
    @staticmethod
    def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
        if k <= 1: return 0

        prod = 1
        ans = left = 0

        for right, val in enumerate(nums):
            prod *= val
            while k <= prod:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans


class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pass


class TestSolution(unittest.TestCase):
    """
    [10,5,2,6]
    100

    [1,2,3]
    0
    """
    def test_s1(self):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=3)








# end of file
