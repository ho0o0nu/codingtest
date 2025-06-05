import sys
input = sys.stdin.readline

N = int(input())
flowers = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

flowers.sort()
    
t = 301
end_date = 1130
idx = 0
count = 0

while t <= end_date:
    max_end = t
    while idx < N and flowers[idx][0] <= t:
        max_end = max(max_end, flowers[idx][1])
        idx += 1

    if max_end == t:
        print(0)
        exit()

    t = max_end
    count += 1

print(count)