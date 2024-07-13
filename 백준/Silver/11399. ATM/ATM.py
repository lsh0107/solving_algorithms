import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums_idx = []
for i, num in enumerate(nums):
    nums_idx.append([num, i])

nums_idx.sort(key=lambda x: x[0])
dp = [0]*n
dp[0] = nums_idx[0][0]
for i in range(1, n):
    dp[i] = dp[i-1] + nums_idx[i][0]

print(sum(dp))