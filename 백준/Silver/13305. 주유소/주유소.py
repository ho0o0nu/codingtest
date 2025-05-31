N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
min_price = price[0]
for length, price in list(zip(length, price)):
    min_price = min(price, min_price)
    total += length * min_price

print(total)