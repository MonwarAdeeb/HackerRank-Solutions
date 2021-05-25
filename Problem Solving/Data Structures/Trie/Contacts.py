from collections import *

cter = Counter()
for i in range(int(input().strip())):
    cmd, word = input().strip().split(' ')
    if cmd == 'add':
        for i in range(1, len(word) + 1):
            cter.update([word[0:i]])
    else:
        print(cter[word])
