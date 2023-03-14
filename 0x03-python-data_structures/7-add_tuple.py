#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b has less than 2 elements,
    # add 0s to make it a tuple of length 2
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Extract the first two elements of the tuples
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Add the first elements and second elements separately
    result = (a1 + b1, a2 + b2)

    return result
