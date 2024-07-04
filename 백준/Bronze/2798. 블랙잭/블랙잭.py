import sys
from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

condition = lambda comb: sum(comb) <= M
combi = [sum(comb) for comb in combinations(nums, 3) if condition(comb)]
print(max(combi))