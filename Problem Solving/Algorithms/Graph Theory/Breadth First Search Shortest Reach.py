#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n+1):
        graph[num] = set()
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)

    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}

    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for nbour in graph[curr_node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = curr_cost+6
                frontier.append((nbour, curr_cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
