import sys
import math

input = sys.stdin.readline
N = int(input())
people = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0
p_cnt1, p_cnt2 = 0, 0
for i in range(len(people)):
    t_cnt += math.ceil(people[i]/t)

p_cnt1 = N//p
p_cnt2 = N%p

print(t_cnt)
print(p_cnt1, p_cnt2)