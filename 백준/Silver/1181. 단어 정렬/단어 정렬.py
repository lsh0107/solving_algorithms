import sys

input = sys.stdin.readline
N = int(input())
ans = []

for _ in range(N):
    word = input().rstrip()
    ans.append(word)
ans = set(ans)
ans = sorted(ans, key=lambda x: (len(x), x))

for word in ans:
    if word == '':
        pass
    else:
        print(word)