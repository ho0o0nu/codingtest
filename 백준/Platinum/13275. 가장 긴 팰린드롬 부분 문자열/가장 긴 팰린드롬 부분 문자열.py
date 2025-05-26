s = input().strip()

# 문자열 전처리: 특수문자로 확장 (ex. "abba" → "#a#b#b#a#")
t = '#' + '#'.join(s) + '#'
n = len(t)
p = [0] * n  # 각 위치별로 대칭 길이 저장
c = 0  # 현재 중심(center)
r = 0  # 현재 우측 끝(right)

for i in range(n):
    mirror = 2 * c - i
    if i < r:
        p[i] = min(r - i, p[mirror])

    # 양쪽 끝이 같은 동안 확장
    while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
        p[i] += 1

    # 우측 경계 갱신
    if i + p[i] > r:
        c = i
        r = i + p[i]

print(max(p))