#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers, -num)
    else:
        heapq.heappush(highers, num)


def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers, -heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers, -heapq.heappop(highers))


def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    # Write your code here
    lowers = []  # max heap, vals should go in and come out negated
    highers = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)
        result.append(round(getMedian(lowers, highers), 1))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
