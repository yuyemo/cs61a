def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> store_digits(20105)
    Link(2, Link(0, Link(1, Link(0, Link(5)))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    class Link:
        def __init__(self, first, rest=None):
            self.first = first
            self.rest = rest

        def __repr__(self):
            if self.rest is None:
                return f'Link({self.first})'
            else:
                return f'Link({self.first}, {self.rest})'

    def store_digits(n):
        rest = None
        while n > 0:
            digit = n % 10
            rest = Link(digit, rest)
            n = n // 10
        return rest