class Link:
        def __init__(self, first, rest=None):
            self.first = first
            self.rest = rest

        def __repr__(self):
            if self.rest is None:
                return f'Link({self.first})'
            else:
                return f'Link({self.first}, {self.rest})'
def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
    rest=None
    for val, count in zip(reversed(vals), reversed(counts)):
        for _ in range(count):
            rest = Link(val, rest)
    return rest
                   
                
