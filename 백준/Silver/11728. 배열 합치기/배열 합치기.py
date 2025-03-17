N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx_a, idx_b = 0, 0
ans = list()

while idx_a < N and idx_b < M:
    if A[idx_a] <= B[idx_b]:
        ans.append(A[idx_a])
        idx_a += 1
    else:
        ans.append(B[idx_b])
        idx_b += 1

if idx_a != N:
    for _ in range(N - idx_a):
        ans.append(A[idx_a])
        idx_a += 1
elif idx_b != M:
    for _ in range(M - idx_b):
        ans.append(B[idx_b])
        idx_b += 1

print(*ans)
