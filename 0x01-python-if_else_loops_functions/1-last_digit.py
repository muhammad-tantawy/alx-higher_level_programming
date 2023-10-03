#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = int(str(number)[-1]) * -1
else:
    last = int(str(number)[-1])
if last > 5:
    txt = 'and is greater than 5'
elif last == 0:
    txt = 'and is 0'
elif last < 6 and last != 0:
    txt = 'and is less than 6 and not 0'

print("Last digit of {} is {} {}".format(number, last, txt))
