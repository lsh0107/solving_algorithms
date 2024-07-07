import sys

input = sys.stdin.readline
N = int(input())
coord = []
for i in range(N):
    coord.append(list(map(int, input().split())))
    
coord.sort(key=lambda x: (x[1], x[0]))

for c in coord:
    print(c[0], c[1])