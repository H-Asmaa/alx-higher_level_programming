#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, cal.add(a, b)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, cal.sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, cal.mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, cal.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
