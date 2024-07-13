import sys

input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for i in range(n):
    input_ = list(map(str, input().split()))
    d[input_[0]] = input_[1]

ans = []
for j in range(m):
    input_ = input().rstrip()
    ans.append(d[input_])

print('\n'.join(ans))