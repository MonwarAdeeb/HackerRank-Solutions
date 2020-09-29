# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))