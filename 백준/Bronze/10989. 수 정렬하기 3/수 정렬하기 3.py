import sys

input = sys.stdin.readline
N = int(input())
nums = [0] * 10001

for _ in range(N):
    num = int(input())
    if nums[num] == 0:
        nums[num] = 1
    else:
        nums[num] += 1

for i in range(1, len(nums)):
    if nums[i] == 0:
        pass
    else:
        for _ in range(nums[i]):
            print(i)