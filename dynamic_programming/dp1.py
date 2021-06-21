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

n = 10
print(f'\n_> fib({n}) = ', fibonacci_dp(n))




# end of file
