H, W = map(int, input().split())
height = list(map(int, input().split()))

left, right = 0, W - 1
max_left, max_right = height[left], height[right]

volume = 0

while left < right:
    max_left, max_right = max(height[left], max_left), \
                          max(height[right], max_right)
    if max_left <= max_right:
        volume += max_left - height[left]
        left += 1
    else:
        volume += max_right - height[right]
        right -= 1

print(volume)