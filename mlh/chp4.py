"""
reduction,
induction,
recursion,
"""

from random import randrange
import pprint

pretty = pprint.PrettyPrinter(indent=4).pprint


class Induction:
    def __init__(self):
        # self.quadratic()
        self.loglinear()

    @staticmethod
    def quadratic():  # {
        seq = [randrange(10 * 10) for _ in range(100)]
        xx, yy, dd = None, None, float('inf')
        for x in seq:
            for y in seq:
                if y == x: continue
                d = abs(x - y)
                if d < dd:
                    xx, yy, dd = x, y, d
        pretty(seq)
        print(str(xx), str(yy))
    # }

    @staticmethod
    def loglinear():
        seq, xx, yy = [randrange(10 * 10) for _ in range(100)], None, None
        seq.sort()
        dd = float('inf')
        for i in range(len(seq) - 1):
            x, y = seq[i], seq[i+1]
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d
        print(xx, yy)




Induction()

# end of file
