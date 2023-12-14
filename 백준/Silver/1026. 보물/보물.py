n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


# 모든 경우의 수를 다 따져봐야 함.
# 하지만 한 배열은 오름차순, 한 배열은 내림차순 정렬을 하고 서로 곱하면 가장작게 됨
a = sorted(a)
b = sorted(b, reverse=True)

_sum = 0
for i in range(n):
    _sum += a[i] * b[i]

print(_sum)