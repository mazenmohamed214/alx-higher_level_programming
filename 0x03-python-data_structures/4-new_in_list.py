#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_cpy = [x for x in my_list]
    if 0 <= idx < len(my_list):
        list_cpy[idx] = element
        return list_cpy
    return my_list
