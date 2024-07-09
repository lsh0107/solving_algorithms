import sys

input = sys.stdin.readline
n = int(input().rstrip())

stack = []
for _ in range(n):
    num = int(input().rstrip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))