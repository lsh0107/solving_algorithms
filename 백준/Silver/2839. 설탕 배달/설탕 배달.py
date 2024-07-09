import sys

input = sys.stdin.readline
n = int(input())
ans = 1000000000
five = 5
three = 3

for i in range(n // five + 1):
    remaining = n - five * i
    if remaining % three == 0:
        j = remaining // three
        ans = min(ans, i + j)

if ans == 1000000000:
    ans = -1

print(ans)