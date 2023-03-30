def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while my_list[count] and count < x:
            print(my_list[count], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
