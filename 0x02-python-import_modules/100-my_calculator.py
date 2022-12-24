#!/usr/bin/python3
from sys import argv
from calculator_1 import *

if __name__ == "__main__":
    args_len = len(argv) - 1

    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        
    operand = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operand == "+":
        print("{:d} {} {:d} = {:d}".format(a, operand, b, add(a, b)))
    elif operand == "-":
        print("{:d} {} {:d} = {:d}".format(a, operand, b, sub(a, b)))
    elif operand == "*":
        print("{:d} {} {:d} = {:d}".format(a, operand, b, mul(a, b)))
    elif operand == "/":
        print("{:d} {} {:d} = {:d}".format(a, operand, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
