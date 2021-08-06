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


def knapsack_practice():
    # k = knapsack problem
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
        if index <= -1 or c_target <= 0:
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


# TODO: spend more time understanding this!
def longest_common_subsequence_practice():
    subsequence = ''
    frame_count = 0
    call_stack = []

    def lcs_n(str1, str2, str1_len, str2_len, frame) -> int:
        # TODO: spend more time understanding this!
        nonlocal subsequence, frame_count
        frame_count += 1
        if str1_len == 0 or str2_len == 0:
            return 0

        c1 = str1[str1_len - 1]
        c2 = str2[str2_len - 1]
        if c1 == c2:
            call_stack.append({
                'frame': frame,
                'frame_count': frame_count,
                'str1_len': str1_len,
                'str2_len': str2_len,
                'c1': c1,
                'c2': c2
            })
            return 1 + lcs_n(str1, str2, str1_len - 1, str2_len - 1, frame + 1)
        else:
            call_stack.append({
                'frame': frame,
                'frame_count': frame_count,
                'str1_len': str1_len,
                'str2_len': str2_len,
                'c1': c1,
                'c2': c2,
            })
            # rp = recursive parameter
            rp1 = lcs_n(str1, str2, str1_len - 1, str2_len, frame + 1)

            call_stack.append({
                'frame': frame,
                'frame_count': frame_count,
                'str1_len': str1_len,
                'str2_len': str2_len,
                'c1': c1,
                'c2': c2,
                'rp1': rp1,
            })
            rp2 = lcs_n(str1, str2, str1_len, str2_len - 1, frame + 1)

            return max(rp1, rp2)

    def lcs_init(str1, str2) -> int:
        return lcs_n(str1, str2, len(str1), len(str2), 0)

    def lcs_dp(str1, str2):
        # TODO: spend more time understanding this!
        row_len = len(str1)
        col_len = len(str2)
        matrix = [[0] * col_len for _ in range(row_len)]

        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if str1[r - 1] == str2[c - 1]:
                    matrix[r][c] = 1 + matrix[r - 1][c - 1]
                else:
                    matrix[r][c] = max(matrix[r - 1][c], matrix[r][c - 1])

        return matrix[row_len - 1][col_len - 1]

    # print("lcs_init('AGGTAB', 'GXTXAYB') = ", lcs_init('AGGTAB', 'GXTXAYB'))
    print("lcs_dp('AGGTAB', 'GXTXAYB') = ", lcs_dp('AGGTAB', 'GXTXAYB'))
    print()
    print(subsequence)

# longest_common_subsequence_practice()

# end of file
