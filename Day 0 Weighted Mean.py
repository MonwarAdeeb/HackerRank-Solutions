# Enter your code here. Read input from STDIN. Print output to STDOUT
i = input()

values = []
weights = []

values = list(map(int,input().split()))
weights = list(map(int,input().split()))


s = 0
for x, y in zip(values, weights):
    s += x * y

weighted_avg = round(s / sum(weights), 1)

print(weighted_avg)
