#!/usr/bin/python3
def max_integer(my_list=[]):
    # if the list is empty, return None
    if not my_list:
        return None
    else:
        # set/assign first element (my_list[0]) in my_list as  max_num
        max_num = my_list[0]
        # iterate through the list
        for num in my_list:
            if num > max_num:
                max_num = num
    return max_num
