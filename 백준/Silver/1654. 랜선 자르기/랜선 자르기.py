import sys

input = sys.stdin.readline
k, n = map(int, input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

nums.sort()
length = len(nums)

low = 1
high = max(nums)
ans = 0
while low <= high:
    cnt = 0
    mid = (high + low) // 2
    for i in range(length):
        cnt += (nums[i]//mid)
    
    if cnt < n:
        high = mid - 1

    elif cnt >= n:
        low = mid + 1
        ans = mid

print(ans)