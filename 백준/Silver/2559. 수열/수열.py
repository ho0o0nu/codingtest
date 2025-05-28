N, K = map(int, input().split())
temps = list(map(int, input().split()))

l, r = 0, K - 1
total = sum(temps[:K])
max_temp = total

while r < N - 1:
	total -= temps[l]
	l += 1
	r += 1
	total += temps[r]
	max_temp = max(total, max_temp)
    
print(max_temp)