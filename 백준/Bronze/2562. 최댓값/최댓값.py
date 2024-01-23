ans = []
for _ in range(9):
    N = int(input())
    ans.append(N)

MAX = max(ans)
print(MAX)
print(ans.index(MAX)+1)