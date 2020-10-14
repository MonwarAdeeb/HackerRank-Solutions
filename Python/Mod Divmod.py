# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y = int(input()), int(input())
a,b = divmod(x,y)
print(a,b, (a,b), sep='\n')