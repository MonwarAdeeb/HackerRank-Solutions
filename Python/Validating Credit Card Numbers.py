# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

validity = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for _ in range(int(input().strip())):

    if validity.search(input().strip()):
        print("Valid")
    else:
        print("Invalid")
