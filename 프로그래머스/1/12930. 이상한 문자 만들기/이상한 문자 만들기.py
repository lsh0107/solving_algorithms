def solution(s):
    answer = ''
    string = s.split(' ')
    for char in string:
        for idx, c in enumerate(char):
            if idx % 2 == 0:
                answer += c.upper()
                
            else:
                answer += c.lower()
            
        answer += ' '
    return answer[:-1]