def solution(msg):
    answer = []
    dic = []
    for i in range(26):
        dic += chr(i + 65)
        
    m = ''
    for c in msg:
        m += c
        if m in dic:
            continue
        
        else:
            dic.append(m)
            answer.append(dic.index(m[:-1]) + 1)
            m = c
            
    answer.append(dic.index(m) + 1)
    return answer