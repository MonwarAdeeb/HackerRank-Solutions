# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    string = input()
    print(string[0::2], string[1::2])
