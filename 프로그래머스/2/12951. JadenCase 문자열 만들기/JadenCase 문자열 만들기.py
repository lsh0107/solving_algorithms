def solution(s):
    answer = ''
    chars = [s for s in s.split(' ')]
    for i in range(len(chars)):
        if chars[i] and chars[i][0].isdigit():
            if i + 1 < len(chars):
                answer += chars[i].lower() + ' '
            else:
                answer += chars[i].lower()
        else:
            if chars[i]:
                if i + 1 < len(chars):
                    answer += chars[i][0].upper() + chars[i][1:].lower() + ' '
                
                else:
                    answer += chars[i][0].upper() + chars[i][1:].lower()
            
            else:
                if i + 1 == len(chars):
                    return answer
                else:
                    answer += ' '

    return answer