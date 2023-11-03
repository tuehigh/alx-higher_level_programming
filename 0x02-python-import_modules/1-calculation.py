#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5

    result = calc.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
