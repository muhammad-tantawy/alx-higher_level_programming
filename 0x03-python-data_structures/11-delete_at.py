#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    num = len(my_list) - 1
    if idx < 0:
        return (my_list)
    if idx > num:
        return(my_list)
    my_list = my_list[0:idx] + my_list[idx + 1:]
    return (my_list)
