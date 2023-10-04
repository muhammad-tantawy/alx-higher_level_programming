#!/usr/bin/python3
def print_last_digit(number):
    last digit = (int(str(number)[-1]))
    if number > 0:
        print("{}".format(number))
    elif number < 0:
        print("{}".format(number * -1))
