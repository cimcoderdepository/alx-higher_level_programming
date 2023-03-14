def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Using str.format() to print integers
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                # print space between elements in a row
                print(" ", end="")
        # print a new line after printing each row
        print()
