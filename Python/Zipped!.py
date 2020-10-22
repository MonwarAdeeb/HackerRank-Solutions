# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(int, input().split())

marks = []
for _ in range(b):
    marks.append(map(float, input().split()))

for i in zip(*marks):
    print(sum(i)/len(i))