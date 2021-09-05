"""
from studying:
https://www.udemy.com/course/algorithmic-problems-in-python/
"""


def factorial_practice_1():
    def factorial_no_accumulator(n):
        """ This version will insert frames on the stack """
        if 1 == n: return 1
        return n * factorial_no_accumulator(n - 1)

    def factorial_with_accumulator(n, accumulator=1):
        """ This version won't insert frames on the stack """
        if 1 == n: return accumulator
        return factorial_with_accumulator(n-1, n * accumulator)

    print(factorial_no_accumulator(4))
    print(factorial_with_accumulator(4))


factorial_practice_1()

# end of file
