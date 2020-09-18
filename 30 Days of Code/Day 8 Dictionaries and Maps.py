# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
phoneBook = {}
info = []

for _ in range(N):
    info = list(map(str, (input().split())))
    phoneBook[info[0]] = info[1]
    info.clear()

while True:
    try:
        name = str(input())
        if name in phoneBook.keys():
            number = phoneBook[name]
            print("{}={}".format(name,number))
        else:
            print("Not found")
    except:
        break
        
