"""
topics
- Binary Search
"""
import unittest
from typing import List


class Solution1:
    """
    Binary Search
    space: O(1)
    time:  O(logN)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = self.findBound(nums, target, False)
        return [lower_bound, upper_bound]

    @staticmethod
    def findBound(nums: List[int], target: int, is_first: bool) -> int:
        n = len(nums)
        begin, end = 0, n - 1
        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                if is_first:
                    # we found the lower bound
                    if mid == begin or nums[mid-1] < target:
                        return mid
                    # search the left side
                    end = mid - 1
                else:
                    # we found the upper bound
                    if mid == begin or nums[mid+1] > target:
                        return mid
                    # search the right side
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1


class Test_Solutions(unittest.TestCase):
    def test_s1(self):
        s = Solution1()
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4], 'test that input returns [3,4]')
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1], 'test target not found')
        self.assertEqual(s.searchRange([], 0), [-1, -1], 'test an empty list')
        self.assertEqual(s.searchRange([5, 7, 7, 8, 10], 8), [3, 3], 'test when target is only found once')
        self.assertEqual(s.searchRange([5, 7, 7, 7, 7, 8, 10], 7), [1, 4], 'test when target is found 4 times')


if __name__ == '__main__':
    unittest.main(verbosity=3)

# end of file
