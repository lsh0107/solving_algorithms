import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    floor = int(input())
    unit = int(input())
    mat = [[0 for _ in range(unit)] for _ in range(floor+1)]
    
    for i in range(0, len(mat[0])):
        mat[0][i] = i+1

    for i in range(1, len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = sum(mat[i-1][:j+1])
            
    print(mat[floor][unit-1])