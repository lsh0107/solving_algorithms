import sys

input = sys.stdin.readline
n = int(input())
stack = []
ans = []
nums = []
for _ in range(n):
    nums.append(int(input()))

idx, i = 0, 1
while idx < n:
    if i <= nums[idx]:
        stack.append(i)
        ans.append('+')
        i += 1
    
    elif stack[-1] == nums[idx]:
        stack.pop()
        ans.append('-')
        idx += 1
    
    else: break
    
if not stack:
    print('\n'.join(ans))
else:
    print('NO')