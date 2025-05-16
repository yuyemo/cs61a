def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    while True:
        try:
            if n%2==0:
                n//=2
                yield n
            elif n!=1:
                n=n*3+1
                yield n
            else:
                yield 1
        except StopIteration:
             break