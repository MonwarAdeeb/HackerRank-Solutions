# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

odict = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(' ', 1)
    odict[item] = odict.get(item, 0) + int(price)

[print(item, odict[item]) for item in odict]