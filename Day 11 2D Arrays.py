#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum_list = []

    for r in range(0, 4):
        for c in range(0, 4):
            s = sum(arr[r][c:c+3]) + arr[r+1][c+1] + sum(arr[r+2][c:c+3])
            sum_list.append(s)

    print(max(sum_list))
