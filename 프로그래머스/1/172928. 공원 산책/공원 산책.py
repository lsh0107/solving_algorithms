def solution(park, routes):
    # 공원 가로x세로 50x50
    # 명령 50
    # 장애물에 막히거나 공원 밖을 나가면 해당 명령은 취소 후 다음 명령 진행
    # 이동 명령은 동서남북 1~9 칸씩
    # 동서남북 순서
    start_x = None
    start_y = None
    for idx1, row in enumerate(park):
        if 'S' in row:
            start_y = idx1
            break

    if start_y is not None:
        for idx2, col in enumerate(park[start_y]):
            if 'S' == col:
                start_x = idx2
                break

    for cnt in routes:
        dir = cnt[0]
        move = int(cnt[-1])
        prev_x, prev_y = start_x, start_y
        for _ in range(move):
            if dir == 'E' and check(start_x + 1, start_y, len(park[0]), park):
                start_x += 1
                    
            elif dir == 'W' and check(start_x - 1, start_y, len(park[0]), park):
                start_x -= 1

            elif dir == 'S' and check(start_x, start_y + 1, len(park), park):
                start_y += 1

            elif dir == 'N' and check(start_x, start_y - 1, len(park), park):
                start_y -= 1

            else:            
                start_x, start_y = prev_x, prev_y
                break
            
    return [start_y, start_x]

def check(x, y, n, park):
    return 0 <= x and x < n and 0 <= y and y < n and park[y][x] != 'X'