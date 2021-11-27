"""
from studying:
https://www.udemy.com/course/algorithmic-problems-in-python/
"""


def recursion_practice_1():
    def factorial_no_accumulator(n):
        """ This version will insert frames on the stack """
        if 1 == n: return 1
        return n * factorial_no_accumulator(n - 1)

    def factorial_with_accumulator(n, accumulator=1):
        """ This version won't insert frames on the stack """
        if 1 == n:
            return accumulator
        return factorial_with_accumulator(n - 1, n * accumulator)

    print(factorial_no_accumulator(4))
    print(factorial_with_accumulator(4))


def recursion_practice_2():
    div_by_3 = []

    def factorial(n):
        nonlocal div_by_3
        if n == 0:
            return 1
        r1 = factorial(n - 1)
        r2 = n * r1
        if r2 % 3 == 0:
            div_by_3.append(r2)
        return r2

    def factorial_dp(n, accumulator=1):
        if n == 0:
            return accumulator
        return n * factorial_dp(n - 1, n * accumulator)

    def fibonacci(n):
        nonlocal div_by_3

        if n == 0:
            return 0
        if n == 1:
            return 1

        fib1 = fibonacci(n - 1)
        fib2 = fibonacci(n - 2)
        sequence = fib1 + fib2

        if sequence % 3 == 0:
            div_by_3.append(sequence)

        return sequence

    def fibonacci_dp(n, a=0, b=1):
        if n == 0: return a
        if n == 1: return b
        return fibonacci_dp(n-1, b, a+b)

    #print('factorial', factorial(5))
    print('fibonacci', fibonacci(6))
    b36 = 1


recursion_practice_2()

# end of file
