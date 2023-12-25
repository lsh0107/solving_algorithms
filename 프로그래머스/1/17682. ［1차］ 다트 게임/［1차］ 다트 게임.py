def solution(dartResult):
    answer = 0
    dartResult = [c for c in dartResult]
    char = ''
    stack = []

    while dartResult:
        if dartResult[0].isdigit():
            char = str(char)
            char += dartResult.pop(0)
        
        if dartResult and dartResult[0] in ['S', 'D', 'T']:
            char = int(char)
            if dartResult[0] == 'S':
                dartResult.pop(0)
                stack.append(char**1)
            
            elif dartResult[0] == 'D':
                dartResult.pop(0)
                stack.append(char**2)
            
            elif dartResult[0] == 'T':
                dartResult.pop(0)
                stack.append(char**3)
            char = ''
        
        if dartResult and dartResult[0] in ['*', '#']:
            if dartResult[0] == '*':
                if stack and len(stack) >= 2:
                    v2 = stack.pop()*2
                    v1 = stack.pop()*2
                    stack.append(v1)
                    stack.append(v2)
                    dartResult.pop(0)
                elif stack and len(stack) == 1:
                    stack.append(stack.pop()*2)
                    dartResult.pop(0)
                else:
                    stack.append(stack.pop()*2)
                    dartResult.pop(0)

            elif dartResult[0] == '#':
                stack.append(stack.pop()*(-1))
                dartResult.pop(0)

    answer = sum(stack)
    return answer