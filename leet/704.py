class Solution:
    @staticmethod
    def search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:  # why <= ?
            pivot = left + (right - left)
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


print(Solution.search([1, 2, 3], 2))
print(Solution.search([-1, 0, 3, 5, 9, 12], 9))

#
