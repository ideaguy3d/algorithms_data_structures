import re


def practice1():
    s1 = 'foo123bar'
    r1 = re.search(r'[0-9]+', s1)
    print('found ', r1.group())
    s2 = 'per33cep'
    r2 = re.search(r'[0-9]+', s2)
    print('found ', r2.group())
    s3 = 'ab324, cccc23b and f44aaa'
    r3 = re.search(r'[0-9]+', s3)
    print('found ', r3.group())
    b1 = 1


practice1()


#
