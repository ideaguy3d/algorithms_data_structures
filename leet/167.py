from typing import List



class Solution:
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

#
