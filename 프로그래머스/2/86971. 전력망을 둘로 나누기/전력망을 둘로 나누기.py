def solution(n, wires):
    answer = 100000000
    graph = [[] for _ in range(n+1)]
    link = [[True] * (n+1) for _ in range(n+1)]
    
    def dfs(start, graph, visited, link):
        visited[start] = True
        cnt = 1

        for end in graph[start]:
            if not visited[end] and link[start][end]:
                cnt += dfs(end, graph, visited, link)

        return cnt
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n+1)
        link[a][b] = False
        cnt_a = dfs(a, graph, visited, link)
        cnt_b = dfs(b, graph, visited, link)
        link[a][b] = True
        
        answer = min(abs(cnt_a - cnt_b), answer)
        
    return answer
