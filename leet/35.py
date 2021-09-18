from typing import List
import math


class Solution1:
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


class Solution2:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            p = (left + right) >> 1
            if target == nums[p]: return p
            if target < nums[p]:
                right = p - 1
            else:
                left = p + 1
        return left


class Solution3:
    @staticmethod
    def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            return 0
        elif target > nums[right]:
            return right + 1

        # binary search
        while left <= right:
            pivot = left + (right - 1)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot - 1] < target < nums[pivot]:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1


print(Solution3().searchInsert([1, 3, 5, 6], 5))
print(Solution3().searchInsert([1, 3, 5, 6], 2))

# end of file
