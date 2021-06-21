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

num = 10
print(f'\n_> fib({num}) = ', fibonacci_dp(num))




# end of file
