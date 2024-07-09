import sys

input = sys.stdin.readline
n = int(input())
ns = map(int, input().split())
m = int(input())
ms = map(int, input().split())

dct = {}
for i in ns:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for j in ms:
    if j in dct:
        print(dct[j])
    else:
        print(0)
