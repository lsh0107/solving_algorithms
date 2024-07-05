import sys

input = sys.stdin.readline
N = int(input())

i = 665
cnt = 0
while True:
    i += 1
    if str(i).count('6') >= 3 and '666' in str(i):
        cnt += 1
    
    if cnt == N:
        print(i)
        break