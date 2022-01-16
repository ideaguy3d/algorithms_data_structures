"""
topics
- dynamic programming
- combinations & permutations
- memoization
"""
import unittest


class Solution1:
    """
    recursion
    - space: O(n)
    - time:  O(2^n)
    """

    def climbStairs(self):
        pass


class Solution2:
    """
    recursion with memoization
    - space: O(n)
    - time:  O(n)
    """

    def climbStairs(self):
        pass


class Solution3:
    """
    dynamic programming
    - space: O(n)
    - time:  O(n)
    """
    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1: return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Test_Solutions(unittest.TestCase):
    def test_s1(self):
        pass

    def test_s2(self):
        pass

    def test_s3(self):
        s = Solution3
        self.assertEqual(s.climbStairs(6), 13, 'input 6 returns 13')
        self.assertEqual(s.climbStairs(2), 2, 'input 2 returns 2')
        self.assertEqual(s.climbStairs(3), 3, 'input 3 returns 3')


if __name__ == '__main__':
    unittest.main()

# end of file
