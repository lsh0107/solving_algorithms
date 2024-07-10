import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, pos = map(int, input().split())
    temp = list(map(int, input().split()))
    nums = deque()
    for i, num in enumerate(temp):
        nums.append([i, num])
    
    ans = max(nums, key=lambda x: x[1])[1]
    i = 0
    while True:
        if nums[0][1] == ans:
            i += 1
            if pos == nums[0][0]:
                print(i)
                break
            else:
                nums.popleft()
                ans = max(nums, key=lambda x: x[1])[1]

        else:
            nums.append(nums.popleft())
        