import sys

input = sys.stdin.readline
n, m = map(int, input().split())
listen = set()
see = set()
for i in range(n):
    input_ = input().rstrip()
    listen.add(input_)

for j in range(m):
    input_ = input().rstrip()
    see.add(input_)


l_s = list(listen & see)
l_s.sort()
print(len(l_s))
print('\n'.join(l_s))
