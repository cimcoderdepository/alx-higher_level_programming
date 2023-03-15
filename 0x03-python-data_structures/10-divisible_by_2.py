#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a new list with True or False, depending on whether the integer at
    the same position in the original list is a multiple of 2
    """
    result = []
    for item in my_list:
        result.append(item % 2 == 0)
    return result
