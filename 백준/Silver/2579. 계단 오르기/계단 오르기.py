import sys

input = sys.stdin.readline
n = int(input())
steps = []
for _ in range(n):
    steps.append(int(input()))

dp = [0]*(n)
if n <= 2:
    print(sum(steps[:n]))
else:
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + steps[i] + steps[i-1], dp[i-2] + steps[i])

    print(dp[-1])