ans = 1
for _ in range(3):
    N = int(input())
    ans *= N

ans = str(ans)
print(str(ans).count('0'))
for i in range(1, 10):
    print(ans.count(str(i)))
