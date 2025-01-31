def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
   
    n=max(a,b,c)
    m=min(a,b,c)
    if a==n:
        a=b
    if a==n:
        a=c
    if a==m:
        a=b
    if a==m:
        a=c
    return a
x,y,z=int(input('a=')),int(input('b=')),int(input('c='))
n=middle(x,y,z)
print(n)
