from typing import List
import math


def implementation_1():
    class Solution:
        def searchInsert(self, nums: List[int], target: int) -> int:
            self.nums = nums
            self.tar = target
            self.nums_right = len(nums) - 1

            if target > nums[self.nums_right]:
                return self.nums_right + 1
            elif target < nums[0]:
                return 0

            search = self.binary_search()
            if search > -1:
                return search

            return self.positional_binary_search()

        def binary_search(self):
            left = 0
            right = len(self.nums) - 1
            while left <= right:
                mid = math.floor(left + (right - left) / 2)
                if self.tar == self.nums[mid]:
                    return mid
                if self.tar < self.nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        def positional_binary_search(self):
            nums, target = self.nums, self.tar
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = math.floor(left + (right - left) / 2)
                cur, _next = nums[mid], nums[mid + 1]
                if cur < target < _next:
                    return cur
                if target < cur:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

    print(Solution().searchInsert([1, 3, 5, 6], 2))


def implementation_2():
    class Solution:
        def searchInsert(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                p = (left + right) >> 1
                if target == nums[p]: return p
                if target < nums[p]:
                    right = p - 1
                else:
                    left = p + 1
            return left


implementation_1()

# end of file
