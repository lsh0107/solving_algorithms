N = map(int, input().split())
answer = 0

for idx, _ in enumerate(N):
    if idx == 0:
        answer += _
    else:
        answer -= _

print(answer)