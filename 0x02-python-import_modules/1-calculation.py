#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = c =  10
    b = d = 5
    print ("{} + {} = {}".format(c, d, calculator_1.add(a, b)))
    print ("{} - {} = {}".format(c, d, calculator_1.sub(a, b)))
    print ("{} * {} = {}".format(c, d, calculator_1.mul(a, b)))
    print ("{} / {} = {}".format(c, d, calculator_1.div(a, b)))
