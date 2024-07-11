import sys

input = sys.stdin.readline
m = int(input())
all_ = {i: 1 for i in range(1, 21)}
set_ = {i: 0 for i in range(1, 21)}
for _ in range(m):
    action = input().split()
    if action[0] == 'add':
        if set_[int(action[1])] == 0:
            set_[int(action[1])] = 1

    elif action[0] == 'remove':
        if set_[int(action[1])] == 1:
            set_[int(action[1])] = 0

    elif action[0] == 'check':
        if set_[int(action[1])] == 1:
            print(1)
        else:
            print(0)

    elif action[0] == 'toggle':
        if set_[int(action[1])] == 1:
            set_[int(action[1])] = 0
        else:
            set_[int(action[1])] = 1

    elif action[0] == 'all':
        set_ = all_.copy()
        
    elif action[0] == 'empty':
        set_ = {i: 0 for i in range(1, 21)}