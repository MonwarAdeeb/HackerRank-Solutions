# Enter your code here. Read input from STDIN. Print output to STDOUT

(_, A) = (int(input()), set(map(int, input().split())))
B = int(input())
for _ in range(B):
    (command, newset) = input().split()[0], set(map(int, input().split()))
    getattr(A, command)(newset)

print(sum(A))