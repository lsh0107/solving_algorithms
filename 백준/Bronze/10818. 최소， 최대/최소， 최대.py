N = int(input())
ans = []
num = input().split()
ans = [int(x) for x in num]
print(min(ans), max(ans))