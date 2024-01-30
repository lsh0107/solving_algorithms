def solution(s):
    s = [char for char in s[::-1]]
    stack = []

    if not s:
        return 0
    
    while True:
        if not stack:
            stack.append(s.pop())
        
        if stack and s:
            if stack[-1] == s[-1]:
                stack.pop()
                s.pop()
                
            else:
                stack.append(s.pop())
        
        if not stack and not s:
            return 1
        
        if not s and stack:
            return 0