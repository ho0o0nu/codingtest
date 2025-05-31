N = int(input())
line = sorted(list(map(int, input().split())))
answer = 0

for i, v in enumerate(line):
	answer += v * (len(line) - i)

print(answer)