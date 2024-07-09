import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

As = {}
for i in A:
    if i not in As:
        As[i] = 1
    else:
        As[i] += 1

for i in M:
    try:
        if As[i] >= 1:
            print(1)
    
    except:
        print(0)