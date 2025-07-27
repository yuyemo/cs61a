class Link:
        def __init__(self, first, rest=None):
            self.first = first
            self.rest = rest

        def __repr__(self):
            if self.rest is None:
                return f'Link({self.first})'
            else:
                return f'Link({self.first}, {self.rest})'
def duplicate_link(s, val):
    """Mutates s so that each element equal to val is followed by another val.

    >>> x = Link(5, Link(4, Link(5)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(5, Link(5)))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, (Link(2, Link(3)))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    temp=s
    while temp!=None:
        if temp.first==val:
            t=Link(val)
            t.rest=temp.rest
            temp.rest=t
            temp=t.rest
        else:
            temp=temp.rest
            