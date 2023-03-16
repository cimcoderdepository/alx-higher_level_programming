#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value in a_dictionary.items():
        if not value:
            return a_dictionary
#        return a_dictionary.pop('key')
