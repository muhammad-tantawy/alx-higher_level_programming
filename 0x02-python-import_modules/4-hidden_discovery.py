#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    text = dir(hidden_4)
    for c in text:
        if not c.startswith( '__'):
            print("{}".format(c))
