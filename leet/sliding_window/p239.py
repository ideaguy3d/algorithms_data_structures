"""
Sliding Window Maximum
"""
import unittest
from typing import List


class Solution1a:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums

        left = [0] * n
        right = [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            j = n - i - 1
            if j % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


class Solution1b:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums

        left, right = [0] * n, [0] * n
        left[0], right[n - 1] = nums[0], nums[n - 1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            j = n - i - 1
            if j % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output


class TestSolutions(unittest.TestCase):
    """
    [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
    7

    [1,3,-1,-3,5,3,6,7]
    3

    [1]
    1
    """
    a1, a2 = [-6, -10, -7, -1, -9, 9, -8, -4, 10, -5, 2, 9, 0, -7, 7, 4, -2, -10, 8, 7], 7
    b1, b2 = [1, 3, -1, -3, 5, 3, 6, 7], 3
    c1, c2 = [1], 1

    def test_s1a(self):
        """
        [9,9,10,10,10,10,10,10,10,9,9,9,8,8]
        [3,3,5,5,6,7]
        [1]
        :return:
        """
        s = Solution1a
        self.assertEqual([9, 9, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8],
                         s.maxSlidingWindow(self.a1, self.a2),
                         "1. test input with len greater 8")
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow(self.b1, self.b2), "2. test basic input")
        self.assertEqual([1], s.maxSlidingWindow(self.c1, self.c2), "3. test edge case 1")

    def test_s1b(self):
        s = Solution1b
        self.assertEqual([9, 9, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8],
                         s.maxSlidingWindow(self.a1, self.a2),
                         "1. test input with len greater 8")
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow(self.b1, self.b2), "2. test basic input")
        self.assertEqual([1], s.maxSlidingWindow(self.c1, self.c2), "3. test edge case 1")


if __name__ == '__main__':
    unittest.main(verbosity=3)
