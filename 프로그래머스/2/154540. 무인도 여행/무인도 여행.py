from collections import deque

def solution(maps):
    def bfs(x, y):
        queue = deque([(x, y)])
        val = 0
        while queue:
            x, y = queue.popleft()
            if maps[x][y] != -1:  # 이미 방문한 곳은 무시
                val += maps[x][y]
                maps[x][y] = -1

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y

                    if (0 <= nx < len(maps) and 0 <= ny < len(maps[0])) and maps[nx][ny] != -1 and maps[nx][ny] != 'X':
                        queue.append((nx, ny))
        return val
    
    result = []
    maps = [[int(char) if char != 'X' else char for char in row] for row in maps]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                val = bfs(i, j)
                if val > 0:
                    result.append(val)
    
    return sorted(result) if result else [-1]