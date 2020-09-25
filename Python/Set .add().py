# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

names = set()

for _ in range(int(n)):
    names.add(input())

print(len(names))