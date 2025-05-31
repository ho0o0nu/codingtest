N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

time = 0
count = 0
intervals = sorted(intervals, key=lambda x: (x[1], x[0]))

for start, end in intervals:
    if start >= time:
        time = end
        count += 1

print(count)