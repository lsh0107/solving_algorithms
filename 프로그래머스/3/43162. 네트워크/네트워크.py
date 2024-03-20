def solution(n, computers):
    answer = 0
    
    def dfs(idx, computers, visited):
        visited[idx] = True
        for next_ in range(len(computers[idx])):
            if computers[idx][next_] == 1 and not visited[next_]:
                dfs(next_, computers, visited)

    visited = [False] * (n)
    
    for idx in range(n):
        if not visited[idx]:
            dfs(idx, computers, visited)
            answer += 1
        
    return answer