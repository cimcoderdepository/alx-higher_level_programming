#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # clone a shadow copy of my_list[:] into new_list
    new_list = my_list[:]
    if idx < 0:
        return my_list[:]       # return original copy my_list[:]

    if idx > len(my_list) - 1:
        return my_list[:]       # return original copy my_list[:]

    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element
        return (new_list)
