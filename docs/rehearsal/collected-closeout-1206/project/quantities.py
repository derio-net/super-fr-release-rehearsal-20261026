"""Strict aggregation of nonnegative integer quantities."""


def total_units(values):
    """Sum an iterable once, rejecting booleans, non-ints and negatives."""
    total = 0
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("quantities must be integers, not booleans")
        if value < 0:
            raise ValueError("quantities must be nonnegative")
        total += value
    return total
