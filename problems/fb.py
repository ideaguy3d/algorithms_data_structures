
test2 = 'ABA'
test1 = 'BBBAB'
RESULT = ''
start_length = None


def switch_letter(n, c):
    global RESULT, start_length
    if not start_length:
        start_length = n - 1
    n = n - 1
    if n > -1:
        RESULT += 'A' if c[start_length - n] == 'B' else 'B'


def get_wrong_answers(n: int, c: str) -> str:
    switch_letter(n, c)
    if n < 0:
        return RESULT
    return get_wrong_answers(n-1, c)


get_wrong_answers(len(test1), test1)

b22 = 1



#
