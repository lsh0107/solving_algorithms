import sys

input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    action = input().split()
    if action[0] == 'push':
        stack.append(int(action[1]))
    
    elif action[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif action[0] == 'size':
        print(len(stack))
    
    elif action[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    elif action[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)