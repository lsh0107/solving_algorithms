import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(node):
    global count
    visited[node] = True
    count += 1

    for next_ in graph[node]:
        if visited[next_] == False:
            dfs(next_)

dfs(1)
print(count-1)