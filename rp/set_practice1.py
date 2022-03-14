def unique1(s: str) -> int:
    """
    $ python3 -m doctest j_set.py
    Count number of uniqe characters in s
    >>> unique1("aabb")
    2
    >>> unique1("abcdef")
    6
    """
    # set comprehension
    return len({c for c in s})


def unique2(s: str) -> int:
    return len(set(s))

# end of file
