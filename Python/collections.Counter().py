from collections import Counter

number_of_shoes = int(input())
shoes = Counter(map(int, input().split()))
number_of_customers = int(input())
income = 0

for _ in range(number_of_customers):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)