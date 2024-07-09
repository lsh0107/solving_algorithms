import sys

input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    ps = input().rstrip()
    stack = []
    flag = True
    for i in ps:
        if i == '(':
            stack.append(i)
        
        else:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                
                else:
                    flag = False
                    break
    
    if flag and not stack:
        print('YES')
    else:
        print('NO')