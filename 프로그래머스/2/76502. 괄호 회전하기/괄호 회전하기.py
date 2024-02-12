def solution(s):
    answer = 0
    stack = []
    cnt = len(s)
    count = 0
    check = 0

    while True:
        if len(s)%2 == 1:
            return 0
        
        for i in s:
            check += 1
            if i == '[' or i == '{' or i == '(':
                stack.append(i)

            else:
                if i == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()

                    else: break
                
                elif i == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()

                    else: break

                elif i == ')':    
                    if stack and stack[-1] == '(':
                        stack.pop()
                        
                    else: break
        if check == cnt and not stack:
            answer += 1
        
        check = 0
        s = s[1:] + s[0]
        count += 1

        if count == cnt:
            break

    return answer