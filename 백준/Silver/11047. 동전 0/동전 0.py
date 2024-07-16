import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    input_ = int(input())
    coins.append(input_)

cnt = 0
while k != 0:
    if coins[-1] > k:
        coins.pop()
    
    else:
        cnt = cnt + (k//coins[-1])
        k = k % coins[-1]
        
print(cnt)