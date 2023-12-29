def solution(babbling):
    answer = 0
    languages = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        s = ''
        stack = []
        for idx, char in enumerate(bab):
            s += char
            
            # if len(stack) != 0 and s == stack[-1]:
            #     answer -= 1
            real_s = s
            if s in languages:
                if stack and stack[-1] == s:
                    stack = []
                    break
                else:
                    stack.append(s)
                    s = ''

            if stack and len(s) >= 1 and (len(bab) - idx <= 1):
                stack = []
        if stack:
            answer += 1

    return answer
