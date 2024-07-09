import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = []
for i in range(1, n+1):
    nums.append(i)

dq = deque(nums)

while len(dq) > 1:
    dq.popleft()
    num = dq.popleft()
    dq.append(num)

print(dq.pop())