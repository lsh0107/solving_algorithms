import sys
import math

input = sys.stdin.readline
N = int(input())
fact = str(math.factorial(N))
nums = list(fact)[::-1]

cnt = 0
for i in range(len(nums)):
    if int(nums[i]) == 0:
        cnt += 1
    else:
        print(cnt)
        break