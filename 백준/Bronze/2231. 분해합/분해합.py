import sys
input = sys.stdin.readline

N = int(input())
min_ = 1000001
for i in range(1, N+1):
    num = sum(map(int, str(i)))
    ans = num + i
    if ans == N:
        print(i)
        break
    if i == N:
        print(0)