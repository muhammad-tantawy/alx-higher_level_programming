#!/usr/bin/python3

# function returns true if the letter is lower case
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
