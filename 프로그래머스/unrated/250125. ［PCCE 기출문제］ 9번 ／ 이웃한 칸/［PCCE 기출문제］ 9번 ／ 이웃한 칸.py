def solution(board, h, w):
    answer = 0
    dh, dw = [0 ,1 ,-1, 0], [1, 0, 0, -1]
    n = len(board)
    looking_for = board[h][w]

    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        
        if in_range(h_check, w_check, n):
            if board[h_check][w_check] == looking_for:
                answer += 1

    return answer

def in_range(dh, dw, n):
    if (dh >= 0 and dh < n) and (dw >= 0 and dw < n):
        return True
    return False