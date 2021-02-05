# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, mod = map(int, input().split())

numbers = []
temp =[]

for _ in range(k):
    temp = map(int,input().split()[1:])
    numbers.append(map(lambda x:x**2%mod, temp))
    
print(max(map(lambda x: sum(x)%mod, product(*numbers))))