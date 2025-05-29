N = int(input())
nums = list(map(int, input().split()))
nums.sort()

l, r = 0, N - 1
aprx = float('inf')

while l < r:
	total = nums[l] + nums[r]
	if abs(total) < aprx:
		aprx = abs(total)
		answer = (nums[l], nums[r])
	if total == 0:
		break
	elif total < 0:
		l += 1
	else:
		r -= 1
		
print(*answer)