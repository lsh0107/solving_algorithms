import sys
import math

def realround(x):
    if x-math.floor(x)>=0.5:
        return math.floor(x)+1
    else:
        return math.floor(x)

input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
    sys.exit()

people = []
for _ in range(n):
    people.append(int(input()))

people.sort()
rmv = int(realround(len(people)*0.15))
for i in range(rmv):
    people[i] = 0

for j in range(1, rmv+1):
    people[-j] = 0

total_people = len(people) - rmv*2
total_score = sum(people)
ans = int(realround(total_score/total_people))
print(ans)