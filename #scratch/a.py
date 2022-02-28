from collections import deque
from datetime import datetime
import bisect

q = deque([(0, 0)])

df = {
    'us': {
        'old': 'data/castle'
    }
}


def practice_open():
    for country in df:
        xf = open(df[country]['old'], 'r')
        xf_info = xf.readlines()
        b18 = 1


def _date_practice(node=None):
    d1 = datetime.now()
    Q = deque([node])
    while Q:
        pass
    print(d1)


def bit_practice():
    x = 2
    y = 14
    print(bin(x))
    print(bin(y))
    print(bin(x & y))
    z = x & y
    print(bin(x & y), z)


def p1():
    arr = [[0, 1], [0, 2], [0, 3], [1, 4]]
    for a, b in arr:
        print(a, b)


def single_line_lambda():
    _list = [1, 2, -5, 4]
    # wrap a lambda in () to make it a 1 liner
    x = [(lambda x: x % 2 == 1)(num) for num in _list]
    print(x)


def bisect_practice():
    pass

single_line_lambda()
# p1()
# bit_practice()
# _date_practice()
# practice_open()


#
