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


def practice2():
    def kn(index, _weights, _values, _target):  #
        if index <= -1 or _target <= 0:
            result = 0
        elif _weights[index] > _target:
            result = kn(index - 1, _weights, _values, _target)
        else:
            v = kn(index - 1, _weights, _values, _target)
            v_plus1 = _values[index] + kn(index - 1, _weights, _values, _target - _weights[index])
            result = max(v, v_plus1)
        return result

    def kn2(index, c_target):
        if index <= -1 or c_target <= 0:
            result = 0
        elif weights[index] > c_target:
            result = kn2(index - 1, c_target)
        else:
            cur = kn2(index - 1, c_target)
            cur_plus1 = values[index] + kn2(index - 1, c_target - weights[index])
            result = max(cur, cur_plus1)
        return result

    def kdp(index: int, c_target: int, matrix: dict):
        h = str(index) + '_' + str(c_target)
        if h in matrix:
            return matrix[h]
        elif index <= -1 or c_target <= 0:
            result = 0
        elif weights[index] > c_target:
            result = kdp(index - 1, c_target, matrix)
        else:
            cur = kdp(index - 1, c_target, matrix)
            cur_plus1 = values[index] + kdp(index - 1, c_target - weights[index], matrix)
            result = max(cur, cur_plus1)
        matrix[h] = result
        return result

    weights = [1, 2, 4, 2, 5]
    values = [5, 3, 5, 3, 2]
    target = 10

    print('\nknd = ', kdp(4, target, {}))
    print()
    print('kn2 = ', kn2(4, target))


#general_practice()
practice2()

# end of file
