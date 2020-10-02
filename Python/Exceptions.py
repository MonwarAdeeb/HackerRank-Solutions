# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a,b=map(int, input().split())
        print(a//b) #For integer division in Python 3 use //
    except BaseException as e:
        print("Error Code:",e)