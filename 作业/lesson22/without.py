class Link:
        def __init__(self, first, rest=None):
            self.first = first
            self.rest = rest

        def __repr__(self):
            if self.rest is None:
                return f'Link({self.first})'
            else:
                return f'Link({self.first}, {self.rest})'
def without(s, i):
    """Return a new linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 0)
    Link(5, Link(7, Link(9)))
    >>> without(s, 2)
    Link(3, Link(5, Link(9)))
    >>> without(s, 4)           # There is no index 4, so all of s is retained.
    Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 4) is not s  # Make sure a copy is created
    True
    """
    t=s
    if i!=0:
        temp1=Link(s.first)
        i-=1
        t=t.rest
    else:
        temp1=Link(s.rest.first)
        t=t.rest.rest
        i-=1
    def add(t,i,temp):
        if t!=None:
            if i!=0:
                temp.rest=Link(t.first)
                t=t.rest
                return add(t,i-1,temp.rest)
            else:
                t=t.rest
                return add(t,i-1,temp)
        else:
            return temp1
    return add(t,i,temp1)