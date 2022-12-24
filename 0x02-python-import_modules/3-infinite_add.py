#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    args_len = len(argv) - 1
    res = 0

    for item in range(1, args_len + 1):
        item_num = int(argv[item])

        res += item_num
    print(res)
