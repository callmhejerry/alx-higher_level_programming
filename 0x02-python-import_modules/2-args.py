#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_list = sys.argv
    args_len = len(args_list) - 1
    if args_len < 1:
        print("{:d} arguments:".format(args_len))
    else:
        if args_len == 1:
            print("{:d} argument:".format(args_len))
        else:
            print("{:d} arguments:".format(args_len))
        for count in range(1, args_len + 1):
            print("{:d}: {}".format(count, args_list[count]))
