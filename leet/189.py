from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k): nums.insert(0, nums.pop())
        print(nums)


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
# end of file
