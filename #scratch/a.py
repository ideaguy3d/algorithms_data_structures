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
        xf = open(country['old'], 'r')
        xf_info = xf.readlines()
        b18 = 1


def _date_practice(node=None):
    d1 = datetime.now()
    Q = deque([node])
    while Q:
        pass
    print(d1)


#_date_practice()
practice_open()





#
