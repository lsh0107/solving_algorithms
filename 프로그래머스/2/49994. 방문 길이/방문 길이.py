def solution(dirs):
    maps = [[False for _ in range(11)] for _ in range(11)]
    answer = 0
    dx, dy = 5, 5
    set_ = set()
    for dir in dirs:
        if dir == 'U':
            nx, ny = dx - 1, dy
        elif dir == 'D':
            nx, ny = dx + 1, dy
        elif dir == 'R':
            nx, ny = dx, dy + 1
        elif dir == 'L':
            nx, ny = dx, dy - 1

        if is_valid(nx, ny, 11):
            set_.add((nx, ny, dx, dy))
            set_.add((dx, dy, nx, ny))
            dx, dy = nx, ny
            
        else:
            nx, ny = dx, dy
            
    answer = len(set_)
    return answer//2

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n
