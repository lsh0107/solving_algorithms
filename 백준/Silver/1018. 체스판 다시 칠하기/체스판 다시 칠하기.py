import sys

input = sys.stdin.readline
n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(list(input().rstrip()))

white = ['WBWBWBWB', 'BWBWBWBW'] * 4
black = ['BWBWBWBW', 'WBWBWBWB'] * 4
ans = float('inf')
for i in range(n-7):
    for j in range(m-7):
        cnt_w, cnt_b = 0, 0
        for x in range(8):
            for y in range(8):
                if chess[x+i][y+j] != white[x][y]:
                    cnt_w += 1
                if chess[x+i][y+j] != black[x][y]:
                    cnt_b += 1

        ans = min(ans, cnt_w, cnt_b)

print(ans)