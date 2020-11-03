# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    number = input()
    if re.match(r"[789]{1}\d{9}$", number):
        print("YES")
    else:
        print("NO")