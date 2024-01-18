#!/usr/bin/python3
"""Create a function that prints a list of integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Create a functions that creates a list of integers."""
    try:
        count = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                count += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError:
        print("Type not an integer!")
    else:
        print("")
        return count
