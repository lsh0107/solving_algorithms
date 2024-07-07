import sys

input = sys.stdin.readline
N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))


for x, y in people:
    cnt = 1
    for p, q in people:
        if x < p and y < q:
            cnt += 1
    print(cnt)