n = int(input())
start = 1
end = 1
total = 1
count = 0

while start <= n:
    if total == n:
        count += 1
        end += 1
        total += end
    elif total < n:
        end += 1
        total += end
    else:
        total -= start
        start += 1

print(count)