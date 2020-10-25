# Enter your code here. Read input from STDIN. Print output to STDOUT
_, n = input(), input().split()
print( all([int(i)>0 for i in n]) and any([j==j[::-1] for j in n]) )