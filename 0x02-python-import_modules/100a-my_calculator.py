#!/usr/bin/python3
from sys import all
if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: {} {} {} {}'.format(argv[0], argv[1], argv[2], argv[3]))
        exit 1
        if operator not '+' or operator not '-' or operator not '*' or\
                operator not '/':
            print(f'Unknown operator. Available operators: +, -, * and /')
            exit 1
        else:
            print(operator)
    print('{} {} {} = {}'.format(a, operator, b, all))
