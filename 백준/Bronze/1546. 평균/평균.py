import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

max_ = max(nums)

new_nums = [num/max_ * 100 for num in nums]

print(sum(new_nums)/N)