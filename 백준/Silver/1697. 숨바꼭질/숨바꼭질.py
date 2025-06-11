from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0


def bfs(start: int, target: int) -> int:
	visited = [0] * 100001
	queue = deque([start])
	
	while queue:
		x = queue.popleft()
		
		if x == target:
			return visited[x]
		
		for next_pos in [x - 1, x + 1, 2 * x]:
			if 0 <= next_pos <= 100000 and not visited[next_pos]:
				visited[next_pos] = visited[x] + 1
				queue.append(next_pos)


print(bfs(N, K))
