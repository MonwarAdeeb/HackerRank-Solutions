#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(p):
    fuel = 0
    ll = len(p)
    l = 0
    i = l
    while i < ll:
        fuel = fuel+p[i][0]-p[i][1]
        if fuel < 0:
            l = l+1
            i = l
            fuel = 0
        else:
            i += 1
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
