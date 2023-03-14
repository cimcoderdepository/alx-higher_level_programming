#!/usr/bin/python3
def no_c(my_string):
    # Create an empty string to hold the result
    result = ""

    # Iterate through each character in the input string
    for char in my_string:
        # If the current character is not 'c' or 'C', add
        # (concatenate) it to the result string
        if char != 'c' and char != 'C':
            result += char

    # Return the final result string
    return result
