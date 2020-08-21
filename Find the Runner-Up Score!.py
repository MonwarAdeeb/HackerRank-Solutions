#URL : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

newlist = []

for i in arr:
    if i not in newlist:

        newlist.append(i)

    newlist.sort(reverse=True)

print(newlist[1])
