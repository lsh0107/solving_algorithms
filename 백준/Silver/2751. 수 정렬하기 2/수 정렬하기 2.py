import sys

input = sys.stdin.readline
N = int(input())
nums = [0]*2000001


for _ in range(N):
    num = int(input())
    if num >0:
        nums[num+1000000] = num
    elif num == 0:
        nums[num+1000000] = '0'
    else:
        nums[num-1000001] = num

for i in range(len(nums)):
    if nums[i] != 0 or nums[i] == '0':
        print(nums[i])