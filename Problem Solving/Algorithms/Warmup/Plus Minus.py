n = int(input().strip())

temp = list(map(int, input().split()))
arr = []

for item in temp:
    if item == 0:
        arr.append(0)
    elif item > 0:
        arr.append(1)
    else:
        arr.append(-1)

print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
