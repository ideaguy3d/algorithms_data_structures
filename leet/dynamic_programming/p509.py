"""
recurrence relation:
f(n) = f(n-1) + f(n-2)
"""
import unittest


class Solution1:
    """
    recursive,
    space: O(n)
    time: O(2^n)
    """
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    """
    bottom up iterative tabulation,
    space: O(n)
    time: O(n)
    """
    def fib(self, n):
        pass


class Test_Solutions(unittest.TestCase):
    def test_s1(self):
        print('Testing Solution1')
        s1 = Solution1()
        self.assertEqual(s1.fib(2), 1, 'Test that fib(2) = 2')
        self.assertEqual(s1.fib(4), 3, 'test fib(4)')

    def test_s2(self):
        print('Testing Solution2')


if __name__ == '__main__':
    unittest.main()


# end of file
