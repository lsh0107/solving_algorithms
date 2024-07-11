import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic_name = {}
dic_num = {}
for i in range(1, n+1):
    input_ = input().rstrip()
    dic_name[input_] = i
    dic_num[i] = input_
for j in range(m):
    input_ = input().rstrip()
    if input_.isnumeric():
        print(dic_num[int(input_)])
    else:
        print(dic_name[input_])