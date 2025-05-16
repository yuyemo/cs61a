def merge(a, b):
    """
    Return a generator that has all of the elements of generators a and b,
    in increasing order, without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_val, b_val = next(a), next(b)
    while True:
        if a_val == b_val:
            i=a_val
            a_val=next(a)
            b_val=next(b)
            yield i
        elif a_val < b_val:
            i=a_val
            a_val=next(a)
            yield i
        else:
            i=b_val
            b_val=next(b)
            yield i
def sequence(start, step):
    while True:
        yield start
        start += step
a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
[next(result) for _ in range(10)]