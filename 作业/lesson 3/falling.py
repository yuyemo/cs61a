def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    i=0
    f=1
    while i<k:
        f=f*n
        n-=1
        i+=1
    return f
x,y=int(input('n=')),int(input('k='))
print('falling=',falling(x,y))