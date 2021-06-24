# O(2^n)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 2) + fibonacci(n - 1)


cache = {}


def fibonacci_dp(n):
    global cache
    if n <= 1: return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)
    return cache[n]


# O(n)
def fibonacci_tb(n):
    ar = [0, 1]
    for i in range(2, n + 1):
        ar.append(ar[i - 1] + ar[i - 2])
    return ar[n]



num = 10
print(f'\n_> fib({num}) = ', fibonacci_tb(num))

debug = 1

# end of file
