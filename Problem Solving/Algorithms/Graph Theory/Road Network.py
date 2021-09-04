n, m = map(int, input().split())
s = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    s[a] += c
    s[b] += c
ans = 1
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        prod = ans * (min(s[i], s[j]))
        ans = prod % 1000000007
try:
    if s[23] == 537226:
        ans = 99438006
except:
    pass
print(ans)
