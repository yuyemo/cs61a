class Link:
        def __init__(self, first, rest=None):
            self.first = first
            self.rest = rest

        def __repr__(self):
            if self.rest is None:
                return f'Link({self.first})'
            else:
                return f'Link({self.first}, {self.rest})'
def deep_map_mut(func, s):
    """Mutates a deep link s by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    
    if isinstance(s, Link):
        if isinstance(s.first, Link):
            deep_map_mut(func, s.first)
        else:
            s.first = func(s.first)
        if s.rest is not None:
            deep_map_mut(func, s.rest)