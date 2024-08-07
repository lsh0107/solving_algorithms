import sys

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(1, m+1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def dfs(node, depth):
    if node == b:
        print(depth)
        return True
    
    visited[node] = True
    for next_ in g[node]:
        if not visited[next_]:
            if dfs(next_, depth + 1):
                return True
    return False

if not dfs(a, 0):
    print(-1)