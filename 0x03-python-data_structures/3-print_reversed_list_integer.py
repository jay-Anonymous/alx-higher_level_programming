#!/usr/bin/python3

"""
Docstring goes here

"""


def print_reversed_list_integer(my_list=[]):
    my_list = my_list if my_list and type(my_list) is list else []
    if my_list is not None:
        my_list.reverse()
        for i in range(len(my_list)):
            print('{:d}'.format(my_list[i]))


if __name__ == '__main__':
    my_list = [i for i in range(6)]
    print_reversed_list_integer(my_list)
