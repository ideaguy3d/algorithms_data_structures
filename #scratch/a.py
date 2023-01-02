from collections import deque
from datetime import datetime
import bisect

q = deque([(0, 0)])

df = {
    'us': {
        'old': 'data/castle'
    }
}


def openai1():
    '''
    https://beta.openai.com/docs/guides/fine-tuning/preparing-your-dataset

    {
                "prompt":
    "Samsung Galaxy Feel\n
    The Samsung Galaxy Feel is an Android smartphone developed by Samsung Electronics exclusively for the Japanese market.
    The phone was released in June 2017 and was sold by NTT Docomo. It runs on Android 7.0 (Nougat), has a 4.7 inch display,
    and a 3000 mAh battery.\nSoftware\nSamsung Galaxy Feel runs on Android 7.0 (Nougat), but can be later updated to Android 8.0 (Oreo).
    \nHardware\nSamsung Galaxy Feel has a 4.7 inch Super AMOLED HD display, 16 MP back facing and 5 MP front facing cameras. It has a 3000 mAh battery,
    a 1.6 GHz Octa-Core ARM Cortex-A53 CPU, and an ARM Mali-T830 MP1 700 MHz GPU. It comes with 32GB of internal storage,
    expandable to 256GB via microSD. Aside from its software and hardware specifications, Samsung also introduced a
    unique a hole in the phone's shell to accommodate the Japanese perceived penchant for personalizing their mobile phones.
    The Galaxy Feel's battery was also touted as a major selling point since the market favors handsets with longer battery life.
    The device is also waterproof and supports 1seg digital broadcasts using an antenna that is sold separately.\n\n###\n\n",

                "completion":
    "Looking for a smartphone that can do it all? Look no further than Samsung Galaxy Feel!
    With a slim and sleek design, our latest smartphone features high-quality picture and video capabilities,
    as well as an award winning battery life. END"}

    '''
    pass


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
