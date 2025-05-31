N, K = map(int, input().split())
wallet = []
for _ in range(N):
    wallet.append(int(input()))

result = 0
for i in range(len(wallet) - 1, 0 - 1, -1):
    count = K // wallet[i]
    result += count
    K = K - wallet[i] * count
    if K == 0:
        break

print(result)