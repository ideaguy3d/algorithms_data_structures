"""
twoSum
https://leetcode.com/problems/two-sum/
"""
from typing import List, Tuple
import unittest


# template
class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        pass


class Solution1a:
    @staticmethod
    def twoSum(nums: List[int], target: int):
        _map = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in _map:
                return [i, _map.get(x)]
            _map[num] = i


# template
class Solution1b:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> Tuple[int, int]:
        m = {}
        for i, n in enumerate(nums):
            c = target - n  # mf
            if c in m: return i, m[c]
            m[n] = i



class TestSolutions(unittest.TestCase):
    """
    [2,7,11,15]
    9
    """
    def test_s1a(self):
        s = Solution1a
        result1 = s.twoSum([2, 7, 11, 15], 9)
        print("result1 = ", result1)
        self.assertIn(result1, [[1, 0], (1, 0), (0, 1)], 'test_s1a assertion 1, result in container')

    def test_s1b(self):
        solution = Solution1b
        result1 = solution.twoSum([2, 7, 11, 15], 9)
        print("result1 = ", result1)
        self.assertIn(result1, [[1, 0], (1, 0), (0, 1)], 'test_s1b assertion 1, result in container')



if __name__ == '__main__':
    unittest.main(verbosity=3)


# end of file
