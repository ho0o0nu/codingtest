answer = list()
for i in range(int(input())):
    answer.append(input())
answer = list(set(answer))
answer = sorted(answer, key=lambda x: (len(x), x))
print(*answer, sep='\n')