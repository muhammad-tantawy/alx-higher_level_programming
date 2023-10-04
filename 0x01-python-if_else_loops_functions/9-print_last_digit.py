#!/usr/bin/python3
def print_last_digit(number):
    last = (int(str(number)[-1]))
    if number > 0:
        print("{}".format(last))
    elif number < 0:
        print("{}".format(last * -1))
