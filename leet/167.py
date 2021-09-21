from typing import List



class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, outer in enumerate(nums):
            for j, inner in enumerate(nums):
                if i == j and nums[i] == nums[j]:
                    continue
                if outer + inner == target:
                    return i+1, j+1


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            added = nums[left] + nums[right]
            if added == target:
                return [left+1, right+1]
            elif added < target:
                left += 1
            else:
                right -= 1


class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        2_pointer algorithm
        nums - a sorted ascending list
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            _sum = nums[left] + nums[right]
            if target == _sum:
                return left + 1, right + 1
            if target < _sum:
                right -= 1
            else:
                left += 1
        return -1

print(Solution.two_sum([1, 2, 3, 4, 5], 5))


#
