def solution(maps):
    from collections import deque
    answer = 0
    queue = deque([(0, 0, 1)])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while queue:
        x, y, answer = queue.popleft()
        
        if x == (len(maps) - 1) and y == (len(maps[0]) - 1):
            return answer
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            
            if (0 <= nx < len(maps) and 0 <= ny < len(maps[0])) and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, answer + 1))
        
    return -1