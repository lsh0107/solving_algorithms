import sys

input = sys.stdin.readline

while True:
    stack = []
    msg = input().rstrip()
    if msg == '.': break

    flag = True
    for m in msg:
        if m == '(' or m == '[':
            stack.append(m)
        
        elif m == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                flag = False
                break
            
        elif m == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else: 
                flag = False
                break

    if flag and not stack:
        print('yes')
    else:
        print('no')