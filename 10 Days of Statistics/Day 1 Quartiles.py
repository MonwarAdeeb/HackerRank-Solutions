# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

n = int(input())

X = [int(x) for x in input().split()]
X.sort()

t = int(len(X)/2)

if len(X)%2 == 0:
    L = X[:t]
    U = X[t:]
else:
    L = X[:t]
    U = X[t+1:]
    
print(int(median(L)))
print(int(median(X)))
print(int(median(U)))
