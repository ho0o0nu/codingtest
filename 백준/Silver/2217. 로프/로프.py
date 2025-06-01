import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)
max_weight = 0
for i in range(1, len(ropes) + 1):
	max_weight = max(max_weight, min(ropes[i-1:i]) * i)
print(max_weight)