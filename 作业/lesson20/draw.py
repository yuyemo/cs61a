def draw(hand, positions):
    """Remove and return the items at positions from hand.
    Fill in each blank with one of these names: list, map, filter, reverse, reversed, sort, sorted, append, insert, index, remove, pop, zip, or sum. See the built-in functions and list methods documentation for descriptions of what these do.

    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))