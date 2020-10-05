# Enter your code here. Read input from STDIN. Print output to STDOUT
c,a = int(input()), input().split()
d,b = int(input()), input().split()

x=set(a)
y=set(b)

m=x.difference(y)
n=y.difference(x)

o=m.union(n)

print('\n'.join(sorted(o, key=int)))