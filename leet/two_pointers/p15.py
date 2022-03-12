"""
Doubly linked list / two pointers
"""
import unittest
from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSumII(nums, i, res)

        return res

    @staticmethod
    def twoSumII(nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            _sum = nums[i] + nums[lo] + nums[hi]
            if _sum < 0:
                lo += 1
            elif _sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


class TestSolution(unittest.TestCase):
    """
    [-1,0,1,2,-1,-4]
    []
    [0]
    --
    [[-1,-1,2],[-1,0,1]]
    []
    []
    """

    def test_s1(self):
        s = Solution1()
        self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -4]),
                         [[-1, -1, 2], [-1, 0, 1]],
                         "Test that input gets back a list of 2 lists of ints")


if __name__ == '__main__':
    unittest.main(verbosity=3)



#
