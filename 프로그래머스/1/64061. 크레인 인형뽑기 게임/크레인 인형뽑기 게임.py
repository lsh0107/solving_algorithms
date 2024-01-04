def solution(board, moves):
    answer = 0
    bucket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] == 0:
                pass
            elif board[i][move-1] != 0:
                if bucket and bucket[-1] == board[i][move-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    
    return answer