def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    i=0
    while i<k:
        n=n//10
        i+=1
    return n%10

n=int(input('n='))
k=int(input('k='))
f=digit(n,k)
print('number=',f)
