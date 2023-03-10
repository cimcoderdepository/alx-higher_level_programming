#!/usr/bin/python3
import sys
if __name__ == "__main__":

# Get all the arguments except the first one (which is the script name)
    arguments = sys.argv[1:]

# Convert each argument to a float and sum them up
    result = sum(map(int, arguments))

# Print the result
    print(result)

