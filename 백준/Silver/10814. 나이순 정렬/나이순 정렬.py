import sys

input = sys.stdin.readline
N = int(input())
people = []
for i in range(N):
    man = list(map(str, input().split()))
    man[0] = int(man[0])
    man.append(i+1)
    people.append(man)

people.sort(key=lambda x: (x[0], x[2]))

for person in people:
    print(person[0], person[1])