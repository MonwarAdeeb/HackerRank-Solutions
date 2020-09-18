# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = list(map(int, input().split()))

d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)

for i in range(m):
    print(' '.join(map(str,d[input()])) or -1)
