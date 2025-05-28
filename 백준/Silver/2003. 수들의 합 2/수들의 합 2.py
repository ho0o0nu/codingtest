N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
total, answer = 0, 0

while True:
	if total >=  M:
		total -= nums[left]
		left += 1
	elif right == N:
		break
	else:
		total += nums[right]
		right += 1

	if total == M:
		answer += 1
		
print(answer)