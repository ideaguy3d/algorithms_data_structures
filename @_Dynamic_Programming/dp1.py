cache = {}
cache_step = {}


def general_practice():
    def dp_ways_to_cover_steps(steps):
        global cache_step
        if steps < 0: return 0
        if steps == 0: return 1
        if steps in cache_step:
            return cache_step[steps]
        else:
            cache_step[steps] = dp_ways_to_cover_steps(steps - 1) \
                                + dp_ways_to_cover_steps(steps - 2) + dp_ways_to_cover_steps(steps - 3)
        return cache_step[steps]

    def ways_to_cover_steps(steps):
        if steps < 0: return 0
        if steps == 0: return 1
        return ways_to_cover_steps(steps - 3) + ways_to_cover_steps(steps - 2) + ways_to_cover_steps(steps - 1)

    isteps = 12
    print(f'\nways_to_cover_steps({isteps}) = ', dp_ways_to_cover_steps(isteps))


def fibonacci_practice():
    # O(2^n)
    def fibonacci(n):
        if n <= 1: return n
        return fibonacci(n - 2) + fibonacci(n - 1)

    # O(n)
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


general_practice()
# end of file
