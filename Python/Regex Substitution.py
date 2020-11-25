# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    line = input()

    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")

    print(line)
