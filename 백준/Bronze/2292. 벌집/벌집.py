import sys
N = int(input())

cnt = 1

i = 1
ans = 1
while ans < N:
    ans += i*6
    i += 1

print(i)