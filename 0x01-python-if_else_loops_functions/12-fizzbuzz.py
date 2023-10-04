#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            output = 'Fizz'
        elif i % 5 == 0:
            output = 'Buzz'
        elif i % 15 ==0:
            output = 'FizzBuzz'
        else:
            output = i
        
    print("{}".format(output))
