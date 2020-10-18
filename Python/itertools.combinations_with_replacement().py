# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, a = input().split()
for b in combinations_with_replacement(sorted(s), int(a)):
    print("".join(b))