# Enter your code here. Read input from STDIN. Print output to STDOUT
x = input()
a = set(map(int, input().split()))
y = input()
b = set(map(int, input().split()))

print(len(a.intersection(b)))