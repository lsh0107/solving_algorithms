import sys

input = sys.stdin.readline
n, k = map(int, input().split())

nums = []
for i in range(n):
    nums.append(i+1)

pos = 0
i = 0
size = n
ans = []
while i < n:
    pos = (pos + k-1) % size
    ans.append(nums.pop(pos))
    size = len(nums)
    i += 1

print("<" + ", ".join(map(str, ans)) + ">")